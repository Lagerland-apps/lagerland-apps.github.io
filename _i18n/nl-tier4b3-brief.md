# Writer brief: Dutch (nl, Netherlands) Tier 4, batch 3 (journal posts)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/nl-tier4b2-brief.md` and follow it** (it points you to `_i18n/nl-tier4-brief.md` above its «Per-post notes»
heading and to `_i18n/nl-writer-brief.md`). This file replaces only what it lists. Read one reviewed batch 2 local-only post
(for example `nl/journal/hartslag-in-rust/index.md`) for the finished Dutch house style, and the sheet `_i18n/nl.md` paragraphs
«From the Tier 4 reviews» and «From the Tier 4 batch 2 reviews»: they are the reviewers' must-fix list (no «ik», no meta sentences
about what sources do not say, no title that promises what the body says doesn't exist, no invented reassurance, no near-verbatim
copies of Apple or government sentences, no contrast reveals).

## What changes for batch 3

- **Research file:** `/Users/anttiaittamaa/Downloads/githubcode/nl-tier4-research-2026-11-19.md`, section «Batch 3» and all raw
  lists (keywords only from there, `_i18n/nl.md` or `_i18n/nl-keywords.md`).
- **Sources folder:** `/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/b562e572-a501-462e-86d4-d96e70f0914a/scratchpad/nl-t4b3/sources/<slug>/`.
  Save the page TEXT (not condensed notes), URL on line 1. `curl -sL` + `python3 -I` to strip HTML; if a site blocks curl, use
  WebFetch and say so in the file; PubMed blocks curl, use Europe PMC or NCBI E-utilities. A page you could not fetch is not a source.
- **Dutch pages you may link:** everything in `ls nl/journal nl/guides nl/for nl/alternatives` plus the ten batch 3 posts:
  `/nl/journal/how-to-sleep-after-a-night-shift/`, `/nl/journal/ontwormen-hond/`, `/nl/journal/vlooien-hond/`, `/nl/journal/vo2max/`,
  `/nl/journal/remslaap/`, `/nl/journal/warming-up-krachttraining/`, `/nl/journal/foto-verkleinen-iphone/`,
  `/nl/journal/pdf-verkleinen-mac/`, `/nl/journal/hoeveel-dagen-tot-kerst/`, `/nl/journal/geluid-uit-video-halen-iphone/`.
  Dutch comparison pages now exist (`ls nl/alternatives`): link the Dutch one when it exists, otherwise the English URL with
  `{: hreflang="en"}` and « (in het Engels)».
- **Keyword collisions, added to the batch 1 and 2 lists:** the batch 2 primaries (`rpe schaal`, `abonnementen bekijken iphone`,
  `video verkleinen voor mail`, `ploegendienst rooster`, `hoeveel diepe slaap heb je nodig`, `hartslag in rust`, `slaaptekort
  inhalen`, `progressive overload`, `hoeveel sets per spiergroep per week`, `feestdagen 2027`); AfterShift keeps `slapen na
  nachtdienst`; Pawza keeps `vaccinatieboekje hond`, `vaccinaties kat`, `dierenpaspoort`; MediaKit keeps `pdf comprimeren`, `pdf
  verkleinen`, `video verkleinen iphone`, `heic naar jpg`; Soon. keeps `aftel app`, `countdown widget iphone`; the countdown guide keeps
  `aftellen op iphone`.
- **Local-only front matter and fact rules:** as in the batch 2 brief. Every fact from a saved source or the app's facts
  (`_apps/<slug>.md`, the Dutch app page, `_i18n/nl-glossary.md`, APP_BLUEPRINT.md §10; UI strings checked in the app's `nl`
  catalog, read-only, when in doubt). Models are for structure; never copy their wording or numbers without re-fetching the source.
  Health and pet posts keep one plain «geen medisch advies» / «geen diergeneeskundig advies» line. No product names or prices for
  medicines, flea or worm treatments.
- **Links to local-only posts:** plain `/nl/journal/<slug>/` (never through `l.html`).
- Reply with the same five points as in batch 1.

## Per-post notes

| Post | Write to | Primary query | Notes |
|---|---|---|---|
| how-to-sleep-after-a-night-shift (translation) | nl/journal/how-to-sleep-after-a-night-shift/index.md | nachtdienst slapen | Secondaries: «nachtdienst hoe slapen», «nachtdienst wanneer slapen», «nachtdienst tips slapen», «overdag slapen nachtdienst», «slecht slapen nachtdienst». Never `slapen na nachtdienst` as primary or in seo.title (AfterShift's). Template de/journal/how-to-sleep-after-a-night-shift and fr twin. US-only items (US agencies, US drowsy-driving figures) keep their English source with the marker or are cut; a Dutch line (Thuisarts on night work, Arboportaal on rest after night shifts) only from a fetched page. AfterShift labels from the glossary and the Dutch page |
| (local-only) ontwormen-hond | nl/journal/ontwormen-hond/index.md | ontwormen hond | `mentioned_apps: [pawza]`. «ontwormen hond hoe vaak», «ontwormen hond schema», «ontwormen hond puppy», «ontwormen hond dierenarts»; «wormen kat» only if the post covers cats from a source. Models fr/journal/vermifuger-son-chien, de/journal/wurmkur-hund-wie-oft, es/journal/desparasitar-perro, pt/journal/desparasitar-gato-e-cao. Dutch sources: ESCCAP (esccap.org, a Benelux or Dutch page if one exists), LICG (licg.nl), KNMvD, Thuisarts for any human-health line. Frequencies and risk groups exactly as the source states; never a brand or price |
| (local-only) vlooien-hond | nl/journal/vlooien-hond/index.md | vlooien hond | `mentioned_apps: [pawza]`. «vlooien hond herkennen», «vlooien hond bestrijden», «vlooien hond op mensen», «vlooien hond en kat», «teken hond», «teken hond verwijderen». Models fr/journal/puces-tiques-chien, es/journal/pulgas-y-garrapatas-perro, it/journal/pulci-e-zecche-cane. Sources LICG, ESCCAP, RIVM (tekenbeten, ziekte van Lyme) or Thuisarts for people. Never a brand or price |
| (local-only) vo2max | nl/journal/vo2max/index.md | vo2max waarde | `mentioned_apps: [observa]`. «vo2max tabel», «vo2max waarden vrouwen», «vo2 max waarde mannen», «vo2max verbeteren», «vo2max apple watch». Apple NL calls it «cardioconditie» (VO2 max); fetch Apple's nl-nl cardio fitness page. Models de/journal/vo2max-apple-watch, fr/es/it/pt vo2-max. Any reference table only as a fetched source gives it, with its source named |
| (local-only) remslaap | nl/journal/remslaap/index.md | hoeveel remslaap heb je nodig | `mentioned_apps: [observa]`. «hoeveel remslaap per nacht», «hoeveel remslaap is normaal», «remslaap wat is dat». Apple NL stage names ‘Remslaap’, ‘Kernslaap’, ‘Diepe slaap’, ‘Wakker’. Models fr/journal/sommeil-paradoxal, es/journal/sueno-rem, it/journal/sonno-rem, pt/journal/sono-rem. Link /nl/journal/hoeveel-diepe-slaap/ (plain href). Never a sleep-disorder diagnosis claim |
| (local-only) warming-up-krachttraining | nl/journal/warming-up-krachttraining/index.md | warming up krachttraining | `mentioned_apps: [liftlog, gymlogger-x]` (as discussed). «warming up oefeningen krachttraining», «korte warming up krachttraining», «warming up krachttraining benen», «beste warming up voor krachttraining». Models fr/journal/echauffement-musculation, it/journal/riscaldamento-palestra, pt/journal/aquecimento-antes-do-treino. Warm-up set facts of the apps from the Dutch app pages (‘Warming-upsets’, the GymLogger X warm-up marking) |
| (local-only) foto-verkleinen-iphone | nl/journal/foto-verkleinen-iphone/index.md | foto verkleinen iphone | `mentioned_apps: [mediakit]`. «foto verkleinen iphone gratis», «foto verkleinen iphone mb», «foto kleiner maken iphone», «bestandsgrootte foto verkleinen iphone». Models fr/journal/reduire-taille-photo-iphone, it/journal/ridurre-dimensioni-foto-iphone. iOS's own options (Foto’s, Mail’s size choice, camera format HEIC/‘Meest compatibel’) exactly as Apple NL support pages say them. MediaKit tool names from the catalog |
| (local-only) pdf-verkleinen-mac | nl/journal/pdf-verkleinen-mac/index.md | pdf verkleinen mac | `mentioned_apps: [mediakit]`. «pdf kleiner maken mac», «pdf verkleinen macbook», «pdf verkleinen mac gratis», «pdf verkleinen voor mail». Never `pdf verkleinen` or `pdf comprimeren` alone as keyword. Models fr/journal/compresser-pdf-mac, es/journal/comprimir-pdf-mac, pt/journal/reduzir-tamanho-pdf-mac. Voorvertoning's Quartz filter exactly as Apple NL support writes it. Online services: «you upload the file», nothing more |
| (local-only) hoeveel-dagen-tot-kerst | nl/journal/hoeveel-dagen-tot-kerst/index.md | hoeveel dagen tot kerst | `mentioned_apps: [soon]`. «hoeveel dagen tot kerst 2026», «hoeveel dagen tot kerstavond», «hoeveel dagen tot kerstvakantie», «aftellen naar kerst». Models de/journal/countdown-bis-weihnachten, fr/journal/compte-a-rebours-noel, es/journal/cuantos-dias-faltan-para-navidad, it/journal/conto-alla-rovescia-natale. NEVER a typed «nog N dagen» that goes stale: give the weekdays of 24, 25 and 26 December 2026 and 2027 (computed in Python), the counting rule (whether today counts) and the kerstvakantie 2026 dates per region only from the saved rijksoverheid.nl overview. How to count down with Soon. (widgets, toegangsscherm, ‘Stand-by’) from its Dutch page and glossary |
| (local-only) geluid-uit-video-halen-iphone | nl/journal/geluid-uit-video-halen-iphone/index.md | geluid uit video halen iphone | `mentioned_apps: [mediakit]`. «geluid uit video halen», «geluid uit video halen gratis», «geluid uit video halen online» (answered honestly: upload). Models fr/journal/extraire-son-video-iphone, it/journal/estrarre-audio-da-video-iphone. iOS options (Opdrachten, iMovie) only as Apple NL pages describe them. MediaKit's audio tool names from the catalog |
