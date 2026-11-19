# Writer brief: Dutch (nl, Netherlands) Tier 1 pages

For the agents who write the Dutch pages. Never published (`_i18n` is excluded from the build).
Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

## Read first (only what you need)

1. `TRANSLATION.md` sections 1, 4.1 (front matter, fact fields that must NOT appear), 6.1 to 6.3, 7.2, 7.6 and 8.
2. `_i18n/nl.md`: the language sheet. Register (je), vocabulary, typography, formats, glossary table, language
   claims, keyword table, tells to cut. Everything decided there is final.
3. `_i18n/nl-glossary.md` (only your app's section: `grep -n "^### \|^## " _i18n/nl-glossary.md`) and
   `_i18n/nl-apple-terms.md` (Apple Netherlands' names: use them exactly).
4. `_i18n/nl-keywords.md`: your page's section (primary, secondaries, FAQ-style questions people in the Netherlands
   type), and the keyword table in `_i18n/nl.md` (final primaries; it overrides the research file where they differ).
5. The ENGLISH source page: it holds the facts. Every fact on your page must be on the English page (or in the
   catalog that feeds both). Write from its meaning.
6. The ITALIAN page with the same path under `it/` (reviewed, live): use it ONLY as the structural template (which
   front-matter keys exist, list lengths, Liquid code, how links and tokens are written, what the layout expects).
   Never translate from Italian; write from English. Where the Italian page says «App Store italiano» / «in Italia»,
   Dutch says «de Nederlandse App Store».
7. The copy-editing skill `~/.claude/skills/copy-editing/SKILL.md`: READ THE FILE and apply its full Seven Sweeps and
   AI-tell removal to your finished Dutch before you hand it back.

## How to write

- Write as a good Dutch copywriter from the Netherlands would write the page from scratch, for the primary query in
  the sheet: `seo.title`, H1 (`title`) and `quick_answer` are written for it. Natural Dutch word order (verb at the end
  of subordinate clauses), short sentences, not sentence-by-sentence translation. Netherlands Dutch, never Flemish
  (no gsm, plezant, ge).
- Register: je / jij / jouw, lowercase, everywhere. Never u / uw.
- Quotes “…” (inner ‘…’); UI labels in ‘…’ (Apple NL style) or bare when clearly a name. Sentence case in every
  heading. No em or en dashes (8.3). No Oxford comma («A, B en C»). Decimal comma; percent with no space («30%»);
  a space between number and unit («8 uur», «35 °C»). Metric units. Dates in prose «26 oktober 2026».
- Closed compounds («slaaptracker», «appontwikkelaar»); hyphen with names, abbreviations and vowel clashes
  («Gezondheid-app», «iCloud-synchronisatie», «HRV-meting», «data-economie»). Never split a compound.
- «de app», «de App Store», «de iPhone», «de Apple Watch», «de Mac». App names without an article.
- Search forms vs spelling: visible text uses correct Dutch compounds («aftelapp», «schaakapp», «to-dolijst», «app voor
  krachttraining»); split search forms («aftel app», «schaak app») go only into `seo.keywords` (sheet).
- `seo.title` 60 characters or fewer, keyword first; `seo.description` 70 to 155 characters, contains the primary
  query; `seo.keywords` 5 to 8, lowercase, Dutch queries from the keyword file (real queries only).
  Count characters AFTER tokens expand: `{APP_COUNT}` is 2 characters; a price token like `{P_MONTHLY}` is about 6.
- `quick_answer`: answers the page's main question on its own, two or three sentences.
- `faq`: start from the English questions; phrase each the way people in the Netherlands ask it; keep every English
  question's facts; add a question only if the English page or the app's facts answer it. The visible question must
  equal the schema question (on app pages the layout does that for you; on hand-written pages keep the two strings
  identical).
- Every alt text and caption, and any names or descriptions inside the page's own JSON-LD, in Dutch.

## Facts and machinery (never break these)

- Prices, app counts, platforms, trials and dates ONLY through the tokens and includes the English and Italian pages
  use: `{P_MONTHLY}`, `{P_YEARLY}`, `{P_WEEKLY}`, `{P_LIFETIME}`, `{P_APP}`, `{P_IAP_MIN}`, `{P_IAP_MAX}`,
  `{P_IAP:<label>}`, `{TRIAL}`, `{PLATFORMS}`, `{SAVE_YEARLY}`, `{P_ZERO}`, `{APP_COUNT}`, `{APP_COUNT_OTHER}`,
  cross-app `{P_MONTHLY@slug}`, `_includes/date.html`, `app-facts.html`. Tokens are single-brace. Never type a price,
  a currency sign, an app count or a release date in any form. «€» never appears in your text.
- Fact fields never appear in a translation file (TRANSLATION.md 4.1 list: name, category, status, app_store_url,
  price, schema_*, icon, screenshots, hero.device, release, ratings, alternatives_to, support, privacy.tracking ...).
  Copy the Italian page's KEY SET, not its values.
- Never invent a fact, number, review, source, feature or competitor detail. If the English page doesn't support a
  sentence, leave it out. No roadmaps or dated promises. Keep every hedge and qualifier ("may", "about", "only",
  "on your device", "optional") exactly as strong as in English.
- App names, competitor names and "Lagerland Apps" are never translated. Never any person's name.
- «Geen abonnement» (no subscription) only for LiftLog, Millrace, Mockly and Tare. Others: «geen abonnement nodig» or
  «eenmalige aankoop / levenslang», where true. Millrace's copy never mentions the number title it replaced (never
  write the digits 2048). Observa's HRV is SDNN: «HRV (SDNN)»; never RMSSD as Observa's HRV.
- Feature names exactly as the app's Dutch interface shows them (nl-glossary.md), unless the glossary flags that
  string as defective: then use the clean form and note it in your reply. Tier names follow the app's Dutch UI
  (Chessful is Pro on the site, as in every language).
- Observa's Dutch UI mixes je and u: quote only its je strings or nouns and labels. Quote nouns and labels rather than
  whole UI sentences in general.
- Language claims: never say AppMeta or Mockly is in Dutch (no Dutch UI; say plainly the interface is English where
  the page talks about languages). Every other app may be described as available in Dutch; name the English-only gaps
  nowhere unless the English page mentions languages.

## Links

- Internal links go to the `/nl/` version when it will exist in Tier 1 (`/nl/`, `/nl/apps/`, `/nl/apps/<slug>/`, its
  `support/` and `privacy/`, `/nl/lagerland-apps/`, `/nl/support/`, `/nl/transparency/`). Every other target
  (journal, guides, for, alternatives, other English-only pages) goes to English with `hreflang="en"` and the marker.
- In Liquid page files (`.html`), write links the way the Italian page does:
  `<a href="{% include l.html url="/apps/observa/" %}"{% if l_en %} hreflang="en"{% endif %}>Observa{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>`
  (it picks the Dutch URL once it exists, else English with the marker).
- In front-matter strings (app pages' `faq` answers etc.), hard links are plain HTML: a Tier 1 Dutch target as
  `<a href=\"/nl/apps/observa/\">…</a>`; an English-only target as
  `<a href=\"/journal/<slug>/\" hreflang=\"en\">… (in het Engels)</a>`. Follow how the Italian page writes the same link.

## Front matter on every page

`ref` (the English URL), `permalink` (`/nl/...`), `translated_from` (the English page's `last_updated`, as a date
`YYYY-MM-DD`), `slug` on app, support and privacy pages, `layout` as on the Italian page, and `last_updated:
2026-11-19` (privacy pages instead keep the ENGLISH policy's `last_updated`). Never `lang` (the folder default sets
it). Replace every `it` / `/it/` / `"it"` in Liquid code with `nl` / `/nl/` / `"nl"` (language codes in `where`
filters, data keys such as `site.data.i18n_transparency.nl`, URLs). A literal JSON-LD `"inLanguage": "it"` in a
hand-written page becomes `"inLanguage": "nl"`. Unlisted Clippet pages keep the Italian twin's `sitemap: false` and
`noindex: true`.

## Do NOT

- run `jekyll build`, `scripts/i18n.py map` or `stamp-last-updated.py` (the main session does, once per batch);
- touch any file other than the one(s) you were given;
- edit English, Italian or any other language's pages (report English-side errors in your reply instead);
- `git add`, commit or run any git command that writes;
- write scratch files inside the repo (use `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-sfRxDf/a0f20936-3297-4b44-a744-abd8a39f3d0e/scratchpad/`).

You MAY run `python3 scripts/i18n.py check 2>&1 | grep -A3 "<your path>"` to see source-side errors for your file.

## Reply with

1. The path(s) written.
2. Primary query used and the final `seo.title` (with its character count after token expansion).
3. Any sentence you left out because the English page didn't support it in Dutch, and any glossary string you
   replaced because it was defective.
4. English-side errors you noticed (facts that contradict the app's glossary or the master), for ISSUES.md.
