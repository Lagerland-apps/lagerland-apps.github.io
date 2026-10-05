#!/usr/bin/env python3
"""Validate composed surface JSON files and write a compact digest for the cross-catalogue critics."""
import json, os, sys, glob

BOARD = '/tmp/claude-0/-home-user-lagerland-apps-github-io/5553b341-96c8-5ef2-9d5c-b9201c3f3508/scratchpad/board'
EXPECTED = ['studio', 'aftershift', 'allpaid', 'appmeta-pulse', 'appmeta', 'chessful', 'earnlock', 'gymlogger-x', 'liftlog',
            'mediakit', 'millrace', 'mockly', 'observa', 'pawza', 'rightsplit', 'shogiful', 'soon', 'tare', 'taskful-day',
            'wanderwiki', 'xiangqiful']
STYLE_KEYS = ['id', 'label', 'kicker', 'sourceIndex', 'lineage', 'thesis', 'scene', 'scheme', 'colorStrategy', 'palette', 'type',
              'materials', 'firstViewportDesktop', 'firstViewportMobile', 'conversion', 'visitorPath', 'navigation',
              'signatureInteraction', 'motionGrammar', 'readModeVariant', 'assetsNeeded', 'risk', 'memoryTest']

def load(sid):
    p = f'{BOARD}/data/{sid}.json'
    if not os.path.exists(p):
        return None, 'missing file'
    try:
        d = json.load(open(p))
    except Exception as e:
        return None, f'bad json: {e}'
    probs = []
    if len(d.get('styles', [])) != 3:
        probs.append(f"{len(d.get('styles', []))} styles")
    for st in d.get('styles', []):
        miss = [k for k in STYLE_KEYS if k not in st]
        if miss:
            probs.append(f"style {st.get('id')} missing {miss}")
    return d, '; '.join(probs)

def main():
    out = []
    ok = True
    for sid in EXPECTED:
        d, prob = load(sid)
        if d is None or prob:
            ok = False
            print(f'{sid}: {prob}')
        if d is None:
            continue
        d['surface'] = sid
        out.append({
            'surface': d['surface'],
            'mechanism': d['dossier']['mechanism'],
            'categoryDefault': d['dossier']['categoryDefault'],
            'seed': d['seed'],
            'styles': [{k: st.get(k) for k in ['id', 'label', 'kicker', 'lineage', 'thesis', 'scene', 'scheme', 'colorStrategy',
                                               'palette', 'type', 'materials', 'firstViewportDesktop', 'firstViewportMobile',
                                               'conversion', 'visitorPath', 'signatureInteraction', 'readModeVariant',
                                               'assetsNeeded', 'risk']} for st in d['styles']],
        })
    json.dump(out, open(f'{BOARD}/data/_digest.json', 'w'), ensure_ascii=False, indent=0)
    print('digest surfaces:', len(out), 'bytes:', os.path.getsize(f'{BOARD}/data/_digest.json'), 'all ok' if ok else 'PROBLEMS ABOVE')
    # quick face census
    faces = {}
    for s in out:
        for st in s['styles']:
            for role in ('display', 'text', 'utility'):
                f = (st['type'] or {}).get(role)
                if f:
                    key = f.split('(')[0].split(',')[0].strip()
                    faces.setdefault(key, []).append(f"{s['surface']}-{st['id']}:{role}")
    dup = {k: v for k, v in faces.items() if len({x.split('-')[0] if not x.startswith('appmeta-pulse') and not x.startswith('gymlogger-x') and not x.startswith('taskful-day') else x.rsplit('-', 1)[0] for x in v}) > 1}
    print('faces used:', len(faces))
    for k, v in sorted(dup.items(), key=lambda kv: -len(kv[1])):
        print('  shared face:', k, '->', ', '.join(v))

if __name__ == '__main__':
    main()

# ---- per-lens digests + normalised face census ----
import re as _re
def fam(s):
    if not s: return None
    s = _re.split(r'\s+\d|\(|,|—| variable| Variable|:| at | for ', s.strip())[0]
    return s.strip(' .;') or None

def trunc(v, n):
    if isinstance(v, str): return v if len(v) <= n else v[:n] + '…'
    if isinstance(v, list): return [trunc(x, n) for x in v]
    return v

def lens_digests():
    surfaces = []
    for sid in EXPECTED:
        d, _ = load(sid)
        if d: d['surface'] = sid; surfaces.append(d)
    fields = {
        'distinctness': dict(label=200, kicker=40, lineage=200, thesis=300, scene=250, scheme=120, colorStrategy=80, palette=None, materials=200, firstViewportDesktop=700, firstViewportMobile=300),
        'truth-contract': dict(label=200, firstViewportDesktop=700, firstViewportMobile=500, conversion=700, visitorPath=220, readModeVariant=400, assetsNeeded=300),
        'feasibility': dict(label=200, scheme=120, palette=None, firstViewportMobile=500, signatureInteraction=600, motionGrammar=300, assetsNeeded=300),
    }
    for lens, fl in fields.items():
        out = []
        for d in surfaces:
            styles = []
            for st in d['styles']:
                o = {'id': st['id']}
                for k, n in fl.items():
                    o[k] = st.get(k) if n is None else trunc(st.get(k), n)
                if lens != 'truth-contract':
                    o['type'] = {r: trunc((st.get('type') or {}).get(r), 260 if lens == 'feasibility' else 140) for r in ('display', 'text', 'utility')}
                styles.append(o)
            out.append({'surface': d['surface'], 'mechanism': trunc(d['dossier']['mechanism'], 300), 'categoryDefault': trunc(d['dossier']['categoryDefault'], 300), 'styles': styles})
        p = f'{BOARD}/data/_digest-{lens}.json'
        json.dump(out, open(p, 'w'), ensure_ascii=False, separators=(',', ':'))
        print(lens, 'digest KB:', os.path.getsize(p) // 1000)
    census = {}
    for d in surfaces:
        for st in d['styles']:
            for role in ('display', 'text', 'utility'):
                f = fam((st.get('type') or {}).get(role))
                if f and f.lower() not in ('none', 'n/a', '—'):
                    census.setdefault(f, []).append(f"{d['surface']}-{st['id']}:{role[0]}")
    lines = []
    for f, uses in sorted(census.items(), key=lambda kv: (-len({u.rsplit('-', 1)[0] for u in kv[1]}), kv[0])):
        surf = {u.rsplit('-', 1)[0] for u in uses}
        if len(surf) > 1:
            lines.append(f'{f}: ' + ', '.join(uses))
    open(f'{BOARD}/data/_face-census.txt', 'w').write('\n'.join(lines))
    print('faces shared across surfaces:', len(lines)); print('\n'.join(lines))

lens_digests()
