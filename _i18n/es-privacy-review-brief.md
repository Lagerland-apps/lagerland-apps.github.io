# Reviewer brief: Spanish privacy policies and terms (es, Spain)

For reviewer agents. You did not write these pages. Never published. Repo:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit only the Spanish files you were given.

Read `_i18n/es-reviewer-brief.md` (general rules), `_i18n/es.md`, `_i18n/es-apple-terms.md`, TRANSLATION.md 6.2.

These are legal texts. For each page, compare with the English page sentence by sentence:

1. **Meaning is exact.** Every obligation, permission, qualifier («may», «only», «not», «if», «optional», «on your
   device», «knowingly»), list item and section of the English text is present, in the same order, with the same
   scope. Nothing is added, softened or strengthened. Fix any drift.
2. **Front matter.** `layout: privacy` (or the French twin's layout for terms), `slug`, `ref`, `permalink`,
   `translated_from` = English `last_updated`, `last_updated` = the English POLICY date (not today), `title`, seo
   block, the prose keys the English page has (including `refund_requests` where the English has it). Never
   `app_name`, `contact_email`, `back_url`. Unreleased Clippet keeps `sitemap: false` + `noindex: true`.
3. **Apple and app terms.** Apple Spain's own words: «No se recopilan datos» (App Store «Privacidad de la app»; not
   «Datos no recopilados»), «Salud» / «Salud de Apple», «Tiempo de uso», «En familia», «cuenta de Apple», «Ajustes»,
   «copia de seguridad en iCloud», rastreo, «Permitir que las apps soliciten rastrearte», «identificador de
   publicidad»/IDFA as es-apple-terms.md says (check; use the file's form). Menu paths with « > » (no arrows →).
   App UI labels quoted only if they are the app's real Spanish strings (`_i18n/es-glossary.md`).
4. **Register.** Plain, consistent Spain legal Spanish: «tratar/tratamiento», «recopilar», «compartir», «a sabiendas».
   One term per concept across all pages you review (make them consistent). tú throughout. No em/en dashes; « > »
   for paths. Sentence case headings.
5. **Copy-editing**, lightly: read `~/.claude/skills/copy-editing/SKILL.md` and apply only the sweeps that do not
   change legal meaning (clarity, grammar, AI tells). Precision beats style.
6. **seo**: title ≤ 60 chars, natural, unique across all Spanish privacy pages; description 70–155 chars;
   5–7 lowercase keywords.
7. Run `python3 scripts/i18n.py check 2>&1 | grep -A3 "es/apps/<slug>/privacy\|es/apps/clippet/terms"`. Do NOT run
   jekyll build, map or stamp.

Reply with: per page, what you changed and why (especially any meaning fix); the term choices you standardized;
legal terms a Spanish lawyer should look at (for the language sheet); English-side issues.
