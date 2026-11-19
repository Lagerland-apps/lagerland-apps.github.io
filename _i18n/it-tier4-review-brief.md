# Reviewer brief: Italian (it, Italy) Tier 4, batch 1 (journal posts)

For reviewer agents (TRANSLATION.md section 9). You did not write the posts you review. Never published.
Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit only the Italian post files you
were given. Other sessions (nl, es, pt) work in this same checkout: no git commands that change state, no builds.

## Read

`_i18n/it-reviewer-brief.md` (the general Italian review steps), `_i18n/it-tier4-brief.md` (the rules the writers
followed, with the per-post notes), `_i18n/it-writer-brief.md`, `_i18n/it.md` (register tu, typography, glossary, tier
names, keyword tables, every «Decisions» and «Tells» section), `_i18n/it-apple-terms.md`, your apps' sections of
`_i18n/it-glossary.md`, TRANSLATION.md 6.5, 6.7, 7.2, 8, 9.

## For every post, in this order

1. **Copy-editing.** Read `~/.claude/skills/copy-editing/SKILL.md` and follow it fully (Seven Sweeps plus AI-tell
   removal) on every Italian string: title, seo, lede, quick_answer, excerpt, faq, body, table cells, link texts,
   read_time. Italian tells: TRANSLATION.md 8.2 and the sheet. tu, “ ” quotes, typographic ’, sentence case, no dashes
   (em or en), no Oxford comma, U+00A0 before €, $, units and «min», no space before %, decimal comma, 8000 vs 10.000.
   Gendered words addressed to the reader. Trailing gerunds. Calques. Gym words as the brief lists them.
2. **Fact diff against the English post** `_journal/<slug>.md`, sentence by sentence: every number, study, author, year,
   table row, caveat, hedge («about», «often», «may», «in one study») and qualifier present with the same strength;
   nothing added. Recompute every worked example converted to kg or written in Italian number format. Allowed changes
   only: US context replaced by Italian context from a source the writer saved (step 3), metric conversion, links to
   Italian pages, «(in inglese)» markers.
3. **Sources (YMYL additions and the local-only page).** The writer saved fetched pages under
   `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-d7tDJh/69d88126-1df9-4e51-857f-b06117579141/scratchpad/it-t4/sources/<slug>/`.
   Re-fetch each one live (`curl -sL` with a Safari UA, strip HTML with `python3 -I`) and check every Italian claim
   against it, claim by claim. Remove or soften any claim no source supports. No quote over 15 words, no near-verbatim
   sentence. For the local-only holiday post: every holiday, date and law reference must come from a saved source;
   recompute every 2027 weekday (`python3 -c "import datetime; print(datetime.date(2027,10,4).strftime('%A'))"`) and every
   ponte.
4. **App claims.** Against `_apps/<slug>.md`, the Italian app page `it/apps/<slug>/index.md`, the glossary and the app's
   APP_BLUEPRINT.md §10 (path in `~/Downloads/githubcode/.agents/product-marketing.md`). UI strings exactly as the Italian
   catalog shows them; when in doubt read the `.xcstrings` (`it`, `python3 -I`, read-only; source folders in
   it-glossary.md). Prices only through tokens, single braces. House rules: «senza abbonamento» only for LiftLog,
   Millrace, Mockly, Tare; Observa HRV (SDNN), never «VFC», never RMSSD as Observa's; no roadmaps; no person's name.
5. **SEO and structure.** seo.title ≤ 60 characters keyword-first for the brief's primary query; description 70–155 with
   the query, not opening with a question; keywords 5–8 lowercase real queries, none owned by another Italian page (the
   brief's collision list); quick_answer answers the query on its own, not opening with a self-answered keyword question;
   every English FAQ kept; front matter per the brief (ref, permalink, translated_from = English last_updated, date and
   last_updated 2026-11-19, mentioned_apps copied; local-only: `local_only: true`, no ref, no translated_from); read_time
   = body words ÷ 200 («N min di lettura» with U+00A0). Links: Italian targets only where the page exists (`ls it/...`,
   plus the ten posts of this batch); English targets with `{: hreflang="en"}` and «(in inglese)», Italian link text. Run
   `python3 scripts/i18n.py check 2>&1 | grep -B1 -A3 "it/journal/<slug>"` and fix source-side errors.

## Reply with

Per post: a table of changes (where | before | after | why), the fact-diff result (claims missing or added and what you
did), source checks (claim → source → verdict), UI strings corrected from the catalog, then new Italian tells worth
adding to the sheet, and English-side or app-side issues for ISSUES.md.
