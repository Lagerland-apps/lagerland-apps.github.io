# Writer brief: Portuguese (pt, Portugal) Tier 4, batch 4 (10 local-only posts)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/pt-tier4-batch3-brief.md` first and follow all of it** (it points to the batch 2 brief, `_i18n/pt-tier4-brief.md`
and `_i18n/pt-writer-brief.md`: read those too). Every rule there applies: the three rules, local-only front matter, sources,
Do NOT, Reply with. Also read the «From the Tier 4 batch 1/2/3 reviews» paragraphs in `_i18n/pt.md`: they are the reviewers'
must-fix list. The most common batch 3 fixes:

- claims taken from a blueprint's §4 or the code instead of §10, `_apps/<slug>.md` or the pt app page; UI names a brief suggested
  but nobody checked in the app's catalog or code (always check);
- dropped hedges («normalmente», «podem», «como por exemplo»), invented absolutes, warnings widened beyond the source;
- meta lines about what the page does or refuses to do, staged openers, headings that announce an absence, editorial verdicts;
- a source credited to one of its joint authors; a list's condition generalised to every item;
- «e-mail» in prose (keywords as typed); «o VO2 máx.»; «o 1RM»; one-word UI labels bare, multi-word in «».

All ten posts are local-only (no English twin): front matter as in the batch 2 brief, `local_only: true`, no `ref`, no
`translated_from`, `date` and `last_updated` 2026-11-19. Roughly 1100 to 2000 words each.

## Links

All Portuguese journal posts in `pt/journal/` (run `ls pt/journal`) plus this batch's:
`/pt/journal/frequencia-respiratoria-normal/`, `/pt/journal/saturacao-de-oxigenio-normal/`,
`/pt/journal/zonas-de-frequencia-cardiaca/`, `/pt/journal/leishmaniose-cao/`, `/pt/journal/vacina-raiva-gato/`,
`/pt/journal/regras-do-xadrez/`, `/pt/journal/juntar-pdf-mac/`, `/pt/journal/cafeina-quanto-tempo-dura/`,
`/pt/journal/ciclo-circadiano/`, `/pt/journal/quantos-dias-faltam-para-o-natal/`.
Link pointers only: never summarise another post you didn't use as a source.

## Keyword collisions (add to batches 1 to 3)

All batch 1 to 3 primaries are taken (see `_i18n/pt.md` «Tier 4 keywords»). Also: Chessful keeps `app xadrez`; the chess guide
keeps `melhor app de xadrez`; Observa keeps `hrv apple watch`, `app sono apple watch`; the countdown guide keeps `como fazer
contagem decrescente no iphone`; Soon. keeps `contagem decrescente iphone`, `app contador de dias`; MediaKit keeps `comprimir pdf
iphone`; AfterShift keeps `como dormir de dia quem trabalha à noite`, `dívida de sono`.

## Sources folder

`/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/dc12c9e7-7c3a-4bcf-a153-f479639bd3fa/scratchpad/pt-t4b4/sources/<slug>/`
(this replaces the batch 3 path). PubMed via NCBI efetch; diariodarepublica.pt via pgdlisboa.pt; PDFs: the Swift PDFKit extractor
at `/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/dc12c9e7-7c3a-4bcf-a153-f479639bd3fa/scratchpad/pt-t4b3/pdftxt`
(usage: `pdftxt file.pdf > file.txt`). Models (structure only; never translate them, re-fetch every source): the es, it and fr
posts named per row.

---

## Per-post notes

| Post | Write to | Primary | Notes |
|---|---|---|---|
| frequência respiratória normal | pt/journal/frequencia-respiratoria-normal/index.md | `frequência respiratória normal` | Secondaries: «frequência respiratória normal adulto», «… durante o sono», «… por idade». YMYL: normal adult range, children by age only if a source gives it, when to see a doctor, ONLY from fetched SNS 24 / DGS / a medical reference (MSD Manual, NHLBI, MedlinePlus); Apple's respiratory rate in Saúde (measured during sleep with Apple Watch) from Apple pt-pt pages. Observa only per pt/apps/observa, `_apps/observa.md` and the catalog (check whether Observa uses respiratory rate at all; if not, say only that it reads Saúde data or keep it out of mentioned_apps). «não é um conselho médico». Model es frecuencia-respiratoria-normal. mentioned_apps [observa]. |
| saturação de oxigénio normal | pt/journal/saturacao-de-oxigenio-normal/index.md | `saturação de oxigénio normal` | Secondaries: «saturação de oxigénio normal em adultos», «… durante o sono», «… em idoso». YMYL: normal SpO2 range and low thresholds ONLY from fetched SNS 24 / DGS / medical reference; Apple's «Oxigénio no sangue» app: which models, regions and availability ONLY as Apple Portugal's pages state (it is not a medical device; availability has changed: say only what the fetched page says). Observa per its page and catalog (same check). Models es saturacion-de-oxigeno-normal, it saturazione-apple-watch. mentioned_apps [observa]. |
| zonas de frequência cardíaca | pt/journal/zonas-de-frequencia-cardiaca/index.md | `zonas de frequência cardíaca` | Secondaries: «zonas de frequência cardíaca por idade», «… corrida», «… calculadora», «zonas de treino frequência cardíaca». Apple Watch heart-rate zones in the Treino app (how calculated, manual zones) only from Apple pt-pt pages; any max-HR formula (220 − idade, Tanaka) only with a fetched source and stated as an estimate; worked example by age computed with python. Observa / GymLogger X only if their pt pages state something about zones (check; otherwise mentioned_apps [observa] with a minimal, supported line, or the app the pages support). Model es zonas-de-frecuencia-cardiaca. |
| leishmaniose no cão | pt/journal/leishmaniose-cao/index.md | `leishmaniose cão` | Secondaries: «leishmaniose cão sintomas», «leishmaniose cão tratamento», «leishmaniose cães tem cura», «leishmaniose cães vacina», «leishmaniose cão para humano». YMYL vet: DGAV leishmaniose page (endemic in Portugal, Phlebotomus, not transmitted directly between dog and human as DGAV states, annual testing at the rabies campaign), ESCCAP (GL5 or the ESCCAP Portugal PDF: monthly repellents in endemic areas); symptoms, treatment and vaccine statements ONLY as fetched sources state them; no product names, no doses. Consistent with pt/journal/pulgas-e-carracas and desparasitar-gato-e-cao. Pawza per its pt page. Model es leishmaniosis-perro. mentioned_apps [pawza]. |
| vacina da raiva no gato | pt/journal/vacina-raiva-gato/index.md | `vacina raiva gato` | Secondaries: «vacina raiva gatos idade», «vacina raiva gato quanto tempo», «vacina raiva gato gratuita», «vacina raiva gato valor» (answer honestly: no official price). DGAV: rabies vaccination voluntary for cats in Portugal; campaign; travel within the EU requires it (Your Europe: 12 weeks, 21 days, microchip first); islands rule for cats per DGAV. Consistent with pt/journal/puppy-and-kitten-vaccination-schedule and passaporte-animal-de-companhia (re-read them). AAFP/AAHA feline guidance only as the vaccines post already cites it (re-fetch). Pawza per its pt page. mentioned_apps [pawza]. |
| regras do xadrez | pt/journal/regras-do-xadrez/index.md | `regras do xadrez` | Secondaries: «regras do xadrez movimento das peças», «regras do xadrez para iniciantes», «como jogar xadrez», «regras do xadrez cavalo». FIDE Laws of Chess (fetch the current handbook page; article numbers as FIDE gives them): board, pieces and moves, castling, en passant, promotion, check, checkmate, stalemate, draws (50 moves, threefold repetition, insufficient material). Portuguese chess terms as Portuguese sources use them (roque, en passant / tomada en passant, promoção, xeque, xeque-mate, afogamento / rei afogado: check a Portuguese source such as the Federação Portuguesa de Xadrez or a Portuguese FIDE translation; never Brazilian forms). Chessful per its pt page (catalog for UI names). Model es reglas-del-ajedrez. mentioned_apps [chessful]. |
| juntar PDF no Mac | pt/journal/juntar-pdf-mac/index.md | `juntar pdf mac` | Secondaries: «juntar pdf», «como juntar vários pdf mac», «juntar pdf macbook». Apple's Pré-visualização steps to combine PDFs ONLY from a fetched support.apple.com/pt-pt page (labels exactly). MediaKit: PDF merge only if §10, `_apps/mediakit.md` or pt/apps/mediakit state it (check; the blueprint's §4 is not enough), tool name from the pt-PT catalog, free/Pro status per the pt page, prices via tokens. Online tools: upload only. Link reduzir-tamanho-pdf-mac. Model es unir-pdf-mac. mentioned_apps [mediakit]. |
| cafeína: quanto tempo dura | pt/journal/cafeina-quanto-tempo-dura/index.md | `cafeína quanto tempo dura` | Secondaries: «cafeína quanto tempo dura no corpo», «quanto tempo dura o efeito da cafeína», «quanto tempo dura cafeína no sangue». Half-life and safe intakes ONLY from fetched sources (EFSA Scientific Opinion on the safety of caffeine 2015; a Portuguese official page if one exists, e.g. SNS 24 / DGS / ASAE; a pharmacology reference for half-life ranges); pregnancy and other cautions at source strength; the shift-work caffeine timing as pt/journal/turnos-rotativos and the English night-shift post state it (link, don't summarise). AfterShift's caffeine cut-off reminder per pt/apps/aftershift and the catalog. «não é um conselho médico». mentioned_apps [aftershift]. |
| ciclo circadiano | pt/journal/ciclo-circadiano/index.md | `ciclo circadiano` | Secondaries: «ciclo circadiano do sono», «ciclo circadiano como regular», «ritmo circadiano». Definition, light, melatonin, shift work and jet lag ONLY from fetched sources (NIH NIGMS circadian rhythms fact sheet, a Portuguese official or university source if fetchable, the English night-shift and rotating-shift posts for shift-work facts); no supplement advice. AfterShift per its pt page. Link turnos-rotativos. «não é um conselho médico». mentioned_apps [aftershift]. |
| quantos dias faltam para o Natal | pt/journal/quantos-dias-faltam-para-o-natal/index.md | `quantos dias faltam para o natal` | Secondaries: «quantos dias faltam para o natal em portugal», «quantos dias faltam para o natal de 2026», «… 24 de dezembro». No live counter (static page): explain the date arithmetic, give the count from a few fixed dates (computed with python: e.g. from 1 December 2026, 1 November 2026) and note that 24 de dezembro is one day fewer; 25 December 2026 weekday computed; Natal is a national holiday per art. 234 (link pt/journal/feriados-2027, which covers 2027). Soon.: an event per date, widgets, free limits only per pt/apps/soon and `_apps/soon.md`; link the countdown guide. Models es cuantos-dias-faltan-para-navidad, fr compte-a-rebours-noel. mentioned_apps [soon]. |
