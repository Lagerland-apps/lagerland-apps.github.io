# Reviewer brief: Dutch (nl, Netherlands) Tier 1 pages

For the reviewer agents (TRANSLATION.md section 9). You did not write the pages you review. Never published.
Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit only the Dutch files
you were given.

## Read

`_i18n/nl-writer-brief.md` (the rules the writers followed), `_i18n/nl.md` (je register, vocabulary, typography,
formats, glossary table, language claims, keyword table, tells to cut), `_i18n/nl-apple-terms.md`, your apps' sections
of `_i18n/nl-glossary.md`, and TRANSLATION.md sections 6.2, 7.2, 8 and 9.

## For every page, in this order

1. **Copy-editing.** Read `~/.claude/skills/copy-editing/SKILL.md` (the whole file) and follow it fully (all Seven
   Sweeps plus its AI-tell removal) on every Dutch string: front matter (tagline, quick_answer, seo, hero, who_for,
   value_points, features, how_it_works, plans, comparison labels, faq, captions, alt texts, enrichment), and body
   text. Apply the Dutch tells in TRANSLATION.md 8.2 and the sheet's «Tells to cut». Watch for three-negation lists
   («geen X, geen Y, geen Z»), «het is niet X, het is Y» reveals, trailing comma clauses, calques («maakt zin», «dat
   gezegd hebbende», «gebruiker» everywhere), verb-second word order in subordinate clauses, title case, dashes, split
   compounds. Writers apply the rules by hand only, so this pass matters.
2. **Netherlands Dutch and register.** je/jij/jouw lowercase everywhere; no u/uw. No Flemish words. Apple NL terms.
3. **Fact diff** against the English page (`_apps/<slug>.md` for app pages): every claim, number, feature, caveat and
   qualifier of the English page is present, as strong as in English; nothing is added. Allowed additions only:
   (a) a «Is de app in het Nederlands?» FAQ answered from the glossary's coverage facts (TRANSLATION.md 6.2); for AppMeta
   and Mockly it may only say the interface is English; never name English-only gaps of other apps; (b) «de Nederlandse
   App Store» in place of the English "Prices in USD"; (c) a link to an existing English page with `hreflang="en"` and
   «(in het Engels)». Remove any other added fact (BTW, Dutch law, a competitor detail the English page doesn't have).
   Prices, counts, platforms, trials only through tokens; no typed €, price or count.
4. **Glossary check.** Feature names exactly as the app's Dutch interface shows them. When a writer says a UI string
   was "not verified" or "written from the meaning", look it up in the app's catalog (source folder in
   `_i18n/nl-research-brief.md`; parse `.xcstrings` JSON, locale `nl`, with `python3 -I`, read-only; GymLogger X uses
   JSON tables) and use the real string unless the glossary flags it as defective, or rephrase so it isn't presented
   as a UI label. Apple names per nl-apple-terms.md. Chessful's tier = Pro.
5. **SEO.** `seo.title` ≤ 60 characters after token expansion, keyword-first for the sheet's primary query;
   `seo.description` 70–155 characters containing the primary query (a natural inflection is fine); keywords 5–8,
   lowercase, real queries from nl-keywords.md. `quick_answer` answers the page's question on its own.
5a. **Spelling of search forms.** Visible text (seo.title, H1, description, quick_answer, body, FAQ) uses correct
   Dutch compounds («aftelapp», «schaakapp», «to-dolijst», «app voor krachttraining»); split search forms («aftel app»,
   «schaak app», «to do lijst app») only in `seo.keywords` (sheet, «Search forms vs spelling»). Fix the visible ones.
5b. **Tokens in Dutch sentences.** `{TRIAL}` expands to «gratis proefperiode van 7 dagen» (a noun phrase, lowercase):
   write «met een {TRIAL}», «begint met een {TRIAL}»; at the start of a list item it is fine bare. `{P_LIFETIME}` is a
   price: «{P_LIFETIME} eenmalig». «Prices in USD» becomes «De prijzen zijn die van de Nederlandse App Store; in andere
   landen toont de App Store bij het afrekenen de prijs in je eigen valuta» (allowed, as on other languages).
6. **House rules.** «geen abonnement» only for LiftLog, Millrace, Mockly, Tare. Never the digits 2048 on Millrace.
   Observa HRV = «HRV (SDNN)», never RMSSD as Observa's HRV. No roadmaps. No person's name.
7. **Structure.** Run `python3 scripts/i18n.py check 2>&1 | grep -B1 -A3 "nl/apps/<slug>"` for each page and fix
   source errors. Do NOT run jekyll build, `i18n.py map` or the stamp script. No git commands that write.

## Reply with

Per page: a short table of changes (field | before | after | why), the fact-diff result (missing or added claims and
what you did), UI strings you corrected from the catalog, and new Dutch AI tells worth adding to the sheet. Then
English-side or app-side issues for ISSUES.md.
