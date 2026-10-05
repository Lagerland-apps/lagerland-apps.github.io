export const meta = {
  name: 'lagerland-crosscheck',
  description: 'Cross-catalogue critique of all 63 proposed styles through three lenses: distinctness/slop, truth and contract, feasibility/perf/a11y',
  phases: [{ title: 'Cross-check', detail: 'three lens critics over every surface and style' }],
}
const BRIEF = args.brief
const BOARD = args.board
const REPO = args.repo

const ISSUES = {
  type: 'object',
  properties: {
    issues: { type: 'array', items: { type: 'object', properties: {
      surface: { type: 'string' }, style: { type: 'string' }, severity: { type: 'string', enum: ['blocker', 'major', 'minor'] }, issue: { type: 'string' }, fix: { type: 'string' },
    }, required: ['surface', 'style', 'severity', 'issue', 'fix'] } },
    catalogueNotes: { type: 'string' },
  },
  required: ['issues', 'catalogueNotes'],
}

const LENSES = [
  ['distinctness', `DISTINCTNESS & SLOP: (1) cross-catalogue collisions — two surfaces (or two styles of one surface) sharing a world, a palette family, a display face, or a first-viewport topology. Pay special attention to the board-game trio (chessful, shogiful, xiangqiful), the strength pair (gymlogger-x, liftlog), the AppMeta pair (appmeta, appmeta-pulse), the planning pair (taskful-day, soon), the money pair (allpaid, rightsplit), the body trio (observa, aftershift, earnlock), and the studio world vs the microsites. A display face should appear in at most one surface unless the reuse is argued; flag every reuse (the digest census helps). (2) AI-default clusters (cream+serif+terracotta; near-black+neon glow; editorial hairlines+italic serif+tracked mono labels) and the training-default face list in the brief. (3) Category guessability (chess→wood/gold, health→dark neon dashboard, finance→blue fintech, dev tools→terminal). (4) Template skeletons in costume (split hero copy-left/phone-right/badge row; centred headline over cards) and posters with no working parts. (5) Styles that are only a hero skin over the incumbent section order rather than a from-scratch page. (6) Styles within one surface that are not materially different.`],
  ['truth-contract', `TRUTH, CONVERSION & SEO CONTRACT: (1) any invented claim — numbers, ratings, user counts, press, prices, features, testimonials — not present in the app's front matter/body/_data (VERIFY in ${REPO}/_apps/<slug>.md and ${REPO}/_data/*.yml); star ratings anywhere (no app has ≥25 ratings). (2) The App Store action: official Apple badge present and unmistakable in the first viewport at 1440 and 390, never redrawn/recoloured; desktop QR scan-to-install present (de-emphasis acceptable for Mac-only apps); sticky download bar described; price statement truthful to price.value; Smart App Banner unaffected. (3) quick_answer visible and high; ai-canonical Quick reference kept visible (not hidden); FAQ, HowTo steps (how_it_works), comparison table, privacy summary + links to privacy policy / support / transparency, maker/freshness line all present in visitorPath where the app has them. (4) Content hidden behind interactions without a visible no-JS fallback (tabs, carousels, accordions that hide crawlable text by default). (5) Privacy claims stated without the transparency link. (6) Read-mode variants that would break reading (world in the reading column). (7) Tare: upcoming, no images — anything implying a live App Store listing it doesn't have.`],
  ['feasibility', `FEASIBILITY, PERFORMANCE & ACCESSIBILITY: (1) every named face exists on Fontsource (\`npm view @fontsource/<kebab-name> name\`) with the weights/italics named; total font payload per page plausible ≤ ~160 KB latin. (2) Palette contrast: compute WCAG 2.x ratios with a small python script for the text/ground pairs each style implies (body text on ground, secondary text on ground, text on accent fills, badge surround) — body ≥ 4.5:1, large ≥ 3:1; flag failures with the hex pair and a corrected hex. (3) Signature interactions buildable in vanilla JS/CSS on static Jekyll with a no-JS fallback that shows all content and a reduced-motion fallback; flag anything needing heavy libraries, WebGL without fallback, server code, build steps, huge assets, or new raster art that does not exist and is not listed in assetsNeeded. (4) Mobile 390px viability of the first viewport (badge, offer, evidence readable without horizontal scroll). (5) LCP risk (giant images/video/fonts in the first viewport). (6) Maintenance: anything that would need hand-editing per page instead of being driven by front matter.`],
]

phase('Cross-check')
const ACTIVE = args.only ? LENSES.filter(l => args.only.includes(l[0])) : LENSES
const results = await parallel(ACTIVE.map(([k, lens]) => () => agent(`You are a cross-catalogue critic for the Lagerland Apps redesign shape round. Read ${BRIEF} first (binding contract, calibration, craft floor, owner decisions). The digest of all 63 proposed styles prepared for your lens is ${BOARD}/data/_digest-${k}.json (read it fully, in chunks if needed); the normalised typeface census (faces shared across surfaces) is ${BOARD}/data/_face-census.txt; full cards per surface are in ${BOARD}/data/<surface>.json when you need detail. Note: only ONE style per surface will ship, so a resource shared between style x of surface A and style y of surface B is a conditional collision: resolve shared DISPLAY faces and shared worlds/palette families (major — say which side changes), treat a shared TEXT/utility face as minor unless it becomes a monoculture (a face used across more than two surfaces must be cut back to at most two).
Judge ALL surfaces and styles through ONE lens:
${lens}
Be specific and adversarial; every issue names the surface id, the style id (a|b|c, or "all"), severity (blocker = must change before the owner sees it; major = should change; minor = polish), the issue, and a concrete fix (e.g. "swap display face X for Y because ...", "replace this style's world with the surface's candidate #k because it collides with <other surface> style <x>"). When two surfaces collide, say WHICH one should change and why (keep the one where the world is more native). Do not invent problems to fill a quota; do not restate the brief.
Before finishing, write your exact JSON result to ${BOARD}/data/issues-${k}.json with the Write tool, then return it as structured output.`, { label: `critic:${k}`, phase: 'Cross-check', schema: ISSUES })))
return results.map((r, i) => r ? { lens: ACTIVE[i][0], issues: r.issues.length, blockers: r.issues.filter(x => x.severity === 'blocker').length, majors: r.issues.filter(x => x.severity === 'major').length } : { lens: ACTIVE[i][0], failed: true })
