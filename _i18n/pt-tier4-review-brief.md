# Reviewer brief: Portuguese (pt, Portugal) Tier 4, batch 1 (journal posts)

For reviewer agents (TRANSLATION.md section 9). You did not write the posts you review. Never published.
Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit only the Portuguese files you
were given. Other sessions (nl, es, it) work in this same checkout: no git commands that change state, no builds.

## Read

`_i18n/pt-reviewer-brief.md` (the general Portuguese review steps), `_i18n/pt-tier4-brief.md` (the rules the writers
followed, with the per-post notes and the keyword collision list), `_i18n/pt-writer-brief.md`, `_i18n/pt.md` (impersonal
register, typography, glossary, keyword tables, every «Decisions» and «Tells to cut» section: those are known must-fix
items), `_i18n/pt-apple-terms.md`, your apps' sections of `_i18n/pt-glossary.md`, TRANSLATION.md 6.5, 6.7, 7.2, 8, 9.

## For every post, in this order

1. **Copy-editing.** Read `~/.claude/skills/copy-editing/SKILL.md` and follow it fully (Seven Sweeps plus AI-tell removal)
   on every Portuguese string: title, seo, lede, quick_answer, excerpt, faq, body, table cells, link texts, read_time.
   Portuguese tells: TRANSLATION.md 8.2 and the sheet. European Portuguese only (AO90; never academia, celular, tela,
   usuário, arquivo, baixar, «está fazendo», «porcentagem», «filhote»); impersonal register (never você, never tu forms;
   «o seu / a sua» only where unavoidable); «…» quotes; sentence-case headings; no em or en dashes; no comma before e/ou;
   U+00A0 before €, $, units and «min», NO space before %; decimal comma; 8000 vs 10 000 (U+00A0). Gendered words addressed
   to the reader. Trailing gerunds. Calques. App names with the masculine article («o Observa»), «a app».
2. **Fact diff against the English post** `_journal/<slug>.md`, sentence by sentence: every number, study, author, year,
   table row, caveat, hedge («about», «often», «may», «in one study») and qualifier present with the same strength;
   nothing added. Recompute every worked example converted to kg/km or written with Portuguese number format. Allowed
   changes only: US context replaced by Portugal context from a source the writer saved (step 3), metric conversion,
   «App Store de Portugal», links to Portuguese pages, «(em inglês)» markers.
3. **Sources (YMYL additions, Portugal replacements and the local-only post).** The writer saved fetched pages under
   `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-NWyIpj/dc12c9e7-7c3a-4bcf-a153-f479639bd3fa/scratchpad/pt-t4/sources/<slug>/`.
   Re-fetch each one live (`curl -sL`, strip HTML with `python3 -I`) and check every Portugal claim against it, claim by
   claim. Remove or soften any claim no source supports. Check that no quote is over 15 words and no sentence is a
   near-verbatim copy. For the local-only post every fact must come from a saved source or MediaKit's facts.
4. **App claims.** Against `_apps/<slug>.md`, the Portuguese app page `pt/apps/<slug>/index.md`, the glossary and the app's
   APP_BLUEPRINT.md §10 (path in `~/Downloads/githubcode/.agents/product-marketing.md`). UI strings exactly as the pt-PT
   catalog shows them (unless the glossary flags them as Brazilian); when in doubt read the `.xcstrings` (`pt-PT`,
   `python3 -I`, read-only; source folders in pt-glossary.md). Prices only through tokens, single braces, never «€».
   House rules: «sem subscrição» only for LiftLog, Millrace, Mockly, Tare; Observa HRV = VFC (SDNN); Millrace never
   with the number title or the digits 2048; no roadmaps; no person's name.
5. **SEO and structure.** seo.title ≤ 60 characters keyword-first for the brief's primary query; description 70–155 with the
   query; keywords 5–8 lowercase real queries in pt-PT phrasing, none on the collision list; quick_answer answers the
   query on its own; every English FAQ kept; front matter per the brief (ref, permalink, translated_from = English
   last_updated, date and last_updated 2026-11-19, mentioned_apps copied; local-only: `local_only: true`, no ref, no
   translated_from); read_time = body words ÷ 200 («N min de leitura» with U+00A0). Links: Portuguese targets only where
   the page exists (`ls pt/...`, plus the ten posts of this batch); English targets with `{: hreflang="en"}` and
   «(em inglês)», Portuguese link text. Run `python3 scripts/i18n.py check 2>&1 | grep -B1 -A3 "pt/journal/<slug>"` and fix
   source errors.

## Reply with

Per post: a table of changes (where | before | after | why), the fact-diff result (claims missing or added and what you
did), source checks (claim → source → verdict), UI strings corrected from the catalog, then new Portuguese tells worth adding
to the sheet, and English-side or app-side issues for ISSUES.md. Also give the final seo.title and H1, and the corrected
llms.txt routing line if the writer's no longer matches the post.
