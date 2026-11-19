# Reviewer brief: Portuguese (pt, Portugal) Tier 2, batch 1

Never published. Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. You did not write
the pages you review. Edit only the Portuguese files you were given. Scratch: `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-n8q8Hr/80c59503-7bb0-423d-955c-db00baf42c73/scratchpad/pt-t2/`.

## Read

`_i18n/pt-reviewer-brief.md` (the Tier 1 review procedure: follow its steps 1 to 6 on every page), `_i18n/pt-tier2-brief.md`
(what the writers were told for Tier 2), `_i18n/pt.md`, `_i18n/pt-apple-terms.md`, the glossary sections of the apps named,
and `/Users/anttiaittamaa/Downloads/githubcode/pt-tier2-research-2026-11-19.md` (queries and Portuguese store data).

## Tier 2 additions to the procedure

1. **Copy-editing**: read `~/.claude/skills/copy-editing/SKILL.md` (the whole file) and run its full Seven Sweeps and AI-tell
   removal on every Portuguese string (front matter, body, card text, table cells, alt text, JSON-LD names and answers).
2. **Fact diff** against the English page, section by section: every claim, number, caveat and hedge present and as strong;
   nothing added. Allowed changes: US-only data replaced by Portugal data from the research file or a saved store page;
   facts dropped because the app is not sold in Portugal or no Portuguese figure exists; «A app está em português?»-type
   language facts for our apps from the glossary (never for Mockly); I-0349/I-0351/I-0352 handling described in the
   Tier 2 brief.
3. **Competitor data**: every rating, price and store title must match the research file or a file saved in
   `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-n8q8Hr/80c59503-7bb0-423d-955c-db00baf42c73/scratchpad/pt-t2/sources/competitors/` (open them). A number with no source: remove it. Prices with U+00A0 before €; «(App Store
   de Portugal, consultado a 19 de novembro de 2026)» once per page. Competitor arithmetic only where the English page
   does the same calculation (check the inputs and the rounding).
4. **Local-only page** (pt/guides/limitar-tempo-de-ecra-iphone.html): no English twin, so the fact diff is against the sources
   in `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-n8q8Hr/80c59503-7bb0-423d-955c-db00baf42c73/scratchpad/pt-t2/sources/limitar-tempo-de-ecra-iphone/`, claim by claim. Re-fetch the two Apple Portugal pages live
   (https://support.apple.com/pt-pt/guide/iphone/iphbfa595995/ios and https://support.apple.com/pt-pt/guide/iphone/iphb0c7313c9/ios)
   with curl and check every Apple label and step against the raw text (earlier reviews found invented Apple paths and
   reversed meanings). Check each competitor sentence against its saved lookup JSON `description`. EarnLock claims against
   `pt/apps/earnlock/index.md` and APP_BLUEPRINT.md §10 in `~/Downloads/EarnScreen/` (claims register only). Quotes under
   15 words.
5. **Structure**: JSON-LD valid (strip Liquid tags and parse), `inLanguage` "pt-PT", skeleton as the Spanish twin (no
   ItemList inside the breadcrumb), every FAQ `name` identical to its visible `<summary>`, schema answer = visible answer.
   Tokens single-brace. Links through l.html. `seo.title` ≤ 60, description 70–155, keywords 5–8 real queries from the
   research file (European forms only: «principiantes», never Brazilian «iniciantes», «academia», «celular», «tela»).
6. Run `python3 scripts/i18n.py check 2>&1 | grep -B1 -A3 "<your path>"` per page. Do NOT run jekyll build, i18n.py map or
   the stamp script. No state-changing git commands (other sessions share this checkout).

## Known points from the writers' reports to check

- Chess: keyword «melhor app de xadrez para iniciantes» is Brazilian; Chess.com price range «entre 5,49 € e 109,99 €» (check
  sources/competitors/chesscom.html); «vs Chessis» link kept although Chessis is not in the Portuguese store.
- Workout: only 4 keywords (needs 5 to 8, real queries without colliding with GymLogger X's «app treino ginásio grátis»); the
  ten-year box numbers (lowest monthly × 120: Strong 4,99 €, Hevy 3,49 €, Fitbod 10,99 €) against the saved store pages.
- Xiangqi: a FAQ was replaced (Tiantian not sold in Portugal); the Best XiangQi tracking sentence could not be checked
  against the Portuguese privacy label (rests on the English page: keep it as strong as English, no stronger).
- Apple Health: Observa «Prontidão» (app term) vs Apple «Preparação»: keep Observa's term only where it names Observa's score.
- Shift workers: no labour-law or health claims beyond English.

## Reply with

Per page: a table of changes (field | before | after | why), the fact-diff result, competitor numbers checked (and removed),
new Portuguese AI tells for the sheet, and English-side or app-side issues for ISSUES.md.
