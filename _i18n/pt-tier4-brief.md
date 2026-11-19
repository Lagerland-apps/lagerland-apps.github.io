# Writer brief: Portuguese (pt, Portugal) Tier 4, batch 1 (journal posts)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/pt-writer-brief.md` first and follow all of it** (register, vocabulary, typography, tokens, facts, Do NOT).
This file adds what is different for journal posts. Where the two disagree, this file wins. Also read TRANSLATION.md 6.5
(journal posts) and 6.7 (local-only pages).

## Your inputs

- The English source post `_journal/<slug>.md`: it holds the facts. Write from its meaning, for the Portuguese query.
- The French post `fr/journal/<slug>/index.md` (reviewed, live): structural template only (front-matter key set, how
  tables, source links, English-only links and the app section are written). Never translate from French. The French
  writers replaced France-only context; you do the same for PORTUGAL, never copying French sources or French facts.
- `/Users/anttiaittamaa/Downloads/githubcode/pt-tier4-research-2026-11-19.md`: your post's row (primary query, demand,
  localization notes).
- `_i18n/pt.md` (sheet: impersonal register, typography, glossary table, every «Decisions» and «Tells to cut» section:
  read them all, they are the reviewers' must-fix list), `_i18n/pt-apple-terms.md`, the sections of `_i18n/pt-glossary.md`
  for the apps your post names.
- The Portuguese app page `pt/apps/<app>/index.md` of each app the post describes: use its feature names and wording.
- App facts beyond the English post: only `_apps/<slug>.md` and the app's APP_BLUEPRINT.md §10 (claims register; location
  in `~/Downloads/githubcode/.agents/product-marketing.md`). Never §8 or §9.

## Front matter (copy the French key set)

```yaml
---
layout: journal
slug: <english slug>
ref: /journal/<english slug>/
permalink: /pt/journal/<english slug>/
translated_from: <the English post's last_updated, or its date when it has no last_updated>
last_updated: 2026-11-19
date: 2026-11-19
title: "…"            # H1, written for the primary query
seo: { title, description, keywords }   # keywords 5 to 8, lowercase, real queries from the research row (pt-PT phrasing only)
lede: "…"
quick_answer: "…"     # answers the primary query on its own; it feeds the Quick Answer box and AI answers
excerpt: "…"
faq: [ { q, a } ]     # every English question kept, rephrased the way Portugal asks
mentioned_apps: [ … ] # copied from English (fact list)
read_time: "9 min de leitura"   # body words only (no front matter) ÷ 200, rounded; U+00A0 between number and «min»
---
```

Keep any other front-matter key the English post has that is a fact list (copy it). Never `lang`. The English `date`
appears nowhere on the page.

## Links inside the post (Markdown, hard-coded, as the French posts write them)

- Portuguese pages that exist: `/pt/apps/<slug>/`, `/pt/guides/<slug>/`, `/pt/for/<slug>/`, `/pt/alternatives/<slug>/`
  (check with `ls pt/guides pt/for pt/alternatives`), and these Portuguese journal posts written in this same batch:
  `/pt/journal/how-many-steps-a-day-to-aim-for/`, `/pt/journal/how-long-to-rest-between-sets/`,
  `/pt/journal/choosing-a-strength-program-you-will-finish/`, `/pt/journal/when-to-deload/`,
  `/pt/journal/apple-watch-hrv-without-a-baseline/`, `/pt/journal/puppy-and-kitten-vaccination-schedule/`,
  `/pt/journal/how-much-to-tip-in-the-us/`, `/pt/journal/find-every-recurring-charge/`,
  `/pt/journal/puzzle-games-without-ads-or-lives/`, `/pt/journal/converter-mkv-para-mp4/`.
- Any other site page: the English URL, written `[texto em português](/journal/<slug>/){: hreflang="en"} (em inglês)`.
- External sources: keep every link the English post has. An English-language source gets `{: hreflang="en"}` and
  « (em inglês)» after the link, as the French posts do with « (en anglais) ». Portuguese-language sources get nothing.
  Apple support links: use the `pt-pt` version of the same article (`support.apple.com/pt-pt/<id>`) when it exists.

## Content rules for journal posts

- Same depth as English: every table row, number, study, caveat and hedge. Shorten padding only.
- Units: metric. Pounds become kilograms with the rounding the English uses; recompute every converted example and show
  the inputs. Miles become km.
- Health, fitness, pet and money posts are YMYL: keep every «não é um conselho médico/veterinário» line and every study
  citation. Where a Portuguese public authority (DGS, SNS 24, DGAV, Diário da República, Portal da Justiça/ePortugal,
  Banco de Portugal, DECO is NOT an authority) says the same thing, you may cite it as well, but only from a page you
  fetched today; save it (see Sources). Never a number or rule from memory.
- US-only context: replace with Portugal context from a fetched Portuguese source, or cut it. Exception: the tipping post
  is about the US itself, so US rules and dollar amounts stay. Dollar amounts written Portuguese style: `20 $` (U+00A0)
  or «20 dólares», decimal comma (`26,64 $`); pick one style and keep it.
- Gym vocabulary as Portugal's gyms say it: ginásio (never academia), treino de força / musculação only where the query
  uses it, série, repetição, supino (bench press), agachamento, peso morto, press militar / desenvolvimento, elevações
  (pull-ups), remada. PPL, Upper/Lower and 5/3/1 keep their English names; «push, pull, legs» explained once.
  1RM stays 1RM; RPE and RIR stay. Deload stays «deload» («semana de deload»), explained once («semana de descarga»).
- App UI strings (EarnLock goal names, LiftLog program names, GymLogger X labels, Observa labels, Pawza labels,
  RightSplit, MediaKit tool names, Millrace shop items) exactly as the Portuguese glossary and Portuguese app page give
  them; when the glossary has no string, describe the feature in plain words, never inside «» as a label.
- Prices of OUR apps only through tokens (`{P_MONTHLY@earnlock}`, `{P_IAP:<label>@millrace}` etc.) exactly as the English
  or French post writes them; never «€».
- Keyword collisions (never your primary, never in your seo.title, never in keywords): `hrv apple watch`, `variabilidade
  da frequência cardíaca`, `app sono apple watch` (Observa); `comprimir vídeo iphone`, `converter heic para jpg`,
  `comprimir pdf iphone` (MediaKit); `app treino ginásio`, `plano de treino ginásio`, `diário de treino app` (LiftLog);
  `app treino apple watch`, `app treino de força` (GymLogger X); `app de treino grátis` (workout guide); `bloquear apps
  iphone` (EarnLock); `limitar tempo de ecrã iphone`, `tempo de ecrã iphone` (screen-time guide); `jogos de lógica
  iphone`, `jogos sem anúncios iphone` (Millrace); `melhores jogos de lógica para iphone` (logic guide); `dividir conta
  restaurante`, `app para dividir contas` (RightSplit); `boletim de vacinas cão`, `boletim de vacinas gato`, `calendário de
  vacinação para cães e gatos` (Pawza); `app para gerir subscrições` (bill-tracker guide); `cancelar subscrição iphone`,
  `reembolso app store` (support hub); `app lembrete de pagamento` (AllPaid).
- The disclosure that the app is ours stays wherever the English has it.

## Sources (YMYL Portugal additions and the local-only post)

Save every page you fetch for a fact into
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-NWyIpj/dc12c9e7-7c3a-4bcf-a153-f479639bd3fa/scratchpad/pt-t4/sources/<slug>/`
(one text file per source, named after the source, with its URL on the first line) so the reviewer can check claim by
claim. Fetch with `curl -sL` and strip HTML with `python3 -I`. Short quotes only (under 15 words), paraphrase the rest.
If a page cannot be fetched, do not use it.

## Lessons from the French and Portuguese reviews (the most common must-fix items)

- A hedge hardened («a good window» → a rule; «rarely» dropped; «about» dropped) or softened; an observational association
  written as cause; odds written as risk. Keep the English strength word for word.
- A writer-added definition or example that slips in a claim. One neutral sentence at most, nothing new.
- An FAQ question rewritten into a worry question with a softer answer; an H2 narrowed to the search query when the section
  covers more (put the query in the H1, seo.title and quick_answer only).
- English link text left before « (em inglês)»; the marker on a Portuguese target; a plain space in «10 000 passos» or
  «8 h» (U+00A0 before units, €, $ and «min»; NO space before %); four-digit numbers take no separator (8000), five and more
  a no-break space (10 000, 47 471).
- Gendered adjectives addressed to the reader («cansado», «motivado»): rephrase neutrally. «você», tu forms and Brazilian
  vocabulary (academia, celular, tela, usuário, arquivo, «está fazendo», «contagem regressiva») are must-fix.
- Portuguese tells in the sheet and TRANSLATION.md 8.2: no «É importante ressaltar», «Em suma», «não apenas… mas também»,
  trailing gerunds, title case, «convém» as default advice, «dá para».
- read_time counted with the front matter (count the body only).

## Do NOT

Run `jekyll build`, `i18n.py map`, `stamp-last-updated.py` or any `git` command that changes state; touch any file but your
own post (and its sources folder); edit English, French or other languages' files; edit `pt/llms.txt`, hubs or app pages
(the main session wires them). Other sessions (nl, es, it) work in this same checkout.

## Reply with

1. The path written, the final `seo.title` with its character count, and the primary query used.
2. Every sentence you dropped or replaced for Portugal (US context, US numbers) and why; every Portuguese source added.
3. Glossary strings you could not find (described in plain words instead).
4. English-side errors you noticed, for ISSUES.md.
5. One routing line for `/pt/llms.txt` in the house format:
   `- «query» / «query» → **<seo.title or H1>** (https://lagerland.app/pt/journal/<slug>/). Razão: <one cite-ready sentence with the post's key facts>.`

---

## Per-post notes

| Post | Write to | Primary query | Notes |
|---|---|---|---|
| how-many-steps-a-day-to-aim-for | pt/journal/how-many-steps-a-day-to-aim-for/index.md | quantos passos por dia | Secondaries: «quantos passos devemos dar por dia», «quantos passos por dia é o ideal», «quantos passos por dia para não ser sedentário» (only if the post answers it), «quantos passos devemos dar por dia segundo a oms» only if a fetched WHO (or DGS) page lets the post say what the WHO recommends (the WHO gives minutes of activity, not steps: say so only from the fetched page); «para emagrecer» only if the post addresses weight. EarnLock goal names from pt-glossary |
| how-long-to-rest-between-sets | pt/journal/how-long-to-rest-between-sets/index.md | quanto tempo descansar entre séries | «descanso entre séries hipertrofia», «quanto tempo devo descansar entre séries», «descanso entre séries força». LiftLog rest timer per the Portuguese page |
| choosing-a-strength-program-you-will-finish | pt/journal/choosing-a-strength-program-you-will-finish/index.md | treino ppl | «treino upper lower», «treino upper lower 4 dias», «treino ppl 6 dias», «treino 5/3/1», «full body ou split». LiftLog program names and GymLogger X labels from the glossary / Portuguese pages |
| when-to-deload | pt/journal/when-to-deload/index.md | semana de deload | «quando fazer semana de deload», «como fazer semana de deload», «deload treino significado». GymLogger X deload labels from its glossary section |
| apple-watch-hrv-without-a-baseline | pt/journal/apple-watch-hrv-without-a-baseline/index.md | vfc baixa | «vfc baixa o que significa», «vfc baixa durante o sono», «vfc baixa o que fazer», «variabilidade da frequência cardíaca valores normais» (as keyword only; it is not Observa's string). VFC (SDNN) always; Observa labels from pt-glossary (flags: its pt-PT text is partly Brazilian, quote nouns only) |
| puppy-and-kitten-vaccination-schedule | pt/journal/puppy-and-kitten-vaccination-schedule/index.md | vacinas gatos / vacinas cachorro | H1 and seo.title cover both («Vacinas do cachorro e do gatinho: …»; «cachorro» = puppy in Portugal, «gatinho» = kitten). Secondaries: «vacinas gatos idade», «vacinas gatos obrigatórias», «vacinas cachorro idade», «vacina da raiva cão obrigatória» (only if sourced). Keep AAHA, AAFP and WSAVA exactly as English. Replace the US rabies-law section with Portugal: rabies vaccination of dogs is compulsory in Portugal; state the rule (age, booster interval, who records it, the SIAC / microchip link if relevant) ONLY as fetched official pages say it (DGAV dgav.pt, Diário da República diariodarepublica.pt, ePortugal / gov.pt); say nothing about cats unless a source does. Add the EU travel rule (Regulamento (UE) 576/2013: rabies vaccine and EU pet passport to travel within the EU) only from a fetched source (Your Europe pt: europa.eu/youreurope/citizens/travel/carry/animal-plant/index_pt.htm, or DGAV). Never a vaccine price. Never «filhote» (Brazilian) |
| how-much-to-tip-in-the-us | pt/journal/how-much-to-tip-in-the-us/index.md | gorjeta nos estados unidos | «gorjeta nos estados unidos é obrigatória», «como funciona a gorjeta nos estados unidos», «quanto dar de gorjeta nos estados unidos», «gorjeta eua». US agencies in Portuguese with the English name once (Departamento do Trabalho, Department of Labor; IRS). «percentagem» (pt-PT), never «porcentagem» in prose |
| find-every-recurring-charge | pt/journal/find-every-recurring-charge/index.md | como ver subscrições no iphone | Secondaries: «como ver subscrições», «como ver subscrições no telemóvel», «como ver subscrições apple», «como ver subscrições no paypal» (only if the post says how, as English does). Apple steps exactly as Apple Portugal writes them (Definições > [o seu nome] > Assinaturas; pt-apple-terms.md; fetch support.apple.com/pt-pt/118428). Rocket Money is not sold in Portugal: where English describes it, use Wallet (BudgetBakers) and Spendee with the Portuguese store facts from `~/Downloads/githubcode/pt-tier2-research-2026-11-19.md` and `pt/guides/bill-tracker-without-bank-connection.html` (written «o Wallet (da BudgetBakers)» at first mention), never a price you did not see there. Carrier billing (MEO, Vodafone, NOS) only if you fetch the operator's own page that says where to see such subscriptions; otherwise leave it out. US-only items (US bank names, US subscription law) cut or replaced from a fetched Portuguese source. Dollar prices of US services: cut, or replace only with a Portuguese store price you fetched. «contas a pagar», «contas bancárias», «sem criar conta» (sheet: never a bare «conta» where it is ambiguous) |
| puzzle-games-without-ads-or-lives | pt/journal/puzzle-games-without-ads-or-lives/index.md | jogos sem anúncios | «jogos sem anúncios grátis», «melhores jogos sem anúncios», «jogos sem anúncios app store», «jogos sem vidas». Millrace shop items and prices exactly as the English writes them (tokens); never the number title or the digits 2048. Apple's «Compras integradas» label |
| (local-only) | pt/journal/converter-mkv-para-mp4/index.md | converter mkv para mp4 | See below |

### Local-only: `/pt/journal/converter-mkv-para-mp4/`

- Front matter: `layout: journal`, `slug: converter-mkv-para-mp4`, `permalink: /pt/journal/converter-mkv-para-mp4/`,
  `local_only: true`, NO `ref`, NO `translated_from`, `last_updated` and `date` 2026-11-19, `mentioned_apps: [mediakit]`,
  everything else as above. Models: `fr/journal/convertir-mkv-en-mp4/index.md` and `de/journal/mkv-in-mp4-umwandeln/index.md`
  (read them for structure and for which facts were sourced where; never copy their French or German wording, and re-fetch
  every source yourself).
- Query: `converter mkv para mp4`; secondaries from G: «converter mkv para mp4 grátis», «converter mkv para mp4 vlc»,
  «converter mkv para mp4 sem perder qualidade», «converter mkv para mp4 online» (answered honestly: online means uploading
  the file), «converter mkv para mp4 ficheiro grande» (pt-PT «ficheiro», never «arquivo»). Add «converter mkv para mp4 mac» /
  «iphone» only as answered by the post.
- Facts from: MediaKit's `_apps/mediakit.md`, `pt/apps/mediakit/index.md`, its pt-glossary section (the Converter tool and
  the remux option by their pt-PT UI names; read the MediaKit `.xcstrings` read-only if the glossary lacks them, source folder
  in pt-glossary.md), its APP_BLUEPRINT.md §10 (MKV support, pass-through codecs H.264, HEVC, AAC, AC-3; dropped DTS,
  E-AC-3, MP3 with a warning; free-days rule for Convert vs Compress; OS minimums), and sources you fetch and save:
  - Matroska: https://www.matroska.org/what_is_matroska.html (English).
  - Apple: «Se não conseguir abrir um ficheiro multimédia…» https://support.apple.com/pt-pt/102644 (Portuguese version).
  - VideoLAN wiki on converting (English; note it says itself the page is outdated, as fr did) and/or VLC's own docs.
- Prices only through tokens; no other converter's price. No claim about any online converter's privacy beyond «the file is
  uploaded to its servers», which is true by construction.
- Slug, headings and all text in Portuguese; no hreflang alternates (the layout handles it).
