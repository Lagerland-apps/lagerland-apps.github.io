# Writer brief: Dutch (nl, Netherlands) Tier 4, batch 4 (journal posts)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/nl-tier4b3-brief.md` (everything above its «Per-post notes») and, through it, `_i18n/nl-tier4b2-brief.md`, and follow them** (it points you to `_i18n/nl-tier4-brief.md` above its «Per-post notes»
heading and to `_i18n/nl-writer-brief.md`). This file replaces only what it lists. Read one reviewed batch 3 local-only post
(for example `nl/journal/vlooien-hond/index.md`) for the finished Dutch house style, and the sheet `_i18n/nl.md` paragraphs
«From the Tier 4 reviews», «From the Tier 4 batch 2 reviews» and «From the Tier 4 batch 3 reviews»: they are the reviewers' must-fix list (no «ik» on local-only pages, no meta sentences
about what sources do not say, no title that promises what the body says doesn't exist, no invented reassurance, no near-verbatim
copies of Apple or government sentences, no contrast reveals).

## What changes for batch 4

- **Research file:** `/Users/anttiaittamaa/Downloads/githubcode/nl-tier4-research-2026-11-19.md`, section «Batch 4» and all raw
  lists (keywords only from there, `_i18n/nl.md` or `_i18n/nl-keywords.md`).
- **Sources folder:** `/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/b562e572-a501-462e-86d4-d96e70f0914a/scratchpad/nl-t4b4/sources/<slug>/`.
  Save the page TEXT (not condensed notes), URL on line 1. `curl -sL` + `python3 -I` to strip HTML; if a site blocks curl, use
  WebFetch and say so in the file; PubMed blocks curl, use Europe PMC or NCBI E-utilities. A page you could not fetch is not a source.
- **Dutch pages you may link:** everything in `ls nl/journal nl/guides nl/for nl/alternatives` plus the ten batch 4 posts:
  `/nl/journal/how-to-organize-bills-each-month/`, `/nl/journal/telefoonverslaving/`, `/nl/journal/hrv-verbeteren/`, `/nl/journal/powernap/`,
  `/nl/journal/slaapcyclus/`, `/nl/journal/fooi-nederland/`, `/nl/journal/spierpijn-na-training/`, `/nl/journal/rar-bestand-openen-mac/`,
  `/nl/journal/to-do-lijst-maken/`, `/nl/journal/ontwormen-kat/`.
  Link a Dutch comparison page only if `git cat-file -e main:nl/alternatives/<slug>.html` succeeds; otherwise the English URL with
  `{: hreflang="en"}` and « (in het Engels)».
- **Keyword collisions:** every primary of batches 1 to 3 (see the research file and `_i18n/nl.md` «Tier 4 batch … primaries»); Observa keeps
  `hrv apple watch`, the HRV post keeps `hrv waarde`, `lage hrv`; the night-shift post keeps `nachtdienst slapen`; AllPaid keeps `vaste
  lasten app`, `rekeningen bijhouden app`; the bill guide keeps `vaste lasten bijhouden app`, `huishoudboekje app zonder bankrekening`;
  the screen-time guide keeps `schermtijd beperken iphone`, `app om minder op je telefoon te zitten`; EarnLock keeps `apps blokkeren
  iphone`; Taskful Day keeps `to do lijst app`, `to do lijst iphone`, `dagplanner app`, `takenlijst app`; RightSplit keeps `rekening
  splitsen app`, the US tipping post keeps `fooi amerika`; MediaKit keeps `heic naar jpg`, `pdf verkleinen`; Pawza keeps `vaccinaties kat`.
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
| how-to-organize-bills-each-month (translation) | nl/journal/how-to-organize-bills-each-month/index.md | vaste lasten overzicht maken | Secondaries: «vaste lasten overzicht», «vaste lasten overzicht voorbeeld», «vaste lasten overzicht excel» (only if the post covers a spreadsheet), «vaste lasten overzicht app». Template de/journal/how-to-organize-bills-each-month (and other twins if they exist). US-only items (US bill types, US banks, US autopay terms) replaced with Dutch equivalents only from fetched Dutch pages (a bank's own help page, Nibud for budgeting guidance) or cut; Dutch words: vaste lasten, automatische incasso, periodieke overboeking. AllPaid labels from the glossary and the Dutch page |
| (local-only) telefoonverslaving | nl/journal/telefoonverslaving/index.md | telefoonverslaving | `mentioned_apps: [earnlock]`. «telefoonverslaving stoppen», «telefoonverslaving aanpakken», «telefoonverslaving symptomen», «minder op je telefoon zitten». Sources: Trimbos-instituut, Thuisarts, Jellinek, a Dutch government page, or peer-reviewed studies, only as fetched. Never call it a diagnosis or a disorder unless a source does and say who. iOS ‘Schermtijd’ steps exactly as Apple NL; link the local-only guide with a plain `/nl/guides/schermtijd-beperken-iphone/` href. EarnLock facts from the Dutch page and glossary |
| (local-only) hrv-verbeteren | nl/journal/hrv-verbeteren/index.md | hrv verbeteren | `mentioned_apps: [observa]`. «lage hrv verbeteren», «hrv score verbeteren», «hrv verbeteren hoe». Link /nl/journal/apple-watch-hrv-without-a-baseline/. HRV is SDNN on the Apple Watch. Only levers a fetched source names (sleep, alcohol, training load, illness and so on), with the source's strength; no supplements or devices |
| (local-only) powernap | nl/journal/powernap/index.md | powernap hoe lang | `mentioned_apps: [aftershift]`. «powernap duur», «powernap gezond», «dutje doen hoe lang», «dutje doen overdag». Sources: Sleep Foundation, Hersenstichting, Thuisarts, NIOSH (via WebFetch if blocked), studies as fetched. Link /nl/journal/how-to-sleep-after-a-night-shift/ via plain href. AfterShift's ‘Dutje loggen’ and nap timer from the glossary |
| (local-only) slaapcyclus | nl/journal/slaapcyclus/index.md | slaapcyclus volwassenen | `mentioned_apps: [observa]`. «slaapcyclus», «slaapcyclus berekenen» (answer honestly: cycle length varies; a calculator gives an estimate). Baby queries out of scope. Sources as fetched (Hersenstichting, Sleep Foundation, Apple's sleep-stage page). Link /nl/journal/remslaap/ and /nl/journal/hoeveel-diepe-slaap/ |
| (local-only) fooi-nederland | nl/journal/fooi-nederland/index.md | fooi nederland | `mentioned_apps: [rightsplit]`. «hoeveel fooi nederland», «fooi nederland restaurant», «fooi nederland belasting», «gemiddelde fooi nederland». Model pt/journal/gorjeta-em-portugal (structure only). The tax side (fooien en loonheffing) only as a fetched Belastingdienst page says it; amounts or customs only from a fetched survey or trade body (KHN), with its year and source named; if none can be fetched, say what the sources give and nothing more. Link /nl/journal/how-much-to-tip-in-the-us/. RightSplit tip presets from the Dutch page |
| (local-only) spierpijn-na-training | nl/journal/spierpijn-na-training/index.md | spierpijn na training | `mentioned_apps: [liftlog]` (and gymlogger-x if discussed). «is spierpijn na training goed», «geen spierpijn na training», «spierpijn na elke training». Sources: Thuisarts, studies on DOMS as fetched (Europe PMC). Never treatment advice beyond the sources; one «geen medisch advies» line |
| (local-only) rar-bestand-openen-mac | nl/journal/rar-bestand-openen-mac/index.md | rar openen mac | `mentioned_apps: [mediakit]`. «rar openen iphone», «rar bestand openen gratis», «rar openen online» (honest: upload), «zip openen iphone». Models fr/journal/ouvrir-fichier-rar-mac-iphone, es/journal/descomprimir-rar-mac, pt/journal/abrir-ficheiro-rar. Apple NL Archiefhulpprogramma / Bestanden-app behaviour only from fetched Apple NL pages. MediaKit archive facts (RAR4 and RAR5 extract, no RAR creation, no encrypted RAR) from the app facts and catalog |
| (local-only) to-do-lijst-maken | nl/journal/to-do-lijst-maken/index.md | to do lijst maken | `mentioned_apps: [taskful-day]`. «to do lijst», «to do lijstje», «to do lijst maken» (visible text «to-dolijst», sheet). Method claims only from fetched sources (for example a study or a reputable Dutch source); otherwise describe plainly what Taskful Day does (unfinished tasks roll over to today, 50 tasks free in total, 7 days Pro) from its Dutch page and glossary. Taskful Day's sentence parser has no Dutch keywords (I-0391): don't present Dutch sentence entry |
| (local-only) ontwormen-kat | nl/journal/ontwormen-kat/index.md | ontwormen kat | `mentioned_apps: [pawza]`. «ontwormen kat hoe vaak», «ontwormen kat schema», «wormen kat», «wormen kat symptomen». Model pt/journal/desparasitar-gato-e-cao (structure). Sources: LICG cat pages, ESCCAP Benelux PDFs, as fetched; no brands, no prices, no active ingredients unless a source warns about one. Link /nl/journal/ontwormen-hond/ and /nl/journal/vlooien-hond/. Pawza facts as in the reviewed dog post |
