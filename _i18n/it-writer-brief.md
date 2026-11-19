# Writer brief: Italian (it, Italy) Tier 1 pages

For the agents who write the Italian pages. Never published (`_i18n` is excluded from the build).
Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.
Other sessions are translating Spanish and Portuguese in this same checkout at the same time: touch ONLY the file(s)
you were given.

## Read first (only what you need)

1. `TRANSLATION.md` sections 1, 4.1 (front matter, fact fields that must NOT appear), 6.1 to 6.3, 7.2, 7.6 and 8.
2. `_i18n/it.md`: the language sheet. Register, typography, formats, glossary table, tier names, store names,
   keyword table, tells to cut, decisions from earlier reviews. Everything decided there is final.
3. `_i18n/it-glossary.md` (only your app's section: `grep -n "^### " _i18n/it-glossary.md`) and
   `_i18n/it-apple-terms.md` (Apple Italy's own names: use them exactly).
4. `_i18n/it-keywords.md`: your page's section (primary, secondaries, FAQ-style questions people in Italy type).
5. The ENGLISH source page: it holds the facts. Every fact on your page must be on the English page (or in the
   catalog that feeds both). Write from its meaning.
6. The FRENCH page with the same path under `fr/`: use it ONLY as the structural template (which front-matter keys
   exist, list lengths, Liquid code, how links and tokens are written, what the layout expects). Never translate
   from French (or from the Spanish twin under `es/`); write from English. Where the French page says
   « App Store français », Italian says «App Store italiano».
7. The copy-editing skill `~/.claude/skills/copy-editing/SKILL.md`: apply its full Seven Sweeps and AI-tell removal
   to your finished Italian before you hand it back.

## How to write

- Write as a good copywriter from Italy would write the page from scratch, for the primary query in the sheet:
  `seo.title`, H1 (`title`) and `quick_answer` are written for it. Natural Italian word order, not sentence by
  sentence translation. **tu** throughout, never Lei, never voi for one reader.
- Quotes “…” (U+201C/U+201D, as Apple Italy writes UI labels; never « »), no space inside, punctuation after:
  Tocca “Tempo di utilizzo”. Typographic apostrophe ’ (U+2019) in elisions: l’app, un’altra, c’è (never a straight '
  in prose; inside YAML double-quoted strings the ’ is fine). App Store bare after prepositions: «su App Store»,
  «Scarica su App Store», «da App Store». Sentence case in every heading. No em or en dashes (8.3). No Oxford comma
  («A, B e C»). Decimal comma; no-break space (U+00A0) before € and units (`3,99 €`, `5 GB`), but **no space before %**
  (`30%`). Metric units. Dates in prose «26 ottobre 2026», «1 novembre». Accents: è/é, perché, più, già, così
  (never e' or piu').
- `seo.title` 60 characters or fewer, keyword first; `seo.description` 70 to 155 characters, contains the primary
  query; `seo.keywords` 5 to 8, lowercase, Italian queries from the keyword file (real queries only).
  Count characters AFTER tokens expand: `{APP_COUNT}` is 2 characters; a price token like `{P_MONTHLY}` is about 6.
- `quick_answer`: answers the page's main question on its own, two or three sentences.
- `faq`: start from the English questions; phrase each the way people in Italy ask it; keep every English
  question's facts; add a question only if the English page or the app's facts answer it. The visible question must
  equal the schema question (on app pages the layout does that for you; on hand-written pages keep the two strings
  identical).
- Every alt text and caption, and any names or descriptions inside the page's own JSON-LD, in Italian.

## Facts and machinery (never break these)

- Prices, app counts, platforms, trials and dates ONLY through the tokens and includes the English and French pages
  use: `{P_MONTHLY}`, `{P_YEARLY}`, `{P_WEEKLY}`, `{P_LIFETIME}`, `{P_APP}`, `{P_IAP_MIN}`, `{P_IAP_MAX}`,
  `{P_IAP:<label>}`, `{TRIAL}`, `{PLATFORMS}`, `{SAVE_YEARLY}`, `{P_ZERO}`, `{APP_COUNT}`, `{APP_COUNT_OTHER}`,
  cross-app `{P_MONTHLY@slug}`, `_includes/date.html`, `app-facts.html`. Tokens are single-brace (`{P_MONTHLY}`,
  never `{{P_MONTHLY}}`). Never type a price, a currency sign, an app count or a release date in any form.
  «€» never appears in your text.
- Fact fields never appear in a translation file (TRANSLATION.md 4.1 list: name, category, status, app_store_url,
  price, schema_*, icon, screenshots, hero.device, release, ratings, alternatives_to, support, privacy.tracking ...).
  Copy the French page's KEY SET, not its values.
- Never invent a fact, number, review, source, feature or competitor detail. If the English page doesn't support a
  sentence, leave it out. No roadmaps or dated promises.
- App names, competitor names and "Lagerland Apps" are never translated. Never any person's name.
- «Senza abbonamento» only for LiftLog, Millrace, Mockly and Tare. Others: «nessun abbonamento obbligatorio» or
  «opzione a vita», where true. Millrace's copy never mentions the number title it replaced (never write the digits
  2048). Observa's HRV is SDNN: «HRV (SDNN)» / «variabilità della frequenza cardiaca (SDNN)» as the sheet says;
  never RMSSD as Observa's HRV.
- Feature names exactly as the app's Italian interface shows them (it-glossary.md), unless the glossary flags that
  string as defective (English left in, typos, Lei forms, wrong meaning): then use the clean form and note it in
  your reply. Tier names per the sheet.
- Before saying the app itself is in Italian, check the sheet's coverage line for your app; never name English-only
  gaps on the page unless the English page mentions languages.

## Links

- Internal links go to the `/it/` version when it will exist in Tier 1 (`/it/`, `/it/apps/`, `/it/apps/<slug>/`, its
  `support/` and `privacy/`, `/it/lagerland-apps/`, `/it/support/`, `/it/transparency/`). Every other target
  (journal, guides, for, alternatives, other English-only pages) goes to English with `hreflang="en"` and the marker.
- In Liquid page files (`.html`), write links the way the French page does:
  `<a href="{% include l.html url="/apps/observa/" %}"{% if l_en %} hreflang="en"{% endif %}>Observa{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>`
  (it picks the Italian URL once it exists, else English with the marker).
- In front-matter strings (app pages' `faq` answers etc.), hard links are plain HTML: a Tier 1 Italian target as
  `<a href=\"/it/apps/observa/\">…</a>`; an English-only target as
  `<a href=\"/journal/<slug>/\" hreflang=\"en\">… (in inglese)</a>`. Follow how the French page writes the same link.

## Front matter on every page

`ref` (the English URL), `permalink` (`/it/...`), `translated_from` (the English page's `last_updated`, as a date
`YYYY-MM-DD`), `slug` on app, support and privacy pages, `layout` as on the French page, and `last_updated:
2026-11-19` (privacy pages instead keep the ENGLISH policy's `last_updated`). Never `lang` (the folder default sets
it). Replace every `fr` / `/fr/` / `"fr"` in Liquid code with `it` / `/it/` / `"it"` (language codes in `where`
filters, data keys such as `site.data.i18n_transparency.it`, URLs). A literal JSON-LD `"inLanguage": "fr"` in a
hand-written page becomes `"inLanguage": "it"`.

## Do NOT

- run `jekyll build`, `scripts/i18n.py map` or `stamp-last-updated.py` (the main session does, once per batch);
- touch any file other than the one(s) you were given;
- edit English, French or Spanish pages (report English-side errors in your reply instead).

You MAY run `python3 scripts/i18n.py check 2>&1 | grep -A3 "<your path>"` to see source-side errors for your file.

## Reply with

1. The path(s) written.
2. Primary query used and the final `seo.title` (with its character count after token expansion).
3. Any sentence you left out because the English page didn't support it in Italian, and any glossary string you
   replaced because it was defective.
4. English-side errors you noticed (facts that contradict the app's glossary or the master), for ISSUES.md.
