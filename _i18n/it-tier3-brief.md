# Writer brief: Italian (it, Italy) Tier 3, batch 1 (comparison pages)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/it-writer-brief.md` first and follow all of it.** This file adds what is different for Tier 3.
Where the two disagree, this file wins.

## Your inputs

- The English source page `alternatives/<slug>.html`: it holds the facts about OUR app and the comparison.
- The Spanish page `es/alternatives/<slug>.html` and the French page `fr/alternatives/<slug>.html`: structural template
  only (Liquid, JSON-LD skeleton, table and card markup, how links and tokens are written, how they replaced US
  competitor data with their own store's data). Never translate from French or Spanish; write from English.
- `/Users/anttiaittamaa/Downloads/githubcode/it-tier3-research-2026-11-19.md`: your page's row (Italian primary query,
  the Italian suggest phrasings that show demand).
- `/Users/anttiaittamaa/Downloads/githubcode/it-tier3-store-2026-11-19.md`: the competitor in the ITALIAN App Store,
  checked today (Italian store name, Italian ratings, languages, IAP rows in euro, full Italian description).
- `_i18n/it.md` (sheet), `_i18n/it-apple-terms.md`, `_i18n/it-glossary.md` (your app's section), `_i18n/it-keywords.md`
  (your app's section), and the Italian app page `it/apps/<app>/index.md` (its wording, tier names and feature names
  are already reviewed: reuse them).

## Pages in this batch

| English source | Write to | Our app | Primary query |
|---|---|---|---|
| alternatives/tricount.html | it/alternatives/tricount.html | RightSplit | alternativa a tricount (twin: tricount come funziona) |
| alternatives/splitwise.html | it/alternatives/splitwise.html | RightSplit | alternativa a splitwise |
| alternatives/chess-com.html | it/alternatives/chess-com.html | Chessful | alternativa a chess com |
| alternatives/lichess.html | it/alternatives/lichess.html | Chessful | meglio lichess o chess com |
| alternatives/whoop.html | it/alternatives/whoop.html | Observa | alternativa a whoop senza abbonamento |
| alternatives/oura.html | it/alternatives/oura.html | Observa | oura ring senza abbonamento |
| alternatives/hevy.html | it/alternatives/hevy.html | LiftLog | hevy app come funziona |
| alternatives/forest.html | it/alternatives/forest.html | EarnLock | forest app come funziona |
| alternatives/pdf-expert.html | it/alternatives/pdf-expert.html | MediaKit | pdf expert gratis |
| (local-only, no English twin) | it/alternatives/alternativa-a-wallet-budgetbakers.html | AllPaid | wallet budgetbakers recensioni |

The hub `it/alternatives/index.html` is written by the main session after your pages.

Keyword collisions: `app per dividere il conto` and `dividere il conto alla romana` belong to RightSplit's app page,
`app scacchi` to Chessful, `hrv apple watch` and `app sonno apple watch` to Observa, `app diario allenamento palestra`
and `app palestra senza abbonamento` to LiftLog, `bloccare app iphone` to EarnLock, `comprimere pdf iphone` to MediaKit,
`app promemoria pagamenti` and `app scadenze bollette` to AllPaid, `migliore app per scadenze pagamenti` to the bill
tracker guide, `migliore app scacchi iphone` to the chess guide. Not in your seo.title or as your primary; fine in body
text or as a secondary keyword. The two RightSplit pages and the two Chessful pages must not share a primary or a
seo.title pattern: tricount owns `alternativa a tricount` / `tricount come funziona`, splitwise owns `alternativa a
splitwise` (`meglio splitwise o tricount` may be a secondary on both); chess-com owns `alternativa a chess com`, lichess
owns `meglio lichess o chess com`. Whoop owns `alternativa a whoop`, Oura owns `oura ring senza abbonamento` (`meglio oura
o whoop` may be a secondary on both).

## Competitor facts (TRANSLATION.md 6.4)

- Every fact about the competitor is per market. Use ONLY the Italian store file (and what the English page says that
  is not market-specific, such as how the product works). A US price, a US rating or a US-only feature on an Italian
  page is wrong.
- Prices: only the euro amounts in the store file's IAP rows (or a web price the store file quotes with its URL), typed
  as `3,99 €` with U+00A0, with «(App Store in Italia, 19 novembre 2026)» once per page (or «sito ufficiale, 19 novembre
  2026» for a web price). When several rows exist for one plan, give the range as the Spanish Forest page does («da
  25,00 € a 27,95 € all’anno»). If the store file has no row for a plan the English page prices, keep the qualitative
  fact («abbonamento mensile o annuale», «a pagamento») and drop the number. Never convert dollars. Never arithmetic on
  OUR prices; arithmetic on a competitor's euro price only where the English page does the same calculation.
- Ratings: only the Italian count and average from the store file, as «Su App Store in Italia ha 4,8 su 5 con 13.704
  valutazioni (dato del 19 novembre 2026)», or leave ratings out.
- Competitor names as in English (Tricount, Splitwise, Chess.com, Lichess, WHOOP/Whoop as the English page writes it,
  Oura, Hevy, Forest, PDF Expert, Wallet by BudgetBakers). The Italian store title once where it helps people find the
  app. Competitor App Store links: `https://apps.apple.com/it/app/id<ID>`.
- Where the competitor's listing is not in Italian (store file: IT no), you may say so once if the English page talks
  about languages; never invent the app's interface languages.
- Feature claims about competitors: only what the English page says, cross-checked against the Italian description; if
  the Italian description contradicts the English page (a feature gone, now free, now paid), follow the Italian store
  file and report the English-side error in your reply.

## Our apps' rules on these pages

- Prices only through tokens (`{P_MONTHLY@observa}` etc. on these pages, exactly as the es/fr page writes them).
- «Senza abbonamento» only for LiftLog (house rule). Observa, RightSplit, Chessful, EarnLock, MediaKit and AllPaid
  sell subscriptions: for them write «nessun abbonamento obbligatorio» or «opzione a vita» only where the English page
  and the catalog support it. The Whoop and Oura pages answer «senza abbonamento» queries by stating the facts (Whoop
  and Oura need a membership as the English page says; Observa has a free version and a one-time lifetime option,
  through tokens), never by calling Observa «senza abbonamento».
- Observa: «HRV (SDNN)», never RMSSD as Observa's HRV, never «VFC»; Prontezza capitalised; tier Premium; l’app Salute.
  Medical caveats on the Whoop and Oura pages stay exactly as strong as in English.
- RightSplit tier Pro+ («Spazi» or whatever it/apps/rightsplit/index.md and the glossary call Spaces). Chessful tier Pro.
  LiftLog tiers Equo / Buono / Generoso / Mecenate. EarnLock tier Premium. MediaKit tier Pro. AllPaid tier Pro.
- Disclose that the app is ours where the English page does (Lagerland Apps publishes the comparison).

## Links

- Internal links with `{% include l.html url="..." %}` exactly as the es/fr pages write them; never hard-code `/it/` in
  body links (l.html picks the Italian page when it exists). The local-only page and the hub are linked as plain
  `/it/alternatives/<slug>/`.
- Where the English page links another comparison of this batch, keep the link (l.html resolves it to Italian).
- The hub link in the breadcrumb is `{{ site.url }}/it/alternatives/` with the name «Confronti».
- `"inLanguage": "it"` wherever the es page has `"es-ES"` (Italian pages write `"it"`).

## Local-only page: `it/alternatives/alternativa-a-wallet-budgetbakers.html`

- Front matter: `layout: default`, `local_only: true`, NO `ref`, NO `translated_from`, `permalink:
  /it/alternatives/alternativa-a-wallet-budgetbakers/`, `title`, `quick_answer`, full `seo`, `last_updated:
  2026-11-19`; FAQ visible + in JSON-LD; `datePublished` 2026-11-19 where the model has one.
- Structure: model `es/alternatives/alternativa-a-fintonic.html` and `fr/alternatives/alternative-bankin.html` (read
  both). Facts about Wallet by BudgetBakers ONLY from its Italian store description and IAP rows in the store file
  (short quotes under 15 words, paraphrase the rest). Never claim anything about its security, fees, data use or bank
  coverage that the listing doesn't say; no review quotes. The page answers the «wallet budgetbakers recensioni / è
  sicuro / costo / opinioni» intent honestly: what Wallet does (budget, bank sync per its listing), what AllPaid does
  instead (manual bills and due-date reminders, no bank connection), and when Wallet is the better choice.
- AllPaid facts from `_apps/allpaid.md`, `it/apps/allpaid/index.md`, its glossary section, and AllPaid's
  APP_BLUEPRINT.md §10 (claims register only; path in `~/Downloads/githubcode/.agents/product-marketing.md`). Prices via
  `{P_…@allpaid}` tokens as the es page writes them. Link the Italian bill tracker guide
  (`{% include l.html url="/guides/bill-tracker-without-bank-connection/" %}`) once.
- Keywords: `wallet budgetbakers recensioni`, `wallet budgetbakers è sicuro`, `wallet budgetbakers costo`, `wallet by
  budgetbakers opinioni`, `spendee o wallet`, `app scadenze senza collegare la banca` only if a source supports it
  (else leave it out).
- Save any extra page you fetch into
  `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-uxS8e6/ac98050c-36df-44ef-84c7-3da2924e56aa/scratchpad/it-t3/sources/wallet/`.

## Lessons from the French, Spanish and Italian Tier 2 reviews (most common must-fix items)

- Softened or hardened hedges; added definitions that carry a claim; framing sentences added to FAQ answers.
- JSON-LD: keep the es/fr skeleton exactly (WebPage / BreadcrumbList / FAQPage nesting; never paste an ItemList into the
  breadcrumb). Every FAQ `name` equals its visible `<summary>` character for character; the schema answer says the same
  as the visible answer.
- Price tokens single-brace. U+00A0 before every €; no space before %.
- No gendered audience words; no raw-keyword seo.titles; no «(2026)» padding; no meta description opening with a
  question; seo.keywords only real queries from the research file or it-keywords.md.
- Apple App Privacy labels quoted only from it-apple-terms.md.
- The sheet's «Tells to cut» list, all of it (Tier 1 and Tier 2 findings).

## Do NOT

Run `jekyll build`, `i18n.py map` or the stamp script; touch any file but your own; edit English, French, Spanish,
German or Portuguese files; edit `it/llms.txt`, the hub or any app page (the main session wires hubs, llms lines and
inbound links). Other sessions (Dutch, Spanish, Portuguese) work in this same checkout: never run `git` commands that
change state. Do not fetch apps.apple.com yourself (the store file has the data; it 429s under load); the iTunes lookup
API is fine if you need one more field.

## Reply with

The items in it-writer-brief.md «Reply with», plus every competitor fact you dropped because Italian data was missing,
and every place where the Italian store contradicted the English page.
