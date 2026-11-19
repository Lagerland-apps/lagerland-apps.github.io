# Language sheet: Portuguese (pt), Portugal

Never published (`_i18n` is excluded from the build). Rulebook: TRANSLATION.md. Read this sheet before writing or
reviewing any Portuguese page. Every decision a translator would otherwise make differently per page lives here.

## Status

| Item | Status |
|---|---|
| Setup (config default, locales.yml block, `_data/i18n/pt.yml`, sitemap and feed stubs) | done 2026-11-19 (pt.yml written by one agent, reviewed and copy-edited by another: 38 values changed) |
| Keyword research (Tier 1) | done 2026-11-19 from Google suggest, Bing, App Store hints and the iTunes Search API; Search Console for Portugal not read (Claude in Chrome not connected, built-in browser not signed in, no export on disk) |
| Tier 1 pages | written and reviewed 2026-11-19, no native review yet: home, apps hub, 21 app pages (Clippet unlisted), 21 support pages, 21 privacy policies + Clippet terms, about, support hub, transparency (+ `_data/i18n_transparency/pt.yml`). AI files and OG cards in batch 6 (/pt/llms.txt, /pt/llms-full.txt, 21 OG cards) |
| Live | yes, `live: true` since 2026-11-19 (Tier 1; go-live commit not yet pushed) |
| Tier 2 | batch 1 written and reviewed 2026-11-19, no native review yet: both hubs, chess, logic, workout and xiangqi guides, 3 /for/ pages, local-only /pt/guides/limitar-tempo-de-ecra-iphone/. Batch 2 (same day): shogi guide, bill tracker rewritten around Wallet (BudgetBakers) and Spendee (the two apps sold in Portugal whose own listing says they connect to the bank; Portugal has no single default like Fintonic), local-only /pt/guides/como-fazer-contagem-decrescente-iphone/. Tier 2 complete; for/indie-ios-developers stays English-only. Research: ~/Downloads/githubcode/pt-tier2-research-2026-11-19.md; briefs `_i18n/pt-tier2-brief.md`, `_i18n/pt-tier2-review-brief.md` |
| Tier 3 | batch 1 written and reviewed 2026-11-19, no native review yet: hub /pt/alternatives/ and 10 comparisons (WHOOP, Oura, Splitwise, Tricount, Hevy, Chess.com, Lichess, PDF Expert, Forest, Opal). No local-only comparison: no Portugal-born competitor has demand (the gap found is a guide, `app para dividir despesas`). Research: ~/Downloads/githubcode/pt-tier3-research-2026-11-19.md; store data ~/Downloads/githubcode/pt-tier3-store-2026-11-19.md; briefs `_i18n/pt-tier3-brief.md`, `_i18n/pt-tier3-review-brief.md`. Batch 2 (same day): Documents by Readdle, Bevel, AutoSleep, Gentler Streak, Strong, Fitbod, one sec, ScreenZen, RISE, Habitica; hub now 20; store data ~/Downloads/githubcode/pt-tier3-store-batch2-2026-11-19.md; brief `_i18n/pt-tier3-batch2-brief.md`. Batch 3 (same day): Flow Free, Two Dots, KAMI 2 (first Millrace comparisons), Productive, Streaks, HandBrake, CloudConvert, Welltory, Jefit, Settle Up; hub now 30; store data ~/Downloads/githubcode/pt-tier3-store-batch3-2026-11-19.md; brief `_i18n/pt-tier3-batch3-brief.md`. Next candidates in the research file |
| Tier 4 | batch 1 written and reviewed 2026-11-19, no native review yet: hub /pt/journal/ («Blog») and 10 posts: how-many-steps-a-day-to-aim-for, how-long-to-rest-between-sets, choosing-a-strength-program-you-will-finish, when-to-deload, apple-watch-hrv-without-a-baseline, puppy-and-kitten-vaccination-schedule (Portugal rabies rule from DGAV, EU travel rule from Your Europe), how-much-to-tip-in-the-us, find-every-recurring-charge (Rocket Money replaced with Wallet and Spendee from their Portuguese listings), puzzle-games-without-ads-or-lives and the local-only /pt/journal/converter-mkv-para-mp4/. Inbound links from the workout, bill-tracker, logic-puzzle and screen-time guides, /pt/for/apple-health-power-users/ and /pt/alternatives/handbrake/. Research: ~/Downloads/githubcode/pt-tier4-research-2026-11-19.md (next candidates there); briefs `_i18n/pt-tier4-brief.md`, `_i18n/pt-tier4-review-brief.md` |
| Native review | none (NATIVE REVIEWER: none). Every page is logged as "no native review yet" |
| Build time | 72 s before Portuguese (main at the setup, 2026-11-19, other sessions' agents running); 85 s with Portuguese Tier 1 (762 audited pages) |

## Market and register

- Market: Portugal. Folder `/pt/`, `<html lang="pt-PT">`, hreflang `pt-PT` plus the bare `pt` until `/pt-br/` exists
  (TRANSLATION.md 2: moving the bare tag later changes only hreflang, never a URL), og:locale `pt_PT`, territory PRT,
  currency EUR. Brazilian readers who land here see EUR prices; the App Store link opens their own storefront.
- Engines (TRANSLATION.md 7.4): Google first, then Bing (also feeds DuckDuckGo, Ecosia, Copilot). Tools: Search
  Console, Bing Webmaster Tools. IndexNow covers Bing and the engines that use it.
- **Formality: impersonal, as Apple Portugal writes (proposed 2026-11-19, to confirm with the owner).** Third-person
  imperatives without a pronoun where an instruction is needed («Toque em», «Abra», «Descarregue», «Contacte»),
  infinitives on buttons and labels («Ver todas as apps», «Restaurar compras»), impersonal sentences otherwise
  («os dados ficam no iPhone»). «o seu / a sua» only where a possessive can't be avoided. Never «você», never «tu».
  Reasons:
  1. TRANSLATION.md 13 for pt: «tu, or impersonal phrasing; avoid você». This is the impersonal option.
  2. Apple Portugal never writes tu or você: 0 hits in 51 iPhone guide pages, the Watch and Mac guides, 15 support
     articles and apple.com/pt marketing. It writes «Toque» (620 in the iPhone guide), «Vá», «Abra», «Clique» and
     «o seu / a sua» (348) (pt-apple-terms.md, Register).
  3. Our own apps split: tu in AfterShift, Chessful (lessons; its paywall mixes), EarnLock, LiftLog, Millrace,
     Soon. (main app), Pawza and Clippet; formal third person in AllPaid, AppMeta, AppMeta Pulse, MediaKit, Observa,
     RightSplit, Shogiful, Tare, Taskful Day, WanderWiki and Xiangqiful, and in most of our Portuguese store texts
     (pt-glossary.md, register counts per app). A tu site would contradict Apple and most of the apps; impersonal copy
     reads naturally next to both.
  Consequence: quote app UI nouns and labels, not whole UI sentences (a quoted sentence would carry the app's own
  register).
- European Portuguese only, AO90 spelling: ecrã, telemóvel, utilizador, ficheiro, partilhar, descarregar,
  palavra-passe, Definições, equipa, registar, gerir, guardar, apagar, contacto, receção, ativo, ótimo,
  «estar a fazer». Never the Brazilian forms: tela, celular, usuário, arquivo, compartilhar, baixar, senha, Ajustes,
  equipe, registrar, gerenciar, salvar, contato, cadastro, aplicativo, academia (for gym: ginásio), gerund
  progressives («está fazendo»), clitic before the verb at a sentence start («Me ajuda»).

## Typography and punctuation

House rules (TRANSLATION.md 8.3), with the characters to type:

- Quotes: «…» (Portuguese press style; TRANSLATION.md lets pt choose), no inner spaces; inner quotes “…”. Apple
  Portugal's guides use “…” for UI labels; the site uses «…» throughout for consistency. A one-word UI label is
  written bare; a multi-word label goes in «…». Full stop after the closing quote.
- Menu paths: Definições > [o seu nome] > Assinaturas (spaces around >; Apple's exact labels).
- Headings and labels in sentence case: only the first word and proper names take a capital (Apple Portugal's
  title case on feature names, «Partilha com a família» excepted as written, is not a model for headings).
- No em or en dashes. Apple Portugal uses a spaced em dash; the site does not. Ranges «de 3 a 5 kg» or «entre 3 e 5».
  Lists «A, B e C» (no comma before e/ou).
- Numbers: decimal comma (4,8); thousands with a no-break space from five digits on (12 500), four digits without a
  separator (6005), as Apple Portugal writes them. Percent with NO space: «30%» (Apple Portugal, 576 to 0). No-break
  space U+00A0 between a number and €, units: `3,99 €`, `35 °C`, `8 h`, `5 GB`. Metric units only.
- Times: 24-hour, «22:30». Dates in prose: «26 de outubro de 2026», months lowercase, «1 de novembro» (no ordinal).
  Templates use date.html.
- «app» in body copy, feminine («a app», «as apps»; Apple Portugal's articles, marketing and App Store text write
  app, its user guides «aplicação»). «aplicação» in titles and H1s where the search phrase uses it.
- Gender: «a App Store» (feminine, Apple Portugal 38 to 0), «a Mac App Store», «o Apple Watch», «o iPhone», «o iPad»,
  «o Mac», «a Apple», «o iCloud».
- App names take the masculine article, as Apple Portugal writes its own apps («o Safari», «o Pages»): «o Observa»,
  «o AllPaid», «o Pawza», «o Soon.», «do Chessful», «no MediaKit». The common noun stays feminine: «a app», «esta app».
  Decision 2026-11-19, the same on every Portuguese page.
- Anglicisms: Portuguese word where Apple Portugal or common use has one (subscrição, Definições, cópia de segurança,
  captura de ecrã, descarregar). English where Portuguese searchers and Apple keep it: App Store, App Store Connect,
  widget, Dynamic Island, Apple Watch, iCloud, Siri, ASO, privacy manifest, puzzle.

## Formats (checked 2026-11-19 against the Portuguese App Store)

Source: the iTunes lookup API (`itunes.apple.com/lookup?country=pt&lang=pt_pt`) and the apps.apple.com/pt product
pages for Mockly (id6756589122, paid), Things 3 (id904237743), Observa and LiftLog (pt-apple-terms.md, storefront
section; raw bytes read).

| What | Format seen | Where | In the site |
|---|---|---|---|
| Price | `14,99 €`, `9,99 €` (U+00A0 before €), IAP rows `24,99 €` | Mockly, Things 3 | locales.yml `EUR: position after, space U+00A0, decimal ",", group U+00A0` |
| Free app | `Grátis` (web page; the API says «Gratuito»), «Compras integradas» | product pages | `strings.free: "Grátis"` |
| Get button | Obter | product pages | badge text is Apple's artwork wording, see below |
| Thousands | `2 000 000:1` (U+00A0); `1000 nits` | Apple Portugal | `group: U+00A0` |
| Rating | `4,8`, «298 classificações», «425 mil classificações» | App Store | `strings.decimal: ","` |
| Dates | «29 de setembro de 2026» in running text | support.apple.com/pt-pt | `date_long "{d} de {month} de {Y}"` |

Price line pattern: `Grátis, Premium desde 3,99 €/mês, 24,99 €/ano ou 59,99 € vitalício` (strings.from «desde»,
per_month «/mês», per_year «/ano», lifetime «vitalício», or «ou»). Zero price on plan cards: `{P_ZERO}` → `0 €`.

Note: the Portuguese App Store shows the developer's personal name and address (seller line). That name never goes
on the site; attribute to "Lagerland Apps".

## Glossary

Companion files: `_i18n/pt-glossary.md` (per app: Portugal coverage, feature names verbatim from the string catalogs,
Portuguese App Store name and subtitle, tier names, register, flags) and `_i18n/pt-apple-terms.md` (Apple Portugal's
own names, each with its Apple source URL). Rule: a feature name is written exactly as the app's pt-PT interface shows
it, unless the glossary flags it as Brazilian or defective; an Apple product or feature name exactly as Apple Portugal
writes it.

**Language claims.** Never say **Mockly** is in Portuguese (Portugal): it is pt-BR only, and its Portuguese store listing
is Brazilian too. **GymLogger X** supports European Portuguese (owner decision 2026-11-19: pt-PT devices get its base
`pt` strings), so its page may say it is in Portuguese; its text is still largely Brazilian (2737 of 2923 strings equal
pt-BR, I-0341), so never quote its UI sentences. The other 19 (18 live plus Clippet) have a pt-PT catalog (99 to 100 % of
keys); AllPaid, AppMeta, Pulse,
Chessful, Observa, Shogiful and Xiangqiful carry a large share of Brazilian text inside pt-PT (46 to 90 % of values
identical to pt-BR), so never quote their UI sentences, and check every UI noun from them against the flags. Gaps to
keep off the pages: AllPaid's Siri phrases and AfterShift's calendar prompt are English only; Pawza's camera and photo
prompts are English only; LiftLog has 8 untranslated statistics labels.

The terms that matter most across the site:

| English | Portuguese on the site | Source |
|---|---|---|
| (address) you | impersonal; third-person imperative without pronoun; never você or tu | this sheet |
| Download on the App Store (badge) | Descarregar na / App Store (Mac: Descarregar na / Mac App Store) | Apple badge artwork pt-pt (tools.applemediaservices.com) |
| Free (price) | Grátis | Portuguese App Store |
| In-App Purchases | Compras integradas | Portuguese App Store |
| subscription / cancel | «subscrição» in prose (the searched word: «cancelar subscrição iphone»; most apps' word); Apple's own labels quoted exactly: Definições > [o seu nome] > Assinaturas > «Cancelar assinatura» | keyword research; support.apple.com/pt-pt/118428 |
| request a refund | «Pedir um reembolso» (reportaproblem.apple.com) | support.apple.com/pt-pt |
| lifetime (purchase) | «vitalício / vitalícia» (all pt-PT catalogs); «compra única» in prose | app catalogs |
| Family Sharing | Partilha com a família | Apple Portugal |
| Data Not Collected | Dados não recolhidos (section «Privacidade da app») | Portuguese App Store |
| Health app / Apple Health | a app Saúde (Apple Portugal has no «Apple Health» name; «a app Saúde da Apple» where the brand is needed) | Apple Portugal |
| Heart Rate Variability (HRV) | variabilidade da frequência cardíaca (VFC); always SDNN for Apple Health; «VFC (SDNN)» on Observa. Portugal keeps the accent in «cardíaca» | Apple Portugal, Observa catalog |
| Resting heart rate | frequência cardíaca em repouso | Apple Portugal |
| Sleep stages | Acordado, REM, essencial, profundo | Apple Portugal |
| Screen Time | Tempo de ecrã | Apple Portugal |
| Focus / Sleep Focus | modo de concentração / modo de concentração «Dormir» | Apple Portugal |
| Home Screen / Lock Screen / widgets | ecrã principal / ecrã bloqueado / widgets | Apple Portugal |
| Live Activities / Smart Stack / StandBy | atividades em tempo real / pilha inteligente / Em espera | Apple Portugal |
| iCloud sync | sincronização com o iCloud | Apple Portugal, app catalogs |
| Settings (iOS) | Definições (Mac: Definições do Sistema) | Apple Portugal |
| Shortcuts / Wallet / Weather | Atalhos / Carteira / Meteorologia | Apple Portugal |
| Workout (Apple) | Treino | Apple Portugal |
| VO2 max / Cardio Fitness | VO2 máx. / cardiofitness | Apple Portugal |
| Sign in with Apple | Iniciar sessão com a Apple | Apple Portugal |
| Apple Account | conta Apple | Apple Portugal |
| App Tracking Transparency / tracking | «Permitir pedidos de seguimento das aplicações»; tracking = seguimento | Apple Portugal |
| Universal Clipboard | Clipboard universal; clipboard in general «área de transferência» (Clippet's word) | Apple Portugal, Clippet catalog |
| countdown | contagem decrescente (Soon.'s word; «contagem regressiva» is Brazilian) | Soon. catalog |
| Journal (section) | Blog (hub title, nav, feed); URLs stay `/pt/journal/` | as decided for Spanish |
| stamp sheet (design metaphor) | folha (de selos), «Folha 2025-{year} · Emitida na Finlândia» | proposed |
| privacy manifest | «manifesto de privacidade» in prose, «manifesto de privacidade (privacy manifest)» at the first mention on home and transparency | as for Spanish |
| reviews / ratings (App Store) | críticas / classificações | Portuguese App Store |

## Keyword research

Full notes, sources and FAQ-style questions per page: `_i18n/pt-keywords.md` (Google suggest hl=pt-PT gl=pt, Bing
qsonhs mkt=pt-PT, App Store search hints for the Portugal storefront 143453-2, iTunes Search API country=pt,
2026-11-19). Every query below came from one of those sources. Google's Portugal suggest mixes in Brazilian and
Spanish phrasing; the picks are phrases natural in Portugal.

Search Console for Portugal: not read in this session. Revisit 4 to 6 weeks after go-live with the page filter
`/pt/` and the country filter Portugal.

`seo.title`, the H1 and `quick_answer` of each page are written for its primary query.

| Page | Primary query | Secondary queries |
|---|---|---|
| Home (/pt/): studio of privacy-first Apple apps | `apps sem anúncios` (weak: B and A only; the privacy angle has no Portuguese demand) | `aplicações para iphone` (`melhores apps iphone` is the hub's) |
| Apps hub (/pt/apps/) | `melhores apps iphone` | `melhores aplicações para iphone`, `melhores aplicações apple watch`, `aplicações para mac` |
| About (/pt/lagerland-apps/) | none with demand: brand-led («Lagerland Apps» + «programador independente») | `desenvolvedor de aplicações para ios` (the searched form; the page says «programador») |
| Support hub (/pt/support/) | `cancelar subscrição iphone` | `reembolso app store`, `cancelar subscrição app store`, `restaurar compras app store` |
| Transparency (/pt/transparency/) | `app tracking transparency` (Portuguese searchers type the English) | `privacy manifest`, `app tracking transparency iphone` |
| AfterShift | `como dormir de dia quem trabalha à noite` | `como recuperar o sono de quem trabalha à noite`, `dívida de sono`, `distúrbio do sono trabalho por turnos` |
| AllPaid | `app lembrete de pagamento` (weak) | `app para lembrar pagamentos`, `app lembrete de contas a pagar` |
| AppMeta | `app store connect mac app` (developers search in English) | `aso app store optimization`, `criar conta app store connect` |
| AppMeta Pulse | `app store connect iphone` | `app store connect api`, `app store connect ios` |
| Chessful | `app xadrez` | `melhor app de xadrez`, `app para aprender xadrez`, `análise de partidas de xadrez` |
| EarnLock | `bloquear apps iphone` | `tempo de ecrã iphone`, `limite de apps iphone`, `bloquear instagram iphone` |
| GymLogger X | `app treino apple watch` | `app treino de força`, `app musculação apple watch` |
| LiftLog | `app treino ginásio` («sem subscrição» has no demand; kept in the copy as the differentiator) | `plano de treino ginásio`, `diário de treino app` |
| MediaKit | `comprimir vídeo iphone` | `comprimir pdf iphone`, `converter heic para jpg`, `reduzir tamanho vídeo whatsapp` |
| Millrace (never write the number title) | `jogos de lógica iphone` | `jogos de raciocínio lógico iphone`, `jogos sem anúncios iphone` |
| Mockly | `screenshots app store` (developers type the English) | `app store screenshot generator`, `app store screenshot maker`, `mockup app store` |
| Observa | `hrv apple watch` | `variabilidade da frequência cardíaca`, `app sono apple watch`, `qualidade do sono apple watch` |
| Pawza | `boletim sanitário de cães e gatos` (always pair «boletim» with cão/gato: alone it returns livestock or the SNS 24 human booklet) | `boletim de vacinas cão`, `boletim de vacinas gato`, `calendário de vacinação para cães e gatos` |
| RightSplit | `dividir conta restaurante` | `app para dividir contas`, `app para dividir despesas com amigos`, `calculadora dividir conta` |
| Shogiful | `shogi` | `xadrez japonês`, `shogi regras`, `como jogar shogi` |
| Soon. | `contagem decrescente iphone` (small; the Brazilian «contagem regressiva» is stronger but wrong here) | `app contador de dias`, `contagem decrescente casamento`, `contagem decrescente widget` |
| Tare | `melhores jogos de puzzle iphone` (moved off Millrace's query) | `jogos de puzzle iphone`, `jogos offline iphone` |
| Taskful Day | `app lista de tarefas` | `app tarefas diárias`, `app para organizar o dia`, `app to do list` («planeador diário» in body text) |
| WanderWiki | `wikipedia aleatória` (tiny demand) | `wikipedia página aleatória`, `artigo aleatório wikipedia`, `app wikipédia` |
| Xiangqiful | `xadrez chinês` (title carries «xiangqi» too: «xadrez chinês» also means Chinese checkers) | `xiangqi`, `xadrez chinês como jogar`, `xadrez chinês regras` |
| Clippet (unreleased, unlisted) | `histórico área de transferência iphone` | `histórico área de transferência mac`, `como ver a área de transferência no mac`, `copiar e colar iphone mac` |

## Tier 2 keywords (2026-11-19)

| Page | Primary | Notes |
|---|---|---|
| /pt/guides/best-chess-apps-iphone/ | `melhor app de xadrez` | taken from Chessful (which keeps `app xadrez`) |
| /pt/guides/best-logic-puzzle-games-iphone/ | `melhores jogos de lógica para iphone` | Millrace keeps `jogos de lógica iphone`, Tare `melhores jogos de puzzle iphone` |
| /pt/guides/workout-app-without-subscription/ | `app de treino grátis` (angle «sem subscrição») | GymLogger X keeps `app treino ginásio grátis` |
| /pt/guides/best-xiangqi-apps-iphone/ | `xadrez chinês online` (seo.title only; H1 without «online», the apps are mostly offline) | Xiangqiful keeps `xadrez chinês` |
| /pt/guides/limitar-tempo-de-ecra-iphone/ (local-only) | `limitar tempo de ecrã iphone` | takes `tempo de ecrã iphone`, `limite de apps iphone` from EarnLock |
| /pt/for/shift-workers/ | `trabalho por turnos saúde` | AfterShift keeps its sleep queries |
| /pt/for/apple-health-power-users/ | `apps para apple watch` + `melhor app saúde iphone` | Observa keeps `hrv apple watch`, `app sono apple watch` |
| /pt/for/calm-productivity/ | `apps de produtividade iphone` | Taskful Day keeps its to-do queries |
| /pt/guides/best-shogi-apps-iphone/ | `shogi online` | Shogiful keeps `shogi`, `xadrez japonês`, `como jogar shogi` |
| /pt/guides/bill-tracker-without-bank-connection/ | `app para gerir subscrições` | AllPaid keeps `app lembrete de pagamento`, `app lembrete de contas a pagar` |
| /pt/guides/como-fazer-contagem-decrescente-iphone/ (local-only) | `como fazer contagem decrescente no iphone` | Soon. keeps `contagem decrescente iphone`, `contagem decrescente widget`, `app contador de dias` |

## Tier 3 keywords (2026-11-19)

| Page | Primary | Notes |
|---|---|---|
| /pt/alternatives/whoop/ | `alternativa a whoop` (prose «alternativa à Whoop», Whoop feminine) | + `whoop sem subscrição` (answered with facts, I-0369), `oura ou whoop` shared with oura |
| /pt/alternatives/oura/ | `oura ring ou apple watch` | + `oura ring tem subscrição` |
| /pt/alternatives/splitwise/ | `alternativa ao splitwise` | `tricount ou splitwise` shared with tricount |
| /pt/alternatives/tricount/ | `alternativa a tricount` (prose «alternativa ao Tricount») | + `tricount como funciona` |
| /pt/alternatives/hevy/ | `hevy como funciona` | + `hevy pro preço`, `hevy ou strong` |
| /pt/alternatives/chess-com/ | `chess.com premium preço` | + `chess com alternativas`, `chess com grátis análise` |
| /pt/alternatives/lichess/ | `chess.com ou lichess` | + `lichess grátis`, `lichess xadrez` |
| /pt/alternatives/pdf-expert/ | `pdf expert grátis mac` | `comprimir pdf iphone` stays with MediaKit |
| /pt/alternatives/forest/ | `forest app como funciona` | + `forest app preço`, `forest app apple watch` |
| /pt/alternatives/opal/ | `opal app como funciona` | `bloquear apps iphone` stays with EarnLock |
| /pt/alternatives/documents-by-readdle/ | `documents by readdle` | 4 keywords only (no fifth real query) |
| /pt/alternatives/bevel/ | `bevel app` | + `bevel apple watch`, `bevel vs gentler streak` |
| /pt/alternatives/autosleep/ | `autosleep apple watch` | `qualidade do sono apple watch` stays with Observa |
| /pt/alternatives/gentler-streak/ | `gentler streak` | + `gentler streak premium` |
| /pt/alternatives/strong-workout-app/ | `strong workout tracker` | `hevy ou strong` shared with hevy; 4 keywords |
| /pt/alternatives/fitbod/ | `fitbod é pago` | + `fitbod é bom`, `fitbod em português` |
| /pt/alternatives/one-sec/ | `one sec app` | 3 keywords (no more real queries) |
| /pt/alternatives/screenzen/ | `screenzen` | + `screenzen em português`, `screenzen vs opal` |
| /pt/alternatives/rise-sleep-tracker/ | `rise sleep tracker` | + `rise sleep funciona` |
| /pt/alternatives/habitica/ | `habitica em português` | + `habitica como funciona` |
| /pt/alternatives/flow-free/ | `flow free` | + `flow free grátis` (the «free flow» suggestions are tolls) |
| /pt/alternatives/two-dots/ | `two dots` | + `two dots grátis` |
| /pt/alternatives/kami-2/ | `kami 2` | brand query only |
| /pt/alternatives/productive/ | `productive app` | 3 keywords |
| /pt/alternatives/streaks-app/ | `streaks app` | + `streaks apple watch` |
| /pt/alternatives/handbrake/ | `alternativa handbrake` | + `handbrake como funciona` |
| /pt/alternatives/cloudconvert/ | `cloudconvert grátis` | + `cloudconvert como funciona`; `cloudconvert ou convertio` left for a future Convertio page |
| /pt/alternatives/welltory/ | `welltory` | + `welltory português` |
| /pt/alternatives/jefit/ | `jefit em português` | + `hevy ou jefit` |
| /pt/alternatives/settle-up/ | `settle up como funciona` | + `settle up vs splitwise` |

Store facts per competitor: ~/Downloads/githubcode/pt-tier3-store-2026-11-19.md. «IAP rows: none shown» there means the
listing flags in-app purchases but renders no rows: never write «sem compras integradas» from it.

Google Portugal suggest returns Brazilian forms (iniciantes, academia, «os apps», celular, tela): never use them as keywords.

## Tier 4 keywords (2026-11-19)

| Page | Primary | Notes |
|---|---|---|
| /pt/journal/ (hub) | none of its own | keywords borrow the posts' primaries, as on fr |
| /pt/journal/how-many-steps-a-day-to-aim-for/ | `quantos passos por dia` | + `quantos passos devemos dar por dia`, `… segundo a oms` (the WHO fact sheet gives 150 minutes a week, not steps), `10000 passos por dia` |
| /pt/journal/how-long-to-rest-between-sets/ | `quanto tempo descansar entre séries` | + `descanso entre séries hipertrofia`, `intervalo entre séries`; «descanso entre séries força» returns nothing |
| /pt/journal/choosing-a-strength-program-you-will-finish/ | `treino ppl` | + `treino upper lower`, `treino upper lower 4 dias`, `treino 5/3/1`, `quantos dias por semana devo treinar` |
| /pt/journal/when-to-deload/ | `semana de deload` | + `quando fazer deload`; «semana de descarga» returns Spanish suggestions |
| /pt/journal/apple-watch-hrv-without-a-baseline/ | `vfc baixa` | + `vfc baixa o que significa`, `vfc valores normais`; Observa keeps `hrv apple watch`, `variabilidade da frequência cardíaca` |
| /pt/journal/puppy-and-kitten-vaccination-schedule/ | `vacinas gatos` + `vacinas cachorro` | «cachorro» = puppy in Portugal; Pawza keeps the «boletim» queries |
| /pt/journal/how-much-to-tip-in-the-us/ | `gorjeta nos estados unidos` | + `gorjeta eua`, `gorjeta é obrigatória nos eua` |
| /pt/journal/find-every-recurring-charge/ | `como ver subscrições no iphone` | + `como ver subscrições`, `… no paypal`, `… google`; support hub keeps `cancelar subscrição iphone` |
| /pt/journal/puzzle-games-without-ads-or-lives/ | `jogos sem anúncios` | Millrace keeps `jogos sem anúncios iphone` |
| /pt/journal/converter-mkv-para-mp4/ (local-only) | `converter mkv para mp4` | + `… sem perder qualidade`, `… vlc`, `… grátis` |

## Decisions from the Tier 1 reviews (2026-11-19)

- App names take the masculine article on every page and in the interface strings («o Observa», «do Pawza», «ao
  Tare»; pt.yml strings with {name} carry it too).
- Tracking: «seguimento» as the noun, «seguir a sua atividade» as the verb phrase (Apple Portugal); never «rastreio»,
  «rastreamento», «rastreadores», never «fazer seguimento».
- «Wikipédia» in Portuguese prose (the app, the Portuguese store listing and the Portuguese edition write it so);
  «Wikipedia (oficial)» only as the competitor app's name; URLs unchanged.
- Mistake cards on Chessful, Shogiful and Xiangqiful: «cartão»; «ficha» only for an App Store listing.
- Bills (AllPaid): «contas a pagar» where «conta» could mean an account; tip: «gorjeta».
- Support pages: one title pattern «<App>: suporte e contacto». Privacy pages: «Privacidade do <App>: sem seguimento
  nem conta» (Tare: «sem recolha de dados nem conta»; Mockly adds «anúncios»).
- The advertising clause mirrors the English ambiguity, as in Spanish: «não vende, não partilha nem utiliza … para
  fins publicitários».
- «App Store de Portugal» where the English says "Prices in USD" (footnotes, price FAQs).
- Founder lines: «Programador Apple independente · Estúdio de uma só pessoa desde 2025 · Finlândia» (English order).
- GymLogger X counts as available in Portuguese (owner, 2026-11-19); Mockly never does.
- Open, for a native reader: the gender of Apple Intelligence (the apps' catalogs write both; the site writes «a Apple
  Intelligence»); «o ecrã de bloqueio (shield)» for EarnLock's shield; trial phrase «teste grátis».
- Legal terms for a Portuguese lawyer: «tratar/tratamento», «recolher conscientemente», «Ao efetuar uma compra, o
  utilizador aceita que possamos responder…» (consent by purchase), «responsável» (controller), «Provedor de Proteção
  de Dados da Finlândia» (working name), «crianças com menos de 13 anos» (Portugal's digital-consent age is 13, Lei
  58/2019), «dados pessoais sensíveis» (GDPR: «categorias especiais de dados pessoais»), «data de entrada em vigor»,
  and in Clippet's terms «tal como está» / «conforme disponível», «comerciabilidade», «adequação a um fim específico»,
  «danos indiretos, acidentais, especiais, consequenciais ou punitivos», «normas de conflitos de leis», «leis
  imperativas de defesa do consumidor», «alterações substanciais».

## Local competitors (for Tier 3)

Researched 2026-11-19 (pt-tier3-research-2026-11-19.md): no Portugal-born competitor with search demand for any of our
apps. Bill splitting is Splitwise and Tricount; budgeting is Wallet (BudgetBakers), Spendee and Money Lover (covered by
the bill-tracker guide); app blocking is Opal, Forest, one sec and AppBlock.

## Tells to cut in Portuguese (TRANSLATION.md 8.2, plus what reviews find)

Stock phrasing: «No mundo acelerado de hoje», «Na era digital», «Vamos mergulhar», «É importante ressaltar que»,
«Vale a pena notar que», «desempenha um papel crucial», «não apenas … mas também», «Em suma», «Em resumo»,
«Quer seja … quer …», «descubra como», «leve o seu … ao próximo nível», «potenciar», «solução», «uma experiência
fluida», «sem complicações», «revolucionário», «de forma eficiente».

Found in the interface-strings review (2026-11-19): «fazer seguimento» for tracking (reads as "follow up": write
«seguir a atividade», keep «seguimento» for the label noun); «Mais do mesmo …» at a line start (the "more of the
same" idiom); «alternativa face a» (write «alternativa a»); one object shared by verbs with different complements
(«lê e responde a todas»); «constam da» (stiff: «estão indicados na»); «site em linha» («site publicado»); «Isto é
uma tradução» («Esta é»); «datadas» for "dated" (reads "outdated"); double «para» («para aqui para»); «Também pode
gostar» without «de» and an object.
From the batch 1 review (home, hub): «de que mais gente se muda» (calque of "switching from": «que mais gente está a
trocar»); pre-AO90 «revêem», «lêem», «vêem» (AO90: reveem, leem, veem); «Acesso às Chaves» (Brazilian macOS: pt-PT
«porta-chaves»); «obriga a» for "asks you to" (strengthens the claim); «dar o suporte» («dar apoio»); «segue a
atividade» with no owner (Apple Portugal: «seguir a sua atividade»); «ficha» for a card («cartão»; «ficha» is the App
Store listing).
From the privacy and batch 5 reviews: «opera servidores» («tem servidores»); passives that drop the user as agent («se
forem utilizadas», «a menos que seja traduzido»: name «o utilizador»); «a nível do dispositivo»; «preferimos que aprove»
for "would prefer" (conditional: «preferiríamos que aprovasse»); trailing gerunds («analisando… oferecendo»); «dos
mesmos» as a stiff pronoun; «faz seguimento de quem a usa» («segue a sua atividade»); «rastreio», «rastreadores»
(Brazilian: «seguimento»); «em local» («localmente»); «liga um SDK» («integra»); «nem … ou» mixed in one negated list;
«exige» for "asks you to"; «tomas de cafeína» (medicine word: «consumos»); «desenho da app» («conceção»).
Privacy pages standard lines: «tratar/tratamento», «recolher», «conscientemente», «dados pessoais», «crianças com
menos de 13 anos», «não se dirige a» (directed at) / «não se destina a» (intended for), «que opções o utilizador tem»,
«Ao efetuar uma compra, o utilizador aceita que possamos responder…», «A Apple toma a decisão final sobre cada
reembolso.», «data de entrada em vigor», «framework» feminine.

From the Tier 2 batch 1 reviews (2026-11-19): «deixa em paz o resto do tempo» for "leaves you alone" (reads as the reverse:
«não incomoda no resto do tempo»); subjectless «quando falha um dia» («quando se falha»); «no próprio iCloud» for "your own
iCloud" («no iCloud de cada pessoa»); «melhorias» for paid upgrades («compras opcionais do Pro»); «deixa-se o sono ser
importado»; «Quem quer que … tem no X»; «está a tratar o corpo»; «dá para» in prose and «Dá para…?» in questions («é
possível»); gendered «farto», «atrasado», «Ser guiado»; «utilização» / «consoante o uso» for "job" («objetivo», «tarefa»);
Spanish leaks «Comparativas», «frente ao» (write «vs»), «caráter» (pt-PT «carácter»); «compará-la» after a masculine app
name; «etiqueta de privacidade» (Apple Portugal: «Privacidade da app»); «À primeira vez» inventing a condition Apple doesn't
state; quoting one's own translation of an English-only listing as if it were the app's text; dropping «inteiramente» /
«nunca» from a competitor's privacy claim; «estruturas de trabalho» («frameworks»); «seguimento do progresso» (privacy word:
«acompanhamento»); «combina com» for "suits" («presta-se a»); «dar nome a» a value («determinar»); «destacado» for Editors'
Choice («escolhido pelos editores»); «o editor deste guia» next to «a Lagerland Apps» («que publica este guia»); «cópias na
nuvem» for cloud saves; «inundar» for colour-flood; «ambos jogam-se» («ambos se jogam»); added «com frequência»; dropped
"instead" and "we built"; competitor names replaced by their Portuguese store titles (store title once at most).
From the Tier 2 batch 2 reviews: «convém» as the default piece of advice (five on one page: «vale a pena», «o melhor é»,
or say it plainly); «ao alcance de ganhar»; «travado» (gendered); «metem logo» with no object; «espera que se aprenda a jogar»
for "learn by playing"; «feitos em torno de» for "built around"; «uma só vez» for lifetime («vitalício»); «artigo do diário»
(«blog»); «repete partidas» for replays («revê»); «contas» meaning bills, bank accounts and in-app accounts on one page
(«contas a pagar», «contas bancárias», «sem criar conta»); bare «o Wallet» next to Apple's Wallet («o Wallet (da
BudgetBakers)»); puns («à mão»); a listing's «adicionar» turned into «registo manual»; a meta clause tacked onto a
disclosure; «widgets circular» (agreement); «Central de Notificações» capitalised (Apple Portugal: lowercase in prose);
one-word UI labels in «»; «junto com» («a par de»); our own app's facts credited to «a ficha».
apps.apple.com sometimes returns an empty 1 KB app shell: check the saved file's size (an `Accept-Language: pt-PT` header
returned the full page).
Apple Portugal's own Screen Time guide switches the schedule on with «Programação» and off with «Horário», and writes
«Limites de tempo» on one page, «Limites de tempo permitido» on another: quote each step as written.

From the Tier 3 batch 1 reviews (2026-11-19): infinitive bullets or a second «se» under a card title ending «… se»
(«Não ser preciso que…», «se quer…»): write «serve para quem…» + a verb, or an indicative clause; «se se» doubles;
impersonal-se bullets («Quer-se ver…», «Escolha-se o X»): third person without pronoun as on the app pages; «a
alternativa» for "an alternative"; «alternativa a X» in prose where the page writes «o X» (keywords stay as typed);
«compras na app» / «compras dentro da app» (Apple Portugal: «compras integradas»); «listagem» («ficha»); «opção de
compra única vitalícia» («opção vitalícia»); «contrata-se» for a lifetime purchase («vende-se»); «entram» with no
complement («entram no grupo»); «quem o lê» for a service; gerund progressives «vão-se registando», «vai preenchendo»;
«copia-se» with no object; «confirmem-se», «confira» («confirme»); «por X por ano»; «Fazem trabalhos diferentes»
(«Servem para coisas diferentes»); «fica melhor servido» (gendered); «frente a» (Spanish: «comparado com», «vs»);
«uma pulseira que se usa no pulso»; «verificado com dados» («testado com»); one Portuguese name for two competing
scores (qualify the competitor's: «pontuação diária de esforço (Strain) da Whoop»); «uma categoria em seis» («uma das
seis categorias»); ratings with two decimals (one, as the store shows); hardening a competitor fact with «só»;
invented popularity closers («muita gente usa ambos»); editorial summaries no source makes («a diferença está
sobretudo em…»); «treino de hoje» for "daily training" outside the UI label; «revê» for "checks» («verifica»); one
gender per competitor feature across sibling pages («a Game Review»); «tokens opacos» («identificadores opacos»);
«bloco» for a focus session («sessão»); «versão grátis» where the app page says «plano grátis»; «Não indicado» against
a feminine label; a sentence that opens with its verb and holds the subject back; meta clauses about where a fact came
from («vem da verificação feita para a página em inglês»).
From the Tier 3 hub and llms review: «ninguém mais» (Brazilian order: «mais ninguém»); «X face ao Y» as "vs" in lists
(«o X comparado com o Y»); «tira do Apple Watch» for scores computed from Health data; «por agora em inglês» (an implied
roadmap: «estão em inglês»); «quando fica melhor a app conhecida»; competitor names without their article in titles and
descriptions («ao Splitwise, à Whoop»; keywords stay as typed).
From the Tier 3 batch 2 reviews: «numa só compra», «só se paga por subscrição», «uma só vez» for lifetime («opção
vitalícia»); «face ao/à» piled up for "against your baseline" («em relação a»); «ecrã principal» for an app's own home
screen («ecrã inicial da app»); «Ambas» for two masculine app names («As duas apps»); verdicts added to quick_answer;
«revista a» for "checked" («verificada a»); unclear «o seu / a sua» («a política de privacidade do Bevel»); «não há uso
para»; a writer's wording quoted as a UI string; footnote meta sentences («os preços são os dessa ficha»); «a AutoSleep»
(masculine app name); store titles with an en dash; «pede registo» where «registo» also means logging; «não há nada
para criar» ("nothing to sign up for": «sem registo»); «gere» (gerar or gerir: «crie»); «antes de mudar» («antes de trocar
de app»); «a do X corre» for "X's can"; a bare multi-word UI label as a subject (put it in «»); «encontra no X a app mais
completa»; guessed competitor UI labels; «nível grátis» where the app page says «versão grátis»; invented causal links
in competitor summaries; «Confirme os preços … do seu país» on a Portugal page; «entre os» hedging a full privacy list;
«funciona muito bem» for "works well"; a trial tied to one IAP row; a clause whose object reads as the subject («atrasa
a abertura de uma app que distrai com uma respiração»); «ao lado do» for "compared with"; «quem se contenta com»;
«Não consta» as a table value («Nenhuma indicada»); «quem o desenvolve» («o programador»); a second H1 line copied from a
sibling page; trailing participle after a price list; «um muito bom X» («um X muito bom»); «sincronizar nuvens».
From the Tier 3 batch 3 reviews: dropping an English fact because the store is silent (silence is not a contradiction);
«vive de anúncios» («tem anúncios»); «na cloud» («na nuvem»); «uma boa candidata» for a masculine app; «a escolher onde…»
(«para quem escolhe»); a language list repeated after the quick_answer said it; a bare «livro» for a ledger («livro de
contas»); «é o assunto todo»; «servem de lembrete para» («lembram de»); «uma conta» where account and bill both fit;
«a Productive» (masculine app names); anacoluthon «Quem …, o X serve melhor» («Para quem …»); «pesam um contra o outro»;
«cria hábitos à volta de»; «divulgações» («declarações de privacidade»); gerund chains for input methods; «pagar uma só vez»
for a competitor («preço único»); «quando for oportuno»; trial terms read into IAP row names; elliptical table cells with
no noun.
From the batch 3 Millrace and hub reviews: «tira os anúncios» right after «remove os anúncios»; «o guardado automático»
(«guardar o progresso»); «se se» in table cells; «O que se vê vir»; «classificações» for ranks (clashes with store
ratings); «avaliações» for App Store reviews (the store says «críticas»); a footnote widening its source list beyond the
English one; «se quiser» breaking the impersonal register; «para computador» where the page names the systems; «cobrar
uma só conta» next to «livro de contas»; a list of three whose last item changes the subject; «ainda não existem em
português» (implied roadmap: «sem versão em português»); card wording drifting from the page.

From the Tier 4 batch 1 reviews (2026-11-19): «ajuste» for an app setting («definição»); a drifting object pronoun
(«querem-no dado» after «comprovativo»); «precisar» without «de» in questions; a noun dropped after a number («cerca de um»);
indicative after «garantir que»; typos in copied source URLs (diff every external URL against English); «a curva dobra» for
"bends" (reads "doubles": «inflete»); «inferior à de 2000» after step counts (reads as the year); «com mais de 30 anos» for
"from 30 years earlier"; «quadro» for "frame" («referência»); «saúde de consumo»; «estou avariado» as the reader's thought;
«Moderadamente ativo» for "somewhat active" («Algo ativo»); «um objetivo que se mantém» for "a goal you'll keep" («que se
consiga manter»); an H1 that inverts "means nothing without X"; «se está encalhado» (gendered: «quando não se vê saída»);
«descomprime» for unpacking a container («desempacota»); «segundo a ficha da app» for our own page; a quick_answer opener that
hardens a hedge («basta ler» for "most can be spotted"); «Execute a ferramenta» (name the button: Executar); «manobrista»
(Brazilian: «valet (quem estaciona o carro)»; «arrumador» is a different job); «a IRS» for the US agency (in Portugal «o IRS» is
the Portuguese income tax: «o fisco dos Estados Unidos (IRS)»); «quem serve ao balcão» («barman»); «recolha à porta» for
curbside; «está na maioria» («faz parte da maioria»); «varrimento» («revisão»); «por conceção» for "by design" («de
propósito»); «contas» for arithmetic on a bills page («cálculos»); «predefinição» for a training default («ponto de partida»);
«ganhar volume» for muscle size where «volume» means training volume; «competidores» in a survey («atletas de competição»); an
invented gloss for an English term («taper (período de afinação)»); «escritos à mão» for "self-written"; «tomam partidos
diferentes»; «fizeram N adultos seguir» («puseram N adultos a seguir»); «entre 1 e 12» for a range; turning the English first
person into «tanto quanto se sabe» (the posts keep the first person, never gendered). Process: writers who skip the copy-editing
skill or the fact diff leave twice the fixes; writers extend the English with extra facts from localized Apple/PayPal pages (a
Portugal source may replace US context, never add to it); a local-only post written line by line from the French model.

Translationese: title case headings; gerund chains copied from English -ing («oferecendo», «permitindo»); passive
«é … por» where Portuguese uses «se»; possessives on body parts and devices copied from English; «utilizador»
everywhere where Portuguese says «quem»; Brazilian vocabulary and grammar on this Portugal site (see Market and
register); «você» or tu forms slipping in; clitic placement copied from Brazil.

## House rules carried over

- No public roadmaps or dated promises. Describe what an app does today.
- Prices only through tokens. No arithmetic on our prices.
- «Sem subscrição» only for LiftLog, Millrace, Mockly and Tare. For the others «sem subscrição obrigatória» or
  «opção vitalícia», where true.
- «calmas» and «que respeitam a privacidade» once, where they state positioning.
- Never the owner's personal name. Attribute to "Lagerland Apps".
- Millrace's copy never mentions the number title it replaced; Observa's HRV is SDNN, never RMSSD (RMSSD only for
  Observa's ECG-based Premium feature, as on the English page).
- App names, competitor names and "Lagerland Apps" as written in English.

## Review log

| Pages | Writer | Reviewer | Back-translation | Native |
|---|---|---|---|---|
| `_data/i18n/pt.yml` (323 strings) | 1 writer | 1 reviewer (copy-editing skill, fact diff, glossary): 38 changed; later 38 strings given the masculine article, 2 support keyword stems widened | n/a | no native review yet |
| /pt/, /pt/apps/ | 2 writers | 1 reviewer (24 fixes) | home: 8 meaning shifts fixed | no native review yet |
| 21 app pages | 21 writers | 4 reviewers (3 to 6 pages each), then one fixer for the who_for/who_not_for bullets on 8 pages | all 21: meaning shifts fixed on 14 pages (dropped "exact", "signed in", "your own key", "about", softened "scraped", added sentences), none on 7 | no native review yet |
| 21 support pages | 7 writers | 1 reviewer: every description rewritten to promise only topics the page shows | n/a | no native review yet |
| 21 privacy policies + Clippet terms | 6 writers | 4 reviewers, sentence by sentence: about 12 meaning fixes (contact vs contacts, HealthKit "transmitted", Apple IDs, plain marker, warranties, "would prefer", "was available") | n/a | no native review yet |
| about, support hub, transparency | 3 writers | 1 reviewer | about: 3 meaning shifts fixed | no native review yet |
| /pt/llms.txt, /pt/llms-full.txt | 1 writer | 1 reviewer (every reason checked against the app's Portuguese page; one invented query replaced) | n/a | no native review yet |
| Tier 2 batch 1: chess, logic, workout, xiangqi guides; 3 /for/ pages; local-only screen-time guide (2026-11-19) | 8 Sonnet writers | 4 reviewers (for pages; chess + xiangqi; workout + local, Apple pages re-fetched live; logic): about 150 fixes, incl. double-brace tokens, a wrong Apple label, a translated quote, «Nonogramas Katana» renamed, hedges restored | n/a | no native review yet |
| Tier 2 batch 2: shogi, bill tracker (Portugal rewrite), local-only countdown guide (2026-11-19) | 3 Sonnet writers | 3 reviewers (Apple pages re-fetched live; every competitor sentence against its Portuguese listing): about 50 fixes, incl. Big Days' in-app purchases, Soon.'s free task list, Shogi Wars offline play per its listing | n/a | no native review yet |
| Tier 3 batch 1: 10 comparisons (2026-11-19) | 10 Sonnet writers | 6 reviewers (Splitwise + Tricount; WHOOP + Oura; Hevy; Chess.com + Lichess; PDF Expert; Forest + Opal; raw Portuguese store pages re-read for Opal and Forest): about 150 fixes, incl. US-store references and US privacy and Family Sharing data replaced by Portuguese store data, Forest's Apple Vision restored, Opal's lifetime row, hardened «só para Mac», added Hevy Pro list and lichess community claims cut, colliding keywords replaced | n/a | no native review yet |
| Tier 3 batch 2: 10 comparisons (2026-11-19) | 10 Sonnet writers | 6 reviewers (Bevel + AutoSleep + Gentler Streak; Strong + Fitbod; one sec + ScreenZen; RISE + Habitica; Documents; raw Portuguese store pages and the iTunes lookup re-read): about 160 fixes, incl. colliding and invented keywords removed, added verdicts and store claims cut, RISE privacy list completed and its language FAQ cut, Documents' Mac, MP3 and ZIP/RAR rows corrected from the store, Gentler Streak rating 4,7 | n/a | no native review yet |
| Tier 3 batch 3: 10 comparisons (2026-11-19) | 10 Sonnet writers | 6 reviewers (Flow Free + Two Dots + KAMI 2; Productive + Streaks; HandBrake + CloudConvert; Welltory; Jefit; Settle Up): invented keywords dropped, Jefit's «Elite removes ads» restored, «a Productive» → «o Productive», meta footnotes and an unrequested language line cut | n/a | no native review yet |
| Tier 3 hub /pt/alternatives/, /pt/llms.txt lines, Observa and RightSplit FAQ links | 1 Sonnet writer | 1 reviewer (ItemList names and llms titles synced to final page titles; colliding queries removed) | n/a | no native review yet |
| Tier 2 hubs, /pt/llms.txt lines, 6 inbound links | 1 Sonnet writer | 1 reviewer (ItemList names and llms titles synced to final page titles, two unrouted queries routed) | n/a | no native review yet |
| Tier 4 batch 1: hub and 10 journal posts incl. local-only converter-mkv-para-mp4 (2026-11-19) | 10 Sonnet writers (hub by the main session) | 5 reviewers (gym ×3; steps + HRV; vaccines; tipping + subscriptions; games + MKV; DGAV, Your Europe, WHO, Apple pt-pt, PayPal, Matroska, VideoLAN and the iTunes lookup re-fetched live; app catalogs read): about 250 fixes, incl. an inverted HRV H1, invented keywords replaced with suggest-confirmed ones, a broken AAHA/AAFP link, writer-added facts from localized pages removed, «manobrista» and «a IRS», hedges restored («a maioria», "mostly agree", "instead") | n/a | no native review yet |

Points for a native reader: the trial phrase «teste grátis» (Apple's support pages say «período experimental»);
«segue a sua atividade» for "tracks you"; «Direitos do utilizador» as the privacy heading; «é para si?»; category
«empresas» for business.

## Apps still on English screenshots

MediaKit and Mockly (2026-11-19, `scripts/i18n.py check`). The other 19 apps already had complete `pt` sets in
`assets/screenshots/<slug>/pt/` from commit 763463c («localized sets for 16 languages»), so their pages and OG cards
show Portuguese screenshots. Their headlines speak tu («Sabes ao certo…»), while the site copy is impersonal.
