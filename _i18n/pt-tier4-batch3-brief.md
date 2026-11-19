# Writer brief: Portuguese (pt, Portugal) Tier 4, batch 3 (3 translations, 7 local-only posts)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/pt-tier4-batch2-brief.md` first and follow all of it** (it points to `_i18n/pt-tier4-brief.md` and
`_i18n/pt-writer-brief.md`: read those too). Its three rules, local-only front matter, sources rules, Do NOT and Reply with all
apply. This file only changes the links, the collision list, the sources folder and the per-post rows. Also read the «From
the Tier 4 batch 1 reviews» and «From the Tier 4 batch 2 reviews» paragraphs in `_i18n/pt.md`: they list what reviewers
fixed most, including:

- app claims ONLY from the blueprint's claims register §10, `_apps/<slug>.md` and the pt app page, never from §4 or the
  code alone (batch 2 lost MediaKit's free audio route and Mute for this reason);
- one guideline version (the current English or Portuguese text), never another country's older national version;
- no hardened hedges, no editorial verdicts, no near-verbatim paraphrase of a source, no gloss from one source inside a table
  credited to another, no summary of another post you didn't use as a source, no own arithmetic in seo.description;
- a local-only post is roughly 1100 to 2200 words; it does not translate a long English post wholesale.

## Links

Portuguese journal posts that exist (batches 1 and 2) or are written in this batch:

- batch 1: `/pt/journal/how-many-steps-a-day-to-aim-for/`, `/pt/journal/how-long-to-rest-between-sets/`,
  `/pt/journal/choosing-a-strength-program-you-will-finish/`, `/pt/journal/when-to-deload/`,
  `/pt/journal/apple-watch-hrv-without-a-baseline/`, `/pt/journal/puppy-and-kitten-vaccination-schedule/`,
  `/pt/journal/how-much-to-tip-in-the-us/`, `/pt/journal/find-every-recurring-charge/`,
  `/pt/journal/puzzle-games-without-ads-or-lives/`, `/pt/journal/converter-mkv-para-mp4/`
- batch 2: `/pt/journal/how-to-estimate-your-one-rep-max/`, `/pt/journal/frequencia-cardiaca-em-repouso/`,
  `/pt/journal/sono-profundo/`, `/pt/journal/sono-rem/`, `/pt/journal/feriados-2027/`, `/pt/journal/sobrecarga-progressiva/`,
  `/pt/journal/series-por-musculo-por-semana/`, `/pt/journal/turnos-rotativos/`, `/pt/journal/desparasitar-gato-e-cao/`,
  `/pt/journal/extrair-audio-de-video/`
- batch 3: `/pt/journal/rpe-and-rir-explained/`, `/pt/journal/compress-a-video-for-email/`,
  `/pt/journal/double-progression-explained/`, `/pt/journal/aquecimento-antes-do-treino/`, `/pt/journal/pulgas-e-carracas/`,
  `/pt/journal/passaporte-animal-de-companhia/`, `/pt/journal/reduzir-tamanho-pdf-mac/`, `/pt/journal/abrir-ficheiro-rar/`,
  `/pt/journal/vo2-max/`, `/pt/journal/gorjeta-em-portugal/`

In a translated post, a link the English has to one of these English posts becomes the Portuguese URL (no marker).

## Keyword collisions (add to the batch 1 and 2 lists)

Batch 2 primaries are taken: `como calcular 1rm`, `frequência cardíaca em repouso`, `sono profundo`, `sono rem`, `feriados 2027
portugal`, `sobrecarga progressiva`, `quantas séries por músculo por semana`, `turnos rotativos`, `desparasitar gato`,
`desparasitar cão`, `extrair áudio de vídeo`. MediaKit keeps `comprimir vídeo iphone`, `comprimir pdf iphone`, `converter heic
para jpg`; the support hub keeps `cancelar subscrição iphone`; RightSplit keeps `dividir conta restaurante`; the US tipping post
keeps `gorjeta nos estados unidos`.

## Sources folder

`/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/dc12c9e7-7c3a-4bcf-a153-f479639bd3fa/scratchpad/pt-t4b3/sources/<slug>/`
(this replaces the batch 2 path). PubMed web pages block curl: use NCBI efetch
(`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=<PMID>&rettype=abstract&retmode=text`) or the PMC page.
diariodarepublica.pt returns an empty app shell to curl: pgdlisboa.pt carries consolidated law text.

---

## Per-post notes

| Post | Write to | Primary | Notes |
|---|---|---|---|
| rpe-and-rir-explained (translation) | pt/journal/rpe-and-rir-explained/index.md | `rir treino` | Secondaries: «rir treino significado», «o que significa rir no treino», «rpe e rir», «rpe treino» (check). English `_journal/rpe-and-rir-explained.md`; fr template. GymLogger X has no per-set RPE entry: keep the English wording on what it has (pt app page, glossary; nouns only). |
| compress-a-video-for-email (translation) | pt/journal/compress-a-video-for-email/index.md | `enviar vídeo grande por email` | Secondaries: «comprimir vídeo para email», «como enviar vídeo grande por email iphone», «… outlook». Mail limits exactly as English states them (Gmail, Outlook, iCloud Mail); Apple's Mail Drop by Apple Portugal's name and facts from a fetched support.apple.com/pt-pt page. «vídeo» with accent. MediaKit compress tool and presets per its pt page and §10. Recompute the bitrate arithmetic. |
| double-progression-explained (translation) | pt/journal/double-progression-explained/index.md | `dupla progressão` | Secondaries: «dupla progressão treino», «método progressão dupla», «progressão dupla». English `_journal/double-progression-explained.md`; fr template. ISSUES I-0438: the English says Plotkin 2022 had 38 lifters and gives +21.8 vs +19.3 kg, and attributes «two consecutive sessions» and smaller increases for small muscles to ACSM 2009. Fetch Plotkin 2022 (peerj.com/articles/14142, or PMC/efetch) and the ACSM 2009 abstract; write each figure as the source states it (and say in your reply what you changed and why). Link /pt/journal/sobrecarga-progressiva/ (it uses the abstract's 43). LiftLog: «Dupla progressão» and the scheme names per pt/apps/liftlog. Examples in kg (recompute). |
| local: aquecimento antes do treino | pt/journal/aquecimento-antes-do-treino/index.md | `aquecimento antes do treino` | Secondaries: «aquecimento antes do treino de musculação», «exercícios de aquecimento antes do treino», «como fazer aquecimento antes do treino». Facts from studies you fetch (the fr model cites a 2010 meta-analysis, a 2015 review and a 2014 trial: fetch and check each); warm-up sets per GymLogger X and LiftLog only as their pt pages state (both mark warm-up sets apart from volume and records: verify). Link the rest, sets-per-muscle and 1RM posts. Model fr echauffement-musculation. |
| local: pulgas e carraças | pt/journal/pulgas-e-carracas/index.md | `pulgas e carraças` | Secondaries: «pulgas e carraças cães», «pulgas e carraças gatos», «pulgas cão», «carraças cão», «carraça cão como tirar» (only if a source says how). YMYL vet: ESCCAP ectoparasite guidance (GL3, and the ESCCAP Portugal general-recommendations PDF already used for desparasitar), DGAV if relevant (Leishmania, ticks); diseases named only as sources name them; no product names, no doses, no brand («Bravecto» etc. never). «não substitui o conselho de um veterinário». Pawza reminders per the pt page and catalog (medication Repetição offers Diário/Semanal/Mensal; check). Link desparasitar and the vaccines post. Model fr puces-tiques-chien. |
| local: passaporte animal de companhia | pt/journal/passaporte-animal-de-companhia/index.md | `passaporte cão portugal` | Secondaries: «passaporte animal de companhia», «passaporte de animal de companhia da união europeia», «passaporte cão», «passaporte animal portugal». Rules only from Your Europe pt (already used in the vaccines post: microchip, rabies vaccine from 12 weeks, 21 days, EU passport) and DGAV pages you fetch (who issues it in Portugal, SIAC, travel outside the EU); no price unless an official page states one; say plainly what you could not source. Pawza: storing the passport scan / vet records only per its pt page. Link the vaccines post. Model fr passeport-europeen-chien-chat. |
| local: reduzir tamanho PDF no Mac | pt/journal/reduzir-tamanho-pdf-mac/index.md | `reduzir tamanho pdf mac` | Secondaries: «reduzir tamanho pdf», «reduzir tamanho pdf sem perder qualidade», «reduzir tamanho pdf macbook». Apple's built-in route (Pré-visualização, «Exportar», «Filtro Quartz», «Reduzir tamanho do ficheiro») ONLY as a fetched support.apple.com/pt-pt page states it. MediaKit PDF compression only per §10, `_apps/mediakit.md` and pt/apps/mediakit (tool name from the pt-PT catalog). Online tools: they need the file uploaded. Model fr compresser-pdf-mac. |
| local: abrir ficheiro RAR | pt/journal/abrir-ficheiro-rar/index.md | `abrir ficheiro rar` | Secondaries: «abrir rar mac», «abrir rar iphone», «abrir ficheiro rar mac», «abrir ficheiro rar iphone». What macOS's built-in Utilitário de Arquivo / Ficheiros on iPhone open, ONLY from a fetched Apple pt-pt page (say plainly if a page says nothing about RAR). MediaKit's archive support only per §10, `_apps/mediakit.md` and pt/apps/mediakit; if §10 doesn't list RAR, MediaKit gets no RAR claim. Online tools: upload. Model fr ouvrir-fichier-rar-mac-iphone. |
| local: VO2 máx. | pt/journal/vo2-max/index.md | `vo2 max` | Secondaries: «vo2 max o que é», «vo2 max valores de referência», «vo2 max apple watch», «vo2 max tabela» (only if a source gives a table). Definition and units from a fetched authoritative source; Apple's cardiofitness (VO2 máx.) from Apple pt-pt pages (which Watch models, outdoor walk/run/hike, levels); the Apple validation white paper as the fr model cites it (fetch and check every number). Observa only per pt/apps/observa and the glossary («cardiofitness (VO2 máx.)» card name exactly). «não é um conselho médico». Model fr vo2-max, de vo2max-apple-watch. |
| local: gorjeta em Portugal | pt/journal/gorjeta-em-portugal/index.md | `gorjeta em portugal` | Secondaries: «gorjeta em portugal é obrigatória», «tem gorjeta em portugal», «gorjeta em portugal como se diz», «gorjeta portugal restaurante». CONDITION: write this post only if you fetch at least one official or legal Portuguese source that says something about tips or service charges (Portal do Consumidor / Direção-Geral do Consumidor, ASAE on «couvert» and service charges, Diário da República on prices shown including taxes, VisitPortugal / Turismo de Portugal). Say only what those pages say; no customary percentages from memory or blogs. If no such source can be fetched, do NOT write the file: reply saying so, with the URLs you tried. RightSplit: tip presets and «Arredondar com justiça» per pt/apps/rightsplit; link the US tipping post. |
