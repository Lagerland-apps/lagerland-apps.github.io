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
