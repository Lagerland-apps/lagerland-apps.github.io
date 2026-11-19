# Writer and reviewer brief: Italian privacy policies and terms (it, Italy)

For the agents who write and review the Italian privacy pages. Never published. Repo:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit only the Italian files you were given
(other sessions work on Spanish and Portuguese in this checkout).

Read `_i18n/it-writer-brief.md` (general rules), `_i18n/it.md`, `_i18n/it-apple-terms.md`, TRANSLATION.md 6.2.

These are legal texts. Writers translate the full English policy (`apps/<slug>/privacy/index.html`) with its meaning
exact, using the French twin (`fr/apps/<slug>/privacy/index.html`) only for the key set and Liquid. Reviewers compare
the Italian with the English sentence by sentence:

1. **Meaning is exact.** Every obligation, permission, qualifier («può», «solo», «non», «se», «facoltativo», «sul tuo
   dispositivo», «consapevolmente»), list item and section of the English text is present, in the same order, with the
   same scope. Nothing is added, softened or strengthened. Fix any drift.
2. **Front matter.** `layout: privacy` (or the French twin's layout for Clippet's terms), `slug`, `ref`, `permalink`,
   `translated_from` = English `last_updated`, `last_updated` = the English POLICY date (not today), `title`, seo
   block, the prose keys the English page has (including `refund_requests` where the English has it). Never
   `app_name`, `contact_email`, `back_url`. Unreleased Clippet keeps `sitemap: false` + `noindex: true` as its French
   twin does.
3. **Apple and app terms.** Apple Italy's own words: «Dati non raccolti» (section «Privacy dell’app»), «l’app Salute»
   / «Salute», «Tempo di utilizzo», «In famiglia», «Apple Account», «Impostazioni», «backup su iCloud» / “Backup
   iCloud”, «tracciamento», “Richiesta tracciamento attività”, «identificativo per gli inserzionisti (IDFA)». Menu
   paths with « > » (no arrows). App UI labels quoted only if they are the app's real Italian strings
   (`_i18n/it-glossary.md`).
4. **Register.** Plain, consistent Italian legal language as Italian privacy notices use it (Informativa sulla privacy,
   «trattare / trattamento», «raccogliere», «condividere», «consapevolmente», «titolare del trattamento» only where the
   English names a controller; GDPR terms as the Italian text of the GDPR writes them: «dati personali», «interessato»
   only if the English says "data subject"). One term per concept across all pages. tu throughout (the reader), never
   Lei. No em/en dashes. Sentence case headings. “ ” quotes, typographic ’.
5. **Copy-editing**, lightly: read `~/.claude/skills/copy-editing/SKILL.md` and apply only the sweeps that do not
   change legal meaning (clarity, grammar, AI tells). Precision beats style.
6. **seo**: title ≤ 60 chars, natural («Informativa sulla privacy di <App>»), unique across all Italian privacy pages;
   description 70–155 chars; 5–7 lowercase keywords.
7. The page carries the interface line saying the English text is the reference (the layout prints it from
   `t`; check the French twin for how).
8. Run `python3 scripts/i18n.py check 2>&1 | grep -A3 "it/apps/<slug>/privacy\|it/apps/clippet/terms"`. Do NOT run
   jekyll build, map or stamp.

Reply with: per page, what you changed and why (especially any meaning fix); the term choices you standardized;
legal terms an Italian lawyer should look at (for the language sheet); English-side issues.
