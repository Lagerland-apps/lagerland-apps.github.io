# Writer brief: German (de, Germany) Tier 3, batch 4 (comparison pages), 2026-11-19

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

German is live; 35 German comparisons already exist under `de/alternatives/`. They are reviewed and are your
best model for German wording, structure and Liquid. You write ONE page.

## Read first, in this order

1. `TRANSLATION.md` sections 6.1, 6.4, 6.7, 7.2, 7.5, 7.6, 8 (all) and 9.
2. `_i18n/de.md`, all of it: du (lowercase, never Sie), „…“ quotes, decimal comma, U+00A0 before €, closed or
   hyphenated compounds, no em/en dashes, no Oxford comma, and the full «Tells to cut in German» list.
3. `_i18n/de-apple-terms.md` (Apple's German names; App Privacy labels are quoted only from there),
   `_i18n/de-glossary.md` (your app's section) and `_i18n/de-keywords.md` (your app's section).
4. The German app page `de/apps/<app>/index.md`: its tier names, feature names and wording are reviewed; reuse them.
5. The English source page `alternatives/<slug>.html`: it holds the facts about OUR app and the comparison. Write
   from English, the way a good German copywriter would write the page from those facts. Not sentence by sentence.
6. Structure model: the German comparison listed for your page below (front matter, Liquid, JSON-LD skeleton,
   tables, cards, how tokens and `l.html` links are written, the „Stand“ line on competitor prices). Where a
   French/Spanish/Portuguese page with your slug exists, look at it ONLY to see how that session replaced US
   competitor data with its own store's data. Never translate from it.
7. `/Users/anttiaittamaa/Downloads/githubcode/de-tier3-store-2026-11-19.md`: the competitor in the GERMAN App Store,
   checked today (German store name, German ratings, languages, devices, IAP rows in euro, full German description).
8. Your app's blueprint, claims register §10 only (never §8 non-claims or §9 hidden items). Paths are in
   `/Users/anttiaittamaa/Downloads/githubcode/.agents/product-marketing.md` (section 2 table).
9. `/Users/anttiaittamaa/Downloads/githubcode/ISSUES.md` items I-0380, I-0142, I-0157 (known English-side errors on
   the Jefit and StrongLifts pages: undated US prices and loose claims). Don't copy those errors into German.

## Pages in this batch

| English source | Write to | Our app | German structure model | Primary query | Secondary queries (only these, plus app-side ones from de-keywords.md) |
|---|---|---|---|---|---|
| alternatives/chess-com.html | de/alternatives/chess-com.html | Chessful | de/alternatives/lichess.html | `chess.com alternative` | `chess.com kosten`, `chess.com premium kosten`, `chess.com kostenlose analyse`, `chess.com oder lichess`, `chessful vs chess.com` |
| alternatives/chessable.html | de/alternatives/chessable.html | Chessful | de/alternatives/lichess.html | `chessable alternative` | `chessable kosten`, `chessable deutsch`, `chessable erfahrungen`, `chessable kurse deutsch` |
| alternatives/pdf-expert.html | de/alternatives/pdf-expert.html | MediaKit | de/alternatives/cloudconvert.html | `pdf expert alternative` | `pdf expert kostenlose alternative`, `pdf expert kostenlos`, `pdf expert abo kosten`, `pdf expert alternative mac`, `pdf expert alternative ipad` |
| alternatives/documents-by-readdle.html | de/alternatives/documents-by-readdle.html | MediaKit | de/alternatives/cloudconvert.html | `documents readdle alternative` | `documents by readdle alternative`, `documents readdle kosten`, `readdle documents preise`, `dokumente app readdle` |
| alternatives/handbrake.html | de/alternatives/handbrake.html | MediaKit | de/alternatives/convertio.html | `handbrake alternative mac` | `handbrake alternative`, `handbrake iphone`, `handbrake video komprimieren`, `video konvertieren mac` |
| alternatives/jefit.html | de/alternatives/jefit.html | GymLogger X | de/alternatives/fitbod.html | `jefit alternative` | `jefit kosten`, `jefit erfahrungen`, `jefit deutsch`, `jefit apple watch` |
| alternatives/stronglifts-5x5.html | de/alternatives/stronglifts-5x5.html | GymLogger X | de/alternatives/alpha-progression.html | `stronglifts 5x5 alternative` | `stronglifts alternative`, `stronglifts 5x5 app`, `stronglifts 5x5 deutsch`, `stronglifts 5x5 apple watch` |
| alternatives/gentler-streak.html | de/alternatives/gentler-streak.html | Observa | de/alternatives/bevel.html | `gentler streak alternative` | `gentler streak kosten`, `gentler streak deutsch`, `gentler streak erfahrungen`, `gentler streak apple watch` |
| alternatives/rise-sleep-tracker.html | de/alternatives/rise-sleep-tracker.html | AfterShift | de/alternatives/autosleep.html | `rise app alternative` | `rise schlaf app`, `rise schlaf app erfahrungen`, `rise app kosten` |
| alternatives/hrv4training.html | de/alternatives/hrv4training.html | Observa | de/alternatives/welltory.html | `hrv4training alternative` | `hrv4training deutsch`, `hrv4training erfahrungen`, `hrv4training apple watch`, `hrv messen apple watch` |
| (local-only, no English twin) | de/alternatives/splid-alternative.html | RightSplit | de/alternatives/finanzguru-alternative.html (local-only front matter) + de/alternatives/tricount.html (body) | `splid alternative` | `splid app kostenlos`, `splid alternative kostenlos`, `splid oder splitwise`, `splid oder tricount`, `splid app erfahrungen`, `splid pro version` |

Demand evidence (Google suggest de/DE, 2026-11-19; German store ratings): Chess.com 103.987, PDF Expert 63.961,
Documents 64.073, Splid 40.566, RISE 2.247, Jefit 1.325, StrongLifts 1.204, Gentler Streak 1.136, Chessable 1.132,
HRV4Training 89 (paid). HandBrake is a desktop program.

Keyword collisions (never in your seo.title or as your primary; fine in body text): `schach app`, `schach lernen app`,
`schach analyse app` (Chessful app page); `beste schach app iphone` (chess guide); `schach app lichess` (Lichess page);
`video komprimieren iphone`, `pdf komprimieren iphone`, `video konvertieren iphone` (MediaKit app page);
`mkv in mp4 umwandeln` (journal post); `trainingstagebuch app`, `trainingstagebuch apple watch`, `apple watch
krafttraining app` (GymLogger X); `hrv app`, `hrv apple health`, `schlaf analyse app` (Observa); `schichtarbeit schlaf`,
`nachtschicht schlafen` (AfterShift, /de/for/shift-workers/); `rechnung teilen app`, `kosten teilen app` (RightSplit);
`splitwise alternative`, `tricount alternative`, `settle up app alternative` (their pages). Pages for the same app
must not share a seo.title pattern: vary the angle after the colon.

## Competitor facts (TRANSLATION.md 6.4)

- Every fact about the competitor is per market. Use ONLY the German store file (and what the English page says that
  is not market-specific, such as how the product works). A US price, US rating or US-only feature is wrong here.
- Prices: only the euro amounts in the store file's IAP rows (or a web price the store file quotes with its URL),
  typed `9,99 €` with U+00A0 before €, plus one „Stand“ sentence per page in the style of de/alternatives/fitbod.html
  („Die Preise … haben wir am 19. November 2026 im deutschen App Store geprüft …“). Several rows for one plan: give a
  range („zwischen 4,99 € und 9,99 € im Monat“). No row for a plan the English page prices: keep the qualitative fact
  („Abo, monatlich oder jährlich“) and drop the number. Never convert dollars. No arithmetic on OUR prices.
- Ratings: only the German count and average from the store file („Im deutschen App Store hat … 4,8 von 5 Sternen bei
  13.704 Bewertungen, Stand 19. November 2026“), or leave ratings out.
- Competitor names as in English (Chess.com, Chessable, PDF Expert, Documents by Readdle, HandBrake, Jefit/JEFIT as
  the English page writes it, StrongLifts 5x5, Gentler Streak, RISE, HRV4Training, Splid). The German store title once
  where it helps people find the app („Dokumente – …“ is Readdle's German name: write it with a colon or in quotes, no
  dash). Competitor App Store links: `https://apps.apple.com/de/app/id<ID>`.
- Languages: say whether the competitor's listing includes German only from the store file. Never invent interface
  languages.
- Feature claims about competitors: only what the English page says, cross-checked against the German description.
  If the German description contradicts the English page (feature gone, now free, now paid), follow the German store
  file and report the English-side error in your reply.

## Our apps' rules on these pages

- Prices only through tokens, single brace, exactly as the German model pages write them (`{P_MONTHLY@observa}`,
  `{P_LIFETIME@mediakit}` …). Never type our price, an app count or a platform list.
- „Ohne Abo“ only for LiftLog, Millrace, Mockly and Tare. Chessful, MediaKit, GymLogger X, Observa, AfterShift and
  RightSplit sell subscriptions: write „kein Abo nötig“ or „auch als Einmalkauf“ only where the English page and the
  catalog support it. Answer „kostenlos“ queries with the facts (free tier, what Pro/Premium adds), never by calling
  our app free when a feature is paid.
- Tier names: Chessful Pro, MediaKit Pro, GymLogger X Pro, Observa Premium, AfterShift Premium, RightSplit Pro+
  (with „Bereiche“ for Spaces, as de/apps/rightsplit/index.md writes it). Feature names as on the German app page and in the glossary.
- Observa: „HRV (SDNN)“, never RMSSD as Observa's HRV; Apple's „Health“ app name as in de-apple-terms.md; medical
  caveats exactly as strong as in English. AfterShift and Observa pages are health topics: keep every caveat.
- All 20 apps have a German interface (sheet, checked 2026-10-26); use the German UI names from the glossary.
- Disclose that the app is ours where the English page does (Lagerland Apps publishes the comparison).

## Links

- Internal links with `{% include l.html url="..." %}` exactly as the German model pages write them; never hard-code
  `/de/` in body links to pages that have an English twin (l.html picks the German page when it exists and adds the
  English marker otherwise, as the model shows). The local-only Splid page, the Finanzguru page and the hub are linked
  as plain `/de/alternatives/<slug>/`.
- Where the English page links another comparison of this batch, keep the link (l.html resolves it to German).
- Breadcrumb: `{{ site.url }}/de/alternatives/` named „Alternativen“, exactly as de/alternatives/bevel.html.
- `"inLanguage": "de"`. Keep the model's JSON-LD skeleton exactly (WebPage with BreadcrumbList, then FAQPage); never
  paste an ItemList into the breadcrumb.
- Every FAQ `name` equals its visible `<summary>` character for character; the schema answer says the same as the
  visible answer (the visible one may be shorter).

## Front matter

- Translations: `layout: default`, `ref: /alternatives/<slug>/`, `permalink: /de/alternatives/<slug>/`,
  `translated_from: <the English page's last_updated>`, `title` („<Competitor>-Alternative“ in the model's style),
  `quick_answer` (two to four sentences that answer „what's a good alternative to X and when is X the better choice“
  on their own), full `seo` (title ≤ 55 chars ideally, never > 60; description 70 to 155 chars; 5 to 8 lowercase
  keywords from the table above), `last_updated: 2026-11-19`.
- Splid (local-only): `layout: default`, `local_only: true`, NO `ref`, NO `translated_from`,
  `permalink: /de/alternatives/splid-alternative/`, `title: "Splid-Alternative"`, quick_answer, full seo,
  `last_updated: 2026-11-19`.

## Local-only page: de/alternatives/splid-alternative.html

- Splid („Splid – Abrechnen mit Freunden“, id991473495, seller Nicolas Jersch) is a German-made group-expense app with
  40.566 German ratings, more than Tricount in Germany. Facts about Splid ONLY from its German store description and
  IAP rows in the store file (quotes under 15 words, paraphrase the rest). Never claim anything about its data use,
  accounts, ads, sync or prices that the listing doesn't say; no review quotes.
- Body modelled on de/alternatives/tricount.html and de/alternatives/splitwise.html (same app, same reader); the
  French local-only page fr/alternatives/splid.html shows one way to structure a Splid page, but write from the facts.
- The page answers „splid alternative / splid app kostenlos / splid oder splitwise / splid oder tricount“ honestly:
  what Splid does (group expenses entered by hand, who owes whom, settle up), what RightSplit does instead (from
  `_apps/rightsplit.md`, `de/apps/rightsplit/index.md`, its glossary section and the blueprint §10), and when Splid is
  the better choice. Link the German Tricount and Splitwise comparisons once each with l.html, and the RightSplit app
  page.
- FAQ: four to six questions people ask (kostenlos?, Splid oder Splitwise?, Splid oder Tricount?, Konto nötig?,
  German UI?), answered only from the store file and our facts.
- Save any extra page you fetch into
  `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-rdt3ut/a3aafb6b-92be-4766-b02a-e38d08a951a3/scratchpad/de-t3/sources/splid/`.

## Lessons from earlier reviews (most common must-fix items)

- Softened or hardened hedges; added definitions that carry a claim; framing sentences added to FAQ answers.
- Stacked noun chains copied from English; „X als Standard“; „gebaut für“; „gilt als“; „dort“ as filler; capital
  „Sie“ meaning "they" at a sentence start (rephrase); headings stuffed with search phrases; a first paragraph that
  repeats the lede.
- A generic „Pro“ tier where the app's German UI says Premium.
- No gendered audience words; no raw-keyword seo.titles; no „(2026)“ padding; no meta description opening with a
  question; seo.keywords only from the table above or de-keywords.md.
- Price tokens single-brace; U+00A0 before €; „%“ with a space before it in German („25 %“).

## Do NOT

Run `jekyll build`, `i18n.py map`, the stamp script or any `git` command that changes state; touch any file but your
own page; edit English, French, Spanish, Italian, Portuguese or Dutch files; edit `de/llms.txt`, the hub or any app
page (the main session wires hubs, llms lines and inbound links). Other sessions (nl, fr, es, it, pt) work in this
same checkout. Don't fetch apps.apple.com (the store file has the data; it 429s); the iTunes lookup API
(`https://itunes.apple.com/lookup?id=<id>&country=de`) is fine for one more field.

## Reply with

1. The file you wrote and its word count against the English page's.
2. Your seo.title, seo.description and primary keyword.
3. Every competitor fact you dropped because German data was missing, and every place where the German store
   contradicted the English page (English-side errors, with the English line).
4. Anything about OUR app you couldn't verify in the German app page, glossary or blueprint §10.
5. Open questions for the owner, if any.
