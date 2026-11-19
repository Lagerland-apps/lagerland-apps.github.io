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
