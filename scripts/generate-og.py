#!/usr/bin/env python3
"""
Generate beautiful 1200x630 Open Graph share cards for every app.

For each `_apps/<slug>.md` it reads the front matter (name, tagline, icon,
screenshot) and renders a branded card to `assets/og/<slug>.png`.

Pipeline: build a self-contained HTML document (fonts + icon + screenshot all
base64-inlined, so headless Chrome never makes a network/file fetch), render it
with headless Google Chrome at 2x device-scale, then downscale to 1200x630 with
PIL Lanczos for crisp text. Output is opaque sRGB RGB PNG to match the existing
hand-made cards.

Usage:
    python3 scripts/generate-og.py                 # all apps
    python3 scripts/generate-og.py --only pawza shogiful
    python3 scripts/generate-og.py --dry-run       # list what would render
"""

import argparse
import base64
import re
import subprocess
import sys
import tempfile
from io import BytesIO
from pathlib import Path

import yaml
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parent.parent
APPS_DIR = REPO_ROOT / "_apps"
OG_DIR = REPO_ROOT / "assets" / "og"
ICONS_DIR = REPO_ROOT / "assets" / "icons"
SHOTS_DIR = REPO_ROOT / "assets" / "screenshots"
FONTS_DIR = Path(__file__).resolve().parent / "og-assets" / "fonts"

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

W, H = 1200, 630
DOMAIN = "lagerland-apps.github.io"

# ---------------------------------------------------------------------------
# Curated, hand-authored brand data (auto icon-colour extraction is too muddy).
# accent  : the brand accent that tints the gradient + colours the tagline.
# tagline : overrides the front-matter tagline when it is empty / too long.
# meta    : the small "·"-separated value line.
# variant : "light" for the paper/serif treatment (calm, literary apps).
# ---------------------------------------------------------------------------
ACCENT = {
    "aftershift":    "#5B8DEF",
    "allpaid":       "#2D8CF0",
    "appmeta-pulse": "#6C6CF5",
    "appmeta":       "#4D6BF5",
    "chessful":      "#CF9A4E",
    "driftlines":    "#9A8156",
    "earnlock":      "#7FCB7F",
    "gymlogger-x":   "#2FC4C0",
    "liftlog":       "#E3A23C",
    "mediakit":      "#8A7CF2",
    "mockly":        "#5B7CF7",
    "observa":       "#F2643C",
    "pawza":         "#E0A05A",
    "rightsplit":    "#4F9CF7",
    "shogiful":      "#EBB23E",
    "soon":          "#9D8CF5",
    "taskful-day":   "#3FC79A",
    "wanderwiki":    "#2FAACB",
}

TAGLINE = {
    "aftershift":    "Naps that count as real recovery.",
    "appmeta-pulse": "Your App Store Connect dashboard.",
    "gymlogger-x":   "Log lifts fast. Built for the gym.",
    "taskful-day":   "Plan the day. Finish it — calmly.",
}

META = {
    "aftershift":    "Free · Shift Recovery Score · No account · iPhone",
    "allpaid":       "Free · No bank login · Widgets + Siri · iPhone",
    "appmeta-pulse": "Free · Read-only App Store Connect · iPhone",
    "appmeta":       "App Store Connect, native · $17.99/yr · Mac",
    "chessful":      "Free · Mistake analysis · iPhone · iPad · Mac",
    "driftlines":    "Daily prose · One-time $59.99 · iPhone",
    "earnlock":      "$19.99 lifetime · No account · iPhone + Watch",
    "gymlogger-x":   "Free · Apple Watch · No account · iPhone",
    "liftlog":       "Pay once · Feels like equipment · iPhone",
    "mediakit":      "Every media tool, one app · iPhone + Mac",
    "mockly":        "Pro App Store screenshots · $12.99 once · Mac",
    "observa":       "Free · 100% on-device · No account · iPhone + iPad",
    "pawza":         "Free · On-device AI · No account · iPhone + iPad",
    "rightsplit":    "Free · Scan receipts · $7.99 lifetime · iPhone",
    "shogiful":      "Plain-English coaching · YaneuraOu engine · iPhone & Mac",
    "soon":          "Free · Beautiful countdowns · Widgets · iPhone",
    "taskful-day":   "Free · Calm planning · iPhone · iPad · Mac · Watch",
    "wanderwiki":    "Swipe Wikipedia · 33 languages · Ad-free · iPhone",
}

VARIANT = {"driftlines": "light"}

# Pick a specific screenshot when the first one is a busy marketing collage.
SHOT = {}


def b64_font(name):
    return base64.b64encode((FONTS_DIR / name).read_bytes()).decode()


def b64_img(path, max_w=None):
    """Base64-inline a PNG, optionally pre-downscaled to keep the temp HTML lean."""
    im = Image.open(path).convert("RGBA")
    if max_w and im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    buf = BytesIO()
    im.save(buf, "PNG")
    return base64.b64encode(buf.getvalue()).decode()


FONTS = {
    "i6": b64_font("inter-600.woff2"),
    "i7": b64_font("inter-700.woff2"),
    "i8": b64_font("inter-800.woff2"),
    "s4": b64_font("newsreader-400.woff2"),
    "s5": b64_font("newsreader-500.woff2"),
}


def hex_rgba(h, a):
    h = h.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{a})"


def is_landscape(slug):
    first = sorted((SHOTS_DIR / slug).glob("*.png")) + sorted((SHOTS_DIR / slug).glob("*.jpg"))
    if not first:
        return False
    w, h = Image.open(first[0]).size
    return w > h


def first_shot(slug):
    if slug in SHOT:
        chosen = SHOTS_DIR / slug / SHOT[slug]
        if chosen.exists():
            return chosen
    shots = sorted((SHOTS_DIR / slug).glob("*.png")) + sorted((SHOTS_DIR / slug).glob("*.jpg"))
    return shots[0] if shots else None


def mockup_html(slug, light):
    shot = first_shot(slug)
    if shot is None:
        return ""
    if is_landscape(slug):
        img = b64_img(shot, 1400)
        return f"""
        <div class="mac">
          <div class="bar"><span></span><span></span><span></span></div>
          <img src="data:image/png;base64,{img}">
        </div>"""
    img = b64_img(shot, 760)
    frame = "phone light" if light else "phone"
    return f"""
        <div class="{frame}">
          <div class="island"></div>
          <div class="scr"><img src="data:image/png;base64,{img}"></div>
        </div>"""


def render_html(slug, fm):
    accent = ACCENT.get(slug, "#6FE3FF")
    light = VARIANT.get(slug) == "light"
    name = fm.get("name", slug).rstrip(".")
    tagline = TAGLINE.get(slug) or fm.get("tagline") or ""
    meta = META.get(slug, "")
    icon = b64_img(ICONS_DIR / f"{slug}.png", 200)
    mock = mockup_html(slug, light)
    lay = "lay-mac" if is_landscape(slug) else "lay-phone"

    if light:
        bg = (f"radial-gradient(80% 90% at 18% 8%, {hex_rgba(accent,0.16)} 0%, transparent 52%),"
              f"radial-gradient(70% 80% at 96% 100%, {hex_rgba(accent,0.12)} 0%, transparent 55%),"
              f"linear-gradient(150deg, #FBF8F2 0%, #F2ECE0 100%)")
        ink, ink_soft, ink_mute = "#1C1A14", "rgba(28,26,20,.78)", "rgba(28,26,20,.50)"
        name_font, tag_font = "'Newsreader',serif", "'Newsreader',serif"
        name_weight, name_ls = "500", "-.01em"
        framecol = "#E7DFCF"
    else:
        bg = (f"radial-gradient(75% 85% at 16% 6%, {hex_rgba(accent,0.20)} 0%, transparent 50%),"
              f"radial-gradient(65% 80% at 99% 96%, {hex_rgba(accent,0.16)} 0%, transparent 52%),"
              f"linear-gradient(145deg, #11142E 0%, #080A18 60%, #05060F 100%)")
        ink, ink_soft, ink_mute = "rgba(255,255,255,.97)", "rgba(255,255,255,.80)", "rgba(255,255,255,.46)"
        name_font, tag_font = "'Inter',sans-serif", "'Inter',sans-serif"
        name_weight, name_ls = "800", "-.025em"
        framecol = "#0a0a0c"

    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Inter';font-weight:600;font-display:block;src:url(data:font/woff2;base64,{FONTS['i6']}) format('woff2')}}
@font-face{{font-family:'Inter';font-weight:700;font-display:block;src:url(data:font/woff2;base64,{FONTS['i7']}) format('woff2')}}
@font-face{{font-family:'Inter';font-weight:800;font-display:block;src:url(data:font/woff2;base64,{FONTS['i8']}) format('woff2')}}
@font-face{{font-family:'Newsreader';font-weight:400;font-display:block;src:url(data:font/woff2;base64,{FONTS['s4']}) format('woff2')}}
@font-face{{font-family:'Newsreader';font-weight:500;font-display:block;src:url(data:font/woff2;base64,{FONTS['s5']}) format('woff2')}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px}}
.card{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:{bg};
  font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}}
.left{{position:absolute;left:80px;top:0;height:100%;width:600px;display:flex;
  flex-direction:column;justify-content:center;padding:56px 0}}
.lay-mac .left{{width:468px}}
.idrow{{display:flex;align-items:center;gap:18px;margin-bottom:28px}}
.icon{{width:76px;height:76px;border-radius:18px;box-shadow:0 12px 36px rgba(0,0,0,.40);
  {"border:1px solid rgba(0,0,0,.06)" if light else "border:1px solid rgba(255,255,255,.10)"}}}
.studio{{font-size:18px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  color:{hex_rgba(accent,0.95) if not light else accent}}}
.name{{font-family:{name_font};font-weight:{name_weight};letter-spacing:{name_ls};
  font-size:74px;line-height:1.02;color:{ink}}}
.tag{{font-family:{tag_font};font-size:30px;line-height:1.22;font-weight:600;
  color:{accent};margin-top:20px;max-width:560px}}
.meta{{font-size:19px;font-weight:600;color:{ink_mute};margin-top:26px;letter-spacing:.01em}}
.domain{{position:absolute;left:80px;bottom:48px;font-size:17px;font-weight:600;
  letter-spacing:.05em;color:{ink_mute}}}
.domain b{{color:{accent};font-weight:700}}
/* iPhone mockup */
.phone{{position:absolute;right:74px;top:96px;width:340px;height:736px;border-radius:52px;
  background:{framecol};padding:11px;transform:rotate(-4deg);
  box-shadow:0 40px 90px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.05)}}
.phone.light{{box-shadow:0 36px 80px rgba(60,50,30,.30),0 0 0 1px rgba(0,0,0,.06)}}
.phone .scr{{width:100%;height:100%;border-radius:42px;overflow:hidden;background:#000}}
.phone .scr img{{width:100%;height:100%;object-fit:cover;object-position:top center}}
.phone .island{{position:absolute;top:26px;left:50%;transform:translateX(-50%);
  width:104px;height:30px;background:#000;border-radius:16px;z-index:2}}
/* Mac window mockup */
.mac{{position:absolute;right:-22px;top:50%;transform:translateY(-50%) rotate(-2deg);
  width:606px;border-radius:14px;overflow:hidden;background:#1A1F42;
  box-shadow:0 40px 90px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.06)}}
.mac .bar{{height:34px;background:#232A52;display:flex;align-items:center;gap:9px;padding-left:16px}}
.mac .bar span{{width:13px;height:13px;border-radius:50%;background:rgba(255,255,255,.22)}}
.mac img{{display:block;width:100%}}
</style></head><body>
<div class="card {lay}">
  <div class="left">
    <div class="idrow">
      <img class="icon" src="data:image/png;base64,{icon}">
      <div class="studio">Lagerland Apps</div>
    </div>
    <div class="name">{name}</div>
    <div class="tag">{tagline}</div>
    <div class="meta">{meta}</div>
  </div>
  {mock}
  <div class="domain">{DOMAIN}</div>
</div></body></html>"""


def capture(html, out_png):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        tmp_html = f.name
    tmp_png = out_png.with_suffix(".2x.png")
    subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=2",
        f"--window-size={W},{H}",
        "--default-background-color=ff05060f",
        "--virtual-time-budget=8000",
        "--run-all-compositor-stages-before-draw",
        f"--screenshot={tmp_png}",
        f"file://{tmp_html}",
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    img = Image.open(tmp_png).convert("RGB").resize((W, H), Image.LANCZOS)
    img.save(out_png, "PNG", optimize=True)
    Path(tmp_html).unlink(missing_ok=True)
    tmp_png.unlink(missing_ok=True)
    return out_png.stat().st_size


def parse_app(path):
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    return yaml.safe_load(m.group(1)) if m else {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="only these slugs")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    apps = sorted(APPS_DIR.glob("*.md"))
    if args.only:
        want = set(args.only)
        apps = [p for p in apps if p.stem in want]

    OG_DIR.mkdir(parents=True, exist_ok=True)
    for path in apps:
        slug = path.stem
        fm = parse_app(path)
        if args.dry_run:
            print(f"would render {slug:14} accent={ACCENT.get(slug,'?')} "
                  f"variant={VARIANT.get(slug,'dark')} "
                  f"layout={'mac' if is_landscape(slug) else 'phone'}")
            continue
        html = render_html(slug, fm)
        size = capture(html, OG_DIR / f"{slug}.png")
        print(f"  ✓ {slug:14} {size//1024} KB")


if __name__ == "__main__":
    main()
