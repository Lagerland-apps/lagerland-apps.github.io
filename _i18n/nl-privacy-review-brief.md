# Reviewer brief: Dutch privacy policies and terms (nl, Netherlands)

For reviewer agents. You did not write these pages. Never published. Repo:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`. Edit only the Dutch files you were given.

Read `_i18n/nl-reviewer-brief.md` (general rules), `_i18n/nl.md`, `_i18n/nl-apple-terms.md`, TRANSLATION.md 6.2.

These are legal texts. For each page, compare with the English page sentence by sentence:

1. **Meaning is exact.** Every obligation, permission, qualifier («may», «only», «not», «if», «optional», «on your
   device», «knowingly»), list item and section of the English text is present, in the same order, with the same
   scope. Nothing is added, softened or strengthened. Fix any drift.
2. **Front matter.** `layout: privacy` (or the Italian twin's layout for terms), `slug`, `ref`, `permalink`,
   `translated_from` = English `last_updated`, `last_updated` = the English POLICY date (not today), `title`, seo
   block, the prose keys the English page has (including `refund_requests` where the English has it). Never
   `app_name`, `contact_email`, `back_url`. Unreleased Clippet keeps `sitemap: false` + `noindex: true`.
3. **Apple and app terms.** Apple Netherlands' own words per nl-apple-terms.md: «Er worden geen gegevens verzameld»
   (App Store «Privacy van app»), «Aan jou gekoppelde gegevens», «Niet aan jou gekoppelde gegevens», «Gegevens die
   worden gebruikt om je te volgen», «de Gezondheid-app», «Schermtijd», «Delen met gezin», «Apple Account»,
   «Instellingen», iCloud-reservekopie / back-up as the file says, tracking ‘Sta trackingverzoeken van apps toe’,
   advertentie-ID (IDFA) as the file says. Menu paths with « > » (no arrows). App UI labels quoted only if they are
   the app's real Dutch strings.
4. **Register.** Plain, consistent Netherlands Dutch legal language, addressed with je (Apple NL's own privacy pages do):
   «verwerken/verwerking», «verzamelen», «delen», «bewust» (for "knowingly"), «persoonsgegevens», «verwerkingsverantwoordelijke»
   or plain «wij» as the English does. One term per concept across all pages you review (make them consistent).
   No u/uw. No em/en dashes; sentence case headings. No Flemish forms.
5. **Copy-editing**, lightly: read `~/.claude/skills/copy-editing/SKILL.md` and apply only the sweeps that do not
   change legal meaning (clarity, grammar, AI tells). Precision beats style.
6. **seo**: title ≤ 60 chars, natural, unique across all Dutch privacy pages; description 70–155 chars;
   5–7 lowercase keywords.
7. Run `python3 scripts/i18n.py check 2>&1 | grep -A3 "nl/apps/<slug>/privacy\|nl/apps/clippet/terms"`. Do NOT run
   jekyll build, map or stamp. No git commands that write.

Reply with: per page, what you changed and why (especially any meaning fix); the term choices you standardized;
legal terms a Dutch lawyer should look at (for the language sheet); English-side issues.

## Standard terms across all Dutch privacy pages (main session, 2026-11-19)

Use exactly these, on every page:

- advertising identifier: «reclame-ID (IDFA)» (Apple NL, support.apple.com/nl-nl/102420); never «advertentie-ID».
- backup: «back-up», «iCloud-back-up», «de back-up van je apparaat» (Apple NL, support.apple.com/nl-nl/108770); never «reservekopie».
- refund: «terugbetaling»; the Apple label ‘Om restitutie verzoeken’ only where the English names the step.
- effective date: «ingangsdatum»; "Last updated": ‘Laatst bijgewerkt’ (nl.yml).
- process / collect / share / knowingly / personal data: «verwerken», «verzamelen», «delen», «bewust», «persoonsgegevens».
- "you agree that we may answer": «ga je ermee akkoord dat wij … mogen antwoorden» (flag for a lawyer, don't vary it).
- Apple apps and settings: «de Gezondheid-app», «Schermtijd», «Delen met gezin», «Apple Account», «Instellingen > Privacy en
  beveiliging > …», ‘Sta trackingverzoeken van apps toe’, «Agenda», «Kaarten» / «de Kaarten-app», «de Weer-app», «Foto’s».
  Apple NL writes «Apple apparaten» (open) for "Apple devices"; «Apple-instellingen» is not an Apple form: write «de instellingen
  van je Apple Account / apparaat» as the English means.
- App UI labels only when they are the app's real Dutch strings (check the catalog); otherwise describe without quotes.
- Tier names as the app's Dutch UI and the Dutch app page use them («Levenslang», not «Lifetime»).
- Apostrophes curly: foto’s, SDK’s.
