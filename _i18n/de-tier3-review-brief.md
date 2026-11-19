# Reviewer brief: German (de) Tier 3, batch 4 (comparison pages), 2026-11-19

Never published. Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.
You did not write these pages. You review a group of German comparison pages, fix what you find directly in those
files, and report. Writers worked from `_i18n/de-tier3-brief.md`: read it first, it is the spec you check against.

## Read

1. `_i18n/de-tier3-brief.md` (the writer spec, including keyword table and competitor-fact rules).
2. `_i18n/de.md` (sheet), all of it, especially «Tells to cut in German».
3. `TRANSLATION.md` sections 6.4, 6.7, 7.2, 8 and 9.
4. The copy-editing skill: `~/.claude/skills/copy-editing/SKILL.md` (full Seven Sweeps plus its AI-tell removal),
   applied to German text. House rules in TRANSLATION.md 8.3 and the sheet win over the skill.
5. `/Users/anttiaittamaa/Downloads/githubcode/de-tier3-store-2026-11-19.md` (German store facts, checked today).
6. For each page: the English source `alternatives/<slug>.html` (none for the local-only Splid page), the German app
   page `de/apps/<app>/index.md`, the app's section of `_i18n/de-glossary.md`, `_i18n/de-apple-terms.md`, and the
   app's blueprint §10 (paths in `/Users/anttiaittamaa/Downloads/githubcode/.agents/product-marketing.md`).

## Per page, in this order

1. **Copy-editing** (Seven Sweeps) on every German text: body, title, seo.title/description, quick_answer, FAQ (visible
   and JSON-LD), table cells, card text, alt text. Cut AI tells and translationese (sheet list + TRANSLATION.md 8.2
   de row): stacked noun chains, „nicht nur … sondern auch“, stock openers/closers, „gilt als“, „gebaut für“, filler
   „dort“, one-line closers, forced triads, sales language, a first paragraph that repeats the lede, keyword-stuffed
   headings. Make it read like a careful German writer: natural word order, du everywhere (no Sie/Ihr), „…“ quotes,
   decimal comma, U+00A0 before €, „25 %“, closed or hyphenated compounds, no em/en dashes, no Oxford comma.
2. **Fact diff against English**, claim by claim: nothing about OUR app added, dropped, softened or hardened (hedges,
   caveats, conditions, tier boundaries free vs Pro/Premium/Pro+, platforms). Rewrites drop facts most often in
   triads, qualifiers and lists. Tokens only for our prices; single braces; „ohne Abo“ only for LiftLog, Millrace,
   Mockly, Tare; Observa HRV = SDNN; health caveats as strong as English.
3. **Competitor facts against the German store file**: every euro price, rating, language, device and feature claim
   must be in the store file (or the English page for how the product works). US prices or dollar conversions are
   errors. Each price block carries the „Stand 19. November 2026“ / „im deutschen App Store geprüft“ line. For the
   local-only Splid page, every Splid claim must be in the store file's Splid section.
4. **Our-app claims against the blueprint §10 and the German app page/glossary**: feature and tier names as the German
   UI and page name them; nothing from §8/§9.
5. **SEO and structure**: seo.title ≤ 60 (aim 55), description 70 to 155 chars, keyword-first for the primary in the
   brief table, unique on /de/ (grep `de/` for duplicate titles/descriptions), 5 to 8 lowercase keywords from the brief
   table or de-keywords.md, no collision keyword as seo.title/primary. Front matter per the brief (ref,
   translated_from = English last_updated, permalink, last_updated 2026-11-19; Splid: local_only true, no ref, no
   translated_from). JSON-LD skeleton identical to the German model page (WebPage + BreadcrumbList „Alternativen“,
   FAQPage; `"inLanguage": "de"`), valid JSON (check with python after Liquid tags are stripped or by eye), FAQ
   `name` equal to its `<summary>` character for character. Internal links via `{% include l.html url=... %}` as in
   the model pages; plain `/de/...` only for local-only pages and the hub.
6. **Glossary**: feature names match the German app UI (glossary); Apple terms from de-apple-terms.md.

Fix every must-fix directly in the German page (use Edit). Don't touch any other file. Don't run jekyll, i18n.py,
the stamp script or git commands that change state; other sessions (nl, fr, es, it, pt) share this checkout.

## Report back

Per page: the must-fix items you fixed (one line each: what was wrong → what it is now), anything you couldn't
resolve, English-side errors found (with the English line), and new German tells worth adding to the sheet. Then a
count of fixes per page.
