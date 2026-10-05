#!/usr/bin/env python3
"""Self-contained local page showing the rendered layout sketches (desktop + phone) for selected surfaces."""
import json, os, base64, subprocess, html, sys
S = '/tmp/claude-0/-home-user-lagerland-apps-github-io/5553b341-96c8-5ef2-9d5c-b9201c3f3508/scratchpad'
B = f'{S}/board'
SURF = [('studio', 'Lagerland Apps — studio homepage'), ('observa', 'Observa — app microsite')]

def webp_b64(png, width=None):
    out = png.replace('.png', '.board.webp')
    vf = ['-vf', f'scale={width}:-2'] if width else []
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', png, *vf, '-c:v', 'libwebp', '-quality', '84', out], check=True)
    return 'data:image/webp;base64,' + base64.b64encode(open(out, 'rb').read()).decode()

e = html.escape
parts = []
for sid, title in SURF:
    d = json.load(open(f'{B}/data/{sid}.json'))
    cards = []
    for st in d['styles']:
        dp, mp = f'{B}/renders/{sid}-{st["id"]}-desktop.png', f'{B}/renders/{sid}-{st["id"]}-mobile.png'
        if not (os.path.exists(dp) and os.path.exists(mp)):
            cards.append(f'<article class="st"><header><p class="k">{e(st["kicker"])}</p><h3>{e(st["label"])}</h3></header><p class="miss">Layout not rendered.</p></article>')
            continue
        sk = {}
        if os.path.exists(f'{B}/data/sketch-{sid}-{st["id"]}.json'):
            try: sk = json.load(open(f'{B}/data/sketch-{sid}-{st["id"]}.json'))
            except Exception: pass
        dsrc, msrc = webp_b64(dp, 1200), webp_b64(mp)
        dev = f'<p class="dev"><b>Where the sketch departs from the card:</b> {e(sk.get("deviations", ""))}</p>' if sk.get('deviations') else ''
        cards.append(f'''<article class="st" id="{sid}-{st["id"]}">
  <header><p class="k">{e(st["kicker"])} · style {st["id"].upper()}</p><h3>{e(st["label"])}</h3><p class="th">{e(st["thesis"])}</p></header>
  <div class="frames">
    <figure class="desk"><img src="{dsrc}" alt="{e(st["label"])} — desktop layout, two screens" loading="lazy"><figcaption>Desktop 1440 — first screen + the section below</figcaption></figure>
    <figure class="phone"><img src="{msrc}" alt="{e(st["label"])} — phone layout, two screens" loading="lazy"><figcaption>Phone 390</figcaption></figure>
  </div>
  <p class="meta"><b>Type:</b> {e(st["type"]["display"][:140])} · <b>Signature:</b> {e(st["signatureInteraction"][:260])}</p>{dev}
</article>''')
    parts.append(f'<section class="surf"><h2>{e(title)}</h2>' + '\n'.join(cards) + '</section>')

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lagerland Layout Sketches</title>
<style>
:root{{--bg:#E4E7EA;--sheet:#F6F7F8;--ink:#121518;--ink2:#465058;--line:#C5CBD0}}
@media (prefers-color-scheme:dark){{:root{{--bg:#101214;--sheet:#191C1F;--ink:#ECEFF1;--ink2:#A4ADB4;--line:#2E3338;color-scheme:dark}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;padding:24px clamp(16px,3vw,40px) 80px}}
h1{{font-size:clamp(26px,4vw,40px);margin:0 0 6px;letter-spacing:-.02em}}.lede{{color:var(--ink2);max-width:72ch;margin:0 0 28px}}
.surf{{margin-top:36px}}.surf h2{{font-size:24px;margin:0 0 16px;border-top:2px solid var(--ink);padding-top:14px}}
.st{{background:var(--sheet);border:1px solid var(--line);border-radius:14px;padding:18px;margin:0 0 22px}}
.k{{font:11px/1 ui-monospace,Menlo,monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--ink2);margin:0}}
.st h3{{font-size:22px;margin:6px 0 4px}}.th{{margin:0 0 14px;max-width:90ch}}
.frames{{display:grid;grid-template-columns:minmax(0,3.2fr) minmax(0,1fr);gap:18px;align-items:start}}
figure{{margin:0}}figure img{{display:block;width:100%;height:auto;border-radius:8px;border:1px solid var(--line)}}
figcaption{{font-size:12px;color:var(--ink2);margin-top:6px}}
.phone img{{max-width:330px}}.meta,.dev{{font-size:13px;color:var(--ink2);margin:12px 0 0}}.miss{{color:var(--ink2)}}
@media (max-width:800px){{.frames{{grid-template-columns:1fr}}.phone img{{max-width:100%}}}}
</style></head><body>
<h1>Layout sketches: studio + Observa</h1>
<p class="lede">Local preview only — nothing is published or live. Each style is drawn two screens tall: the first screen exactly as its card describes, then the section that follows. Sketches use real copy, real screenshots and the official App Store badge; they are design studies, not the final build.</p>
{''.join(parts)}
</body></html>'''
open(f'{S}/lagerland-layouts-studio-observa.html', 'w', encoding='utf-8').write(page)
print('MB', round(os.path.getsize(f'{S}/lagerland-layouts-studio-observa.html') / 1e6, 1))
