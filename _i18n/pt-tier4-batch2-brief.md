# Writer brief: Portuguese (pt, Portugal) Tier 4, batch 2 (journal posts, mostly local-only)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/pt-tier4-brief.md` first and follow all of it** (it points to `_i18n/pt-writer-brief.md`: read that too).
This file adds batch 2. Where they disagree, this file wins. Batch 1 is live under `/pt/journal/`: read one reviewed post
(e.g. `pt/journal/when-to-deload/index.md` or `pt/journal/puppy-and-kitten-vaccination-schedule/index.md`) to see the
final house style after review.

## Three rules batch 1 broke most (each cost a reviewer dozens of fixes)

1. **Read `~/.claude/skills/copy-editing/SKILL.md` (the file, not just its name) and apply its Seven Sweeps and AI-tell
   removal**, then do a sentence-by-sentence fact check against your sources before replying. Say in your reply that you
   did both, or say honestly which you skipped.
2. **Never add a fact no source supports.** For a translation, nothing beyond the English post (a Portuguese source may
   replace US context, never extend it). For a local-only post, every sentence of fact traces to a page you fetched today
   and saved, to the English posts named in your row, or to our app's facts (`_apps/<slug>.md`, `pt/apps/<slug>/index.md`,
   pt-glossary, the blueprint §10).
3. **Write from the facts, not from the French or German model.** The models show structure (sections, FAQ shape, how the
   app section and sources are written). A post rendered line by line from French is a calque and gets rewritten.

Also from the batch 1 tells (all in `_i18n/pt.md` «From the Tier 4 batch 1 reviews»): keywords must be real Google
Portugal suggestions (from the research row, or confirm one yourself with
`curl -s 'https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-PT&gl=pt&q=<query>'`); multi-word UI labels
in «», one-word labels bare; no comma before e/ou; U+00A0 before units, €, $ and «min»; keep the English first person where
a translated post has it (never gendered).

## Local-only front matter

```yaml
---
layout: journal
slug: <the Portuguese slug below>
permalink: /pt/journal/<slug>/
local_only: true
last_updated: 2026-11-19
date: 2026-11-19
title: "…"
seo: { title, description, keywords }
lede: "…"
quick_answer: "…"
excerpt: "…"
faq: [ { q, a } ]
mentioned_apps: [ <app slug(s)> ]
read_time: "N min de leitura"
---
```

No `ref`, no `translated_from`. The translated post (1RM) uses the batch 1 front matter (ref, translated_from = English
last_updated).

## Links

Portuguese journal posts that exist or are written in this batch (link them where the topic fits; at least one link to a
related batch 1 post where one fits):

- batch 1: `/pt/journal/how-many-steps-a-day-to-aim-for/`, `/pt/journal/how-long-to-rest-between-sets/`,
  `/pt/journal/choosing-a-strength-program-you-will-finish/`, `/pt/journal/when-to-deload/`,
  `/pt/journal/apple-watch-hrv-without-a-baseline/`, `/pt/journal/puppy-and-kitten-vaccination-schedule/`,
  `/pt/journal/how-much-to-tip-in-the-us/`, `/pt/journal/find-every-recurring-charge/`,
  `/pt/journal/puzzle-games-without-ads-or-lives/`, `/pt/journal/converter-mkv-para-mp4/`
- batch 2: `/pt/journal/how-to-estimate-your-one-rep-max/`, `/pt/journal/frequencia-cardiaca-em-repouso/`,
  `/pt/journal/sono-profundo/`, `/pt/journal/sono-rem/`, `/pt/journal/feriados-2027/`,
  `/pt/journal/sobrecarga-progressiva/`, `/pt/journal/series-por-musculo-por-semana/`, `/pt/journal/turnos-rotativos/`,
  `/pt/journal/desparasitar-gato-e-cao/`, `/pt/journal/extrair-audio-de-video/`

Everything else as in the batch 1 brief (`ls pt/guides pt/for pt/alternatives` for other Portuguese targets; English
targets with `{: hreflang="en"}` and «(em inglês)»).

## Keyword collisions (in addition to the batch 1 brief's list)

Batch 1 primaries are taken: `quantos passos por dia`, `quanto tempo descansar entre séries`, `treino ppl`, `semana de
deload`, `vfc baixa`, `vacinas gatos`, `vacinas cachorro`, `gorjeta nos estados unidos`, `como ver subscrições no iphone`,
`jogos sem anúncios`, `converter mkv para mp4`. Also `trabalho por turnos saúde` (/pt/for/shift-workers/),
`como dormir de dia quem trabalha à noite`, `dívida de sono` (AfterShift), `contagem decrescente iphone`, `app contador de
dias` (Soon.), `como fazer contagem decrescente no iphone` (countdown guide). Within this batch, sono profundo and sono
rem must not take each other's primary (each may name the other once).

## Sources

Save every fetched page into
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-NWyIpj/dc12c9e7-7c3a-4bcf-a153-f479639bd3fa/scratchpad/pt-t4b2/sources/<slug>/`
(one text file per source, URL on the first line). `curl -sL --compressed`, strip HTML with `python3 -I`. Quotes under
15 words; paraphrase the rest. A page you could not fetch is not a source. Portuguese official sources first (SNS 24
sns24.gov.pt, DGS dgs.pt, Diário da República diariodarepublica.pt, DGAV dgav.pt, ePortugal / gov.pt), then primary
studies and international bodies (WHO, ACSM, ESCCAP), then Apple's pt-pt support pages for Apple facts. Never a
commercial clinic or blog as the only source for a health number.

## Do NOT

As in the batch 1 brief: no build, no map, no stamp, no git; touch only your post and its sources folder. Other sessions
(nl, es, it, pt Tier 3) work in this checkout.

## Reply with

As in the batch 1 brief (path, seo.title + count, primary; every source used and the claims it supports; glossary gaps;
English-side or app-side issues; one /pt/llms.txt routing line), plus: whether you read and applied the skill file, and
whether you did the fact check.

---

## Per-post notes

| Post | Write to | Primary | Notes |
|---|---|---|---|
| how-to-estimate-your-one-rep-max (translation) | pt/journal/how-to-estimate-your-one-rep-max/index.md | `como calcular 1rm` | Secondaries: «1rm o que é», «calculadora 1rm», «como calcular 1rm fórmula», «fórmula brzycki» (check), «como calcular 1rm supino». English source `_journal/how-to-estimate-your-one-rep-max.md`; French template `fr/journal/how-to-estimate-your-one-rep-max/index.md` (it rebuilt examples in kg: recompute every example yourself with the formulas, show the inputs). GymLogger X labels from its glossary section (its pt text is largely Brazilian: nouns only). Lift names: supino, agachamento, peso morto. |
| local: frequência cardíaca em repouso | pt/journal/frequencia-cardiaca-em-repouso/index.md | `frequência cardíaca em repouso` | Secondaries: «frequência cardíaca em repouso normal», «… ideal», «… atletas», «… abaixo de 60», «… alta», «batimentos por minuto normal». YMYL: the normal range, athlete values, when to see a doctor ONLY from fetched SNS 24 / DGS / Fundação Portuguesa de Cardiologia / a cardiology society or WHO page; Apple's resting HR definition from Apple pt-pt (Apple Watch / app Saúde). Observa: resting HR as one of its readiness inputs, compared with the person's own baseline (pt/apps/observa, glossary; nouns only). «Não é um conselho médico». Models: fr frequence-cardiaque-au-repos, de ruhepuls-normalwerte. |
| local: sono profundo | pt/journal/sono-profundo/index.md | `sono profundo` | Secondaries: «sono profundo significado», «sono profundo tempo ideal», «quantas horas de sono profundo», «sono profundo baixo», «sono profundo e sono leve». YMYL: what deep sleep is, its share of the night, how it changes with age, recommended total sleep for adults ONLY from fetched sources (SNS 24 / DGS / a Portuguese sleep society / a sleep-medicine source such as the AASM or NIH pages); say plainly if no source sets a minimum. Apple's sleep stages from Apple pt-pt (Acordado, REM, essencial, profundo) and that the Apple Watch gives estimates. Observa / AfterShift only as their pages state. Model: fr sommeil-profond-combien-d-heures, de tiefschlaf-wie-viel. |
| local: sono REM | pt/journal/sono-rem/index.md | `sono rem` | Secondaries: «sono rem significado», «sono rem e não rem», «sono rem vs sono profundo», «sono rem ideal», «sono rem baixo». Same source rules as sono profundo. Model: fr sommeil-paradoxal. Link sono profundo once. |
| local: feriados 2027 | pt/journal/feriados-2027/index.md | `feriados 2027 portugal` | Secondaries: «feriados 2027», «pontes 2027», «feriados 2027 carnaval», «feriados 2027 lisboa» / «porto» / «açores» / «madeira» only if a fetched official page gives those holidays. The national list from Código do Trabalho art. 234 (and art. 235 for Carnaval and the municipal holiday as optional/facultative) as published on diariodarepublica.pt; Easter 2027 (28 March 2027) and the dates that move with it (Sexta-feira Santa, Páscoa, Corpo de Deus, Carnaval) computed and stated with the rule; the weekday of every 2027 date computed with Python and double-checked; «pontes» described only as the days between a holiday and a weekend (no claims about which employers grant them). Lisboa (Santo António) and Porto (São João) municipal holidays and the Açores and Madeira regional days only from fetched official municipal or regional pages, else leave them out. Soon.: an event per holiday as a countdown, with its widgets, only as pt/apps/soon and the glossary describe; the /pt/guides/como-fazer-contagem-decrescente-iphone/ link. Model: fr jours-feries-2027. |
| local: sobrecarga progressiva | pt/journal/sobrecarga-progressiva/index.md | `sobrecarga progressiva` | Secondaries: «sobrecarga progressiva como fazer», «princípio da sobrecarga progressiva», «progressão de carga treino», «treino sobrecarga progressiva». Facts from the ACSM 2009 position stand (fetch it) and the English posts double-progression-explained and choosing-a-strength-program (link the pt version of the latter). LiftLog and GymLogger X: only what blueprint §10 / the pt app pages state (I-0301: the progression engine and the overload score have no §10 rows: describe them only in the words the pt app pages already use). Models: fr surcharge-progressive-musculation, de progressive-overload. |
| local: séries por músculo por semana | pt/journal/series-por-musculo-por-semana/index.md | `quantas séries por músculo por semana` | Secondaries: «quantas séries por músculo», «quantas séries por músculo para hipertrofia», «séries por grupo muscular por semana», «quantas séries por treino». Facts from Schoenfeld et al. 2017 (dose-response meta-analysis) and the ACSM 2026 resistance-training position stand as fetched (the French model cites both; re-fetch and check every number). GymLogger X «Volume de séries (Pro)» per its pt page. Model: fr series-par-muscle-par-semaine. |
| local: turnos rotativos | pt/journal/turnos-rotativos/index.md | `turnos rotativos` | Secondaries: «turnos rotativos significado», «turnos rotativos como funciona», «turnos rotativos de 8 horas», «trabalho por turnos código do trabalho», «trabalho por turnos legislação». Law ONLY from the Código do Trabalho (Lei n.º 7/2009) as fetched from diariodarepublica.pt: arts. 220–222 (organização de turnos, rotation, «trabalho por turnos» definition), 214 (descanso diário of at least 11 consecutive hours, and its exceptions only as written), 223–225 (trabalho noturno). Do not state «depois dos 50 anos» rights unless the fetched text says so. Health and sleep facts from the English posts `_journal/rotating-shift-schedules-explained.md` (forward vs backward rotation, quick returns, cited studies) and `_journal/how-to-sleep-after-a-night-shift.md` (link both in English with the marker). AfterShift: rotation builder and what it tracks only from pt/apps/aftershift and the glossary (preset names exactly). /pt/for/shift-workers/ linked once. Models: es turnos-rotativos (structure only), fr travail-en-3x8. |
| local: desparasitar gato e cão | pt/journal/desparasitar-gato-e-cao/index.md | `desparasitar gato` + `desparasitar cão` | Secondaries: «desparasitar gatos de quanto em quanto tempo», «desparasitação interna e externa», «desparasitar cão de quanto em quanto tempo», «desparasitar gatos bebés». YMYL vet: intervals, ages, internal vs external, the 4-times-a-year baseline and risk-based schedules ONLY from fetched ESCCAP guidance (esccap.org; a Portuguese version if fetchable) and DGAV if it says anything; no product names, no doses, no medicine claims; «não substitui o conselho de um veterinário». Pawza: recurring reminders and the vet record only as pt/apps/pawza and the glossary state («Repetição», etc.). Link /pt/journal/puppy-and-kitten-vaccination-schedule/. Models: fr vermifuger-son-chien, de wurmkur-hund-wie-oft. |
| local: extrair áudio de vídeo | pt/journal/extrair-audio-de-video/index.md | `extrair áudio de vídeo` | Secondaries: «extrair áudio de vídeo mp3», «extrair áudio de vídeo grátis», «extrair áudio de vídeo mp4», «extrair áudio de vídeo iphone» (only if the post answers it). MediaKit's audio-extraction tool, its output formats, which tools are free for good and the free-days rule only from `_apps/mediakit.md`, pt/apps/mediakit, the glossary and the pt-PT catalog (tool names exactly). Online extractors: say only that they need the file uploaded. YouTube/Instagram extraction: say nothing about downloading others' content. Any Apple built-in route only from a fetched Apple pt-pt page. Link /pt/journal/converter-mkv-para-mp4/. Model: fr extraire-son-video-iphone. |
