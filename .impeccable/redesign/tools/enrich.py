#!/usr/bin/env python3
"""Add specimen data (ground/ink/accent, Google Fonts families) and queued fixes to each style; validate fonts on Google Fonts."""
import json, os, re, urllib.request, urllib.parse, concurrent.futures as cf
S = '/tmp/claude-0/-home-user-lagerland-apps-github-io/5553b341-96c8-5ef2-9d5c-b9201c3f3508/scratchpad'
BOARD = f'{S}/board'; REPO = '/home/user/lagerland-apps.github.io'
CACHE = f'{S}/gf-cache.json'
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}

def fam(s):
    if not s: return None
    s = re.split(r'\s+\d|\(|,|—| variable| Variable|:| at | for | with |;', s.strip())[0]
    s = s.strip(' .;') or None
    return {'Source Sans': 'Source Sans 3', 'Source Serif': 'Source Serif 4', 'M PLUS Rounded': 'M PLUS Rounded 1c'}.get(s, s)

def weight(s, default):
    m = re.search(r'\b([1-9]00)\b', s or '')
    return int(m.group(1)) if m else default

def gf_ok(spec):
    if spec in cache: return cache[spec]
    url = 'https://fonts.googleapis.com/css2?family=' + urllib.parse.quote(spec, safe=':@;+') + '&display=swap'
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 Chrome/120'}), timeout=20) as r:
            ok = r.status == 200
    except Exception:
        ok = False
    cache[spec] = ok
    return ok

def lum(h):
    h = h.lstrip('#')
    if len(h) == 3: h = ''.join(c*2 for c in h)
    r, g, b = [int(h[i:i+2], 16)/255 for i in (0, 2, 4)]
    f = lambda c: c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r) + 0.7152*f(g) + 0.0722*f(b)
def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la+0.05)/(lb+0.05)
def sat(h):
    h = h.lstrip('#'); r, g, b = [int(h[i:i+2], 16) for i in (0, 2, 4)]
    mx, mn = max(r, g, b), min(r, g, b)
    return 0 if mx == 0 else (mx-mn)/mx

def headline(sid):
    if sid == 'studio': return ('Private software for iPhone, iPad, Watch and Mac', 'One developer in Finland. No tracking, no ads, no accounts.')
    txt = open(f'{REPO}/_apps/{sid}.md', encoding='utf-8').read()
    def get(key):
        m = re.search(r'^\s{2}' + key + r':\s*"?(.*?)"?\s*$', txt, re.M)
        return m.group(1) if m else ''
    tag = re.search(r'^tagline:\s*"?(.*?)"?\s*$', txt, re.M)
    return (get('headline') or sid, tag.group(1) if tag else '')

specs = set()
data = {}
for f in sorted(os.listdir(f'{BOARD}/data')):
    if not f.endswith('.json') or f.startswith(('_', 'issues', 'sketch', 'plan')): continue
    sid = f[:-5]
    d = json.load(open(f'{BOARD}/data/{f}'))
    data[sid] = d
    for st in d['styles']:
        df, tf = fam(st['type'].get('display')), fam(st['type'].get('text'))
        if tf and tf.lower().startswith('the same'): tf = df
        dw = weight(st['type'].get('display'), 700)
        st['_df'], st['_tf'], st['_dw'] = df, tf, dw
        if df: specs.update([f'{df}:wght@{dw}', df])
        if tf: specs.update([tf])
with cf.ThreadPoolExecutor(16) as ex:
    list(ex.map(gf_ok, sorted(specs)))
json.dump(cache, open(CACHE, 'w'), indent=0)

links = set()
for sid, d in data.items():
    h1, sub = headline(sid)
    issues = json.load(open(f'{BOARD}/data/issues/{sid}.json')) if os.path.exists(f'{BOARD}/data/issues/{sid}.json') else []
    for st in d['styles']:
        pal = [c['hex'] for c in st['palette'] if re.match(r'^#[0-9a-fA-F]{6}$', c['hex'])]
        bg = pal[0] if pal else '#ffffff'
        rest = pal[1:] or ['#000000']
        ink = max(rest, key=lambda c: contrast(bg, c))
        others = [c for c in rest if c != ink] or [ink]
        accent = max(others, key=lambda c: (sat(c), contrast(bg, c)))
        df, tf, dw = st.pop('_df'), st.pop('_tf'), st.pop('_dw')
        dspec = f'{df}:wght@{dw}' if df and cache.get(f'{df}:wght@{dw}') else (df if df and cache.get(df) else None)
        tspec = tf if tf and cache.get(tf) else None
        for sp in (dspec, tspec):
            if sp: links.add(sp)
        st['specimen'] = {'bg': bg, 'ink': ink, 'accent': accent, 'display': df or 'system-ui', 'dw': dw if dspec and ':wght@' in dspec else 400,
                          'text': tf or 'system-ui', 'h1': h1, 'sub': sub, 'fontsOk': bool(dspec), 'textOk': bool(tspec)}
        mine = [i for i in issues if i['severity'] in ('blocker', 'major') and i['style'].strip().lower() in (st['id'], 'all', f"{st['id']} ", 'a,b,c', 'a, b, c')]
        st['fixes'] = [{'sev': i['severity'], 'text': i['fix']} for i in mine]
    d['pageFixes'] = [{'sev': i['severity'], 'issue': i['issue']} for i in issues if i['severity'] == 'blocker' and i['style'].strip().lower() == 'all']
    json.dump(d, open(f'{BOARD}/data/{sid}.json', 'w'), ensure_ascii=False, indent=1)
# Chunk google font links (one bad spec would break a combined URL, but every spec here was validated)
links = sorted(links)
chunks = [links[i:i+15] for i in range(0, len(links), 15)]
urls = ['https://fonts.googleapis.com/css2?' + '&'.join('family=' + urllib.parse.quote(s, safe=':@;+').replace('%20', '+') for s in c) + '&display=swap' for c in chunks]
json.dump(urls, open(f'{BOARD}/data/_fontlinks.json', 'w'), indent=0)
bad = sorted({k.split(':')[0] for k, v in cache.items() if not v and ':' not in k})
print('specs checked:', len(specs), 'font links:', len(urls), 'families not on Google Fonts (fallback to system):', bad)
