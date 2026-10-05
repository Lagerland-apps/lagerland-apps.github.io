// Usage: node render.mjs <mock-file.html> [<mock-file.html> ...]
// Each mock file = one style. It must contain:
//   <!-- fonts: Family Name:400,700,400i | Other Family:500 -->   (open-license faces on Fontsource; self-hosted, latin subset; 'i' = italic)
//   <style> ...every selector scoped under .s-<id> ... </style>
//   <div class="s-<id> mk mk--desktop"> ... 1440x900 first viewport ... </div>
//   <div class="s-<id> mk mk--mobile">  ... 390x844 first viewport ... </div>
// Asset paths are relative to the board root (e.g. assets/observa/s1.jpg).
// Writes renders/<basename>-desktop.png and renders/<basename>-mobile.png.
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'node:fs'; import path from 'node:path';
import { fontCss } from './fonts.mjs';
const root = path.dirname(new URL(import.meta.url).pathname);
const browser = await chromium.launch();
for (const file of process.argv.slice(2)) {
  const src = fs.readFileSync(file, 'utf8');
  const fm = src.match(/<!--\s*fonts:\s*([^>]*?)-->/);
  let link = '';
  if (fm) { try { const r = fontCss(fm[1], '/fonts/'); link = `<style>${r.css}</style>`; r.report.forEach(x => console.log(x)); } catch (e) { console.log('FONT ERROR', e.message); } }
  const base = path.basename(file, '.html');
  for (const [kind, w, h] of [['desktop', 1440, 1800], ['mobile', 390, 1688]]) {
    const html = `<!doctype html><html><head><meta charset="utf-8"><base href="/">${link}
<style>html,body{margin:0;padding:0;background:#777}.mk{width:${w}px;height:${h}px;overflow:hidden;position:relative;box-sizing:border-box}.mk *{box-sizing:border-box}.mk--${kind === 'desktop' ? 'mobile' : 'desktop'}{display:none!important}</style>
</head><body>${src}</body></html>`;
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    fs.mkdirSync(path.join(root, '_render'), { recursive: true });
    fs.writeFileSync(path.join(root, '_render', `${base}-${kind}.html`), html);
    await page.goto(`http://localhost:4200/_render/${base}-${kind}.html`, { waitUntil: 'networkidle' }).catch(() => {});
    await page.evaluate(() => document.fonts && document.fonts.ready);
    await page.waitForTimeout(250);
    const el = await page.$(`.mk--${kind}`);
    const out = path.join(root, 'renders', `${base}-${kind}.png`);
    if (el) { await el.screenshot({ path: out }); console.log('wrote', out); }
    else console.log('MISSING .mk--' + kind + ' in', file);
    // report text overflow / fonts actually loaded
    const fontsLoaded = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight + ' ' + f.style));
    console.log(kind, 'fonts loaded:', [...new Set(fontsLoaded)].join(', ') || 'none');
    await page.close();
  }
}
await browser.close();
