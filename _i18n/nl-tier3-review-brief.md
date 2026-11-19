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

## Batch 2 (2026-11-19)

Same method. Store and web data: `/Users/anttiaittamaa/Downloads/githubcode/nl-tier3-store-batch2-2026-11-19.md`. Writer rules:
the «Batch 2» section of nl-tier3-brief.md. Writers' notes:
`/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/f5e34407-a458-4d5c-863d-92d8a8cb7431/scratchpad/nl-t3b2/notes/<slug>.md`.
Extra checks:
- HandBrake and CloudConvert are a desktop app and a web service: facts only from the store file's web sections; no App Store
  claim or rating for HandBrake; no CloudConvert rating (★6); no paid CloudConvert amounts (not in the fetched page); no
  security verdict for «cloudconvert betrouwbaar».
- Tikkie page: RightSplit never moves money; payment links exactly as the blueprint (PayPal.me and Revolut prefill; Venmo and
  Wise open the profile; IBAN and Apple Pay no link; no iDEAL); Tikkie's «veilig» sentence never repeated as fact; no other
  payment services named; honest «Tikkie is the tool for getting paid» framing kept.
- Sleep Cycle page: Observa has no alarm and records no sound; no medical claims; Premium rows have no period.
- Welltory, Bevel, Sleep Cycle: health caveats exactly as strong as English; Observa HRV (SDNN), «Gereedheid»,
  «zonder verplicht abonnement».
- Distinct primaries and seo.title patterns across all 20 Dutch comparisons (batch 1 is in nl/alternatives/ too).
- Every batch 1 tell («From the Tier 3 reviews» in nl.md) applies: check for each.

## Batch 3 (2026-11-19)

Same method and the batch 2 checks. Store and web data: `/Users/anttiaittamaa/Downloads/githubcode/nl-tier3-store-batch3-2026-11-19.md`.
Writer rules: the «Batch 3» section of nl-tier3-brief.md. Writers' notes:
`/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/f5e34407-a458-4d5c-863d-92d8a8cb7431/scratchpad/nl-t3b3/notes/<slug>.md`.
Extra checks: grep every Millrace page for «2048» (must be zero); Brick and Unpluq pages give no device price; Tare's hint and star rules
exactly as the brief; the six EarnLock pages and all 30 Dutch comparisons have distinct primaries and seo.title formulas; every batch 1
and 2 tell in nl.md checked.

## Batch 4 (2026-11-19)

Same method and the batch 2 and 3 checks. Store data: `/Users/anttiaittamaa/Downloads/githubcode/nl-tier3-store-batch4-2026-11-19.md`.
Writer rules: the «Batch 4» section of nl-tier3-brief.md. Writers' notes:
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-9yVUda/ece2d429-efbb-49e4-9722-d366e374c50a/scratchpad/nl-t3b4/notes/<slug>.md`.
Extra checks:
- Every competitor price against the store file row by row: a period only where the row names one («Premium» rows on Way of Life,
  «Sleep Improvement Membership» on RISE, «Premium» on iZip, unlabelled Ladder and Magnus Trainer rows have none); ranges cover all
  rows of a plan; «(Legacy Pricing)» / «[Legacy]» rows left out or only said to exist.
- «NL UI» claims only from the store file (RISE has a Dutch store title but no Dutch in its language list; Productive, Jefit, Ladder,
  Athlytic, Gentler Streak, Compress Videos, iZip, Chessable, Magnus Trainer have no Dutch).
- Taskful Day is a day planner, not a habit tracker; ISSUES I-0391 (no promise that a typed Dutch sentence becomes a dated task).
- Millrace page (kami-2): zero «2048». LiftLog (ladder) may say «geen abonnement»; no other app may.
- Observa (athlytic, gentler-streak): HRV (SDNN), «Gereedheid», never «zonder abonnement», caveats as strong as English.
- AfterShift (rise-sleep-tracker, supershift-alternatief): no medical claims; Supershift's «meest gedownloade» claim never repeated;
  no claim that Supershift export and AfterShift calendar import were tested together.
- Distinct primaries and seo.title formulas across all 51 Dutch comparisons, especially within Taskful Day (3), Observa (8),
  MediaKit (7), GymLogger X (6), EarnLock (7), Chessful (4), RightSplit (5).
