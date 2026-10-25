#!/usr/bin/env python3
"""Set the top-level `last_updated: YYYY-MM-DD` front-matter field on site pages.

`last_updated` drives <lastmod> in sitemap.xml / ai-sitemap.xml, the
`dateModified` in JSON-LD and (on journal posts) the visible "Updated" date.
Search engines only trust lastmod when it moves on real edits, so stamp
every page you change, and only those.

Usage (run from the repo root):
  python3 scripts/stamp-last-updated.py --changed          # files changed vs HEAD (staged + unstaged + untracked)
  python3 scripts/stamp-last-updated.py FILE [FILE ...]    # explicit files, stamped with today's date
  python3 scripts/stamp-last-updated.py --backfill         # pages with no last_updated get their last git commit date
  add --date YYYY-MM-DD to force a date, --dry-run to only print.

Never touched: privacy pages (their last_updated is the policy's effective
date; change it by hand when the policy text changes), files without front
matter, and anything outside the content folders below.
"""
import argparse, datetime, os, re, subprocess, sys

CONTENT_DIRS = ("_apps/", "_journal/", "alternatives/", "guides/", "for/",
                "apps/", "journal/", "lagerland-apps/", "transparency/", "support/")
BOT_PREFIX = "Sync App Store ratings"


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def is_content(path):
    if not (path.endswith(".html") or path.endswith(".md")):
        return False
    return path == "index.html" or path.startswith(CONTENT_DIRS)


def last_commit_date(path):
    """Date of the newest commit touching `path`, ignoring the ratings bot."""
    for line in git("log", "--format=%cs%x09%s", "--", path).splitlines():
        date, _, subject = line.partition("\t")
        if not subject.startswith(BOT_PREFIX):
            return date
    return None


def split_front_matter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    return text[4:end + 1], text[end + 1:]


def stamp(path, date, only_if_missing=False, dry=False):
    text = open(path, encoding="utf-8").read()
    parts = split_front_matter(text)
    if not parts:
        return "skip (no front matter)"
    fm, rest = parts
    if re.search(r"^layout:\s*privacy\s*$", fm, re.M):
        return "skip (privacy policy date is set by hand)"
    has = re.search(r"^last_updated:.*$", fm, re.M)
    if has and only_if_missing:
        return "skip (already has last_updated)"
    line = f"last_updated: {date}"
    if has:
        if has.group(0).strip() == line:
            return "unchanged"
        fm = fm[:has.start()] + line + fm[has.end():]
    else:
        fm = fm + line + "\n"
    if not dry:
        open(path, "w", encoding="utf-8").write("---\n" + fm + rest)
    return f"-> {date}"


def changed_files():
    files = []
    for line in git("status", "--porcelain", "--untracked-files=all").splitlines():
        status, path = line[:2], line[3:]
        if "D" in status:
            continue
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        files.append(path.strip('"'))
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--changed", action="store_true")
    ap.add_argument("--backfill", action="store_true")
    ap.add_argument("--date")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    today = a.date or datetime.date.today().isoformat()

    if a.backfill:
        for p in sorted(git("ls-files").splitlines()):
            if not is_content(p) or p.startswith("_journal/"):
                continue  # journal posts fall back to `date`; bump them when you edit them
            d = a.date or last_commit_date(p)
            if d:
                print(f"{p}: {stamp(p, d, only_if_missing=True, dry=a.dry_run)}")
        return 0
    files = a.files or (changed_files() if a.changed else [])
    if not files:
        ap.error("give files, --changed or --backfill")
    for p in files:
        if os.path.isfile(p) and is_content(p):
            print(f"{p}: {stamp(p, today, dry=a.dry_run)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
