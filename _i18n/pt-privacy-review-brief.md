# Reviewer brief: Portuguese privacy policies and terms (pt, Portugal)

For reviewer agents. You did not write these pages. Never published. Repo:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit only the Portuguese files you were given.

Read `_i18n/pt-reviewer-brief.md` (general rules), `_i18n/pt.md`, `_i18n/pt-apple-terms.md`, TRANSLATION.md 6.2.

These are legal texts. For each page, compare with the English page sentence by sentence:

1. **Meaning is exact.** Every obligation, permission, qualifier («may», «only», «not», «if», «optional», «on your
   device», «knowingly»), list item and section of the English text is present, in the same order, with the same
   scope. Nothing is added, softened or strengthened. Fix any drift.
2. **Front matter.** `layout: privacy` (or the Spanish twin's layout for terms), `slug`, `ref`, `permalink`,
   `translated_from` = English `last_updated`, `last_updated` = the English POLICY date (not today), `title`, seo
   block, the prose keys the English page has (including `refund_requests` where the English has it). Never
   `app_name`, `contact_email`, `back_url`. Unreleased Clippet keeps `sitemap: false` + `noindex: true`.
3. **Apple and app terms.** Apple Portugal's own words per pt-apple-terms.md: «Dados não recolhidos» (App Store
   «Privacidade da app»), «Dados associados a si», «a app Saúde», «Tempo de ecrã», «Partilha com a família», «conta
   Apple», «Definições», cópia de segurança do iCloud, seguimento («Permitir pedidos de seguimento das aplicações»),
   identificador de publicidade (IDFA) as the file says. Menu paths with « > » (no arrows →). App UI labels quoted
   only if they are the app's real pt-PT strings.
4. **Register.** Plain, consistent European Portuguese legal language: «tratar/tratamento», «recolher», «partilhar»,
   «conscientemente» (for "knowingly"), «dados pessoais», «responsável». One term per concept across all pages you
   review (make them consistent). Impersonal register: no «você», no tu; «o utilizador» acceptable in legal text.
   No em/en dashes; sentence case headings. No Brazilian forms (coletar, compartilhar, usuário, arquivo, contato).
5. **Copy-editing**, lightly: read `~/.claude/skills/copy-editing/SKILL.md` and apply only the sweeps that do not
   change legal meaning (clarity, grammar, AI tells). Precision beats style.
6. **seo**: title ≤ 60 chars, natural, unique across all Portuguese privacy pages; description 70–155 chars;
   5–7 lowercase keywords.
7. Run `python3 scripts/i18n.py check 2>&1 | grep -A3 "pt/apps/<slug>/privacy\|pt/apps/clippet/terms"`. Do NOT run
   jekyll build, map or stamp.

Reply with: per page, what you changed and why (especially any meaning fix); the term choices you standardized;
legal terms a Portuguese lawyer should look at (for the language sheet); English-side issues.
