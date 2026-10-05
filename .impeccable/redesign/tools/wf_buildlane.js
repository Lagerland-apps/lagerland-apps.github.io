export const meta = {
  name: 'lagerland-sketch-lane',
  description: 'Sketch lane: per surface, apply cross-check fixes to the style cards, build three HTML direction sketches (1440 + 390), review them against the cards, fix once',
  phases: [
    { title: 'Revise', detail: 'apply cross-catalogue issues to the surface cards' },
    { title: 'Sketch', detail: 'one Sonnet agent per style: HTML first-viewport sketch, render, inspect, fix once', model: 'sonnet' },
    { title: 'Review', detail: 'one reviewer per surface judges the three sketches against the cards' },
    { title: 'Fix', detail: 'Sonnet applies review fixes, re-renders', model: 'sonnet' },
  ],
}
const BRIEF = args.brief
const MOCKSPEC = args.mockSpec
const BOARD = args.board
const REPO = args.repo
const SEED = REPO + '/.claude/skills/impeccable/scripts/impeccable concept-seed'

const REVISED = {
  type: 'object',
  properties: { changed: { type: 'boolean' }, summary: { type: 'string' }, rejected: { type: 'string' }, labels: { type: 'array', items: { type: 'string' } } },
  required: ['changed', 'summary', 'rejected', 'labels'],
}
const SKETCH = {
  type: 'object',
  properties: { id: { type: 'string' }, file: { type: 'string' }, desktopPng: { type: 'string' }, mobilePng: { type: 'string' }, fontsLoaded: { type: 'string' }, deviations: { type: 'string' }, selfVerdict: { type: 'string' } },
  required: ['id', 'file', 'desktopPng', 'mobilePng', 'fontsLoaded', 'deviations', 'selfVerdict'],
}
const REVIEW = {
  type: 'object',
  properties: {
    verdicts: { type: 'array', items: { type: 'object', properties: {
      style: { type: 'string', enum: ['a', 'b', 'c'] }, verdict: { type: 'string', enum: ['keep', 'fix'] }, fixes: { type: 'array', items: { type: 'string' } }, note: { type: 'string' },
    }, required: ['style', 'verdict', 'fixes', 'note'] } },
    distinctness: { type: 'string' },
  },
  required: ['verdicts', 'distinctness'],
}

const data = id => `${BOARD}/data/${id}.json`

function revisePrompt(id) {
  return `You are revising one surface ("${id}") of the Lagerland Apps redesign shape round after a cross-catalogue critique. Read ${BRIEF} first. Your surface's current proposal is ${data(id)} (full JSON: dossier, seven candidates, seed, three style cards, canon). The issues raised against it are in ${BOARD}/data/issues/${id}.json; the critics' catalogue-wide notes are in ${BOARD}/data/issues/_notes.md (read for context: other surfaces may be changing to resolve collisions with you — the issue text says which side should change).
Apply every blocker and major fix; apply minor fixes when correct; reject a fix only with a stated factual reason. If a style's world must be replaced (collision or failure), replace it with your next-ranked unused grounded candidate from the candidates list and keep the kicker semantics; style a (THE ROLL) keeps candidate N unless it has a named product-truth failure — then re-roll from the repo with \`cd ${REPO} && ${SEED} --scope direction --mode persuade --from <seed.key> --reroll <next k>\` and record it in seed + notes. Verify facts in ${REPO} when an issue concerns them; verify any new face on Fontsource (\`npm view @fontsource/<kebab> name\`).
Write the FULL revised JSON back to ${data(id)} with the Write tool (same schema, every field kept, notes extended with a short "Revised:" summary). Return the structured summary (changed, summary, rejected fixes with reasons, the three final style labels).`
}

function sketchPrompt(id, x) {
  return `You are building ONE direction sketch for the Lagerland Apps redesign shape round. Read ${BRIEF} (context), ${MOCKSPEC} (exact sketch file format, render and inspection procedure) and ${REPO}/.claude/skills/impeccable/reference/craft-floor.md first.
Surface "${id}"${id === 'studio' ? ' (the studio homepage)' : ` (app microsite /apps/${id}/ — real copy is in ${REPO}/_apps/${id}.md)`}. Style "${x}". Its card is the style with id "${x}" in ${data(id)} (also read that file's dossier). Write ${BOARD}/mocks/${id}-${x}.html with every selector scoped under .s-${id}-${x}.
Build this style exactly as its card describes, at full commitment, as a top-of-class first viewport: the card is the contract (palette hex values, faces, materials, first-viewport composition at 1440 and at 390, navigation, App Store route placement, the signature move shown in its resting/no-JS state). Real copy and real assets only. The sketch must be recognisable as THIS style at thumbnail size and could belong to no other product.
After the bounded render→inspect→fix loop in the spec, write a small JSON record {"id":"${x}","file":...,"desktopPng":...,"mobilePng":...,"fontsLoaded":...,"deviations":...,"selfVerdict":...} to ${BOARD}/data/sketch-${id}-${x}.json (deviations = where and why the sketch departs from the card, or ""), then return the same as structured output.`
}

function reviewPrompt(id) {
  return `You review the three direction sketches of surface "${id}" in the Lagerland Apps redesign shape round. Read ${BRIEF} and ${MOCKSPEC} first, then the cards in ${data(id)}. Open all six renders with the Read tool: ${['a', 'b', 'c'].map(x => `${BOARD}/renders/${id}-${x}-desktop.png and ${BOARD}/renders/${id}-${x}-mobile.png`).join('; ')} (sources: ${BOARD}/mocks/${id}-<x>.html).
For each style decide keep or fix, as a demanding design director: (1) faithful to its card — palette, faces, composition, signature move; (2) reads as its world at thumbnail size, not a template skeleton in costume and not a poster without working parts; (3) the offer, the official App Store badge${id === 'studio' ? ' (or the studio\'s route to the apps)' : ''}, the price statement and (desktop) the QR are present and legible${id === 'tare' ? ' (Tare is upcoming: follow its front matter)' : ''}; (4) nothing clipped/overflowing/illegible, contrast AA, the phone composition is real and not a squeezed desktop; (5) craft-floor refusals respected (no eyebrow labels over headings, no same-size card grids, no gradient text, no emoji icons); (6) top of class — would this hold up next to the best product sites? "fix" only for material problems; list concrete, buildable fixes (what to move/resize/recolour/replace). Also say whether the three are materially distinct (distinctness).`
}

function fixPrompt(id, x, fixes) {
  return `Apply review fixes to one Lagerland redesign direction sketch. Read ${MOCKSPEC} first (format + render procedure) and ${REPO}/.claude/skills/impeccable/reference/craft-floor.md. File: ${BOARD}/mocks/${id}-${x}.html (scoped under .s-${id}-${x}). Card: style "${x}" in ${data(id)}.
Fixes to apply, all in one batch: ${JSON.stringify(fixes)}
Edit the file, re-render (\`cd ${BOARD} && node render.mjs mocks/${id}-${x}.html\`), open both PNGs once to confirm, update ${BOARD}/data/sketch-${id}-${x}.json (deviations/selfVerdict), and return the structured output.`
}

const out = await pipeline(args.surfaces,
  id => args.revise.includes(id)
    ? agent(revisePrompt(id), { label: `revise:${id}`, phase: 'Revise', schema: REVISED }).then(r => ({ id, revised: r }))
    : Promise.resolve({ id, revised: null }),
  prev => parallel(['a', 'b', 'c'].map(x => () => agent(sketchPrompt(prev.id, x), { label: `sketch:${prev.id}-${x}`, phase: 'Sketch', schema: SKETCH, model: 'sonnet' })))
    .then(sk => ({ ...prev, sketches: sk })),
  prev => agent(reviewPrompt(prev.id), { label: `review:${prev.id}`, phase: 'Review', schema: REVIEW }).then(rv => ({ ...prev, review: rv })),
  prev => {
    const toFix = prev.review ? prev.review.verdicts.filter(v => v.verdict === 'fix' && v.fixes.length) : []
    return parallel(toFix.map(v => () => agent(fixPrompt(prev.id, v.style, v.fixes), { label: `fix:${prev.id}-${v.style}`, phase: 'Fix', schema: SKETCH, model: 'sonnet' })))
      .then(f => ({ id: prev.id, revised: prev.revised ? prev.revised.summary : null, sketched: prev.sketches.filter(Boolean).map(s => s.id), review: prev.review, fixed: f.filter(Boolean).map(s => s.id) }))
  })
return out
