# Reviewer brief: Dutch (nl, Netherlands) Tier 3, batch 1 (comparison pages)

You did not write these pages. Never published. Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit ONLY the Dutch files assigned to you
(Spanish, Italian and Portuguese sessions work in this checkout; never run git commands that change state, never run
jekyll build, `i18n.py map` or the stamp script).

## Read

`_i18n/nl-reviewer-brief.md` (the Tier 1 review method: copy-editing, fact diff, glossary, SEO, house rules, structure)
and follow it, with the Tier 3 differences below. Also: `_i18n/nl-tier3-brief.md` (the writers' brief: what they were
allowed to use), `_i18n/nl.md` (sheet, ALL of «Tells to cut»), `_i18n/nl-apple-terms.md`, the app sections of
`_i18n/nl-glossary.md`, `/Users/anttiaittamaa/Downloads/githubcode/nl-tier3-store-2026-11-19.md` (the Dutch App Store
data for each competitor, checked today), `/Users/anttiaittamaa/Downloads/githubcode/nl-tier3-research-2026-11-19.md`
(primaries and keyword evidence) and the writers' notes in
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-UxGsub/f5e34407-a458-4d5c-863d-92d8a8cb7431/scratchpad/nl-t3/notes/<slug>.md`
(each page's known risks: added FAQs, added listing facts, skipped skill passes; check every one).

## Tier 3 checks

1. **Copy-editing**: run the full skill (`~/.claude/skills/copy-editing/SKILL.md`, Seven Sweeps + AI-tell removal) on
   every Dutch string: front matter, body, FAQ, JSON-LD names and answers, alt texts. Several writers do a hand pass only.
2. **Fact diff, two sources**:
   - Our app: every claim must be on the English page (`alternatives/<slug>.html`) or in the Dutch app page /
     `_apps/<app>.md` that feeds both; prices only via tokens (single braces).
   - The competitor: every market-specific fact (price, rating, store name, platforms, languages, in-app rows) must match
     the Dutch store file EXACTLY (U+00A0 between € and the digit, «bekeken op 19 november 2026», Dutch number format
     «41.703», four digits without a dot). US prices, US ratings and US dates must be gone. A period («per maand», «per
     jaar») may be attached to a price only when the store row names it. A competitor feature claim must be on the English
     page or in the Dutch description in the store file; if the page adds one from the description, keep it only if the
     description says it plainly. Added FAQs: keep only if every fact in the answer comes from the English page or the store
     file; the visible question must equal the schema name character for character.
   - Local-only pages (WieBetaaltWat, Dyme): every competitor fact from the store file's description and in-app rows; no
     security, data-use, fee or bank-coverage judgement beyond the listing's own words; marketing claims (user counts,
     savings) attributed or cut; no review quotes. AllPaid and RightSplit facts as in the brief. The Dyme page must stay
     consistent with `nl/guides/bill-tracker-without-bank-connection.html`.
3. **House rules**: «geen abonnement» only for LiftLog. Observa, RightSplit, Chessful, EarnLock, MediaKit, AllPaid are
   never called «zonder abonnement» (titles included: «Whoop-alternatief zonder abonnement» must not read as if Observa had
   none; «zonder verplicht abonnement» is fine where true). Observa's HRV is SDNN; Observa's readiness is «Gereedheid»;
   medical caveats exactly as strong as English. «we/wij» only where the English says "we". No «voorlopig» / «nog niet»
   (implied promises). Disclosure that the app is ours where the English page has one.
4. **SEO**: primaries per page as in nl-tier3-brief.md; no two pages in this batch share a seo.title pattern or primary;
   the three RightSplit pages and the two Observa pages clearly distinct; seo.title ≤ 60 after token expansion,
   description 70 to 155, not opening with a question; seo.keywords only real queries (research file or nl-keywords.md),
   none taken from a Tier 1 or Tier 2 page's primary (list in the writers' brief); visible text uses correct spelling
   («Forest-app», «Chess.com-abonnement»), split search forms only in keywords.
5. **Structure**: JSON-LD skeleton identical to `it/alternatives/<slug>.html` (or the local-only model); parse every
   `<script type="application/ld+json">` block after stripping Liquid (`{{ … }}` → "x", `{% … %}` → "") to catch JSON
   errors; FAQ names equal visible summaries. Typography by script: no straight apostrophes in Dutch prose (foto’s), no
   « », no em/en dashes, every € followed by U+00A0 and a digit (and never U+00A0 inside `{…}` tokens or Liquid tags), no
   space before %, `“…”` for quotes and ‘…’ for UI labels. Links through `{% include l.html url="..." %}`; the local-only
   pages and hub as plain `/nl/alternatives/<slug>/` hrefs; breadcrumb hub name «Vergelijkingen».

## Reply with

Per page: a short change table (field | before | after | why), fact-diff result, and new Dutch tells for the sheet.
Then English-side issues for ISSUES.md (one line each, with file).
