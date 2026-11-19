#!/usr/bin/env python3
"""
Build _data/sale.json (the Black Friday 2026 offer-code sale) from the App Store Connect read-back.

Source: prices_by_country.csv in ~/Downloads/BlackFriday2026/ (outside the repo). It holds, for every product and
every territory, the regular price and the offer-code price that App Store Connect returned from
/v1/inAppPurchaseOfferCodes/{id}/prices after the offers were created (2026-11-19). Nothing here is typed by hand
except the sale's dates, code and the app list, which come from that folder's HANDOFF.md.

The site shows sale prices only through _includes/sale.html, which reads this file in the page's territory.
The regular price in this file must equal the catalog's (_data/catalog.json) for every site territory, or the
script stops: a mismatch means App Store Connect prices changed after the sale was set up.

Also renders a redeem QR per app to assets/qr/bf/<slug>.svg (desktop visitors scan it with their iPhone).

Usage: python3 scripts/build-sale-data.py [path/to/prices_by_country.csv]
"""
import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import segno
import yaml

ROOT = Path(__file__).resolve().parent.parent
CSV = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Downloads/BlackFriday2026/prices_by_country.csv"

CODE = "BLACKFRIDAY2026"
SALE = {
    "id": "black-friday-2026",
    "code": CODE,
    "percent": 50,
    "starts": "2026-11-19",
    "weekend": "2026-11-27",          # Black Friday: the ribbon switches to its weekend line
    "last_day": "2026-11-30",         # Cyber Monday: last full day the site promises
    # The code's expirationDate in App Store Connect is 2026-12-01. Sale elements hide at the visitor's local
    # midnight after the last day, and at this instant at the latest (00:00 Pacific on Dec 1).
    "hide_after_utc": "2026-12-01T08:00:00Z",
}

# site slug -> product id in the CSV (HANDOFF.md, "Apps, products and IDs"). Clippet is left out on purpose.
PRODUCTS = {
    "observa": "carlosdeketkuli.observa.pro.lifetime",
    "aftershift": "carlosdeketkuli.aftershift.lifetime",
    "pawza": "petcare.pro.lifetime",
    "taskful-day": "daskfulday.pro.lifetime",
    "mediakit": "carlosdeketkuli.clearcut.lifetime",
    "gymlogger-x": "com.carlos.gymloggerx.pro.lifetime",
    "appmeta": "appmeta.pro.lifetime",
    "chessful": "carlosdeketkuli.chessful.lifetime",
    "allpaid": "allpaid.pro.lifetime",
    "wanderwiki": "carlosdeketkuli.wanderwiki.lifetime",
    "shogiful": "carlosdeketkuli.shogiful.lifetime",
    "xiangqiful": "carlosdeketkuli.xiangqiful.lifetime",
    "earnlock": "earnscreen.premium.lifetime",
    "appmeta-pulse": "carlosdeketkuli.pulse.lifetime",
    "soon": "thewait.premium.lifetime",
    "rightsplit": "rightsplit.proplus.lifetime",
    "tare": "carlosdeketkuli.tare.fullaccess",
    "millrace": "carlosdeketkuli.millrace.themes.complete",
}
# Products sold as an "other IAP" in the catalog rather than a lifetime plan: the catalog label.
IAP_LABEL = {"tare": "Tare Full Access", "millrace": "Millrace Complete Collection"}


def front_matter(path):
    m = re.match(r"^---\n(.*?)\n---", path.read_text(encoding="utf-8"), re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def main():
    cat = json.load(open(ROOT / "_data/catalog.json", encoding="utf-8"))
    terrs = [t["code"] for t in cat["meta"]["territories"]]
    rows = {}
    for r in csv.DictReader(open(CSV, encoding="utf-8")):
        rows.setdefault(r["product_id"], {})[r["territory"]] = r

    hide = datetime.strptime(SALE["hide_after_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    out = dict(SALE, hide_after_epoch=int(hide.timestamp()),
               source="App Store Connect offer-code prices, read back 2026-11-19", apps={})
    problems = []
    qr_dir = ROOT / "assets/qr/bf"
    qr_dir.mkdir(parents=True, exist_ok=True)

    for slug, pid in PRODUCTS.items():
        app = cat["apps"][slug]
        fm = front_matter(ROOT / "_apps" / f"{slug}.md")
        app_id = re.search(r"id(\d+)", fm["app_store_url"]).group(1)
        if slug in IAP_LABEL:
            prod = next(o for o in app["other_iaps"] if o["label"] == IAP_LABEL[slug])
            token = "{P_IAP:" + IAP_LABEL[slug] + "}"
            plan_index = next((i for i, p in enumerate(fm.get("plans") or []) if token in str(p.get("price", ""))), None)
        else:
            prod = app["plans"]["lifetime"]
            plan_index = next((i for i, p in enumerate(fm.get("plans") or []) if p.get("kind") == "lifetime"
                               or "{P_LIFETIME}" in str(p.get("price", ""))), None)
        prices = {}
        for t in terrs:
            r = rows[pid].get(t)
            if not r:
                problems.append(f"{slug}: no sale row for {t}")
                continue
            cp = prod["prices"].get(t)
            if not cp or float(cp["amount"]) != float(r["regular_price"]):
                problems.append(f"{slug} {t}: catalog {cp and cp['amount']} != read-back regular {r['regular_price']}")
            prices[t] = {"currency": cp["currency"] if cp else None, "regular": cp["amount"] if cp else r["regular_price"],
                         "sale": r["sale_price"]}
        redeem = f"https://apps.apple.com/redeem?ctx=offercodes&id={app_id}&code={CODE}"
        plats = app.get("platforms") or []
        out["apps"][slug] = {
            "app_id": app_id,
            "iap_label": IAP_LABEL.get(slug),
            "plan_index": plan_index,
            "family_sharing": bool(prod.get("family_sharing")),
            "iphone": "iOS" in plats,
            "redeem_url": redeem,
            "prices": prices,
        }
        segno.make(redeem, error="m").save(str(qr_dir / f"{slug}.svg"), scale=4, border=2, dark="#0B0E22", light="#FFFFFF")

    if problems:
        sys.exit("Sale data NOT written:\n  " + "\n  ".join(problems))
    out["count"] = len(out["apps"])
    (ROOT / "_data/sale.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"_data/sale.json: {out['count']} apps x {len(terrs)} territories; QR codes in assets/qr/bf/")


if __name__ == "__main__":
    main()
