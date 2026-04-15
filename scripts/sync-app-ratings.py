#!/usr/bin/env python3
"""
Sync App Store ratings from Apple's iTunes Lookup API into each app's
frontmatter. Queries every major Apple storefront in parallel and
aggregates into a weighted global average — because Apple's API
returns per-storefront ratings, not a single global number.

Usage:
    python3 scripts/sync-app-ratings.py            # aggregate across all default regions
    python3 scripts/sync-app-ratings.py --dry-run  # show what would change
    python3 scripts/sync-app-ratings.py --verbose  # per-region breakdown
    python3 scripts/sync-app-ratings.py --regions us,gb,fi  # limit regions

The default region list covers 37 Apple storefronts spanning North
America, Europe, Nordics, LATAM, Asia-Pacific, and the Middle East —
together this captures >95% of global iOS user base for a typical
indie app. Run with --verbose to see which regions contributed.

Jekyll cannot make HTTP requests at build time on GitHub Pages safe
mode, so rating data must be baked into source frontmatter before
deploy. Run this script, commit, push.
"""

import argparse
import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
APPS_DIR = REPO_ROOT / "_apps"
APP_ID_RE = re.compile(r"id(\d+)")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

DEFAULT_REGIONS = [
    "us", "gb", "ca", "au", "de", "fr", "it", "es", "nl",
    "fi", "se", "dk", "no", "is",
    "jp", "cn", "kr", "tw", "hk", "sg", "th", "my", "id", "ph", "vn", "in",
    "br", "mx", "cl", "ar", "co",
    "be", "ch", "at", "pt", "ie", "lu",
    "pl", "cz", "hu", "ro", "gr", "tr",
    "ru", "ua",
    "ae", "sa", "il", "za", "eg",
    "nz",
]


def extract_app_id(path: Path):
    text = path.read_text()
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    for line in m.group(1).splitlines():
        if line.startswith("app_store_url:"):
            match = APP_ID_RE.search(line)
            if match:
                return match.group(1)
    return None


def fetch_region(region: str, ids: list) -> tuple:
    """Return (region, {app_id: {value, count}}). Silent on network errors."""
    url = f"https://itunes.apple.com/{region}/lookup?id={','.join(ids)}"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.load(resp)
    except Exception:
        return region, {}
    out = {}
    for r in data.get("results", []):
        tid = str(r.get("trackId"))
        count = int(r.get("userRatingCount") or 0)
        if count > 0:
            out[tid] = {
                "value": float(r.get("averageUserRating") or 0),
                "count": count,
            }
    return region, out


def aggregate(per_region: dict, app_ids: list) -> dict:
    """Weighted average across regions → global rating per app."""
    result = {}
    for app_id in app_ids:
        total_count = 0
        weighted_sum = 0.0
        contributing = []
        for region, region_data in per_region.items():
            if app_id not in region_data:
                continue
            r = region_data[app_id]
            weighted_sum += r["value"] * r["count"]
            total_count += r["count"]
            contributing.append((region, r["value"], r["count"]))
        if total_count > 0:
            result[app_id] = {
                "value": round(weighted_sum / total_count, 1),
                "count": total_count,
                "contributing": contributing,
            }
    return result


def parse_existing(fm: str):
    m = re.search(r"\nratings:\n((?:  .*\n?)+)", fm)
    if not m:
        return None
    block = m.group(1)
    value_m = re.search(r'value:\s*"?([\d.]+)"?', block)
    count_m = re.search(r"count:\s*(\d+)", block)
    if not value_m or not count_m:
        return None
    return {"value": round(float(value_m.group(1)), 1), "count": int(count_m.group(1))}


def update_frontmatter(path: Path, rating: dict, dry_run: bool) -> str:
    text = path.read_text()
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "malformed"

    fm = m.group(1)
    today = date.today().isoformat()
    new_block = (
        f"ratings:\n"
        f'  value: "{rating["value"]}"\n'
        f'  count: {rating["count"]}\n'
        f'  last_synced: "{today}"'
    )

    old_rating = parse_existing(fm)
    if old_rating and old_rating["value"] == rating["value"] and old_rating["count"] == rating["count"]:
        return "unchanged"

    ratings_block_re = re.compile(r"\nratings:\n(?:  .*\n?)+")
    if ratings_block_re.search(fm):
        new_fm = ratings_block_re.sub("\n" + new_block, fm).rstrip()
    else:
        new_fm = fm.rstrip() + "\n\n" + new_block

    if dry_run:
        return "updated"

    new_text = "---\n" + new_fm + "\n---\n" + text[m.end():]
    path.write_text(new_text)
    return "updated"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", "-v", action="store_true", help="show per-region breakdown")
    parser.add_argument("--regions", help=f"comma-separated storefront codes (default: {len(DEFAULT_REGIONS)} regions)")
    parser.add_argument("--workers", type=int, default=12, help="parallel API workers")
    args = parser.parse_args()

    regions = args.regions.split(",") if args.regions else DEFAULT_REGIONS

    app_files = sorted(APPS_DIR.glob("*.md"))
    id_to_path = {}
    for path in app_files:
        app_id = extract_app_id(path)
        if app_id:
            id_to_path[app_id] = path

    if not id_to_path:
        print("No app_store_url IDs found in _apps/*.md", file=sys.stderr)
        return 1

    print(f"Querying {len(regions)} Apple storefronts for {len(id_to_path)} apps...")
    per_region = {}
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = {ex.submit(fetch_region, r, list(id_to_path.keys())): r for r in regions}
        for fut in as_completed(futures):
            region, data = fut.result()
            per_region[region] = data

    hits = sum(len(v) for v in per_region.values())
    contributing = sum(1 for v in per_region.values() if v)
    print(f"Got {hits} rating hits from {contributing} contributing regions.\n")

    aggregated = aggregate(per_region, list(id_to_path.keys()))

    updated = unchanged = zero = 0
    for app_id, path in sorted(id_to_path.items(), key=lambda x: x[1].name):
        rating = aggregated.get(app_id)
        if rating is None:
            print(f"  [zero]  {path.name:<30}  (0 ratings across all {len(regions)} storefronts)")
            zero += 1
            continue
        status = update_frontmatter(path, rating, args.dry_run)
        marker = "[would]" if args.dry_run and status == "updated" else f"[{status}]"
        print(f"  {marker} {path.name:<30}  global: {rating['value']:.1f} stars, {rating['count']} ratings")
        if args.verbose:
            for region, val, cnt in sorted(rating["contributing"], key=lambda x: -x[2]):
                print(f"          └── {region}: {val:.1f} × {cnt}")
        if status == "updated":
            updated += 1
        elif status == "unchanged":
            unchanged += 1

    print()
    print(f"Summary: {updated} updated, {unchanged} unchanged, {zero} with zero ratings")
    if args.dry_run:
        print("Dry run — no files were written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
