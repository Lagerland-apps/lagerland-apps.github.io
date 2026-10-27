#!/usr/bin/env python3
"""Translation tooling for the multilingual site (TRANSLATION.md 4.13). Run from the repo root.

  python3 scripts/i18n.py map               # write _data/i18n_map.json from every translated page's ref
  python3 scripts/i18n.py stale             # translations whose English page changed after translated_from
  python3 scripts/i18n.py check             # source + built-site checks; exit 1 on any error
  python3 scripts/i18n.py check --site DIR  # built-site checks against another build dir (default: _site)
  add --root DIR to run against a copy of the repo (default: the current directory)

What `check` fails on (data contract: the "Phase 0 data contract", mirrored in TRANSLATION.md 4.1, 4.13, 6.2):
  - a fact field (name, price, screenshots, ...) in a translation file, or a fact sub-key inside a text structure
  - a text field the English master has that the translation lacks (app, support, privacy and other pages);
    plans, release_notes and screenshot_captions must have the master's length and item keys
  - _data/i18n/<code>.yml keys that differ from en.yml (recursive, list lengths) or whose {placeholders} differ
  - a ref that points nowhere (or at a redirect), a missing or wrong permalink, two pages translating one ref
  - _data/i18n_map.json not what `map` would write now
  - in the BUILT site: a translated page linking to an English URL that has a version in its language, and
    leftover English interface strings (en.yml values of 12+ characters found verbatim in visible text)
It warns, per language, about apps whose translated page still shows the English screenshots and about
incomplete localized screenshot sets (assets/screenshots/<slug>/<code>/).

Needs PyYAML for front matter and the i18n files (generate-og.py and generate-qr.py use it too).
"""
import argparse, collections, datetime, html, json, os, re, subprocess, sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("scripts/i18n.py needs PyYAML (python3 -m pip install pyyaml).")

SITE = "https://lagerland-apps.github.io"
LANGS = ("de", "fr", "it", "es", "pt", "zh", "ja", "ko", "id", "es-mx", "pt-br", "pl", "tr", "nl", "ru", "ar")
LANG_RE = re.compile(r"^(%s)/" % "|".join(re.escape(c) for c in sorted(LANGS, key=len, reverse=True)))

# --- the data contract's field lists -------------------------------------------------------------
APP_FACT_KEYS = ("name", "category", "status", "app_store_url", "price", "schema_price", "schema_high_price",
                 "schema_offer_count", "icon", "og_image", "screenshots", "release", "ratings", "alternatives_to",
                 "related_apps", "support", "show_body", "jump_nav", "free_tier", "redirect_from", "plans_kind")
APP_FACT_SUBKEYS = {"hero": ("device", "video", "video_poster"),
                    "privacy": ("tracking", "account_required", "policy_url"),
                    "founder": ("entity_type", "support_email", "photo"),
                    "related_journal": ("slug",)}
PLAN_FACT_KEYS = ("kind", "highlight")
# `price` is the plan card's display string: tokens plus words ("{P_LIFETIME} once"), so it is translated.
PLAN_TEXT_KEYS = ("name", "price", "summary", "features", "highlight_label")
# A currency sign or code left in a price string once its {TOKENS} are removed means a hand-typed price.
TYPED_PRICE_RE = re.compile(r"[$€£¥₩₺₽₹]|R\$|\bzł\b|\b(?:USD|EUR|GBP|JPY|KRW|CNY|IDR|MXN|BRL|PLN|TRY|RUB|SAR)\b|ر\.س")
APP_TEXT_KEYS = ("tagline", "quick_answer", "who_for", "who_not_for", "value_points", "features", "how_it_works",
                 "faq", "plans_footnote", "pricing_note", "price_lead", "price_tier", "price_override",
                 "about_heading", "comparison_table", "example_insights", "plateau_disclosure",
                 "training_vocabulary", "spotlight", "value_math", "coach_cta")
HERO_TEXT_KEYS = ("headline", "subheadline", "alt", "secondary", "pre_headline", "cta_label", "cta_subline")
PRIVACY_TEXT_KEYS = ("data_collection", "notes", "app_privacy_label")
SEO_KEYS = ("title", "description", "keywords")
SUPPORT_FORBIDDEN = ("name", "support")
PRIVACY_PROSE = ("overview", "data_collection", "data_storage", "icloud_sync", "third_parties", "your_choices",
                 "your_rights", "sensitive_data", "children", "changes")
PRIVACY_FORBIDDEN = ("app_name", "contact_email", "back_url")
PLACEHOLDER_RE = re.compile(r"\{[a-z_][a-z0-9_]*\}")
MIN_LEFTOVER_LEN = 12


# --- reading the source tree ---------------------------------------------------------------------
def split_fm(text):
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---[ \t]*\r?\n(.*?\r?\n)?---[ \t]*(\r?\n|$)", text, re.S)
    if not m:
        return None, text
    try:
        fm = yaml.safe_load(m.group(1) or "") or {}
    except yaml.YAMLError as e:
        return {"__yaml_error__": str(e).splitlines()[0]}, text[m.end():]
    return (fm if isinstance(fm, dict) else {}), text[m.end():]


def dstr(v):
    """Front-matter dates come back from YAML as date objects; compare them as ISO strings."""
    if isinstance(v, (datetime.date, datetime.datetime)):
        return v.isoformat()[:10]
    return str(v).strip()[:10] if v is not None else None


class Repo:
    def __init__(self, root):
        self.root = os.path.abspath(root)
        cfg = self.yaml("_config.yml") or {}
        self.exclude = set(cfg.get("exclude") or [])
        self.include = set(cfg.get("include") or [])
        self.locales = self.yaml("_data/locales.yml") or {}
        self.pages = []          # dicts: path, url, lang, fm, body, kind (page|apps|journal)
        self.redirects = set()   # URLs that are redirect_from stubs
        self._scan()

    def p(self, *parts):
        return os.path.join(self.root, *parts)

    def yaml(self, rel):
        fp = self.p(rel)
        if not os.path.isfile(fp):
            return None
        with open(fp, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _skip_dir(self, rel):
        top = rel.split("/")[0]
        if rel in ("_site", "scripts", ".git", "node_modules", "assets") or top in ("_site", ".git", "assets"):
            return True
        if rel in self.exclude or top in self.exclude:
            return True
        name = rel.split("/")[-1]
        if name.startswith(".") and rel not in self.include:
            return True
        if name.startswith("_") and rel not in ("_apps", "_journal"):
            return True
        return False

    def _scan(self):
        for dp, dns, fns in os.walk(self.root):
            rel_dir = os.path.relpath(dp, self.root).replace(os.sep, "/")
            rel_dir = "" if rel_dir == "." else rel_dir
            dns[:] = sorted(d for d in dns if not self._skip_dir((rel_dir + "/" + d).lstrip("/")))
            for fn in sorted(fns):
                if not fn.endswith((".html", ".md")) or fn.startswith((".", "_")):
                    continue
                rel = (rel_dir + "/" + fn).lstrip("/")
                if rel in self.exclude:
                    continue
                with open(self.p(rel), encoding="utf-8", errors="replace") as f:
                    text = f.read()
                fm, body = split_fm(text)
                if fm is None:
                    continue  # static file, not a page
                kind = "apps" if rel.startswith("_apps/") else "journal" if rel.startswith("_journal/") else "page"
                m = LANG_RE.match(rel)
                lang = fm.get("lang") or (m.group(1) if m else "en")
                url = self.url_of(rel, fm, kind)
                pg = {"path": rel, "url": url, "lang": str(lang), "fm": fm, "body": body, "kind": kind,
                      "folder_lang": m.group(1) if m else "en"}
                self.pages.append(pg)
                rf = fm.get("redirect_from") or []
                for r in ([rf] if isinstance(rf, str) else rf):
                    self.redirects.add(str(r))

    @staticmethod
    def url_of(rel, fm, kind):
        pl = fm.get("permalink")
        if pl:
            return str(pl)
        stem = os.path.splitext(os.path.basename(rel))[0]
        if kind == "apps":
            return "/apps/%s/" % (fm.get("slug") or stem)
        if kind == "journal":
            return "/journal/%s/" % (fm.get("slug") or stem)
        if rel == "index.html" or rel == "index.md":
            return "/"
        if os.path.basename(rel) in ("index.html", "index.md"):
            return "/" + os.path.dirname(rel) + "/"
        return "/" + os.path.splitext(rel)[0] + ".html"

    # derived views
    def english(self):
        return {pg["url"]: pg for pg in self.pages if pg["lang"] == "en"}

    def translations(self):
        return [pg for pg in self.pages if pg["lang"] != "en"]

    def locale(self, code):
        return (self.locales or {}).get(code) or {}

    def live(self, code):
        return self.locale(code).get("live") is True

    def build_map(self):
        out = collections.defaultdict(dict)
        for pg in self.translations():
            ref = pg["fm"].get("ref")
            if not ref or pg["fm"].get("local_only"):
                continue
            ref = str(ref)
            out[ref]["en"] = ref
            out[ref][pg["lang"]] = pg["url"]
        return {k: dict(sorted(v.items())) for k, v in sorted(out.items())}

    def map_text(self):
        return json.dumps(self.build_map(), indent=2, sort_keys=True, ensure_ascii=False) + "\n"

    def app_master(self, slug):
        return next((pg for pg in self.pages if pg["kind"] == "apps" and
                     (pg["fm"].get("slug") or os.path.splitext(os.path.basename(pg["path"]))[0]) == slug), None)


# --- map -----------------------------------------------------------------------------------------
def cmd_map(repo, args):
    text = repo.map_text()
    fp = repo.p("_data", "i18n_map.json")
    old = open(fp, encoding="utf-8").read() if os.path.isfile(fp) else None
    if old == text:
        print("_data/i18n_map.json is up to date (%d English URLs with translations)." % len(repo.build_map()))
        return 0
    with open(fp, "w", encoding="utf-8") as f:
        f.write(text)
    print("Wrote _data/i18n_map.json (%d English URLs with translations)." % len(repo.build_map()))
    return 0


# --- stale ---------------------------------------------------------------------------------------
def git(repo, *a):
    try:
        return subprocess.run(["git", "-C", repo.root, *a], capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, OSError):
        return None


def english_date(pg):
    fm = pg["fm"]
    return dstr(fm.get("last_updated") or fm.get("date"))


def cmd_stale(repo, args):
    en = repo.english()
    by_lang = collections.defaultdict(list)
    missing = []
    for pg in repo.translations():
        ref = pg["fm"].get("ref")
        if not ref or pg["fm"].get("local_only"):
            continue
        src = en.get(str(ref))
        tf = dstr(pg["fm"].get("translated_from"))
        if src is None or not tf:
            missing.append((pg, "no English page" if src is None else "no translated_from"))
            continue
        ed = english_date(src)
        if ed and ed > tf:
            by_lang[pg["lang"]].append((pg, src, tf, ed))
    has_git = git(repo, "rev-parse", "--git-dir") is not None
    n = 0
    for code in sorted(by_lang):
        items = sorted(by_lang[code], key=lambda x: x[0]["url"])
        print("\n== %s (%d stale)%s" % (code, len(items), "" if repo.live(code) else "  [not live]"))
        for pg, src, tf, ed in items:
            n += 1
            print("  %s  translated_from %s, English %s updated %s" % (pg["path"], tf, src["path"], ed))
            if not has_git:
                print("     (no git repository here: diff unavailable)")
                continue
            rev = (git(repo, "rev-list", "-1", "--before=%s 23:59:59" % tf, "HEAD", "--", src["path"]) or "").strip()
            if not rev:
                print("     (no commit of %s on or before %s)" % (src["path"], tf))
                continue
            cmd = ["diff", rev[:10], "--", src["path"]]
            stat = (git(repo, "diff", "--stat", rev, "--", src["path"]) or "").rstrip()
            diff = git(repo, *cmd) or ""
            print("     since %s:  git %s" % (rev[:10], " ".join(cmd)))
            if stat:
                print("     " + stat.replace("\n", "\n     "))
            if diff and diff.count("\n") <= args.max_diff_lines:
                print("     " + diff.rstrip().replace("\n", "\n     "))
            elif diff:
                print("     (diff has %d lines; run the command above to read it)" % diff.count("\n"))
            else:
                print("     (no textual change since then: only last_updated moved, or the edit is uncommitted)")
    for pg, why in missing:
        print("  ? %s: %s (run check)" % (pg["path"], why))
    print("\n%d stale translation(s) in %d language(s)." % (n, len(by_lang)))
    return 0


# --- check ---------------------------------------------------------------------------------------
class Findings:
    def __init__(self):
        self.items = collections.defaultdict(list)

    def err(self, kind, where, msg=""):
        self.items[("ERROR", kind)].append((where, msg))

    def warn(self, kind, where, msg=""):
        self.items[("WARN", kind)].append((where, msg))

    def count(self, lvl):
        return sum(len(v) for (l, _), v in self.items.items() if l == lvl)

    def report(self, verbose):
        for (lvl, kind), items in sorted(self.items.items(), key=lambda kv: (kv[0][0] != "ERROR", kv[0][1])):
            print("\n%s  %s (%d)" % (lvl, kind, len(items)))
            lim = None if (verbose or lvl == "ERROR") else 12
            for w, m in items[:lim]:
                print("   %s  %s" % (w, m))
            if lim and len(items) > lim:
                print("   ... %d more (-v to list all)" % (len(items) - lim))


def nonempty(v):
    if v is None:
        return False
    if isinstance(v, str):
        return v.strip() != ""
    if isinstance(v, (list, dict)):
        return len(v) > 0
    return True


def check_i18n_files(repo, F):
    d = repo.p("_data", "i18n")
    files = sorted(fn for fn in os.listdir(d) if fn.endswith(".yml")) if os.path.isdir(d) else []
    if not files:
        return {}, {}
    data = {}
    for fn in files:
        try:
            data[fn[:-4]] = yaml.safe_load(open(os.path.join(d, fn), encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            F.err("i18n file does not parse", "_data/i18n/" + fn, str(e).splitlines()[0])
    en = data.get("en")
    if en is None:
        F.err("_data/i18n/en.yml missing (it is the master key set)", "_data/i18n/")
        return data, {}
    for code in sorted(data):
        if code == "en":
            continue
        where = "_data/i18n/%s.yml" % code
        if code not in LANGS:
            F.err("i18n file for an unknown language code", where)

        def walk(a, b, path):
            if isinstance(a, dict):
                if not isinstance(b, dict):
                    F.err("i18n value has the wrong type (en has a map)", where, path or "(root)")
                    return
                for k in a:
                    if k not in b:
                        F.err("i18n key missing", where, (path + "." if path else "") + str(k))
                    else:
                        walk(a[k], b[k], (path + "." if path else "") + str(k))
                for k in b:
                    if k not in a:
                        F.err("i18n key not in en.yml (extra)", where, (path + "." if path else "") + str(k))
            elif isinstance(a, list):
                if not isinstance(b, list):
                    F.err("i18n value has the wrong type (en has a list)", where, path)
                elif len(a) != len(b):
                    F.err("i18n list length differs from en.yml", where, "%s: en %d, %s %d" % (path, len(a), code, len(b)))
                else:
                    for i, (x, y) in enumerate(zip(a, b)):
                        walk(x, y, "%s[%d]" % (path, i))
            elif isinstance(a, str):
                if b is None or (isinstance(b, str) and not b.strip() and a.strip()):
                    F.err("i18n value empty", where, path)
                elif not isinstance(b, str):
                    F.err("i18n value has the wrong type (en has a string)", where, path)
                elif sorted(PLACEHOLDER_RE.findall(a)) != sorted(PLACEHOLDER_RE.findall(b)):
                    F.err("i18n placeholders differ from en.yml", where,
                          "%s: en %s, %s %s" % (path, sorted(set(PLACEHOLDER_RE.findall(a))), code,
                                                sorted(set(PLACEHOLDER_RE.findall(b)))))
        walk(en, data[code], "")
    return data, en


def check_app(repo, pg, F):
    fm, where = pg["fm"], pg["path"]
    slug = fm.get("slug")
    master = repo.app_master(slug) if slug else None
    if not slug:
        F.err("translated app page has no slug", where)
    elif master is None:
        F.err("translated app page slug has no _apps/<slug>.md master", where, str(slug))
    ref = fm.get("ref")
    if master and ref and str(ref) != master["url"]:
        F.err("app page ref does not match its slug's master URL", where, "ref %s, master %s" % (ref, master["url"]))
    for k in APP_FACT_KEYS:
        if k in fm:
            F.err("fact field in a translation file", where, k)
    for k, subs in APP_FACT_SUBKEYS.items():
        v = fm.get(k)
        if isinstance(v, dict):
            for s in subs:
                if s in v:
                    F.err("fact field in a translation file", where, "%s.%s" % (k, s))
    if isinstance(fm.get("related_journal"), dict):
        for s in fm["related_journal"]:
            if s != "anchor":
                F.err("related_journal may only carry anchor", where, s)
    if master is None:
        return
    m = master["fm"]
    for k in APP_TEXT_KEYS:
        if nonempty(m.get(k)) and not nonempty(fm.get(k)):
            F.err("text field the English master has is missing", where, k)
    for parent, subs in (("seo", SEO_KEYS), ("hero", HERO_TEXT_KEYS), ("privacy", PRIVACY_TEXT_KEYS)):
        mv = m.get(parent)
        if not isinstance(mv, dict):
            continue
        tv = fm.get(parent) if isinstance(fm.get(parent), dict) else {}
        for s in subs:
            if nonempty(mv.get(s)) and not nonempty(tv.get(s)):
                F.err("text field the English master has is missing", where, "%s.%s" % (parent, s))
    if isinstance(m.get("founder"), dict):
        tv = fm.get("founder") if isinstance(fm.get("founder"), dict) else {}
        for s, v in m["founder"].items():
            if s not in APP_FACT_SUBKEYS["founder"] and nonempty(v) and not nonempty(tv.get(s)):
                F.err("text field the English master has is missing", where, "founder.%s" % s)
    rj = m.get("related_journal")
    if isinstance(rj, dict) and nonempty(rj.get("anchor")):
        tv = fm.get("related_journal")
        if not (isinstance(tv, dict) and nonempty(tv.get("anchor"))):
            F.err("text field the English master has is missing", where, "related_journal.anchor")
    # per-item lists: same length and order as the master, text keys only
    mp, tp = m.get("plans"), fm.get("plans")
    if isinstance(mp, list) and mp:
        if not isinstance(tp, list):
            F.err("text field the English master has is missing", where, "plans")
        elif len(tp) != len(mp):
            F.err("plans length differs from the master", where, "master %d, translation %d" % (len(mp), len(tp)))
        else:
            for i, (a, b) in enumerate(zip(mp, tp)):
                b = b if isinstance(b, dict) else {}
                for s in b:
                    if s in PLAN_FACT_KEYS:
                        F.err("fact field in a translation file", where, "plans[%d].%s" % (i, s))
                    elif s not in PLAN_TEXT_KEYS:
                        F.err("unknown key in translated plans item", where, "plans[%d].%s" % (i, s))
                for s in PLAN_TEXT_KEYS:
                    if nonempty((a or {}).get(s)) and not nonempty(b.get(s)):
                        F.err("text field the English master has is missing", where, "plans[%d].%s" % (i, s))
                if isinstance(b.get("price"), str) and TYPED_PRICE_RE.search(re.sub(r"\{[^}]*\}", "", b["price"])):
                    F.err("hand-typed price (use the tokens, {P_ZERO} for zero)", where, "plans[%d].price: %s" % (i, b["price"]))
    elif tp is not None:
        F.err("plans in a translation whose master has none", where)
    for k in ("price_override", "price_lead", "price_tier", "plans_footnote", "pricing_note"):
        v = fm.get(k)
        if isinstance(v, str) and TYPED_PRICE_RE.search(re.sub(r"\{[^}]*\}", "", v)):
            F.err("hand-typed price (use the tokens, {P_ZERO} for zero)", where, "%s: %s" % (k, v))
    mr, tr = m.get("release_notes"), fm.get("release_notes")
    if isinstance(mr, list) and mr:
        if not isinstance(tr, list):
            F.err("text field the English master has is missing", where, "release_notes")
        elif len(tr) != len(mr):
            F.err("release_notes length differs from the master", where, "master %d, translation %d" % (len(mr), len(tr)))
        else:
            for i, b in enumerate(tr):
                b = b if isinstance(b, dict) else {}
                for s in b:
                    if s != "note":
                        F.err("fact field in a translation file" if s == "date" else "unknown key in translated release_notes item",
                              where, "release_notes[%d].%s" % (i, s))
                if not nonempty(b.get("note")):
                    F.err("text field the English master has is missing", where, "release_notes[%d].note" % i)
    shots = m.get("screenshots") or []
    caps = fm.get("screenshot_captions")
    if any(isinstance(s, dict) and (s.get("alt") or s.get("caption")) for s in shots):
        if not isinstance(caps, list):
            F.err("text field the English master has is missing", where, "screenshot_captions")
        elif len(caps) != len(shots):
            F.err("screenshot_captions length differs from the master screenshots", where,
                  "master %d, translation %d" % (len(shots), len(caps)))
        else:
            for i, (a, b) in enumerate(zip(shots, caps)):
                a = a if isinstance(a, dict) else {}
                b = b if isinstance(b, dict) else {}
                for s in b:
                    if s not in ("alt", "caption"):
                        F.err("screenshot_captions items carry only alt/caption", where, "[%d].%s" % (i, s))
                for s in ("alt", "caption"):
                    if nonempty(a.get(s)) and not nonempty(b.get(s)):
                        F.err("text field the English master has is missing", where, "screenshot_captions[%d].%s" % (i, s))
                    if not nonempty(a.get(s)) and nonempty(b.get(s)):
                        F.err("screenshot_captions item has a key the master item lacks", where, "[%d].%s" % (i, s))
    if m.get("show_body") is True and not pg["body"].strip():
        F.err("translated app page has no body (master has show_body: true)", where)


def check_seo_block(pg, F, src_fm, keys):
    fm, where = pg["fm"], pg["path"]
    seo = fm.get("seo") if isinstance(fm.get("seo"), dict) else {}
    src_seo = src_fm.get("seo") if isinstance(src_fm.get("seo"), dict) else {}
    for k in keys:
        if not nonempty(seo.get(k)) and (k != "keywords" or nonempty(src_seo.get(k))):
            F.err("seo field missing", where, "seo." + k)


def check_pages(repo, F):
    en = repo.english()
    en_urls = set(en)
    seen = {}
    trans = repo.translations()
    for pg in trans:
        fm, where, code = pg["fm"], pg["path"], pg["lang"]
        if "__yaml_error__" in fm:
            F.err("front matter does not parse", where, fm["__yaml_error__"])
            continue
        if code not in LANGS:
            F.err("unknown language code", where, code)
            continue
        if pg["folder_lang"] != code:
            F.err("page language differs from its folder", where, "lang %s in folder %s" % (code, pg["folder_lang"]))
        if pg["kind"] != "page":
            F.err("translations must be plain pages in the language folder, not collection documents", where)
        if not repo.locale(code):
            F.err("language has pages but no block in _data/locales.yml", where, code)
        local = fm.get("local_only") is True
        ref = fm.get("ref")
        perm = fm.get("permalink")
        if not perm:
            F.err("translated page has no permalink", where)
        elif not str(perm).startswith("/%s/" % code):
            F.err("permalink does not start with the language folder", where, str(perm))
        if local:
            if ref:
                F.err("local_only page must not carry a ref", where, str(ref))
            continue
        if not ref:
            F.err("translated page has no ref (or local_only: true)", where)
            continue
        ref = str(ref)
        if perm and str(perm) != "/%s%s" % (code, ref):
            F.err("permalink is not /<code> + ref (slugs stay identical)", where, "%s vs /%s%s" % (perm, code, ref))
        if ref in repo.redirects and ref not in en_urls:
            F.err("ref points at a redirect stub", where, ref)
        src = en.get(ref)
        if src is None:
            if ref not in repo.redirects:
                F.err("ref points nowhere (no English page with that URL)", where, ref)
            continue
        if (code, ref) in seen:
            F.err("two pages translate the same ref in one language", where, "%s and %s" % (seen[(code, ref)], where))
        seen[(code, ref)] = where
        if not fm.get("translated_from"):
            F.err("translated page has no translated_from", where)
        layout = src["fm"].get("layout") or ("app" if src["kind"] == "apps" else "journal" if src["kind"] == "journal" else None)
        if fm.get("layout") and layout and fm.get("layout") != layout:
            F.err("layout differs from the English page", where, "%s vs %s" % (fm.get("layout"), layout))
        if layout == "app":
            check_app(repo, pg, F)
        elif layout == "support":
            if not fm.get("slug"):
                F.err("translated support page has no slug", where)
            for k in SUPPORT_FORBIDDEN:
                if k in fm:
                    F.err("fact field in a translation file", where, k)
            check_seo_block(pg, F, src["fm"], SEO_KEYS)
        elif layout == "privacy":
            if not fm.get("slug"):
                F.err("translated privacy page has no slug", where)
            for k in PRIVACY_FORBIDDEN:
                if k in fm:
                    F.err("fact field in a translation file", where, k)
            if not nonempty(fm.get("title")):
                F.err("text field the English page has is missing", where, "title")
            check_seo_block(pg, F, src["fm"], SEO_KEYS)
            for k in PRIVACY_PROSE:
                if nonempty(src["fm"].get(k)) and not nonempty(fm.get(k)):
                    F.err("text field the English page has is missing", where, k)
            if dstr(fm.get("last_updated")) != dstr(src["fm"].get("last_updated")):
                F.err("privacy last_updated differs from the English policy date", where,
                      "%s vs %s" % (dstr(fm.get("last_updated")), dstr(src["fm"].get("last_updated"))))
        else:
            check_seo_block(pg, F, src["fm"], ("title", "description"))
            for k in ("title", "quick_answer", "faq"):
                if nonempty(src["fm"].get(k)) and not nonempty(fm.get(k)):
                    F.err("text field the English page has is missing", where, k)
            if src["body"].strip() and not pg["body"].strip():
                F.err("translated page has no body (the English page has one)", where)
    return trans


def check_screenshots(repo, F, trans):
    shots_root = repo.p("assets", "screenshots")
    apps = {}
    for pg in repo.pages:
        if pg["kind"] == "apps":
            slug = pg["fm"].get("slug") or os.path.splitext(os.path.basename(pg["path"]))[0]
            files = [os.path.basename(str(s.get("src", ""))) for s in (pg["fm"].get("screenshots") or [])
                     if isinstance(s, dict) and s.get("src")]
            apps[slug] = files
    still_english = collections.defaultdict(list)
    for pg in trans:
        if not re.fullmatch(r"/apps/[^/]+/", str(pg["fm"].get("ref") or "")):
            continue  # app pages only (support and privacy pages show no screenshots)
        slug = pg["fm"].get("slug")
        files = apps.get(slug)
        if not files:
            continue
        d = os.path.join(shots_root, str(slug), pg["lang"])
        if not all(os.path.isfile(os.path.join(d, f)) for f in files):
            still_english[pg["lang"]].append(slug)
    for code in sorted(still_english):
        F.warn("apps still showing English screenshots", code, ", ".join(sorted(set(still_english[code]))))
    for slug, files in sorted(apps.items()):
        for code in LANGS:
            d = os.path.join(shots_root, slug, code)
            if not os.path.isdir(d) or not files:
                continue
            have = [f for f in files if os.path.isfile(os.path.join(d, f))]
            if len(have) != len(files):
                F.warn("incomplete localized screenshot set (English set shown)", "assets/screenshots/%s/%s/" % (slug, code),
                       "missing " + ", ".join(f for f in files if f not in have))


class Visible(HTMLParser):
    """Visible text of a page plus alt/aria-label/title attribute values; skips script and style."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.chunks, self.anchors, self._skip = [], [], 0
        self.refresh = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self._skip += 1
            return
        if tag == "meta" and (a.get("http-equiv") or "").lower() == "refresh":
            self.refresh = True
        if tag == "a":
            self.anchors.append(a)
        for k in ("alt", "aria-label", "title"):
            if a.get(k) and tag not in ("link", "meta"):
                self.chunks.append(" " + a[k] + " ")

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, d):
        if not self._skip:
            self.chunks.append(d)


def ws(s):
    s = s.replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def strings_of(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from strings_of(v)
    elif isinstance(o, list):
        for v in o:
            yield from strings_of(v)
    elif isinstance(o, str):
        yield o


def check_built(repo, F, site, imap, i18n_data, en_strings):
    if not os.path.isfile(os.path.join(site, "index.html")):
        if repo.translations():
            F.err("no built site to check (build first, or pass --site DIR)", site)
        return 0
    n = 0
    lang_strings = {c: set(ws(s) for s in strings_of(v)) for c, v in i18n_data.items()}
    candidates = sorted({ws(s) for s in strings_of(en_strings)
                         if len(ws(s)) >= MIN_LEFTOVER_LEN and "{" not in s})
    for code in LANGS:
        base = os.path.join(site, code)
        if not os.path.isdir(base):
            continue
        own = lang_strings.get(code, set())
        cands = [s for s in candidates if s not in own]
        for dp, _, fns in os.walk(base):
            for fn in sorted(fns):
                if not fn.endswith(".html"):
                    continue
                fp = os.path.join(dp, fn)
                rel = "/" + os.path.relpath(fp, site).replace(os.sep, "/")
                url = rel[:-10] if rel.endswith("/index.html") else rel
                v = Visible()
                v.feed(open(fp, encoding="utf-8", errors="replace").read())
                if v.refresh:
                    continue
                n += 1
                reported = set()
                for a in v.anchors:
                    h = a.get("href") or ""
                    if h.startswith(SITE):
                        h = h[len(SITE):] or "/"
                    if not h.startswith("/") or h.startswith("//"):
                        continue
                    if a.get("lang") and a.get("lang") != code and a.get("hreflang"):
                        continue  # the language switcher links each version in its own language on purpose
                    path = unquote(urlparse(h).path)
                    if LANG_RE.match(path.lstrip("/") + ("/" if not path.endswith("/") else "")):
                        continue
                    tr = (imap.get(path) or {}).get(code)
                    if tr and path not in reported:
                        reported.add(path)
                        F.err("translated page links to an English page that has a version in its language",
                              url, "%s -> use %s" % (path, tr))
                text = ws(html.unescape(" ".join(v.chunks)))
                for kp in keep_english(repo):
                    text = text.replace(kp, " ")
                for s in cands:
                    if s in text:
                        F.err("leftover English interface string", url, repr(s[:70]))
    return n


def keep_english(repo):
    """Proper names that stay in English in every language (_i18n/keep-english.txt, one per line, # comments).
    They are removed from a page's text before the leftover-English check, so "App Tracking Transparency" does
    not count as the interface string "Transparency"."""
    fp = repo.p("_i18n", "keep-english.txt")
    if not os.path.isfile(fp):
        return []
    lines = [l.strip() for l in open(fp, encoding="utf-8")]
    return sorted((l for l in lines if l and not l.startswith("#")), key=len, reverse=True)


def cmd_check(repo, args):
    F = Findings()
    i18n_data, en_strings = check_i18n_files(repo, F)
    trans = check_pages(repo, F)
    fp = repo.p("_data", "i18n_map.json")
    want = repo.map_text()
    have = open(fp, encoding="utf-8").read() if os.path.isfile(fp) else None
    if have is None:
        F.err("_data/i18n_map.json missing (run scripts/i18n.py map)", "_data/i18n_map.json")
    elif have != want:
        F.err("_data/i18n_map.json is out of date (run scripts/i18n.py map)", "_data/i18n_map.json")
    langs_with_pages = sorted({p["lang"] for p in trans if p["lang"] in LANGS})
    for code in langs_with_pages:
        if i18n_data and code not in i18n_data:
            F.err("language has pages but no _data/i18n/<code>.yml", code)
    check_screenshots(repo, F, trans)
    site = args.site if os.path.isabs(args.site) else os.path.join(repo.root, args.site)
    n_built = check_built(repo, F, site, repo.build_map(), i18n_data, en_strings)
    per = collections.Counter(p["lang"] for p in trans)
    lang_desc = ", ".join("%s %d%s" % (c, per[c], "" if repo.live(c) else " (not live)") for c in sorted(per)) or "none"
    ne, nw = F.count("ERROR"), F.count("WARN")
    print("i18n check: %d translated pages (%s), %d i18n files, %d built translated pages. %d errors, %d warnings."
          % (len(trans), lang_desc, len(i18n_data), n_built, ne, nw))
    F.report(args.verbose)
    return 1 if ne else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("command", choices=("map", "stale", "check"))
    ap.add_argument("--root", default=".", help="repo root (default: current directory)")
    ap.add_argument("--site", default="_site", help="built site for check (default: _site under --root)")
    ap.add_argument("--max-diff-lines", type=int, default=60, help="stale: print diffs up to this many lines")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()
    if not os.path.isfile(os.path.join(args.root, "_config.yml")):
        sys.exit("No _config.yml in %s: run from the repo root or pass --root." % os.path.abspath(args.root))
    repo = Repo(args.root)
    return {"map": cmd_map, "stale": cmd_stale, "check": cmd_check}[args.command](repo, args)


if __name__ == "__main__":
    sys.exit(main())
