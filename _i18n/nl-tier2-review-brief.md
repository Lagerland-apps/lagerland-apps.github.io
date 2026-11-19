# Reviewer brief: Dutch (nl, Netherlands) Tier 2, batch 1

Never published. Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. You did not write
the pages you review. Edit only the Dutch files you were given. Scratch (below `$S`):
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-MVirY8/10bb35b8-de8b-405d-996b-c7615d2e76fa/scratchpad/nl-t2/`.

## Read

`_i18n/nl-reviewer-brief.md` (the Tier 1 review procedure: follow its steps 1 to 7 on every page), `_i18n/nl-tier2-brief.md`
(what the writers were told for Tier 2), `_i18n/nl.md`, `_i18n/nl-apple-terms.md`, the glossary sections of the apps named,
`/Users/anttiaittamaa/Downloads/githubcode/nl-tier2-research-2026-11-19.md` (queries and Dutch store data), `$S/iap-nl.txt`
(Dutch in-app rows) and `$S/writer-notes.md` (points the writers raised).

## Tier 2 additions to the procedure

1. **Copy-editing**: read `~/.claude/skills/copy-editing/SKILL.md` (the whole file) and run its full Seven Sweeps and AI-tell
   removal on every Dutch string (front matter, body, card text, table cells, alt text, JSON-LD names and answers).
2. **Fact diff** against the English page, section by section: every claim, number, caveat and hedge present and as strong;
   nothing added. Allowed changes: US-only data replaced by Netherlands data from the research file, `$S/iap-nl.txt` or a
   saved store page; facts dropped because the app is not sold in the Netherlands or no Dutch figure exists; the
   I-0349/I-0351/I-0352/I-0310 handling described in the Tier 2 brief. A date copied from the Italian page («bekeken op 1
   oktober 2026» and the like) is only allowed if the English page states that same check date; otherwise use what was
   checked for the Dutch page (19 november 2026) or drop the date.
3. **Competitor data**: every rating, price and store title must match the research file, `$S/iap-nl.txt` or a file in
   `$S/sources/` (open them). A number with no source: remove it. U+00A0 between € and the amount (`€ 3,49`, never «3,49 €»);
   «(Nederlandse App Store, bekeken op 19 november 2026)» once per page. Competitor arithmetic only where the English page
   does the same calculation (check inputs and rounding; one rule for every app).
4. **Local-only page** (nl/guides/schermtijd-beperken-iphone.html): no English twin, so the fact diff is against the sources in
   `$S/sources/schermtijd-beperken-iphone/`, claim by claim. Re-fetch the two Apple Netherlands pages live with curl
   (https://support.apple.com/nl-nl/guide/iphone/iphbfa595995/ios and https://support.apple.com/nl-nl/guide/iphone/iphb0c7313c9/ios)
   and check every Apple label and step against the raw text (earlier reviews in other languages found invented Apple paths,
   reversed on/off labels and dropped conditions). Check each competitor sentence against its saved lookup JSON
   `description` (several listings are English: no Dutch text in quotes presented as the app's own words). EarnLock claims
   against `nl/apps/earnlock/index.md` and APP_BLUEPRINT.md §10 in `~/Downloads/EarnScreen/` (claims register only). Quotes
   under 15 words.
5. **Structure**: JSON-LD valid (strip Liquid tags and parse), `inLanguage` "nl", skeleton as the Italian twin (no ItemList
   inside the breadcrumb), every FAQ `name` identical to its visible `<summary>`, schema answer = visible answer. Tokens
   single-brace and never containing U+00A0. Links through l.html. `seo.title` ≤ 60, description 70–155, keywords 5–8 real
   queries from the research file, none colliding with the Tier 1 app keywords listed in the Tier 2 brief.
6. Run `python3 scripts/i18n.py check 2>&1 | grep -B1 -A3 "<your path>"` per page. Do NOT run jekyll build, i18n.py map or
   the stamp script. No state-changing git commands (other sessions share this checkout).

## Reply with

Per page: a table of changes (field | before | after | why), the fact-diff result, competitor numbers checked (and removed),
new Dutch AI tells for the sheet, and English-side or app-side issues for ISSUES.md.
