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
stamp); llms.txt / llms-full.txt / ai-index.json parse and every URL in them
resolves; every app, guide and journal post is routed in llms.txt; robots.txt
allows crawling and lists the sitemaps.
"""
import argparse, collections, html, json, os, re, sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET

SITE = "https://lagerland-apps.github.io"
GENERIC_DESC = "Calm, privacy-first apps for iPhone"
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = None; self._t = False
        self.metas, self.links, self.anchors, self.imgs = [], [], [], []
        self.h1 = []; self._h1 = False; self._h1buf = ""
        self.jsonld = []; self._ld = False; self._ldbuf = ""
        self.lang = None; self.text = []; self._skip = 0; self.refresh = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = a.get("lang")
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

    pages, redirects, noindex = {}, set(), set()
    titles, descs = collections.defaultdict(list), collections.defaultdict(list)
    for dp, _, fns in os.walk(root):
        for fn in fns:
            if not fn.endswith(".html"): continue
            path = os.path.join(dp, fn)
            src = open(path, encoding="utf-8", errors="replace").read()
            p = Page(); p.feed(src)
            url = url_for(path)
            if p.refresh: redirects.add(url); continue
            if url.endswith(("/google9835ba948bb89980.html", "/yandex_ad81e17bf10db464.html")): continue
            meta = {}
            for m in p.metas:
                k = m.get("name") or m.get("property")
                if k and k not in meta: meta[k] = m.get("content") or ""
            robots = meta.get("robots", "")
            is_noindex = "noindex" in robots
            if is_noindex: noindex.add(url)
            pages[url] = p
            title = (p.title or "").strip(); desc = meta.get("description", "")
            if not title: err("title missing", url)
            else:
                titles[title].append(url)
                if len(title) > 65: warn("title > 65 chars", url, f"{len(title)}: {title}")
            if not desc: err("meta description missing", url)
            else:
                descs[desc].append(url)
                if desc.startswith(GENERIC_DESC) and url != SITE + "/":
                    err("generic site tagline used as description (add seo.description)", url)
                if len(desc) > 165: warn("description > 165 chars", url, str(len(desc)))
                if len(desc) < 70: warn("description < 70 chars", url, desc)
            canon = [l.get("href") for l in p.links if l.get("rel") == "canonical"]
            if not is_noindex:
                if len(canon) != 1: err("canonical count != 1", url, str(canon))
                elif canon[0] != url: err("canonical does not match URL", url, canon[0])
            if len(p.h1) != 1: err("H1 count != 1", url, str(p.h1[:3]))
            if p.lang != "en": err("html lang missing", url)
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
                if not resolve(h): err("broken internal link", url, h)
            for im in p.imgs:
                if im.get("alt") is None: warn("img without alt", url, im.get("src"))
                s = im.get("src") or ""
                if s.startswith(("/", SITE)) and not resolve(s): err("image 404", url, s)

    for t, us in titles.items():
        if len(us) > 1: warn("duplicate title", us[0], f"{t} (also {', '.join(u.replace(SITE, '') for u in us[1:])})")
    for d, us in descs.items():
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
        if n > 0.8 * len(s1): err("sitemap lastmod is the same for >80% of URLs (looks like a build stamp)", "sitemap.xml", f"{top} x{n}")
    for u, v in s1.items():
        if not v and u in indexable: warn("sitemap URL without lastmod (set last_updated)", u)

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
