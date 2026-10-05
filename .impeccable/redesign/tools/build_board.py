#!/usr/bin/env python3
"""Assemble the Lagerland Redesign Board artifact from data/*.json, renders/*.png and today/*.png."""
import json, os, subprocess, shutil, re
import markdown
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup

S = '/tmp/claude-0/-home-user-lagerland-apps-github-io/5553b341-96c8-5ef2-9d5c-b9201c3f3508/scratchpad'
BOARD = os.environ.get('BOARD_DIR', f'{S}/board')
PUB = os.environ.get('PUB_DIR', f'{S}/publish')
REPO = '/home/user/lagerland-apps.github.io'
ORDER = ['studio', 'observa', 'chessful', 'shogiful', 'xiangqiful', 'gymlogger-x', 'liftlog', 'aftershift', 'earnlock', 'pawza',
         'allpaid', 'rightsplit', 'taskful-day', 'soon', 'appmeta', 'appmeta-pulse', 'mockly', 'mediakit', 'millrace', 'wanderwiki', 'tare']

def app_name(sid):
    if sid == 'studio':
        return 'Lagerland Apps (studio site)'
    p = f'{REPO}/_apps/{sid}.md'
    for line in open(p, encoding='utf-8'):
        m = re.match(r'^name:\s*"?(.*?)"?\s*$', line)
        if m:
            return m.group(1)
    return sid

def scope(sid):
    if sid == 'studio':
        return 'Homepage, all-apps index, journal, guides, audience pages, comparisons index, transparency, about, support, 404'
    n = 0
    for f in os.listdir(f'{REPO}/alternatives'):
        if f.endswith('.html') and f'"slug", "{sid}"' in open(f'{REPO}/alternatives/{f}', encoding='utf-8').read():
            n += 1
    extra = f' + {n} comparison page{"s" if n != 1 else ""}' if n else ''
    return f'/apps/{sid}/ + its privacy and support pages{extra}'

def webp(src, dst, width=None):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    vf = ['-vf', f'scale={width}:-2'] if width else []
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, *vf, '-c:v', 'libwebp', '-quality', '82', dst], check=True)

def md(text):
    return Markup(markdown.markdown(text or '', extensions=['tables', 'fenced_code', 'sane_lists']))

def main():
    if os.path.exists(PUB):
        shutil.rmtree(PUB)
    os.makedirs(f'{PUB}/img', exist_ok=True)
    surfaces = []
    missing = []
    for sid in ORDER:
        p = f'{BOARD}/data/{sid}.json'
        if not os.path.exists(p):
            missing.append(sid)
            continue
        d = json.load(open(p))
        d['surface'] = sid
        d['name'] = app_name(sid)
        d['scope'] = scope(sid)
        icon_src = f'{BOARD}/assets/lagerland-mark.png' if sid == 'studio' else f'{BOARD}/assets/{sid}/icon.png'
        if os.path.exists(icon_src):
            webp(icon_src, f'{PUB}/img/{sid}-icon.webp', 128)
            d['icon'] = f'img/{sid}-icon.webp'
        else:
            d['icon'] = None
        t = f'{BOARD}/today/{sid}-desktop.png'
        if os.path.exists(t):
            webp(t, f'{PUB}/img/{sid}-today.webp', 1200)
            d['today_desktop'] = f'img/{sid}-today.webp'
        sk = {}
        for x in 'abc':
            sp = f'{BOARD}/data/sketch-{sid}-{x}.json'
            if os.path.exists(sp):
                try:
                    sk[x] = json.load(open(sp))
                except Exception:
                    pass
        for st in d['styles']:
            dpng = f'{BOARD}/renders/{sid}-{st["id"]}-desktop.png'
            mpng = f'{BOARD}/renders/{sid}-{st["id"]}-mobile.png'
            if os.path.exists(dpng) and os.path.exists(mpng):
                webp(dpng, f'{PUB}/img/{sid}-{st["id"]}-d.webp')
                webp(mpng, f'{PUB}/img/{sid}-{st["id"]}-m.webp')
                st['desktop'] = f'img/{sid}-{st["id"]}-d.webp'
                st['mobile'] = f'img/{sid}-{st["id"]}-m.webp'
            st['deviations'] = (sk.get(st['id']) or {}).get('deviations', '')
        surfaces.append(d)
    plan = json.load(open(f'{BOARD}/data/plan.json')) if os.path.exists(f'{BOARD}/data/plan.json') else {
        'summary': 'Plan pending.', 'phases': [], 'architecture': '', 'previewAndSelection': '', 'seoParityGuard': '',
        'performanceAndA11yBudget': '', 'risks': [], 'openQuestions': []}
    for ph in plan['phases']:
        ph['pages_html'] = md(ph['pages'])
        ph['scope_html'] = md(ph['scope'])
        ph['selection_html'] = md(ph['selection'])
    plan['architecture_html'] = md(plan['architecture'])
    plan['preview_html'] = md(plan['previewAndSelection'])
    plan['seo_html'] = md(plan['seoParityGuard'])
    plan['perf_html'] = md(plan['performanceAndA11yBudget'])
    env = Environment(loader=FileSystemLoader(S), autoescape=True)
    html = env.get_template('board_template.html').render(
        surfaces=surfaces, surface_ids=[s['surface'] for s in surfaces], plan=plan,
        font_links=json.load(open(f'{BOARD}/data/_fontlinks.json')) if os.path.exists(f'{BOARD}/data/_fontlinks.json') else [],
        app_count=len([s for s in surfaces if s['surface'] != 'studio']))
    open(f'{PUB}/board.html', 'w', encoding='utf-8').write(html)
    files = sorted(os.listdir(f'{PUB}/img'))
    size = sum(os.path.getsize(f'{PUB}/img/{f}') for f in files) + os.path.getsize(f'{PUB}/board.html')
    print(f'surfaces: {len(surfaces)} missing: {missing} images: {len(files)} total MB: {size/1e6:.1f} html KB: {os.path.getsize(f"{PUB}/board.html")/1e3:.0f}')

if __name__ == '__main__':
    main()
