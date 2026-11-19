# Keyword research, European Portuguese (Portugal)

Part of the language sheet `_i18n/pt.md`. Two research passes on 2026-11-19 (part 1: studio pages and ten apps; part 2: the other eleven apps). Sources: **G** = Google suggest (hl=pt-PT, gl=pt), **B** = Bing autosuggest (qsonhs, mkt=pt-PT), **A** = App Store search hints (storefront 143453-2,29, Portugal), **S** = iTunes Search API (country=pt). Every query was returned by one of them. People also ask was not collected. Search Console for Portugal was not read.

Decision recorded in the sheet: Millrace keeps `jogos de lógica iphone`; Tare takes `melhores jogos de puzzle iphone` and gives up `jogos de raciocínio iphone`, so the two pages do not compete.

## Part 1: studio pages, aftershift to millrace

Part of the language sheet `_i18n/pt.md` (to be written). Research pass on 2026-11-19, part 1: studio pages and ten apps.
Format follows `_i18n/es-keywords.md` and `_i18n/fr-keywords.md`.

Pages: Home, Apps hub, About, Support hub, Transparency, and the app pages aftershift, allpaid, appmeta,
appmeta-pulse, chessful, earnlock, gymlogger-x, liftlog, mediakit, millrace.

Source marks: **G** = Google suggest (hl=pt-PT, gl=pt), **B** = Bing autosuggest (mkt=pt-PT), **A** = App Store search
hints (Portugal storefront 143453), **S** = iTunes Search API (country=pt, lang=pt_pt), used only for competitor names and
the vocabulary in Portuguese app titles. Every query below was returned by one of these sources; nothing was invented.
"Echo" means the source returned only the seed itself back (proves the phrase exists, shows no tail demand). Google
usually returns the unaccented form ("ecra", "ginasio", "assinatura"); I write the accented form where the only
difference is the accent and keep the source mark. Search Console data for Portugal is not included.

## Method note

- **Requests: about 640**, 0.8 s apart. Main run 489 (G 287, B 151, A 31, S 20), a second run of gap-filling and
  question seeds 140 (G 55, B 55, A 16, S 14), plus about 8 probes (endpoint and storefront tests). 151 seeds on G and
  B; alphabet suffixes (a b c d e f g h i l m o p r s t v) on 8 seeds on G only: aplicação xadrez, app ginásio, app
  treino, app lembrete pagamentos, bloquear aplicações iphone, cancelar subscrição, comprimir vídeo iphone, jogos de
  lógica iphone. 47 short seeds on A. 34 searches on S. Scripts and raw JSON are in the session scratchpad, not the repo.
- **Google suggest: worked** (browser User-Agent needed). Alphabet suffixes were productive only for "app treino" (159
  distinct, but about 90 percent Brazilian: academia, treino de academia, pacto, smart fit, "treino hipertrofia"),
  "cancelar subscrição" (147, mostly Portuguese brands: meo, vodafone, benfica tv, element, solinca, holmes place, via
  verde, deco) and "app ginásio" (19, Portuguese gym-chain apps). They gave one or nothing for "aplicação xadrez" (1),
  "app lembrete pagamentos" (0), "bloquear aplicações iphone" (0) and "jogos de lógica iphone" (1). **Portugal
  localisation of G is weak**: hl=pt-PT gl=pt returns Brazilian forms ("assinatura", "celular", "aplicativo", "baixar",
  "academia", "senha", "tela", "treino de academia", "registrar") and Spanish forms in the same list ("cuanto tarda",
  "sin perder calidad", "comprimir un video", "desde iphone", "app treino ... por tiempo"). Each pick below is a phrase
  natural in Portugal; Brazilian and Spanish forms are noted as such and not recommended.
- **Bing (`api.bing.com/qsonhs.aspx?mkt=pt-PT&q=`): worked.** It is noisy: Brazilian phrasing, Spanish, German,
  French and English leak in. Many seeds return unrelated "como ..." questions. I did not use the osjson endpoint
  (the Spanish pass found it throttled).
- **App Store hints (`MZSearchHints`, `X-Apple-Store-Front: 143453-2,29`, `Accept-Language: pt-PT`): worked.**
  Suffixes `-2`, `-8` and `-1` returned identical Portuguese hints; I used `-2`. Hints are Portuguese (storefront
  title vocabulary: "Tempo de Ecrã", "Bloquear Aplicações", "Registo de Treinos", "Subscrições", "Ginásio",
  "Calendário de turnos"). Empty or noise for single-word generic seeds such as "sono" (Sonos) and "aso" (ASOS).
- **iTunes Search API (country=pt, lang=pt_pt): worked.** Our own Portuguese listings already show: "AfterShift:
  Sono & Turnos", "Chessful: Treinar & Analisar", "EarnLock: Bloquear Apps e Foco", "GymLogger X: Treino Tracker",
  "AllPaid - Gestão de Contas", "MediaKit Comprimir e Converter", "Millrace: Puzzle de peças".
- **People also ask: not collected** (it needs a live Google results page). FAQ items below come from question-style
  suggest ("como ...", "qual ...", "o que é ...") on G and B.
- **Weak or empty in Portuguese suggest:** "aplicações sem anúncios", "aplicações sem publicidade", "aplicações sem
  rastreamento", "aplicações sem subscrição" (all empty on G and B), the whole privacy and studio theme (Home, About,
  Transparency), every "sem subscrição" gym seed ("app ginásio sem subscrição", "app treino sem subscrição", "app
  treino pagamento único": empty on G, noise on B), "aplicações úteis iphone", "como limitar o tempo de ecrã" (B noise,
  G empty), "dormir depois de trabalhar à noite" (G empty), the earn-by-moving mechanic ("caminhar para desbloquear
  apps", "bloquear apps até fazer exercício": G empty, B generic unlock) and App Store Connect sales words ("relatórios de
  vendas app store", "receitas app store programador", "app store connect vendas": B returns shop-sales noise).
- **Vocabulary decisions for Portugal** (evidence in the sections):
  - Phone: "telemóvel" (B, G "vício do telemóvel"), never "celular". Screen: "ecrã" (G, A, S: "Tempo de Ecrã"), never
    "tela" (B "tempo de tela iphone" is Brazilian). Subscription: "subscrição" (G, A, S), not "assinatura" (G returns
    both; "assinatura" is Brazilian). App: "app" leads in casual and long-tail queries (G "app xadrez" 10 suggestions,
    "app treino"), "aplicação" is the Portugal formal word (G "aplicação de xadrez", "aplicação ginásio", "melhores
    aplicações para iphone"; A, S titles "Bloquear Aplicações"); "aplicativo" is Brazilian (B only). Gym: "ginásio"
    (G, A, S), never "academia" (G "app treino academia", Brazilian). Strength training: "treino de força" (G, S
    "Metric – Treino de Força"); "musculação" is returned (G `app musculação`) but it is Brazilian-leaning. Log: "registo"
    (A, S "Registo de Treinos"); G returned only the Brazilian "registrar" for the seed `app para registar treinos`.
    Beginners: "iniciantes" (G, Brazilian-leaning) and "principiantes" (G, the Portugal form) both appear. Developer:
    "programador" in Portugal, but G only returned "desenvolvedor" (Brazilian). File: "ficheiro" (B `como converter
    ficheiros heic para jpg`) vs "arquivo" (G/B, Brazilian). Download: "descarregar" (not returned), "baixar" Brazilian.
    Puzzle: "puzzle" (G, A, S), "quebra-cabeça" is Brazilian (S titles).
  - Apple's Portugal term for Screen Time is "Tempo de Ecrã" (G `tempo de ecrã iphone`, A, S); Brazil says "Tempo de Uso".
- **Spanish bleed to avoid:** G for MediaKit seeds (`comprimir video en iphone`, `comprimir tamaño video iphone`) and
  support seeds (`reembolso app store cuanto tarda`, `pedir reembolso apple suscripcion`) is Spanish. Not picked.

---

## Home (/pt/): studio of calm, privacy-first Apple apps

- **Primary:** `apps sem anúncios` (weak). Exact "aplicações sem anúncios" and "aplicações sem publicidade" returned
  nothing on G or B. The real shape of the demand is B `app youtube sem anúncios`, `app ouvir música sem anúncios`,
  `aplicativo de música sem anúncio` and A `jogos sem anúncios`, `bare: navegador sem anúncios`. Use "sem anúncios"
  (not "publicidade", which only appeared inside "bloquear publicidade" on A).
- **Secondary:** `jogos sem anúncios iphone` (G; also `melhores jogos sem anuncios iphone`, G); `apps privadas iphone`
  (G, echo only; different audience, hiding apps); `aplicações para iphone` (G, B, a generic head).
- **FAQ-style (from suggest):** none on topic. Nearest: `como instalar apps sem conta google` (G, Android, irrelevant).
- **Notes:** brand and trust page, not a keyword page. "Sem rastreamento", "respeita a privacidade", "sem subscrição",
  "sem registo" returned nothing. B for "aplicações que respeitam a privacidade" gave definitions of privacy ("o que é
  a privacidade online"). App Store titles do use "privacidade" for VPN and ad-block apps (A: "vpn de privacidade",
  "avast vpn proxy e privacidade"), so the word is a security-product word. "Sem subscrição" is allowed on the site only
  for LiftLog, Millrace, Mockly and Tare (house rule), and has no suggest evidence anyway.

## Apps hub (/pt/apps/): all apps

- **Primary:** `melhores apps iphone` (G with 10 suggestions; B `melhores apps iphone`, `melhores apps para iphone`).
- **Secondary:** `melhores aplicações para iphone` (G, from the seed "aplicações para iphone"; B echo of the seed
  `melhores aplicações iphone` was empty); `melhores aplicações apple watch` (G; B `melhores apps apple watch`);
  `aplicações para mac` (G; also `aplicações para macbook`, `aplicações mac`, G); `melhores aplicações para ipad`
  (G echo).
- **FAQ-style (from suggest):**
  - melhores apps iphone grátis (G)
  - melhores apps pagos iphone (G)
  - melhores apps exclusivos iphone (G)
  - aplicações iphone grátis (G)
  - melhores aplicações para apple watch (G)
  - como fechar aplicações no iphone (B)
- **Notes:** G adds model names and years ("iphone 17", "2025", "2026", "17 pro max"): avoid dated titles. B for
  "melhores aplicações mac" returned finance and study noise (banco do brasil, "a longo prazo"). G mixes in "apps iptv
  iphone" and series-streaming tails. A hints for the generic words "apps"/"aplicações" are app titles ("apps de
  estudo", "appraven: aplicações gratuitas"). Both "apps" and "aplicações" are typed; use "aplicações" in the
  title and "apps" in body copy.

## About (/pt/lagerland-apps/): one-person studio

- **Primary:** brand ("Lagerland Apps"). No real query exists. Closest real phrases: `desenvolvedor de aplicações`
  (G, job-search intent: "móveis com android", "para ios") and `desenvolvedor independente` (G echo only).
- **Secondary:** `desenvolvedor de aplicações` (G); `desenvolvedor de aplicações para ios` (G); `programador
  independente` (B echo only; B for "programador de aplicações" and "programador indie" came back Spanish:
  `programador de aplicaciones`, `programador independiente`).
- **FAQ-style:** none on topic.
- **Not usable:** `estúdio de aplicações independente`, `estúdio de apps independente` (B: study-plan noise, "estúdio" is
  read as "estudo"); `estúdio de jogos independente` (B: Brazilian game studios); `criador de apps iphone` (B: AI app
  builders); `desenvolvedor de apps ios` (B: "modo desenvolvedor ios", Android developers).
- **Notes:** Portugal says "programador" but Google only returned the Brazilian "desenvolvedor"; use "programador
  independente" in prose, "estúdio" only with "apps". "Indie" is not returned as a developer word. "Freelancer" not tested.

## Support hub (/pt/support/)

- **Primary:** `cancelar subscrição iphone` (G, `cancelar subscrição app iphone`; B `como cancelar subscrição iphone`).
  Strongest support-type demand, and "subscrição" is confirmed as the Portugal word (the Brazilian twin `cancelar
  assinatura iphone` also returns 10 suggestions on G).
- **Secondary:** `reembolso app store` (G, 10 suggestions; B `solicitar reembolso app store`); `cancelar subscrição app
  store` (G echo; B `cancelar compra app store`); `restaurar compras app store` (G echo only; B returned noise).
- **FAQ-style:**
  - como cancelar uma subscrição no iphone (G)
  - como cancelar subscrição no telemóvel iphone (G)
  - como cancelar subscrição de app no iphone (G)
  - como cancelar subscrição na app store (G echo)
  - como ver subscrições apple (G echo)
  - ver subscrições iphone (G echo)
  - como pedir reembolso app store (G, B)
  - reembolso app store quanto tempo (G)
  - como pedir reembolso de um jogo na app store (G)
  - como restaurar compras no iphone (G)
  - como cancelar uma compra na app store (B)
  - histórico de compras app store (G unaccented)
  - contactar suporte apple portugal (G)
- **Notes:** nearly all returned demand is per-service ("cancelar subscrição netflix, spotify, chatgpt, meo, vodafone, hbo
  max, benfica tv, element, solinca ..." G alphabet pass), so the hub competes on the Apple-wide phrase only. "A App Store"
  is feminine in Portugal ("na app store", G, B). B returned Brazilian `como cancelar assinatura no iphone` and Spanish
  forms. "Restaurar compras" has no Portuguese demand beyond the echo ("restaurar" on A is photo restoration; B read
  it as restoring the iPhone or the Microsoft Store). "Reembolso" is the word in G, B and A.

## Transparency (/pt/transparency/): tracking, SDKs, privacy manifests

- **Primary:** `app tracking transparency` (G, B `app tracking transparency att`). Same as Spain: Portuguese users type
  the English Apple term, plus developer tails (flutter, expo, framework, permission request).
- **Secondary:** `privacy manifest` (G, B, English, developer audience); `app tracking transparency iphone` (G);
  `rastreamento de apps iphone` (G echo; "rastreamento" is Brazilian, "rastreio" is the Portugal word but returned only
  parcel tracking on A and B).
- **FAQ-style:**
  - what is app tracking transparency (B, English even for the Portuguese seed `o que é o app tracking transparency`)
  - tracking o que é (B)
  - o que é o tempo de ecrã (G, B; adjacent topic)
- **Not usable:** `aplicações que me rastreiam`, `pedir à aplicação para não rastrear`, `permitir que as apps rastreiem`
  (B: phone-tracking and parcel apps); `etiquetas de privacidade app store` (G empty; B: label-printing apps); `que
  dados recolhem as apps` (G empty; B: data-recovery apps); `apps que não recolhem dados` (B: data-recovery); `como
  saber se uma app é segura` (G empty; B returned Spanish and Brazilian twins `como saber se um aplicativo é seguro`);
  `o que é um privacy manifest` (B: "o que é o privacy" adult-site noise).
- **Notes:** developer terms stay English ("privacy manifest", "SDK", "App Tracking Transparency"; B `itms-91061 missing
  privacy manifest`). Apple's own Portugal wording for the OS prompt comes from the OS, not from a query. Demand is thin;
  this is a trust page.

---

## AfterShift (shift-work sleep)

- **Primary:** `como dormir de dia quem trabalha a noite` (G, unaccented as returned; accented "à noite" in copy).
  The shorter head `como dormir de dia` (G, B) is dominated by unrelated tails (diarreia, trança), so keep the long form.
- **Secondary:** `como recuperar o sono de quem trabalha a noite` (G; also `como recuperar sono perdido`, `como recuperar
  o sono atrasado`, G); `dívida de sono` (G; also `calcular divida de sono`, `divida de sono existe`, G);
  `distúrbio do sono trabalho por turnos` (G; Brazilian "distúrbio", the Portugal "perturbação" returned nothing).
- **FAQ-style:**
  - como dormir de dia quem trabalha a noite (G)
  - como recuperar o sono de quem trabalha a noite (G)
  - como recuperar sono perdido (G, B)
  - tem como recuperar sono perdido (G)
  - trabalho noturno e sono (G)
  - sono no trabalho o que fazer (B; sleepiness at work, different intent)
  - quais os turnos de trabalho (B)
  - trabalho por turnos legislação / código do trabalho / reforma / folgas (G; legal intent, a neighbouring audience)
- **Competitors (S/A):** Sono do trabalho em turnos, Lueur: Sono por turnos, Shiftlight: Sono por turnos, ShiftNight:
  Monitor de Sono, Rooster: Alarme Sono Pesado, Beepo: Despertador e Turnos, Daynori: Despertador e Turnos. Roster apps
  (different intent): Calendário de turnos (Shifter), WorkTime: Calendário Turnos, Supershift Escala de trabalho,
  Shift2Cal Calendário Turnos, Turnify, RotaFlow: Escala de Trabalho, Calendário Turno - Agenda; A hints for "turnos":
  calendário de turnos, calendário turnos de trabalho, horário turnos, "shiftmonth: horário de turnos". Our listing:
  "AfterShift: Sono & Turnos".
- **Not usable:** `dormir depois de trabalhar à noite`, `dormir depois do turno da noite`, `app sono turnos`, `app
  horário turnos` (G empty; B: "dormir a noite ou dormir à noite", roster apps). `turno da noite` (G, B) is dominated
  by the Stephen King film and series "Turno da Noite" and by workers' rights ("direitos"). `perturbação do sono trabalho
  por turnos` (G empty; B: sleepiness at work). `aplicação sono` (G) returns baby-sleep, Sonoff and sound apps.
- **Notes:** "trabalho por turnos" is the Portugal word (G head with 10 suggestions, all legislation, reforma, folgas);
  "trabalho noturno" appears but is the Brazilian-leaning form. The roster word on the store is "calendário de turnos" and
  "escala". Keep "a noite" vs "à noite" in mind: Google returns the unaccented form.

## AllPaid (bill reminders, no bank login)

- **Primary:** `app lembrete de pagamento` (G echo). Title vocabulary agrees: S "Lembrete de pagamentos",
  "Avizai - Lembrete de Pagamento", "Billo: Lembretes de Contas", "Lembrete de Contas a Pagar".
- **Secondary:** `app para lembrar pagamentos` (G echo; B `aplicativo para lembrar de pagar contas`); `app lembrete de
  contas a pagar` (G, B); `app para nao esquecer de pagar contas` (G echo).
- **FAQ-style:**
  - app para não esquecer de pagar contas (G)
  - app contas a pagar (G)
  - app despesas fixas (G echo)
  - melhor app finanças pessoais (G)
  - app finanças pessoais portugal (G)
  - lembrete de fatura vencida (B)
- **Competitors (S/A):** Avizai - Lembrete de Pagamento, Lembrete de Contas a Pagar, Lembrete de pagamentos, Billo:
  Lembretes de Contas, Drip: Lembretes e Faturas; subscription trackers: Subby: Gestor de Subscrições, Duly: gestor de
  subscrições, Gerir Subscrições: SubIQ, ReSubs, Gestão de Subscrições, Seguidor de Subscrições, Subscrições: SubClock,
  Despesas e Subscrições; A "subscrições": "controlo de subscrições", "calendário de subscrições", "cancelar subscrições &
  gerir". Our listing: "AllPaid - Gestão de Contas".
- **Not usable:** `lembrete de faturas`, `app renovação contratos`, `aplicação controlar subscrições`, `app subscrições
  iphone`, `app gestão de subscrições` (G empty; B: stock-subscription noise "subscrição de ações"). `app contas a pagar`
  (G) is mostly business accounts-payable and Brazilian ("pessoal", "empresa", "controle").
- **Notes:** "faturas" in Portugal is mostly invoices you issue or e-Fatura validation (S "Criar Faturas", A "validar
  faturas", "e fatura"); for household bills prefer "contas" ("pagar as contas") and "pagamentos". "Subscrição" is the
  Portugal word for subscriptions (A, S). "Contas a pagar" in a title suggests business accounting. "Sem login bancário"
  was not tested.

## AppMeta (App Store Connect for Mac)

- **Primary:** `app store connect mac app` (G; also `app store connect macos`, `app store connect mac download`, G).
  Caution: collides with the consumer error `app store cannot connect mac`, same as in Spain.
- **Secondary:** `aso app store optimization` (G; also `aso app store keywords`, `aso app store screenshots`, `aso app store
  optimization tools`, G); `criar conta app store connect` (G; B `app store connect criar conta`); `app store connect
  api key` (G, B).
- **FAQ-style:**
  - app store connect login (G, B)
  - criar conta app store connect (G, B)
  - what is app store connect (B; English even for the Portuguese seed)
  - app store connect download (B)
- **Competitors (S/A):** Helm for App Store Connect, Lumetric for App Store Connect, AppDab, Big Bucks (A, "for App
  Store Connect"); ASO.dev: Copilot para Connect, ASO Scout, KWRDS ASO Rank Keyword Tracker, Rankify: ASO Rank Analytics,
  AppVisor – ASO & App Intel, Seenlab – ASO App Rank Tracker, AppBoom: App Sales & ASO Tools, "ASO - App Keywords
  Otimization" (S); Apple's own App Store Connect, Apple Developer, TestFlight.
- **Not usable:** `palavras-chave app store`, `otimização app store`, `metadados app store`, `app store connect o que é`
  (G empty; B: "o que é app store", "não foi possível conectar a app store", Windows `pc app store`).
- **Warning:** the bare term `aso` is an occupational-health certificate in Brazilian Portuguese: G `aso o que é` returns
  "aso admissional", "atestado aso", "aso exame". Keep "ASO" always next to "App Store" (`aso app store`, G).
- **Notes:** developers in Portugal search in English ("app store connect", "aso app store optimization"). Keep "App
  Store Connect", "ASO", "metadata" in English in the title; the Portuguese body can say "palavras-chave" and "metadados"
  without keyword evidence. A name clash exists in S: a different app is called "MediaKit : ASO Studio" (see MediaKit).

## AppMeta Pulse (App Store Connect dashboard on iPhone)

- **Primary:** `app store connect iphone` (G; also `app store connect iphone only`, `app store connect login iphone`, G).
- **Secondary:** `app store connect api` (G, B; also `app store connect api key`, `api analytics`, `api customer reviews`,
  G); `app store connect ios` (G; also `app store connect analytics ios version`, G); `app store connect widget` (G echo).
- **FAQ-style:** `app store connect login` (G, B); `app store connect status` (G); `what is app store connect` (B).
- **Competitors (S/A):** Helm, AppDab, Lumetric, Big Bucks (all "for App Store Connect", A, S); AppBoom: App Sales & ASO
  Tools (S).
- **Not usable:** `relatórios de vendas app store`, `receitas app store programador`, `app store connect vendas`, `app
  vendas app store`, `widget app store connect` as a Portuguese phrase (G echo only; B returned English "what is an app
  widget"): the Portuguese money words returned only shop-sales and receipt noise (B: "app de estoque e vendas", "relatório
  de vendas shopee", "app de receitas culinárias").
- **Notes:** collision with the consumer error "app store cannot connect iphone" on G (as in Spain); keep "dashboard",
  "vendas" and the developer angle in the title. **Overlap flag:** AppMeta and AppMeta Pulse both sit on the `app store
  connect` head. Primaries kept distinct: appmeta = `app store connect mac app`, pulse = `app store connect iphone`;
  `app store connect api` is a shared secondary and should go to the Pulse page only (the MCP and API-key angle).

## Chessful (chess learning and analysis)

- **Primary:** `app xadrez` (G with 10 suggestions: gratis, offline, sem anuncios, para iniciantes, online com amigos).
  The formal twin `aplicação de xadrez` returned only its own echo on G (alphabet pass gave 1) and nothing on B.
- **Secondary:** `melhor app de xadrez` (G with 10 suggestions: para iphone, offline, para iniciantes, gratuito);
  `app para aprender xadrez` (G with 9; B `aprender a jogar xadrez`, `xadrez jogar e aprender`); `análise de partidas de
  xadrez` (G, B; B also `analisador de partida de xadrez`, `analisar partida de xadrez gratis`).
- **FAQ-style:**
  - como melhorar no xadrez (G, B)
  - como melhorar no xadrez rapido (G)
  - aprender xadrez passo a passo (G, B)
  - aprender xadrez do zero (G)
  - aprender xadrez jogando (G, B)
  - melhor app de xadrez para iphone (G)
  - melhor app de xadrez para iniciantes (G)
  - melhor app de xadrez offline (G)
  - app xadrez sem anuncios (G)
  - xadrez para principiantes (G, B; Portugal form)
  - xadrez para iniciantes (G, B; Brazilian-leaning, more suggestions)
  - stockfish o que é (G)
  - análise de partidas de xadrez gratuito (G)
- **Competitors (S/A):** Xadrez - Jogar e Aprender, Xadrez - Jogo Offline, Chess Room-Xadrez, ChessBot: Assistente Xadrez
  IA, PVChess: Professor de Xadrez, Lotus Chess – Treinos, Learn Chess with Dr. Wolf, Magnus Trainer, Lichess, Análise
  Xadrez: Chess AI, ChessWOW: Stockfish 19 Análise, Xadrez – Tabuleiro de Análise, Xadrez Analise Chess - SCG, Chess
  Engine - ChessFox, Stockfish AI Chess; A hints for "xadrez": xadrez online, offline, para dois, grátis, "xadrez: aprenda,
  jogue, treine", temporizador xadrez, relogio xadrez. Our listing: "Chessful: Treinar & Analisar".
- **Not usable:** `aplicação para treinar xadrez`, `melhor aplicação de xadrez`, `jogar xadrez iphone`, `aplicação para
  aprender xadrez`, `app de xadrez gratuita` (G empty; B PC downloads and web sites). `xadrez iphone` (G) is phone cases
  ("capinha xadrez iphone"). `app xadrez brasil` (G) is Brazilian.
- **Notes:** "xadrez" is the word; "partidas" for games; B and G often show "pc", "android" and "download" as device words,
  so the iPhone intent has to be on the page. "Stockfish" typed as-is (`stockfish`, `stockfish o que é`, `stockfish xadrez`).
  "Aplicação" is rare here; use "app" in the title and "aplicação" in body copy.

## EarnLock (earn screen time by moving: app blocker)

- **Primary:** `bloquear apps iphone` (G with 10 suggestions: por tempo, com senha, face id, por horário; B `como bloquear
  apps no iphone`). A hint `bloquear aplicações` returns many titles (see competitors).
- **Secondary:** `tempo de ecrã iphone` (G, 10 suggestions; A "tempo de ecrã" gives titles); `limite de apps iphone` (G; also
  `limite de tempo apps iphone`, `como colocar limite de tempo nos apps iphone`); `bloquear instagram iphone` (G; also
  `app para bloquear instagram iphone`).
- **FAQ-style:**
  - como bloquear apps no iphone (G, B)
  - como bloquear apps no iphone por um tempo (G)
  - como bloquear apps com face id no iphone (G)
  - como colocar limite de tempo nos apps iphone (G)
  - tempo de ecrã iphone não funciona (G)
  - código tempo de ecrã iphone (G)
  - desativar tempo de ecrã iphone (G)
  - o que é o tempo de ecrã (G, B)
  - tempo de ecrã recomendado (B)
  - como deixar o vício do telemóvel (G)
  - vício no telemóvel (B)
- **Competitors (S/A):** one sec | menos tempo de ecrã, Unwind - Bloqueador de Apps, Clarymind: Tempo de Ecrã Foco,
  Reduzir Tempo de Ecrã: Pausi, Enso: Tempo de Ecrã & Bloqueio, Ticking: Tempo de Ecrã e Foco, Thrive - Tempo de ecrã smart,
  Foccus: Bloqueio Tempo de Ecrã, Pausewall: Bloquear Aplicações, Braino: Bloqueio de Aplicações, Blokr, Bloquear Aplicações:
  Calma / Focus / Paradox / No Scroll, Disconnect: Bloquear Apps; **earn-by-exercise rivals exist in the Portugal store**:
  Fit to Scroll: App Blocker, RepScroll: Tempo de Ecrã, HabitUnlock: Tempo de Ecrã, Flexões Abrem Apps: RepUnlock, RepLock:
  Bloqueie apps, LockInFit: Bloqueia Apps, SquatKey - Bloqueia Apps, SweatPass: Tempo de Ecrã, Budli. Our listing:
  "EarnLock: Bloquear Apps e Foco" (S also returns the near-name "Earnlocker: App Blocker").
- **Not usable:** `bloquear aplicações iphone` (G empty; B Spanish `bloquear aplicaciones iphone`); `bloqueador de
  aplicações iphone` (B: iPhone activation lock, call blockers); `como limitar o tempo de ecrã` and `limitar tempo de
  ecrã` (G empty or one iphone echo; B: PC and Windows screen time); `app para usar menos o telemóvel`, `app para deixar o
  telemóvel` (B: phone-finder noise); `caminhar para desbloquear apps`, `bloquear apps até fazer exercício` (G empty; B:
  generic unlock): the earn-by-moving idea has no suggest demand. A `bloqueador` hints are ad blockers and call blockers.
- **Notes:** "Tempo de Ecrã" is the Portugal term (G, A, S); B also returns Brazilian `tempo de tela iphone` and `tempo de
  uso iphone`. Use "tempo de ecrã" once with "bloquear apps". Most G suggests for screen time are about removing the code
  or fixing the feature. "Bloquear" is the verb; "bloqueio de apps" in titles. Parental control is another audience (out of
  scope).

## GymLogger X (strength workout tracker with Apple Watch)

- **Primary:** `app treino apple watch` (G; also `melhor app treino apple watch`, `app treino academia apple watch`,
  `app treino corrida apple watch`, `app treino intervalado apple watch`, G; B `treino intervalado apple watch`).
- **Secondary:** `app treino de força` (G; also `treino de força em casa app`, G); `app musculação apple watch` (G; a
  Brazilian-leaning form, but the only strength-plus-watch tail returned); `app treino ginásio grátis` (G; also `app
  ginásio grátis`, G).
- **FAQ-style:**
  - melhor app treino apple watch (G)
  - melhor app de ginásio (G unaccented)
  - melhor app de treino grátis (G)
  - app para montar treino (B)
  - plano de treino ginásio (A, B)
  - plano de treino ginásio iniciantes (B)
  - app para registar treinos (the seed returned `app para registrar treinos`, G, Brazilian spelling)
  - melhor app para musculação iphone (G)
  - app treino iphone (G; also `app treino gratis iphone`, `app para montar treino iphone`, G)
- **Competitors (S/A):** Hevy: Treino de Ginásio, Lyfta: Gym e Plano de Treino, Gym Day: Treino de Ginásio, Treino de ginásio -
  Strive, Pro Fitness: Treino de ginásio, Treino Ginásio - Fitonist, Symmetry: Registo de Treinos, GYMZO: Registo Treino
  Ginásio, Gymaroo - Registo de Treinos, Progression: Diário de Treinos, Alpha Progression Musculação, Metric – Treino de
  Força, BTB Diário Treino e Academia, Logr: Plano de Treino Ginásio, Liftly: Plano de Treino e Gym, GymStreak: Plano de
  Treino IA, SmartGym, WLog, Gym Log Track Registro Treino, ZEUS Gym Logger; A for "ginásio": "treino de ginásio", "plano de
  treino ginásio". Our listing: "GymLogger X: Treino Tracker".
- **Not usable:** `app ginásio apple watch` (G empty; B `ghin app apple watch`, golf); `registar treinos apple watch` (B:
  Apple Watch charging noise); `app registo treino ginásio` (G empty; B plan templates). `app ginásio` alone (G) is
  dominated by Portuguese gym-chain apps (element, be fit, physical, supera, ttf, huc), and `app treino` alphabet (G) is
  about 90 percent Brazilian chain and creator names (pacto, smart fit, bluefit, panobianco, trinca, "ramon dino").
- **Notes:** Portugal says "ginásio" and "treino", "treino de força" for strength, "registo" for log (A, S titles) although
  G only returned "registrar". "Apple Watch" stays English. "Academia" in G is Brazilian (`app treino academia`): do not
  use. "Gym" appears in titles ("Gym Day", "Lyfta: Gym e Plano de Treino"). **Shared pool with LiftLog**, primaries differ.

## LiftLog (lifting log, one purchase, no subscription)

- **Primary:** `app treino ginásio` (G alphabet pass `app treino ginasio`; `app treino ginásio grátis`, G). The strict
  "sem subscrição" phrase has no evidence, so the differentiator goes in the title as copy, not as the keyword.
- **Secondary:** `app plano de treino ginasio` (G alphabet) / `plano de treino ginásio` (A, B); `app para apontar treinos` (G
  echo; B shows `app para montar treino`); `diário de treino app` (G, `app para diario de treino`).
- **FAQ-style:**
  - melhor app de ginásio (G)
  - melhor app ginasio (G)
  - app exercicios ginasio (G)
  - app para treino ginasio (G)
  - melhor app de treino grátis (G)
  - app de treino bom e gratuito (G)
  - plano de treino ginásio (A, B)
- **Competitors (S/A):** same pool as GymLogger X (Hevy, Lyfta, Symmetry: Registo de Treinos, Progression: Diário de Treinos,
  Gym Day, Fitonist ...). **Name collisions in S for "liftlog"**: "LiftLog", "Lift Log — Diário de treino", "Treino de
  Ginásio: Liftlog+", "LiftLog - Gym Workout Tracker", "Lift Log: #1 Weightlifting Log", "No-Frills Lift Log", "LiftLog -
  Strength Workout Log": the brand name alone will not surface our page.
- **Not usable (with note on demand):** every "sem subscrição" and "pagamento único" gym seed returned nothing on G
  (`app ginásio sem subscrição`, `app treino sem subscrição`, `app treino pagamento único`) and noise on B ("como abrir um
  ginásio", Italian "app io metodi di pagamento"). `aplicações sem subscrição` was empty too. `app registo ginásio` (G
  empty). `app de pesos` (G: pesos = currency, "app de pesos a dolares"). So the Portugal differentiator has no keyword
  demand; "grátis" has plenty (`app treino ginásio grátis`, `melhor app de treino grátis`, G), which contradicts a paid-once
  offer: state the 7-day free trial only as far as the master file allows.
- **Notes:** "registo" is the Portugal word for log (A, S) but G never returned it. "Pesos" means weights (the sport) only
  with "gym"; avoid it as the keyword.

## MediaKit (compress/convert video, images, PDF on device)

- **Primary:** `comprimir vídeo iphone` (G `comprimir video iphone`, with Portuguese tails `comprimir video pelo iphone`,
  `comprimir video galeria iphone`, `comprimir vídeo iphone gratis`, `online`; B echo). Spanish tails in the same list
  (`archivo`, `sin perder calidad`, `un video`, `desde iphone`) are not usable.
- **Secondary:** `comprimir pdf iphone` (G with 8 suggestions, B `como comprimir pdf no iphone`); `converter heic para jpg`
  (G with 10: no iphone, em lote, perde qualidade; B with 8); `reduzir tamanho vídeo whatsapp` (G, B; B also `tamanho máximo
  de vídeo no whatsapp`); `converter vídeo para mp4 iphone` (G; `converter mov para mp4 no iphone`, G).
- **FAQ-style:**
  - como comprimir vídeo no iphone (G; B returned Spanish `cómo comprimir un video en iphone`)
  - como comprimir pdf no iphone (G, B)
  - como diminuir pdf no iphone (B)
  - como converter heic para jpg (G, B)
  - como converter heic para jpg no iphone (G)
  - como converter heic para jpg sem perder qualidade (G, B)
  - como converter ficheiros heic para jpg (B; "ficheiros" is the Portugal word)
  - converter mov para mp4 no iphone (G)
  - reduzir tamanho pdf sem perder qualidade (G, B)
  - reduzir tamanho video para whatsapp (G, B)
  - compressor de vídeo para whatsapp (G)
  - converter áudio iphone em mp3 (B)
- **Competitors (S):** video: Comprimir vídeo - Encolher, Comprimir Video e Foto, Comprimir Vídeo e Fotos Master, Compressor
  de Vídeo Fácil, Vídeo Conversor e Compressor, Compressão de Vídeo, Comprimir Fotos Vídeos Reduzir, Panda Video Compress &
  Convert; PDF: Comprimir PDF－Reduzir PDF, Reduzir PDF, Comprimir PDF: Reduzir Tamanho, iLovePDF, Adobe Acrobat Reader; HEIC:
  Conversor HEIC para JPG/PNG, Conversor HEIC de foto e vídeo, Image Converter: HEIC-JPG-PNG; A hints for "comprimir": comprimir
  pdf, comprimir video, "converter e comprimir fotos", "comprimir fotos: compressor"; for "converter": converter para pdf,
  converter vídeo em áudio e mp3, converter foto para pdf. Our listing: "MediaKit Comprimir e Converter".
- **Not usable:** `comprimir imagem iphone` (G: echo and `como comprimir imagem pelo iphone`; B empty), `converter áudio iphone`
  (G/B: Lightning jack and Spanish noise). **Name collision in S:** a different app is called "MediaKit : ASO Studio" (a
  developer ASO tool) and other "Media Kit" apps are creator kits; the brand alone is ambiguous, so the title must carry
  "comprimir e converter".
- **Notes:** most G tails are web tools (online, gratis, ilovepdf, adobe, canva, windows). "Comprimir" is the verb,
  "reduzir tamanho" second, "compressor" the tool, "converter" for formats. WhatsApp is the common destination. There is no
  Portuguese demand for "mac" in these queries (only `comprimir vídeo mac`, G, with Spanish tails).

## Millrace (tile-delivery logic puzzle; house rule applies)

- **Primary:** `jogos de lógica iphone` (G `jogos de logica iphone`, `jogos de logica para iphone`). The head `jogos de
  lógica` is huge but dominated by kids, programming, printables and web games (B: "para crianças", "online", "de programação",
  "matemática"); the iPhone form isolates app intent.
- **Secondary:** `jogos de raciocínio lógico iphone` (G `jogos de raciocinio iphone`, `jogos de raciocínio lógico iphone`);
  `jogos de puzzle iphone` (G `jogos puzzle iphone`, `melhores jogos de puzzle iphone`); `jogos sem anúncios iphone` (G
  `jogos sem anuncios iphone`, `melhores jogos sem anuncios iphone`; B `jogos grátis sem anúncios`).
- **FAQ-style:**
  - melhores jogos de puzzle iphone (G)
  - melhores jogos de lógica (G)
  - melhores jogos sem anuncios iphone (G)
  - jogos sem internet iphone (G)
  - melhores jogos sem internet iphone (G)
  - jogos offline sem internet iphone (G)
  - jogos de raciocínio lógico para adultos (G)
  - melhores jogos para iphone (B)
  - puzzles de lógica (G, B; "puzzles" is the Portugal plural)
- **Competitors (S/A):** Logic Puzzles: Jogos de Lógica, Cross Logic - Quebra-Cabeça, IQ Masters: Enigmas de Mentais, Paper
  Fold: jogo de lógica, Tricky Castle: Jogos de lógica, Hexa Shift - Jogo de lógica, Ring Master: Jogo de Lógica, Pawdoku –
  Puzzle de lógica, Arrows Puzzle: Lógica, Connect Tracks: Puzzle Lógico, Shape Escape: Puzzle de Blocos, Sudoku.com - Puzzle
  clássico, Number Match: Jogos de números, Impulse - Jogos para o cérebro; A hints for "jogos de lógica": Twiro, Arcadeflow,
  Clues by Sam, Cuca Fresca, Desatar, Evo Puzzle, Fallacy ("Nome: jogos de lógica"); A "puzzle": puzzle games, puzzle de setas.
  Our listing: "Millrace: Puzzle de peças". Name collisions in S for "millrace": "Millrace Motor Club", "Millrace Scan".
- **Not usable:** `jogos de lógica sem anúncios`, `jogos de puzzle ipad`, `jogos de lógica para telemóvel`, `jogos de
  números iphone` (G empty; B generic web-game and kids tails); `quebra-cabeça` is Brazilian (S titles). No query involving
  the banned former name was recorded; none was used as a seed.
- **Notes:** title patterns "Nome: jogos de lógica", "Nome: puzzle de lógica". Both "puzzle" (Portugal) and "quebra-cabeça"
  (Brazil) appear; use "puzzle". "Jogos de raciocínio" is a real Portugal phrase (G, A "jogos de raciocínio"); "jogos sem
  internet" has large demand (G, B), so the page can say offline. Avoid the head phrase "jogos de lógica" alone.

---

## Summary table

Flags: "(weak)" = no or echo-only suggest evidence for the primary; page ranks on brand or trust.

| Page | Primary | Secondary 1 | Secondary 2 | Secondary 3 |
|---|---|---|---|---|
| Home | apps sem anúncios (weak; B, A) | jogos sem anúncios iphone (G) | aplicações para iphone (G, B) | |
| Apps hub | melhores apps iphone (G, B) | melhores aplicações para iphone (G) | melhores aplicações apple watch (G) | aplicações para mac (G) |
| About | brand "Lagerland Apps" (weak; closest: desenvolvedor de aplicações, G) | desenvolvedor de aplicações para ios (G) | programador independente (B echo) | |
| Support hub | cancelar subscrição iphone (G, B) | reembolso app store (G, B) | cancelar subscrição app store (G) | restaurar compras app store (G echo) |
| Transparency | app tracking transparency (G, B) | privacy manifest (G, B) | app tracking transparency iphone (G) | |
| aftershift | como dormir de dia quem trabalha a noite (G) | como recuperar o sono de quem trabalha a noite (G) | dívida de sono (G) | distúrbio do sono trabalho por turnos (G) |
| allpaid | app lembrete de pagamento (weak; G echo, S titles) | app para lembrar pagamentos (G echo) | app lembrete de contas a pagar (G, B) | |
| appmeta | app store connect mac app (G) | aso app store optimization (G, B) | criar conta app store connect (G, B) | |
| appmeta-pulse | app store connect iphone (G) | app store connect api (G, B) | app store connect ios (G) | |
| chessful | app xadrez (G) | melhor app de xadrez (G) | app para aprender xadrez (G, B) | análise de partidas de xadrez (G, B) |
| earnlock | bloquear apps iphone (G, B, A) | tempo de ecrã iphone (G, A) | limite de apps iphone (G) | bloquear instagram iphone (G) |
| gymlogger-x | app treino apple watch (G) | app treino de força (G) | app musculação apple watch (G) | |
| liftlog | app treino ginásio (G) | plano de treino ginásio (A, B) | diário de treino app (G) | |
| mediakit | comprimir vídeo iphone (G) | comprimir pdf iphone (G, B) | converter heic para jpg (G, B) | reduzir tamanho vídeo whatsapp (G, B) |
| millrace | jogos de lógica iphone (G) | jogos de raciocínio lógico iphone (G) | jogos de puzzle iphone (G) | jogos sem anúncios iphone (G) |

**Overlap flags**

- appmeta and appmeta-pulse share the `app store connect` head; primaries are distinct (`mac app` vs `iphone`); give
  `app store connect api` to Pulse only.
- gymlogger-x and liftlog share the gym pool; primaries distinct (`app treino apple watch` vs `app treino ginásio`);
  `melhor app de ginásio` and `plano de treino ginásio` should not be a title target on both.
- Home and Millrace both touch "sem anúncios" (Home generic apps, Millrace `jogos ... sem anúncios iphone` as a
  secondary): no clash if Home keeps the studio angle.
- Home and Apps hub are both generic head phrases; Hub takes `melhores apps iphone`, Home takes the studio/no-ads angle.
- No two pages share a primary.

## Failures and gaps

- No hard endpoint failures this run (G, B, A, S all returned). Bing osjson was not tried.
- Portuguese suggest returned nothing for the Home, About and Transparency themes and for every "sem subscrição" seed.
- People also ask not collected (needs a live results page). Search Console for Portugal not read.
- hl=pt-PT gl=pt did not isolate European Portuguese: Brazilian and Spanish forms appear throughout and were filtered by hand.
- The shared scratchpad was also used by other sessions (another process overwrote `run.log`); my result files
  (`out.json`, `p1x/out2.json`) were intact (counts matched my run).

## Part 2: mockly to clippet (European Portuguese, Portugal)

Tier 1 app pages: Mockly, Observa, Pawza, RightSplit, Shogiful, Soon., Tare, Taskful Day, WanderWiki, Xiangqiful,
Clippet. Format follows `_i18n/es-keywords.md` and `_i18n/fr-keywords.md` Part 2.

Collected 2026-11-19. Source marks: **G** = Google suggest (hl=pt-PT, gl=pt), **B** = Bing autosuggest (mkt=pt-PT),
**A** = App Store search hints (Portugal storefront 143453), **S** = iTunes Search API (country=pt, lang=pt_pt), used
only for competitor names and the vocabulary in Portuguese app titles. Every query below was returned by one of these
sources; nothing was invented. Accents are kept as the source returned them: Google mostly returns the unaccented form
(`historico area de transferencia iphone`, `wikipedia aleatória`) and sometimes the accented one; Bing and the App Store
mostly accent. Search Console data is not included.

## Method note

- **Requests: 1,018 in the main run** (G 470, B 470, A 45, S 33), plus 9 probes (1 G, 1 B, 6 A, 1 S) to test the
  endpoints. About 0.8 s between requests. Script: `pt_kw2.py` in the session scratchpad (not in the repo). Seeds per
  app (12 to 22 each), plus alphabet suffixes (a b c d e f g i m o p r s t v, 15 letters) on 12 seeds only:
  `hrv apple watch`, `boletim sanitário`, `app animais de estimação`, `dividir conta`, `app dividir despesas`, `shogi`,
  `xadrez japonês`, `contagem decrescente iphone`, `app contador de dias`, `jogos de lógica iphone`, `jogos de puzzle`,
  `app lista de tarefas`, `planeador diário`, `wikipédia aleatória`, `xadrez chinês`, `xiangqi`,
  `área de transferência iphone`, `gestor área de transferência`. No failed requests (0 errors on all four sources).
- **Google suggest: worked.** Best source. Suffixes were rich on `shogi`, `xiangqi`, `jogos de puzzle`,
  `dividir conta`, `app lista de tarefas` and `área de transferência iphone`; nearly empty on `wikipédia aleatória`
  (two suggestions), `contagem decrescente iphone` (two) and `app animais de estimação`.
- **Google returns a lot of Brazilian and Spanish text for pt-PT.** `hl=pt-PT&gl=pt` does not filter it out.
  Examples: `compartilhada`, `gratuito`, `celular`, `aplicativo`, `propaganda`, `contagem regressiva`, `quebra-cabeça`,
  `planejador`, `monitorar`, `meu`; and for `planeador diário` almost all results are Spanish (`planeador diario con
  horas`, `planificador diario pdf`). Portugal forms are chosen for the primaries and the Brazilian forms are listed
  as variants. Where a Portugal word never came back from any source (`ecrã` only came back once: B `a personalizar
  widgets do ecrã de bloqueio`; `telemóvel` and `utilizador` never came back), it is not claimed as a query: use it in body copy only.
- **Bing `qsonhs.aspx` (mkt=pt-PT): worked** (470 requests). Same noise as in Spain: it drifts to Spanish, Italian,
  German and English, and for suffixed seeds returns the same eight English phrases for every letter (`hrv apple
  watch a` to `v`), so B was used mainly to confirm Google. Did not try `osjson.aspx` (the es run showed it returns 204).
- **App Store hints (Portugal): worked for short seeds.** Storefront `143453-2,29`, `143453-8,29` and `143453-1,29`
  gave **identical** results (tested on `shogi` and `dividir conta`), and the hint titles are Portuguese
  (`dividir contas: despesas grupo`, `shogiful: xadrez japonês`, `contagem decrescente casamento`), so the language
  suffix makes no difference; `-2` was used. Empty for most 3+ word seeds. Many hint titles and S titles are Brazilian
  Portuguese (`tela`, `celular`, `Contagem Regressiva`, `Estresse`, `Bebê`), because the Portugal storefront serves
  the shared pt-BR/pt-PT listings.
- **iTunes Search API (country=pt, lang=pt_pt): worked** (33 searches, 3 per app). Seller names left out.
- **People also ask: not collected** (needs a live Google results page behind a consent wall; not circumvented). FAQ
  lines come from question-form autocomplete (`como`, `o que é`, `qual a melhor`, `onde`).
- **"app" vs "aplicação":** Portuguese searchers type `app` (`app lista de tarefas` G, B; `app para dividir contas` G;
  `app sono apple watch` G; `app contador de dias` G, B). `aplicação` (the Portugal formal word) and `aplicativo`
  (Brazil) came back only occasionally: `aplicativo para dividir despesas entre amigos` (G), `aplicativo de lista de
  tarefas` (B), `aplicativo dividir conta restaurante` (G, Brazilian). Use "app" in titles and H1, "aplicação" in body
  copy (never "aplicativo").
- **Portugal vs Brazil, decisions:** `contagem decrescente` (Portugal) over `contagem regressiva` (Brazil; much richer
  on Google: 6+ suggestions vs 2); `ecrã` over `tela` in body copy; `utilizador` over `usuário`; `boletim sanitário` /
  `boletim de vacinas` (both used in Portugal and Brazil, human vaccine booklet competes: see Pawza); `cão` (Portugal)
  over `cachorro` (Brazil; both appear in G); `puzzle` (Portugal) over `quebra-cabeça` (Brazil); `planeador` over
  `planejador`; `partilhar` (A: `tricount - partilhar despesas`, `lista de tarefas partilhada`) over `compartilhar`.
- **Year/model variants** (`2026`, `iphone 11`, `ultra 3`) avoided per house style.
- **Nothing found at all** (empty on G, B and A, or only echo/noise): `capturas de ecrã app store`,
  `criar screenshots app store`, `gerador de screenshots app store`, `tamanho screenshots app store`, `app para fazer
  screenshots app store`, `app boletim de vacinas` as a pet query (returns human SNS), `app saúde animais de estimação`,
  `app para guardar documentos do veterinário`, `lembrete medicação animal app`, `app dividir recibo`, `shogi iphone`,
  `xadrez japonês app`, `jogar shogi online` (echo only), `aprender xiangqi`, `xadrez chinês app`,
  `xadrez chinês iphone`, `qual a melhor app de xadrez chinês`, `jogo de equilíbrio iphone`, `jogos de puzzle sem
  palavras`, `app tarefas apple watch`, `app tarefas mac`, `app tarefas pendentes` (only a bank app), `como ver artigos
  aleatórios da wikipédia`, `app para descobrir factos interessantes`, `app área de transferência iphone` (only
  unaccented echo), `gestor da área de transferência mac`.
- **Misleading seeds to avoid:** `dividir conta` alone (Netflix, Spotify, PS5, game pass, energy bills, arithmetic),
  `hrv` and `o que é a hrv` on Bing (HIV, Havan, MRV), `frango xadrez` (the dish; every `xadrez japonês` and `xadrez
  chinês` suffix search returns it), `xadrez chinês estrela` and `xadrez chinês 14 bis` (Chinese checkers and a
  board game), `puzzle de pesos` (Silent Hill 2), `jogos de pensar` (kids, poki), `contador de dias` (working days,
  sobriety: `sem fumar`, `sem açúcar`), `dias para app` (Apple sales events), `app tarefas` in Bing (paid micro-tasks:
  `app tarefas lucrativas`), `recuperação apple watch` (device recovery mode), `área de transferência iphone` in Bing
  (data transfer between phones).

---

## Mockly (App Store screenshots on Mac)

- **Primary:** `screenshots app store` (G, B). Portuguese developers keep the English "screenshots" here; `capturas de
  ecrã app store` returned nothing on G, and B/A drifted to generic phone screenshot apps.
- **Secondary:** `app store screenshot generator` (G, B); `app store screenshot maker` (G, B); `mockup app store`
  (G, B). Optional: `app store connect screenshots` (G, B), `screenshots app store size` (G).
- **Not usable:**
  - `capturas de ecrã app store`, `criar screenshots app store`, `gerador de screenshots app store`, `tamanho
    screenshots app store`, `como fazer screenshots para app store`: G empty; B returns `como fazer screenshot em
    windows/no iphone` (how to take a screenshot).
  - `mockup iphone` (G, B): free PSD/Figma/PNG and model-year intent (`mockup iphone 17`, `18 pro max`); Mockly is a
    paid Mac app. `mockup` alone (A, S): T-shirt and clothing mockups (`3DMockups - Criar Roupa`, `Mockup Creator,
    Tshirt Design`).
  - `... free`, `... ai`, `... figma`, `... canva`, `... github`, `... reddit` (G): other intent.
  - `mockup mac app` (G): only itself and `apple imac mockup`.
  - "sem subscrição": allowed for Mockly (one-time purchase) but no returned query contains it.
- **FAQ-style (from suggest).** No Portuguese question forms came back; the queries are English developer ones:
  - screenshots app store size (G) / screenshots app store guidelines (G)
  - app store connect screenshots sizes (B) / app store connect screenshots requirements (G)
  - app store connect screenshots not uploading (G)
  - app to make app store screenshots (B)
  - how to take a screenshot on iPhone (B, as `como fazer screenshot no iphone`) is the generic phone intent, not ours
- **Competitors (S):** StoreView: App Screenshot Tool, Picasso App Screenshot Studio, Screenshot Studio - Capturas,
  Mockup Screenshot, SMPRO: Mockup & Screenshot, Screenshots Pro, AppStore Screenshot Studio, Mockup & Demo Maker:
  Screeny, PoseKit: Quick 3D Mockup. A: `supershot: capturas de ecrã` (for `capturas de ecrã`), `mockups: screenshots
  & video`, `mockup generator - mocksy ai`.
- **Notes:** Same as Spain and France: keep "screenshots" and "mockup" in the title; use "capturas de ecrã" in body
  copy. Almost no query names Mac. Demand is small and English; do not expect Portuguese-language volume.

## Observa (sleep, HRV, recovery from Apple Health; HRV is SDNN)

- **Primary:** `hrv apple watch` (G, B). Portuguese writers keep "HRV" in Latin letters; most of the Google suffix
  results are English or German, so the term is shared across languages.
- **Secondary:** `variabilidade da frequência cardíaca` (G, B, A, S; also `variabilidade da frequência cardíaca apple
  watch` G, `variabilidade cardíaca` A, S); `app sono apple watch` (G, B; `melhor app sono apple watch` G);
  `qualidade do sono apple watch` (G). Optional: `app hrv apple watch` (G), `app stress apple watch` (G; Portugal
  spells it `stress`, Brazil `estresse`: S title `Monitor Estresse`).
- **Not usable:**
  - `o que é a hrv` on B (HIV, Havan, MRV); G returns `o que é a métrica hrv no garmin`.
  - `readiness apple watch` (G, B): English, device compatibility (`ultra 3`, `series 10`). `sdnn hrv` (G, B):
    English only (`meaning`, `formula`).
  - `recuperação apple watch` (G): `recuperação cardiovascular apple watch` and `modo de recuperação apple watch`
    (device recovery mode); `app de recuperação desportiva` (B): file/data recovery.
  - `pontuação de sono apple watch` (G, as `pontuação do sono apple watch`): only itself.
  - `app apple saúde` (G, B): about the Saúde app itself.
  - "sem subscrição" does not apply to Observa (Premium); no returned query contains it.
  - Brazilian forms in G (`app monitorar sono apple watch grátis`, `app apneia do sono`, `meu sono`): usable as
    wording evidence only.
- **FAQ-style (from suggest):**
  - o que é a hrv (G) / o que é a métrica hrv (G) / o'que é a sigla hrv (G)
  - como medir hrv apple watch (G) / como ver hrv apple watch (G) / medir hrv com apple watch (G)
  - apple watch tem hrv (G, as `apple watch tem hrv`)
  - como melhorar hrv (G)
  - hrv valores normais (G)
  - variabilidade da frequência cardíaca valores normais (G) / durante o sono (G) / como medir (G) / baixa (G)
  - como medir o sono apple watch (G) / como medir qualidade do sono apple watch (G)
  - como ver qualidade do sono apple watch (G) / como ativar qualidade do sono no apple watch (G)
  - onde vejo a qualidade do meu sono no apple watch (G)
  - como colocar o apple watch para medir o sono (G)
- **Competitors (S):** StressWatch: Monitor Estresse, Welltory: medir pulsação, Stress Monitor: HRV e Saúde, Heart
  Analyzer: Pulso e HRV, HRV-Tracker, Athlytic: Fitness & Recovery, HeartWatch: Monitor Frequência, HRV Tracker for
  Watch, HRV4LIFE Saúde e Performance, Rastreador VFC e Pulso, Stress HRV: Stress Tracker; sleep: Sleep Cycle - Ciclo do
  Sono, Pillow: Rastreador de sono, Livity: Sono & Saúde Tracker. A: `arry: vfc e recuperação`, `elite hrv: bem-estar
  & fitness`, `traincontrol: hrv & erholung`.
- **Notes:** Portugal app titles use both "HRV" and "VFC" (S `Rastreador VFC e Pulso`, A `arry: vfc e recuperação`);
  queries use "HRV" or the full "variabilidade da frequência cardíaca". Never write RMSSD: Observa's HRV is SDNN, so
  "variabilidade da frequência cardíaca (SDNN)" is the accurate wording. No Portuguese query for "readiness" or
  "recovery score"; `recuperação` is device recovery or data recovery. Body copy only.

## Pawza (pet health records, vaccines, vet documents)

- **Primary:** `boletim sanitário de cães e gatos` (G, B; with `online` G). The pet booklet in Portugal is the
  `boletim sanitário` (S: `Faunora – Boletim sanitário`); `boletim de vacinas` is used for the vaccination pages of
  both pets and humans.
- **Secondary:** `boletim de vacinas cão` (G; `boletim vacinas cão online` G); `boletim de vacinas gato` (G);
  `calendário de vacinação para cães e gatos` (G). Optional: `passaporte animal de companhia` (G, B; `passaporte
  europeu de animal de companhia` G), `cartão de vacinas cão` (B, as `cartão de vacina cães`).
- **Answer to the brief:** in Portugal the pet booklet is called `boletim sanitário` (also `boletim de vacinas`, and
  `cartão de vacina` is Brazilian). Both `boletim sanitário cães e gatos online` and `boletim de vacinas cão online`
  are suggested by G, so both are valid on Portuguese pages. `boletim sanitário` alone is noisy: livestock
  (`boletim sanitário aves`, `suínos`, `bovinos`, G and B), and `boletim de vacinas` alone is dominated by the human
  digital booklet (`boletim de vacinas digital sns`, `app sns 24 boletim de vacinas`, G). Always qualify with
  `cão`, `gato` or `cães e gatos`.
- **Not usable:**
  - `boletim de vacinas digital`, `app boletim de vacinas`, `como aceder ao boletim de vacinas digital`,
    `obter boletim de vacinas digital` (G, B): SNS 24 human booklet.
  - `boletim sanitário aves / suínos / bovinos / de acompanhamento de lote de suínos` (G, B): livestock.
  - `cartão de vacina de cachorro pdf / para imprimir`, `modelo de cartão de vacina para cães` (B): Brazilian
    printable-template intent. `boletim sanitário de cães e gatos preço` (G): price of the paper booklet.
  - `calendário de vacinação` alone (B): human national schedule (`do idoso`, `criança 2026`, `covid`).
  - `app para animais de estimação` (G, B): `criar` and `cuidar de` (virtual pets, games), A: `cachorro virtual`,
    `lavar e tratar animais de estimação`. `app saúde animais de estimação`, `app para guardar documentos do
    veterinário`, `lembrete medicação animal app`: empty or noise on G and B.
  - `app veterinário` (G): vet delivery and booking apps (`app veterinario domicilio`, `simplesvet`).
  - "grátis": Pawza is free for one pet, so allowed in body copy, but `app saúde animais de estimação grátis` was
    not returned.
- **FAQ-style (from suggest):**
  - perdi o boletim de vacinas do meu cão (G) / perdi o boletim de vacinas do meu gato (G)
  - boletim sanitário o que é (G; B returns generic `o que é boletim médico`)
  - boletim sanitário online (G) / boletim sanitário cães online (G)
  - boletim vacinas cão online (G)
  - primeira vacina do cão (B) / quais as vacinas para gatos (B) / vacinas necessárias para gato (B)
  - vacinas obrigatórias para cachorros (B, Brazilian wording)
  - calendário de vacinação para gatos filhotes (G)
  - passaporte animal de companhia da união europeia (G) / viajar com animais de companhia (B)
- **Competitors (S):** Faunora – Boletim sanitário, Furriel – Saúde do Cão e Gato, PetCare: Vacinas do Cão e Gato,
  Catitos: Saúde do seu animal, Truffe: vacinas e saúde animal, Vaccy: Boletim de Vacinas, Snout: Saúde do animal,
  Pidoy: Diário de Saúde Animal, Pawsitive: saúde cão e gato, Petime - Registos do meu cão, Barkibu. Pets Health 24/7,
  Saúde Animais: PetnotePlus, PetHive: A vida do teu animal. A: `vaccy: boletim de vacinas`.
- **Notes:** The mix of `animais de estimação` (Brazil) and `animais de companhia` (Portugal, official: `passaporte
  animal de companhia`, `dgav viajar animais de companhia`) both appear; use "animais de companhia" in body copy
  and `cão`/`gato` in titles. The English page covers rabbits, birds, reptiles and horses, but no Portuguese query
  names them. On-device document scanning has no query demand: body copy only.

## RightSplit (split the bill from a receipt, tips)

- **Primary:** `dividir conta restaurante` (G, via the `r` suffix; also `app dividir conta restaurante` G, `dividir a
  conta no restaurante` G).
- **Secondary:** `app para dividir contas` (G; `app para dividir contas gratuito` G, `melhor app para dividir contas`
  G); `app para dividir despesas com amigos` (G; `app dividir despesas` G); `calculadora dividir conta` (G;
  `calculadora para dividir contas` G). Optional: `calcular gorjeta` (G), `calculadora de gorjeta` (G), `dividir
  conta mbway` (G), `dividir conta amigos` (G).
- **Not usable:**
  - `dividir conta` / `dividir contas` alone: streaming and gaming account sharing (`dividir conta netflix / spotify /
    ps5 / game pass / disney / chatgpt`), energy bills (`dividir conta de luz`), arithmetic (`conta dividir com resto`,
    `conta dividir dois números`), translations (`dividir a conta em inglês`), Brazilian celebrity noise.
  - `dividir conta revolut` (G): other product; `dividir conta mbway` (G) is returned but intent is unclear (MB WAY
    payments), so optional only.
  - `app para dividir contas de streaming / de casa / de viagem / casal` (G): shared-expense and subscription
    intent, not restaurants (RightSplit does not target ongoing shared expenses).
  - `tricount` (G, A, S) and `splitwise alternativa` (G): competitor brand queries; useful for an alternatives
    page, not as the app page primary.
  - `como calcular gorjeta na rescisão` and `... nos eua` (G): payroll and US tipping. Tipping is also marginal in
    Portugal (`gorjeta restaurante portugal` G returned only itself), so tips are a secondary angle.
  - Brazilian forms (`aplicativo dividir conta restaurante`, `app de celular para dividir despesas`, `compartilhada`)
    (G): wording evidence only.
  - "grátis"/"gratuito" (`app para dividir contas gratuito` G): RightSplit is "free to start", allowed in body
    copy, not a primary.
- **FAQ-style (from suggest):**
  - como dividir a conta no restaurante (G)
  - como dividir despesas entre amigos (G)
  - como calcular a gorjeta (G)
  - melhor app para dividir contas (G) / melhor app para dividir despesas (G)
  - app para dividir despesas entre amigos (G) / app para dividir despesas casal (G)
  - app que divide contas de viagem: app para dividir contas de viagem (G)
  - tricount o que é (G)
  - dividir conta mbway (G)
- **Competitors (S):** Splitwise, tricount - Partilhar despesas, Banana Split - Dividir Contas, Splity - Despesas do
  Grupo, ShareCost: Dividir Contas, Dividir a Conta no Restaurante, Dividir conta - Spliteasy, DividirConta, Dividir
  conta: Pezzo, Dividir contas em grupo - dvup, Tabbley, Tip Tap Split, Split - Dividindo contas, justamente,
  TravelSpend, Calculadora Gorjeta Tiply, Calculadora de Gorjetas. A: `banana split - dividir contas`, `dividir
  contas: despesas grupo`, `dividir contas - easy split`, `expensemate: dividir contas`, `depty: dividir conta e
  dívidas`, `calculadora gorjeta・dividir`, `dividir gorjetas da equipa`.
- **Notes:** "conta" = restaurant bill, but also account (streaming), hence the noise; "despesas" moves intent to
  shared expenses. Qualify with "restaurante". The App Store uses "dividir contas" (plural) as the category label
  (A, S); Google prefers "dividir conta" for restaurants and "dividir contas" for apps. Use `dividir conta no
  restaurante` in the title and `app para dividir contas` in the H1/body. Receipt scanning has no returned query:
  "digitalizar a fatura/o talão" in body copy only.

## Shogiful (shogi / Japanese chess, learn and analyze)

- **Primary:** `shogi` (G, B, A, S). Our own listing shows in A and S as "Shogiful: xadrez japonês".
- **Secondary:** `xadrez japonês` (G, B, A, S; G also `shogi (xadrez japonês)`); `shogi regras` (G, B; `regras do
  shogi` B); `como jogar shogi` (G; `shogi como jogar` G; `como aprender a jogar shogi` G); `tsume shogi` (G, B).
- **Not usable:**
  - `frango xadrez japonês`, `arroz xadrez japonês`, `xadrez rima com japonês` (G): the dish and rhymes.
  - `xadrez japones go` (G): confusion with Go; `shogi ichiban`, `shogi mod`, `shogi fabric`, `shogi minecraft`,
    `shogi app yakuza` (G): other things.
  - `shogi regras pdf`, `como jogar shogi pdf` (G): pdf intent; `shogi tabuleiro`, `shogi comprar` (G): physical sets.
  - `shogi app` (G, B) is returned, but only in English forms (`shogi app reddit / android / store`); fine to use
    in body copy, not a Portuguese primary.
  - `shogi iphone`, `xadrez japonês app`, `qual a melhor app de shogi`: empty on G, noise on B.
  - `peças shogi` on B (Shineray, SolidWorks parts).
- **FAQ-style (from suggest):**
  - o que é o jogo shogi (G) / o que é shogi (G) / shogi o que é (G)
  - como aprender a jogar shogi (G) / shogi como jogar (G) / aprender a jogar shogi (G)
  - shogi regras (G, B) / regras do shogi (B)
  - qual é mais difícil shogi ou xadrez (G) / shogi e xadrez diferença (G) / shogi vs xadrez (G)
  - movimento peças shogi (G) / shogi peças (G)
  - shogi em português (G)
  - xadrez japonês regras (G) / xadrez japonês como jogar (G, as `xadrez japones como jogar`)
  - shogi para iniciantes: returned in English only (`shogi for beginners` G)
- **Competitors (S):** Shogi ™, PiyoShogi, Shogi Quest Online, Mestre do Shogi Clássico, Shogi Wars, Shogi Lv.100 Entry
  Edition, 81Dojo, Dr. Shogi, Everybody Shogi, Shogi Master, Xadrez - Jogar e Aprender. A: `shogi quest online`, `shogi
  live`, `shogi lite -chess-`, `shogi lv.100`, `shogi demon`, `shogi quest plus - daily shogi problems`.
- **Notes:** In Portuguese "shogi" is the leading term and "xadrez japonês" the descriptive phrase. Google suffix
  results for `shogi` are mostly English. The tsume term is returned (`tsume shogi` G, B), so the 501 tsume problems
  can be named. "Kanji" and "sem kanji" have no returned query.

## Soon. (countdown app and widgets)

- **Primary:** `contagem decrescente iphone` (G; also `contagem decrescente dias iphone` G). Thin on Google (two
  suggestions); the stronger signals are in the App Store hints (A: `contagem decrescente`, `contagem decrescente
  casamento`, `contagem decrescente da viagem`, `antici: contagem decrescente`).
- **Secondary:** `app contador de dias` (G, B; `app contador de dias iphone` G, `app contador de dias widget` G);
  `contagem decrescente casamento` (G, A); `contagem decrescente widget` (G, as `contagem decrescente widget`);
  `contagem decrescente férias` (G; A `contagem decrescente da férias`). Optional: `contagem decrescente aniversário`
  (G), `app contador de dias para viagem` (G).
- **Brazilian variants (body copy only):** `contagem regressiva iphone` (G, B), `widget contagem regressiva iphone`
  (G, B; `widget contagem regressiva iphone gratuito` G), `contagem regressiva iphone widget / foto / dias / data`
  (G), `colocar contagem regressiva iphone` (G).
- **Not usable:**
  - `contador de dias` alone (G, B, A): working days (`dias úteis`, `dias corridos`), date calculators, and sobriety
    (`app contador de dias sem fumar / sem açúcar / vício`).
  - `dias para app` (G, B): Apple sales events (`dias apple fnac / el corte inglés / media markt`); `contador de dias
    desde` (G): Spanish and date calculators.
  - `quantos dias faltam para o natal 2026 / 2027 / verão / halloween` (B): content, not app intent.
  - `app countdown iphone`, `countdown widget iphone` (G): English; `app contador de dias android / pc` (G): other
    platforms.
  - `como fazer contagem decrescente no iphone` on B: `como fazer conta no iphone` (an account).
  - "grátis": Soon. is free with Premium; `app contador de dias gratis` (G) may appear once in the body, not a
    free-only claim.
- **FAQ-style (from suggest):**
  - como fazer contagem decrescente no iphone (G)
  - quantos dias faltam app (G) / app que mostra quantos dias faltam para eventos (G) / app para contar quantos dias
    faltam (G)
  - a personalizar widgets do ecrã de bloqueio (B; only to confirm `ecrã de bloqueio`)
  - como colocar widgets no iphone (B)
  - contagem decrescente para o meu aniversário (G)
  - app contador de dias para viagem (G)
- **Competitors (S):** Countdown, Eventos Contagem Regressiva, Contagem decrescente ◔, Countdown Buddy, Contagem
  Regressiva Férias, CountFlow Contagem decrescente, Big Days - Contagem Regressiva, Contagens, Contador de Dias,
  Day Counter — Countdown Timer, Widget Casal: Contador de dias, Countdown Star, Days - Event Countdown, Countdown
  Widget & Counter. A: `antici: contagem decrescente`, `contagem decrescente: giovex`, `daysworth: contador de dias`,
  `countdown widget: contagem`, `d-day widget: contagem`, `christmas countdown & advent`.
- **Notes:** Unlike Spain, where `cuenta atrás` is a Google head term, Portugal's `contagem decrescente` is thin in
  Google, and the Brazilian `contagem regressiva` has most of the volume. The App Store titles in Portugal use both.
  Keep `contagem decrescente` in the title for Portugal and name `contagem regressiva` once in body copy. "contador de
  dias" is the second noun phrase for days-until apps. Event types (casamento, férias, aniversário) appear in A.

## Tare (balance logic puzzle game)

- **Primary:** `melhores jogos de puzzle iphone` (G, as `melhores jogos de puzzle iphone` / `... para iphone`; also
  `jogos puzzle iphone` G). Chosen so Tare does **not** compete with Millrace's general `jogos de lógica iphone`
  (see the flag in the summary): "puzzle" is the Portugal word (Brazil: `quebra-cabeça`), it came back from G, and
  Tare's real proposition is a puzzle with a unique mechanic.
- **Secondary:** `jogos de raciocínio iphone` (G; `jogos de raciocínio lógico iphone` G); `jogos sem anúncios iphone`
  (G; `melhores jogos sem anuncios iphone` G); `jogos offline iphone` (G; `jogos offline sem internet iphone` G).
  Optional: `jogos de balança` (G, as `jogos de balança` / `jogos balança de equilíbrio`), `jogos de dedução` (G).
- **Not usable:**
  - `jogos de lógica iphone` / `jogos de lógica para iphone` (G): returned, but reserved for Millrace.
  - `jogos de lógica` (G, B, A): `para crianças`, `para imprimir`, `de programação`, `matemática`, `online`; wrong
    audience.
  - `jogos de balança` (G): thin and mixed (kitchen scales); keep "balança" in the body.
  - `puzzle de pesos` (G): Silent Hill 2 remake puzzles and Crisol; `jogos de equilíbrio` and `jogo de equilíbrio
    iphone` (B): physical balance games and Jenga-style towers.
  - `jogos de pensar` (G, B): kids, poki, `jogos de pensar bilhar`.
  - `jogos de puzzle` alone with suffixes (G): PC, Steam, ps4, roblox, Android, coop; filter with `iphone`.
  - `jogos de dedução` (G): board-game social deduction (`dedução social`).
  - `jogos de puzzle sem palavras` (B): word games.
  - `jogos puzzle sem propaganda` (G) is returned but `propaganda` is Brazilian for "ads": use `anúncios`.
  - "sem subscrição": allowed for Tare (free plus one unlock), but no returned query contains it; `sem anúncios` is
    returned and is allowed because the page says no ads.
- **FAQ-style (from suggest):**
  - melhores jogos de puzzle para iphone (G)
  - melhores jogos raciocinio iphone (G)
  - melhores jogos sem anuncios iphone (G)
  - melhores jogos offline iphone (G)
  - jogos de raciocínio lógico iphone (G)
  - jogos offline sem internet iphone (G)
  - melhores jogos para iphone (B)
  - jogos para treinar o cérebro (B)
- **Competitors (S):** Mobilo: Puzzle de equilíbrio, Logic Puzzles: Jogos de Lógica, Impulse - Jogos para o cérebro,
  Cross Logic - Quebra-Cabeça, IQ Masters: Enigmas de Mentais, Paper Fold: jogo de lógica, Number Match: Jogos de
  números, Sudoku.com - Puzzle clássico, Shape Escape. A: `twiro: puzzle, jogos de lógica`, `clues by sam: jogos de
  lógica`, `desatar - jogos de lógica`, `arrows – puzzle escape`, `puzzle de setas`.
- **Notes:** Portugal titles use "Jogos de lógica", "Jogos de raciocínio", "Puzzle" and "Quebra-cabeça" (Brazil).
  The closest direct competitor is `Mobilo: Puzzle de equilíbrio`, found by the S search `puzzle equilíbrio balança`,
  so "puzzle de equilíbrio" is the most accurate descriptor of Tare even though it has no suggest volume. Demand for
  "jogos de puzzle" is mostly Android, PC and Steam, so the `iphone` qualifier is essential.

## Taskful Day (day planner / to-do list, iPhone + Mac)

- **Primary:** `app lista de tarefas` (G, B; `app lista de tarefas iphone` G).
- **Secondary:** `app tarefas diárias` (G; `app tarefas diarias iphone` G, `app para organizar tarefas diárias` G);
  `app para organizar o dia` (G; `melhor app para organizar o dia` G); `melhor app de tarefas para iphone` (G);
  `app to do list` (G, A as `to do list`; `app to do list iphone` G). Optional: `planeador diário` (G, A, S: app
  titles `Planeador Diário: 3 Tarefas`, `dayline: planeador diário`), `app agenda diária` (G; `app agenda diaria
  iphone` G).
- **Not usable:**
  - `planeador diário` as a search head (G, B): for Google it is Spanish and printable
    (`planeador diario para imprimir / de actividades / con horas`, `planificador diario pdf`); Bing shows
    `planejador diário` (Brazil). Keep it for the page text; it is the correct Portugal word and the S/A app titles use it.
  - `app lista de tarefas compartilhada / compartilhada gratuito / google / microsoft / para equipe` (G): shared
    and team use, other platforms. `app tarefas pendentes` (G): only a bank app.
  - `app de tarefas para ganhar dinheiro / remuneradas / pagas`, `app de tarefas para crianças`, `domésticas`,
    `sala do futuro` (G): paid micro-tasks, kids, school.
  - `app tarefas apple watch`, `app tarefas mac` (G, B): empty or noise (`app tarefas lucrativas`).
  - `app para planear o dia` (G): Spanish only (`app para planear tu dia`).
  - `app de produtividade iphone` (B): `loja de aplicativos do iphone`.
  - "grátis"/"gratuito" (`app lista de tarefas gratuito` G, B): the page offers Pro with a 7-day trial; mention
    "grátis" only if the free tier is confirmed against MASTER.md. "sem conta" has no returned query.
  - Brazilian forms: `aplicativo de lista de tarefas` (B), `compartilhada`, `planejador`.
- **FAQ-style (from suggest):**
  - como organizar o meu dia (G, B) / como organizar melhor o meu dia (G) / como organizar o meu dia de trabalho (G)
  - como organizar o dia a dia (G, B) / como organizar tarefas do dia (G) / como se organizar no dia a dia (G)
  - qual a melhor app para organizar tarefas (G, as `qual o melhor app para organizar tarefas`)
  - melhor app de tarefas (G) / melhor app de tarefas diárias (G) / melhor app lista de tarefas (G)
  - melhor app para organizar tarefas diárias (G)
  - app lembretes tarefas (G, as `app para lembretes de tarefas`)
  - organize o seu dia (B, Portugal imperative)
- **Competitors (S):** To Do List: Lembretes Tarefas, Lembretes, Lista de Tarefas e Lembrete, Todoist: To do
  list–Calendário, TickTick:To-do list,calendário, Google Tasks, Microsoft To Do, Do! – Simple To Do List, Structured -
  Daily Planner, To do list - MinimaList, Habit Tracker - Hábitos, Calma: Planeador PHDA/ADHD, Planeador Diário: 3
  Tarefas. A: `lista de tarefas partilhada`, `lista de tarefas - organizador`, `t3t - tarefas e planeamento`, `todoless:
  tarefas e planeador`, `pomoplan: foco, tarefas, metas`, `bubbles: planeador diário`, `schedy: planeador diário`,
  `doo: to-do list`.
- **Notes:** `lista de tarefas` is the main phrase and `to do list` in English the second (G, A), as in Spain.
  `tarefas diárias` is the strongest day-planner phrase on Google. "planeamento" (Portugal) vs "planejamento" (Brazil).
  Carry-forward and "no red overdue pile" have no query demand: the title should say "lista de tarefas" first.

## WanderWiki (swipe random Wikipedia articles)

- **Primary:** `wikipedia aleatória` (G, B; B accent-free `wikipedia aleatoria`). Wikipedia's own feature is
  "Página aleatória": G returns `wikipedia página aleatória`.
- **Secondary:** `wikipedia página aleatória` (G; `pagina aleatória wikipedia` G); `artigo aleatório wikipedia` (G;
  B `artigo aleatório da wikipédia`); `app wikipédia` (G, B). Optional: `wikipedia a caso` (B, via `wikipédia ao
  acaso`), `wikipedia random` (G, B; English).
- **Not usable:**
  - `wikipedia random article / button / generator / game` (G, B): English; high volume but wrong language.
  - `app wikipedia offline / download / sin internet` (G, B), `wikipedia offline app` (G, B): official or offline
    copy intent. WanderWiki saves articles offline but is not an offline copy of Wikipedia: do not claim it.
  - `curiosidades wikipédia` (G, B): Brazilian trivia content (`curiosidades de pernambuco wikipédia`).
  - `app curiosidades` (G, B: `app curiosidades diarias`, `app para aprender curiosidades`): a different category,
    but a real adjacent one (see competitors).
  - `app wikipédia iphone` (G): only the English `wikipedia app for iphone`.
  - `como ver artigos aleatórios da wikipédia`, `app para descobrir factos interessantes`, `aprender coisas novas app`:
    empty or noise on G and B (`erros aleatórios e sistemáticos`, `app que faz perguntas`).
- **FAQ-style (from suggest).** No question forms came back; the nearest:
  - wikipedia página aleatória (G)
  - artigo aleatorio wikipedia (G) / artigo aleatório da wikipédia (B)
  - app para aprender curiosidades (G)
  - app curiosidades diarias (G, B)
  - coisas interessantes para aprender (B) / como aprender coisas novas (B)
  - sites para aprender coisas novas (B)
- **Competitors (S):** Wikipédia, WikiTok - Scroll, Read & Learn, Wikipanion, Kiwix; curiosities: DuoFacts: Factos
  Curiosos, Miqo: aprenda curiosidades, Arca: Curiosidades diárias 365, Curiosidades Diárias: Sabia?, Tidbit:
  Curiosidades diárias, Daily Fun Facts - IpsoFacto. A: `the wiki game: jogo wikipédia`, `listen to wikipedia`,
  `curio: fatos e curiosidades`, `crazyfacts: curiosidades`.
- **Notes:** As in Spain, demand is a tiny head term (two suggestions on G) and people want the website feature, not
  an app. The title should carry "Wikipedia aleatória" and "iPhone". `WikiTok` in S is the closest product
  (swipeable Wikipedia). Check that 32 Wikipedia language editions includes Portuguese before claiming it on the page.

## Xiangqiful (xiangqi / Chinese chess)

- **Primary:** `xadrez chinês` (G, B, A, S).
- **Secondary:** `xiangqi` (G, B, A, S); `xadrez chinês como jogar` (G, B; `como jogar xadrez chinês` G, `como se
  jogar o xadrez chinês` G); `xadrez chinês regras` (G; `xiangqi regras` G); `xadrez chinês peças` (G; `xiangqi
  peças` G). Optional: `xadrez chinês online` (G, B), `xadrez chinês tabuleiro` (G).
- **Not usable:**
  - `frango xadrez chinês`, `arroz xadrez chinês`, `frango xadrez é chinês ou japonês`, `frango xadrez china`,
    `frango xadrez chinês receita` (G): the dish. `xadrez em chinês` (G): language learning.
  - `xadrez chinês estrela` (G): Chinese checkers (stars); `xadrez chinês 14 bis` (G): a board game; `xadrez chinês
    go` (G): confusion with Go; `xadrez chinês comprar` (G): physical sets.
  - `xiangqi.com app` (G): another app's brand; `xiangqi sg`, `xiangqi ok`, `xiangqin jiao`, `xiangqian lao` (G, B):
    unrelated.
  - `xadrez chinês app`, `xadrez chinês iphone`, `aprender xiangqi`, `qual a melhor app de xadrez chinês`: empty on G
    and A, B returns generic chess (`melhores apps xadrez com ia`).
  - `xadrez chinês diferença xadrez` (B): generic chess questions.
- **FAQ-style (from suggest):**
  - como jogar xadrez chinês (G) / como se jogar o xadrez chinês (G) / xadrez chinês como jogar (G, B)
  - xiangqi como jogar (G)
  - xadrez chinês regras (G) / xiangqi regras (G)
  - xadrez chinês peças (G) / xiangqi peças (G)
  - how to play xiangqi (B; English)
  - xiangqi vs xadrez / xiangqi vs shogi / xiangqi vs chess (G; English forms)
- **Competitors (S):** Xadrez Chinês V+, Xiangqi, Xiangqi One - Xadrez Chinês, Xiangqi – Xadrez Chinês, Xiangqi:
  Xadrez Chinês, Poqi: Xadrez Chinês Xiangqi, Xadrez: Aprende e Joga, Chinese Chess - Best XiangQi, Xiangqi Chinese
  Chess Online, Co Tuong Viet Nam. A: `jardim xiangqi: xadrez chinês`, `pvxiangqi: xadrez chinês`, `xiangqi online -
  zyga chess`, `xiangqi 3d`, `ai chess: chess, xiangqi & go`. Our own "Xiangqiful: Xadrez Chinês" is already in S.
- **Notes:** In Portuguese the name "xadrez chinês" is also used in Brazil for Chinese checkers (`xadrez chinês
  estrela`, G; in Portugal that game is "damas chinesas"), so the page should say "xiangqi" next to it in the title
  and use "xadrez chinês (xiangqi)". Titles in A and S put "Xadrez Chinês" first and "Xiangqi" second. "Pikafish"
  and "problemas de mate" have no returned query.

## Clippet (clipboard manager for iPhone and Mac, unreleased)

Unreleased and unlisted: these keywords are for when it goes live.

- **Primary:** `histórico área de transferência iphone` (G; returned as `historico area de transferencia iphone` and
  `como ver o historico da area de transferencia no iphone`).
- **Secondary:** `histórico área de transferência mac` (G, B; `como ver o historico da area de transferencia no mac`
  G); `como ver a área de transferência no mac` (G, B); `copiar e colar iphone mac` (G, B); `clipboard manager mac`
  (G, B; English). Optional: `app clipboard iphone` (G; English `clipboard app iphone`), `gestor de clipboard` (A, S).
- **Not usable:**
  - `área de transferência iphone` alone (G): `onde fica`, `como acessar`, model variants (`iphone 11`, `iphone 15`),
    keyboard (`gboard`, `teclado`), clearing (`como limpar / apagar area de transferencia iphone`).
  - `área de transferência iphone` on B: data transfer between phones (`transferência de dados iphone`).
  - `como ver o histórico da área de transferência windows 10` (G), `histórico de área de transferência windows` (B):
    other platforms.
  - `como recuperar area de transferencia iphone`, `iphone nao tem area de transferencia` (G): fix intent.
  - `app área de transferência iphone` (G): only the unaccented echo. `gestor de transferencia tecnologica` (G): noise.
  - `copiar no iphone e colar no mac não funciona` (G): troubleshooting for Universal Clipboard.
  - `prancheta` (S: `iCliper - Prancheta`): Brazilian word for the clipboard; no suggest returned it.
  - "sem conta": allowed for Clippet, but no returned query contains it.
- **FAQ-style (from suggest):**
  - onde está a área de transferência no iphone (G, as `onde esta a area de transferencia do iphone`)
  - como ver o histórico da área de transferência (G, B) / como ver o historico da area de transferencia no iphone (G)
  - como ver a área de transferência no mac (G) / como abrir a area de transferencia no mac (G)
  - existe area de transferencia no iphone (G) / o iphone tem area de transferencia (G)
  - como ver historico da area de transferencia mac (G)
  - o que é a área de transferência (G, B)
  - como copiar e colar do iphone para o macbook (G) / como copiar no iphone e colar no mac (B)
- **Competitors (S):** Área de Transferência: Colar, +Clipboard copiar,cortar,colar, Hboard: Área de Transferência,
  Clipboard Manager - OneTap, Clipboard Manager - PastePal, Clipbud - Clipboard Manager, Paste – Área de Transferência,
  ClipBox: Área de Transferência, SnipTray: Gestor de Clipboard, Paste It - Área Transferência, Pasted - Gestor de
  cópias, Clip Flow: Gestor de Recortes, Pastin: Área de Transferência. A: `clipster - gestor de clipboard`, `copiar e
  colar - histórico`, `crosspaste: copiar e colar`, `clipboard keeper: copy history`, `magic clipboard`.
- **Notes:** "Área de transferência" is the only Portuguese noun for the system feature; the App Store titles use
  both "Área de Transferência" and "Clipboard" ("gestor de clipboard", `Gestor de Recortes` and `Histórico de
  Recortes` in S). The page should say that iOS has no clipboard history and that Clippet adds one. Wording in
  Portugal: "ficheiros" and "ecrã" in body copy, "histórico" in the title.

---

## Summary table

| Page | Primary | Secondaries |
|---|---|---|
| mockly | screenshots app store | app store screenshot generator; app store screenshot maker; mockup app store |
| observa | hrv apple watch | variabilidade da frequência cardíaca; app sono apple watch; qualidade do sono apple watch |
| pawza | boletim sanitário de cães e gatos | boletim de vacinas cão; boletim de vacinas gato; calendário de vacinação para cães e gatos |
| rightsplit | dividir conta restaurante | app para dividir contas; app para dividir despesas com amigos; calculadora dividir conta |
| shogiful | shogi | xadrez japonês; shogi regras; como jogar shogi |
| soon | contagem decrescente iphone | app contador de dias; contagem decrescente casamento; contagem decrescente widget |
| tare | melhores jogos de puzzle iphone | jogos de raciocínio iphone; jogos sem anúncios iphone; jogos offline iphone |
| taskful-day | app lista de tarefas | app tarefas diárias; app para organizar o dia; app to do list |
| wanderwiki | wikipedia aleatória | wikipedia página aleatória; artigo aleatório wikipedia; app wikipédia |
| xiangqiful | xadrez chinês | xiangqi; xadrez chinês como jogar; xadrez chinês regras |
| clippet | histórico área de transferência iphone | histórico área de transferência mac; como ver a área de transferência no mac; copiar e colar iphone mac |

**Flags (same-primary or overlapping queries):**

- No two of these 11 pages share a primary.
- **Tare vs Millrace:** `jogos de lógica iphone` came back from G and is the natural Millrace primary, so Tare uses
  `melhores jogos de puzzle iphone`. Tare's secondary `jogos de raciocínio iphone` is close to Millrace's territory
  (raciocínio vs lógica); if Millrace takes both, drop it from Tare and use `jogos de balança` / `jogos de dedução`
  instead (weaker).
- **Pawza vs the human vaccine booklet:** `boletim de vacinas` alone is dominated by the SNS 24 human booklet. Always
  qualify with `cão`, `gato` or `cães e gatos`.
- **Shogiful vs Xiangqiful:** both use "xadrez japonês" and "xadrez chinês" (different heads), but G returns
  `xiangqi vs shogi` and `xiangqi or shogi`; link the two pages to each other.
- **Soon vs Taskful Day:** no overlap (`contador de dias` vs `lista de tarefas`).
