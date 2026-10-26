#!/usr/bin/env python3
"""Make the small stamp icons: assets/icons/<slug>.png (1024px) -> assets/icons/sm/<slug>.webp (256px).

The homepage stamp sheet, app cards and app-page leaflet load these instead of the
1 MB source PNGs. Run it whenever an app icon is added or changed:
    python3 scripts/generate-icons-sm.py
"""
import glob, os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(ROOT, 'assets', 'icons')
out_dir = os.path.join(src_dir, 'sm')
os.makedirs(out_dir, exist_ok=True)
for path in sorted(glob.glob(os.path.join(src_dir, '*.png'))):
    slug = os.path.splitext(os.path.basename(path))[0]
    im = Image.open(path).convert('RGBA')
    im.thumbnail((256, 256), Image.LANCZOS)
    im.save(os.path.join(out_dir, slug + '.webp'), 'WEBP', quality=86, method=6)
    print('wrote', slug)
