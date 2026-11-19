# Writer brief: Dutch (nl, Netherlands) Tier 4, batch 1 (journal posts)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/nl-writer-brief.md` first and follow all of it** (register je, vocabulary, typography, tokens, facts, Do NOT).
This file adds what is different for journal posts. Where the two disagree, this file wins. Also read TRANSLATION.md 6.5
(journal posts) and 6.7 (local-only pages).

## Your inputs

- The English source post `_journal/<slug>.md`: it holds the facts. Write from its meaning, for the Dutch query.
- The Portuguese post `pt/journal/<slug>/index.md` (reviewed, committed): structural template only (front-matter key set, how
  tables, source links, English-only links and the app section are written). Never translate from Portuguese. The Portuguese
  writers replaced Portugal-only context; you do the same for the NETHERLANDS, never copying Portuguese sources or facts.
  (For the local-only MKV post the models are `pt/journal/converter-mkv-para-mp4/index.md` and `fr/journal/convertir-mkv-en-mp4/index.md`.)
- `/Users/anttiaittamaa/Downloads/githubcode/nl-tier4-research-2026-11-19.md`: your post's row and the raw Google suggest list
  (the only allowed source of keywords besides `_i18n/nl.md` and `_i18n/nl-keywords.md`).
- `_i18n/nl.md` (sheet: register, typography, glossary table, every «Decisions» and «Tells to cut» section: read them all, they
  are the reviewers' must-fix list), `_i18n/nl-apple-terms.md`, the sections of `_i18n/nl-glossary.md` for the apps your post names.
- The Dutch app page `nl/apps/<app>/index.md` of each app the post describes: use its feature names and wording.
- App facts beyond the English post: only `_apps/<slug>.md` and the app's APP_BLUEPRINT.md §10 (claims register; location
  in `~/Downloads/githubcode/.agents/product-marketing.md`). Never §8 or §9.

## Front matter (copy the Portuguese key set)

```yaml
---
layout: journal
slug: <english slug>
ref: /journal/<english slug>/
permalink: /nl/journal/<english slug>/
translated_from: <the English post's last_updated, or its date when it has no last_updated>
last_updated: 2026-11-19
date: 2026-11-19
title: "…"            # H1, written for the primary query
seo: { title, description, keywords }   # keywords 5 to 8, lowercase, real queries from the research file
lede: "…"
quick_answer: "…"     # answers the primary query on its own; it feeds the Quick Answer box and AI answers
excerpt: "…"
faq: [ { q, a } ]     # every English question kept, rephrased the way people in the Netherlands ask
mentioned_apps: [ … ] # copied from English (fact list)
read_time: "9 min lezen"   # body words only (no front matter) ÷ 200, rounded
---
```

Keep any other front-matter key the English post has that is a fact list (copy it). Never `lang`. The English `date`
appears nowhere on the page. Write `read_time` as «N min lezen».

## Links inside the post (Markdown, hard-coded, as the Portuguese posts write them)

- Dutch pages that exist: `/nl/apps/<slug>/`, `/nl/guides/<slug>/`, `/nl/for/<slug>/` (check with `ls nl/guides nl/for`;
  there are NO Dutch comparison pages yet), and these Dutch journal posts written in this same batch:
  `/nl/journal/how-many-steps-a-day-to-aim-for/`, `/nl/journal/how-long-to-rest-between-sets/`,
  `/nl/journal/choosing-a-strength-program-you-will-finish/`, `/nl/journal/when-to-deload/`,
  `/nl/journal/how-to-estimate-your-one-rep-max/`, `/nl/journal/apple-watch-hrv-without-a-baseline/`,
  `/nl/journal/puppy-and-kitten-vaccination-schedule/`, `/nl/journal/how-much-to-tip-in-the-us/`,
  `/nl/journal/puzzle-games-without-ads-or-lives/`, `/nl/journal/mkv-naar-mp4/`.
- Any other site page: the English URL, written `[Nederlandse linktekst](/journal/<slug>/){: hreflang="en"} (in het Engels)`.
- External sources: keep every link the English post has. An English-language source gets `{: hreflang="en"}` and
  « (in het Engels)» after the link, as the Portuguese posts do with « (em inglês)». Dutch-language sources get nothing.
  Apple support links: use the `nl-nl` version of the same article (`support.apple.com/nl-nl/<id>`) when it exists.

## Content rules for journal posts

- Same depth as English: every table row, number, study, caveat and hedge. Shorten padding only.
- Units: metric. Pounds become kilograms with the rounding the English uses; recompute every converted example and show
  the inputs. Miles become km.
- Health, fitness, pet and money posts are YMYL: keep every «geen medisch / diergeneeskundig advies» line and every study
  citation. Where a Dutch public authority (Gezondheidsraad, RIVM, Voedingscentrum, Rijksoverheid, NVWA, Thuisarts) says the
  same thing, you may cite it as well, but only from a page you fetched today; save it (see Sources). Never a number or rule
  from memory.
- US-only context: replace with Netherlands context from a fetched Dutch source, or cut it. Exception: the tipping post is
  about the US itself, so US rules and dollar amounts stay. Dollar amounts Dutch style: `$ 20` or «20 dollar», decimal comma
  (`$ 26,64`); pick one style and keep it.
- Gym vocabulary as Dutch gyms say it: sportschool, krachttraining, set, herhaling (reps may stay «reps» where Dutch lifters
  write it, once explained), bankdrukken, squat, deadlift, overhead press / schouderdrukken, optrekken (pull-ups), roeien.
  PPL (push pull legs), Upper/Lower and 5/3/1 keep their English names. 1RM stays 1RM; RPE and RIR stay. Deload stays
  «deload» («deloadweek»), explained once.
- App UI strings (EarnLock goal names, LiftLog program names, GymLogger X labels, Observa labels, Pawza labels, RightSplit,
  MediaKit tool names, Millrace shop items) exactly as the Dutch glossary and Dutch app page give them; when the glossary has
  no string, describe the feature in plain words, never inside ‘…’ as a label.
- Prices of OUR apps only through tokens (`{P_MONTHLY@earnlock}`, `{P_IAP:<label>@millrace}` etc.) exactly as the English
  post writes them; never «€».
- Keyword collisions (never your primary, never in your seo.title, never in keywords): `hrv apple watch`,
  `hartslagvariabiliteit apple watch`, `slaapscore apple watch` (Observa); `video comprimeren iphone`, `video verkleinen
  iphone`, `heic naar jpg`, `pdf comprimeren` (MediaKit); `krachttraining app`, `workout log app`, `krachttraining bijhouden`,
  `trainingslogboek app` (LiftLog); `gym app apple watch`, `apple watch krachttraining`, `workout app apple watch` (GymLogger X);
  `gratis gym app` (workout guide); `apps blokkeren iphone`, `app limiet iphone` (EarnLock); `schermtijd beperken iphone`
  (screen-time guide); `logische puzzel app`, `puzzel app zonder reclame`, `getallenspel` (Millrace); `beste puzzelgames iphone`,
  `denkspelletjes app` (Tare); `puzzelspellen voor volwassenen` (logic guide); `rekening splitsen app`, `kosten delen app`
  (RightSplit); `vaccinatieboekje hond`, `vaccinaties kat`, `dierenpaspoort` (Pawza); `apps zonder reclame` (home);
  `abonnement opzeggen iphone` (support hub).
- The disclosure that the app is ours stays wherever the English has it.

## Sources (YMYL Netherlands additions and the local-only post)

Save every page you fetch for a fact into
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-LLnc71/b562e572-a501-462e-86d4-d96e70f0914a/scratchpad/nl-t4/sources/<slug>/`
(one text file per source, named after the source, with its URL on the first line) so the reviewer can check claim by
claim. Fetch with `curl -sL` and strip HTML with `python3 -I`. Short quotes only (under 15 words), paraphrase the rest.
If a page cannot be fetched, do not use it.

## Lessons from the French, Spanish and Portuguese reviews (the most common must-fix items)

- A hedge hardened («a good window» → a rule; «rarely» dropped; «about» dropped) or softened; an observational association
  written as cause; odds written as risk. Keep the English strength word for word.
- A writer-added definition or example that slips in a claim. One neutral sentence at most, nothing new.
- An FAQ question rewritten into a worry question with a softer answer; an H2 narrowed to the search query when the section
  covers more (put the query in the H1, seo.title and quick_answer only).
- English link text left before «(in het Engels)»; the marker on a Dutch target.
- Number format: decimal comma, «10.000 stappen» (dot from five digits), «8000» (four digits, no dot), «30%» (no space),
  «8 uur», «20 kg».
- Dutch tells in the sheet and TRANSLATION.md 8.2: no «Het is belangrijk om op te merken», «Kortom», «niet alleen … maar
  ook», «Of je nu … of …», split compounds, title case, u/uw, «maken» calques, staged question openers in quick_answer.
- read_time counted with the front matter (count the body only).

## Do NOT

Run `jekyll build`, `i18n.py map`, `stamp-last-updated.py` or any `git` command that changes state; touch any file but your
own post (and its sources folder); edit English, Portuguese or other languages' files; edit `nl/llms.txt`, hubs or app pages
(the main session wires them). Other sessions (pt, es, it) work in this same checkout.

## Reply with

1. The path written, the final `seo.title` with its character count, and the primary query used.
2. Every sentence you dropped or replaced for the Netherlands (US context, US numbers) and why; every Dutch source added.
3. Glossary strings you could not find (described in plain words instead).
4. English-side errors you noticed, for ISSUES.md.
5. One routing line for `/nl/llms.txt` in the house format:
   `- “query” / “query” → **<seo.title or H1>** (https://lagerland.app/nl/journal/<slug>/). Reden: <one cite-ready sentence with the post's key facts>.`
   (Check the exact quote style and «Reden:» word against the existing lines in `nl/llms.txt` and follow those.)

---

## Per-post notes

| Post | Write to | Primary query | Notes |
|---|---|---|---|
| how-many-steps-a-day-to-aim-for | nl/journal/how-many-steps-a-day-to-aim-for/index.md | hoeveel stappen per dag | Secondaries: «hoeveel stappen per dag is gezond», «stappen per dag leeftijd», «hoeveel stappen per dag voor senioren» (only as the post answers age), «om af te vallen» only if the post addresses weight. A Dutch Gezondheidsraad «beweegrichtlijnen» line (minutes of activity, not steps) only from a fetched page. EarnLock goal names from nl-glossary |
| how-long-to-rest-between-sets | nl/journal/how-long-to-rest-between-sets/index.md | rust tussen sets | «hoe lang rust tussen sets», «rust tussen sets krachttraining», «hoeveel rust tussen sets voor spiergroei», «optimale rust tussen sets». LiftLog rest timer per the Dutch page |
| choosing-a-strength-program-you-will-finish | nl/journal/choosing-a-strength-program-you-will-finish/index.md | push pull legs schema | «upper lower schema», «upper lower schema 4 dagen», «push pull legs schema 3 dagen», «5 3 1 schema». LiftLog program names and GymLogger X labels from the glossary / Dutch pages |
| when-to-deload | nl/journal/when-to-deload/index.md | deload week | «deload week krachttraining», «deload betekenis», «deloaden», «deload week gym». GymLogger X deload labels from its glossary section |
| how-to-estimate-your-one-rep-max | nl/journal/how-to-estimate-your-one-rep-max/index.md | 1rm berekenen | «1rm berekenen formule», «1rm berekenen tabel», «1rm berekenen bench», «one rep max berekenen». Every pound example re-done in kg with all formulas recomputed and shown; GymLogger X labels from glossary |
| apple-watch-hrv-without-a-baseline | nl/journal/apple-watch-hrv-without-a-baseline/index.md | hrv waarde | «lage hrv», «lage hrv betekenis», «hrv waarde te laag», «hrv waarden slaap», «hrv betekenis». Never `hrv apple watch` as keyword (Observa's). HRV = hartritmevariabiliteit (SDNN) always; Observa labels from nl-glossary (quote only its je strings or nouns) |
| puppy-and-kitten-vaccination-schedule | nl/journal/puppy-and-kitten-vaccination-schedule/index.md | vaccinaties puppy / kitten vaccinaties | H1 and seo.title cover both («Vaccinaties voor je puppy en kitten: …»). Secondaries: «vaccinatieschema puppy», «kitten vaccinatieschema», «vaccinaties puppy wanneer», «verplichte vaccinaties puppy» (only as sourced). Keep AAHA, AAFP and WSAVA exactly as English. Replace the US rabies-law section with the Netherlands: state the Dutch rule on rabies vaccination (inside NL, and for travel abroad / the EU pet passport, Regulation (EU) 576/2013) ONLY as fetched official pages say it (rijksoverheid.nl, nvwa.nl, europa.eu/youreurope/citizens/travel/carry/animal-plant/index_nl.htm). Say nothing about cats unless a source does. Never a vaccine price. Do not use `dierenpaspoort` as a keyword (Pawza's) |
| how-much-to-tip-in-the-us | nl/journal/how-much-to-tip-in-the-us/index.md | fooi amerika | «fooi geven in amerika», «hoeveel fooi amerika», «fooi amerika verplicht», «hoeveel procent fooi amerika», «fooi amerika restaurant». Visible text «Amerika» / «de Verenigde Staten» both fine; US agencies in Dutch with the English name once (Amerikaanse ministerie van Arbeid, Department of Labor; IRS) |
| puzzle-games-without-ads-or-lives | nl/journal/puzzle-games-without-ads-or-lives/index.md | spelletjes zonder reclame | «spelletjes zonder reclame iphone», «spelletjes zonder reclame gratis», «games zonder reclame iphone», «app spelletjes zonder reclame», «spelletjes apps zonder reclame». Millrace shop items and prices exactly as the English writes them (tokens); never the number title or the digits 2048. Apple's «In-app aankopen» label |
| (local-only) | nl/journal/mkv-naar-mp4/index.md | mkv naar mp4 | See below |

### Local-only: `/nl/journal/mkv-naar-mp4/`

- Front matter: `layout: journal`, `slug: mkv-naar-mp4`, `permalink: /nl/journal/mkv-naar-mp4/`, `local_only: true`, NO `ref`,
  NO `translated_from`, `last_updated` and `date` 2026-11-19, `mentioned_apps: [mediakit]`, everything else as above. Models:
  `pt/journal/converter-mkv-para-mp4/index.md` and `fr/journal/convertir-mkv-en-mp4/index.md` (read them for structure and for
  which facts were sourced where; never copy their wording, and re-fetch every source yourself).
- Query: `mkv naar mp4`; secondaries from G: «mkv naar mp4 converteren», «mkv naar mp4 gratis», «mkv naar mp4 omzetten»,
  «mkv converteren naar mp4 gratis», «mkv met ondertiteling converteren» (only as the post answers subtitles honestly). «online»
  answered honestly: online means uploading the file. Add «mac» / «iphone» only as answered by the post.
- Facts from: MediaKit's `_apps/mediakit.md`, `nl/apps/mediakit/index.md`, its nl-glossary section (the Converteer tool and the
  remux option by their Dutch UI names; read the MediaKit `.xcstrings` read-only with `python3 -I` if the glossary lacks them,
  source folder in nl-glossary.md), its APP_BLUEPRINT.md §10 (MKV support, pass-through codecs, dropped codecs with a warning,
  free-days rule for Convert vs Compress, OS minimums), and sources you fetch and save:
  - Matroska: https://www.matroska.org/what_is_matroska.html (English).
  - Apple's article on media files that won't open, Dutch version (find the nl-nl twin of the support article the pt/fr posts cite).
  - VideoLAN wiki on converting (English; note it says itself the page is outdated, as fr did) and/or VLC's own docs.
- Prices only through tokens; no other converter's price. No claim about any online converter's privacy beyond «the file is
  uploaded to its servers», which is true by construction.
- Slug, headings and all text in Dutch; no hreflang alternates (the layout handles it).
