# Reviewer brief: Italian (it, Italy) Tier 3, batch 1 (comparison pages)

You did not write these pages. Never published. Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit ONLY the Italian files assigned to you
(Dutch, Spanish and Portuguese sessions work in this checkout; never run git commands that change state, never run
jekyll build, `i18n.py map` or the stamp script).

## Read

`_i18n/it-reviewer-brief.md` (the Tier 1 review method: copy-editing, fact diff, glossary, SEO, house rules,
structure) and follow it, with the Tier 3 differences below. Also: `_i18n/it-tier3-brief.md` (the writers' brief: what
they were allowed to use), `_i18n/it.md` (sheet, all of «Tells to cut»), `_i18n/it-apple-terms.md`, the app sections of
`_i18n/it-glossary.md`, `/Users/anttiaittamaa/Downloads/githubcode/it-tier3-store-2026-11-19.md` (the Italian App Store
data for each competitor, checked today) and the writers' own notes in
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-uxS8e6/ac98050c-36df-44ef-84c7-3da2924e56aa/scratchpad/it-t3/writer-notes.md`
(each page's known risks: added FAQs, added listing facts, skipped skill passes; check every one).

## Tier 3 differences

1. **Copy-editing**: run the full skill (`~/.claude/skills/copy-editing/SKILL.md`, Seven Sweeps + AI-tell removal) on
   every Italian string. Several writers did a hand pass only.
2. **Fact diff, two sources**:
   - Our app: every claim must be on the English page (`alternatives/<slug>.html`) or in the Italian app page /
     catalog that feeds both; prices only via tokens.
   - The competitor: every market-specific fact (price, rating, store name, platforms, languages, IAP) must match the
     Italian store file EXACTLY (U+00A0 before €, «dato del 19 novembre 2026»). US prices, US dates («checked 29
     October», «US App Store») must be gone. A competitor feature claim must be on the English page or in the Italian
     description in the store file; if the page adds one from the Italian description, keep it only if the description
     says it plainly, else cut it. Added FAQs: keep only if every fact in the answer comes from the English page, the
     Italian store file, or (Lichess page) the existing Italian chess guide `it/guides/best-chess-apps-iphone.html`;
     the visible question must equal the schema name character for character.
   - Local-only Wallet page: every Wallet fact from the store file's description/IAP rows; Spendee facts only as the
     Italian bill tracker guide states them; no security/fee/bank-coverage judgement beyond the listing's own words;
     no review quotes.
3. **House rules**: «senza abbonamento» only for LiftLog. Observa, RightSplit, Chessful, EarnLock, MediaKit, AllPaid
   are never called «senza abbonamento» (titles included: a title like «Oura Ring senza abbonamento: alternativa…» must
   not read as if Observa had no subscription; rephrase if it does). «noi» only where the English says "we" (the studio
   is one person: «non li riportiamo», «non abbiamo provato» → passive or «Lagerland Apps …» unless English says we).
   No «per ora» / «non ancora» (implied translation promises).
4. **SEO**: primaries per page as in it-tier3-brief.md; no two pages in this batch share a seo.title pattern or
   primary; seo.keywords only real queries (research file `/Users/anttiaittamaa/Downloads/githubcode/it-tier3-research-2026-11-19.md`
   or it-keywords.md); no app-page primary used as a primary here.
5. **Structure**: JSON-LD skeleton identical to `es/alternatives/<slug>.html` (WebPage / BreadcrumbList / FAQPage);
   parse every `<script type="application/ld+json">` block after stripping Liquid (`{{ … }}` → "x") to catch JSON
   errors; FAQ names equal visible summaries. Check typographic details by script: no straight apostrophes in prose,
   no « », no em/en dashes, every € preceded by U+00A0 (and no double space before it), no space before %.

## Reply with

Per page: a short change table (field | before | after | why), fact-diff result, and new Italian tells for the sheet.
Then English-side issues for ISSUES.md (one line each, with file).

## Batch 2 (2026-11-19)

Same method. Store and web data: `/Users/anttiaittamaa/Downloads/githubcode/it-tier3-store-batch2-2026-11-19.md`.
Writer notes: the same `writer-notes.md` (batch 2 section; batch 1 notes are in `writer-notes-batch1.md`). Batch 2 rules
for writers are the «Batch 2» section of it-tier3-brief.md. Extra checks:
- HandBrake, Convertio, CloudConvert are web or desktop tools: facts from the English page plus their own sites as the
  store file quotes them; Convertio prices stay in dollars as its site shows them; no «App Store» claim for HandBrake or
  Convertio.
- seo.keywords must not take an app page's own queries (MediaKit: `comprimere video iphone`, `comprimere pdf iphone`,
  `convertire video in mp4 iphone`; RightSplit: `app per dividere le spese`, `app per dividere il conto`): remove them.
- Writers added FAQs to cover the primary query («X è gratis?», «X è in italiano?», «Come funziona X?»): keep only those
  whose every fact comes from the English page or the store file; no pointer-only answers («vedi la sezione…»).
- Competitor claims kept from English with an English-side check date («8 novembre 2026», App Privacy labels): a
  privacy-label claim is per-market; keep it only if the Italian store file supports it, else cut it.
- seo.title patterns must differ from batch 1 titles and from each other; no raw keyword-then-colon titles
  («AppBlock: recensioni…», «Splid: come funziona…», «Fitbod costo in Italia…» read as raw keywords: rephrase if so).

## Batch 3 (2026-11-19)

Same method and batch 2 checks. Store/web data: `/Users/anttiaittamaa/Downloads/githubcode/it-tier3-store-batch3-2026-11-19.md`
(includes the Italian App Privacy labels). Writer notes: `writer-notes.md` (batch 3). Research rows: «Batch 3» in the
research file. Batch 3 rules: the «Batch 3» section of it-tier3-brief.md (Sleep Cycle: Observa has no alarm and records no
sound; Monefy: AllPaid is not an expense tracker). Most writers again did a hand pass only: run the full skill.

## Batch 4 (2026-11-19)

Same method and batch 2 checks. Store/web data: `/Users/anttiaittamaa/Downloads/githubcode/it-tier3-store-batch4-2026-11-19.md`
(Italian App Privacy labels and an «English page claims to check» list per competitor). Writer notes:
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-8uOgRv/283749dc-223e-4f60-b1dc-dcaf5366b46b/scratchpad/it-t3/notes/<slug>.md`. Research rows: «Batch 4 shortlist» in the research file. Writer rules: the «Batch 4» section of
it-tier3-brief.md. Extra checks: Millrace pages never contain the digits of the number game it replaced (grep for 2048);
AfterShift and Observa pages keep every health caveat and make no medical claim; WanderWiki pages never claim offline reading
or Italian-language Wikipedia unless the English page or it/apps/wanderwiki/index.md says so; the three WanderWiki pages and
the two GymLogger X pages have distinct primaries and seo.title patterns from each other and from the 25 existing Italian
comparisons. Run the full skill on every page.
