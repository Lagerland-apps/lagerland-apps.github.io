#!/usr/bin/env python3
"""
Lagerland notifier — polls Apple for new reviews and IAP events, pushes
alerts to a Telegram chat. Designed to run from launchd every 5 minutes
on a personal Mac. All secrets and state stay local to the machine.

Reads:
    ~/lagerland-notifier/config.json          API keys, bot token, apps
    ~/lagerland-notifier/state.json           per-app last-seen markers
    ~/lagerland-notifier/keys/AuthKey_*.p8    Apple private key

Writes:
    ~/lagerland-notifier/state.json           updated after each successful cycle
    ~/lagerland-notifier/logs/notifier.log    rotating script log

Usage:
    python3 scripts/notifier.py                 one poll cycle
    python3 scripts/notifier.py --dry-run       simulate; no sends, no state writes
    python3 scripts/notifier.py --verbose       debug-level logging
    python3 scripts/notifier.py --test-telegram send one test message and exit

First run per app is "mark as seen" — existing reviews/IAPs are NOT
replayed. You only get alerts for events that happen after the first
successful poll.
"""

import argparse
import base64
import json
import logging
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

try:
    import jwt  # PyJWT
except ImportError:
    sys.exit("Missing dependency: pip3 install --user 'pyjwt[crypto]'")


BASE = Path(os.environ.get("LAGERLAND_NOTIFIER_HOME", Path.home() / "lagerland-notifier"))
CONFIG_PATH = BASE / "config.json"
STATE_PATH = BASE / "state.json"
LOG_PATH = BASE / "logs" / "notifier.log"

APP_STORE_CONNECT = "https://api.appstoreconnect.apple.com"
APP_STORE_SERVER = "https://api.storekit.itunes.apple.com"

logger = logging.getLogger("notifier")


# ---------------------------------------------------------------------------
# io / config / state
# ---------------------------------------------------------------------------

def setup_logging(verbose: bool) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(message)s",
        handlers=[
            logging.FileHandler(LOG_PATH),
            logging.StreamHandler(sys.stdout),
        ],
    )


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        sys.exit(
            f"No config at {CONFIG_PATH}. "
            "See the setup steps printed when the notifier was installed."
        )
    with open(CONFIG_PATH) as f:
        return json.load(f)


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"apps": {}}
    with open(STATE_PATH) as f:
        return json.load(f)


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(state, f, indent=2, sort_keys=True)
    tmp.replace(STATE_PATH)


# ---------------------------------------------------------------------------
# apple auth + http
# ---------------------------------------------------------------------------

def make_jwt(key_path: str, key_id: str, issuer_id: str, *, bundle_id: str = None, lifetime: int = 1200) -> str:
    """ES256-sign a JWT for Apple APIs. bundle_id is required for the
    App Store Server API; it must be omitted for App Store Connect calls."""
    resolved = Path(key_path).expanduser()
    with open(resolved) as f:
        private_key = f.read()
    now = int(time.time())
    claims = {
        "iss": issuer_id,
        "iat": now,
        "exp": now + lifetime,
        "aud": "appstoreconnect-v1",
    }
    if bundle_id:
        claims["bid"] = bundle_id
    return jwt.encode(
        claims, private_key, algorithm="ES256",
        headers={"kid": key_id, "typ": "JWT"},
    )


def http(url: str, bearer: str, *, method: str = "GET", body: dict = None) -> tuple:
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Bearer {bearer}")
    req.add_header("User-Agent", "lagerland-notifier/1.0")
    if body is not None:
        req.add_header("Content-Type", "application/json")
        req.data = json.dumps(body).encode()
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            raw = resp.read()
            return resp.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, {"raw": raw.decode(errors="replace")[:400]}
    except urllib.error.URLError as e:
        return 0, {"error": str(e)}


# ---------------------------------------------------------------------------
# reviews — App Store Connect API
# ---------------------------------------------------------------------------

def poll_reviews(app: dict, token: str, app_state: dict) -> list:
    app_name = app["name"]
    app_id = app["app_id"]
    last_seen = app_state.get("last_review_id")
    url = f"{APP_STORE_CONNECT}/v1/apps/{app_id}/customerReviews?sort=-createdDate&limit=20"
    status, data = http(url, token)
    if status != 200:
        logger.warning("reviews poll failed for %s: %s %s", app_name, status, data)
        return []
    items = data.get("data", [])
    if not items:
        return []
    if last_seen is None:
        # Seed run: record newest, don't replay history.
        app_state["last_review_id"] = items[0]["id"]
        logger.info("reviews: seeded %s — %d existing marked as already seen", app_name, len(items))
        return []
    new = []
    for item in items:
        if item["id"] == last_seen:
            break
        new.append(item)
    if new:
        app_state["last_review_id"] = new[0]["id"]
        logger.info("reviews: %d new on %s", len(new), app_name)
    # Oldest first so notifications arrive in the order they were written.
    return list(reversed(new))


def format_review(app_name: str, review: dict) -> str:
    a = review.get("attributes", {})
    rating = int(a.get("rating") or 0)
    stars = "★" * rating + "☆" * (5 - rating)
    title = (a.get("title") or "").strip() or "(no title)"
    body = (a.get("body") or "").strip()
    author = (a.get("reviewerNickname") or "?").strip()
    territory = a.get("territory") or ""
    when = (a.get("createdDate") or "")[:19].replace("T", " ")

    def esc(s):
        return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    body_trim = body[:900] + (" …" if len(body) > 900 else "")
    head = f"<b>{stars}</b>  New review · <b>{esc(app_name)}</b>"
    if territory:
        head += f" · <code>{esc(territory)}</code>"
    return (
        f"{head}\n"
        f"<i>by {esc(author)}</i>\n"
        f"<b>{esc(title)}</b>\n\n"
        f"{esc(body_trim)}\n\n"
        f"<i>{when} UTC</i>"
    )


# ---------------------------------------------------------------------------
# IAPs — App Store Server Notifications history
# ---------------------------------------------------------------------------

def poll_iaps(app: dict, token: str, app_state: dict) -> list:
    """Query notifications history for the window since last check.
    Requires App Store Server Notifications to be configured (pointing
    at any URL — Apple logs the notification regardless of delivery)."""
    app_name = app["name"]
    now_ms = int(time.time() * 1000)
    last_query_ms = app_state.get("last_iap_query_ms")
    if last_query_ms is None:
        app_state["last_iap_query_ms"] = now_ms
        logger.info("iaps: seeded %s — alerts start from now", app_name)
        return []
    start_ms = last_query_ms - 60_000  # 60s overlap to cover clock skew
    body = {"startDate": start_ms, "endDate": now_ms}

    notifications = []
    pagination_token = None
    url_base = f"{APP_STORE_SERVER}/inApps/v1/notifications/history"
    while True:
        url = url_base + (f"?paginationToken={urllib.parse.quote(pagination_token)}" if pagination_token else "")
        status, data = http(url, token, method="POST", body=body)
        if status != 200:
            logger.warning("iap poll failed for %s: %s %s", app_name, status, data)
            return []
        notifications.extend(data.get("notificationHistory", []))
        pagination_token = data.get("paginationToken")
        if not data.get("hasMore") or not pagination_token:
            break

    # De-dupe against a rolling window of seen UUIDs.
    seen = set(app_state.get("seen_notif_uuids", []))
    fresh = []
    for n in notifications:
        payload = decode_jws_claims(n.get("signedPayload", ""))
        uuid_key = payload.get("notificationUUID") or n.get("notificationUuid") or json.dumps(n, sort_keys=True)[:40]
        if uuid_key in seen:
            continue
        fresh.append((uuid_key, n))
    new_seen = list(seen) + [u for u, _ in fresh]
    app_state["seen_notif_uuids"] = new_seen[-200:]
    app_state["last_iap_query_ms"] = now_ms
    if fresh:
        logger.info("iaps: %d new on %s", len(fresh), app_name)
    return [n for _, n in fresh]


def decode_jws_claims(signed: str) -> dict:
    """Decode the middle segment of a JWS (claims). Does NOT verify the
    signature — purely informational parsing for display."""
    try:
        parts = signed.split(".")
        if len(parts) < 2:
            return {}
        padded = parts[1] + "=" * (-len(parts[1]) % 4)
        return json.loads(base64.urlsafe_b64decode(padded))
    except Exception:
        return {}


NOTIFICATION_EMOJI = {
    "SUBSCRIBED":                 "🎉",
    "DID_RENEW":                  "🔁",
    "DID_FAIL_TO_RENEW":          "⚠️",
    "EXPIRED":                    "🔚",
    "REFUND":                     "💸",
    "REFUND_DECLINED":            "🚫",
    "REFUND_REVERSED":            "🔄",
    "CONSUMPTION_REQUEST":        "📝",
    "DID_CHANGE_RENEWAL_STATUS":  "🔁",
    "DID_CHANGE_RENEWAL_PREF":    "🔀",
    "PRICE_INCREASE":             "💲",
    "ONE_TIME_CHARGE":            "💰",
    "OFFER_REDEEMED":             "🎁",
    "REVOKE":                     "🛑",
    "GRACE_PERIOD_EXPIRED":       "⌛",
    "EXTERNAL_PURCHASE_TOKEN":    "🎟",
    "TEST":                       "🧪",
}


def format_iap(app_name: str, notification: dict) -> str:
    signed = notification.get("signedPayload", "")
    payload = decode_jws_claims(signed)
    notif_type = payload.get("notificationType", "UNKNOWN")
    subtype = payload.get("subtype", "")
    emoji = NOTIFICATION_EMOJI.get(notif_type, "📩")

    data = payload.get("data", {}) or {}
    env = data.get("environment", "")
    trans = decode_jws_claims(data.get("signedTransactionInfo", "") or "")
    renewal = decode_jws_claims(data.get("signedRenewalInfo", "") or "")

    product_id = trans.get("productId") or renewal.get("productId") or ""
    price_micros = trans.get("price")
    currency = trans.get("currency") or ""
    country = trans.get("storefront") or ""
    quantity = trans.get("quantity") or 1
    kind = trans.get("type") or ""
    price_str = f"{price_micros / 1_000_000:.2f} {currency}" if price_micros and currency else ""

    def esc(s):
        return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    title = f"{emoji} <b>{esc(notif_type)}</b>"
    if subtype:
        title += f" · <code>{esc(subtype)}</code>"

    env_tag = ""
    if env and env.lower() != "production":
        env_tag = f" <code>[{esc(env)}]</code>"

    lines = [
        f"{title}{env_tag}",
        f"<b>{esc(app_name)}</b>",
    ]
    if product_id:
        suffix = f" ×{quantity}" if quantity and quantity != 1 else ""
        lines.append(f"Product: <code>{esc(product_id)}</code>{suffix}")
    if price_str:
        lines.append(f"Price: <b>{esc(price_str)}</b>")
    if country:
        lines.append(f"Storefront: <code>{esc(country)}</code>")
    if kind:
        lines.append(f"Kind: {esc(kind)}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# telegram
# ---------------------------------------------------------------------------

def telegram_send(bot_token: str, chat_id: str, html_text: str) -> bool:
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": html_text,
        "parse_mode": "HTML",
        "disable_web_page_preview": "true",
    }).encode()
    req = urllib.request.Request(url, data=payload, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except urllib.error.HTTPError as e:
        logger.warning("telegram send %s: %s", e.code, e.read().decode(errors="replace")[:400])
        return False
    except urllib.error.URLError as e:
        logger.warning("telegram network error: %s", e)
        return False


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def run_once(config: dict, state: dict, dry_run: bool = False) -> int:
    apple = config["apple"]
    tg = config["telegram"]
    apps = config["apps"]

    asc_token = make_jwt(apple["key_path"], apple["key_id"], apple["issuer_id"])

    sent = 0
    for app in apps:
        app_state = state["apps"].setdefault(str(app["app_id"]), {})

        if app.get("poll_reviews", True):
            try:
                for r in poll_reviews(app, asc_token, app_state):
                    msg = format_review(app["name"], r)
                    if dry_run:
                        logger.info("[dry] review: %s", msg[:160].replace("\n", " ⏎ "))
                    else:
                        telegram_send(tg["bot_token"], tg["chat_id"], msg)
                    sent += 1
            except Exception:
                logger.exception("review poll crashed for %s", app["name"])

        if app.get("poll_iaps", False):
            try:
                server_token = make_jwt(
                    apple["key_path"], apple["key_id"], apple["issuer_id"],
                    bundle_id=app["bundle_id"],
                )
                for n in poll_iaps(app, server_token, app_state):
                    msg = format_iap(app["name"], n)
                    if dry_run:
                        logger.info("[dry] iap: %s", msg[:160].replace("\n", " ⏎ "))
                    else:
                        telegram_send(tg["bot_token"], tg["chat_id"], msg)
                    sent += 1
            except Exception:
                logger.exception("iap poll crashed for %s", app["name"])

    if not dry_run:
        save_state(state)
    logger.info("cycle complete — %d notification(s) sent", sent)
    return sent


def cmd_test_telegram(config: dict) -> None:
    tg = config["telegram"]
    ok = telegram_send(
        tg["bot_token"], tg["chat_id"],
        "<b>✅ Lagerland notifier</b>\nTelegram channel works. You're set up.",
    )
    if not ok:
        sys.exit("Telegram test failed. Double-check bot_token and chat_id in config.")
    print("Telegram test message sent.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--dry-run", action="store_true", help="don't send or save state")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--test-telegram", action="store_true", help="send a hello message and exit")
    args = parser.parse_args()

    setup_logging(args.verbose)
    config = load_config()

    if args.test_telegram:
        cmd_test_telegram(config)
        return

    state = load_state()
    run_once(config, state, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
