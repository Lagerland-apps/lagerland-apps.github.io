#!/usr/bin/env python3
"""
Generate an App Store "scan to install" QR code for every app.

For each `_apps/<slug>.md` it reads `app_store_url` from the front matter and
renders a crisp, dark-on-white SVG QR to `assets/qr/<slug>.svg`. The codes are
dark modules on an opaque white background (with a quiet zone) so they scan
reliably regardless of the surrounding light/dark theme on the page.

These are static assets committed to the repo — GitHub Pages builds without
custom plugins, so the QR must exist at commit time, exactly like the OG cards.

Usage:
    python3 scripts/generate-qr.py                 # all apps
    python3 scripts/generate-qr.py --only observa   # a subset
    python3 scripts/generate-qr.py --dry-run       # list what would render
"""

import argparse
import re
import sys
from pathlib import Path

import segno
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
APPS_DIR = REPO_ROOT / "_apps"
QR_DIR = REPO_ROOT / "assets" / "qr"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

# Dark-on-white keeps the code scannable on any page background. The dark tone
# matches the site's --bg-0 rather than pure black so it reads as intentional.
DARK = "#0B0E22"
LIGHT = "#FFFFFF"


def read_front_matter(md_path):
    text = md_path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="Only render these slugs")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    QR_DIR.mkdir(parents=True, exist_ok=True)

    rendered, skipped = 0, 0
    for md_path in sorted(APPS_DIR.glob("*.md")):
        slug = md_path.stem
        if args.only and slug not in args.only:
            continue

        fm = read_front_matter(md_path)
        if not fm:
            print(f"  skip {slug}: no front matter", file=sys.stderr)
            skipped += 1
            continue

        url = fm.get("app_store_url")
        if not url:
            print(f"  skip {slug}: no app_store_url", file=sys.stderr)
            skipped += 1
            continue

        out = QR_DIR / f"{slug}.svg"
        if args.dry_run:
            print(f"  would render {out.relative_to(REPO_ROOT)}  ->  {url}")
            continue

        # ecc="m" (~15%) is the sweet spot for a URL this short: dense enough to
        # stay small, robust enough to scan off a screen. border=3 = quiet zone.
        qr = segno.make(url, error="m")
        qr.save(
            str(out),
            kind="svg",
            scale=1,
            border=3,
            dark=DARK,
            light=LIGHT,
            svgclass=None,
            lineclass=None,
            omitsize=True,          # no fixed width/height — CSS scales it
            svgns=True,
        )
        print(f"  rendered {out.relative_to(REPO_ROOT)}")
        rendered += 1

    print(f"\nDone. {rendered} rendered, {skipped} skipped.")


if __name__ == "__main__":
    main()
