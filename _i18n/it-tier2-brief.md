# Writer brief: Italian (it, Italy) Tier 2, batch 1 (guides and audience pages)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/it-writer-brief.md` first and follow all of it.** This file adds what is different for Tier 2.
Where the two disagree, this file wins.

## Your inputs

- The English source page (`guides/<slug>.html` or `for/<slug>.html`): it holds the facts.
- The French page with the same path under `fr/` (and the Spanish one under `es/`): structural template only (Liquid,
  JSON-LD skeleton, card and table markup, how links and tokens are written). Those writers replaced US-only context
  (US prices, US ratings) with their own market's data; you do the same with ITALY data. Never translate from French or
  Spanish.
- `/Users/anttiaittamaa/Downloads/githubcode/it-tier2-research-2026-11-19.md`: your page's row (Italian primary and
  secondary queries, demand) and the Italian App Store data at the bottom (which competitors are sold in Italy, their
  Italian store names, Italian rating counts, whether the listing is in Italian).
- `_i18n/it.md` (sheet), `_i18n/it-apple-terms.md`, `_i18n/it-glossary.md` (the sections of the apps your page names).

## Pages in this batch

| Page | Write to | Primary query |
|---|---|---|
| guides/best-chess-apps-iphone.html | it/guides/best-chess-apps-iphone.html | migliore app scacchi iphone |
| guides/best-logic-puzzle-games-iphone.html | it/guides/best-logic-puzzle-games-iphone.html | migliori giochi di logica iphone |
| guides/workout-app-without-subscription.html | it/guides/workout-app-without-subscription.html | app palestra gratis senza abbonamento |
| for/shift-workers.html | it/for/shift-workers.html | lavoro a turni e salute |
| for/apple-health-power-users.html | it/for/apple-health-power-users.html | migliore app salute apple watch |
| for/calm-productivity.html | it/for/calm-productivity.html | migliori app produttività iphone |
| (local-only, no English twin) | it/guides/limitare-tempo-di-utilizzo-iphone.html | come limitare il tempo di utilizzo di un app su iphone |
| (local-only, no English twin) | it/guides/come-mettere-conto-alla-rovescia-iphone.html | come mettere un conto alla rovescia su iphone |
| guides/index.html, for/index.html (hubs, written last) | it/guides/index.html, it/for/index.html | brand-led |

Keyword collisions to respect: `app scacchi` belongs to Chessful, `giochi di logica iphone` to Millrace, `giochi
rompicapo iphone` to Tare, `app diario allenamento palestra` and `app palestra senza abbonamento` to LiftLog, `app
scheda palestra apple watch` to GymLogger X, `dormire dopo il turno di notte` to AfterShift, `hrv apple watch` and `app
sonno apple watch` to Observa, `app to do list` and `app per organizzare la giornata` to Taskful Day, `bloccare app
iphone` to EarnLock, `conto alla rovescia iphone` and `app conto alla rovescia` to Soon. Don't use those as your primary
or in your `seo.title`; a mention in body text or as a secondary keyword is fine.

The workout guide may say «senza abbonamento» about LiftLog (house rule) and in the page's own framing (the English
page's subject is "without a subscription"), never about GymLogger X or a competitor that sells subscriptions.

## Competitors (Tier 2 rules, TRANSLATION.md 6.4 and 6.6)

- A "best X apps" page lists only apps sold in the Italian App Store (research file). An app marked NOT SOLD IN ITALY
  is dropped, with any sentence that depends on it.
- Competitor facts are per market. Ratings: only the Italian count and average from the research file, written as
  «Su App Store in Italia ha 4,7 su 5 con 44.551 valutazioni (dato del 19 novembre 2026)», or leave ratings out.
  Never the US, French or Spanish numbers.
- Competitor prices: the research file has Italian euro prices only for paid apps (Baba Is You 7,99 €, Threes! 6,99 €,
  Suika 2,99 €, AutoSleep 9,99 €, Kanazawa Shogi 2 6,99 €). In-app prices were NOT collected. You may fetch the
  apps.apple.com/it product page once per app (`curl -sL -A "Mozilla/5.0" "https://apps.apple.com/it/app/id<ID>"` (needs `-L`, and a full Safari UA string such as `"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 Safari/605.1.15"`; with a bare `Mozilla/5.0` the page is a 1147-byte JS shell), read
  the «Acquisti in-app» rows) and save it to your sources folder; if it fails (HTTP 429) or the row isn't there, drop
  the number and keep the qualitative fact («a pagamento», «abbonamento mensile o annuale», «acquisto unico»). Typed as
  `13,99 €` with U+00A0, with «(App Store in Italia, 19 novembre 2026)» once per page. Never convert dollars. Never
  arithmetic on OUR prices; arithmetic on a competitor's verified euro price only where the English page does the same
  calculation.
- Competitor names as in English (Chess.com, Hevy, Strong); the Italian store title may be mentioned once where it
  helps people find the app («su App Store in Italia si chiama “Scacchi - Giocare ed Imparare”»).
- App Store links to competitors: `https://apps.apple.com/it/app/id<ID>`.
- Where a competitor's Italian listing is in English only (research file: IT-lang False), you may say so once if the
  English page talks about the app's language; never invent the app's own interface languages.
- Feature claims about competitors: only what the English page says (or, on the local-only pages, what the app's own
  Italian App Store description says, see below).

## Links

- Use `{% include l.html url="..." %}` for every internal link, as the French and Spanish pages do. It resolves to the
  Italian page when it exists at build time (all Tier 1 pages and the other pages of this batch), else English with the
  marker. Do not hard-code `/it/` URLs in body links. The two local-only guides have no English twin: link them as
  plain `/it/guides/<slug>/` URLs.
- Each page links to the relevant Italian app pages and, where the English page links to another page of this batch,
  to it.
- Where the language matters, set `"inLanguage": "it-IT"` or `"it"` exactly as the Italian Tier 1 pages do
  (`grep -rn inLanguage it/ | head`); keep the French skeleton otherwise.

## YMYL pages (shift-workers, apple-health-power-users)

Keep every caveat and every "not medical advice" line. No new health claims, numbers or studies. Where the English
page cites a source, keep the citation. Apple names exactly as it-apple-terms.md: l’app Salute (never «Apple Salute»),
«HRV (SDNN)» for Observa's HRV, frequenza cardiaca a riposo, Apple sleep stages Veglia / REM / Principale / Profondo,
full immersion Sonno, tono cardiovascolare. AfterShift, Observa, GymLogger X, Taskful Day, AllPaid, Soon. feature names
from it-glossary.md.

## Lessons from the French and Spanish Tier 2 reviews (most common must-fix items)

- Softened hedges ("may" became "will") and hardened ones ("often" became "always"); keep the English strength.
- Added definitions or explanations that carry a claim the English page doesn't make.
- JSON-LD: keep the French skeleton exactly (WebPage / BreadcrumbList / ItemList / FAQPage nesting). Every FAQ `name`
  equals its visible `<summary>` character for character; every schema answer says the same as the visible answer.
- Price tokens are single-brace: `{P_MONTHLY@chessful}`, never `{{P_…}}`. Tokens go inside text the page passes
  through the token include, exactly as the French page does; copy its pattern.
- Type U+00A0 before € (no Spanish writer did); no space before %.
- No gendered audience words («stanco», «bloccato», «sei uno sviluppatore»): use neutral phrasing («chi lavora a turni»).
- No raw keyword seo.titles; no «(2026)» or «guida onesta» padding; seo.keywords only real queries from the research
  file or it-keywords.md.
- Apple App Privacy labels quoted only from it-apple-terms.md («Dati non raccolti», «Dati utilizzati per monitorarti»).
- Card titles that are quotes end without a full stop inside “…”.

## Local-only pages (TRANSLATION.md 6.7)

Both: front matter `local_only: true`, NO `ref`, NO `translated_from`, the permalink below, `last_updated: 2026-11-19`,
full `seo`, `quick_answer`, faq in JSON-LD + visible, `datePublished` 2026-11-19. Short quotes only (under 15 words),
paraphrase the rest. Save every page you fetch for facts into
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-Dg10Mu/74a2811e-d61b-4f13-9e3c-097376f519cd/scratchpad/it-t2/sources/<slug>/`
(one file per source, named by app or Apple page) so the reviewer can check claim by claim.

### `it/guides/limitare-tempo-di-utilizzo-iphone.html`, permalink `/it/guides/limitare-tempo-di-utilizzo-iphone/`

- Structure: model it on `es/guides/limitar-tiempo-de-pantalla-iphone.html` and
  `fr/guides/limiter-temps-ecran-iphone.html` (read both), but every fact must come from an Italian or primary source
  you fetched yourself today:
  - Apple's Screen Time («Tempo di utilizzo») in iOS 27, Italy wording:
    https://support.apple.com/it-it/guide/iphone/iphbfa595995/ios and the rows in it-apple-terms.md (“Orari di ‘Tempo
    di utilizzo’”, “Limiti di tempo”). iOS 27 names first. Do not describe iOS 26 labels (Downtime / App Limits Italian
    names are not verified).
  - Each competitor's own Italian App Store description:
    `curl -s "https://itunes.apple.com/lookup?country=it&lang=it_it&id=<ID>"` (field `description`). IDs: Opal
    1497465230, one sec 1532875441, Jomo 1609960918, Cape 6444819615, Forest 866450515, AppBlock 1515753232, ScreenZen
    1541027222 (English listing: describe it from that listing and say the listing is in English). Brick (6448794069)
    is sold but English-only and a hardware product: leave it out unless the es/fr page keeps it and its listing
    supports the sentence. Describe each app only with what its listing says; no prices unless you can quote the
    Italian listing. Italian ratings from the research file.
  - EarnLock facts from `_apps/earnlock.md`, the Italian page `it/apps/earnlock/index.md`, its glossary section and
    `~/Downloads/githubcode/.agents/product-marketing.md` → EarnLock's APP_BLUEPRINT.md §10 (claims register only).
    EarnLock's prices only through `{P_MONTHLY@earnlock}`, `{P_YEARLY@earnlock}`, `{P_LIFETIME@earnlock}` as the French
    page does. Disclose that EarnLock is ours (Lagerland Apps publishes this guide).
- Scope note as in the es/fr page: these apps limit your own use; the guide does not cover parental controls (Google
  Family Link etc.).
- Keywords: `come limitare il tempo di utilizzo di un app su iphone`, `come ridurre il tempo di utilizzo del telefono
  iphone`, `bloccare app iphone tempo`, `app per smettere di guardare il telefono`, `tempo di utilizzo iphone`.

### `it/guides/come-mettere-conto-alla-rovescia-iphone.html`, permalink `/it/guides/come-mettere-conto-alla-rovescia-iphone/`

- Structure: model `es/guides/como-poner-cuenta-atras-iphone.html` and `fr/guides/application-compte-a-rebours-iphone.html`.
- Facts from: Apple Italy's iOS 27 iPhone guide pages on widgets (home screen and lock screen; start at
  https://support.apple.com/it-it/guide/iphone/iphb8f1bf206/ios and find the lock-screen one from
  https://support.apple.com/it-it/guide/iphone/welcome/ios; save them), each app's Italian description via the lookup
  API (IDs 576177593 Countdown Star, 1403367428 Countdown App, 940109775 Big Days, 917514700 Conto alla rovescia -
  Widget, 1534850579 Countdown Buddy), Soon.'s `_apps/soon.md`, `it/apps/soon/index.md`, its glossary section and its
  APP_BLUEPRINT.md §10 (prices via `{P_…@soon}` tokens; disclose it is ours). Italian ratings from the research file.
  «conto alla rovescia» (also «countdown» once, people type it). If iOS itself has no countdown widget, say what the
  Apple page you fetched shows, only if it says so. Apple Watch support per app only if its listing says so.
- Keywords: `come mettere un conto alla rovescia su iphone`, `come aggiungere un conto alla rovescia su iphone`, `come
  creare un conto alla rovescia su iphone`, `conto alla rovescia widget iphone`, `app per contare quanti giorni mancano`.

## Hubs (`it/guides/index.html`, `it/for/index.html`), one writer, after the others

- Model the French and Spanish hubs. The guides hub lists the guides that exist in Italian (this batch: chess, logic
  puzzles, workout, the two local-only guides) in its card grid and ItemList; English-only guides (shogi, xiangqi, bill
  tracker) appear as the es/fr hub handles English-only entries (check: if the hub shows them with the marker, do the
  same; if it omits them, omit them).
- The for hub lists shift-workers, apple-health-power-users and calm-productivity in Italian, and indie-ios-developers
  as English-only with the marker, exactly as fr/for/index.html and es/for/index.html do.

## Blueprints

Use only §10 (claims register); §8 lists non-claims and §9 hidden items, never sources.

## Do NOT

Run `jekyll build`, `i18n.py map` or the stamp script; touch any file but your own; edit English, French, Spanish,
German or Portuguese files; edit `it/llms.txt` or any app page (the main session wires hubs, llms lines and inbound
links). Other sessions (Spanish, Portuguese) work in this same checkout: never run `git` commands that change state.

## Reply with

The items in it-writer-brief.md «Reply with», plus: every competitor fact you dropped because Italy data was missing,
and (local-only pages) the list of sources saved.

---

## Batch 2 (2026-11-19)

Same rules as batch 1. Research rows: the «Batch 2» section at the bottom of the research file. Fetch App Store product
pages only with `curl -sL` (without `-L` you save an empty 301 stub). Every € typed with U+00A0 before it.

| Page | Write to | Primary query |
|---|---|---|
| guides/best-shogi-apps-iphone.html | it/guides/best-shogi-apps-iphone.html | shogi online |
| guides/best-xiangqi-apps-iphone.html | it/guides/best-xiangqi-apps-iphone.html | xiangqi online |
| guides/bill-tracker-without-bank-connection.html | it/guides/bill-tracker-without-bank-connection.html | migliore app per scadenze pagamenti |

- Shogi: Kakinoki Shogi is not sold in Italy: drop it and every sentence that depends on it (as es did). None of the
  listed apps has an Italian listing; say which languages they offer only where the English page does. Shogiful is ours
  (it/apps/shogiful/index.md and its glossary section: drops are «paracadute», explained once; prices via tokens).
  `shogi` is Shogiful's keyword: not in your seo.title as the bare word.
- Xiangqi: the China-store app 403941510 (Tiantian) is not sold in Italy: keep the English page's point only as «è
  sull’App Store cinese, quindi in Italia non lo trovi», or drop it as es/fr did (check them). Xiangqiful is ours
  (it/apps/xiangqiful/index.md, glossary). `scacchi cinesi` and `xiangqi` are Xiangqiful's keywords: seo.title leads with
  «xiangqi online» or «scacchi cinesi online».
- Bill tracker: Rocket Money, Truebill (now Rocket Money), Monarch and Copilot are not sold in Italy. Rewrite the comparison
  around the bank-linked apps people in Italy use, Wallet by BudgetBakers, Spendee and Toshl Finanze, using ONLY what
  each one's own Italian App Store description says (saved in
  `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-Dg10Mu/74a2811e-d61b-4f13-9e3c-097376f519cd/scratchpad/it-t2/sources/bill-tracker/<name>.json`,
  field `description`; re-fetch if you need more and save it there). Keep the English page's general points about bank
  aggregation only where they do not name a US company or a US rule; drop Plaid, US banks and US law. Structural models:
  `fr/guides/bill-tracker-without-bank-connection.html` (rewritten around Bankin' and Linxo) and
  `es/guides/bill-tracker-without-bank-connection.html` (around Fintonic). AllPaid facts from `_apps/allpaid.md`,
  `it/apps/allpaid/index.md`, its glossary section and its APP_BLUEPRINT.md §10; prices via `{P_…@allpaid}` tokens;
  disclose that AllPaid is ours. Never claim anything about these apps' security, fees, data use or bank coverage that
  their listing doesn't say; no review quotes. «bollette» for utility bills, «scadenze» for due dates, «abbonamenti» for
  subscriptions. AllPaid keeps `app promemoria pagamenti` and `app scadenze bollette`.
