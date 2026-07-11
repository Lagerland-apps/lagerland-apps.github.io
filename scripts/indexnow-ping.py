#!/usr/bin/env python3
"""
Ping IndexNow so Bing, Yandex, Seznam, Naver, and other participating
search engines re-crawl changed pages within minutes instead of waiting
for their normal crawl cycle. A single submission to the aggregator
endpoint (api.indexnow.org) is shared to every participating engine, so
this covers Bing (and therefore DuckDuckGo, Ecosia, and Copilot/ChatGPT
search, which lean on Bing's index) plus Yandex in one call.

IndexNow authenticates via a public key file served at the site root.
This repo ships it as `<key>.txt` (committed, because the key is public
by design — it only proves you control the host). GitHub Pages serves it
as text/plain, which is all IndexNow's validation needs. The key file
must already be live before the first ping, or the API returns 403.

No third-party dependencies — standard library only, like the other
scripts here. Jekyll cannot make HTTP calls at build time on GitHub
Pages, so this runs after deploy (locally as part of the publish loop, or
from the IndexNow GitHub Action).

Usage:
    # Submit only pages whose SOURCE changed in the last commit (the
    # normal "I just published" hook). Maps changed source files to their
    # live permalinks; a change to a shared layout/include/config/data
    # file is treated as sitewide and submits the whole sitemap.
    python3 scripts/indexnow-ping.py --changed

    # Submit changes since an arbitrary git ref (e.g. what a push added)
    python3 scripts/indexnow-ping.py --changed origin/main

    # Submit specific URLs (absolute, or site-relative starting with /)
    python3 scripts/indexnow-ping.py /apps/observa/ /journal/apple-watch-hrv-without-a-baseline/

    # Submit EVERY live URL from the sitemap. Use sparingly — after a
    # sitewide refresh, not routinely; engines discourage resubmitting
    # unchanged URLs.
    python3 scripts/indexnow-ping.py --all

    # Preview the exact URL list without calling the API
    python3 scripts/indexnow-ping.py --changed --dry-run
    python3 scripts/indexnow-ping.py --all --verbose
"""

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

HOST = "lagerland-apps.github.io"
SITE_URL = f"https://{HOST}"
KEY = "2d7ad1f04403b09927998f4df4528f37"
KEY_LOCATION = f"{SITE_URL}/{KEY}.txt"
# Aggregator endpoint: forwards the submission to every participating
# engine, so we don't have to ping Bing and Yandex separately.
ENDPOINT = "https://api.indexnow.org/indexnow"
SITEMAP_URL = f"{SITE_URL}/sitemap.xml"
LOCAL_SITEMAP = REPO_ROOT / "_site" / "sitemap.xml"
# IndexNow accepts at most 10,000 URLs per request.
MAX_URLS_PER_REQUEST = 10000
TIMEOUT = 30

# A change to any of these shared, content-affecting files can alter the
# rendered HTML/text of many or all pages, so a changed-file run submits
# the whole sitemap. Pure-styling dirs (_sass, assets/css, assets/js) are
# deliberately NOT here: a CSS/JS-only change doesn't alter crawlable
# text, and IndexNow discourages resubmitting text-unchanged URLs. This
# list is kept in sync with the path filter in .github/workflows/indexnow.yml.
GLOBAL_TRIGGERS = (
    "_config.yml",
    "_includes/",
    "_layouts/",
    "_data/",
)

# Source files that never correspond to a crawlable HTML page.
SKIP_PREFIXES = ("scripts/", "_site/", ".github/", "assets/", ".well-known/")
SKIP_EXACT = {
    "README.md", "CLAUDE.md", "robots.txt", "feed.xml", "humans.txt",
    "llms.txt", "llms-full.txt", "ai-index.json", "ai-sitemap.xml",
    "sitemap.xml", "sitemap_index.xml", "404.html", ".gitignore",
    # Search Console verification token — a real 200 page but never
    # indexable (config sets sitemap:false, and it has no front matter of
    # its own to detect). It's the one file that would otherwise reach the
    # extension-preserving fallback below.
    "google9835ba948bb89980.html",
}
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
PERMALINK_RE = re.compile(r"^permalink:\s*[\"']?(/[^\"'\n]*)", re.MULTILINE)
SITEMAP_FALSE_RE = re.compile(r"^sitemap:\s*false\b", re.MULTILINE)


def read_frontmatter(rel_path):
    """Return a page's raw YAML front-matter block, or None if it has none."""
    try:
        head = (REPO_ROOT / rel_path).read_text(encoding="utf-8", errors="ignore")[:8192]
    except OSError:
        return None
    if not head.startswith("---"):
        return None
    block = FRONTMATTER_RE.match(head)
    return block.group(1) if block else head


def path_to_url(rel_path):
    """Map a repo-relative source path to its live URL, or None if the
    file does not produce a standalone, indexable page.

    Handles the collections and permalink conventions this site uses:
    `_apps/<slug>.md` -> /apps/<slug>/, `_journal/<slug>.md` ->
    /journal/<slug>/, any page with an explicit `permalink:`
    (alternatives/for/guides all set one), and `index.html` files. Pages
    whose front matter sets `sitemap: false` are treated as deliberately
    excluded and return None. The fallback keeps the `.html` extension
    because the site configures no site-wide pretty permalink — that is
    Jekyll's actual default.
    """
    rel_path = rel_path.strip()
    if not rel_path or rel_path in SKIP_EXACT:
        return None
    if any(rel_path.startswith(p) for p in SKIP_PREFIXES):
        return None
    if not (rel_path.endswith(".html") or rel_path.endswith(".md")):
        return None

    fm = read_frontmatter(rel_path)
    if fm and SITEMAP_FALSE_RE.search(fm):
        return None  # deliberately kept out of the index

    if fm:
        permalink = PERMALINK_RE.search(fm)
        if permalink:
            return SITE_URL + permalink.group(1).strip()

    if rel_path.startswith("_apps/") and rel_path.endswith(".md"):
        return f"{SITE_URL}/apps/{Path(rel_path).stem}/"
    if rel_path.startswith("_journal/") and rel_path.endswith(".md"):
        return f"{SITE_URL}/journal/{Path(rel_path).stem}/"
    if rel_path == "index.html":
        return f"{SITE_URL}/"
    if rel_path.endswith("/index.html"):
        return f"{SITE_URL}/{rel_path[:-len('index.html')]}"
    # No explicit permalink and not in a collection: Jekyll's default
    # keeps the extension (the site sets no `permalink: pretty`).
    return f"{SITE_URL}/{rel_path.rsplit('.', 1)[0]}.html"


def git_changed_files(base_ref):
    """(files, used_ref) changed between a base ref and HEAD, excluding
    deletions — a removed page has no content to crawl (submitting a URL
    for de-indexing is a separate, deliberate action). Falls back to the
    last commit when the ref is missing/invalid: a first push whose
    `before` SHA is all zeros, an unfetched SHA, or a manual
    workflow_dispatch run (which passes an empty ref)."""
    zero = re.fullmatch(r"0{40}", base_ref or "")
    candidates = [] if (not base_ref or zero) else [base_ref]
    candidates.append("HEAD~1")
    for ref in candidates:
        try:
            out = subprocess.run(
                ["git", "-C", str(REPO_ROOT), "diff", "--name-only",
                 "--diff-filter=ACMR", ref, "HEAD"],
                capture_output=True, text=True, check=True,
            ).stdout
            return [line for line in out.splitlines() if line.strip()], ref
        except (subprocess.CalledProcessError, FileNotFoundError, OSError):
            continue
    print("ERROR: could not compute a git diff (no valid base ref, no HEAD~1).",
          file=sys.stderr)
    print("       Pass an explicit ref: --changed <ref>, or use --all.",
          file=sys.stderr)
    sys.exit(2)


def parse_sitemap(text):
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", text)


def load_sitemap():
    """Live sitemap first (authoritative for what's actually published);
    fall back to a local _site build if the network fetch fails."""
    try:
        with urllib.request.urlopen(SITEMAP_URL, timeout=TIMEOUT) as resp:
            urls = parse_sitemap(resp.read().decode("utf-8", "ignore"))
            if urls:
                return urls
    except (urllib.error.URLError, OSError) as exc:
        print(f"WARNING: could not fetch live sitemap ({exc}); trying {LOCAL_SITEMAP}",
              file=sys.stderr)
    if LOCAL_SITEMAP.exists():
        return parse_sitemap(LOCAL_SITEMAP.read_text(encoding="utf-8", errors="ignore"))
    print("ERROR: no sitemap available (live fetch failed and no local _site build).",
          file=sys.stderr)
    sys.exit(2)


def normalize_url(raw):
    """Accept absolute same-host URLs or site-relative paths; reject
    anything on another host (IndexNow rejects cross-host URLs)."""
    raw = raw.strip()
    if not raw:
        return None
    if raw.startswith("/"):
        return SITE_URL + raw
    if raw.startswith(f"{SITE_URL}/") or raw == SITE_URL:
        return raw
    if raw.startswith("http://") or raw.startswith("https://"):
        print(f"WARNING: skipping cross-host URL (not on {HOST}): {raw}", file=sys.stderr)
        return None
    # Bare path like "apps/observa/"
    return f"{SITE_URL}/{raw.lstrip('/')}"


def dedupe(urls):
    seen, out = set(), []
    for url in urls:
        if url and url not in seen:
            seen.add(url)
            out.append(url)
    return out


def collect_changed_urls(base_ref, verbose):
    files, used_ref = git_changed_files(base_ref)
    if verbose:
        print(f"Changed files ({len(files)}) since {used_ref}:")
        for f in files:
            print(f"  {f}")
    triggered = [f for f in files if any(f == t or f.startswith(t) for t in GLOBAL_TRIGGERS)]
    if triggered:
        print(f"Sitewide change detected ({triggered[0]} ...) — submitting the full sitemap.")
        return load_sitemap()
    urls = [u for u in (path_to_url(f) for f in files) if u]
    return dedupe(urls)


def submit(urls, dry_run, verbose):
    urls = dedupe(urls)
    if not urls:
        print("Nothing to submit.")
        return 0
    print(f"{'Would submit' if dry_run else 'Submitting'} {len(urls)} URL(s) "
          f"to IndexNow via {ENDPOINT}:")
    if dry_run or verbose:
        for url in urls:
            print(f"  {url}")

    failures = 0
    for start in range(0, len(urls), MAX_URLS_PER_REQUEST):
        chunk = urls[start:start + MAX_URLS_PER_REQUEST]
        payload = {
            "host": HOST,
            "key": KEY,
            "keyLocation": KEY_LOCATION,
            "urlList": chunk,
        }
        if dry_run:
            continue
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            ENDPOINT, data=data, method="POST",
            headers={"Content-Type": "application/json; charset=utf-8"},
        )
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                print(f"  -> {resp.status} {_explain(resp.status)} ({len(chunk)} URLs)")
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "ignore").strip()
            print(f"  -> {exc.code} {_explain(exc.code)} ({len(chunk)} URLs)"
                  + (f" — {body}" if body else ""), file=sys.stderr)
            failures += 1
        except urllib.error.URLError as exc:
            print(f"  -> network error: {exc}", file=sys.stderr)
            failures += 1
    return failures


def _explain(code):
    return {
        200: "OK — submitted",
        202: "Accepted — received, key validation pending",
        400: "Bad request — invalid URL/JSON format",
        403: "Forbidden — key not found or invalid at keyLocation",
        422: "Unprocessable — URL host mismatch or key mismatch",
        429: "Too many requests — slow down",
    }.get(code, "unexpected status")


def main():
    parser = argparse.ArgumentParser(
        description="Ping IndexNow (Bing/Yandex/etc.) for changed or specific URLs.")
    parser.add_argument("urls", nargs="*",
                        help="Explicit URLs (absolute or site-relative /path/).")
    parser.add_argument("--changed", nargs="?", const="", metavar="REF",
                        help="Submit pages changed since REF (default: the last commit).")
    parser.add_argument("--all", action="store_true",
                        help="Submit every live URL from the sitemap (use sparingly).")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be submitted without calling the API.")
    parser.add_argument("--verbose", action="store_true",
                        help="List every URL and changed file.")
    args = parser.parse_args()

    modes = sum([args.changed is not None, args.all, bool(args.urls)])
    if modes == 0:
        parser.error("choose one of: --changed [REF], --all, or explicit URLs.")
    if modes > 1:
        parser.error("--changed, --all, and explicit URLs are mutually exclusive.")

    if args.all:
        urls = load_sitemap()
    elif args.changed is not None:
        urls = collect_changed_urls(args.changed, args.verbose)
    else:
        urls = [u for u in (normalize_url(u) for u in args.urls) if u]

    failures = submit(urls, args.dry_run, args.verbose)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
