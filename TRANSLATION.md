# TRANSLATION.md: rulebook for the translated site

How to translate lagerland-apps.github.io into 16 market languages, one language at a time, and how to keep
every language search- and AI-optimized when apps, guides, comparisons and journal posts are added later.

This file is excluded from the build (`exclude:` in `_config.yml`), like CLAUDE.md, DESIGN.md and PRODUCT.md.
Everything in the repo CLAUDE.md still applies to translated pages. This file adds the rules that only exist
because a page has more than one language.

Read order for any translation session: repo `CLAUDE.md`, then this file, then the language sheet
`_i18n/<code>.md` for the language you are working on (section 5).

---

## 0. Status

| Item | Status |
|---|---|
| Phase 0 groundwork (section 4) | done 2026-10-26 (what it built: 4.16) |
| Languages live | de (German), 2026-10-27: Tier 1 |

Update this table in the same commit that finishes Phase 0 or launches a language. Per-language status
(tiers done, open stale pages) lives in each language sheet.

Suggested launch order. The owner picks; the reasons are what matters.

1. German (`de`) as the pilot: a large paying market, Latin script, and it exercises every part of the
   pipeline without font or right-to-left work.
2. The other Latin-1 languages: `fr`, `es`, `it`, `nl`, `pt-br`, `es-mx`, `pt`, `id`. Cheap once the pilot works.
3. `pl` and `tr`: need the latin-ext font subset (section 4.11).
4. `ja` and `ko`: CJK typography and different title lengths.
5. `ru`: Cyrillic font subset, Yandex as a first-class engine.
6. `ar`: right-to-left layout work.
7. `zh`: decide the hosting question in section 12 first.

---

## 1. Principles

1. English is the master. Every fact on a translated page also exists on the English page, or in the catalog
   that feeds both. The only exception is a local-only page (section 6.7).
2. Facts live in one place, words live in one file per language. Prices, platforms, counts, trials, ratings,
   App Store links, screenshots and release dates come from `_data/catalog.json` and `_apps/<slug>.md`.
   A translation file holds words only, so the ratings bot and the App Store Connect sync update every language
   at once.
3. Localize, don't transliterate. Research what people in that market type into Google, Naver, Yandex or the
   App Store, and write the page for that query. A word-for-word copy of the English title is almost never the
   right title.
4. No mixed-language pages. A translated page is complete in its language, interface included, or it does not
   ship. Links to pages that are not translated yet go to the English page and say so (section 7.6).
5. A language goes live only when its Tier 1 set is complete (section 3). Until then nothing links to it and the
   language switcher does not show it.
6. Every translated page passes the same SEO / AEO gate as an English page, plus the translation checks in
   section 10.
7. Every text that goes on the site, in any language, gets a copy-editing pass in that language (section 8).
8. A published URL never changes, in any language. The repo CLAUDE.md rule on ranking safety applies per language.

---

## 2. Language register

One row per market. The code is the folder name, the `lang` value in front matter and the key in every data file.

| Market | Code and folder | `<html lang>` | hreflang | og:locale | App Store Connect localization | Territory | Currency | Script |
|---|---|---|---|---|---|---|---|---|
| (master) | root `/` | `en` | `en` and `x-default` | `en_US` | English (U.S.) | USA | USD | Latin |
| Germany | `de` `/de/` | `de` | `de` | `de_DE` | German | DEU | EUR | Latin |
| France | `fr` `/fr/` | `fr` | `fr` | `fr_FR` | French | FRA | EUR | Latin |
| Italy | `it` `/it/` | `it` | `it` | `it_IT` | Italian | ITA | EUR | Latin |
| Spain | `es` `/es/` | `es-ES` | `es-ES` (plus `es`, see below) | `es_ES` | Spanish (Spain) | ESP | EUR | Latin |
| Portugal | `pt` `/pt/` | `pt-PT` | `pt-PT` (plus `pt`, see below) | `pt_PT` | Portuguese (Portugal) | PRT | EUR | Latin |
| China | `zh` `/zh/` | `zh-CN` | `zh-CN` | `zh_CN` | Chinese, Simplified | CHN | CNY | Han |
| Japan | `ja` `/ja/` | `ja` | `ja` | `ja_JP` | Japanese | JPN | JPY | Japanese |
| Korea | `ko` `/ko/` | `ko` | `ko` | `ko_KR` | Korean | KOR | KRW | Hangul |
| Indonesia | `id` `/id/` | `id` | `id` | `id_ID` | Indonesian | IDN | IDR | Latin |
| Mexico | `es-mx` `/es-mx/` | `es-MX` | `es-MX` (plus `es`) | `es_MX` | Spanish (Mexico) | MEX | MXN | Latin |
| Brazil | `pt-br` `/pt-br/` | `pt-BR` | `pt-BR` (plus `pt`) | `pt_BR` | Portuguese (Brazil) | BRA | BRL | Latin |
| Poland | `pl` `/pl/` | `pl` | `pl` | `pl_PL` | Polish | POL | PLN | Latin (ext) |
| Turkey | `tr` `/tr/` | `tr` | `tr` | `tr_TR` | Turkish | TUR | TRY | Latin (ext) |
| Netherlands | `nl` `/nl/` | `nl` | `nl` | `nl_NL` | Dutch | NLD | EUR | Latin |
| Russia | `ru` `/ru/` | `ru` | `ru` | `ru_RU` | Russian | RUS | RUB | Cyrillic |
| Saudi Arabia | `ar` `/ar/` | `ar` | `ar` | `ar_SA` | Arabic | SAU | SAR | Arabic, right to left |

The territories and currencies already exist in `_data/catalog.json` (`meta.territories`), so translated pages
get local prices from the same App Store Connect export as English. The apps themselves are already localized
into all 16 languages (checked in the Xcode string catalogs), but confirm per app before a page says
"the app is in German" (section 6.1).

Regional pairs. Spanish and Portuguese each have two sites. The bare language tag (`es`, `pt`) catches every
Spanish or Portuguese reader whose country has no version of its own:

- `es` goes to `/es-mx/` once it exists, because Latin America has far more Spanish readers than Spain.
  Until `/es-mx/` exists, `/es/` carries `es`. Same for `pt`: `/pt-br/` once it exists, `/pt/` before that.
- Moving the bare tag later is safe: only the hreflang changes, never a URL.
- Never use numeric region codes such as `es-419`. Google does not accept them.

The bare tags for the other languages (`de`, `fr`, `ar` and so on) already cover neighbouring countries
(Austria, Belgium, Switzerland, the Gulf). Those readers see the home market's currency, which is acceptable;
the App Store link opens their own storefront and price anyway.

URL slugs stay identical to English after the language prefix: `/apps/observa/` becomes `/de/apps/observa/`,
`/journal/how-to-sleep-after-a-night-shift/` becomes `/de/journal/how-to-sleep-after-a-night-shift/`. Words in
the URL are a very weak ranking signal, while identical slugs keep the hreflang map, IndexNow and the staleness
check trivial and avoid percent-encoded URLs in five non-Latin languages. Only local-only pages (6.7) get a slug
in the local language, ASCII only, no diacritics.

---

## 3. What gets translated, in what order

A full language is roughly 270 pages. Do it in tiers. Count pages per tier with the live site, these numbers are
from 2026-10-26.

| Tier | Pages | Count today | Rule |
|---|---|---|---|
| 1, launch set | `/<code>/` home, `/<code>/apps/`, every live app page, every app's support and privacy page, `/<code>/lagerland-apps/` (about), `/<code>/support/`, `/<code>/transparency/`, plus `/<code>/llms.txt` and `/<code>/llms-full.txt` | about 66 | All of it before the language goes live |
| 2, hubs and guides | `/<code>/for/` and the audience pages, `/<code>/guides/` and the guides | about 13 | Each page needs local keyword research first |
| 3, comparisons | `/<code>/alternatives/` hub and the comparison pages that make sense in that market, plus local-only comparisons | up to 123 | Only competitors people in that market use (6.4) |
| 4, journal | `/<code>/journal/` hub and selected posts | up to 70 | Only posts with search demand in that language (6.5) |

Hubs (`/<code>/journal/`, `/<code>/alternatives/`, `/<code>/guides/`, `/<code>/for/`) are created together with
the first page of their type, never empty.

Large-scale risk to keep in mind: Google's spam policies treat mass-produced, auto-translated pages that add
little for the reader as scaled content abuse. The tiers, the per-market research and the native review in
section 9 are what keep this site on the right side of that line. Never publish a whole tier in one push
without the review steps.

---

## 4. Phase 0: one-time groundwork

Done once, before the first language, in commits that change no visible English output except what is listed
here. Check that by building `_site` before and after and diffing it. Each item names the files it touches.

### 4.1 Folders and front matter

Every translated page is a plain Jekyll page inside its language folder, with an explicit `permalink:`
(the site has no `permalink: pretty`, and `scripts/indexnow-ping.py` maps pages by their permalink).

```
de/index.html                         -> /de/
de/apps/index.html                    -> /de/apps/
de/apps/observa/index.md              -> /de/apps/observa/            (layout: app)
de/apps/observa/support/index.html    -> /de/apps/observa/support/
de/apps/observa/privacy/index.html    -> /de/apps/observa/privacy/
de/journal/<slug>/index.md            -> /de/journal/<slug>/          (layout: journal)
de/alternatives/<slug>.html           -> /de/alternatives/<slug>/
de/guides/<slug>.html, de/for/<slug>.html, de/lagerland-apps/, de/support/, de/transparency/
de/llms.txt, de/llms-full.txt, de/feed.xml, de/sitemap.xml
```

Front matter keys that every translated page carries:

| Key | Meaning |
|---|---|
| `lang` | Never typed by hand: set by a `_config.yml` default per folder (`scope: { path: "de" }`, `values: { lang: de }`) |
| `ref` | The English URL this page translates, e.g. `/apps/observa/`. It is the translation key |
| `translated_from` | The English page's `last_updated` at the moment the translation was written or last synced |
| `last_updated` | This page's own last real edit, set by the stamp script as today |
| `local_only: true` | Only on pages with no English twin (6.7); such pages have no `ref` |

Example, a translated app page. It holds words only; every fact comes from `_apps/observa.md`.

```yaml
---
layout: app
slug: observa                      # same slug: facts and catalog prices are looked up with it
ref: /apps/observa/
permalink: /de/apps/observa/
translated_from: 2026-10-26
last_updated: 2026-11-03
title: "..."
tagline: "..."
quick_answer: "..."
seo:
  title: "..."
  description: "..."
  keywords: [ ... ]
hero: { headline: "...", subheadline: "...", alt: "..." }
who_for: [ ... ]
who_not_for: [ ... ]
value_points: [ ... ]
features: [ ... ]
how_it_works: { heading: "...", intro: "...", steps: [ ... ] }
screenshot_captions: [ ... ]       # same order as the English screenshots list
faq: [ { q: "...", a: "..." } ]
about_heading: "..."
---
(translated body, if the English page has show_body: true)
```

Fact fields never appear in a translation file: `name`, `category`, `status`, `app_store_url`, `price`,
`schema_*`, `icon`, `og_image`, `screenshots` (files), `hero.device`, `hero.video`, `release`, `ratings`,
`alternatives_to`, `related_apps`, `support`, `founder.entity_type`, `founder.support_email`, `founder.photo`,
`privacy.tracking`, `privacy.account_required`, `show_body`, `jump_nav`, `free_tier`, and inside lists
`plans[].kind`, `plans[].highlight`, `release_notes[].date`, `related_journal.slug`. Text fields (`tagline`,
`quick_answer`, `seo`, hero text, `who_for`, `features`, `faq`, `how_it_works`, `privacy` prose, `plans_footnote`,
`pricing_note`, `price_lead`, `price_tier`, `price_override`, captions, alt texts, founder story,
`comparison_table`, `example_insights` and the other optional sections) are all translated.
`scripts/i18n.py check` enforces both lists.

Lists that pair words with facts are translated item by item, in the master's order and length:

- `plans`: each item carries `name`, `price`, `summary`, `features`, `highlight_label`. `price` is the card's
  display string, tokens plus words ("{P_LIFETIME} einmalig", "{P_ZERO}"), so it is text; `kind` stays in the
  master. A currency sign typed into it fails the check.
- `release_notes`: `note` only; the dates come from the master.
- `screenshot_captions`: one item per master screenshot, `{ alt: "..." }` and/or `{ caption: "..." }` mirroring
  the master item.
- `related_journal`: `{ anchor: "..." }`; the post is the master's, shown in the page language when translated.
- `enrichment` (optional): the words of `_data/app_enrichment.yml` for this app (`use_cases`, `recommend_when`,
  `recommend_why`, `pricing_tiers`) in the language. Without it the quick-reference block and llms-full.txt leave
  those lines out on that language.

Support and privacy translations carry `slug` (the app slug) so the layouts find the app; they never carry
`name`, `support`, `app_name`, `contact_email` or `back_url`.

### 4.2 `_config.yml`

- One `defaults:` entry per language folder setting `lang`.
- Add `TRANSLATION.md` and `_i18n` to `exclude:` (folders starting with `_` are skipped anyway, listing it
  makes the intent explicit).

### 4.3 Locale data: extend `_data/locales.yml`

The file already says how: add one block per language next to `en:`. `money.html` and `app-facts.html` already
read `page.lang` and the territory. Each block gets:

```yaml
de:
  territory: DEU
  html_lang: de
  hreflang: [de]                  # es/pt blocks list the bare tag here while they carry it (section 2)
  og_locale: de_DE
  dir: ltr
  native_name: "Deutsch"          # shown in the language switcher
  live: false                     # true only in the go-live commit (see below)
  currencies:
    EUR: { symbol: "€", position: after, decimals: 2, decimal: ",", group: "." }   # position: before, before_space, after
  strings: { free: "Kostenlos", from: "ab", per_month: "/Monat", ..., trial_days: "{n} Tage gratis testen" }   # every key that en has

`live` is the one switch for a language. While it is false the language's pages build but carry noindex (with a
self canonical), stay out of every sitemap, get no hreflang, and do not appear in the switcher, the footer
language row, ai-index.json or the 404 page. The go-live commit sets it to true.
```

Currency formats must match what the App Store shows in that storefront. Open one of the apps in that storefront
on the web, copy the format, and note the date you checked in the language sheet. Starting points to verify:

| Code | Example | Code | Example |
|---|---|---|---|
| de, fr, it, es, pt | `3,99 €` (fr uses a narrow no-break space) | nl | `€ 3,99` |
| pl | `14,99 zł` | pt-br | `R$ 14,90` |
| es-mx | `$39.00` (check whether Apple adds MXN) | ru | `349 ₽` (check decimals) |
| tr | `₺79,99` (check symbol position) | ja | `¥600` (no decimals) |
| ko | `₩5,500` (no decimals) | zh | `¥18` or `¥18.00` (check) |
| id | `Rp 39.000` (no decimals) | ar | `17.99 ر.س` or `SAR 17.99`, and which digits (check) |

The trial label (`7-day free trial`) and the platform list join word come from the catalog and `strings`.
The trial label is built from the catalog's `free_trial.duration` with the patterns `trial_days`, `trial_months`
and `trial_years` in `strings` (`_includes/trial.html`). A zero price is the token `{P_ZERO}` (0 in the
territory's currency, no decimals), so no translation ever types "$0" or "0 €".

### 4.4 Interface strings: `_data/i18n/<code>.yml`

Every English word in `_layouts/` and `_includes/` moves into `_data/i18n/en.yml`, and templates print
`{{ t.key }}` with `{% assign t = site.data.i18n[page.lang] | default: site.data.i18n.en %}`. About 250 text
nodes today, most of them in `_layouts/app.html`, `_includes/footer.html`, `_layouts/support.html`,
`_layouts/privacy.html`, `_includes/hero.html`, `_includes/header.html` and `_includes/alternatives.html`.
That includes the header imprint (`Sheet 2025-{year} · Issued in Finland`), footer columns, "Last updated",
"Cancel anytime", the default how-it-works heading, breadcrumb names, aria-labels and alt texts.

Rule from then on: a template never contains a visible English word. A new string goes into `en.yml` and into
every live language's file in the same commit. The check fails on a missing key.

Pages such as `index.html`, `apps/index.html` and `alternatives/index.html` are content, not templates: they get a
translated copy per language like any other page.

### 4.5 Facts from the master

`_layouts/app.html` reads facts from the master document and words from the page:
`{% assign m = site.apps | where: "slug", page.slug | first %}`, then fact reads use `m.` and text reads use `page.`.
On English pages `m` is the page itself, so English output does not change. The same pattern applies to the
support and privacy layouts (they already look the app up through `site.apps`) and to the homepage stamp sheet,
which takes names and icons from `site.apps` and taglines from the translated app page of the current language.

Every loop that lists apps or posts on a translated page filters by language:
`site.pages | where: "lang", page.lang | where: "layout", "app"`. English loops keep using `site.apps` and
`site.journal` and must never pick up translated pages (translations are plain pages, not collection documents,
so they cannot leak into those loops).

Screenshots follow the same idea: `_includes/screenshots.html` and the JSON-LD `screenshot` list take the file
names from the master's `screenshots:` list and load them from `assets/screenshots/<slug>/<code>/` when that folder
holds the full set (checked with `site.static_files`, as `head.html` already does for share images), otherwise
from the English folder (section 6.8).

### 4.6 `_includes/head.html`

- `<html lang>` and `dir` from the locale block (in `_layouts/default.html`).
- Canonical: always the page's own URL. A translation never points its canonical at English.
- hreflang: one `<link rel="alternate" hreflang>` per existing version, itself included, plus `x-default` to the
  English URL, read from `_data/i18n_map.json` (4.12) with `page.ref | default: page.url` as the key. The set must be
  identical on every version of the page. English pages list their translations the same way.
- `og:locale` from the locale block, plus one `og:locale:alternate` per other existing version.
- JSON-LD: every `"inLanguage": "en"` (WebSite, Article, SoftwareApplication, HowTo) becomes the page language.
  One `Organization` node, `@id` `{{ site.url }}/#organization`, shared by every language. One `WebSite` node per
  language, `@id` `{{ site.url }}/<code>/#website`, with a translated name and description. Breadcrumb names are
  translated and their items point at the same-language URLs.
- Share image: `/assets/og/<code>/<slug>.png` when it exists, else the English card.
- Feed and AI-file alternates point at the language's own `/<code>/feed.xml`, `/<code>/llms.txt` and
  `/<code>/llms-full.txt`.
- The meta `author` and `publisher` stay "Lagerland Apps" in every language.

### 4.7 Dates

`{{ page.last_updated | date: "%B %-d, %Y" }}` prints English month names. Replace every visible date with an
include, `_includes/date.html`, that reads the pattern and month names from `_data/i18n/<code>.yml`.
JSON-LD and sitemap dates stay ISO (`2026-10-26`).

| Code | Visible format | Code | Visible format |
|---|---|---|---|
| de | 26. Oktober 2026 | fr | 26 octobre 2026 |
| it | 26 ottobre 2026 | es, es-mx | 26 de octubre de 2026 |
| pt, pt-br | 26 de outubro de 2026 | nl | 26 oktober 2026 |
| pl | 26 października 2026 (genitive month) | ru | 26 октября 2026 г. (genitive month) |
| tr | 26 Ekim 2026 | id | 26 Oktober 2026 |
| ja, zh | 2026年10月26日 | ko | 2026년 10월 26일 |
| ar | 26 أكتوبر 2026 (Gregorian; check digits) | | |

### 4.8 App Store links and the badge

- `app_store_url` is storefront-free (`https://apps.apple.com/app/id…`), so it already opens the visitor's own
  storefront. Keep it that way in every language; the QR codes stay valid too.
- `_includes/appstore-badge.html` draws "Download on the App Store" as text. Each language uses the wording of
  Apple's official localized badge for that language (Apple's marketing resources publish them). Copy Apple's
  wording, never translate it yourself. The aria-label goes through `t`.
- The developer link stays `https://apps.apple.com/developer/id1855943133` everywhere.

### 4.9 Language switcher, and no redirects

- A switcher in the header and the footer lists the versions of the current page that exist (from the map),
  each in its own language and script: Deutsch, Français, Italiano, Español (España), Español (México),
  Português (Portugal), Português (Brasil), 简体中文, 日本語, 한국어, Bahasa Indonesia, Polski, Türkçe, Nederlands,
  Русский, العربية. Each link carries `hreflang` and `lang`.
- No flags. A flag is a country, and these are languages.
- No automatic redirect by IP address or browser language. Googlebot crawls mostly from the US with no
  language preference, so a redirect hides the translations from it. An optional dismissible hint ("this page
  is available in Deutsch") is fine; it must not store anything beyond `localStorage` and must not move the page.
- GitHub Pages serves one `404.html` for the whole site. Its text picks the language from the path with a few
  lines of JS, with English as the no-JS default.

### 4.10 Layout, right to left, and text length

- Text in German, Russian, Polish, French and Dutch runs 20 to 35 percent longer than English. Check stamps,
  nav, buttons, price pills and the sticky download bar at 320 px wide.
- `hyphens: auto` works once `<html lang>` is right; use it on body text for de, nl, pl, ru.
- Arabic: `dir="rtl"`. Replace physical CSS properties (`margin-left`, `padding-right`, `left:`, `text-align: left`)
  with logical ones (`margin-inline-start` and so on) in `assets/css/style.css`. Mirror icons that point a
  direction (arrows, chevrons); never mirror screenshots, app icons, logos or the stamp artwork. Wrap Latin app
  names, prices and URLs in `<bdi>` or `dir="ltr"` so they don't reorder.
- CJK: no letter-spacing on CJK text, no `text-transform: uppercase`, no italics. `word-break: keep-all` for
  Korean, `line-break: strict` for Japanese and Chinese, line-height around 1.75 for body text.
- Turkish: the browser uppercases `i` to `İ` only when `lang="tr"` is set, which the head change guarantees.

### 4.11 Fonts

The self-hosted Jost and Inter files are Latin-1 subsets (`unicode-range: U+0000-00FF` plus a few signs).
Without more subsets, Polish ł or Turkish ş render in a fallback font mid-word, which looks broken.

- `pl`, `tr`: add latin-ext subsets of Jost and Inter as separate woff2 files with their own `unicode-range`, so
  English pages never download them.
- `ru`: add Cyrillic subsets (check both families cover Cyrillic; if Jost doesn't, pick a matching display face).
- `ar`: self-host an OFL Arabic face (for example IBM Plex Sans Arabic or Noto Sans Arabic), loaded only on `/ar/`.
- `ja`, `ko`, `zh`: no web font (full CJK fonts are several megabytes). Use system stacks per language with
  `:lang()`: Hiragino Sans and Yu Gothic for ja, Apple SD Gothic Neo and Malgun Gothic for ko, PingFang SC and
  Microsoft YaHei for zh, then Noto Sans CJK.
- The repo rule stands: no third-party font hosts.

### 4.12 Machine-readable files

| File | Per language | Built from |
|---|---|---|
| `sitemap.xml`, `ai-sitemap.xml` | no change: they already list every indexable page, translations included | `_includes/sitemap-urls.xml` |
| `/<code>/sitemap.xml` | yes, only that language's URLs; listed in `sitemap_index.xml` and as a `Sitemap:` line in `robots.txt` | same include, filtered by `lang` |
| `/<code>/llms.txt` | yes, in that language: catalogue loop, hand-written AI recommendation guide in that language, hubs, guides, journal, comparisons | shared include with a `lang` parameter |
| `/<code>/llms-full.txt` | yes, generated from that language's front matter | shared include with a `lang` parameter |
| `/<code>/feed.xml` | yes, that language's journal posts | shared include |
| `/llms.txt` (root) | stays English; gets an `## Other languages` section listing each live language's home and llms files | hand-written section |
| `/ai-index.json` | one file; gets a `languages` list and a `localized_urls` map per app, page, guide and post | loops plus the map |
| `robots.txt` | stays open to every crawler; add only the per-language `Sitemap:` lines | static |
| `_data/i18n_map.json` | the translation map: English URL to `{code: URL}` | `scripts/i18n.py map` |

Write each per-language file as a short stub that includes a shared template, so a fix lands in every language.

### 4.13 Scripts

- New `scripts/i18n.py` (stdlib only, like the others):
  - `map` writes `_data/i18n_map.json` from every page's `ref` and `lang`.
  - `stale` lists translations whose English source has a newer `last_updated` than their `translated_from`,
    grouped by language, with the English git diff since that date.
  - `check` fails on: a fact field in a translation file, a missing text field the English page has, a missing
    key in `_data/i18n/<code>.yml`, a `ref` that points nowhere, a missing `permalink`, a translated page linking
    to an English page that now has a version in its language, and leftover English interface strings
    (any `en.yml` value found verbatim on a non-English page). It also warns, per language, about apps still
    showing English screenshots and about incomplete localized screenshot sets.
- `scripts/stamp-last-updated.py`: add the language folders to `CONTENT_DIRS` (a pattern such as
  `^[a-z]{2}(-[a-z]{2})?/`). Translated privacy pages keep the privacy exception.
- `scripts/indexnow-ping.py`: works through explicit permalinks; confirm a translated page maps to its URL and
  that `_data/i18n/*.yml` changes count as sitewide.
- `scripts/seo-audit.py` gets the translation checks:
  - `<html lang>` equals the folder's `html_lang` (today the audit errors on anything but `en`, so this must
    change in Phase 0), `dir="rtl"` on `/ar/`.
  - hreflang: present on every page that has translations, self-referencing, reciprocal (every version lists the
    same set), every target indexable and not a redirect, `x-default` points at English, valid codes only.
  - Canonical equals the page URL on translated pages too.
  - Title and description limits per script (section 7.2); duplicate checks run per language.
  - Prices: the existing USD check, extended to every territory and currency format.
  - Every `/<code>/` app, guide and journal URL is routed in `/<code>/llms.txt`; every URL in the per-language AI
    files resolves; each per-language sitemap equals that language's indexable pages.
  - WARN for internal links from a translated page to an English page (expected while tiers are incomplete).
- `scripts/generate-og.py`: a `--lang` option that renders `assets/og/<code>/<slug>.png` with the translated
  tagline and a font that covers the script (add CJK, Arabic, Cyrillic and latin-ext fonts to `scripts/og-assets/fonts/`),
  and the localized first screenshot when the language has a set.

### 4.14 Build time

GitHub Pages stops a build after about ten minutes. A full language adds roughly 270 pages, and 16 languages
multiply any per-page loop over all pages. Baseline on 2026-10-26: about 10 seconds locally for 277 pages.
Measure the local build time before Phase 0 and after each language,
note it in that language's sheet, and keep templates on map lookups and `where` filters instead of nested loops
over `site.pages`.

### 4.15 Done when

English `_site` is unchanged apart from the intended head, template and file changes; `scripts/seo-audit.py`
reports 0 errors; `scripts/i18n.py check` passes; a throwaway test page in a test language folder renders with
correct lang, hreflang, prices, dates and strings, and is deleted before the commit.

---

### 4.16 What Phase 0 built (reference)

Done 2026-10-26. Build time: 9.9 s before, about 12.5 s after, for the same 277 English pages.

- Strings: `_data/i18n/en.yml` holds every visible word of `_layouts/` and `_includes/` (about 300 keys, some
  nested: `months`, `categories`, `price_models`, `series`, `lf`, `llms_groups`). Layouts start with
  `{% include t.html %}` (assigns `t` and `loc`). YAML reads the bare keys `yes`/`no` as booleans, so they are
  `word_yes`/`word_no`. Liquid cannot take `}` inside `{{ }}` or nested brackets (`a[b[0]]`): replace
  placeholders and look up nested keys in `{% assign %}` first.
- Facts and words: `_layouts/app.html` reads facts from `m` (the master) and words from `page`; the includes take
  `app=` (master) and `tx=` (words). Other apps on a page (cards, stamps, footer, lists) find their page in the
  current language with `_includes/tx-app.html` and are left out on a translated page that has no translation.
- Links: `_includes/l.html url="/apps/"` prints the same-language URL from `_data/i18n_map.json` or the English
  URL, and sets `l_en` so the caller adds `hreflang="en"` and `t.english_marker`.
- Dates: `_includes/date.html date=... fmt="long"|"dmy"`. Prices: `money.html` (position `before_space` added),
  `trial.html`, `{P_ZERO}`. Screenshots: `_includes/screenshot-set.html` (6.8). Share image: `_includes/og-image.html`.
- Head: `<html lang dir>`, hreflang and `og:locale:alternate` from the map for live languages, one WebSite node per
  language (`site_title`, `site_description` in the strings), per-language feed and llms alternates.
- Switcher: `_includes/lang-switch.html` in the header nav; a language row in the footer (every live language, to
  this page's version or that language's home). Both render nothing while English is the only live language.
- 404: one template per live language inside `404.html`, swapped in by a few lines of JS for `/<code>/` paths.
- Machine files, as shared includes: `_includes/sitemap-urls.xml lang=`, `_includes/feed.xml lang=`,
  `_includes/llms-full.txt` (generated part, labels in `t.lf`), `_includes/llms-catalog.txt` (the app catalogue of
  llms.txt). English loops over `site.pages` filter `where: "lang", "en"`. ai-index.json has `languages` and
  `localized_urls`.
- Per-language stubs, created in a language's setup commit:
  - `<code>/sitemap.xml`: front matter `layout: none`, `permalink: /<code>/sitemap.xml`, `sitemap: false`; body
    as root sitemap.xml with `{%- include sitemap-urls.xml lang="<code>" %}`.
  - `<code>/feed.xml`: `permalink: /<code>/feed.xml`, `layout: none`; body `{% include feed.xml lang="<code>" %}`.
  - `<code>/llms-full.txt`: as root llms-full.txt, with the preamble written in the language.
  - `<code>/llms.txt`: hand-written in the language, with `{% include llms-catalog.txt %}` for the catalogue and
    the language's own AI recommendation guide.
- CSS: switcher, footer row, `.en-marker`, hyphenation for de, nl, pl, ru and the CJK rules (4.10). The
  right-to-left conversion of physical CSS properties (4.10) and the extra font subsets (4.11) are not done:
  they land in the setup commit of ar, and of pl, tr, ru, respectively.
- Scripts: `scripts/i18n.py` (`map`, `stale`, `check`; needs PyYAML, like generate-og.py), the translation checks in
  `seo-audit.py`, language folders in `stamp-last-updated.py`, live-language filter in `indexnow-ping.py`,
  `generate-og.py --lang <code>` (fonts for non-Latin-1 scripts go in `scripts/og-assets/fonts/` under the names in
  its `SCRIPT_FONTS`).

---

## 5. Launching one language

### 5.1 The language sheet `_i18n/<code>.md`

Create it first. It is never published. It holds every decision a translator would otherwise make differently
on each page:

- Formality (section 12 gives the default to confirm) and the reason.
- Punctuation and typography rules for the language (section 8.3).
- Currency, number and date formats, with the date they were checked against the App Store storefront.
- Glossary: feature names exactly as the app's own localized interface shows them (from the app's
  `Localizable.xcstrings` in its Xcode project and its localized App Store listing), Apple product and feature
  names as Apple localizes them, recurring sentences (privacy clauses, "no account", iCloud sync answers) with
  their one approved translation.
- The localized App Store name and subtitle of each app, if they differ from English.
- Keyword research notes: the primary query and the main secondary queries per page.
- Local competitors found for Tier 3.
- Review log: which pages had a native review, a back-translation check, and when. Reviewers are noted by role,
  never by name on the site.
- Per-language status: tiers done, stale pages open, apps still showing English screenshots.

### 5.2 Setup commit for the language

- `_config.yml` default for the folder; the locale block in `_data/locales.yml` with `live: false`;
  `_data/i18n/<code>.yml` with every key translated and copy-edited; the per-language stubs from 4.16.
- Fonts if the script needs them (4.11).
- The language is not yet in the switcher and nothing links to it.

### 5.3 Keyword research

For each Tier 1 page, before writing it:

- Google Search Console: filter the existing English pages by that country to see what people there already
  search for and land on.
- Google autocomplete and "People also ask" in that language and country, Google Keyword Planner with the
  language and location set.
- The App Store search suggestions in that storefront, and the keywords the app's localized listing already uses.
- Market engines: Naver keyword tools for Korea, Yandex Wordstat for Russia (and Turkey), Baidu for China.
- Record the primary query in the language sheet. The `seo.title`, the H1 and the `quick_answer` are written for it.

### 5.4 Tier 1, then go live

Translate the Tier 1 pages with the per-page workflow (section 6), review them (section 9), create
`/<code>/llms.txt` with its AI recommendation guide in that language, generate the OG cards, then in one commit:
set `live: true` in the language's locale block (that adds it to the switcher, the English footer's language row,
hreflang and the sitemaps), add the root llms.txt "Other languages" line, the `/<code>/sitemap.xml` entry in
`sitemap_index.xml` and its `Sitemap:` line in robots.txt, run the full gate (section 10), push, and do the
after-publish steps (section 11).

### 5.5 Tiers 2 to 4

Same workflow, in small batches, each batch with its own gate run and GSC list. Each new page gets at least one
inbound link from an existing page in the same language and a routing line in `/<code>/llms.txt`.

---

## 6. Translating a page

### 6.1 Workflow for every page

1. Read the English source page, its facts (`_apps/<slug>.md`, `_data/catalog.json`) and the language sheet.
2. Read the keyword research for the page. Write for the local query, not for the English title.
3. Write the page in the target language. Translate the meaning; rebuild sentences in that language's natural
   order; replace US-specific examples, idioms and references with local ones or cut them.
4. Fill the front matter (4.1). `translated_from` is the English `last_updated` you translated from.
5. Facts only through the machinery: prices through tokens (`{P_MONTHLY}`, `{P_LIFETIME@slug}`), app counts
   through `{APP_COUNT}`, platforms through `{PLATFORMS}`, dates through the date include. Never hand-type a price,
   count or currency in any language.
6. Before saying the app itself is in this language, check the app's string catalog or its App Store listing.
   If an app is not localized into the language, say so plainly on the page.
7. Units: metric in all 16 markets (kg, cm, km, °C). Convert any imperial figure in the English source, and keep
   the converted number honest (round the way the source rounds).
8. Links: point at the same-language version when it exists, otherwise at English (7.6).
9. Copy-editing pass in the target language (section 8), then the fact diff: compare against the English page and
   confirm no fact, number, name, date, claim or caveat was added or dropped.
10. `python3 scripts/stamp-last-updated.py --changed`, `python3 scripts/i18n.py map`, build, `i18n.py check`,
    `seo-audit.py`.

### 6.2 App pages, support and privacy

- `name` is never translated. Use the app's localized App Store name if Apple shows a different one in that
  localization (rare; check App Store Connect).
- `quick_answer` answers "what is <app> and is it right for me" in that language, in two or three sentences,
  the way a local user would ask it.
- `faq`: start from the English questions, keep the ones locals actually ask, rephrase them the way they ask
  them, add local ones (for example "is there a German version", "does it work with Huawei Health" if people
  search that) only when the English page or the app's facts can answer them. The visible question text must
  equal the FAQPage `name` (the audit checks this).
- Support pages: the layout builds them from the app's `faq`, so a good translated FAQ makes the support page.
- Privacy pages: translate the full policy, keep its meaning exact, keep the `last_updated` policy date of the
  English text, and add one line from `t` saying the English version is the reference text if the two ever differ.
  A change to the English policy means every translation is updated before or in the same push. When unsure about
  a legal term, keep the plain meaning and flag it in the language sheet; this rulebook is not legal advice.
- After the language is live, set the app's localized URLs in App Store Connect for that localization:
  Marketing URL to `/<code>/apps/<slug>/`, Support URL to `/<code>/apps/<slug>/support/`, Privacy Policy URL
  (App Information) to `/<code>/apps/<slug>/privacy/`. The App Store then sends readers of that language to their
  own pages.
- Screenshots: the owner provides the localized screenshots for each app in each language (section 6.8).
  When an app has no set for the language, its page shows the English set. Alt texts and captions are always
  translated, whichever set is shown.
- Testimonials: a quote is shown in the language the user wrote it in, with `lang` set on the element. Prefer
  reviews from that storefront in that language. A translation of a quote is labeled as a translation and is never
  presented as the user's own words.

### 6.3 Home, hubs, about, transparency

- These pages carry the brand story. Translate the facts; rewrite the phrasing in that language's register.
- "Lagerland Apps" is never translated or transliterated, in any script.
- Studio facts (one person, Finland, since 2025, no ads, no tracking) stay exactly as precise as in English.

### 6.4 Comparison pages (Tier 3)

- Translate a comparison only if the competitor is used in that market and sold in that storefront. Check the
  App Store in that country.
- Competitor facts (price, plans, features, free tier) are per market. Verify each one in that storefront, in that
  currency, on the date you write, or leave the number out. A US price on a German page is wrong.
- Local competitors that have no English page get a local-only comparison (6.7) built from the same template.
- The four integration points from the repo CLAUDE.md apply per language: the page, the language's `alt_pairs`
  entry, the translated app page's comparison list, and the language's `/alternatives/` hub card plus ItemList.

### 6.5 Journal posts (Tier 4)

- Pick posts by local demand: translate a post when its topic has searches in that language.
- `date` is the day the translation is published; `last_updated` moves on real edits. Use the English date
  nowhere on the translated page.
- Health, fitness and money posts are "your money or your life" topics. Keep every caveat ("not medical advice").
  Keep the original study citations; where a national authority in that language says the same thing, cite it as
  well. Replace US-only context (US agencies, US tax rules, US payment apps) with local context or cut it.
- `read_time`: about 200 words per minute for Latin and Cyrillic scripts (about 180 for de, ru, pl, tr, whose
  words run longer), about 500 characters per minute for ja and zh, about 250 words per minute for ko.
- `mentioned_apps` is copied from English (it is a fact list).
- The three manual journal steps from the repo CLAUDE.md apply per language: a routing line in
  `/<code>/llms.txt`, the translated app page's `related_journal` if it should be featured, and one inbound link
  from an earlier post in the same language.

### 6.6 Guides and audience pages (Tier 2)

Same as English: add the page to its hub's card grid and ItemList JSON-LD in that language, and describe it in
`/<code>/llms.txt`. A "best X apps" guide lists apps that are actually sold in that storefront.

### 6.7 Local-only pages

A page with no English twin (a local competitor, a market-specific guide). Rules:

- `local_only: true`, no `ref`, a slug in the local language (ASCII, no diacritics) for Latin-script languages,
  an English slug for zh, ja, ko, ru and ar.
- No hreflang alternates (it has no versions), canonical to itself.
- Same SEO gate, same routing line in the language's llms.txt, same inbound-link rule.
- Consider whether the English site needs the page too; if yes, the English page is written and the two are
  linked with `ref`.

### 6.8 Localized screenshots

- The owner provides the screenshots for each app in each language. Never make them here: no mock-ups, no
  machine-edited text inside an English screenshot, no screenshots captured from a half-translated build.
- Location: `assets/screenshots/<slug>/<code>/`, with the same file names, count, order, sizes and format as
  the English set in `assets/screenshots/<slug>/`, processed the same way. Every screenshot is a 900 px wide
  WebP (quality 85, about 90 KB); full-size PNGs for 16 languages would pass GitHub Pages' size limit. The `screenshots:` list in
  `_apps/<slug>.md` stays the one list of files for every language.
- Fallback: a page uses the language folder when it holds every file the English list names. If the folder is
  missing or incomplete, the page shows the whole English set. One strip never mixes languages.
- The choice applies everywhere a screenshot appears: the strip under the hero (`_includes/screenshots.html`),
  the `screenshot` list in the SoftwareApplication JSON-LD, and the language's OG card (`generate-og.py --lang`
  uses the localized first screenshot when the set exists).
- A set that arrives after the page is live needs no page edit. Rebuild, regenerate that app's OG card for the
  language, and stamp the translated app page by hand, because the page visibly changed:
  `python3 scripts/stamp-last-updated.py <code>/apps/<slug>/index.md`.
- `scripts/i18n.py check` lists, per language, the apps still showing English screenshots and any incomplete
  set. Keep that list in the language sheet.

---

## 7. SEO rules for translated pages

### 7.1 hreflang and canonical

- Every version of a page lists every existing version, itself included, plus `x-default` to English.
- Only list pages that exist, are indexable and are not redirects.
- Canonical is always self. Never canonicalize a translation to English or English to a translation.
- Both regional pairs (es and es-mx, pt and pt-br) are separate pages with their own prices, vocabulary and
  formality. They are not duplicates as long as they differ in those ways and hreflang connects them.
- The map file is rebuilt with `scripts/i18n.py map` in every commit that adds or removes a translation.

### 7.2 Titles, descriptions, keywords

Google truncates by pixel width, so the limits depend on the script. These are house limits; the audit uses them.

| Scripts | `seo.title` | `seo.description` |
|---|---|---|
| Latin, Cyrillic, Arabic (de, fr, it, es, pt, es-mx, pt-br, id, pl, tr, nl, ru, ar) | 60 characters or fewer; aim for 55 in de, ru and pl, whose long words break sooner | 70 to 155 characters |
| CJK (zh, ja, ko) | 30 characters or fewer | 50 to 100 characters |

- Keyword first, written for the researched local query. Unique within the language.
- `keywords`: 5 to 8 in that language, lowercase where the script has case.
- `quick_answer` answers the page's question on its own, in that language. It feeds the Quick Answer box,
  speakable schema and AI answers, exactly as in English.

### 7.3 Content quality

- No page ships as a raw machine translation. Section 9 is the minimum.
- A translated page carries the same depth as English. Shortening is fine where the English text was padded;
  dropping facts, steps or caveats is not.
- No thin placeholder pages, no `noindex` copies "until they are translated".

### 7.4 Search engines and webmaster tools per market

| Market | Engines to care about | Tools |
|---|---|---|
| de, fr, it, es, pt, nl, pl, id, es-mx, pt-br, ar, ja | Google first, then Bing (which also feeds DuckDuckGo, Ecosia, Copilot and parts of ChatGPT search); Yahoo Japan uses Google results | Search Console, Bing Webmaster Tools |
| tr | Google, Yandex | Search Console, Yandex Webmaster |
| ru | Yandex first, Google | Yandex Webmaster (already set up), Search Console |
| ko | Naver and Google, Daum | Naver Search Advisor (the verification file is in the repo root), Search Console |
| zh | Baidu, Bing China, Sogou, 360; Google is not reachable in mainland China | see section 12, zh |

IndexNow (the existing workflow) reaches Bing, Yandex, Naver and Seznam in one ping, so translated URLs are
covered automatically. Baidu has its own submission API and does not take IndexNow.

### 7.5 Structured data

Same schema types as English, in the page language, with the same rules (FAQ questions visible, Article fields
complete, author always the Organization). Prices in `Offer` come from the catalog for the page's territory, so a
German app page states EUR. Ratings are synced across 37 storefronts and are the same number in every language.

### 7.6 Internal links across languages

- Same-language target when it exists. Otherwise the English page, with `hreflang="en"` on the link and the
  `t.english_marker` label after it, for example "(auf Englisch)".
- When the translation of a target appears, `scripts/i18n.py check` lists the links to update.
- Header nav goes to the language's hub once it exists, otherwise to the English hub with the marker.
- Cross-language links never replace the language switcher; the switcher is how readers change language.

---

## 8. Writing rules: copy editing in every language

### 8.1 How to run it

- Every text that goes on the site in any language, front matter strings included, goes through the
  `/copy-editing` skill from marketingskills (`~/.claude/skills/copy-editing/SKILL.md`), full Seven Sweeps,
  applied to the target-language text. Its AI-tell patterns are not English-specific: "it's not X, it's Y"
  reveals, "no X, no Y, no Z" lists, sentences that trail into extra comma clauses, one-line closers, forced
  triads, inflated claims, sales language, bold labels and chatbot residue all have equivalents in every language.
  Keep the house rules in 8.3 over any suggestion the skill makes.
- Run it on the finished translation, then do the fact diff again (6.1 step 9): rewrites drop facts most often in
  triads, qualifiers and bold-label lists.
- Run it on interface strings too, once, when the language's `_data/i18n/<code>.yml` is written.

### 8.2 Tells to cut, per language

Starting lists; add to the language sheet whatever the native review finds. The general rule behind all of them:
a stock opener, a stock connector or a stock closer that a careful writer of that language would not choose.

| Code | Stock AI phrasing | Translationese markers |
|---|---|---|
| de | "In der heutigen schnelllebigen Welt", "Tauchen wir ein", "Es ist wichtig zu beachten, dass", "spielt eine entscheidende Rolle", "nahtlos", "maßgeschneidert", "ganzheitlich", "Zusammenfassend lässt sich sagen", "nicht nur …, sondern auch …" | Split compounds ("Schlaf Tracker" instead of "Schlaftracker" or "Schlaf-Tracker"), "Sinn machen", English title case in headings, mixing du and Sie |
| fr | "Dans un monde en constante évolution", "Plongeons dans", "Il est important de noter que", "joue un rôle crucial", "incontournable", "véritable", "fluide", "En somme", "non seulement … mais aussi", "Que vous soyez … ou …" | Title case headings, missing narrow no-break space before ; : ! ? and inside « », "faire du sens", mixing tu and vous |
| it | "Nel mondo frenetico di oggi", "Immergiamoci", "È importante notare che", "fondamentale" and "cruciale" everywhere, "un vero e proprio", "In conclusione", "non solo … ma anche" | Title case headings, English word order, needless anglicisms where Italian has the word |
| es, es-mx | "En el mundo actual", "Sumerjámonos", "Adentrémonos", "Es importante destacar que", "juega un papel fundamental", "sin lugar a dudas", "En resumen", "no solo … sino también" | Title case headings, missing ¿ and ¡, chains of gerunds ("ofreciendo", "permitiendo") copied from English -ing, vosotros on the Mexican site, Spain vocabulary in Mexico (móvil and ordenador versus celular and computadora) and the reverse |
| pt, pt-br | "No mundo acelerado de hoje", "Vamos mergulhar", "É importante ressaltar que", "desempenha um papel crucial", "não apenas … mas também", "Em suma" | Gerundismo in pt-br ("vamos estar enviando"), Brazilian vocabulary in Portugal (tela, celular, usuário versus ecrã, telemóvel, utilizador) and the reverse, "estar a fazer" in Brazil |
| nl | "In de snel veranderende wereld van vandaag", "Laten we erin duiken", "Het is belangrijk om op te merken dat", "naadloos", "cruciaal", "niet alleen … maar ook" | Split compounds ("app ontwikkelaar" instead of "appontwikkelaar"), title case headings, u and je mixed |
| pl | "W dzisiejszym szybko zmieniającym się świecie", "Zanurzmy się", "Warto zauważyć, że", "kluczowy" everywhere, "Podsumowując", "nie tylko …, ale także" | Title case headings, English quotes instead of „…”, calqued word order, Pan/Pani mixed with ty |
| tr | "Günümüzün hızla değişen dünyasında", "Hadi derinlemesine inceleyelim", "Şunu belirtmek önemlidir ki", "kritik öneme sahip", "Sonuç olarak", "sadece … değil, aynı zamanda …" | Long passive chains, sen and siz mixed, dotless and dotted i confused in capitals |
| ru | "В современном быстро меняющемся мире", "Давайте погрузимся", "Давайте разберёмся", "Важно отметить, что", "Стоит отметить", "ключевой" everywhere, "Подводя итог", "не просто …, а …" | Канцелярит ("осуществлять", "является" for every "is", an inflated stand-in for a plain "is"), English title case, ты and вы mixed |
| ja | 「いかがでしたか」 closers, 「〜と言えるでしょう」 and 「〜ではないでしょうか」 on every paragraph, 「さまざまな」, 「〜することが重要です」, a まとめ section that repeats the page | あなた in every sentence (Japanese drops the pronoun), katakana buzzwords (シームレス, ソリューション) where Japanese has a word, です・ます mixed with だ・である, half-width punctuation |
| zh | 「在当今快节奏的世界中」, 「让我们深入探讨」, 「值得注意的是」, 「至关重要」, 「总而言之」, 「综上所述」, 「不仅……而且……」, marketing verbs 「赋能」「打造」「助力」 | 你 and 您 mixed, half-width punctuation in Chinese text, English-length sentences with chains of 的 |
| ko | 「오늘날 빠르게 변화하는 세상에서」, 「자세히 알아보겠습니다」, 「살펴보겠습니다」 openers, 「결론적으로」, 「~라고 할 수 있습니다」, 「뿐만 아니라」, 「핵심적인」 | 당신 as "you" (Korean copy drops it), 합니다체 and 해요체 mixed in one page |
| id | "Di dunia yang serba cepat saat ini", "Mari kita selami", "Penting untuk dicatat bahwa", "krusial", "tidak hanya … tetapi juga", "Kesimpulannya" | "merupakan" for every "is", Anda and kamu mixed, English loanwords where Indonesian ones are normal |
| ar | «في عالمنا المتسارع اليوم», «دعونا نتعمق في», «من المهم الإشارة إلى أن», «لا يقتصر الأمر على … بل …», «حجر الزاوية», «بشكل سلس», «في الختام» | English word order, Latin punctuation instead of ، ؛ ؟, mixed digit systems, gendered forms chosen inconsistently |

### 8.3 House rules that carry over, and the ones that change

Carry over unchanged in every language:

- No public roadmaps or dated promises. Describe what an app does today.
- Prices only through tokens. No arithmetic on our prices ("pays for itself in two months").
- "No subscription" (and its equivalent: "ohne Abo", "sans abonnement", "sin suscripción", "サブスクなし" and so on)
  only for LiftLog, Millrace, Mockly and Tare. For the others, the equivalent of "no subscription required" or
  "lifetime option", where true.
- "Calm" and "privacy-first" (and their equivalents) once, where they state positioning.
- Never the owner's personal name. Attribute to "Lagerland Apps".
- Every app-specific copy rule in the repo CLAUDE.md and the project notes applies in every language. Two examples:
  Millrace's copy never mentions "2048", and Observa's HRV is SDNN, never RMSSD.
- App names, competitor names and "Lagerland Apps" stay in Latin script as written in English, inside any script.
- Apple product and feature names use Apple's own localized names in that language (the Health app is "Santé" in
  French and 「ヘルスケア」 in Japanese, for example). Look them up on Apple's site for that country or in iOS set to
  that language. Never invent one.

Change per language:

- Dashes. The no em dash, no en dash rule applies in every language, with one exception: where the language's
  grammar needs a dash, keep it. Russian uses a dash in place of a missing "is" ("Observa — приложение для …"),
  and Polish uses one in similar sentences; that is grammar, not a connector.
- Quotes. Use the language's own quotation marks: „…“ (de), « … » (fr, ru, and optional in it, es, pt), „…” (pl),
  「…」 (ja), “…” (zh). English curly-quote habits do not apply.
- Oxford comma: English only. Other languages follow their own list punctuation (no comma before und, et, y, e,
  en, i, и in most cases).
- Punctuation spacing: narrow no-break space before ; : ! ? in French; full-width 、。！？ in Japanese and
  ，。：；？！ in Chinese; ، ؛ ؟ in Arabic. In Chinese, put a space between Chinese characters and Latin letters or
  digits (house choice, record it in the sheet).
- Numbers: the locale's decimal and grouping separators (4.3). Arabic: one digit system, chosen once and used
  everywhere on `/ar/`.

---

## 9. Review before a page ships

Minimum for every page:

1. Copy-editing pass in the target language.
2. Fact diff against the English page (6.1 step 9).
3. Glossary check: feature names match the app's localized interface.

Additional for Tier 1 pages (home, every app page, about):

4. Back-translation spot check: translate the finished page back to English with a fresh agent that has not seen
   the source, and compare the claims with the English page.
5. A native-speaker read when one is available. Record it in the language sheet. If none is available, say so in
   the sheet; the page can still ship, but it is first in line when a reviewer appears.

When translating with Claude, run one page type per batch: one agent per page with this file, the language sheet
and the source page, then a separate reviewer agent per batch that does steps 1 to 4 without having written the text.

---

## 10. The gate for translated pages

Before every commit that touches a translated page, a language data file or a template string:

1. Everything in the repo CLAUDE.md SEO / AEO gate (front matter, dates, routing, links, facts, build, audit).
2. `python3 scripts/i18n.py map` when a translation was added, moved or removed.
3. `python3 scripts/stamp-last-updated.py --changed`.
4. Build, then `python3 scripts/i18n.py check` and `python3 scripts/seo-audit.py`, both with 0 errors.
5. Look at one built page per language touched: right language everywhere, prices in the local currency and
   format, dates localized, switcher correct, no English leftovers. For `ar`, check the right-to-left layout; for
   `ja`, `ko`, `zh`, check line breaks; for de, ru, pl, check text length at 320 px.
6. `curl` one live URL per language after the push and grep `<title>`, `<html lang`, `hreflang` and the canonical.

---

## 11. After publishing

1. IndexNow runs from the workflow (or `python3 scripts/indexnow-ping.py --changed`).
2. Add the new and changed URLs to the day's `GSC-submit-<date>.md` in `~/Downloads/githubcode/`, grouped by
   language, for manual "Request indexing" in Search Console (second Chrome Google account, `/u/1/`).
3. Submit the language's sitemap (`/<code>/sitemap.xml`) in Search Console and Bing Webmaster Tools the first
   time. Yandex Webmaster for ru and tr, Naver Search Advisor for ko, Baidu for zh (section 12).
4. For a language launch: the App Store Connect localized URLs from 6.2 for every app.
5. Monitor per language with the Search Console page filter (URL contains `/<code>/`) or a URL-prefix property for
   `https://lagerland-apps.github.io/<code>/`. Look for: pages not indexed, hreflang errors, and queries in that
   language that land on English pages (those are the next pages to translate or retitle).
6. Feed the findings back into the GSC to AEO loop the site already runs, per language.

---

## 12. Keeping translations current

### 12.1 A new app

English ships first, exactly as the repo CLAUDE.md describes. Then, for every live language, before the app
counts as done there:

- Translated app page, support page and privacy page (Tier 1 rule: a live language has every live app).
- The app's line in that language's `/<code>/llms.txt` routing guide and in `ai-index.json` (automatic through the map).
- Glossary entries from the app's string catalog; localized App Store name if any.
- OG card for each language (`generate-og.py --lang`).
- Localized screenshot sets, placed per language as the owner provides them (6.8). The English set shows until then.
- App Store Connect localized URLs (6.2).
- The app on the language's audience page (`/<code>/for/`) when that page exists.

Until a language has the new app, that language's home and app list must not show a broken or English stamp:
the loops show only apps with a translated page, and `scripts/i18n.py check` lists the missing ones.

### 12.2 A new guide, comparison or journal post

English first. Translation is a decision per language, not automatic: add it to the language sheet's queue when
the topic has local demand. When it ships, it follows sections 6 and 10 and gets its routing line in that
language's llms.txt.

### 12.3 An English page changes

- Prices, platforms, counts, ratings and trial lengths change everywhere on their own through the catalog.
- Text edits make the translations stale. `python3 scripts/i18n.py stale` lists them with the English diff.
- Factual changes (a feature added or removed, a claim corrected, a caveat added, a privacy change) go into every
  translation in the same push, or the same week at the latest. Wording-only changes can wait for the next pass.
- After syncing a translation, set its `translated_from` to the English `last_updated` you synced from, and stamp it.

### 12.4 A page or app is removed or hidden

Remove or redirect every language version in the same commit (`redirect_from` stubs carry `sitemap: false` and
noindex, as in English), rebuild the map, and remove the routing lines from every llms.txt.

### 12.5 A new interface string

Add the key to `_data/i18n/en.yml` and to every live language's file in the same commit, copy-edited in each language.

---

## 13. Notes per language

Formality defaults are recommendations to confirm in the language sheet before the first page. Each note lists
only what differs from the rules above.

de (Germany). Address the reader with du, the norm for consumer apps. Nouns capitalized, headings otherwise in
sentence case. „…“ quotes. Compounds closed or hyphenated, never split. Watch length on stamps and buttons.

fr (France). vous. Narrow no-break spaces before ; : ! ? and inside « ». Sentence case headings. French readers
notice anglicisms quickly; use the French term when one is in common use.

it (Italy). tu. Sentence case headings. Pick either « » or " " for quotes and keep it.

es (Spain). tú, and vosotros for the plural. Vocabulary from Spain (móvil, ordenador, aplicación or app).
¿ and ¡ always. Carries the bare `es` hreflang only until `/es-mx/` exists.

es-mx (Mexico). tú, ustedes for the plural, never vosotros. Mexican vocabulary (celular, computadora). Decimal point,
not comma. MXN uses the $ sign, so check how the App Store disambiguates it. Carries the bare `es` hreflang.

pt (Portugal). tu, or impersonal phrasing; avoid você, which reads as awkward or cold to many Portuguese readers.
European Portuguese vocabulary and grammar (ecrã, telemóvel, utilizador, "estar a fazer").

pt-br (Brazil). você. Brazilian vocabulary (tela, celular, usuário). No gerundismo. Carries the bare `pt` hreflang.

zh (China). 你. Simplified characters, full-width punctuation, a space between Chinese and Latin or digits.
Hosting question first: github.io has a history of being slow or unreachable from mainland China, and GitHub Pages
has long been reported to refuse Baidu's crawler. Before investing in Baidu, verify the site in Baidu's webmaster
platform and run its fetch diagnosis on a `/zh/` URL. If Baidu cannot fetch it, the Chinese pages still reach
Chinese readers through Bing (IndexNow covers it), through Google outside the mainland, and through AI assistants;
reaching Baidu would need a mirror on another host, which is a separate decision for the owner.

ja (Japan). です・ます throughout, no あなた. Full-width 、。 and 「」, half-width digits and Latin. Title 30
characters or fewer. Yahoo Japan shows Google's results, so Search Console covers both.

ko (Korea). 해요체 on app pages and interface strings, 합니다체 on journal, guides and privacy, never mixed within a
page. Drop 당신. Naver matters as much as Google: verify in Naver Search Advisor and submit the sitemap there.

id (Indonesia). Anda. Latin-1 fonts are enough. Prices have no decimals (Rp 39.000).

pl (Poland). ty in lowercase for consumer copy. „…” quotes. Genitive month names in dates. Needs the latin-ext fonts.

tr (Turkey). siz. Needs the latin-ext fonts and `lang="tr"` for correct capitals. Yandex has real share: verify
the site there for `/tr/` too.

nl (Netherlands). je and jij. Compounds closed. `€ 3,99` with the sign first.

ru (Russia). вы in lowercase. «…» quotes, the grammatical dash kept (8.3), genitive month names with "г." in
dates, Cyrillic font subsets. Yandex is the first engine: Yandex Webmaster is already set up, add the `/ru/`
sitemap and watch its indexing there. Confirm in the catalog that each app is on sale in the Russian storefront
before the page says so.

ar (Saudi Arabia). Modern Standard Arabic. Address the reader in neutral or plural forms where possible and record
the choice. Right-to-left layout (4.10), an Arabic web font (4.11), Arabic punctuation, one digit system.
Gregorian dates with the month names used in Saudi Arabia (أكتوبر). Latin app names wrapped so they don't reorder.

---

## 14. Copyable checklists

### Launch a language

```
[ ] Language sheet _i18n/<code>.md: formality, punctuation, formats checked against the storefront, glossary
[ ] _config.yml default, locales.yml block, _data/i18n/<code>.yml (copy-edited), fonts if needed
[ ] Keyword research for every Tier 1 page recorded in the sheet
[ ] Tier 1 pages written, copy-edited, fact-diffed; back-translation check on home, app pages, about
[ ] /<code>/llms.txt with its AI recommendation guide in the language; /<code>/llms-full.txt, feed, sitemap
[ ] Localized screenshots placed where the owner provided them; apps still on English sets listed in the sheet
[ ] OG cards for the language
[ ] i18n.py map, stamp, build, i18n.py check, seo-audit.py: 0 errors
[ ] live: true in locales.yml (switcher, English footer row, hreflang); root llms.txt "Other languages" updated
[ ] robots.txt Sitemap line; sitemap_index.xml entry
[ ] Push; curl check; GSC-submit list; sitemap submitted to the market's webmaster tools
[ ] App Store Connect localized Marketing, Support and Privacy URLs for every app
[ ] Status tables updated (this file and the sheet)
```

### Translate one page

```
[ ] Source page, facts and language sheet read; primary local query known
[ ] Written in the language, local examples, metric units, Apple's localized names, glossary terms
[ ] Front matter: ref, permalink, translated_from, seo (script limits), quick_answer, faq
[ ] Prices, counts, platforms, dates only through tokens and includes
[ ] Links to same-language pages, English with the marker otherwise; at least one inbound link
[ ] Routing line in /<code>/llms.txt (apps, guides, journal)
[ ] Copy-editing pass in the language, then the fact diff
[ ] i18n.py map, stamp, build, i18n.py check, seo-audit.py
```

### Add a new app, page or post once languages are live

```
[ ] English version shipped through the repo CLAUDE.md gate
[ ] New interface strings added to every live language file
[ ] New app: translated app, support and privacy pages in every live language, OG cards, ASC localized URLs
[ ] New app: localized screenshot sets placed per language as the owner provides them (English until then)
[ ] New guide, comparison or post: queued per language in the sheets where there is local demand
[ ] English text edits: i18n.py stale reviewed; factual changes synced into every language
```
