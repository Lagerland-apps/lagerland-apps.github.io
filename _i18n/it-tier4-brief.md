# Writer brief: Italian (it, Italy) Tier 4, batch 1 (journal posts)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/it-writer-brief.md` first and follow all of it.** This file adds what is different for journal posts.
Where the two disagree, this file wins. Also read TRANSLATION.md 6.5 (journal posts) and 6.7 (local-only pages).

## Your inputs

- The English source post `_journal/<slug>.md`: it holds the facts. Write from its meaning, for the Italian query.
- The French post `fr/journal/<slug>/index.md` (and the Spanish `es/journal/<slug>/index.md` where it exists):
  structural template only (front-matter key set, how tables, source links, English-only links and the app section are
  written, read_time format). Never translate from French or Spanish. They replaced France- or Spain-only context; you
  do the same for ITALY, never copying their sources.
- `/Users/anttiaittamaa/Downloads/githubcode/it-tier4-research-2026-11-19.md`: your post's row (primary query, demand,
  localization notes).
- `_i18n/it.md` (sheet: register tu, typography, glossary table, tier names, every «Decisions» and «Tells» section),
  `_i18n/it-apple-terms.md`, the sections of `_i18n/it-glossary.md` for the apps your post names.
- The Italian app page `it/apps/<app>/index.md` of each app the post describes: reuse its feature names and wording.
- App facts beyond the English post: only `_apps/<slug>.md` and the app's APP_BLUEPRINT.md §10 (claims register;
  location in `~/Downloads/githubcode/.agents/product-marketing.md`). Never §8 or §9.

## Front matter (copy the French key set)

```yaml
---
layout: journal
slug: <english slug>
ref: /journal/<english slug>/
permalink: /it/journal/<english slug>/
translated_from: <the English post's last_updated, or its date when it has none>
last_updated: 2026-11-19
date: 2026-11-19
title: "…"            # H1, written for the primary query
seo: { title, description, keywords }   # keywords 5 to 8, lowercase, real queries from the research row
lede: "…"
quick_answer: "…"     # answers the primary query on its own; feeds the Quick Answer box and AI answers
excerpt: "…"
faq: [ { q, a } ]     # every English question kept, rephrased the way Italians ask it
mentioned_apps: [ … ] # copied from English (fact list)
read_time: "9 min di lettura"   # body words only (no front matter) ÷ 200, rounded; U+00A0 between number and «min»
---
```

Keep any other front-matter key the English post has that is text; copy fact lists (`related_apps`) as they are. Never
`lang`. The English `date` appears nowhere on the page.

## Links inside the post (Markdown, hard-coded, as the French posts write them)

- Italian pages that exist: `/it/apps/<slug>/`, `/it/guides/<slug>/`, `/it/for/<slug>/`, `/it/alternatives/<slug>/`
  (check with `ls it/guides it/for it/alternatives`), and these Italian posts written in this same batch:
  `/it/journal/how-many-steps-a-day-to-aim-for/`, `/it/journal/how-long-to-rest-between-sets/`,
  `/it/journal/how-to-estimate-your-one-rep-max/`, `/it/journal/rpe-and-rir-explained/`,
  `/it/journal/choosing-a-strength-program-you-will-finish/`, `/it/journal/when-to-deload/`,
  `/it/journal/how-much-to-tip-in-the-us/`, `/it/journal/apple-watch-hrv-without-a-baseline/`,
  `/it/journal/puppy-and-kitten-vaccination-schedule/`, `/it/journal/festivita-2027/`.
- Any other site page: the English URL, written `[testo in italiano](/journal/<slug>/){: hreflang="en"} (in inglese)`.
- External sources: keep every link the English post has. An English-language source gets `{: hreflang="en"}` and
  « (in inglese)» after the link, as the French posts do with « (en anglais) ». Italian-language sources get nothing.

## Content rules for journal posts

- Same depth as English: every table row, number, study, caveat and hedge. Shorten padding only.
- Units: metric. Pounds become kilograms with the rounding the English uses (the French 1RM post rebuilt the worked
  examples in kg; recompute every example yourself and show the inputs). Decimal comma; 8000 (four digits, no
  separator), 10.000 (five and more, period); U+00A0 before units, €, $ and «min»; no space before %.
- Health, fitness, pet and money posts are YMYL: keep every «non è un consiglio medico/veterinario» line and every study
  citation. Where an Italian public authority (Ministero della Salute, ISS, Gazzetta Ufficiale, a Regione) says the same
  thing, you may cite it as well, but only from a page you fetched today and saved (see Sources). Never a number or a rule
  from memory.
- US-only context: replace with Italian context from a fetched Italian source, or cut it. Exception: the tipping post is
  about the US itself, so US rules and dollar amounts stay, written Italian style: `20 $` (U+00A0) or «20 dollari»,
  decimal comma (`26,64 $`); pick one style and keep it.
- Gym vocabulary as Italian gyms say it: «panca piana», «squat», «stacco da terra», «military press», «trazioni»,
  «rematore»; «massimale» for 1RM (write «massimale (1RM)» once, then either); «recupero» for rest between sets;
  «scheda» for a programme card; «settimana di scarico» for deload («deload» once); RPE and RIR stay, with «ripetizioni
  in riserva» once and the Italian gym word «buffer» once where RIR is introduced; PPL, upper/lower, full body and 5/3/1
  keep their English names (Italians type them so), with «push pull legs» spelled out once.
- App UI strings (EarnLock goal names, LiftLog program and tier names, GymLogger X labels, Observa labels, Pawza
  labels, RightSplit, Soon.) exactly as the Italian glossary and the Italian app page give them; when the glossary has no
  string, describe the feature in plain words, never inside “ ” as a label.
- Prices of OUR apps only through tokens (`{P_MONTHLY@earnlock}` etc.), single braces, as the French post does; never «€».
- Keyword collisions (never your primary or in your seo.title; fine in body text): `hrv apple watch`, `variabilità della
  frequenza cardiaca` (Observa), `bloccare app iphone` (EarnLock), `app diario allenamento palestra`, `app palestra senza
  abbonamento` (LiftLog), `app scheda palestra apple watch` (GymLogger X), `app palestra gratis senza abbonamento`
  (workout guide), `app per dividere il conto`, `dividere il conto alla romana` (RightSplit), `libretto sanitario cane`
  (Pawza), `conto alla rovescia iphone` (Soon.), `come mettere un conto alla rovescia su iphone` (countdown guide).
- The disclosure that the app is ours stays wherever the English has it. «Lagerland Apps» or «lo studio»; «noi» only where
  the English says "we".
- Italian tells (sheet «Tells to cut» and TRANSLATION.md 8.2): no «È importante notare», «In conclusione», «non solo… ma
  anche», «fondamentale/cruciale» everywhere, trailing gerunds, title case, «a livello di», «andare a + infinito». Gendered
  words addressed to the reader («stanco», «motivato», «sei pronto»): rephrase neutrally.

## Sources (YMYL Italy additions and the local-only page)

Save every page you fetch for a fact into
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-d7tDJh/69d88126-1df9-4e51-857f-b06117579141/scratchpad/it-t4/sources/<slug>/`
(one text file per source, named after the source, with its URL on the first line) so the reviewer can check claim by
claim. Fetch with `curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko)
Version/17.0 Safari/605.1.15"` and strip HTML with `python3 -I`. Short quotes only (under 15 words), paraphrase the rest.

## Lessons from the French and Spanish Tier 4 reviews (the most common must-fix items)

- A hedge hardened («a good window» → a rule; «rarely» dropped; «about» dropped) or softened; an observational
  association written as cause; odds written as risk. Keep the English strength word for word.
- A writer-added definition or example that slips in a claim. One neutral sentence at most, nothing new.
- An FAQ question rewritten into a worry question with a softer answer; an H2 narrowed to the search query when the
  section covers more (put the query in the H1, seo.title and quick_answer only).
- English link text left before « (in inglese)»; the marker on an Italian target; a plain space in «10.000 passi» or
  «8 h».
- read_time counted with the front matter (count the body only).

## Do NOT

Run `jekyll build`, `i18n.py map`, `stamp-last-updated.py` or any `git` command that changes state; touch any file but
your own post (and its sources folder); edit English, French or other languages' files; edit `it/llms.txt`, hubs or app
pages (the main session wires them). Other sessions (nl, es, pt) work in this same checkout at the same time.

## Reply with

1. The path written and the final `seo.title` with its character count; the primary query used.
2. Every sentence you dropped or replaced for Italy (US context, US numbers) and why; every Italian source added.
3. Glossary strings you could not find (described in plain words instead).
4. English-side errors you noticed, for ISSUES.md.

---

## Per-post notes

| Post | Primary query | Notes |
|---|---|---|
| how-many-steps-a-day-to-aim-for | quanti passi al giorno | Secondaries: «quanti passi al giorno bisogna fare», «quanti passi al giorno per stare bene», «10000 passi al giorno», «10000 passi al giorno benefici». «per dimagrire» only if the post addresses weight (it likely doesn't: leave it out). EarnLock goal names from it-glossary / it/apps/earnlock |
| how-long-to-rest-between-sets | recupero tra le serie | «tempo di recupero tra le serie», «recupero tra le serie ipertrofia», «quanto riposare tra una serie e l’altra». LiftLog rest timer per the Italian page |
| how-to-estimate-your-one-rep-max | calcolo massimale | «calcolare massimale», «formula brzycki», «calcolo massimale panca», «calcolo massimale indiretto». Examples in kg (recompute). GymLogger X uses Epley |
| rpe-and-rir-explained | rpe e rir | «rir palestra», «rpe palestra», «scala rpe palestra», «rpe e rir differenza», «buffer palestra». GymLogger X has no per-set RPE entry (keep the English wording on what it has) |
| choosing-a-strength-program-you-will-finish | push pull legs | «scheda push pull legs», «scheda upper lower», «meglio full body o split», «push pull legs upper lower». LiftLog program names from its Italian page / glossary. The Italian GymLogger X page's related_journal anchor will be set to your H1 |
| when-to-deload | settimana di scarico | «settimana di scarico palestra», «settimana di scarico ogni quanto», «scarico palestra», «deload palestra». Never «Project Invictus» (a brand). GymLogger X deload labels from its Italian page |
| how-much-to-tip-in-the-us | mancia in america | «mancia in america obbligatoria», «mancia in america quanto», «mancia in america percentuale», «mancia negli stati uniti». US agencies named in Italian with the English name once (Dipartimento del Lavoro, Department of Labor; IRS). RightSplit wording from it/apps/rightsplit |
| apple-watch-hrv-without-a-baseline | hrv bassa | «hrv bassa cosa significa», «hrv bassa cause», «hrv bassa di notte». HRV (SDNN) always, never «VFC». Observa labels from it-glossary (its baseline strings are flagged inconsistent: describe in plain words where in doubt) |
| puppy-and-kitten-vaccination-schedule | vaccinazioni cane (H1 also covers kittens) | «vaccini cucciolo cane», «vaccinazioni cane obbligatorie», «vaccini cucciolo cane quando», «vaccini gattino». YMYL. AAHA, AAFP, WSAVA as English states them. Replace the US rabies-law section with ITALY: whether the rabies vaccine is compulsory in Italy (nationally, regionally, for travel) only from fetched official pages (salute.gov.it pages on rabies and on travelling with pets; a Regione page only if you cite it). EU travel rule (Reg. (UE) 576/2013: microchip, rabies vaccine, EU pet passport) only from a fetched source (salute.gov.it or Your Europe it). Name no region you did not source. Never a vaccine price. «cucciolo» and «gattino» |
| (local-only) festivita-2027 | festività 2027 | See below |

### Local-only: `/it/journal/festivita-2027/`

- Front matter: `layout: journal`, `slug: festivita-2027`, `permalink: /it/journal/festivita-2027/`, `local_only: true`, NO
  `ref`, NO `translated_from`, `last_updated` and `date` 2026-11-19, `mentioned_apps: [soon]`, everything else as above.
  Model: `fr/journal/jours-feries-2027/index.md` (read it for structure; never copy its French facts or sources).
- Query: `festività 2027`; secondaries from G: «festività 2027 italia», «ponti 2027», «festività 2027 calendario»,
  «festività 2027 san francesco», «ponti 2027 lavoro», «festività 2027 4 ottobre».
- The page answers: the Italian national holidays of 2027 with their weekday (a table), how many fall on a weekend, the
  new 4 October holiday (San Francesco d’Assisi, festa nazionale from 2026, Legge 8 ottobre 2025, n. 151, Gazzetta
  Ufficiale Serie generale n. 236 del 10 ottobre 2025: fetch the text from gazzettaufficiale.it or normattiva.it and state
  only what it says), Easter and Easter Monday 2027 (Pasqua 28 marzo, Lunedì dell’Angelo 29 marzo 2027: verify with a
  fetched calendar or compute and say it is computed), the ponti 2027 worked out from the calendar (a «ponte» is a
  working day between a holiday and a weekend; say clearly that a ponte is not a right and depends on the employer or
  the contract, only as strongly as a fetched source says), patron saints («ogni comune festeggia il proprio santo
  patrono»: give no list beyond what a fetched source names; Rome’s 29 June, Milan’s 7 December only if sourced).
- The base list of national holidays: Legge 27 maggio 1949, n. 260 as amended (fetch from normattiva.it), or a fetched
  official page (governo.it, a ministry) listing them. Compute each 2027 weekday yourself and double-check it.
- Pay and work on a holiday: only what a fetched official or primary source says; otherwise leave it out. No CCNL detail
  from memory.
- Soon.: what it does for a holiday countdown only from `_apps/soon.md`, `it/apps/soon/index.md`, the glossary and the
  blueprint §10 (free event limit, pinning, widgets: wording exactly as the Italian app page). Link the Italian countdown
  guide `/it/guides/come-mettere-conto-alla-rovescia-iphone/` once.
- Slug, headings and all text in Italian; no hreflang alternates (the layout handles it).

---

# Batch 2 (2026-11-19): 4 translations + 6 local-only posts

Everything above applies. Batch 1 is live: read one finished Italian post of your topic area first
(`it/journal/<slug>/index.md`) for tone, link style and front matter, and `_i18n/it.md` § «Decisions from the Tier 4 reviews»
and the «Found in the Tier 4 reviews» tells. Those were the reviewers' most common fixes: hyphen ranges, dropped hedges,
writer-added definitions, keywords with no suggest evidence, gendered address, bold-label bullets, reviewer-facing meta in copy.

Italian journal posts you may link (batch 1, live): the ten listed in "Links inside the post" above. Batch 2 posts (will exist):
`/it/journal/find-every-recurring-charge/`, `/it/journal/double-progression-explained/`,
`/it/journal/puzzle-games-without-ads-or-lives/`, `/it/journal/how-plan-mode-builds-a-checklist/`,
`/it/journal/frequenza-cardiaca-a-riposo/`, `/it/journal/sonno-rem/`, `/it/journal/vo2-max/`,
`/it/journal/passaporto-europeo-cane/`, `/it/journal/convertire-mkv-in-mp4/`, `/it/journal/sovraccarico-progressivo/`.
Italian comparisons now also include jefit, strong-workout-app, xnconvert, documents-by-readdle, hrv4training, one-sec, flow-free,
two-dots, rise-sleep-tracker, wikipedia-app, kiwix, wikiwand (`ls it/alternatives`).

New keyword owners (never your primary): `giochi senza pubblicità iphone` (Tare), `giochi di logica senza pubblicità` (Millrace),
`cancellare abbonamento iphone` (support hub), `gestione abbonamenti app iphone` and `migliore app per scadenze pagamenti` (bill
guide), `convertire video in mp4 iphone` (MediaKit), `hrv valori normali` (batch 1 HRV post).

## Local-only posts (6): common rules

Front matter: `layout: journal`, `slug` = the Italian slug, `permalink: /it/journal/<slug>/`, `local_only: true`, NO `ref`, NO
`translated_from`, `date` and `last_updated` 2026-11-19, `mentioned_apps` as the table says. Structural models: the French and
Spanish local-only posts named per row (read for structure only; never copy their facts or sources). Every fact comes from:
(a) an Italian or international source you fetched today and saved (sources folder, URL on line 1), (b) an English post on this site
that says it (cite it as the English post does, or link it with «(in inglese)»), or (c) the app's facts (`_apps/<slug>.md`, the
Italian app page, the glossary, blueprint §10). Never a number from memory. Health and pet posts are YMYL: a «non è un consiglio
medico/veterinario» line, and «parlane con il medico / con il veterinario» only as strongly as a source supports. Quote under 15
words, paraphrase the rest.

## Batch 2 per-post notes

| Post | Write to | Primary | Notes |
|---|---|---|---|
| find-every-recurring-charge (AllPaid) | it/journal/find-every-recurring-charge/index.md | come vedere abbonamenti iphone | Secondaries «come vedere abbonamenti attivi iphone», «abbonamenti attivi apple», «addebiti ricorrenti», «addebiti ricorrenti paypal». Rocket Money / Truebill are not sold in Italy: replace that section with Wallet by BudgetBakers and Spendee as the Italian bank-linked examples, using ONLY the facts on `it/alternatives/alternativa-a-wallet-budgetbakers.html` and in `~/Downloads/githubcode/it-tier2-research-2026-11-19.md` (Spendee: «Sincronizza il tuo conto bancario»); no prices unless those files give them. Where the English names US places (Venmo, US carriers) use Italian ones only from fetched official help pages (Apple Italy «Visualizzare o annullare gli abbonamenti», PayPal Italia «pagamenti automatici», Google Play it); Postepay/bank-app «addebiti ricorrenti» only if you fetch an official page. Model: es/journal/find-every-recurring-charge (Fintonic). The Apple path as Apple Italy writes it: Impostazioni > [il tuo nome] > Abbonamenti |
| double-progression-explained (LiftLog) | it/journal/double-progression-explained/index.md | doppia progressione | «doppia progressione palestra», «metodo doppia progressione», «progressione doppia allenamento». Examples in kg, recomputed. LiftLog progression names from its Italian page/glossary |
| puzzle-games-without-ads-or-lives (Millrace) | it/journal/puzzle-games-without-ads-or-lives/index.md | giochi senza pubblicità | «giochi senza pubblicità gratis», «giochi senza pubblicità online», «migliori giochi iphone senza pubblicità». NEVER the number title Millrace replaced (no «2048» anywhere, not even as a genre). Any competitor game named in the English: check it is sold in the Italian App Store (iTunes lookup country=it) before keeping a store fact; drop US-only store facts |
| how-plan-mode-builds-a-checklist (Soon.) | it/journal/how-plan-mode-builds-a-checklist/index.md | checklist matrimonio | «checklist organizzazione matrimonio», «lista cose da fare matrimonio», «lista cose da fare per organizzare matrimonio». Soon. plan-mode labels exactly as the Italian app page / glossary. Do NOT claim an Italian event title picks the event type (I-0295: type is read from English title words); if the English says the type comes from the title, describe what the English says without implying it works for Italian titles, or cut it. Wedding timings only as the English gives them |
| local-only frequenza-cardiaca-a-riposo (Observa) | it/journal/frequenza-cardiaca-a-riposo/index.md | frequenza cardiaca a riposo | «frequenza cardiaca a riposo normale», «frequenza cardiaca a riposo donna», «frequenza cardiaca a riposo uomo», «frequenza cardiaca a riposo ideale». Models fr frequence-cardiaque-au-repos, es frecuencia-cardiaca-en-reposo. Sources: ISS / Ministero della Salute / an Italian university-hospital page for the normal range; Apple Italy for «Battito cardiaco a riposo» and how the Watch measures it; Observa facts. English posts to reuse: `apple-health-metrics-worth-interpreting`, `your-apple-health-data-doesnt-mean-what-you-think` |
| local-only sonno-rem (Observa) | it/journal/sonno-rem/index.md | sonno rem | «sonno rem cos’è», «sonno rem e non rem», «sonno rem quanto deve durare», «sonno rem e sonno profondo». Model fr sommeil-paradoxal. Apple Italy's stages Veglia, REM, Principale, Profondo (support.apple.com/it-it/108906) and Apple's own caveat on accuracy; percentages only from a fetched source (e.g. an Italian sleep-medicine society or university page, or a cited study). Observa: only what its Italian page says about sleep |
| local-only vo2-max (Observa) | it/journal/vo2-max/index.md | vo2 max | «vo2 max cos’è», «vo2 max apple watch», «vo2 max valori», «vo2 max come si calcola». Model fr vo2-max. Apple Italy «tono cardiovascolare» (support.apple.com/it-it pages on cardio fitness: how it's estimated, which workouts, the age range, «Basso» level and notifications); value tables only from a fetched source with its name; Observa facts |
| local-only passaporto-europeo-cane (Pawza) | it/journal/passaporto-europeo-cane/index.md | passaporto europeo cane | «passaporto europeo cane come ottenerlo», «passaporto cane dove si fa», «passaporto cane quanto dura», «passaporto europeo cane costo» (cost only if an official ASL/Regione page states it; else say it varies by ASL and to ask yours, only as the source says). Model fr passeport-europeen-chien-chat. Reuse the batch 1 sources in `…/sources/puppy-and-kitten-vaccination-schedule/` (salute.gov.it passport, microchip, viaggio verso l’Italia, Your Europe it): copy the files you rely on into your own sources folder. Cats and ferrets too where the sources say so |
| local-only convertire-mkv-in-mp4 (MediaKit) | it/journal/convertire-mkv-in-mp4/index.md | convertire mkv in mp4 | «convertire mkv in mp4 con vlc», «convertire mkv in mp4 senza perdere qualità», «convertire mkv in mp4 mac», «app per convertire mkv in mp4». Model fr convertir-mkv-en-mp4, es convertir-mkv-a-mp4. Sources: matroska.org, VideoLAN docs (VLC convert), Apple Italy support on supported formats; HandBrake only as its site says (link /it/alternatives/handbrake/). MediaKit facts only from blueprint §10 and it/apps/mediakit (free tools, Pro, iPhone and Mac, on-device). No claim that remuxing never loses anything beyond what a source says |
| local-only sovraccarico-progressivo (LiftLog, GymLogger X) | it/journal/sovraccarico-progressivo/index.md | sovraccarico progressivo | «sovraccarico progressivo come si fa», «sovraccarico progressivo esempi», «sovraccarico progressivo significato», «principio del sovraccarico progressivo». Model fr surcharge-progressive-musculation, es sobrecarga-progresiva. Studies and numbers only as the English posts `double-progression-explained`, `choosing-a-strength-program-you-will-finish`, `how-long-to-rest-between-sets` cite them, or from a paper you fetch (PubMed abstract). Link the Italian double-progression, program and deload posts. Never «Project Invictus» |

---

# Batch 3 (2026-11-19): 10 local-only posts

Everything above applies, especially "Local-only posts: common rules" (batch 2) and the Tier 4 «Decisions» and «Found in the
Tier 4 reviews» lists in `_i18n/it.md` (batch 2 additions included). Read one finished batch 2 local-only post of your area first for
tone, sourcing and front matter: health `it/journal/sonno-rem/index.md`, pets `it/journal/passaporto-europeo-cane/index.md`, media
`it/journal/convertire-mkv-in-mp4/index.md`, gym `it/journal/sovraccarico-progressivo/index.md`, calendar `it/journal/festivita-2027/index.md`.

**Sources folder for batch 3** (new path): `/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/69d88126-1df9-4e51-857f-b06117579141/scratchpad/it-t4/sources/<slug>/`
(one text file per source, URL on line 1). Batch 1 and 2 sources stay readable at
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-d7tDJh/69d88126-1df9-4e51-857f-b06117579141/scratchpad/it-t4/sources/<slug>/`;
copy any you rely on into your own folder.

Italian posts you may link: all twenty in `ls it/journal/`, plus these ten (will exist): `/it/journal/estrarre-audio-da-video-iphone/`,
`/it/journal/ridurre-dimensioni-foto-iphone/`, `/it/journal/riscaldamento-palestra/`, `/it/journal/quante-serie-per-gruppo-muscolare/`,
`/it/journal/pulci-e-zecche-cane/`, `/it/journal/sverminare-cane/`, `/it/journal/conto-alla-rovescia-natale/`,
`/it/journal/turni-a-ciclo-continuo/`, `/it/journal/sonno-profondo/`, `/it/journal/saturazione-apple-watch/`.

Rules that matter most here: every fact from a saved source, an English post on this site, or the app's facts (`_apps/<slug>.md`, the
Italian app page, the glossary, APP_BLUEPRINT §10 only, never §4/§8/§9); state source disagreements side by side; label your own
arithmetic «un calcolo fatto per questa pagina»; never quote an app's defective Italian string (glossary flags); no product brand,
dose or price on pet and health posts; «non è un consiglio medico/veterinario»; keywords only real suggest queries; U+00A0 before every
unit and in read_time; no hyphen ranges; no bold-label bullets; no «noi», «cioè» glosses or reviewer-facing meta in the copy.

## Batch 3 per-post notes

| Post (write to it/journal/<slug>/index.md) | App | Primary | Secondaries (suggest) and notes |
|---|---|---|---|
| estrarre-audio-da-video-iphone | MediaKit | estrarre audio da video iphone | «… gratis», «… imovie», «… comandi rapidi», «estrarre solo audio da video iphone». Model fr extraire-son-video-iphone. Apple Italy pages for iMovie / Comandi Rapidi steps only as they write them (fetch support.apple.com/it-it); MediaKit facts from §10 and it/apps/mediakit (audio formats it writes; which tools are free) |
| ridurre-dimensioni-foto-iphone | MediaKit | ridurre dimensioni foto iphone | «… gratis», «… mentre si scatta», «ridurre dimensioni file foto iphone», «app per ridurre dimensioni foto iphone». Model fr reduire-taille-photo-iphone. Apple Italy on HEIF/HEVC vs «Più compatibile», Mail attachment size choices, Foto; MediaKit image tools (Ridimensiona immagine, Comprimi immagine are free per §10: check) |
| riscaldamento-palestra | GymLogger X, LiftLog | riscaldamento palestra | «riscaldamento palestra esercizi», «… pesi», «… cosa fare», «… 5 minuti». Model fr echauffement-musculation. Studies only from PubMed abstracts / PMC you fetch (general vs specific warm-up, stretching before lifting); GymLogger X preventive warm-up in the Smart Program Creator and warm-up sets that don't count (Italian app pages); LiftLog warm-up sets don't count toward records |
| quante-serie-per-gruppo-muscolare | LiftLog, GymLogger X | quante serie per gruppo muscolare | «… a settimana», «quante serie allenanti per gruppo muscolare a settimana», «… per ipertrofia». Model fr series-par-muscle-par-semaine. ACSM 2026 (PMC12965823; reuse the batch 2 sovraccarico sources), dose-response meta-analyses (PubMed abstracts you fetch); GymLogger X “Volume di serie” (Pro) per the Italian page; link sovraccarico, deload, program posts |
| pulci-e-zecche-cane | Pawza | pulci e zecche cane | «pulci e zecche cane periodo», «… cucciolo», «protezione pulci e zecche cane». Model fr puces-tiques-chien. YMYL vet: ESCCAP Italia (esccap.it), Ministero della Salute / ISS / an Istituto Zooprofilattico page (leishmaniosi, malattie trasmesse da zecche) as they say it; no product, brand, dose or price; Pawza treatment reminders per the Italian page |
| sverminare-cane | Pawza | sverminare cane | «sverminare cane cucciolo», «sverminare cane adulto», «sverminare cane ogni quanto». Model fr vermifuger-son-chien. YMYL vet: ESCCAP Italia guideline (frequency by risk), Ministero/Your Europe on echinococco for travel (reuse batch 2 passport sources); no product, dose or price; Pawza reminders |
| conto-alla-rovescia-natale | Soon. | conto alla rovescia natale | «conto alla rovescia natale 2026», «… app», «… settimane», «conto alla rovescia natale 2027». Model fr compte-a-rebours-noel. Weekdays and day counts computed with python3 and labelled as computed; Italian Christmas dates only from a fetched source if you name any (Vigilia, Santo Stefano are in festivita-2027: link it); Soon. facts and widget names as the Italian Soon. page; link the countdown guide /it/guides/come-mettere-conto-alla-rovescia-iphone/ (it owns `come mettere un conto alla rovescia su iphone`) |
| turni-a-ciclo-continuo | AfterShift | turni a ciclo continuo | «turni a ciclo continuo significato», «… come funziona», «riposo tra un turno e l’altro», «riposo minimo tra un turno e l’altro», «11 ore di riposo tra un turno e l’altro legge». Models es turnos-rotativos, fr travail-en-3x8. Law: D.lgs. 8 aprile 2003, n. 66 from Normattiva (art. 1 definitions of lavoro a turni / notturno, art. 7 riposo giornaliero 11 ore consecutive, art. 13 night work limits, and the derogations exactly as written); schemes (3 2, 4 2, 6 2, 4 o 5 squadre) only as a fetched source describes them; sleep facts as the English posts rotating-shift-schedules-explained and how-to-sleep-after-a-night-shift cite them; AfterShift facts only from its Italian page/§10. «parlane con il medico competente» only if a fetched source supports it |
| sonno-profondo | Observa | sonno profondo | «sonno profondo quanto dura», «sonno profondo quanto deve durare», «sonno profondo e sonno rem», «sonno profondo e sonno leggero». Never «sonno profondo banana yoshimoto» (a novel). Models fr sommeil-profond-combien-d-heures, es cuantas-horas-de-sueno-profundo. Reuse the batch 2 sonno-rem sources (Treccani, Cleveland Clinic, Sleep Foundation, NINDS, Ohayon, Apple 108906, Apple white paper); Apple's «Profondo» stage; link /it/journal/sonno-rem/ and stay consistent with it |
| saturazione-apple-watch | Observa | saturazione apple watch | «saturazione apple watch affidabile», «come vedere saturazione apple watch», «apple watch saturazione bassa», «saturazione sangue apple watch». No model. Apple Italy pages on the «Livelli O₂» app (Apple Italy's name; «ossigeno nel sangue» only in prose; support.apple.com/it-it: which models, how to measure, background readings, «not for medical use» wording, factors that affect it); ISSalute or another Italian public page for normal SpO2 values; Observa reads «ossigeno nel sangue» from Salute (Italian app page). No claim about availability outside Italy unless Apple Italy says it |

---

# Batch 4 (2026-11-19): 10 local-only posts

Everything above applies: "Local-only posts: common rules" (batch 2), the batch 3 rules (sources folder path, app claims only from §10
and the Italian app page, never §3/§4/§11), and every Tier 4 «Decisions» and «Found in the Tier 4 reviews» list in `_i18n/it.md`
(batch 3 additions included). The batch 3 reviewers' most common fixes: keyword-then-colon H1s and FAQ questions; process meta («le fonti
consultate», «studi letti», «lette il 19 novembre»); absence claims built from a page's examples; near-verbatim copies of a source
sentence; ranges written «4 o 12»; a hedge or a legal condition dropped; app claims from the wrong blueprint section. Avoid them.

Sources folder (same as batch 3): `/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/69d88126-1df9-4e51-857f-b06117579141/scratchpad/it-t4/sources/<slug>/`.
Earlier sources you may copy: that folder (batch 3) and `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-d7tDJh/69d88126-1df9-4e51-857f-b06117579141/scratchpad/it-t4/sources/` (batches 1 and 2).

Italian posts you may link: all thirty in `ls it/journal/`, plus these ten (will exist): `/it/journal/scadenza-bollo-auto/`,
`/it/journal/10000-passi-quanti-km/`, `/it/journal/convertire-heic-in-jpg/`, `/it/journal/convertire-mov-in-mp4/`,
`/it/journal/unire-pdf-iphone/`, `/it/journal/comprimere-video-whatsapp/`, `/it/journal/caffeina-quanto-dura-effetto/`,
`/it/journal/frequenza-cardiaca-notturna/`, `/it/journal/regole-degli-scacchi/`, `/it/journal/microchip-gatto/`.

Keyword owners (never your primary or seo.title): MediaKit `comprimere video iphone`, `comprimere pdf iphone`, `convertire video in mp4
iphone`; Chessful `app scacchi`, `imparare scacchi app`; chess guide `migliore app scacchi iphone`; AllPaid `app promemoria pagamenti`,
`app scadenze bollette`; steps post `quanti passi al giorno`; resting-HR post `frequenza cardiaca a riposo`; Pawza `libretto sanitario
cane`; AfterShift `dormire dopo il turno di notte`.

## Batch 4 per-post notes

| Post (it/journal/<slug>/index.md) | App | Primary | Secondaries and notes |
|---|---|---|---|
| scadenza-bollo-auto | AllPaid | scadenza bollo auto | «scadenza bollo auto con targa», «scadenza bollo auto verifica», «scadenza revisione auto», «scadenza revisione auto come funziona». The bollo (tassa automobilistica) is regional: say how deadlines generally work only as ACI / Agenzia delle Entrate / a Regione page states it, name only regions whose page you fetched, and point to the official «verifica» services as their pages describe them. Revisione intervals from the Codice della strada art. 80 (Normattiva) or the Portale dell’automobilista. No fines or amounts unless an official page states them, dated. AllPaid: reminders for a bill or contract per its Italian page (it does not know your car's deadlines; you enter them). No model page |
| 10000-passi-quanti-km | EarnLock | 10000 passi quanti km sono | «10000 passi quanti km sono in quanto tempo», «… calorie», «quante calorie si bruciano camminando», «quante calorie si bruciano camminando per 1 ora». Stride length, walking speed and MET values only from fetched sources (a university or public health page; the Compendium of Physical Activities); every km, minute and kcal figure is «un calcolo fatto per questa pagina» with its inputs; health caveat; link /it/journal/how-many-steps-a-day-to-aim-for/. EarnLock facts per its Italian page |
| convertire-heic-in-jpg | MediaKit | convertire heic in jpg | «convertire heic in jpg gratis», «… iphone», «… mac». Apple Italy pages: «Più compatibile», automatic JPEG when sharing (support.apple.com/it-it/116944, reuse the batch 3 photo sources), Foto/Anteprima export on Mac. MediaKit: Converti immagine is NOT one of the five free tools; after the first 3 days it needs Pro, even for one file (I-0392): say exactly that, never «gratis» for MediaKit's HEIC conversion. Model fr/es pages only if one exists |
| convertire-mov-in-mp4 | MediaKit | convertire mov in mp4 | «convertire mov in mp4 gratis», «… mac», «… senza perdere qualità», «… con vlc», «… iphone». Model: it/journal/convertire-mkv-in-mp4/index.md (reuse its VLC, Apple QuickTime sources); MediaKit Converti per §10 / Italian page (trial rule as in the MKV post) |
| unire-pdf-iphone | MediaKit | unire pdf iphone | «unire pdf iphone gratis», «unire due pdf iphone», «unire foto in pdf iphone». Model es/journal/unir-pdf-mac (structure only). Apple Italy only for what its pages document (File app, Anteprima on Mac, «Crea PDF» if documented); MediaKit PDF Unisci and whether it is free per §10 / the Italian page |
| comprimere-video-whatsapp | MediaKit | comprimere video whatsapp | «comprimere video per whatsapp gratis», «comprimere video iphone per whatsapp», «comprimere video per stato whatsapp». WhatsApp Help Center (Italian pages, faq.whatsapp.com) for size limits, HD and document sending, exactly as they say it, dated; MediaKit Comprimi video is one of the five free tools (Italian page); link the English compress-a-video-for-email post with «(in inglese)» |
| caffeina-quanto-dura-effetto | AfterShift | quanto dura l’effetto della caffeina | «quanto dura l’effetto della caffeina di un caffè», «… nel corpo», «… nel sangue», «caffeina quanto dura l’effetto». YMYL: EFSA's 2015 caffeine opinion (half-life range, safe intakes, sleep effects) from efsa.europa.eu, plus an Italian public page (ISS, Ministero) if found; caffeine per cup only from a fetched source; AfterShift caffeine timing exactly as its Italian page says; «non è un consiglio medico» |
| frequenza-cardiaca-notturna | Observa | frequenza cardiaca notturna | «frequenza cardiaca notturna normale», «… bassa», «frequenza cardiaca durante il sonno», «frequenza cardiaca durante il sonno quanto deve essere». YMYL: reuse the batch 2 resting-HR sources (ISSalute, Humanitas, MSD, Apple 120277) and the sleep sources (NINDS); nocturnal dip only from a fetched study abstract; Observa shows nocturnal heart rate and its dip per its Italian page; link /it/journal/frequenza-cardiaca-a-riposo/ and stay consistent with it |
| regole-degli-scacchi | Chessful | regole degli scacchi | «regole degli scacchi per principianti», «… in breve», «… arrocco», «… en passant», «… per bambini». Model es/journal/reglas-del-ajedrez (structure only). Rules from the FIDE Laws of Chess (handbook.fide.com) and the Italian text of the Federazione Scacchistica Italiana if you find it; Italian piece names (re, donna, torre, alfiere, cavallo, pedone), «arrocco», «presa en passant», «promozione», «stallo», «patta»; Chessful facts per its Italian page; link /it/guides/best-chess-apps-iphone/ |
| microchip-gatto | Pawza | microchip gatto obbligatorio | «microchip gatto obbligatorio 2026», «microchip gatto obbligatorio lombardia» (or other regions only if sourced). Only official pages: Ministero della Salute (reuse the batch 2 microchip page), Gazzetta Ufficiale / Normattiva, regional laws or pages. State exactly where and since when the microchip is compulsory for cats; if no national obligation is sourced, say what the sources say (dogs compulsory nationally; cats where a Regione requires it, or for travel abroad) and name only sourced regions. No price. Pawza Scheda di emergenza stores the microchip number per its Italian page; link the passport post |
