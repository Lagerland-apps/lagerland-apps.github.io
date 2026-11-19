# Writer brief: Portuguese (pt, Portugal) Tier 1 pages

For the agents who write and review the Portuguese (Portugal) pages. Never published (`_i18n` is excluded from the build).
Repo root: `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

## Read first (only what you need)

1. `TRANSLATION.md` sections 1, 4.1 (front matter, fact fields that must NOT appear), 6.1 to 6.3, 7.2, 7.6 and 8.
2. `_i18n/pt.md`: the language sheet. Register (impersonal), vocabulary, typography, formats, glossary table, language
   claims, keyword table, tells to cut. Everything decided there is final.
3. `_i18n/pt-glossary.md` (only your app's section: `grep -n "^### \|^## " _i18n/pt-glossary.md`) and
   `_i18n/pt-apple-terms.md` (Apple Portugal's names: use them exactly).
4. `_i18n/pt-keywords.md`: your page's section (primary, secondaries, FAQ-style questions people in Portugal type),
   and the keyword table in `_i18n/pt.md` (final primaries; it overrides the research file where they differ).
5. The ENGLISH source page: it holds the facts. Every fact on your page must be on the English page (or in the
   catalog that feeds both). Write from its meaning.
6. The SPANISH page with the same path under `es/` (reviewed, live): use it ONLY as the structural template (which
   front-matter keys exist, list lengths, Liquid code, how links and tokens are written, what the layout expects).
   Never translate from Spanish; write from English. Where the Spanish page says «App Store de España», Portuguese
   says «App Store de Portugal».
7. The copy-editing skill `~/.claude/skills/copy-editing/SKILL.md`: READ THE FILE and apply its full Seven Sweeps and
   AI-tell removal to your finished Portuguese before you hand it back.

## How to write

- Write as a good copywriter from Portugal would write the page from scratch, for the primary query in the sheet:
  `seo.title`, H1 (`title`) and `quick_answer` are written for it. Natural European Portuguese word order, not
  sentence by sentence translation. European vocabulary and AO90 spelling only (ecrã, telemóvel, utilizador, ficheiro,
  partilhar, descarregar, Definições, registar, guardar, ginásio, «estar a fazer»); never Brazilian forms (tela,
  celular, usuário, arquivo, compartilhar, baixar, Ajustes, registrar, salvar, academia, gerund progressives).
- Register: IMPERSONAL, as Apple Portugal writes. Third-person imperatives without a pronoun where an instruction is
  needed («Toque em», «Abra», «Descarregue»), infinitives for labels, impersonal sentences otherwise («os dados ficam
  no iPhone», «quem trabalha por turnos…»). Never «você», never tu forms (tu, teu, tua, te, podes, tens, toca…).
  «o seu / a sua» only where a possessive can't be avoided. «para si» is acceptable (Apple uses it).
- Quotes «…» (inner “…”). Sentence case in every heading. No em or en dashes (8.3). No Oxford comma («A, B e C»).
  Decimal comma; percent with NO space («30%»); no-break space (U+00A0) before €, units. Metric units. Dates in prose
  «26 de outubro de 2026».
- «app» in body copy, feminine («a app»); «aplicação» in a title or H1 only where the search phrase uses it.
  «a App Store» (feminine), «o Apple Watch», «o iPhone», «o Mac».
- `seo.title` 60 characters or fewer, keyword first; `seo.description` 70 to 155 characters, contains the primary
  query; `seo.keywords` 5 to 8, lowercase, Portuguese queries from the keyword file (real queries only).
  Count characters AFTER tokens expand: `{APP_COUNT}` is 2 characters; a price token like `{P_MONTHLY}` is about 6.
- `quick_answer`: answers the page's main question on its own, two or three sentences.
- `faq`: start from the English questions; phrase each the way people in Portugal ask it; keep every English
  question's facts; add a question only if the English page or the app's facts answer it. The visible question must
  equal the schema question (on app pages the layout does that for you; on hand-written pages keep the two strings
  identical).
- Every alt text and caption, and any names or descriptions inside the page's own JSON-LD, in Portuguese.

## Facts and machinery (never break these)

- Prices, app counts, platforms, trials and dates ONLY through the tokens and includes the English and Spanish pages
  use: `{P_MONTHLY}`, `{P_YEARLY}`, `{P_WEEKLY}`, `{P_LIFETIME}`, `{P_APP}`, `{P_IAP_MIN}`, `{P_IAP_MAX}`,
  `{P_IAP:<label>}`, `{TRIAL}`, `{PLATFORMS}`, `{SAVE_YEARLY}`, `{P_ZERO}`, `{APP_COUNT}`, `{APP_COUNT_OTHER}`,
  cross-app `{P_MONTHLY@slug}`, `_includes/date.html`, `app-facts.html`. Tokens are single-brace. Never type a price,
  a currency sign, an app count or a release date in any form. «€» never appears in your text.
- Fact fields never appear in a translation file (TRANSLATION.md 4.1 list: name, category, status, app_store_url,
  price, schema_*, icon, screenshots, hero.device, release, ratings, alternatives_to, support, privacy.tracking ...).
  Copy the Spanish page's KEY SET, not its values.
- Never invent a fact, number, review, source, feature or competitor detail. If the English page doesn't support a
  sentence, leave it out. No roadmaps or dated promises. Keep every hedge and qualifier ("may", "about", "only",
  "on your device", "optional") exactly as strong as in English.
- App names, competitor names and "Lagerland Apps" are never translated. Never any person's name.
- «Sem subscrição» only for LiftLog, Millrace, Mockly and Tare. Others: «sem subscrição obrigatória» or «opção
  vitalícia», where true. Millrace's copy never mentions the number title it replaced (never write the digits 2048).
  Observa's HRV is SDNN: «VFC (SDNN)»; never RMSSD as Observa's HRV.
- Feature names exactly as the app's pt-PT interface shows them (pt-glossary.md), unless the glossary flags that
  string as Brazilian or defective: then use the clean European form and note it in your reply. Tier names follow
  the app's pt-PT UI (Chessful is Pro on the site, as in every language).
- Apps whose pt-PT text is largely Brazilian (AllPaid, AppMeta, Pulse, Chessful, Observa, Shogiful, Xiangqiful,
  GymLogger X): quote nouns and labels only, never a whole UI sentence.
- Language claims: never say Mockly is in Portuguese (Portugal) (pt-BR only). Every other app may be described as
  available in Portuguese; name the English-only gaps nowhere on the page unless the English page mentions languages.

## Links

- Internal links go to the `/pt/` version when it will exist in Tier 1 (`/pt/`, `/pt/apps/`, `/pt/apps/<slug>/`, its
  `support/` and `privacy/`, `/pt/lagerland-apps/`, `/pt/support/`, `/pt/transparency/`). Every other target
  (journal, guides, for, alternatives, other English-only pages) goes to English with `hreflang="en"` and the marker.
- In Liquid page files (`.html`), write links the way the Spanish page does:
  `<a href="{% include l.html url="/apps/observa/" %}"{% if l_en %} hreflang="en"{% endif %}>Observa{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>`
  (it picks the Portuguese URL once it exists, else English with the marker).
- In front-matter strings (app pages' `faq` answers etc.), hard links are plain HTML: a Tier 1 Portuguese target as
  `<a href=\"/pt/apps/observa/\">…</a>`; an English-only target as
  `<a href=\"/journal/<slug>/\" hreflang=\"en\">… (em inglês)</a>`. Follow how the Spanish page writes the same link.

## Front matter on every page

`ref` (the English URL), `permalink` (`/pt/...`), `translated_from` (the English page's `last_updated`, as a date
`YYYY-MM-DD`), `slug` on app, support and privacy pages, `layout` as on the Spanish page, and `last_updated:
2026-11-19` (privacy pages instead keep the ENGLISH policy's `last_updated`). Never `lang` (the folder default sets
it). Replace every `es` / `/es/` / `"es"` in Liquid code with `pt` / `/pt/` / `"pt"` (language codes in `where`
filters, data keys such as `site.data.i18n_transparency.pt`, URLs). A literal JSON-LD `"inLanguage": "es-ES"` in a
hand-written page becomes `"inLanguage": "pt-PT"` (the layouts emit `pt-PT` from the locale; keep them equal).

## Do NOT

- run `jekyll build`, `scripts/i18n.py map` or `stamp-last-updated.py` (the main session does, once per batch);
- touch any file other than the one(s) you were given;
- edit English, Spanish or any other language's pages (report English-side errors in your reply instead).
- write scratch files inside the repo (use `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-BLVZAo/7d3b6123-9b41-4cdf-94cb-b2404972e5e2/scratchpad/`).

You MAY run `python3 scripts/i18n.py check 2>&1 | grep -A3 "<your path>"` to see source-side errors for your file.

## Reply with

1. The path(s) written.
2. Primary query used and the final `seo.title` (with its character count after token expansion).
3. Any sentence you left out because the English page didn't support it in Portuguese, and any glossary string you
   replaced because it was defective.
4. English-side errors you noticed (facts that contradict the app's glossary or the master), for ISSUES.md.
