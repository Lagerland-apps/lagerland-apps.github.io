// Self-hosted fonts from Fontsource (npm). Spec: "Family Name:400,700,400i | Other:500"
import { execSync } from 'node:child_process'; import fs from 'node:fs'; import path from 'node:path';
const root = path.dirname(new URL(import.meta.url).pathname);
const dir = path.join(root, 'fonts');
export function ensureFamily(family) {
  const kebab = family.trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  const fdir = path.join(dir, kebab);
  if (!fs.existsSync(fdir) || fs.readdirSync(fdir).length === 0) {
    fs.mkdirSync(fdir, { recursive: true });
    const tgzDir = path.join(dir, '_tgz'); fs.mkdirSync(tgzDir, { recursive: true });
    try {
      const out = execSync(`npm pack @fontsource/${kebab} --silent --pack-destination ${tgzDir}`, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).trim().split('\n').pop();
      execSync(`tar xzf ${path.join(tgzDir, out)} -C ${fdir} --wildcards --strip-components=2 'package/files/${kebab}-latin-[0-9]*-*.woff2'`);
    } catch (e) { fs.rmSync(fdir, { recursive: true, force: true }); throw new Error(`Font family not on Fontsource: "${family}" (@fontsource/${kebab}). Pick an open-license Google/Fontsource face.`); }
  }
  return { kebab, fdir, files: fs.readdirSync(fdir) };
}
export function fontCss(spec, urlPrefix = 'fonts/') {
  let css = ''; const report = [];
  for (const part of spec.split('|').map(s => s.trim()).filter(Boolean)) {
    const [fam, ws = '400'] = part.split(':');
    const { kebab, files } = ensureFamily(fam);
    for (const w of ws.split(',').map(s => s.trim())) {
      const italic = w.endsWith('i'); const wt = parseInt(w);
      const f = `${kebab}-latin-${wt}-${italic ? 'italic' : 'normal'}.woff2`;
      if (!files.includes(f)) { const avail = files.map(x => x.replace(`${kebab}-latin-`, '').replace('.woff2', '')).join(' '); report.push(`MISSING ${fam} ${w} (available: ${avail})`); continue; }
      css += `@font-face{font-family:'${fam.trim()}';font-style:${italic ? 'italic' : 'normal'};font-weight:${wt};font-display:block;src:url('${urlPrefix}${kebab}/${f}') format('woff2')}\n`;
    }
  }
  return { css, report };
}
