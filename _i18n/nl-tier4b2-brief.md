# Writer brief: Dutch (nl, Netherlands) Tier 4, batch 2 (journal posts)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/nl-tier4-brief.md` first (everything above its «Per-post notes» heading) and follow it**, and through it
`_i18n/nl-writer-brief.md`. This file replaces only the parts listed here. Batch 1 is live; read one reviewed batch 1 post
(for example `nl/journal/how-long-to-rest-between-sets/index.md`) to see the finished Dutch house style, and read the sheet's
«From the Tier 4 reviews» paragraph in `_i18n/nl.md`: those are the must-fix items the batch 1 reviewers found.

## What changes for batch 2

- **Research file:** `/Users/anttiaittamaa/Downloads/githubcode/nl-tier4-research-2026-11-19.md`, section «Batch 2» and its raw
  list (keywords only from there, from the batch 1 raw list, `_i18n/nl.md` or `_i18n/nl-keywords.md`).
- **Sources folder:** save every fetched page into
  `/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/b562e572-a501-462e-86d4-d96e70f0914a/scratchpad/nl-t4b2/sources/<slug>/`
  (one text file per source, URL on the first line). Fetch with `curl -sL`, strip HTML with `python3 -I`. A page you could not
  fetch is not a source. Short quotes only (under 15 words); no near-verbatim paraphrase of Apple or government sentences.
- **Templates:** the translated posts use the German twin `de/journal/<slug>/index.md` (and the pt/es/fr/it twin where one exists)
  as the structural template only. Never translate from them; write from English.
- **Dutch pages you may link** (check with `ls nl/guides nl/for`): `/nl/apps/<slug>/`, `/nl/guides/<slug>/`, `/nl/for/<slug>/`, the
  ten batch 1 posts (`ls nl/journal`) and the ten batch 2 posts:
  `/nl/journal/rpe-and-rir-explained/`, `/nl/journal/find-every-recurring-charge/`, `/nl/journal/compress-a-video-for-email/`,
  `/nl/journal/rotating-shift-schedules-explained/`, `/nl/journal/hoeveel-diepe-slaap/`, `/nl/journal/hartslag-in-rust/`,
  `/nl/journal/slaaptekort-inhalen/`, `/nl/journal/progressive-overload/`, `/nl/journal/sets-per-spiergroep-per-week/`,
  `/nl/journal/feestdagen-2027/`.
  **Comparison pages: always the English URL** (`/alternatives/<slug>/` with `{: hreflang="en"}` and « (in het Engels)»), even if
  `nl/alternatives/` exists in the checkout: those Dutch pages are not published yet.
- **Keyword collisions, added to the batch 1 list:** the batch 1 primaries are taken (`hoeveel stappen per dag`, `rust tussen sets`,
  `push pull legs schema`, `deload week`, `1rm berekenen`, `hrv waarde`, `lage hrv`, `vaccinaties puppy`, `kitten vaccinaties`,
  `fooi amerika`, `spelletjes zonder reclame`, `mkv naar mp4`); AfterShift keeps `slapen na nachtdienst`, `slaapschuld`,
  `ploegendienst slaap`, `ploegendienst app`; the Dutch comparisons keep `dyme app alternatief`, `hevy app gratis`.
- **Local-only posts** (rows marked local-only below): front matter `layout: journal`, `slug: <dutch slug>`,
  `permalink: /nl/journal/<dutch slug>/`, `local_only: true`, NO `ref`, NO `translated_from`, `date` and `last_updated`
  2026-11-19, `mentioned_apps` as given, everything else as in a translated post (seo, lede, quick_answer, excerpt, faq, read_time).
  Every fact comes from a source you fetched and saved today, or from the app's facts (`_apps/<slug>.md`, the Dutch app page,
  the glossary, APP_BLUEPRINT.md §10). Read the French, German, Spanish or Italian model for structure and to see which facts
  were sourced where; never copy their wording or their sources' numbers without re-fetching the source yourself. Health posts
  keep the «geen medisch advies» line the models carry. Where a model cites a national authority of its own country (HAS,
  Ameli, DGE, Robert Koch), use the Dutch equivalent you can fetch (Thuisarts.nl, Hartstichting, Gezondheidsraad, RIVM,
  Voedingscentrum, Rijksoverheid, Hersenstichting) or the international study the model cites, or leave the claim out.
- Reply with the same five points as in batch 1.

## Per-post notes

| Post | Write to | Primary query | Notes |
|---|---|---|---|
| rpe-and-rir-explained | nl/journal/rpe-and-rir-explained/index.md | rpe schaal | Secondaries: «rpe schaal krachttraining», «rpe schaal 1-10», «rir betekenis», «rir betekenis fitness», «rpe training». The Borg 6–20 scale only as far as the English post mentions it. GymLogger X labels from the glossary / Dutch app page (it logs no RPE per set: keep the English wording on that). Template de/ (also es, fr, it, pt) |
| find-every-recurring-charge | nl/journal/find-every-recurring-charge/index.md | abonnementen bekijken iphone | «abonnementen bekijken», «abonnementen bekijken apple», «google abonnementen bekijken», «abonnementen iphone bekijken», «terugkerende betalingen paypal» (only if the post says how). Apple steps exactly as Apple NL writes them (`_i18n/nl-apple-terms.md`; fetch support.apple.com/nl-nl/118428): Instellingen > [je naam] > ‘Abonnementen’. Rocket Money is not sold in NL: where English describes it, use Dyme, Wallet (BudgetBakers) and Spendee with only the facts `nl/guides/bill-tracker-without-bank-connection.html` states (read it; never a price it doesn't show). US bank names and US law: cut, or replace only from a fetched Dutch source. Template pt/ (it did the same replacement for Portugal) |
| compress-a-video-for-email | nl/journal/compress-a-video-for-email/index.md | video verkleinen voor mail | «video verkleinen voor mail gratis», «video verkleinen voor mail iphone», «grote video versturen via mail», «grote video versturen iphone», «te grote video versturen». Provider attachment limits (Gmail, Outlook, iCloud Mail Drop) exactly as the English states them, or from the provider's nl help page you fetched; KPN, Ziggo or other Dutch mail providers only from their own fetched page. Bitrate math recomputed in Dutch number format. Never `video verkleinen iphone` as a keyword (MediaKit's). Template de/, pt/ |
| rotating-shift-schedules-explained | nl/journal/rotating-shift-schedules-explained/index.md | ploegendienst rooster | «5 ploegendienst rooster», «volcontinu rooster», «3 ploegendienst rooster», «4 ploegendienst rooster», «ploegendienst rooster maken». Keep DuPont, Pitman, 4-on-4-off and Continental with their English names, explained once; Dutch terms («volcontinu», «5-ploegendienst», «2-2-3») only where a fetched Dutch source (Rijksoverheid, a cao or arbo source, Arboportaal) defines them, and never claim a Dutch employer uses a named scheme. Dutch working-time rules (Arbeidstijdenwet: rest after night shifts, max night shifts) only from a fetched rijksoverheid.nl or arboportaal.nl page; US OSHA or NIOSH lines keep their English source. AfterShift labels from glossary. Template de/ |
| (local-only) hoeveel-diepe-slaap | nl/journal/hoeveel-diepe-slaap/index.md | hoeveel diepe slaap heb je nodig | `mentioned_apps: [observa, aftershift]` (check the model's list and keep only apps the post discusses). «hoeveel diepe slaap per nacht», «hoeveel diepe slaap is normaal», «hoeveel diepe slaap heb je nodig per leeftijd», «diepe slaap verbeteren». Models fr/journal/sommeil-profond-combien-d-heures, es/journal/cuantas-horas-de-sueno-profundo, de/journal/tiefschlaf-wie-viel. Apple's sleep-stage names exactly as Apple NL (Wakker, Remslaap, Kernslaap, Diepe slaap; fetch the Apple nl-nl sleep-stages page). Observa's own labels from the glossary. Percentages of deep sleep per age only from a study or Dutch source you fetched |
| (local-only) hartslag-in-rust | nl/journal/hartslag-in-rust/index.md | hartslag in rust | `mentioned_apps: [observa]`. «hartslag in rust vrouw», «hartslag in rust man», «hartslag in rust 50», «rusthartslag», «rusthartslag te hoog» (only as answered). Models fr/journal/frequence-cardiaque-au-repos, es/journal/frecuencia-cardiaca-en-reposo, de/journal/ruhepuls-normalwerte. Normal ranges and when to see a doctor ONLY from fetched pages (Hartstichting, Thuisarts, the studies the models cite). Apple NL term «hartslag in rust». YMYL: not medical advice |
| (local-only) slaaptekort-inhalen | nl/journal/slaaptekort-inhalen/index.md | slaaptekort inhalen | `mentioned_apps: [aftershift, observa]` (as the post discusses them). «kan je slaaptekort inhalen», «hoe snel slaaptekort inhalen», «chronisch slaaptekort inhalen», «langdurig slaaptekort inhalen». Never `slaapschuld` as primary or in seo.title (AfterShift's); in body text «slaapschuld» is fine. Models fr/journal/rattraper-dette-de-sommeil, de/journal/schlafschuld-abbauen. Studies only as fetched |
| (local-only) progressive-overload | nl/journal/progressive-overload/index.md | progressive overload | `mentioned_apps: [liftlog, gymlogger-x]` (as the post discusses them). «progressive overload betekenis», «progressive overload nederlands», «progressive overload uitleg», «progressieve overbelasting», «progressive overload schema». Models de/journal/progressive-overload, fr/journal/surcharge-progressive-musculation, es/journal/sobrecarga-progresiva. Link the Dutch batch 1 posts on rest, deload, 1RM and the strength program where they fit; double progression stays an English link |
| (local-only) sets-per-spiergroep-per-week | nl/journal/sets-per-spiergroep-per-week/index.md | hoeveel sets per spiergroep per week | `mentioned_apps: [liftlog, gymlogger-x]` (as discussed). «sets per spiergroep per week», «hoeveel sets per week voor spiergroei», «hoeveel sets per spiergroep voor spiergroei», «hoeveel sets per spiergroep per training». Model fr/journal/series-par-muscle-par-semaine. Studies (Schoenfeld, Pelland and so on) only as fetched; GymLogger X ‘Setvolume’ label from glossary |
| (local-only) feestdagen-2027 | nl/journal/feestdagen-2027/index.md | feestdagen 2027 | `mentioned_apps: [soon]`. «feestdagen 2027 nederland», «feestdagen 2027 kalender», «feestdagen 2027 met weeknummers» (only if you compute ISO weeks and say so). Models fr/journal/jours-feries-2027, it/journal/festivita-2027. Every date from a fetched rijksoverheid.nl page (officiële feestdagen; Bevrijdingsdag every 5 years as a day off only per the source; Koningsdag date rule). Weekdays computed and double-checked with `python3 -c`. Schoolvakanties 2027 only if a fetched rijksoverheid.nl page lists them, and then as a short table with the regions. Soon. features from its Dutch page and glossary (countdown, widgets); no dated promises |
