# Reviewer brief: Italian (it, Italy) Tier 1 pages

For the reviewer agents (TRANSLATION.md section 9). You did not write the pages you review. Never published.
Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit only the Italian files
you were given (other sessions work on Spanish and Portuguese in this checkout).

## Read

`_i18n/it-writer-brief.md` (the rules the writers followed), `_i18n/it.md` (register tu, typography, formats,
glossary table, tier names, keyword table, tells to cut), `_i18n/it-apple-terms.md`, your apps' sections of
`_i18n/it-glossary.md`, and TRANSLATION.md sections 6.2, 7.2, 8 and 9.

## For every page, in this order

1. **Copy-editing.** Read `~/.claude/skills/copy-editing/SKILL.md` and follow it fully (all Seven Sweeps plus its
   AI-tell removal) on every Italian string: front matter (tagline, quick_answer, seo, hero, who_for, value_points,
   features, how_it_works, plans, comparison labels, faq, captions, alt texts, enrichment), and body text. Apply the
   Italian tells in TRANSLATION.md 8.2 and the sheet's «Tells to cut». Watch for three-negation lists, «non è X, è Y»
   reveals, trailing gerunds, calques («fare senso», «giocare un ruolo», «a livello di», «supportare» for "support a
   feature" where «è compatibile con» / «funziona con» is natural), needless anglicisms, title case, “ ” quotes (never « »), no space before %, App Store bare after prepositions,
   straight apostrophes, dashes, Lei forms or voi to one reader, tu everywhere. Most writers applied the rules by
   hand only, so this pass matters.
2. **Fact diff** against the English page (`_apps/<slug>.md` for app pages): every claim, number, feature, caveat and
   qualifier of the English page is present; nothing is added. Allowed additions only: (a) a «X è in italiano?» FAQ
   answered from the glossary's coverage facts (TRANSLATION.md 6.2), without naming English-only gaps; (b) «App Store
   italiano» in place of the English "Prices in USD"; (c) a link to an existing English page with `hreflang="en"` and
   «(in inglese)». Remove any other added fact (IVA, local laws, competitor details the English page doesn't have).
   Prices, counts, platforms, trials only through tokens; no typed €, price or count.
3. **Glossary check.** Feature names exactly as the app's Italian interface shows them. When a writer says a UI
   string was "not verified" or "written from the meaning", look it up in the app's catalog (source folder named in
   it-glossary.md under `~/Downloads/<folder>/`; parse `.xcstrings` JSON, `it` locale, with `python3 -I`,
   read-only) and use the real string, or rephrase so it isn't presented as a UI label. Apple names per
   it-apple-terms.md. Tier names per the sheet.
4. **SEO.** `seo.title` ≤ 60 characters after token expansion, keyword-first for the sheet's primary query;
   `seo.description` 70–155 characters containing the primary query (a natural inflection is fine); keywords 5–8,
   lowercase, real queries from it-keywords.md. `quick_answer` answers the page's question on its own.
5. **House rules.** «senza abbonamento» only for LiftLog, Millrace, Mockly, Tare. Never the digits 2048 on Millrace.
   Observa HRV = SDNN, never RMSSD as Observa's HRV. No roadmaps. No person's name.
6. **Structure.** Run `python3 scripts/i18n.py check 2>&1 | grep -B1 -A3 "it/apps/<slug>"` for each page and fix
   source errors. Do NOT run jekyll build, `i18n.py map` or the stamp script.

## Reply with

Per page: a short table of changes (field | before | after | why), the fact-diff result (missing or added claims and
what you did), UI strings you corrected from the catalog, and new Italian AI tells worth adding to the sheet. Then
English-side or app-side issues for ISSUES.md.
