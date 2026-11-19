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
