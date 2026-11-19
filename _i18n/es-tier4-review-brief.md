# Reviewer brief: Spanish (es, Spain) Tier 4, batch 1 (journal posts)

For reviewer agents (TRANSLATION.md section 9). You did not write the posts you review. Never published.
Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit only the Spanish files you
were given. Other sessions (nl, fr, de, it, pt) work in this same checkout: no git commands that change state, no builds.

## Read

`_i18n/es-reviewer-brief.md` (the general Spanish review steps), `_i18n/es-tier4-brief.md` (the rules the writers
followed, with the per-post notes), `_i18n/es-writer-brief.md`, `_i18n/es.md` (register tú, typography, glossary,
tier names, keyword tables, every «Decisions» and «Tells to cut» section), `_i18n/es-apple-terms.md`, your apps'
sections of `_i18n/es-glossary.md`, TRANSLATION.md 6.5, 6.7, 7.2, 8, 9.

## For every post, in this order

1. **Copy-editing.** Read `~/.claude/skills/copy-editing/SKILL.md` and follow it fully (Seven Sweeps plus AI-tell
   removal) on every Spanish string: title, seo, lede, quick_answer, excerpt, faq, body, table cells, link texts,
   read_time. Spanish tells: TRANSLATION.md 8.2 and the sheet. Spain vocabulary, tú, ¿¡, «», sentence case, no
   dashes (em or en), no Oxford comma, U+00A0 before %, €, $, units and «min», decimal comma, 8000 vs 10.000.
   Gendered words addressed to the reader. Trailing gerunds. Calques.
2. **Fact diff against the English post** `_journal/<slug>.md`, sentence by sentence: every number, study, author,
   year, table row, caveat, hedge («about», «often», «may», «in one study») and qualifier present with the same
   strength; nothing added. Recompute every worked example converted to kg or written with Spanish number format.
   Allowed changes only: US context replaced by Spain context from a source the writer saved (step 3), metric
   conversion, «App Store de España», links to Spanish pages, «(en inglés)» markers.
3. **Sources (YMYL additions and the local-only page).** The writer saved fetched pages under
   `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-QSBGdz/ae3f3811-617e-4206-99a4-9a9124fc8c81/scratchpad/es-t4/sources/<slug>/`.
   Re-fetch each one live (`curl -sL`, strip HTML with `python3 -I`) and check every Spain claim against it, claim by
   claim. Remove or soften any claim no source supports. Check that no quote is over 15 words and no sentence is a
   near-verbatim copy. For the local-only page every fact must come from a saved source, the two English posts it
   names, or AfterShift's facts.
4. **App claims.** Against `_apps/<slug>.md`, the Spanish app page `es/apps/<slug>/index.md`, the glossary and the
   app's APP_BLUEPRINT.md §10 (path in `~/Downloads/githubcode/.agents/product-marketing.md`). UI strings exactly as
   the Spanish catalog shows them; when in doubt read the `.xcstrings` (`es` or `es-ES`, `python3 -I`, read-only;
   source folders in es-glossary.md). Prices only through tokens, single braces. House rules: «sin suscripción» only for
   LiftLog, Millrace, Mockly, Tare; Observa HRV = VFC (SDNN); no roadmaps; no person's name.
5. **SEO and structure.** seo.title ≤ 60 characters keyword-first for the brief's primary query; description 70–155 with
   the query; keywords 5–8 lowercase real queries, none owned by another Spanish page (the brief's collision list);
   quick_answer answers the query on its own; every English FAQ kept, each ¿…?; front matter per the brief (ref,
   permalink, translated_from = English last_updated, date and last_updated 2026-11-19, mentioned_apps copied;
   local-only: `local_only: true`, no ref, no translated_from); read_time = body words ÷ 200 («N min de lectura» with
   U+00A0). Links: Spanish targets only where the page exists (`ls es/...`, plus the ten posts of this batch); English
   targets with `{: hreflang="en"}` and «(en inglés)», Spanish link text. Run
   `python3 scripts/i18n.py check 2>&1 | grep -B1 -A3 "es/journal/<slug>"` and fix source errors.

## Reply with

Per post: a table of changes (where | before | after | why), the fact-diff result (claims missing or added and what you
did), source checks (claim → source → verdict), UI strings corrected from the catalog, then new Spanish tells worth
adding to the sheet, and English-side or app-side issues for ISSUES.md.
