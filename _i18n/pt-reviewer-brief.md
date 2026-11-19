# Reviewer brief: Portuguese (pt, Portugal) Tier 1 pages

For the reviewer agents (TRANSLATION.md section 9). You did not write the pages you review. Never published.
Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit only the Portuguese files
you were given.

## Read

`_i18n/pt-writer-brief.md` (the rules the writers followed), `_i18n/pt.md` (impersonal register, vocabulary,
typography, formats, glossary table, language claims, keyword table, tells to cut), `_i18n/pt-apple-terms.md`, your
apps' sections of `_i18n/pt-glossary.md`, and TRANSLATION.md sections 6.2, 7.2, 8 and 9.

## For every page, in this order

1. **Copy-editing.** Read `~/.claude/skills/copy-editing/SKILL.md` (the whole file) and follow it fully (all Seven
   Sweeps plus its AI-tell removal) on every Portuguese string: front matter (tagline, quick_answer, seo, hero, who_for,
   value_points, features, how_it_works, plans, comparison labels, faq, captions, alt texts, enrichment), and body
   text. Apply the Portuguese tells in TRANSLATION.md 8.2 and the sheet's «Tells to cut». Watch for three-negation
   lists, «não é X, é Y» reveals, trailing gerunds, calques («a nível de», «fazer sentido» overuse, «jogar um papel»),
   title case, «» quotes, dashes. Most writers apply the rules by hand only, so this pass matters.
2. **European Portuguese and register.** No Brazilian vocabulary or grammar (tela, celular, usuário, arquivo,
   compartilhar, baixar, Ajustes, registrar, salvar, academia, contato, gerund progressives, proclisis at a sentence
   start). Impersonal register: no «você», no tu forms; «o seu / a sua» only where unavoidable. AO90 spelling.
3. **Fact diff** against the English page (`_apps/<slug>.md` for app pages): every claim, number, feature, caveat and
   qualifier of the English page is present, as strong as in English; nothing is added. Allowed additions only:
   (a) a «A app está em português?» FAQ answered from the glossary's coverage facts (TRANSLATION.md 6.2), never for
   Mockly, without naming English-only gaps; (b) «App Store de Portugal» in place of the English "Prices in USD";
   (c) a link to an existing English page with `hreflang="en"` and «(em inglês)». Remove any other added fact (a
   sentence about IVA, local laws, or a competitor detail the English page doesn't have). Prices, counts, platforms,
   trials only through tokens; no typed €, price or count.
4. **Glossary check.** Feature names exactly as the app's pt-PT interface shows them. When a writer says a UI string
   was "not verified" or "written from the meaning", look it up in the app's catalog (source folder named in
   pt-glossary.md under `~/Downloads/<folder>/`; parse `.xcstrings` JSON, locale `pt-PT`, with `python3`, read-only;
   GymLogger X: `GymLogger/Localizations/pt.json`) and use the real string unless the glossary flags it as Brazilian,
   or rephrase so it isn't presented as a UI label. Apple names per pt-apple-terms.md. Chessful's tier = Pro.
5. **SEO.** `seo.title` ≤ 60 characters after token expansion, keyword-first for the sheet's primary query;
   `seo.description` 70–155 characters containing the primary query (a natural inflection is fine); keywords 5–8,
   lowercase, real queries from pt-keywords.md. `quick_answer` answers the page's question on its own.
6. **House rules.** «sem subscrição» only for LiftLog, Millrace, Mockly, Tare. Never the digits 2048 on Millrace.
   Observa HRV = «VFC (SDNN)», never RMSSD as Observa's HRV. No roadmaps. No person's name.
7. **Structure.** Run `python3 scripts/i18n.py check 2>&1 | grep -B1 -A3 "pt/apps/<slug>"` for each page and fix
   source errors. Do NOT run jekyll build, `i18n.py map` or the stamp script.

## Reply with

Per page: a short table of changes (field | before | after | why), the fact-diff result (missing or added claims and
what you did), UI strings you corrected from the catalog, and new Portuguese AI tells worth adding to the sheet. Then
English-side or app-side issues for ISSUES.md.
