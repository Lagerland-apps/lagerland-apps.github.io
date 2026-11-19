# Writer brief: Spanish (es, Spain) Tier 4, batch 1 (journal posts)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/es-writer-brief.md` first and follow all of it.** This file adds what is different for journal posts.
Where the two disagree, this file wins. Also read TRANSLATION.md 6.5 (journal posts) and 6.7 (local-only pages).

## Your inputs

- The English source post `_journal/<slug>.md`: it holds the facts. Write from its meaning, for the Spanish query.
- The French post `fr/journal/<slug>/index.md`: structural template only (front-matter key set, how tables, source
  links, English-only links and the app section are written, read_time format). Never translate from French. The
  French writers replaced France-only context; you do the same for SPAIN, never copying French sources.
- `/Users/anttiaittamaa/Downloads/githubcode/es-tier4-research-2026-11-19.md`: your post's row (primary query, demand,
  localization notes).
- `_i18n/es.md` (sheet: register tú, typography, glossary table, tier names, tells to cut, every «Decisions» section),
  `_i18n/es-apple-terms.md`, the sections of `_i18n/es-glossary.md` for the apps your post names.
- The Spanish app page `es/apps/<app>/index.md` of each app the post describes: use its feature names and wording.
- App facts beyond the English post: only `_apps/<slug>.md` and the app's APP_BLUEPRINT.md §10 (claims register;
  location in `~/Downloads/githubcode/.agents/product-marketing.md`). Never §8 or §9.

## Front matter (copy the French key set)

```yaml
---
layout: journal
slug: <english slug>
ref: /journal/<english slug>/
permalink: /es/journal/<english slug>/
translated_from: <the English post's last_updated, or its date when it has no last_updated>
last_updated: 2026-11-19
date: 2026-11-19
title: "…"            # H1, written for the primary query
seo: { title, description, keywords }   # keywords 5 to 8, lowercase, real queries from the research row / suggest
lede: "…"
quick_answer: "…"     # answers the primary query on its own; it feeds the Quick Answer box and AI answers
excerpt: "…"
faq: [ { q, a } ]     # every English question kept (rephrased the way Spain asks), each ¿…?
mentioned_apps: [ … ] # copied from English (fact list)
read_time: "9 min de lectura"   # body words only (no front matter) ÷ 200, rounded; U+00A0 between number and «min»
---
```

Keep any other front-matter key the English post has that is text (for example `related_apps` stays as a fact list;
copy it). Never `lang`. The English `date` appears nowhere on the page.

## Links inside the post (Markdown, hard-coded, as the French posts write them)

- Spanish pages that exist: `/es/apps/<slug>/`, `/es/guides/<slug>/`, `/es/for/<slug>/`, `/es/alternatives/<slug>/`
  (check with `ls es/guides es/for es/alternatives`), and these Spanish journal posts written in this same batch:
  `/es/journal/how-many-steps-a-day-to-aim-for/`, `/es/journal/how-long-to-rest-between-sets/`,
  `/es/journal/how-to-estimate-your-one-rep-max/`, `/es/journal/rpe-and-rir-explained/`,
  `/es/journal/choosing-a-strength-program-you-will-finish/`, `/es/journal/how-much-to-tip-in-the-us/`,
  `/es/journal/compress-a-video-for-email/`, `/es/journal/apple-watch-hrv-without-a-baseline/`,
  `/es/journal/puppy-and-kitten-vaccination-schedule/`, `/es/journal/turnos-rotativos/`.
- Any other site page: the English URL, written `[texto en español](/journal/<slug>/){: hreflang="en"} (en inglés)`.
- External sources: keep every link the English post has. An English-language source gets `{: hreflang="en"}` and
  « (en inglés)» after the link, as the French posts do with « (en anglais) ». Spanish-language sources get nothing.
- Where the English links to the English post `rotating-shift-schedules-explained`, the Spanish local-only
  `/es/journal/turnos-rotativos/` may be linked instead when the sentence is about rotating shifts in general.

## Content rules for journal posts

- Same depth as English: every table row, number, study, caveat and hedge. Shorten padding only.
- Units: metric. Pounds become kilograms with the rounding the English uses (the French 1RM post shows how: it
  rebuilt the worked examples in kg; recompute every example yourself and show the inputs).
- Health, fitness, pet and money posts are YMYL: keep every «no es un consejo médico/veterinario» line and every
  study citation. Where a Spanish public authority (Ministerio de Sanidad, MAPA, INSST, BOE) says the same thing, you
  may cite it as well, but only from a page you fetched today; save it (see Sources). Never a number or rule from memory.
- US-only context: replace with Spain context from a fetched Spanish source, or cut it. Exception: the tipping post
  is about the US itself, so US rules and dollar amounts stay. Dollar amounts are written Spanish style: `20 $`
  (U+00A0) or «20 dólares», decimal comma (`26,64 $`), pick one style and keep it.
- Lift names as Spain's gyms say them: press de banca (banca), sentadilla, peso muerto, press militar, dominadas,
  remo. «Torso/pierna» for Upper/Lower; PPL stays PPL («empuje, tirón y pierna» once). 1RM stays 1RM; «repetición
  máxima (RM)» once. RPE and RIR stay; «repeticiones en reserva» once.
- App UI strings (EarnLock goal names, LiftLog program names, GymLogger X labels, Observa labels, AfterShift
  presets, Pawza labels, RightSplit, MediaKit presets) exactly as the Spanish glossary and Spanish app page give
  them; when the glossary has no string, describe the feature in plain words, never inside «» as a label.
- Prices of OUR apps only through tokens (`{P_MONTHLY@earnlock}` etc.), as the French post does; never «€».
- Keyword collisions (do not use as your primary or in your seo.title): `hrv apple watch`, `variabilidad frecuencia
  cardiaca` (Observa), `comprimir video iphone` (MediaKit), `app registro gimnasio` (LiftLog), `bloquear apps iphone`
  (EarnLock), `dormir después de trabajar de noche` (AfterShift), `mejor app gimnasio gratis` (workout guide),
  `app para dividir cuenta restaurante` (RightSplit), `cartilla veterinaria digital` (Pawza).
- The disclosure that the app is ours stays wherever the English has it.

## Sources (YMYL Spain additions and the local-only page)

Save every page you fetch for a fact into
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-QSBGdz/ae3f3811-617e-4206-99a4-9a9124fc8c81/scratchpad/es-t4/sources/<slug>/`
(one text file per source, named after the source, with its URL on the first line) so the reviewer can check claim by
claim. Fetch with `curl -sL` and strip HTML with `python3 -I`. Short quotes only (under 15 words), paraphrase the rest.

## Lessons from the French Tier 4 reviews (the most common must-fix items there)

- A hedge hardened («a good window» → a rule; «rarely» dropped; «about» dropped) or softened; an observational
  association written as cause; odds written as risk. Keep the English strength word for word.
- A writer-added definition or example that slips in a claim. One neutral sentence at most, nothing new.
- An FAQ question rewritten into a worry question with a softer answer; an H2 narrowed to the search query when the
  section covers more (put the query in the H1, seo.title and quick_answer only).
- English link text left before « (en inglés)»; the marker on a Spanish target; a plain space in «10.000 pasos» or
  «8 h» (U+00A0 before units, %, $, €, «min»); four-digit numbers take no separator (8000), five and more take a
  period (10.000, 47.471).
- Gendered adjectives addressed to the reader («cansado», «motivado», «tú mismo»): rephrase neutrally.
- Spanish tells in the sheet («Tells to cut») and TRANSLATION.md 8.2: no «Es importante destacar», «En resumen»,
  «no solo… sino también», trailing gerunds, title case, missing ¿¡, «a nivel de».
- read_time counted with the front matter (count the body only).

## Do NOT

Run `jekyll build`, `i18n.py map`, `stamp-last-updated.py` or any `git` command that changes state; touch any file
but your own post (and its sources folder); edit English, French or other languages' files; edit `es/llms.txt`, hubs
or app pages (the main session wires them). Other sessions (nl, fr, de, it, pt) work in this same checkout.

## Reply with

1. The path written and the final `seo.title` with its character count; the primary query used.
2. Every sentence you dropped or replaced for Spain (US context, US numbers) and why; every Spanish source added.
3. Glossary strings you could not find (described in plain words instead).
4. English-side errors you noticed, for ISSUES.md.

---

## Per-post notes

| Post | Write to | Primary query | Notes |
|---|---|---|---|
| how-many-steps-a-day-to-aim-for | es/journal/how-many-steps-a-day-to-aim-for/index.md | cuántos pasos al día | Secondaries from G: «cuántos pasos hay que dar al día», «cuántos pasos al día recomienda la OMS» (only if the post can answer what the WHO says: it may say the WHO gives minutes, not steps, only if a fetched WHO page says so; otherwise keep the keyword out), «cuántos pasos al día para adelgazar» only as a keyword if the post addresses weight (it likely doesn't: then leave it out). EarnLock goal names from es-glossary |
| how-long-to-rest-between-sets | es/journal/how-long-to-rest-between-sets/index.md | cuánto descansar entre series | «descanso entre series hipertrofia», «descanso entre series de fuerza». LiftLog rest timer per the Spanish page |
| how-to-estimate-your-one-rep-max | es/journal/how-to-estimate-your-one-rep-max/index.md | calcular 1rm | «fórmula 1rm», «fórmula brzycki», «fórmula epley», «calculadora rm». Examples in kg (recompute) |
| rpe-and-rir-explained | es/journal/rpe-and-rir-explained/index.md | rpe y rir | «diferencia rpe y rir», «rpe y rir tabla», «rir gimnasio significado». GymLogger X has no per-set RPE entry (keep the English wording on what it has) |
| choosing-a-strength-program-you-will-finish | es/journal/choosing-a-strength-program-you-will-finish/index.md | rutina ppl | «rutina torso pierna», «full body o rutina dividida», «rutina 5/3/1». LiftLog program names from its Spanish catalog / page |
| how-much-to-tip-in-the-us | es/journal/how-much-to-tip-in-the-us/index.md | propina en Estados Unidos | «propina en estados unidos es obligatoria», «propina en estados unidos porcentaje», «propina usa». US agencies named in Spanish with the English name once (Departamento de Trabajo, Department of Labor; IRS) |
| compress-a-video-for-email | es/journal/compress-a-video-for-email/index.md | comprimir vídeo para enviar por correo | «enviar vídeo pesado por correo», «comprimir vídeo para enviar por gmail». «vídeo» with accent in Spanish text (keywords may drop accents as people type them). Mail limits exactly as English states them; Apple «Mail Drop» name per es-apple-terms or Apple Spain (check; else describe) |
| apple-watch-hrv-without-a-baseline | es/journal/apple-watch-hrv-without-a-baseline/index.md | vfc baja | «vfc baja qué significa», «variabilidad de la frecuencia cardiaca valores normales». VFC (SDNN) always; Observa labels from es-glossary («Estableciendo tu referencia» shows for about the first five nights, per the sheet's batch 2 decision) |
| puppy-and-kitten-vaccination-schedule | es/journal/puppy-and-kitten-vaccination-schedule/index.md | vacunas cachorro | «calendario vacunas perros españa», «vacunas gatos calendario», «vacuna rabia perro obligatoria». Keep AAHA, AAFP, WSAVA as English. Replace the US rabies-law section with Spain: whether rabies vaccination is compulsory is set by each comunidad autónoma; state only what fetched official pages say (MAPA, a regional government page, BOE), name no community you did not source, and add the EU travel rule (Reglamento (UE) 576/2013: rabies vaccine and EU pet passport to travel) only from a fetched source (Your Europe es or MAPA). Never a vaccine price. «cachorro» and «gatito» |
| (local-only) | es/journal/turnos-rotativos/index.md | turnos rotativos | See below |

### Local-only: `/es/journal/turnos-rotativos/`

- Front matter: `layout: journal`, `slug: turnos-rotativos`, `permalink: /es/journal/turnos-rotativos/`,
  `local_only: true`, NO `ref`, NO `translated_from`, `last_updated` and `date` 2026-11-19, `mentioned_apps: [aftershift]`,
  everything else as above. Model: `fr/journal/travail-en-3x8/index.md` (read it for structure, never copy its French
  facts or sources).
- Query: `turnos rotativos`; secondaries from G: «turnos rotativos qué significa», «turnos rotativos mañana, tarde y
  noche», «turnos rotativos ejemplo», «cuadrante de turnos rotativos». The page answers: what «turnos rotativos» means,
  example patterns (mañana/tarde/noche; only patterns a fetched source gives or the English post gives), forward vs
  backward rotation, rest between shifts, night work, health and sleep, sleep tips per shift.
- Facts from: the English post `_journal/rotating-shift-schedules-explained.md` (forward/backward rotation, quick
  returns, Shon 2016, NIOSH, the three-shift 8-hour facts; drop its US schedule names unless you explain them as
  names used in the US), the English post `_journal/how-to-sleep-after-a-night-shift.md` for sleep tips (cite as it
  does), and Spanish sources you fetch and save:
  - Estatuto de los Trabajadores (Real Decreto Legislativo 2/2015) on BOE: art. 34.3 (rest between the end of one
    working day and the start of the next), art. 36 (trabajo nocturno, its limits, and the definition of «trabajo a
    turnos» in 36.3). https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430
  - INSST (Instituto Nacional de Seguridad y Salud en el Trabajo) notes on shift and night work (NTP 455 «Trabajo a
    turnos y nocturno: aspectos organizativos», NTP 502 «Trabajo a turnos: criterios para su análisis», or the current
    INSST pages; find them at https://www.insst.es). Use what they actually say, with the NTP number and year.
  - Real Decreto 1561/1995 (jornadas especiales) only if you cite an exception to the 12-hour rest, and only as it says.
- AfterShift: what it does for rotating shifts only from `_apps/aftershift.md`, `es/apps/aftershift/index.md`, the
  glossary (the rotation builder's presets by their Spanish names) and the blueprint §10. No medical claims; keep
  «no es un consejo médico» and «si el sueño sigue mal, habla con tu médico o con el servicio de prevención» (only
  the parts a source supports: the médico del trabajo / servicio de prevención mention needs the INSST or Ley 31/1995
  page you fetched).
- Slug, headings and all text in Spanish; no hreflang alternates (the layout handles it).

---

## Batch 2 (2026-11-19)

Same rules as batch 1, plus the lessons in the sheet's «Found in the Tier 4 batch 1 reviews» and «Decisions from Tier 4 batch 1» (read
both: they are the most common fixes). Research rows: «Batch 2 shortlist» in the research file. Sources folder:
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-QSBGdz/ae3f3811-617e-4206-99a4-9a9124fc8c81/scratchpad/es-t4/sources/<slug>/`.

Spanish pages that exist now (link them, never the English, where the sentence fits): the ten batch-1 posts
(`ls es/journal`), the guides (`ls es/guides`), the comparisons (`ls es/alternatives`), the audience pages (`ls es/for`), the app pages,
and these batch-2 posts: `/es/journal/when-to-deload/`, `/es/journal/puzzle-games-without-ads-or-lives/`,
`/es/journal/what-an-iphone-app-can-actually-block/`, `/es/journal/how-plan-mode-builds-a-checklist/`,
`/es/journal/find-every-recurring-charge/`, `/es/journal/frecuencia-cardiaca-en-reposo/`, `/es/journal/cuantas-horas-de-sueno-profundo/`,
`/es/journal/sobrecarga-progresiva/`, `/es/journal/pasaporte-para-perros/`, `/es/journal/convertir-mkv-a-mp4/`.

Check every seo.keywords entry against Google suggest before you ship it (batch 1 reviewers replaced several writer keywords that suggest
does not return): `curl -s "https://suggestqueries.google.com/complete/search?client=firefox&hl=es&gl=es&q=<url-encoded query>"`.

| Post | Write to | Primary query | Notes |
|---|---|---|---|
| when-to-deload | es/journal/when-to-deload/index.md | semana de descarga gym | «semana de descarga» with «deload» once; GymLogger X deload labels from its Spanish catalog (es.json `load_deload`, `session_score_deload` …) or plain words |
| puzzle-games-without-ads-or-lives | es/journal/puzzle-games-without-ads-or-lives/index.md | juegos sin anuncios iphone | Millrace: NEVER the digits of the number title it replaced, and no hint at it. Millrace's page keeps «juegos de lógica sin anuncios». Competitor games named only as English names them; no Spanish store facts unless you fetch the listing (`itunes.apple.com/lookup?country=es&lang=es_es&id=`) and save it |
| what-an-iphone-app-can-actually-block | es/journal/what-an-iphone-app-can-actually-block/index.md | cómo bloquear una app en iphone | Apple's Screen Time names as Apple Spain writes them for iOS 27 (es-apple-terms.md; fetch support.apple.com/es-es pages you need and save them). Keep the English «by itself» / structural limits exact. The screen-time guide `/es/guides/limitar-tiempo-de-pantalla-iphone/` is the Spanish how-to: link it |
| how-plan-mode-builds-a-checklist | es/journal/how-plan-mode-builds-a-checklist/index.md | lista para organizar una boda | Soon.'s plan-mode strings and event types exactly as its Spanish catalog / es/apps/soon/index.md give them; «evento» on the site (sheet). Suggestions are pre-written, not AI: keep that exact |
| find-every-recurring-charge | es/journal/find-every-recurring-charge/index.md | cómo ver mis suscripciones en iphone | Rocket Money, Truebill, Monarch, Copilot are not sold in Spain: rewrite those sections around Fintonic using ONLY its Spanish App Store description (`curl -s "https://itunes.apple.com/lookup?country=es&lang=es_es&id=672220319"`, save it) and the sheet's Fintonic decisions; model `es/guides/bill-tracker-without-bank-connection.html` and `es/alternatives/alternativa-a-fintonic.html` (read both). Drop Plaid, US banks and US law. Apple's «ver o cancelar suscripciones» path from support.apple.com/es-es/118428 (fetch, save). AllPaid facts via its Spanish page, glossary and blueprint §10; prices via `{P_…@allpaid}`; disclose it is ours |

### Local-only posts (front matter as the batch-1 local-only post: `local_only: true`, no `ref`, no `translated_from`, `slug` = the folder name, `date` and `last_updated` 2026-11-19)

Every fact from a page you fetched today and saved (URL on line 1), from an English post you name, or from the app's facts. Nothing from
memory. YMYL caveats in every health and pet post. Short quotes only. Model the French local-only post named in each row for structure;
never copy French facts or French sources.

| Write to | Primary query | Model (structure only) | Sources to fetch and save | App section |
|---|---|---|---|---|
| es/journal/frecuencia-cardiaca-en-reposo/index.md | frecuencia cardiaca en reposo normal | fr/journal/frequence-cardiaque-au-repos/index.md | Spanish-language medical sources: Fundación Española del Corazón (fundaciondelcorazon.com), MedlinePlus en español (medlineplus.gov/spanish), a Spanish public-health page if one states a range; Apple es-es on resting heart rate («Frecuencia cardiaca en reposo»); any study only as a source you fetched or an English Lagerland post cites it | Observa's resting-heart-rate use (score weight, «rango habitual») from es/apps/observa/index.md and blueprint §10; Observa is not a medical device |
| es/journal/cuantas-horas-de-sueno-profundo/index.md | cuántas horas de sueño profundo | fr/journal/sommeil-profond-combien-d-heures/index.md | Spanish sleep or public-health sources (Sociedad Española de Sueño ses.org.es, MedlinePlus en español, Ministerio de Sanidad if it states adult sleep hours); Apple es-es sleep stages (Despierto, REM, Esencial, Sueño profundo) and that they are estimates. State no minimum or percentage unless a fetched source gives it; a calculation from a source percentage is labelled «cálculo orientativo» | Observa's sleep score and deep-sleep use from its Spanish page and §10. AfterShift's stage names are its own (Ligero, Profundo): don't mix them with Observa |
| es/journal/sobrecarga-progresiva/index.md | sobrecarga progresiva | fr/journal/surcharge-progressive-musculation/index.md | ACSM 2009 position stand abstract (PubMed) and the ACSM 2026 resistance-training position stand (as the French page cites it: fetch and save), plus the English posts `_journal/double-progression-explained.md` and `_journal/when-to-deload.md` for their facts | LiftLog prefills the program's target weight (progression schemes per its Spanish page); GymLogger X spots plateaus («Estancamiento», «En observación», «Estancamiento previsto»; Pro) |
| es/journal/pasaporte-para-perros/index.md | pasaporte para perros | fr/journal/passeport-europeen-chien-chat/index.md | MAPA «Viajar con la mascota. Perros, gatos, hurones» (mapa.gob.es), the BOE or EU regulation text it cites, Your Europe in Spanish, the official page that says who issues the passport in Spain (veterinario autorizado/habilitado) only as fetched. No price unless an official source gives one; dogs, cats and ferrets as the source says. Which documents cover non-EU travel only as the sources say | Pawza stores the passport and vaccine certificates as documents and reminders, per its Spanish page and §10 |
| es/journal/convertir-mkv-a-mp4/index.md | convertir mkv a mp4 | fr/journal/convertir-mkv-en-mp4/index.md | matroska.org (what MKV is), Apple es-es on video formats the iPhone/Mac play (fetch, save), VideoLAN docs for VLC's convert function (the French page shows which); remuxing vs re-encoding only as the sources explain it | MediaKit's convert tool by its Spanish catalog labels («Convertir», formats) and §10; never claim MKV features the blueprint doesn't list |

---

## Batch 3 (2026-11-19)

Same rules as batches 1 and 2. Read the sheet's «Decisions from Tier 4 batch 1» and «batch 2» and every «Found in the Tier 4 … reviews» list
before writing: they are the most common fixes (hedges, near-verbatim copying, writer conclusions, keyword collisions, «X lo explica» link
shapes, indefinido for recent past, gendered words). Research rows: «Batch 3 shortlist» in the research file. Sources folder as before:
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-QSBGdz/ae3f3811-617e-4206-99a4-9a9124fc8c81/scratchpad/es-t4/sources/<slug>/`.
Check every keyword in Google suggest (hl=es, gl=es) before shipping it.

Spanish pages that exist now: `ls es/journal es/guides es/alternatives es/for`, the app pages, plus these batch-3 posts:
`/es/journal/your-photos-shouldnt-ride-the-elevator/`, `/es/journal/festivos-2027/`, `/es/journal/cuantos-dias-faltan-para-navidad/`,
`/es/journal/comprimir-pdf-mac/`, `/es/journal/extraer-audio-de-video-iphone/`, `/es/journal/series-de-aproximacion/`,
`/es/journal/deuda-de-sueno/`, `/es/journal/sueno-rem/`, `/es/journal/vo2-max/`, `/es/journal/desparasitar-perro/`.

PDFs: macOS PDFKit via `swift` extracts real PDFs (`import PDFKit; print(PDFDocument(url: URL(fileURLWithPath: path))!.string!)`); some
official sites serve an HTML viewer whose page carries the full text. PubMed/PMC block curl: use NCBI eutils or Europe PMC. EUR-Lex returns
nothing: use the BOE/DOUE mirror.

| Write to | Primary query | Model (structure only) | Sources to fetch and save | App section |
|---|---|---|---|---|
| es/journal/your-photos-shouldnt-ride-the-elevator/index.md (translation of `_journal/your-photos-shouldnt-ride-the-elevator.md`; `ref`, `translated_from` = English last_updated 2026-11-08) | convertir heic a jpg | fr/journal/your-photos-shouldnt-ride-the-elevator/index.md | Apple es-es pages for HEIF/HEVC and the camera «Más compatible» setting, the Photos «Transferir a Mac o PC» setting, only if the English or the French twin points to that fact | MediaKit per its Spanish page, glossary (with Additions) and §10 |
| es/journal/festivos-2027/index.md | festivos 2027 españa | fr/journal/jours-feries-2027/index.md | The BOE «Resolución … de la Dirección General de Trabajo, por la que se publica la relación de fiestas laborales para el año 2027» (search boe.es; save it). Use its national list and its table by comunidad exactly. If it is not published yet, say so and give only what an official source (BOE, Estatuto de los Trabajadores art. 37.2, Real Decreto 2001/1983 art. 45) states; never a list from memory or from news sites | Soon.: a countdown to a holiday, «Festivo» event type, widgets (free), per its Spanish page and §10 |
| es/journal/cuantos-dias-faltan-para-navidad/index.md | cuántos días faltan para navidad | fr/journal/compte-a-rebours-noel/index.md | Apple es-es pages on widgets (home and lock screen) and «En reposo» (StandBy), only as fetched; no day count typed for a date that changes daily (say how to count, and what Soon. shows) | Soon. widgets, events, Premium (reminders, live activity, widget per event) per its Spanish page and §10 |
| es/journal/comprimir-pdf-mac/index.md | comprimir pdf mac | fr/journal/compresser-pdf-mac/index.md | Apple es-es Vista Previa guide pages (exportar PDF, «Filtro Quartz» / «Reducir tamaño del archivo»), fetched | MediaKit's PDF compression per its Spanish page and §10, labels from its catalog |
| es/journal/extraer-audio-de-video-iphone/index.md | extraer audio de vídeo iphone | fr/journal/extraire-son-video-iphone/index.md | Apple es-es pages for Atajos / iMovie / Fotos only as they say what is possible; nothing about third-party online sites you didn't fetch | MediaKit's audio extraction per its Spanish page, §10 and catalog |
| es/journal/series-de-aproximacion/index.md | series de aproximación | fr/journal/echauffement-musculation/index.md | Fradkin 2010, McCrary 2015, Ribeiro 2014 abstracts (eutils/Europe PMC), as the French page cites them; the Spanish batch-1/2 gym posts for terms | GymLogger X and LiftLog warm-up set handling per their Spanish pages (warm-up sets out of volume and records, no rest timer in LiftLog) |
| es/journal/deuda-de-sueno/index.md | deuda de sueño | fr/journal/rattraper-dette-de-sommeil/index.md | Sociedad Española de Sueño (the Rev Neurol 2016 document the deep-sleep post saved), MedlinePlus en español; any study only as fetched | AfterShift's sleep debt per its Spanish page, glossary («Deuda en aumento», Estable, Recuperando) and §10; not medical advice |
| es/journal/sueno-rem/index.md | sueño rem | fr/journal/sommeil-paradoxal/index.md | SES, NHLBI (es), MedlinePlus en español, Apple es-es sleep stages; no percentage or «normal» amount unless an authoritative source gives it (commercial pages only as in the deep-sleep post, or not at all) | Observa's sleep tab per its Spanish page; link the deep-sleep post |
| es/journal/vo2-max/index.md | vo2 max qué es | fr/journal/vo2-max/index.md | Apple es-es on «VO2 máximo» / cardio fitness on Apple Watch, Apple's VO2 max validation paper (as the French page cites it), a Spanish-language medical source for the definition, Mandsager 2018 only as fetched | Observa's cardio-fitness card per its Spanish page and catalog |
| es/journal/desparasitar-perro/index.md | desparasitar perro | fr/journal/vermifuger-son-chien/index.md | ESCCAP España (esccap.es) guides and recommendations, fetched (PDFs via PDFKit); frequencies only as ESCCAP states them, with their conditions; no product, brand or dose; «no es un consejo veterinario» | Pawza's treatments, recurring reminders and dose history per its Spanish page and §10 |

All but the first row are local-only: `local_only: true`, no `ref`, no `translated_from`, slug = folder name, date and last_updated 2026-11-19.

---

## Batch 4 (2026-11-19)

Same rules as batches 1 to 3. Read every «Decisions from Tier 4 batch …» section and every «Found in the Tier 4 … reviews» list in the sheet
first. All ten posts are local-only (`local_only: true`, no `ref`, no `translated_from`, slug = folder name, date and last_updated 2026-11-19).
Sources folder as before (`…/scratchpad/es-t4/sources/<slug>/`), URL on line 1, fetched today. Check every keyword in Google suggest.
Spanish pages that exist: `ls es/journal es/guides es/alternatives es/for`, the app pages, plus these batch-4 posts:
`/es/journal/descomprimir-rar-mac/`, `/es/journal/unir-pdf-mac/`, `/es/journal/pulgas-y-garrapatas-perro/`, `/es/journal/leishmaniosis-perro/`,
`/es/journal/saturacion-de-oxigeno-normal/`, `/es/journal/frecuencia-respiratoria-normal/`, `/es/journal/zonas-de-frecuencia-cardiaca/`,
`/es/journal/cuantas-series-por-musculo/`, `/es/journal/tecnica-pomodoro/`, `/es/journal/reglas-del-ajedrez/`.
Structure models: the French post named in the row where one exists; otherwise the reviewed Spanish local-only post named there.

| Write to | Primary query | Model | Sources to fetch and save | App section |
|---|---|---|---|---|
| es/journal/descomprimir-rar-mac/index.md | descomprimir rar mac | fr/journal/ouvrir-fichier-rar-mac-iphone/index.md | RARLAB (rarlab.com, what RAR is, RAR5), The Unarchiver and Keka official pages (what they are, price/free only as their pages say), Apple es-es on «Utilidad de Compresión» (Archive Utility) and the formats it opens; nothing about «online» services you didn't fetch | MediaKit extracts RAR4 and RAR5 and creates ZIP (not RAR), per its Spanish page, §10 and catalog; link es/alternatives/izip.html |
| es/journal/unir-pdf-mac/index.md | unir pdf mac | es/journal/comprimir-pdf-mac/index.md | Apple es-es Vista Previa guide page(s) on combining PDFs (drag thumbnails, insert pages), fetched | MediaKit «Combinar PDF» (also an Atajos action) per its Spanish page, §10 and catalog |
| es/journal/pulgas-y-garrapatas-perro/index.md | pulgas y garrapatas perro | fr/journal/puces-tiques-chien/index.md | ESCCAP España guide 3 (ectoparasites, 2nd ed. 2018 — the deworming post saved it under `…/sources/desparasitar-perro/`; re-extract), plus any newer ESCCAP España page; no product, brand, active ingredient, dose or price (the suggest «pipeta …» queries are brand queries: don't target them) | Pawza treatments and recurring reminders; link the deworming post |
| es/journal/leishmaniosis-perro/index.md | leishmaniosis perro | es/journal/desparasitar-perro/index.md | ESCCAP España guide on vector-borne diseases (guía n.º 5 or current), the Ministerio de Sanidad / CNE page on human leishmaniasis in Spain only if fetched (for «se contagia a humanos»), LeishVet only if fetched; symptoms, transmission, prevention as stated; vaccines and treatments only named as categories the source names, no products; «no es un consejo veterinario» | Pawza (records, vaccines, reminders) |
| es/journal/saturacion-de-oxigeno-normal/index.md | saturación de oxígeno normal | es/journal/frecuencia-cardiaca-en-reposo/index.md | MedlinePlus en español (oximetría / saturación), Apple es-es on the Oxígeno en sangre app (availability, «no está diseñado para uso médico», how to measure), any Spanish public-health page if fetched; ranges only as a source states them; «no es un consejo médico» | Observa reads blood oxygen from Salud de Apple (Spanish page, §10); not a medical device |
| es/journal/frecuencia-respiratoria-normal/index.md | frecuencia respiratoria normal | es/journal/frecuencia-cardiaca-en-reposo/index.md | MedlinePlus en español (frecuencia respiratoria / signos vitales, ranges by age as stated), Apple es-es on respiratory rate measured during sleep; «no es un consejo médico» | Observa: respiratory rate in Respiración and its effect on readiness, per its Spanish page and §10 |
| es/journal/zonas-de-frecuencia-cardiaca/index.md | zonas de frecuencia cardiaca | es/journal/vo2-max/index.md | Apple es-es pages on heart rate zones in the Entreno app (how they are calculated, zone names, editing them), any formula only as a fetched source gives it (no 220−age unless a source you fetched states it, with its caveat) | Observa's heart rate zones in Corazón per its Spanish page, §10 and catalog |
| es/journal/cuantas-series-por-musculo/index.md | cuántas series por músculo a la semana | fr/journal/series-par-muscle-par-semaine/index.md | ACSM 2026 position stand (Europe PMC), Schoenfeld 2017 (eutils), as the French page cites them, re-fetched; link es/journal/sobrecarga-progresiva/ (it saved ACSM 2026) | GymLogger X «Volumen de series» (Pro) per its Spanish page, catalog and §10; LiftLog only if its page supports a volume claim |
| es/journal/tecnica-pomodoro/index.md | técnica pomodoro | es/journal/series-de-aproximacion/index.md | Francesco Cirillo's own pages (francescocirillo.com) for what the technique is (25 minutes, breaks), fetched; any study only if fetched; no productivity claims a source doesn't make | Taskful Day «Modo concentración» and its Pro timer (10, 25 or 45 minutes, or 5 to 120), live activity on iPhone, per its Spanish page, glossary, §10 and catalog |
| es/journal/reglas-del-ajedrez/index.md | reglas del ajedrez | es/journal/festivos-2027/index.md (structure of a reference page) | FIDE Laws of Chess (handbook.fide.com, current edition) and the Spanish translation from FEDA (feda.org) if fetched; piece moves, castling, en passant, promotion, check, checkmate, stalemate, draws, clock rules only as the Laws state them; Spanish piece names (rey, dama, torre, alfil, caballo, peón) and notation letters (R, D, T, A, C) | Chessful per its Spanish page, glossary (tier Pro) and §10; link es/guides/best-chess-apps-iphone.html |
