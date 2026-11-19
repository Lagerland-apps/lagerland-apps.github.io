# Reviewer brief: Portuguese (pt, Portugal) Tier 3, batch 1 (comparison pages)

Never published. Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. You did not write
the pages you review. Edit only the Portuguese files you were given. Scratch:
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-vvPVmP/a07fe73c-d938-475e-b597-e41503062630/scratchpad/pt-t3/`.

## Read

`_i18n/pt-reviewer-brief.md` (the Tier 1 review procedure: follow its steps on every page), `_i18n/pt-tier3-brief.md`
(what the writers were told), `_i18n/pt.md` (all of it, especially the tells to cut), `_i18n/pt-apple-terms.md`, the
glossary sections of the apps named, `/Users/anttiaittamaa/Downloads/githubcode/pt-tier3-research-2026-11-19.md`
(queries) and `/Users/anttiaittamaa/Downloads/githubcode/pt-tier3-store-2026-11-19.md` (Portuguese store data).

## Procedure, per page

1. **Copy-editing**: read `~/.claude/skills/copy-editing/SKILL.md` (the whole file) and run its full Seven Sweeps and
   AI-tell removal on every Portuguese string (front matter, body, table cells, card text, alt text, JSON-LD names and
   answers). European Portuguese only, impersonal register, AO90, the sheet's typography (« », U+00A0 before €, no
   dashes, sentence case). Fix in place.
2. **Fact diff** against the English page `alternatives/<slug>.html`, section by section: every claim, number, caveat
   and hedge present and as strong; nothing added. Allowed changes: US competitor data replaced by Portuguese store data
   from the store file; a competitor number dropped because no Portuguese figure exists; the I-0369 (WHOOP «subscrição
   opcional»), I-0174 (no unverified WHOOP price) handling in the writer brief.
3. **Competitor data**: every rating, price and store title must match the store file. A number with no source there:
   remove it. «(App Store de Portugal, consultado a 19 de novembro de 2026)» once per page. Competitor arithmetic only
   where the English page does the same calculation (check inputs and rounding).
4. **Our app**: every claim about our app as on the English page and the Portuguese app page `pt/apps/<app>/index.md`
   (same feature and tier names). Prices only via single-brace tokens. «Sem subscrição» only for LiftLog. Observa «VFC
   (SDNN)», never RMSSD as its HRV.
5. **Structure and SEO**: JSON-LD valid (strip Liquid tags and parse), `inLanguage` "pt-PT", skeleton as the Spanish
   twin, breadcrumb hub «Comparações» at `/pt/alternatives/`, every FAQ `name` identical to its visible `<summary>`,
   schema answer = visible answer. Links through l.html. `seo.title` ≤ 60 characters after tokens, description 70 to
   155, keywords 5 to 8 real queries from the research file or pt-keywords.md (European forms only), primary query in
   seo.title, H1 and quick_answer; no collision with the keywords the writer brief reserves.
6. Run `python3 scripts/i18n.py check 2>&1 | grep -B1 -A3 "<your path>"` per page. Do NOT run jekyll build, i18n.py map
   or the stamp script. No state-changing git commands (other sessions share this checkout).

## Reply with

Per page: a short table of changes (field | before | after | why), the fact-diff result, competitor numbers checked (and
removed), new Portuguese AI tells for the sheet, and English-side or app-side issues for ISSUES.md.
