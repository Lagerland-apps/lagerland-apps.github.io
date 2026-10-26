#!/usr/bin/env python3
"""SEO / AEO audit of the BUILT site. Stdlib only. Run it before every push.

  GEM_HOME=~/.gem/ruby/2.6.0 /usr/bin/ruby ~/.gem/ruby/2.6.0/gems/jekyll-3.9.5/exe/jekyll build
  python3 scripts/seo-audit.py            # audits ./_site
  python3 scripts/seo-audit.py PATH -v    # another build dir, list every warning

Exit code 1 when any ERROR is found. WARN items are worth fixing but don't block.

Checks, per HTML page: <title> and meta description present, not the generic
site tagline, sane length, unique; one canonical that matches the URL; one H1;
lang; Open Graph + Twitter tags; share image exists; every JSON-LD block parses;
breadcrumb targets exist; FAQPage questions and answers are visible on the page;
Article has headline/date/image/author; internal links and images resolve.
Site-wide: sitemap.xml == every indexable page (no redirects, no noindex, no 404s),
ai-sitemap.xml has the same set, lastmod values are real dates (not all one build
stamp: a date shared by most URLs passes only when git shows their source files
edited that day, as after a real sitewide edit); llms.txt / llms-full.txt / ai-index.json parse and every URL in them
resolves; every app, guide and journal post is routed in llms.txt; robots.txt
allows crawling and lists the sitemaps.
Translations (TRANSLATION.md 4.13, 7.1, 7.2): <html lang>/dir per language from _data/locales.yml; hreflang
self-referencing, reciprocal, valid codes, x-default = English, targets indexable and not redirects; canonical
= own URL on translated pages too; per-script title/description limits and per-language duplicate checks;
local-currency prices on translated app pages; per-language llms.txt routing, AI-file URLs and sitemaps;
non-live languages noindex and in no sitemap; WARN for links from a translated page to an English page.
"""
import argparse, collections, datetime, html, importlib.util, json, os, re, subprocess, sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET

SITE = "https://lagerland-apps.github.io"
GENERIC_DESC = "Calm, privacy-first apps for iPhone"
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
LANGS = ("de", "fr", "it", "es", "pt", "zh", "ja", "ko", "id", "es-mx", "pt-br", "pl", "tr", "nl", "ru", "ar")
LANG_PATH_RE = re.compile(r"^/(%s)(/|$)" % "|".join(sorted(LANGS, key=len, reverse=True)))
CJK = ("zh", "ja", "ko")
# TRANSLATION.md section 2, used when a locales.yml block lacks a field: code -> (html_lang, hreflang, dir)
REGISTER = {"en": ("en", ["en"], "ltr"), "de": ("de", ["de"], "ltr"), "fr": ("fr", ["fr"], "ltr"),
            "it": ("it", ["it"], "ltr"), "es": ("es-ES", ["es-ES"], "ltr"), "pt": ("pt-PT", ["pt-PT"], "ltr"),
            "zh": ("zh-CN", ["zh-CN"], "ltr"), "ja": ("ja", ["ja"], "ltr"), "ko": ("ko", ["ko"], "ltr"),
            "id": ("id", ["id"], "ltr"), "es-mx": ("es-MX", ["es-MX"], "ltr"), "pt-br": ("pt-BR", ["pt-BR"], "ltr"),
            "pl": ("pl", ["pl"], "ltr"), "tr": ("tr", ["tr"], "ltr"), "nl": ("nl", ["nl"], "ltr"),
            "ru": ("ru", ["ru"], "ltr"), "ar": ("ar", ["ar"], "rtl")}


def page_lang(url):
    """Language of a URL from its path prefix /<code>/; English otherwise."""
    path = url[len(SITE):] if url.startswith(SITE) else url
    m = LANG_PATH_RE.match(path)
    return m.group(1) if m else "en"


def _scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1].replace('\\"', '"') if v[0] == '"' else v[1:-1].replace("''", "'")
    if v in ("true", "True"): return True
    if v in ("false", "False"): return False
    if re.fullmatch(r"-?\d+", v): return int(v)
    return v


def _flow(v):
    """`[a, b]` and `{ k: v, k2: "v" }` on one line (no nesting inside)."""
    v = v.strip()
    inner = v[1:-1]
    parts, buf, q = [], "", None
    for ch in inner:
        if q:
            buf += ch
            if ch == q: q = None
        elif ch in "\"'":
            q = ch; buf += ch
        elif ch == ",":
            parts.append(buf); buf = ""
        else:
            buf += ch
    if buf.strip(): parts.append(buf)
    if v[0] == "[":
        return [_scalar(x) for x in parts]
    out = {}
    for x in parts:
        k, _, val = x.partition(":")
        out[k.strip()] = _scalar(val)
    return out


def mini_yaml(text):
    """Stdlib fallback for the YAML subset _data/locales.yml and _data/i18n/*.yml use: nested block maps,
    scalars, one-line flow lists/maps, comments. Used only when PyYAML is not installed."""
    root, stack = {}, [(-1, None)]
    stack[0] = (-1, root)
    for raw in text.splitlines():
        line = re.sub(r"\s+#.*$", "", raw) if not re.search(r"[\"'][^\"']*#", raw) else raw
        if not line.strip() or line.lstrip().startswith("#"): continue
        ind = len(line) - len(line.lstrip())
        m = re.match(r"^\s*([^:]+?):(\s+(.*))?$", line)
        if not m: continue
        while stack and stack[-1][0] >= ind: stack.pop()
        parent = stack[-1][1]
        k, v = m.group(1).strip().strip("\"'"), (m.group(3) or "").strip()
        if not v:
            parent[k] = {}; stack.append((ind, parent[k]))
        elif v[0] in "[{":
            parent[k] = _flow(v)
        else:
            parent[k] = _scalar(v)
    return root


def load_yaml(path):
    if not os.path.isfile(path): return {}
    text = open(path, encoding="utf-8").read()
    try:
        import yaml
        return yaml.safe_load(text) or {}
    except ImportError:
        return mini_yaml(text)


def fmt_money(amount, rule, decimals=None):
    """Python twin of _includes/money.html: one catalog amount in a language's currency rule.
    position: before ("$3.99"), before_space ("€ 3,99"), after ("3,99 €"); decimals overrides the rule ({P_ZERO})."""
    whole, _, frac = str(amount).partition(".")
    grp = str(rule.get("group") or "")
    rest, out = whole, ""
    while len(rest) > 3:
        out = grp + rest[-3:] + out; rest = rest[:-3]
    num = rest + out
    dec = int(rule.get("decimals", 2) if rule.get("decimals") is not None else 2) if decimals is None else decimals
    if dec > 0:
        num += str(rule.get("decimal", ".")) + (frac + "000000")[:dec]
    sym = str(rule.get("symbol", ""))
    pos = rule.get("position")
    return f"{num} {sym}" if pos == "after" else f"{sym} {num}" if pos == "before_space" else f"{sym}{num}"


def money_regex(rule):
    sym = re.escape(str(rule.get("symbol", "")))
    g, d = re.escape(str(rule.get("group") or "")), re.escape(str(rule.get("decimal", ".")))
    num = rf"\d{{1,3}}(?:{g}\d{{3}})+(?:{d}\d+)?|\d+(?:{d}\d+)?" if g else rf"\d+(?:{d}\d+)?"
    if rule.get("position") == "after":
        return re.compile(rf"(?<![\d.,])(?:{num})\s?{sym}")
    return re.compile(rf"{sym}\s?(?:{num})(?![\d])")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = None; self._t = False
        self.metas, self.links, self.anchors, self.imgs = [], [], [], []
        self.h1 = []; self._h1 = False; self._h1buf = ""
        self.jsonld = []; self._ld = False; self._ldbuf = ""
        self.lang = None; self.dir = None; self.text = []; self._skip = 0; self.refresh = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = a.get("lang"); self.dir = a.get("dir")
        elif tag == "title": self._t = True; self.title = ""
        elif tag == "meta":
            self.metas.append(a)
            if (a.get("http-equiv") or "").lower() == "refresh": self.refresh = True
        elif tag == "link": self.links.append(a)
        elif tag == "a": self.anchors.append(a)
        elif tag == "img": self.imgs.append(a)
        elif tag == "h1": self._h1 = True; self._h1buf = ""
        elif tag == "script":
            if a.get("type") == "application/ld+json": self._ld = True; self._ldbuf = ""
            else: self._skip += 1
        elif tag == "style": self._skip += 1

    def handle_endtag(self, tag):
        if tag == "title": self._t = False
        elif tag == "h1": self._h1 = False; self.h1.append(self._h1buf.strip())
        elif tag == "script":
            if self._ld: self._ld = False; self.jsonld.append(self._ldbuf)
            elif self._skip: self._skip -= 1
        elif tag == "style" and self._skip: self._skip -= 1

    def handle_data(self, d):
        if self._t: self.title += d
        if self._h1: self._h1buf += d
        if self._ld: self._ldbuf += d; return
        if not self._skip: self.text.append(d)


def norm(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


BOT_PREFIX = "Sync App Store ratings"  # the ratings bot only rewrites rating fields; its commits are not edits


def git_edited_urls(repo, day):
    """Live URLs whose source file git shows as edited on `day` (YYYY-MM-DD): committed that day by anyone but
    the ratings bot, or changed in the working tree when `day` is today. None when git can't answer.
    Source paths map to URLs through scripts/indexnow-ping.py, so both scripts share one mapping."""
    try:
        spec = importlib.util.spec_from_file_location(
            "indexnow_ping", os.path.join(repo, "scripts", "indexnow-ping.py"))
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        since = (datetime.date.fromisoformat(day) - datetime.timedelta(days=2)).isoformat()
        log = subprocess.run(["git", "-C", repo, "log", f"--since={since}", "--format=@@%cs%x09%s", "--name-only"],
                             capture_output=True, text=True, check=True).stdout
        files, take = set(), False
        for line in log.splitlines():
            if line.startswith("@@"):
                d, _, subject = line[2:].partition("\t")
                take = d == day and not subject.startswith(BOT_PREFIX)
            elif line.strip() and take:
                files.add(line.strip())
        if day == datetime.date.today().isoformat():
            st = subprocess.run(["git", "-C", repo, "status", "--porcelain", "--untracked-files=all"],
                                capture_output=True, text=True, check=True).stdout
            for line in st.splitlines():
                files.add(line[3:].split(" -> ")[-1].strip().strip('"'))
    except Exception:
        return None
    return {u for u in map(mod.path_to_url, files) if u}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default="_site")
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    if not os.path.isfile(os.path.join(root, "index.html")):
        sys.exit(f"No built site at {root}. Build first (see the docstring).")

    findings = collections.defaultdict(list)  # (level, kind) -> [(url, msg)]
    def err(kind, url, msg=""): findings[("ERROR", kind)].append((url, msg))
    def warn(kind, url, msg=""): findings[("WARN", kind)].append((url, msg))

    def url_for(path):
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        if rel == "index.html": return SITE + "/"
        if rel.endswith("/index.html"): return SITE + "/" + rel[:-10]
        return SITE + "/" + rel

    def resolve(href):
        if href.rstrip("/") == SITE: return os.path.join(root, "index.html")
        p = unquote(urlparse(href).path)
        if p.startswith(SITE): p = p[len(SITE):]
        if not p.startswith("/"): return None
        cands = [root + p + "index.html"] if p.endswith("/") else [root + p, root + p + ".html", root + p + "/index.html"]
        return next((c for c in cands if os.path.isfile(c)), None)

    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    locales = load_yaml(os.path.join(repo, "_data", "locales.yml")) or {}
    def loc(code): return locales.get(code) or {}
    def html_lang_of(code): return str(loc(code).get("html_lang") or REGISTER.get(code, (code,))[0])
    def dir_of(code): return str(loc(code).get("dir") or REGISTER.get(code, (None, None, "ltr"))[2])
    def hreflangs_of(code):
        h = loc(code).get("hreflang") or REGISTER.get(code, (None, [code]))[1]
        return [str(x) for x in (h if isinstance(h, list) else [h])]
    def is_live(code): return code == "en" or loc(code).get("live") is True
    valid_hreflang = {"x-default"} | {h for c in set(REGISTER) | set(locales) for h in hreflangs_of(c)}
    i18n_desc = {}
    for code in LANGS:
        try: i18n_desc[code] = str((load_yaml(os.path.join(repo, "_data", "i18n", code + ".yml")) or {}).get("site_description") or "")
        except Exception: pass

    pages, redirects, noindex = {}, set(), set()
    titles, descs = collections.defaultdict(list), collections.defaultdict(list)
    alts, langs, en_links = {}, {}, collections.defaultdict(set)
    for dp, _, fns in os.walk(root):
        for fn in fns:
            if not fn.endswith(".html"): continue
            path = os.path.join(dp, fn)
            src = open(path, encoding="utf-8", errors="replace").read()
            p = Page(); p.feed(src)
            url = url_for(path)
            if p.refresh: redirects.add(url); continue
            if url.endswith(("/google9835ba948bb89980.html", "/yandex_ad81e17bf10db464.html",
                             "/naver8c063a2d4bfcc331b0d1f7f45c9ef55b.html")): continue
            meta = {}
            for m in p.metas:
                k = m.get("name") or m.get("property")
                if k and k not in meta: meta[k] = m.get("content") or ""
            robots = meta.get("robots", "")
            is_noindex = "noindex" in robots
            if is_noindex: noindex.add(url)
            pages[url] = p
            lang = page_lang(url); langs[url] = lang
            alts[url] = [(l.get("hreflang"), l.get("href")) for l in p.links
                         if l.get("rel") == "alternate" and l.get("hreflang")]
            title = (p.title or "").strip(); desc = meta.get("description", "")
            if not title: err("title missing", url)
            else:
                titles[(lang, title)].append(url)
                if lang == "en":
                    if len(title) > 65: warn("title > 65 chars", url, f"{len(title)}: {title}")
                else:
                    lim = 30 if lang in CJK else 60
                    if len(title) > lim: warn(f"title > {lim} chars ({'CJK' if lang in CJK else 'Latin/Cyrillic/Arabic'} limit)", url, f"{len(title)}: {title}")
            if not desc: err("meta description missing", url)
            else:
                descs[(lang, desc)].append(url)
                if desc.startswith(GENERIC_DESC) and url != SITE + "/":
                    err("generic site tagline used as description (add seo.description)", url)
                if lang == "en":
                    if len(desc) > 165: warn("description > 165 chars", url, str(len(desc)))
                    if len(desc) < 70: warn("description < 70 chars", url, desc)
                else:
                    lo, hi = (50, 100) if lang in CJK else (70, 155)
                    if not lo <= len(desc) <= hi:
                        warn(f"description not {lo}-{hi} chars ({'CJK' if lang in CJK else 'Latin/Cyrillic/Arabic'} limit)", url, f"{len(desc)}: {desc[:80]}")
                    if i18n_desc.get(lang) and desc == i18n_desc[lang] and not re.fullmatch(r"/[^/]+/", url[len(SITE):]):
                        err("generic site tagline used as description (add seo.description)", url)
            canon = [l.get("href") for l in p.links if l.get("rel") == "canonical"]
            if not is_noindex or lang != "en":  # translated pages: canonical is always self, noindex or not
                if len(canon) != 1: err("canonical count != 1", url, str(canon))
                elif canon[0] != url: err("canonical does not match URL", url, canon[0])
            if len(p.h1) != 1: err("H1 count != 1", url, str(p.h1[:3]))
            want_lang = html_lang_of(lang)
            if not p.lang: err("html lang missing", url)
            elif p.lang != want_lang: err("html lang does not match the page language (locales.yml html_lang)", url, f"{p.lang} vs {want_lang}")
            want_dir = dir_of(lang)
            if p.dir is None:
                err("html dir missing", url, f"want {want_dir}")
            elif p.dir != want_dir: err("html dir does not match the page language", url, f"{p.dir} vs {want_dir}")
            if lang != "en" and not is_live(lang):
                if not is_noindex: err("page of a non-live language is indexable (must be noindex)", url)
                if alts[url]: err("page of a non-live language carries hreflang", url)
            for k in ("og:title", "og:description", "og:image", "og:url", "twitter:card"):
                if not meta.get(k): err("social tag missing", url, k)
            if meta.get("og:image") and not resolve(meta["og:image"]): err("og:image 404", url, meta["og:image"])
            words = len(" ".join(p.text).split())
            if words < 250 and not is_noindex: warn("thin page (< 250 words)", url, str(words))
            text = norm(" ".join(p.text))
            for blk in p.jsonld:
                try: j = json.loads(blk)
                except Exception as e: err("JSON-LD does not parse", url, str(e)[:100]); continue
                nodes = []
                def walk(o):
                    if isinstance(o, dict):
                        if "@type" in o: nodes.append(o)
                        for v in o.values(): walk(v)
                    elif isinstance(o, list):
                        for v in o: walk(v)
                walk(j)
                for n in nodes:
                    ty = n["@type"] if isinstance(n["@type"], list) else [n["@type"]]
                    if "BreadcrumbList" in ty:
                        for li in n.get("itemListElement", []):
                            it = li.get("item"); it = it.get("@id") if isinstance(it, dict) else it
                            if it and it.startswith(SITE) and not resolve(it): err("breadcrumb target 404", url, it)
                    if "FAQPage" in ty:
                        for q in n.get("mainEntity", []):
                            qn = norm(q.get("name"))
                            # Answers may be a condensed version of the schema text (FAQ rich
                            # results are gov/health-only since 2023); questions must match.
                            if qn and qn[:60] not in text: warn("FAQ question in schema but not visible", url, q.get("name", "")[:80])
                    if "Article" in ty or "BlogPosting" in ty:
                        if len(n.get("headline", "")) > 110: warn("Article headline > 110 chars", url)
                        if "Article" in ty:
                            for k in ("headline", "datePublished", "dateModified", "image", "author"):
                                if not n.get(k): err("Article field missing", url, k)
                    if "SoftwareApplication" in ty:
                        for k in ("name", "operatingSystem", "applicationCategory", "offers"):
                            if not n.get(k): err("SoftwareApplication field missing", url, k)
            for an in p.anchors:
                h = an.get("href") or ""
                if not h or h.startswith(("mailto:", "tel:", "#", "javascript:")): continue
                if h.startswith(SITE): h = h[len(SITE):] or "/"
                if h.startswith("//") or re.match(r"^[a-z]+:", h): continue
                if not h.startswith("/"): warn("relative link", url, h); continue
                tgt = resolve(h)
                if not tgt: err("broken internal link", url, h)
                elif lang != "en" and tgt.endswith(".html") and page_lang(url_for(tgt)) == "en" \
                        and not (an.get("lang") and an.get("lang") != lang and an.get("hreflang")):
                    en_links[url].add(url_for(tgt).replace(SITE, ""))  # switcher links (own lang + hreflang) are fine
            for im in p.imgs:
                if im.get("alt") is None: warn("img without alt", url, im.get("src"))
                s = im.get("src") or ""
                if s.startswith(("/", SITE)) and not resolve(s): err("image 404", url, s)

    for (_, t), us in titles.items():
        if len(us) > 1: warn("duplicate title", us[0], f"{t} (also {', '.join(u.replace(SITE, '') for u in us[1:])})")
    for (_, d), us in descs.items():
        if len(us) > 1: warn("duplicate description", us[0], f"also {', '.join(u.replace(SITE, '') for u in us[1:])}")

    # Sitemaps
    def sm(fn):
        try: r = ET.parse(os.path.join(root, fn)).getroot()
        except Exception as e: err("sitemap does not parse", fn, str(e)); return {}
        out = {}
        for u in r.findall("s:url", NS):
            lm = u.find("s:lastmod", NS)
            out[u.find("s:loc", NS).text.strip()] = lm.text if lm is not None else None
        return out
    s1, s2 = sm("sitemap.xml"), sm("ai-sitemap.xml")
    indexable = {u for u in pages if u not in noindex and not u.endswith("/404.html")}
    for u in sorted(indexable - set(s1)): err("indexable page missing from sitemap.xml", u)
    for u in sorted(set(s1) - indexable):
        kind = "redirect" if u in redirects else "noindex" if u in noindex else "404/non-page"
        err(f"sitemap.xml lists a {kind} URL", u)
    if set(s1) != set(s2): err("ai-sitemap.xml URL set differs from sitemap.xml", "ai-sitemap.xml",
                               f"+{len(set(s2) - set(s1))} -{len(set(s1) - set(s2))}")
    vals = [v for v in s1.values() if v]
    if vals:
        top, n = collections.Counter(vals).most_common(1)[0]
        if n > 0.8 * len(s1):
            # One date on most URLs is either a build stamp (the old jekyll-sitemap bug: every lastmod set to
            # the build day) or a real sitewide edit, like the 2026-10-26 copy rewrite. Git tells them apart:
            # a date is real when the page's source file was edited that day. Hubs take the newest date of
            # their section, so they count as backed when any page in their section is.
            repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            edited = git_edited_urls(repo_dir, top)
            same = [u for u, v in s1.items() if v == top]
            if edited is None:
                err("sitemap lastmod is the same for >80% of URLs (looks like a build stamp; git unavailable to confirm)",
                    "sitemap.xml", f"{top} x{n}")
            else:
                hubs = {SITE + "/": ("/apps/", "/journal/"), SITE + "/apps/": ("/apps/",),
                        SITE + "/journal/": ("/journal/",), SITE + "/alternatives/": ("/alternatives/",)}
                def backed(u):
                    if u in edited: return True
                    return any(e[len(SITE):].startswith(sec) for sec in hubs.get(u, ()) for e in edited)
                unbacked = [u for u in same if not backed(u)]
                if len(unbacked) > 0.2 * n:
                    err("sitemap lastmod is the same for >80% of URLs and git shows no edit that day for many "
                        "(looks like a build stamp)", "sitemap.xml", f"{top} x{n}, {len(unbacked)} without a git edit")
                else:
                    for u in unbacked: warn("sitemap lastmod not backed by a git edit that day", u, top)
    for u, v in s1.items():
        if not v and u in indexable: warn("sitemap URL without lastmod (set last_updated)", u)

    # Translations: hreflang (TRANSLATION.md 7.1), per-language sitemaps, non-live languages
    for u in sorted(indexable):
        al = alts.get(u) or []
        if not al: continue
        codes = [c for c, _ in al]
        for c in sorted(set(codes)):
            if codes.count(c) > 1: err("hreflang code listed twice", u, c)
            if c not in valid_hreflang:
                err("invalid hreflang code (not in locales.yml)" + (" (numeric region)" if re.search(r"-\d", c) else ""), u, c)
        hrefs = {h for _, h in al}
        if u not in hrefs: err("hreflang set does not reference the page itself", u)
        xd = [h for c, h in al if c == "x-default"]
        en_v = [h for c, h in al if c != "x-default" and page_lang(h or "") == "en"]
        if len(xd) != 1: err("hreflang x-default missing", u)
        elif page_lang(xd[0]) != "en" or (en_v and xd[0] != en_v[0]): err("hreflang x-default does not point at the English URL", u, xd[0])
        for c, h in al:
            if c == "x-default" or not h: continue
            if c in valid_hreflang and c not in hreflangs_of(page_lang(h)):
                err("hreflang code does not match the target's language", u, f"{c} -> {h.replace(SITE, '')}")
            if not is_live(page_lang(h)): err("hreflang target is in a language that is not live", u, h); continue
            if h in redirects: err("hreflang target is a redirect", u, h); continue
            if h not in pages: err("hreflang target missing from the build", u, h); continue
            if h in noindex: err("hreflang target is noindex", u, h); continue
            if sorted(alts.get(h) or []) != sorted(al): err("hreflang not reciprocal (versions list different sets)", u, h.replace(SITE, ""))
    imap_path = os.path.join(repo, "_data", "i18n_map.json")
    try: imap = json.load(open(imap_path, encoding="utf-8")) if os.path.isfile(imap_path) else {}
    except Exception as e: imap = {}; err("_data/i18n_map.json does not parse", "_data/i18n_map.json", str(e)[:100])
    for ref, versions in sorted(imap.items()):
        u = SITE + ref
        if u not in indexable: continue
        listed = {h for _, h in alts.get(u) or []}
        for code, tu in sorted(versions.items()):
            if code != "en" and is_live(code) and SITE + tu in indexable and SITE + tu not in listed:
                err("hreflang missing a live translation from i18n_map.json", u, tu)
    for u in sorted(s1):
        if page_lang(u) != "en" and not is_live(page_lang(u)): err("sitemap.xml lists a page of a non-live language", u)
    for code in LANGS:
        if not os.path.isdir(os.path.join(root, code)): continue
        want = {u for u in indexable if langs.get(u) == code}
        if os.path.isfile(os.path.join(root, code, "sitemap.xml")):
            got = set(sm(f"{code}/sitemap.xml"))
            for u in sorted(want - got): err(f"indexable page missing from /{code}/sitemap.xml", u)
            for u in sorted(got - want): err(f"/{code}/sitemap.xml lists a URL that is not an indexable {code} page", u)
    for u in sorted(en_links):
        for t in sorted(en_links[u]): warn("translated page links to an English page", u, t)

    # AI files
    llms_path = os.path.join(root, "llms.txt")
    llms = open(llms_path, encoding="utf-8").read() if os.path.isfile(llms_path) else ""
    if not llms.startswith("# "): err("llms.txt must start with an H1", "llms.txt")
    if re.search(r"[^\n#]## [A-Z]", llms):
        err("llms.txt has a heading glued to the previous line (Liquid whitespace trim)", "llms.txt")
    for fn in ("llms.txt", "llms-full.txt"):
        fp = os.path.join(root, fn)
        if not os.path.isfile(fp): err("missing", fn); continue
        txt = open(fp, encoding="utf-8").read()
        if "{{" in txt or "{%" in txt: err("unrendered Liquid in output", fn)
        for m in set(re.findall(re.escape(SITE) + r"[^\s\)\]>\"'`,]*", txt)):
            m = m.rstrip(".;:")
            if not resolve(m or "/"): err(f"{fn} links to a missing page", m)
            elif m in redirects: warn(f"{fn} links to a redirect", m)
    for code in LANGS:
        for fn in (f"{code}/llms.txt", f"{code}/llms-full.txt"):
            fp = os.path.join(root, fn)
            if not os.path.isfile(fp): continue
            txt = open(fp, encoding="utf-8").read()
            if "{{" in txt or "{%" in txt: err("unrendered Liquid in output", fn)
            for m in set(re.findall(re.escape(SITE) + r"[^\s\)\]>\"'`,]*", txt)):
                m = m.rstrip(".;:")
                if not resolve(m or "/"): err(f"{fn} links to a missing page", m)
                elif m in redirects: warn(f"{fn} links to a redirect", m)
        routed = [u for u in sorted(indexable) if langs.get(u) == code and
                  re.fullmatch(rf"/{re.escape(code)}/(apps/[^/]+|guides/[^/]+|journal/[^/]+)/", u[len(SITE):])]
        if routed:
            fp = os.path.join(root, code, "llms.txt")
            ltxt = open(fp, encoding="utf-8").read() if os.path.isfile(fp) else None
            if ltxt is None: err(f"/{code}/llms.txt missing (the language has indexable pages)", f"/{code}/")
            else:
                for u in routed:
                    if u not in ltxt: err(f"not routed in /{code}/llms.txt", u)
    try:
        aj = json.load(open(os.path.join(root, "ai-index.json"), encoding="utf-8"))
        for m in set(re.findall(re.escape(SITE) + r"[^\"\s]*", json.dumps(aj))):
            if not resolve(m or "/"): err("ai-index.json links to a missing page", m)
    except Exception as e:
        err("ai-index.json does not parse", "ai-index.json", str(e)[:120])
    guide = llms.split("## AI assistant recommendation guide", 1)[-1]
    for u in sorted(indexable):
        path = u[len(SITE):]
        if re.fullmatch(r"/apps/[^/]+/", path) or (path.startswith("/journal/") and path != "/journal/"):
            if u not in guide: warn("not routed in llms.txt AI assistant recommendation guide", u)
        if path.startswith(("/guides/", "/for/")) and u not in llms:
            warn("guide/audience page not described in llms.txt", u)
    try:
        ET.parse(os.path.join(root, "feed.xml"))
    except Exception as e:
        err("feed.xml does not parse", "feed.xml", str(e))
    rb = open(os.path.join(root, "robots.txt"), encoding="utf-8").read()
    if re.search(r"(?im)^disallow:\s*/\s*$", rb): err("robots.txt disallows the whole site for some agent", "robots.txt")
    if f"Sitemap: {SITE}/sitemap.xml" not in rb: err("robots.txt does not list sitemap.xml", "robots.txt")

    # Master data (App Store Connect export) vs what the built pages say.
    # _data/catalog.json comes from scripts/sync-asc-master.mjs; pages must never contradict it.
    cat_path = os.path.join(repo, "_data", "catalog.json")
    try:
        cat = json.load(open(cat_path, encoding="utf-8"))
    except Exception as e:
        cat = None
        err("_data/catalog.json missing or invalid (run scripts/sync-asc-master.mjs)", "_data/catalog.json", str(e)[:100])
    if cat:
        live_n = cat["meta"]["live_app_count"]
        site_live = set()
        for fn in os.listdir(os.path.join(repo, "_apps")):
            if fn.endswith(".md"):
                fm = open(os.path.join(repo, "_apps", fn), encoding="utf-8").read().split("\n---", 1)[0]
                if re.search(r"(?m)^status:\s*live\s*$", fm): site_live.add(fn[:-3])
        cat_live = {k for k, v in cat["apps"].items() if v["live"]}
        for slug in sorted(site_live ^ cat_live):
            err("app is live in only one of _apps/*.md and the App Store Connect catalog", "/apps/" + slug + "/")
        for slug, c in cat["apps"].items():
            f = os.path.join(root, "apps", slug, "index.html")
            if not c["live"] or not os.path.isfile(f): continue
            h = open(f, encoding="utf-8").read()
            m = re.search(r"<strong>Platforms:</strong>\s*([^<]*?)\.\s*<strong>", h)
            want = ", ".join(c["platforms"])
            if not m or m.group(1).strip() != want:
                err("page platforms differ from the catalog", "/apps/" + slug + "/", f"page={m.group(1).strip() if m else None!r} catalog={want!r}")
            known = set()
            for pl in c["plans"].values():
                if pl["prices"].get("USA"): known.add(pl["prices"]["USA"]["amount"])
            for o in c["other_iaps"]:
                if o["prices"].get("USA"): known.add(o["prices"]["USA"]["amount"])
            if c["app_price"] and c["app_price"]["prices"].get("USA"): known.add(c["app_price"]["prices"]["USA"]["amount"])
            money = {f"{float(x):.2f}" for x in known} | {"0.00"}
            # the price pills (hero, sticky, comparison CTA) and every plan card
            shown = re.findall(r'class="pill[^"]*"[^>]*>([^<]*\$[^<]*)<', h) + re.findall(r'class="plan-price">([^<]*)<', h)
            for txt in shown:
                for amt in re.findall(r"\$(\d[\d,]*\.?\d*)", txt):
                    if f"{float(amt.replace(',', '')):.2f}" not in money:
                        err("page price is not in the App Store Connect catalog", "/apps/" + slug + "/", f"${amt} in {txt.strip()[:50]!r}")
        # Translated app pages: own prices only, in the language's territory currency and format.
        terr_cur = {t["code"]: t["currency"] for t in cat["meta"].get("territories", [])}
        for code in LANGS:
            if not os.path.isdir(os.path.join(root, code, "apps")): continue
            terr = loc(code).get("territory")
            cur = terr_cur.get(terr)
            rule = ((loc(code).get("currencies") or {}).get(cur) if cur else None)
            if not cur:
                err("language territory not in the catalog (locales.yml territory)", f"/{code}/", str(terr)); continue
            if not rule:
                err("no currency rule for the language's territory currency (locales.yml currencies)", f"/{code}/", cur); continue
            mre = money_regex(rule)
            for slug, c in cat["apps"].items():
                f = os.path.join(root, code, "apps", slug, "index.html")
                if not os.path.isfile(f): continue
                h = open(f, encoding="utf-8").read()
                u = f"/{code}/apps/{slug}/"
                amounts, usd = set(), set()
                for pr in [pl["prices"] for pl in c["plans"].values()] + [o["prices"] for o in c["other_iaps"]] + \
                          ([c["app_price"]["prices"]] if c["app_price"] else []):
                    if pr.get(terr): amounts.add(pr[terr]["amount"])
                    if pr.get("USA"): usd.add(f"{float(pr['USA']['amount']):.2f}")
                ok = {re.sub(r"\s", " ", fmt_money(a, rule)) for a in amounts} | {re.sub(r"\s", " ", fmt_money("0", rule, 0))}
                shown = re.findall(r'class="pill[^"]*"[^>]*>([^<]*)<', h) + re.findall(r'class="plan-price">([^<]*)<', h)
                for txt in shown:
                    txt = re.sub(r"\s", " ", html.unescape(txt))
                    for pm in mre.finditer(txt):
                        if re.sub(r"\s", " ", pm.group(0)) not in ok:
                            err(f"page price is not this app's {terr} catalog price in the {code} format", u,
                                f"{pm.group(0)!r} in {txt.strip()[:50]!r}; expected one of {sorted(ok)}")
                    if cur != "USD" and rule.get("symbol") != "$":
                        for amt in re.findall(r"\$\s?(\d[\d,]*\.?\d*)", txt):
                            err(f"USD price on a page whose territory currency is {cur}", u, f"${amt} in {txt.strip()[:50]!r}")
                if cur != "USD" and rule.get("symbol") != "$":
                    pg = pages.get(SITE + u)
                    vis = " ".join(pg.text) if pg else ""
                    # Body text also carries competitor prices (comparison tables), which can equal our own
                    # USD amounts, so outside the pills and plan cards a dollar amount is only a WARN.
                    for amt in sorted(set(re.findall(r"\$\s?(\d[\d,]*\.\d\d)\b", vis))):
                        own = f"{float(amt.replace(',', '')):.2f}" in usd
                        warn("USD amount on a translated app page (untranslated own price or competitor price?)", u,
                             "$" + amt + (" (equals this app's own USD price)" if own else ""))
        count_re = re.compile(r"\b(\d{2})\s+(?:live |privacy-first |indie |iOS |free )*apps\b", re.I)
        for dp, _, fns in os.walk(root):
            for fn in fns:
                if not fn.endswith((".html", ".txt", ".json", ".xml")): continue
                fp = os.path.join(dp, fn)
                t = open(fp, encoding="utf-8", errors="ignore").read()
                rel = "/" + os.path.relpath(fp, root).replace(os.sep, "/")
                if re.search(r"\{(?:P_[A-Z_]+|P_IAP:[^}]*|TRIAL|PLATFORMS|APP_COUNT)\}", t):
                    err("unresolved price/platform token in output", rel)
                if re.search(r'class="plan-price">\s*(?:/|<)', t):
                    err("plan card rendered without a price", rel)
                if fn.endswith(".html") and "/_" not in rel:
                    plain = re.sub(r"<[^>]+>", " ", t)
                    for cm in count_re.finditer(plain):
                        n = int(cm.group(1))
                        if n == live_n or n < 15: continue
                        if n == live_n - 1 and plain[max(0, cm.start() - 6):cm.start()].lower() == "other ": continue  # "the studio's other N apps"
                        warn("hard-typed app count differs from the catalog count", rel, f"{n} vs {live_n}")

    # Report
    n_err = sum(len(v) for (lvl, _), v in findings.items() if lvl == "ERROR")
    n_warn = sum(len(v) for (lvl, _), v in findings.items() if lvl == "WARN")
    print(f"Audited {len(pages)} pages ({len(noindex)} noindex), {len(redirects)} redirect stubs, "
          f"{len(s1)} sitemap URLs. {n_err} errors, {n_warn} warnings.")
    for (lvl, kind), items in sorted(findings.items(), key=lambda kv: (kv[0][0] != "ERROR", kv[0][1])):
        print(f"\n{lvl}  {kind} ({len(items)})")
        for u, m in items[: None if (a.verbose or lvl == "ERROR") else 8]:
            print(f"   {u.replace(SITE, '')}  {m}")
        if not a.verbose and lvl == "WARN" and len(items) > 8:
            print(f"   … {len(items) - 8} more (-v to list all)")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
