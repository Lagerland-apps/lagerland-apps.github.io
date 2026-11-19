# Apple's own European Portuguese names (pt, Portugal)

Part of the language sheet `_i18n/pt.md`. Verified 2026-11-19 on Apple's Portugal pages (source per row). Use these exactly; never invent an Apple name. Rows marked "not verified" have no Apple Portugal page that names them.

Checked 2026-11-19 against Apple's live Portugal pages: fetched directly with curl, `Accept-Language: pt-PT` and a Safari User-Agent, raw HTML read for characters. Only `support.apple.com/pt-pt/...` (page footer "Portugal", title suffix "Suporte Apple (PT)", guide pages `lang="pt-pt"`), `www.apple.com/pt/...` (title suffix "Apple (PT)") and `apps.apple.com/pt/...` (page `lang="pt-PT"`) were used. No Brazilian (`pt-br`, `/br/`) page is a source for any row. The iPhone and Apple Watch user guides on support.apple.com/pt-pt are for iOS 27 and watchOS 27.

Three things to know before reading the rows:

1. **Apple Portugal does not write "tu".** It writes formal third-person imperatives with no pronoun ("Toque em", "Vá à aplicação Definições", "Abra", "Selecione", "Clique") and "o seu / a sua" possessives. Zero "tu", "você", "teu", "tua" or "te" on every guide, article and apple.com/pt page checked. Counts in section "Register" at the end. This decides the site's formality.
2. **Apple Portugal says "assinatura" for subscription** (127 hits, 0 "subscrição"), "conta Apple" (92, no "Apple ID"), "Definições" (159, no "Ajustes", no "Configurações"), "ecrã" (445, no "tela"), "ficheiro" (85, no "arquivo"), "partilhar" (335, no "compartilhar"), "descarregar" (47) and "palavra-passe" (53, no "senha"). The word "assinatura" is the same word Brazil uses, so it is not a Brazil marker; do not "correct" it to "subscrição".
3. **The word for "app" is split.** The iPhone, Apple Watch and Mac user guides write "aplicação" (iPhone guide 618 hits vs 39 "app/apps", and those 39 are the App Store tab "Apps" and "App Clips" only; Watch plus Mac guides 274 vs 4). The support articles, apple.com/pt marketing and the App Store write "app/apps" (articles 145 vs 10 "aplicação"; marketing 199 vs 2; Things 3 and Observa store pages 113 vs 15). Store text uses both on one page ("Privacidade da app", "Esta aplicação não recebeu classificações"). Gender: "a App Store" (feminine, 38 vs 0 masculine), "o Apple Watch" (masculine, 326 vs 0), "o iPhone", "a Dynamic Island".

Two Brazil-only things Apple Portugal does NOT use, useful as a check: "Ajustes"/"Configurações" for the settings app (Portugal: "Definições"), "tela" (Portugal: "ecrã"). The full list is in the last section.

How Apple writes them in running text:
- **App names**: Apple writes "a aplicação" + capitalised name in the guides, "a app" in articles and marketing, no quotes, no italics: a aplicação Saúde, Fitness, Ficheiros, Lembretes, Definições, Relógio, Diário, Fotografias, Atalhos, Carteira, Mapas, Palavras-passe, Jogos, ECG, Sinais Vitais, Preparação, Treino, Atividade, Sono, Atenção Plena, Ruído, Seguimento do ciclo (Apple Watch). Article 108790 writes "app Treino" and "app Saúde"; article 102420 writes "app" in prose but "aplicação" inside the quoted setting label.
- **Features and multi-word setting labels** go in English-style curly double quotes “ ” (U+201C, U+201D), with no space inside: “Tempo de ecrã”, “Partilha de compras”, “Não incomodar”, “Reduzir interrupções”, “Iniciar sessão com a Apple”, “Sincronizar este iPhone”, “Cancelar assinatura”, “Em espera”. About 1190 “ and 1253 ” on the iPhone, Watch and Mac guide pages fetched, 0 « ». The guide also has about 63 straight " in the same pages, often mismatched (`"Audição”`), and the support articles mostly use straight " (66 straight vs 2 curly: `"recibo da Apple"`, `"Pedir à aplicação para não seguir"`). **Single-word labels are mostly bare or quoted inconsistently**: Assinaturas, Seguimento, Notificações, Resumo, Explorar, Medicação.
- Menu paths use ">" with a no-break space before it and a normal space after: "Vá a Definições&nbsp;> Privacidade e segurança > Seguimento." (the iPhone guide puts a small Settings icon between "Definições" and ">"; 20 NBSP-before-">" vs 6 plain-space on the guide pages). Articles use plain spaces: "Aceda a Definições > Acessibilidade." For steps Apple prefers the verb chain: "Vá à aplicação Definições no iPhone. Toque em “Tempo de ecrã”."
- **Capitalisation**: sentence style in the iPhone guide (“Tempo de ecrã”, “Partilhar entre dispositivos”, “Não incomodar”). The Apple Watch guide and articles Title Case some app names: Sinais Vitais, Oxigénio no Sangue, Atenção Plena. Common nouns for features stay lowercase in running text: as notificações, a central de controlo, a central de notificações, um modo de concentração, o ecrã principal, o ecrã bloqueado, o modo escuro, o modo de voo, a pilha inteligente, "conta Apple" (lowercase "conta"; "Conta Apple" capitalised only when it is a button or settings row: toque em “Conta Apple”). Articles capitalise "Central de controlo", "Modo escuro", "Proteção de dados avançada" as headings. The site should use "conta Apple" lowercase in prose.
- Gender and elision: o iPhone, o iPad, o Mac, **o Apple Watch** ("no Apple Watch"), **a App Store** ("na App Store", "da App Store"), o Apple Vision Pro ("no Apple Vision Pro"), a Dynamic Island, a Siri in articles ("Utilizar a Siri em todos os dispositivos Apple") but bare "Siri" in the guide ("Ativar e acionar Siri"). iCloud: the guide drops the article ("em iCloud", 161 hits; "Usar iCloud"), articles and the store use it sometimes ("no iCloud Drive", "do iCloud", 75 hits). Apple writes "iCloud Drive", "Face ID", "Touch ID", "Apple Pay", "Apple Intelligence", "AirDrop", "Handoff", "Spotlight" in English.
- Other Apple spellings: **Acordo Ortográfico 1990 forms** (338 "ativ-" forms, 1 "activ", 0 "acção", 4 "receção", 0 "recepção"); "frequência cardíaca" **with the accent** (104 hits, 0 "cardiaca"; the Spanish Spain file has no accent, Portugal keeps it); "Wi‑Fi" with U+2011 non-breaking hyphen (20 hits) and plain "Wi-Fi" (16 hits); "e‑mail" with a hyphen (84 hits, 1 "email" in marketing); "palavra‑passe" with hyphen (U+2011 in many places); "picture‑in‑picture"; "vídeo" with accent; "fotografia" (198 hits, 0 "foto" alone); "ecrã"; "secretária" for desktop (41, 0 "ambiente de trabalho"); "rato" for mouse (2, Mac); "telemóvel" (1) and "telefone" (14); "computador" (7); "desporto" (2); "guardar" (51, 0 "salvar"); "apagar" (178, with "eliminar" 2); "descarregar" (47) and "transferir" for transfers (13); "iniciar sessão" (51) and "terminar sessão" (1); "percentagem" (3).
- Apple's inclusive wording is not used in the Portugal guide ("organizador da família", "membros da família", "criança").

Punctuation and spacing (checked in raw bytes on the iPhone, Apple Watch and Mac guides, support articles 118428, 118223, 108906, 102420, 105055, 108756, 108790, 102674, 108350, 111781, 108971, 102651, 108922, apple.com/pt iPhone, iPhone compare, App Store, iCloud, Apple Fitness+, Apple Pay, Apple Intelligence pages, and apps.apple.com/pt): full detail in the "Typography" section at the end.

Abbreviations: ig = iPhone user guide https://support.apple.com/pt-pt/guide/iphone/welcome/ios (table of contents), wg = Apple Watch user guide https://support.apple.com/pt-pt/guide/watch/welcome/watchos, mg = Mac user guide https://support.apple.com/pt-pt/guide/mac-help/welcome/mac, amk = apple.com/pt marketing pages (https://www.apple.com/pt/iphone/, /pt/app-store/, /pt/icloud/, /pt/apple-fitness-plus/, /pt/apple-intelligence/, /pt/apple-pay/, /pt/iphone/compare/), ap = apps.apple.com/pt. Article URLs are https://support.apple.com/pt-pt/NNNNNN. **There is no `www.apple.com/pt/health/` (HTTP 404) and `www.apple.com/pt/privacy/` 301-redirects to the English `www.apple.com/privacy/`**, so the Spanish file's `ah` and `apv` sources have no Portugal equivalent; the Portugal user guides and articles replace them.

## Health and fitness

| English | Portuguese (Portugal) as Apple writes it | Source | Note |
|---|---|---|---|
| Health (app) | Saúde; a aplicação Saúde (guide), a app Saúde (articles) | https://support.apple.com/pt-pt/guide/iphone/iphcae7451f3/ios ; https://support.apple.com/pt-pt/108906 | Translated, never "Health". Tabs: “Resumo”, “Explorar” (iOS 27). The intro page of the same guide once says “Navegar” for the tab; use "Explorar" |
| Apple Health | not verified | no `www.apple.com/pt/health/` page (404); Apple's guides say only "aplicação Saúde" | Developers' pt-PT store text still writes "Apple Health" (Observa's Portugal listing); Apple's pages do not. Use "aplicação Saúde" / "Saúde" |
| Health data | dados de saúde; ecrã “Dados de saúde” (Resumo > tua foto > “Dados de saúde”); "Introdução aos dados de saúde" | https://support.apple.com/pt-pt/guide/iphone/iphbb8259c61/ios ; https://support.apple.com/pt-pt/guide/iphone/iphcae7451f3/ios | “Dados de saúde” is also the name of the profile screen (nome, data de nascimento, tipo sanguíneo) |
| Health profile | “Dados de saúde” screen, reached from “Resumo” > fotografia ou iniciais | https://support.apple.com/pt-pt/guide/iphone/iphcae7451f3/ios | Same screen as above |
| Health records | registos de saúde ("Ver os registos de saúde na aplicação Saúde no iPhone"); "Registos de saúde de prestadores de cuidados de saúde" | https://support.apple.com/pt-pt/guide/iphone/iphbb8259c61/ios | |
| Medical ID | **ficha médica** ("Configurar e ver a ficha médica no Apple Watch"; screen “Ficha médica”; "ficha médica de emergência") | https://support.apple.com/pt-pt/guide/watch/apd58cd0b3f4/watchos ; https://support.apple.com/pt-pt/guide/iphone/iphbb8259c61/ios | Verified (the Spanish file could not verify this one) |
| Health category (Summary pins) | categorias de saúde; ecrã “Resumo”; lista “Afixados”; “Destaques”; “Tendências”; ecrã “Categorias de Saúde” (Explorar) | https://support.apple.com/pt-pt/guide/iphone/iphe3d379c32/ios | "Afixar ao resumo" (pin), "Desafixar" (unpin). Not "Fixados" |
| Sleep (in Health) | Sono (aplicação Sono on Apple Watch; “Configurar Sono”; Saúde > “Explorar” > “Sono” > “Sono”) | https://support.apple.com/pt-pt/guide/iphone/iphaf56dceb4/ios ; https://support.apple.com/pt-pt/guide/iphone/iph72b370881/ios ; https://support.apple.com/pt-pt/108906 ; https://support.apple.com/pt-pt/guide/watch/crpxel1lvun9/watchos | All Portugal pages agree on "Sono" (iPhone guide, article, Watch guide). No "Descanso" tab as in the Spanish iOS 27 guide. Schedule: "horário de sono"; goal: “Meta de sono”; Watch feature “Registo de sono” |
| Sleep Focus | modo de concentração “Dormir” (iPhone guide, article 108906: "Modo de concentração "Dormir""); Focus mode name: Dormir | https://support.apple.com/pt-pt/guide/iphone/iphd6288a67f/ios ; https://support.apple.com/pt-pt/guide/iphone/iphaf56dceb4/ios ; https://support.apple.com/pt-pt/108906 | Not "Descanso". Focus list: “Não incomodar”, “Sem mensagens ao conduzir”, “Dormir”, “Pessoal”, “Trabalhar” (also “Tempo pessoal” in the same page) |
| Sleep Score | **Classificação do sono** ("Ver a classificação do sono"; "pontuação da Classificação do sono de 0 a 100"); scale Muito baixa 0-40, Baixa 41-60, OK 61-80, Alta 81-95, Muito alta 96+ | https://support.apple.com/pt-pt/guide/watch/apded441a669/watchos ; https://support.apple.com/pt-pt/108906 | "classificação", not "pontuação" for the feature name. Note the middle band is "OK", not "Aceitável" |
| Sleep apnea notifications | Notificações de apneia do sono (page title "Receber notificações de apneia do sono no Apple Watch") | https://support.apple.com/pt-pt/guide/watch/apd4e7713562/watchos | Portugal says "apneia" (Spain "apnea") |
| Sleep stages Awake / REM / Core / Deep | **Acordado / Sono REM / essencial / profundo** (article: "o tempo e a percentagem que passou Acordado ou em Sono REM, essencial ou profundo"; Watch guide: "sono REM, essencial ou profundo"); the word for a stage: "fases do sono" | https://support.apple.com/pt-pt/108906 ; https://support.apple.com/pt-pt/guide/watch/crpxel1lvun9/watchos ; https://support.apple.com/pt-pt/guide/iphone/iph72b370881/ios | Core = "essencial". No pages with a capitalised Core/Deep label were found; the article writes "Acordado" capitalised and the others lowercase after "Sono REM" |
| Heart Rate Variability (HRV) | variabilidade da frequência cardíaca; abbreviation **VFC** ("a variabilidade da frequência cardíaca (VFC)"); "variabilidade da frequência cardíaca de recuperação (VFC)" | https://support.apple.com/pt-pt/guide/watch/flx4gnzby346/watchos ; https://support.apple.com/pt-pt/guide/watch/apd15aa7ed96/watchos | Apple Portugal abbreviates VFC, never HRV. Series 12 / Ultra 4 only |
| Resting heart rate | frequência cardíaca em repouso (Watch labels: “Intervalo”, “Em repouso”, “Média a andar”) | https://support.apple.com/pt-pt/guide/iphone/iphe3d379c32/ios ; https://support.apple.com/pt-pt/guide/watch/apda88aefe4c/watchos | Accent: "cardíaca" |
| Heart rate | frequência cardíaca; a aplicação Frequência cardíaca (Watch) | https://support.apple.com/pt-pt/guide/watch/apda88aefe4c/watchos | |
| Respiratory rate | frequência respiratória | https://support.apple.com/pt-pt/guide/watch/apd15aa7ed96/watchos ; https://support.apple.com/pt-pt/108906 | |
| Heart rate zones | zonas de frequência cardíaca ("Ver as zonas de frequência cardíaca no Apple Watch") | https://support.apple.com/pt-pt/guide/watch/apd897dccddf/watchos | |
| ECG app | a aplicação ECG; eletrocardiograma (ECG) | https://support.apple.com/pt-pt/guide/watch/apdea4c50a57/watchos | Saúde > Explorar > Coração > “Eletrocardiograma (ECG)” |
| AFib History | not verified | no pt-pt page naming it was found (the Watch heart pages only mention "avisos de ritmo cardíaco irregular") | Do not invent "Histórico de fibrilhação auricular" |
| Irregular rhythm notifications | avisos de ritmo cardíaco irregular; "ritmos cardíacos irregulares" | https://support.apple.com/pt-pt/guide/iphone/iphbb8259c61/ios ; https://support.apple.com/pt-pt/guide/watch/apda88aefe4c/watchos | |
| Vitals app | a aplicação **Sinais Vitais** (title case); "sinais vitais noturnos"; “Sinais vitais durante a noite”; "métricas de saúde noturnas" | https://support.apple.com/pt-pt/guide/watch/apd15aa7ed96/watchos | "sinais vitais", not "constantes vitais" (that is Spain) |
| Readiness app (watchOS 27) | a aplicação **Preparação**; pontuação de preparação (0 a 10) | https://support.apple.com/pt-pt/guide/watch/flx4gnzby346/watchos | Series 12 and Ultra 4 only. Not "Prontidão" (Observa's own Portuguese text uses that; Apple does not) |
| Training Load | **carga de treino** ("Monitorizar a carga de treino no Apple Watch"; scale "de muito abaixo a muito acima") | https://support.apple.com/pt-pt/guide/watch/apde4c07a6cf/watchos | |
| Cardio Fitness | **cardiofitness** (one word, lowercase; "Controlar os seus níveis de cardiofitness"; Saúde > Coração > Cardiofitness) | https://support.apple.com/pt-pt/108790 ; https://support.apple.com/pt-pt/guide/iphone/iphbb8259c61/ios ("nível baixo de cardiofitness") | |
| VO2 max | **VO2 máx.** ("o volume de oxigénio máximo (VO2 máx.), a quantidade máxima de oxigénio que o corpo pode consumir durante a prática de exercício") | https://support.apple.com/pt-pt/108790 | "oxigénio" with accent (Brazil: "oxigênio") |
| Cycle Tracking | **Seguimento do ciclo** (app and feature; "Configurar Seguimento do ciclo"); "ciclo menstrual" in prose | https://support.apple.com/pt-pt/guide/watch/apd26429adf0/watchos ; https://support.apple.com/pt-pt/guide/iphone/iphcae7451f3/ios | |
| Mindfulness app | a aplicação **Atenção Plena**; sessions “Refletir” and “Respirar”; "atenção plena" in prose; "minutos de atenção plena" | https://support.apple.com/pt-pt/guide/watch/apd371dfe3d7/watchos ; https://support.apple.com/pt-pt/guide/iphone/iphe3d379c32/ios | Not "Mindfulness" |
| State of Mind | **Estado de espírito** (Explorar > “Bem‑estar mental” > “Estado de espírito”; "Registar o estado de espírito") | https://support.apple.com/pt-pt/guide/iphone/iph6a6decb13/ios | Not "estado de ânimo" (Spain) |
| Medications | **Medicação** (Explorar > “Medicação”) and “Medicamentos” (intro page); "Adicionar um medicamento", "Seguir os medicamentos na aplicação Saúde" | https://support.apple.com/pt-pt/guide/iphone/iph811670c81/ios ; https://support.apple.com/pt-pt/guide/iphone/iphcae7451f3/ios | Apple itself is inconsistent: the guide intro says “Medicamentos”, the medications page says “Medicação”. Use "Medicação" for the feature, "medicamentos" for the things |
| Walking Steadiness | **estabilidade a andar** (“Notificações de estabilidade a andar”) | https://support.apple.com/pt-pt/guide/iphone/iphff1bf03ed/ios | Not "estabilidade ao caminhar" |
| Mobility | Mobilidade (Explorar > Mobilidade) | https://support.apple.com/pt-pt/guide/iphone/iphff1bf03ed/ios | |
| Activity rings | anéis de atividade ("anéis de atividade" in the Fitness app; the Watch guide capitalises the app as Atividade) | https://support.apple.com/pt-pt/guide/iphone/ipha5dddb411/ios ; https://support.apple.com/pt-pt/guide/watch/apd3bf6d85a6/watchos | "atividade" without the c |
| Move / Exercise / Stand rings | anel vermelho **Movimento** / anel verde **Exercício** / anel azul “**De pé**” (quoted); wheelchair ring: **Deslocação** | https://support.apple.com/pt-pt/guide/watch/apd3bf6d85a6/watchos | "Movimento, Exercício e “De pé”" |
| Fitness app | a aplicação Fitness (iPhone; tabs “Resumo”, “Treino”) | https://support.apple.com/pt-pt/guide/iphone/ipha5dddb411/ios | English kept |
| Activity app (Apple Watch) | a aplicação Atividade | https://support.apple.com/pt-pt/guide/watch/apd3bf6d85a6/watchos | |
| Workout app | **a aplicação Treino**; "treino" / "treinos" (workout / workouts); "Iniciar um treino" | https://support.apple.com/pt-pt/guide/watch/apdd16e8761a/watchos ; https://support.apple.com/pt-pt/108790 ("app Treino") | Not "Exercício" for the workout and not "entreno" (Spain) |
| Workouts (the plural) | treinos | same | |
| Stand hours | horas de pé | https://support.apple.com/pt-pt/guide/watch/apd3bf6d85a6/watchos | Also "minutos de pé" |
| Exercise minutes | minutos de exercício | https://support.apple.com/pt-pt/guide/iphone/iphbb8259c61/ios | |
| Active energy / calories | calorias ativas | https://support.apple.com/pt-pt/guide/watch/apd3bf6d85a6/watchos | |
| Flights climbed | **lanços de escadas** ("quantos lanços de escada sobe") | https://support.apple.com/pt-pt/guide/iphone/iphbb8259c61/ios | Not "andares"/"pisos" |
| Steps | passos | https://support.apple.com/pt-pt/guide/iphone/iphbb8259c61/ios | |
| Headphone audio levels | níveis do áudio dos auscultadores; “Notificações dos auscultadores”; meter “Nível dos auscultadores”; control “Audição” | https://support.apple.com/pt-pt/guide/iphone/iph0596a9152/ios | Portugal says "auscultadores" (Brazil "fones") |
| Noise / environmental sound | a aplicação **Ruído**; níveis de ruído; "níveis de som ambiente" | https://support.apple.com/pt-pt/guide/watch/apd00a43a9cb/watchos (title "Medir níveis de ruído com o Apple Watch") | |
| Wrist temperature | **temperatura no pulso** ("Registar a temperatura no pulso durante a noite no Apple Watch") | https://support.apple.com/pt-pt/102674 ; https://support.apple.com/pt-pt/guide/watch/apd526d20feb/watchos | "pulso", not "punho" (Spain "muñeca") |
| Blood Oxygen | **Oxigénio no Sangue** (app, title case in the Watch guide index); oxigénio no sangue (prose; Vitals: "oxigénio no sangue*") | https://support.apple.com/pt-pt/guide/watch/apd15aa7ed96/watchos ; wg (index) | "oxigénio" with accent |
| Apple Watch | o Apple Watch | wg ; ap ; https://support.apple.com/pt-pt/108906 | English kept |
| Apple Fitness+ | Apple Fitness+ | https://support.apple.com/pt-pt/guide/iphone/iph6e7917d3f/ios ; https://www.apple.com/pt/apple-fitness-plus/ | English kept. Marketing: "1 mês de Apple Fitness+ grátis", "9,99 € todos os meses ou 59,99 € anualmente" |
| Journal app | a aplicação **Diário** ("Escrever no diário no iPhone") | https://support.apple.com/pt-pt/guide/iphone/iph9824e83ce/ios | |

## System features

| English | Portuguese (Portugal) as Apple writes it | Source | Note |
|---|---|---|---|
| Settings | a aplicação **Definições**; Definições do Sistema (Mac) | https://support.apple.com/pt-pt/guide/iphone/iphd6804774e/ios ; https://support.apple.com/pt-pt/guide/mac-help/mchlc9d0e1f2/mac ; https://support.apple.com/pt-pt/guide/mac-help/mchl534ba392/mac | Not "Ajustes", not "Configurações" (Brazil). "Definições do Sistema" with capital S |
| Screen Time | “**Tempo de ecrã**” (guide: capital T, lowercase rest); "Tempo de ecrã" capitalised as feature | https://support.apple.com/pt-pt/guide/iphone/iphbfa595995/ios | 49 hits. Not "Tempo de Uso" (Brazil), not "Tempo de utilização". Page title: "Configurar o tempo de ecrã para si no iPhone" (lowercase) |
| Screen Time Schedules (iOS 27) | “Horário de tempo de ecrã”; "horários de tempo permitido" | same | |
| Screen Time Limits | “Limites de tempo”; "limites de tempo permitido"; "limites de tempo das aplicações" | same | Also “Gerir tempo de ecrã”, “Partilhar entre dispositivos”, “Ativar atividade em aplicações e sites”, “Média diária” |
| Downtime / App Limits (iOS 26 and earlier) | not verified | the iOS 26 and 18 guide pages for these were not located on pt-pt (the iOS 18 page with the Screen Time id returns a different page) | |
| Screen Time weekly report | relatório semanal de Tempo de ecrã; “Média diária”; “Semana” / “Dia”; "ativações e notificações" | https://support.apple.com/pt-pt/guide/iphone/iphbfa595995/ios | |
| Screen Distance | not verified | no Portugal marketing or guide page opened | |
| Focus | **modo de concentração** (lowercase, plural "modos de concentração"); Settings label “Concentração”; control-centre tile “Modo de concentração” | https://support.apple.com/pt-pt/guide/iphone/iphd6288a67f/ios ; https://support.apple.com/pt-pt/guide/iphone/iph5c3f5b77b/ios | 134 hits "modo de concentração". Not "Foco" (Brazil; one stray "Foco" in a Mac image caption on the Mac control-centre page) |
| Do Not Disturb | “Não incomodar” | same | |
| Reduce Interruptions (Focus) | “Reduzir interrupções” (uses Apple Intelligence) | https://support.apple.com/pt-pt/guide/iphone/iphd6288a67f/ios | |
| Focus Filter / link Focus to Lock Screen | "associar um ecrã bloqueado a um modo de concentração" | https://support.apple.com/pt-pt/guide/iphone/iph4d0e6c351/ios | Focus Filter name not verified |
| Family Sharing | **Partilha com a família** (capital P, no quotes in running text; “Partilha com a família” when a setting); "um grupo de Partilha com a família"; Definições > Família; “Partilha de compras” | https://support.apple.com/pt-pt/guide/iphone/iph4cd8953e2/ios ; https://support.apple.com/pt-pt/guide/iphone/iph6e7917d3f/ios ; ap (Things 3) | 48 hits. Not "Compartilhamento Familiar" (Brazil) |
| Family sharing label on the product page | "Partilha com a família: Se tiver ativado a Partilha com a família, esta aplicação pode ser usada por até seis membros da família." (paid app); "É possível que algumas compras integradas e assinaturas possam ser partilhadas com o grupo familiar quando a Partilha com a família estiver ativada." (app with in-app purchases) | https://apps.apple.com/pt/app/id904237743 ; https://apps.apple.com/pt/app/id6757438990 | Exact store text |
| Ask to Buy | **Pedir para comprar** (“Pedir para comprar”; article title "Aprovar o que a criança pode comprar e descarregar com a funcionalidade Pedir para comprar") | https://support.apple.com/pt-pt/105055 ; https://support.apple.com/pt-pt/guide/iphone/iph6e7917d3f/ios | 24 hits |
| Parental controls | controlo parental ("funcionalidades de controlo parental") | https://support.apple.com/pt-pt/guide/iphone/iphbfa595995/ios | Not "controle parental" |
| Family Controls (framework) | not verified | developer docs are English; the user-facing feature is “Tempo de ecrã” and controlo parental | |
| In-App Purchases | **compras integradas** (store label "Compras integradas"; guide: "tudo sem anúncios ou compras integradas") | https://apps.apple.com/pt/app/id6757438990 ; https://support.apple.com/pt-pt/guide/iphone/iphc90580097/ios ; https://support.apple.com/pt-pt/118223 ("do sistema de compras integradas da Apple") | Not "compras na app", not "compras dentro da app" (Spain) |
| Subscriptions (manage) | "Em Definições, toque no seu nome. Toque em Assinaturas. Toque na assinatura. Toque em Cancelar assinatura." (Mac: "Na App Store, clique no seu nome na parte inferior da barra lateral... Clique em Assinaturas... Clique em Cancelar assinatura.") | https://support.apple.com/pt-pt/118428 | Article title: "Cancelar uma assinatura da Apple". iPhone guide: "Vá à aplicação Definições no iPhone. Toque no seu nome e, depois, toque em “Assinaturas”." |
| Cancel subscription (button) | **Cancelar assinatura** (article, bare); “Cancelar assinatura” and “Cancelar todos os serviços” (guide, quoted); "Renovar" for an expired one | https://support.apple.com/pt-pt/118428 ; https://support.apple.com/pt-pt/guide/iphone/iph4e3e7324f/ios | Expired: "vir uma mensagem de expiração a vermelho". Trial: "cancele-a pelo menos 24 horas antes do fim do período experimental" |
| Apple Account (ex Apple ID) | **conta Apple** (lowercase in prose; 92 hits); “Conta Apple” (settings row/button; 6 hits) | https://support.apple.com/pt-pt/guide/iphone/iph76e54c61e/ios ; https://support.apple.com/pt-pt/118223 | No "ID Apple", no "Apple ID" anywhere on the pages checked |
| iCloud | iCloud | https://support.apple.com/pt-pt/guide/iphone/iphde0f868fd/ios | English kept; "em iCloud" |
| iCloud+ | iCloud+ ("Assinar iCloud+") | https://support.apple.com/pt-pt/guide/iphone/iphde0f868fd/ios ; https://www.apple.com/pt/icloud/ | Marketing plans: "50 GB 0,99 €/mês", "200 GB 2,99 €/mês", "2 TB 9,99 €/mês" |
| iCloud Drive | iCloud Drive | https://support.apple.com/pt-pt/guide/iphone/iphbbcf8827d/ios | |
| iCloud Photos | **Fotografias em iCloud** (article 108922: "as Fotografias em iCloud"); iCloud settings list shows "Fotografias" | https://support.apple.com/pt-pt/108922 ; https://support.apple.com/pt-pt/guide/iphone/iphde0f868fd/ios | "fototeca" for the library, "fotografias e vídeos" |
| Sync this iPhone (iCloud Drive toggle) | “Sincronizar este iPhone” (Definições > [o seu nome] > iCloud > “Drive”) | https://support.apple.com/pt-pt/guide/iphone/iphbbcf8827d/ios | |
| iCloud sync | "manter atualizado entre todos os dispositivos"; "sincronizar com iCloud"; Health toggle “Sincronizar com o iPhone” | https://support.apple.com/pt-pt/guide/iphone/iphde0f868fd/ios ; https://support.apple.com/pt-pt/guide/iphone/iph11f1eb698/ios | No fixed noun phrase |
| iCloud backup | **cópia de segurança em iCloud**; iCloud settings row "Cópia em iCloud"; page title "Efetuar cópias de segurança dos dados da aplicação Saúde em iCloud no iPhone" | https://support.apple.com/pt-pt/guide/iphone/iphde0f868fd/ios ; https://support.apple.com/pt-pt/guide/iphone/iph11f1eb698/ios | "cópia de segurança", not "backup" |
| Advanced Data Protection | **Proteção de dados avançada** ("Como ativar a Proteção de dados avançada para iCloud"; capital P in article titles) | https://support.apple.com/pt-pt/108756 ; https://support.apple.com/pt-pt/102651 | Order "dados avançada" as in Spain |
| Standard data protection | "Proteção de dados padrão" ("é a predefinição da conta") | https://support.apple.com/pt-pt/102651 | |
| Data Protection (iOS file encryption) | not verified | https://support.apple.com/pt-pt/guide/security/secf6276da8a/web returns the English "Data Protection overview" page on pt-pt | The Platform Security guide is not translated for Portugal |
| Apple Push Notification service (APNs) | not verified | https://support.apple.com/pt-pt/guide/security/aside/sec19eabb530/web returns 404 | For users: "notificações" |
| Home Screen | **ecrã principal** (41 hits); "ecrã inicial" once or twice (4 hits, e.g. the Screen Time page) | https://support.apple.com/pt-pt/guide/iphone/iphb8f1bf206/ios ; https://support.apple.com/pt-pt/guide/iphone/iphbfa595995/ios | Prefer "ecrã principal". Not "tela de início" |
| Lock Screen | **ecrã bloqueado** (88 hits; "Ecrã bloqueado" capitalised in article 108906) | https://support.apple.com/pt-pt/guide/iphone/iph4d0e6c351/ios ; https://support.apple.com/pt-pt/108906 | Not "ecrã de bloqueio", not "tela bloqueada" |
| Widgets | widgets; galeria de widgets; “Adicionar widget”; "Editar widgets" (Mac) | https://support.apple.com/pt-pt/guide/iphone/iphb8f1bf206/ios ; https://support.apple.com/pt-pt/guide/mac-help/mchl52be5da5/mac | English kept |
| Smart Stack | **pilha inteligente** ("Uma pilha inteligente (um widget com dois pontos ao lado)"; Watch: "Ver widgets úteis na pilha inteligente") | https://support.apple.com/pt-pt/guide/iphone/iphb8f1bf206/ios ; https://support.apple.com/pt-pt/guide/watch/apdecf142fb9/watchos | 31 hits, 0 "Smart Stack" |
| Live Activities | **atividades em tempo real** ("Ver atividades em tempo real na Dynamic Island no iPhone") | https://support.apple.com/pt-pt/guide/iphone/iph28f50d10d/ios ; https://support.apple.com/pt-pt/guide/watch/bz1vx4mwqbw9/watchos | 24 hits. Not "Live Activities", not "atividades em direto" (Spain) |
| Dynamic Island | Dynamic Island (feminine: "na Dynamic Island") | https://support.apple.com/pt-pt/guide/iphone/iph28f50d10d/ios | English kept |
| StandBy | **“Em espera”** (funcionalidade “Em espera”; "modo Em espera"; Definições > “Em espera”) | https://support.apple.com/pt-pt/guide/iphone/iph878d77632/ios | Not "StandBy". |
| Control Center | **central de controlo** (lowercase in the guide; "Central de controlo" in article 108350) | https://support.apple.com/pt-pt/guide/iphone/iph59095ec58/ios ; https://support.apple.com/pt-pt/guide/mac-help/mchlc9d0e1f2/mac | 77 hits. Not "Centro de controlo" (0 hits), not "Central de controle" (Brazil) |
| Notification Center | **central de notificações** | https://support.apple.com/pt-pt/guide/iphone/iph6534c01bc/ios | 26 hits, 0 "centro de notificações" |
| Notifications | notificações (“Permitir notificações”, “Notificações importantes”, “Resumir notificações”, “Resumo programado”, “Apresentação imediata”) | https://support.apple.com/pt-pt/guide/iphone/iph7c3d96bab/ios ; https://support.apple.com/pt-pt/guide/iphone/iph1fbe7d2b9/ios | Time Sensitive = “Notificações importantes” |
| Share Sheet / Share button | botão Partilhar; menu “Partilhar” | https://support.apple.com/pt-pt/guide/iphone/iphc572ca489/ios | Share-sheet noun not verified |
| AirDrop | AirDrop ("Usar AirDrop para enviar elementos para dispositivos Apple por perto"; options “Só contactos”, “Todos durante 10 minutos”) | https://support.apple.com/pt-pt/guide/iphone/iphcd8b9f0af/ios | English kept |
| Spotlight | Spotlight | https://support.apple.com/pt-pt/guide/iphone/iph3c511548/ios | English kept |
| Siri | Siri (guide: bare; articles: "a Siri"); “Siri” ou “Ei Siri”; Definições > Siri | https://support.apple.com/pt-pt/guide/iphone/iph83aad8922/ios ; https://support.apple.com/pt-pt/105020 | "Ei Siri" (Spain "Oye Siri") |
| Apple Intelligence | Apple Intelligence | https://support.apple.com/pt-pt/guide/iphone/iph1fbe7d2b9/ios ; https://www.apple.com/pt/apple-intelligence/ | English kept |
| Shortcuts (app) | **a aplicação Atalhos**; atalhos; “Galeria”, “Automatização” tabs | https://support.apple.com/pt-pt/guide/iphone/iph47e1c9d7d/ios ; https://support.apple.com/pt-pt/guide/shortcuts/welcome/ios (title "Manual de Utilização da aplicação Atalhos") | Keyboard shortcuts also "atalhos de teclado" |
| Universal Clipboard | **Clipboard universal** ("uma funcionalidade denominada Clipboard universal") | https://support.apple.com/pt-pt/guide/iphone/iph220ea8dca/ios | Masculine ("o Clipboard universal"); the word "clipboard" stays English, never "área de transferência" (0 hits) |
| Copy / Paste | “Copiar” / “Colar” | same | |
| Handoff | Handoff | same | English kept |
| Picture in Picture | **picture-in-picture** (lowercase, hyphenated, sometimes U+2011) ("Multitarefa com picture-in-picture no iPhone") | https://support.apple.com/pt-pt/guide/iphone/iphcc3587b5d/ios | Not translated; 0 "imagem dentro de imagem" |
| Airplane Mode | **modo de voo** | https://support.apple.com/pt-pt/guide/iphone/iph59095ec58/ios ; https://support.apple.com/pt-pt/guide/watch/apdc22c9d320/watchos ("Usar o modo de voo no Apple Watch") | 15 hits, 0 "modo avião" |
| Low Power Mode | **Modo de baixo consumo**; iOS 27: “Modo de consumo” / “Modo alimentação” and “Consumo adaptável” | https://support.apple.com/pt-pt/guide/iphone/iphcab9aecd1/ios | The page itself mixes “Modo alimentação” and “Modo de consumo” |
| Dark Mode | **Modo escuro** (article: capital M; guide: lowercase "modo escuro", 16 hits); setting Definições > “Ecrã e brilho” > “Tons escuros”; automatic: “Automático” | https://support.apple.com/pt-pt/108350 | |
| Appearance (iOS 27) | “**Apresentação**” (Definições > Apresentação > “Tamanho do texto”, “Negrito”, “Liquid Glass”, “Ampliação do ecrã” > “Texto maior”) | https://support.apple.com/pt-pt/guide/iphone/iphd6804774e/ios | Not "Aspecto" (Spain) |
| Accessibility | Acessibilidade | https://support.apple.com/pt-pt/guide/iphone/iph3e2e4367/ios | |
| VoiceOver | "leitor de ecrã incorporado" in prose; VoiceOver as feature name not opened | https://support.apple.com/pt-pt/guide/iphone/iph3e2e4367/ios | Name kept English elsewhere |
| Larger Text (Dynamic Type setting) | “**Tamanho do texto**” (Apresentação); “Texto maior” (under “Ampliação do ecrã”); “Tamanho do texto e visualização” (Acessibilidade) | https://support.apple.com/pt-pt/guide/iphone/iphd6804774e/ios | |
| Reduce Motion | **Reduzir movimento** (Definições > Acessibilidade > Movimento > Reduzir movimento) | https://support.apple.com/pt-pt/111781 | Title: "Reduzir o movimento do ecrã no iPhone, iPad ou iPod touch". Store accessibility label: "Movimento reduzido" |
| Offline | offline ("Descarregar mapas offline", "ouvir offline") | ig TOC | English word kept; "sem ligação" not seen |
| Privacy & Security | **Privacidade e segurança** (bare in paths: "Definições > Privacidade e segurança") | https://support.apple.com/pt-pt/guide/iphone/iph4f4cbd242/ios ; https://support.apple.com/pt-pt/guide/iphone/iph251e92810/ios | "Relatório de privacidade das aplicações" |
| App Tracking | **Seguimento** (Definições > Privacidade e segurança > Seguimento); toggle “**Permitir pedidos de seguimento das aplicações**” | https://support.apple.com/pt-pt/guide/iphone/iph4f4cbd242/ios ; https://support.apple.com/pt-pt/102420 | The tracking word is "seguimento" (55 hits) / "seguir a sua atividade"; "rastreio" 0 hits, "rastreamento" is Brazilian. See App Tracking Transparency below |
| Analytics share with developers | Definições > Privacidade e segurança > **Análise** (or “Análise e melhorias”) > “Partilhar análise do iPhone e do Apple Watch”; “Partilhar com os programadores” (older) | https://support.apple.com/pt-pt/108971 | Newest label not re-read beyond the article |
| Background App Refresh | not verified | no pt-pt page found with the label | |
| Restore purchases | Apple's phrases: "Restaurar elementos comprados e apagados no iPhone"; "Voltar a descarregar aplicações da Apple"; "Descarregar novamente os programas de TV e filmes comprados" | https://support.apple.com/pt-pt/guide/iphone/iphfe205f2e5/ios | In-app StoreKit "Restore Purchases" button label not documented on a Portugal page |

## Built-in apps

| English | Portuguese (Portugal) as Apple writes it | Source | Note |
|---|---|---|---|
| Reminders | **Lembretes** (a aplicação Lembretes) | ig TOC ; https://support.apple.com/pt-pt/guide/iphone/iph3d110f84/ios | |
| Calendar | **Calendário** (a aplicação Calendário); event = "evento"; "aviso" for an alert | https://support.apple.com/pt-pt/guide/iphone/iph3d110f84/ios | |
| Files | **Ficheiros** (a aplicação Ficheiros) | https://support.apple.com/pt-pt/guide/iphone/iphbbcf8827d/ios | Not "Arquivos" (Brazil) |
| Photos | **Fotografias** (a aplicação Fotografias) | ig TOC ; https://support.apple.com/pt-pt/guide/iphone/iph3c511548/ios | Not "Fotos" |
| Camera | **Câmara** (a aplicação Câmara; "controlo da câmara") | ig TOC (section "Câmara") | Not "Câmera" |
| Notes | Notas | ig TOC | |
| Clock / Alarm | Relógio (a aplicação Relógio); alarme; despertador; "Definir um alarme" | ig TOC ; https://support.apple.com/pt-pt/guide/iphone/iphaf56dceb4/ios | |
| Weather | **Meteorologia** (a aplicação Meteorologia; "estado do tempo") | ig TOC ; wg index ; https://support.apple.com/pt-pt/111781 | Not "Tempo" (Spain) |
| Games app | a aplicação **Jogos**; "Apple Games" in prose; Game Center | https://support.apple.com/pt-pt/guide/iphone/iph3aed54d2e/ios | Tabs: “Início”, “Amigos”, “Biblioteca” |
| Wallet | **Carteira** (a aplicação Carteira); "Apple Wallet" appears once in a sentence about availability | https://support.apple.com/pt-pt/guide/iphone/iph9b7f53382/ios ; https://support.apple.com/pt-pt/guide/watch/apd16914b6d1/watchos | Not "Wallet" as the app name |
| Apple Pay | Apple Pay | https://support.apple.com/pt-pt/guide/iphone/iphbd4cf42b4/ios ; https://www.apple.com/pt/apple-pay/ | English kept |
| Sign in with Apple | **“Iniciar sessão com a Apple”** (21 hits) | https://support.apple.com/pt-pt/guide/iphone/iph238921d37/ios | Buttons “Partilhar o meu e‑mail”, “Ocultar o meu e‑mail” |
| Passwords | Palavras-passe (hyphen) | ig TOC | |
| Maps | Mapas | ig TOC | |
| Stocks | Bolsa | ig TOC ("Consultar a bolsa") | |
| Messages / Mail / Safari | Mensagens / Mail / Safari | ig TOC | |
| Voice Memos | **Dictafone** | ig TOC ; https://support.apple.com/pt-pt/guide/iphone/iph28f50d10d/ios | |
| Phone | Telefone | ig TOC | |

## Devices and platforms

| English | Portuguese (Portugal) as Apple writes it | Source | Note |
|---|---|---|---|
| iPhone, iPad, Mac | iPhone, iPad, Mac (o iPhone, o iPad, o Mac) | ap ; ig | |
| Apple Watch | o Apple Watch | ap ; wg | |
| Apple Vision Pro | Apple Vision Pro ("Cancelar uma assinatura no Apple Vision Pro"); store compatibility label "Apple Vision" | https://support.apple.com/pt-pt/118428 ; https://apps.apple.com/pt/app/id6757438990 | |
| iOS, iPadOS, macOS, watchOS, visionOS | unchanged ("Requer o iOS 17.6 ou posterior.") | ap | With the article "o": "Requer o iOS", "Requer o watchOS 10.0 ou posterior." |
| Designed for iPad / iPhone (on Mac) | "Desenvolvida para iPad. Não verificada para macOS." (Observa); "Desenvolvida para iPhone. Não verificada para macOS." (LiftLog) | https://apps.apple.com/pt/app/id6757438990 ; https://apps.apple.com/pt/app/id6760043411 | Feminine participle ("Desenvolvida", "verificada") because it agrees with "aplicação/app". Copy exactly |
| Mac chip wording | "Requer o macOS 14.6 ou posterior e o processador M1 da Apple ou posterior." | https://apps.apple.com/pt/app/id6757438990 | "processador", not "chip" (Spain) |

## App Store and developer

| English | Portuguese (Portugal) as Apple writes it | Source | Note |
|---|---|---|---|
| App Store | **a App Store** (feminine; "na App Store", "da App Store"); the app: "a aplicação App Store" | https://support.apple.com/pt-pt/guide/iphone/iphc90580097/ios ; https://www.apple.com/pt/app-store/ ; https://support.apple.com/pt-pt/118428 | 38 feminine vs 0 masculine hits. Unlike Spain ("el App Store") |
| "Download on the App Store" badge | **Line 1: Descarregar na / Line 2: App Store** | https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/pt-pt (SVG title `Download_on_the_App_Store_Badge_PTPT_RGB_blk_100317`; same file at https://toolbox.marketingtools.apple.com/api/v2/badges/download-on-the-app-store/black/pt-pt; rendered with rsvg-convert and read 2026-11-19) | The locale code in the file name is `PTPT`. Artwork is outlined paths, so there is no text node; read from the rendered image |
| "Download on the Mac App Store" badge | **Line 1: Descarregar na / Line 2: Mac App Store** | https://tools.applemediaservices.com/api/badges/download-on-the-mac-app-store/black/pt-pt (SVG title `Download_on_the_Mac_App_Store_Badge_PTPT_RGB_blk_100317`; rendered and read) | |
| App Privacy (section) | **Privacidade da app** (section heading, repeated twice on the page) | https://apps.apple.com/pt/app/id6757438990 ; https://apps.apple.com/pt/app/id904237743 | Disclaimer: "Esta informação não foi confirmada pela Apple." |
| Data Not Collected | **Dados não recolhidos**; sub-line: "O programador não recolhe quaisquer dados desta app." | https://apps.apple.com/pt/app/id6757438990 ; https://apps.apple.com/pt/app/id6760043411 ; https://apps.apple.com/pt/app/id6756589122 | "recolhidos", not "coletados" |
| Data Used to Track You | **Dados utilizados para o seu seguimento** ("Os seguintes dados podem ser utilizados para o seu seguimento em apps e sites de outras empresas:") | https://apps.apple.com/pt/app/id284882215 ; https://apps.apple.com/pt/app/id389801252 | |
| Data Linked to You | **Dados associados a si** ("Os seguintes dados, que podem ser recolhidos e associados à sua identidade, podem ser utilizados para as seguintes finalidades:") | https://apps.apple.com/pt/app/id904237743 ; id284882215 | |
| Data Not Linked to You | **Dados não associados a si** ("Os seguintes dados podem ser recolhidos, mas não são associados à sua identidade:") | https://apps.apple.com/pt/app/id904237743 | |
| Purposes in the privacy label | "Publicidade de terceiros", "Análise de dados", "Personalização do produto", "Funcionalidade da app", "Outras finalidades"; categories "Conteúdo do utilizador", "Identificadores", "Dados de utilização", "Diagnósticos", "Localização", "Informações de contacto", "Histórico de pesquisa" | https://apps.apple.com/pt/app/id284882215 ; https://apps.apple.com/pt/app/id904237743 | "Publicidade ou marketing do programador" was not seen on the pages fetched |
| Privacy nutrition label | not verified as a noun phrase; the store section is "Privacidade da app"; Apple's help link text: “Definições de privacidade e exemplos” | https://apps.apple.com/pt/app/id904237743 | "etiqueta de privacidade" is NOT confirmed on any Apple Portugal page I fetched |
| Privacy Manifest | not verified | no pt page; developer.apple.com is not localized for Portugal | |
| App Store Connect | App Store Connect (English kept) | https://support.apple.com/pt-pt/guide/app-store-connect/welcome/web returns 404 | not verified |
| TestFlight | TestFlight (English kept) | https://support.apple.com/pt-pt/guide/testflight/welcome/ios redirects to a Korean 404 page | not verified |
| Xcode, CloudKit, Feedback Assistant | English kept | no Portugal developer page | not verified |
| Universal Purchase | not verified | no pt page | Do not invent "compra universal" |
| App Tracking Transparency | Apple Portugal's article title: "Se uma app pedir para seguir a sua atividade"; first sentence: "A Transparência do seguimento por apps permite-lhe optar se uma app pode seguir a sua atividade..."; buttons **Permitir** and **"Pedir à aplicação para não seguir"**; toggle “Permitir pedidos de seguimento das aplicações” | https://support.apple.com/pt-pt/102420 ; https://support.apple.com/pt-pt/guide/iphone/iph4f4cbd242/ios | The ATT system prompt title is not on any Portugal page fetched (not verified). "Transparência do seguimento por apps" is Apple's own name for ATT here |
| Report a Problem (reportaproblem.apple.com) | "Inicie sessão em reportaproblem.apple.com. Toque ou clique em **Gostaria** e, em seguida, selecione **Pedir um reembolso**." (guide: “Gostaria de”) | https://support.apple.com/pt-pt/118223 ; https://support.apple.com/pt-pt/guide/iphone/iph7b4e902b1/ios (title "Comunicar um problema com um jogo na aplicação Jogos no iPhone") | "Comunicar um problema" (not "Informar"/"Notificar") |
| Refund request | **Pedir um reembolso** (article "Pedir um reembolso para apps ou conteúdo que comprou na Apple"); steps: Inicie sessão > Gostaria > Pedir um reembolso > escolha o motivo > Seguinte > escolha a app > Enviar; "Aguardar 24 a 48 horas por notícias sobre o pedido" | https://support.apple.com/pt-pt/118223 | No refund promise; Apple says eligibility varies by country |
| Purchase history | **Histórico de compras** (App Store > a sua fotografia > “Aplicações e histórico de compras” > “Histórico de compras”) | https://support.apple.com/pt-pt/guide/iphone/iph4e3e7324f/ios | |
| Re-download apps | "Ver e descarregar novamente as aplicações"; “As suas aplicações”; “As minhas aplicações” | same | |
| Manage / cancel subscriptions (path) | Definições > o seu nome > Assinaturas > a assinatura > Cancelar assinatura | https://support.apple.com/pt-pt/118428 | |
| Price label | **Grátis** on the web product page ("Grátis · Compras integradas ·"); the iTunes lookup API returns "Gratuito" in `formattedPrice` | https://apps.apple.com/pt/app/id6757438990 ; lookup API | See the storefront section |
| Get button | **Obter** (raw `"title":"Obter"`, 34 hits on one page, 0 "Descarregar") | https://apps.apple.com/pt/app/id6757438990 ; https://support.apple.com/pt-pt/guide/iphone/iph4d0e6c351/ios | |

## Portuguese App Store product page labels

Copied from https://apps.apple.com/pt/app/id904237743 (Things 3, paid iPhone and Watch), https://apps.apple.com/pt/app/id6757438990 (Observa, free with in-app purchases), https://apps.apple.com/pt/app/id6760043411 (LiftLog), https://apps.apple.com/pt/app/id6756589122 (Mockly, paid Mac app), plus id284882215 and id389801252 for the privacy-tracking rows. Seller and person names are developer text and are not recorded here.

| Label | Exact Portuguese text |
|---|---|
| Price line (free app with IAP) | `Grátis · Compras integradas · Desenvolvida para iPad. Não verificada para macOS.` (LiftLog: `... Desenvolvida para iPhone. Não verificada para macOS.`). Separators are plain space, U+00B7 MIDDLE DOT, plain space |
| Price (paid) | `9,99 €` (Things 3), `14,99 €` (Mockly, Mac); Mac app also shows the tag "Apenas para Mac" |
| Free | Grátis (web page); Gratuito (lookup API) |
| Get button | Obter |
| Ratings section | "Classificações e críticas". Empty state: "Esta aplicação não recebeu classificações ou críticas suficientes para apresentar uma descrição geral." Paid app with ratings: `298 classificações` and `4,8` (aria: "4,8 estrelas"); large counts `425 mil classificações` (NBSP before "mil") |
| Rank | "Posição" `N.º 9` + category (Things 3) |
| Age rating | header chip: Classificação etária, value "4+" with caption "Anos" (Observa "9+" "Anos"); Information row: Idade "4+"; Observa adds Contém: "Tópicos de saúde ou bem-estar" |
| Category | header chip and row: Categoria (Things 3: Produtividade; Observa: Saúde e fitness; Mockly: Ferramentas de programação) |
| Developer | header chip: **Programador**; Information row: **Fornecedor** (with "identificou-se como comerciante desta app e confirmou que este produto ou serviço está em conformidade com a legislação da União Europeia.") |
| Language | header chip: Idioma ("PT + 33", "DE + 8"); Information row: Idiomas ("Português e mais 33", "Alemão e mais 8", then the full list; language names capitalised: Português, Alemão, Francês, Inglês, Espanhol, Holandês, Chinês simplificado) |
| Size | Tamanho: `127,9 MB`, `92,7 MB` (plain space before MB in the Information row; hero shows value and unit in separate spans) |
| Compatibility | Compatibilidade: "Requer o iOS 17.6 ou posterior." (NBSP inside "iOS 17.6") / "Requer o iPadOS 17.6 ou posterior." / Mac: "Requer o macOS 14.6 ou posterior e o processador M1 da Apple ou posterior." / Apple Vision: "Requer o visionOS 1.3 ou posterior." / Apple Watch: "Requer o watchOS 10.0 ou posterior." |
| Info section heading | Informação |
| Other Information rows | Endereço, Número de telefone, E-mail, Copyright, "Site do programador", "Política de Privacidade" (capital P), Suporte |
| In-App Purchases | Compras integradas: "Sim", then one row per item with price (`Premium anual 24,99 €`; NBSP before €) |
| Accessibility | Acessibilidade; "Funcionalidades suportadas"; labels "Interface escura", "Movimento reduzido", "Contraste suficiente" ("Permite aumentar o tamanho do texto na app para 200% ou mais.") |
| Family Sharing | "Partilha com a família" (see System features) |
| Privacy section | Privacidade da app; "Dados não recolhidos"; link “Definições de privacidade e exemplos”; disclaimer "Esta informação não foi confirmada pela Apple." |
| Privacy policy link | Política de Privacidade |
| Developer website | Site do programador |
| Other sections | Novidades (version "Versão: 3.25.3 -55 min", "Histórico de versões"); "Mais de: <programador>"; "Sugestões"; "Capturas de ecrã e pré-visualizações"; "Partilhar"; Siri block ("Tire maior partido desta aplicação usando-a com Siri."); footer: "Todos os direitos reservados.", "Termos de serviços da internet", "App Store e Privacidade", "Aviso acerca de cookies", "Suporte" |
| Platform names in nav | iPhone, iPad, Mac, Watch, TV ("Plataforma" menu; nav tabs: Hoje, Jogos, Apps, Arcade, Pesquisa; on the Mac App Store layout: Pesquisa, Descobrir, Arcade, Criar, Trabalhar, Jogar, Programar, Categorias) |
| Meta title / description | `<title>` = U+200E + `App <name> – App Store` (en dash U+2013 with spaces, NBSP inside "App Store"); og:description "Descarregue <name>, da autoria de <developer>, na App Store. Veja capturas de ecrã, classificações e críticas, sugestões de utilizadores e…" (NBSP inside "App Store"; note "na App Store" with the article; "capturas de ecrã", not "capturas de tela") |

In-app purchase price format: `24,99 €`. Comma decimal, then a **NO-BREAK SPACE (U+00A0)**, then €. Checked in the raw HTML (`<span>24,99&nbsp;€</span>`).

## Portuguese App Store category names

Read from the iTunes lookup API `https://itunes.apple.com/lookup?id=...&country=pt&lang=pt_pt` (`genres` field) on 2026-11-19, and confirmed on the product-page "Categoria" field for Things 3 (Produtividade), Observa (Saúde e fitness) and Mockly (Ferramentas de programação). The `apps.apple.com/pt/genre/...` pages were not opened.

| English | Portuguese as the App Store shows it | Sample (lookup id) |
|---|---|---|
| Health & Fitness | Saúde e fitness (NOT "Saúde e bem-estar", NOT "Saúde e forma física" as Spain) | 6757438990 (Observa) |
| Productivity | Produtividade | 1232780281 |
| Finance | Finanças | 283646709 |
| Business | Empresas | 618783545 |
| Developer Tools | Ferramentas de programação | 6756589122 (Mockly, product page) |
| Games > Puzzle | Puzzle | 6806255929 (Tare) |
| Games > Board | Tabuleiro | 6761336870, 6761656926 |
| Games > Strategy | Estratégia | 529479190 |
| Games > Adventure | Aventura | 479516143 |
| Games > Action | Ação | 529479190 |
| Games > Simulation | Simulações | 479516143 |
| Games > Casual | Casual | 6806255929 |
| Games (tab) | Jogos | nav tab on every page |
| Utilities | Utilitários | 6757253009 |
| Education | Ensino | 570060128 |
| Books | Livros | 302584613 |
| Lifestyle | Estilo de vida | 429047995, 6773507068 (Pawza) |
| Graphics & Design | Produção gráfica e design | 916366645 |
| Photo & Video | Fotografia e vídeo | 1500855883 |
| Reference | Referência | 324715238 |
| Entertainment | Entretenimento | 363590051 |
| Travel | Viagens | 401626263 |
| Music | Música | 324684580 |
| Navigation | Navegação | 585027354 |
| Food & Drink | Gastronomia e bebidas | 1058959277 |
| News | Notícias | 1064216828 |
| Sports | Desporto | 382002079 |
| Medical | Medicina | 321367289 |
| Weather | Meteorologia | 295646461 |
| Shopping | Compras | 282614216 |
| Social Networking | Redes sociais | 310633997 |

Not checked: Magazines & Newspapers, Kids, other Games subcategories (Card, Casino, Family, Music, Racing, Role Playing, Sports, Trivia, Word).

## Unverified (best guesses, not confirmed on an Apple Portugal page)

| English | Best guess | Why unverified |
|---|---|---|
| Apple Health (feature name) | none; use "aplicação Saúde" / "Saúde" | `www.apple.com/pt/health/` is a 404, and Apple's guides never use the English name |
| AFib History | none | No pt-pt page names it |
| Downtime / App Limits (iOS 26 and earlier) | none | Older guide pages not located; iOS 27 uses “Horário de tempo de ecrã” and “Limites de tempo” |
| Privacy nutrition label (noun) | none | Not on any Apple Portugal page fetched; the store uses "Privacidade da app" |
| Privacy manifest, Universal Purchase, App Store Connect, TestFlight, Xcode, CloudKit, Feedback Assistant, Family Controls, Dynamic Type (developer term), StoreKit "Restore Purchases" button | English kept | developer.apple.com is not localized for Portugal; support.apple.com/pt-pt guides for App Store Connect and TestFlight return 404 |
| Background App Refresh | none | No Portugal page with the label found |
| ATT system prompt title | none | Only the buttons and settings are documented |
| Data Protection (iOS file encryption), APNs | none | The Platform Security guide on pt-pt is English or 404 |
| Screen Distance, Focus Filter, share-sheet noun | none | No Portugal page opened or none names it |
| Analytics label (newest iOS) | “Análise e melhorias” | Article 108971 names it in the iOS 10 steps; newest label not re-read |
| Medications label | “Medicação” (page) vs “Medicamentos” (intro) | Apple's own pages disagree; use "Medicação" |
| Health tab name Explorar / Navegar | “Explorar” | The intro page of the iPhone guide says “Navegar” once; every other page says “Explorar” |

## Added rows (same extra rows as the French, German and Spanish files)

| English | Portuguese as Apple writes it | Source | Note |
|---|---|---|---|
| Medications (inconsistency) | iPhone guide intro: "toque em “Navegar”, toque em “Medicamentos” e, depois, toque em “Adicionar um medicamento”"; medications page: "Toque em “Explorar” e, depois, em “Medicação”" | https://support.apple.com/pt-pt/guide/iphone/iphcae7451f3/ios ; https://support.apple.com/pt-pt/guide/iphone/iph811670c81/ios | Use "Medicação" for the feature |
| Share With App Developers (Analytics) | Definições > Privacidade e segurança > Análise (e melhorias) > “Partilhar análise do iPhone e do Apple Watch” | https://support.apple.com/pt-pt/108971 | |
| Delete data from iCloud (storage path) | Definições > o seu nome > iCloud > ... ("Gerir o armazenamento em iCloud no dispositivo Apple") | https://support.apple.com/pt-pt/108922 | Exact tap target not re-read |
| Cancel a subscription | iPhone: "Toque em Cancelar assinatura"; Mac and Windows: "Clique em Cancelar assinatura" | https://support.apple.com/pt-pt/118428 | Expired: "mensagem de expiração a vermelho" |
| Request a refund | reportaproblem.apple.com > Gostaria > Pedir um reembolso | https://support.apple.com/pt-pt/118223 | |
| Camera app | **Câmara** | ig TOC | |
| Control Center on Mac | central de controlo (Mac: "clique no respetivo ícone na barra de menus") | https://support.apple.com/pt-pt/guide/mac-help/mchlc9d0e1f2/mac | "respetivo" (AO90, pt-PT) |
| Stage Manager | Stage Manager (kept in English; "Secretária e Stage Manager") | https://support.apple.com/pt-pt/guide/mac-help/mchl534ba392/mac | |
| Desktop widgets (Mac) | widgets na secretária; "central de notificações" | https://support.apple.com/pt-pt/guide/mac-help/mchl52be5da5/mac | |
| System Settings | Definições do Sistema (capital S) | https://support.apple.com/pt-pt/guide/mac-help/mchlc9d0e1f2/mac ; mg TOC ("Alterar as Definições do Sistema") | |
| Calendar event / Reminders list | evento; lembrete; lista | ig TOC | |

## Register: tu, você or neutral?

**Finding: Apple Portugal writes formal third-person singular imperatives with no pronoun, plus "o seu / a sua" possessives. It never writes "tu" and never writes "você".**

Counted 2026-11-19 on the raw text of the pages fetched.

| Corpus | Imperatives (formal) | Possessives "seu/sua/seus/suas" | "tu" forms | "você", "tu", "teu/tua", "te" |
|---|---|---|---|---|
| iPhone user guide (51 pages incl. Health, Screen Time, Focus, iCloud, Family Sharing, Siri, Wallet, Calendar) | Toque 620, Vá 68, Proceda 44, Selecione 40, Abra 20, Clique 16 | 348 | 0 (the 3 hits "toca"/"abre" are third-person present: "quando toca no novo", "quando abre uma aplicação") | 0 / 0 / 0 / 0 ; "Pode" 288, "Podes" 0 |
| Apple Watch + Mac guides (23 pages) | Toque 197, Vá 49, Clique 46, Abra 35, Selecione 19, Proceda 18 | 167 | 0 (the hits are the same third-person present, and a few "Clica" false matches in link text) | 0 / 0 / 0 / 0 ; "Pode" 95 |
| Support articles (15: 118428, 118223, 102420, 108906, 105055, 108756, 108790, 102674, 108350, 111781, 108971, 102651, 108922, 102638, 105020) | Toque 219, Clique 76, Selecione 54, Abra 42 | 158 | 0 | 0 / 0 / 0 / 0 ; "Pode" 117 |
| apple.com/pt marketing (iPhone, App Store, iCloud, Apple Fitness+, Apple Intelligence) | Descubra / Obtenha / Veja / Experimente / Saiba / Compre / Escolha / Use: 30, 10, 12, 86, 40 per page | 36 / 28 / 33 / 34 / 32 | 0 | 0 |

Examples, all Apple Portugal:
- "Vá à aplicação Definições no iPhone. Toque em “Tempo de ecrã” e, depois, toque em “Média diária”." (iPhone guide, Screen Time page)
- "Em Definições, toque no seu nome. Toque em Assinaturas. Toque na assinatura. Toque em Cancelar assinatura." (article 118428)
- "Inicie sessão em reportaproblem.apple.com. Toque ou clique em Gostaria e, em seguida, selecione Pedir um reembolso." (article 118223)
- "Pode cancelar uma assinatura da Apple ou uma assinatura comprada com uma app da App Store na web ou no dispositivo." (article 118428)
- "Certifique-se de que carrega o Apple Watch até, pelo menos, 30% antes de dormir" (article 108906); "Siga as instruções no ecrã" (iPhone guide)
- "Se uma app pedir para seguir a sua atividade" / "Pode conceder ou anular a permissão para que uma app siga a sua atividade a qualquer altura." (article 102420)
- Marketing: "Descubra apps incríveis com uma experiência de pesquisa inovadora." / "Escolhidas para si." (www.apple.com/pt/app-store/)

What this means for the site: this is the **formal "você" register without the pronoun** (imperative in the third person: "Toque", "Abra", "Escolha", "Descubra"; possessive "o seu / a sua"; indirect "lhe", "para si", "a si"). It is neither the informal "tu" ("Abre", "Toca", "o teu"), which only developers write (LiftLog's own pt-PT store text says "Abre o teu iPhone Duo"), nor the explicit "você", which Apple never uses. Mirror Apple: no pronoun, third-person imperatives and "o seu". Closing and consent texts: "Pode ...", "Saiba mais", "Consulte".

## Typography

All measured on the raw HTML of the Portugal pages listed above.

- **Quotes for UI labels**: curly double quotes “ ” (U+201C, U+201D) with **no space inside** in the guides (about 1190 “, 1253 ” on the guide pages; 0 « ». Closing quote sits before the full stop or comma: `”.` 341, `”,` 111, `.”` 1). Straight ASCII `"` are also frequent and often unbalanced (`"Audição”`): 63 on the guide pages, 66 in the 15 articles. No « » on any Portugal Apple page, no ‘ ’. Single-word labels are bare or quoted inconsistently. Marketing pages (apple.com/pt) hardly quote labels (1 curly). Developers' pt-PT store texts use « » (Observa: «Treinar hoje?»); Apple's pages do not.
- **Inner spacing**: no spaces inside “ ”. No spaces before `:`, `;`, `?`, `!` (0 NBSP before ":", 0 space before "?").
- **Menu path separator**: `>` with NBSP before and a plain space after in the iPhone guide (`Definições&nbsp;> Privacidade&nbsp;e segurança > Seguimento`; 20 NBSP-before vs 6 plain); plain spaces in articles (`Aceda a Definições > Acessibilidade`). Steps are usually written as a chain of verbs: "Vá à aplicação Definições no iPhone. Toque em ...". The Watch guide writes "Vá a Treino > Zonas de frequência cardíaca".
- **Decimal comma**: `7,6 polegadas`, `10,5 polegadas`, `127,9 MB`, `4,8` rating, `0,99 €`.
- **Thousands**: four digits with **no separator** (`1000 nits`, `2030`); five or more digits with **NO-BREAK SPACE** (`2 000 000:1` contrast ratio, phone `800 207 758`); "milhares", "425 mil classificações" (NBSP). No period as thousands separator seen on any page. Not "1.000".
- **Units and %**: NBSP between number and unit (`5 GB`, `6 metros`, `25 W`, `1000 nits`, `4 dias`, `3 horas` mostly NBSP; the guide has a few plain spaces too). **Percent with no space**: `30%`, `100%`, `200%` (576 digit+% on the guide pages, 0 with a space; marketing 7 vs 0). Degrees: `35 °C` (with space). Not "30 %" as in Spain.
- **Currency**: `9,99 €`, `16,95 €` with **U+00A0** before € (raw bytes `9,99&nbsp;€`; store and apple.com/pt). `0,99 €/mês`, `9,99 € todos os meses`, `59,99 € anualmente`. Euro sign after the number.
- **Dates in running text**: `29 de setembro de 2026`, `18 de janeiro de 2024`: day without leading zero in text, lowercase month, "de" before month and before year. Article footers: `Data de publicação:&nbsp;29 de setembro de 2026`, with a leading zero on single-digit days ("01 de outubro de 2026"). App Store version history: relative `-55 min`, `-6 dias`; this year `2/11`, `24/03`, `4/06` (day without leading zero, month two digits, no year); older `04/06/2025`, `29/10/2017` (dd/mm/yyyy, leading zero on the day). No month names, no periods.
- **Times**: 24-hour clock with a colon: "das 11:00 às 13:00" (Calendar guide example); the same page also has "às 9:00 da manhã" (12-hour phrase with "da manhã"); no "a.m."/"p.m." anywhere. Durations: "Durante 1 hora", "10 minutos", "24 a 48 horas".
- **Ordinals**: `2.ª geração`, `3.ª geração` with a NBSP after the ordinal (`iPhone SE (2.ª&nbsp;geração)`); rank `N.º 9` (store, plain space). Same ª/º as Spain.
- **Dashes**: spaced em dash ` — ` for asides (6 on the guide pages: "fase do sono — sono REM, essencial ou profundo —"), spaced en dash ` – ` also seen (9), and the store title uses ` – App Store`. Not the Spanish spaceless raya.
- **Apostrophe**: none seen (0 straight, 0 curly).
- **Ellipsis**: `…` appears only in the store's og:description truncation.
- **Hyphens**: U+2011 non-breaking hyphen is used inside "Wi‑Fi" (20 hits), "e‑mail", "palavras‑passe", "picture‑in‑picture", "Bem‑estar" and after verbs ("deslocar‑se", "certifique‑se"); plain hyphen in other places. Do not normalise by replacing with U+2010.
- **NBSP in product names**: Apple's HTML puts U+00A0 inside "App Store", "conta Apple", "Apple Watch", "iOS 27", "Face ID", "iPhone SE (2.ª geração)" and in the store `<title>`; support articles also use plain spaces in places. Page `<title>` for the store starts with U+200E (LEFT-TO-RIGHT MARK).
- **Spelling and punctuation conventions**: AO90 forms, accent kept in "cardíaca", "oxigénio"; `e‑mail` with a hyphen; `Wi‑Fi`.

## App Store storefront formats (Portugal)

Fetched 2026-11-19: iTunes lookup `https://itunes.apple.com/lookup?id=<ID>&country=pt&lang=pt_pt` and product page `https://apps.apple.com/pt/app/id<ID>` (page `lang="pt-PT"`, HTTP 200; no 429 hit). Apps: Mockly 6756589122 (paid, Mac only), Things 3 904237743, Observa 6757438990, LiftLog 6760043411. Developer and seller names on these pages are not recorded.

**Price format** (raw bytes): `14,99\xa0€` (Mockly), `9,99\xa0€` (Things 3) in the lookup `formattedPrice`, in `priceFormatted` and in the page span (`<p class="attributes">9,99&nbsp;€</p>`). Comma decimal, **U+00A0 NO-BREAK SPACE**, € after. In-app purchase list rows use the same: `24,99&nbsp;€`, `59,99&nbsp;€`, `1,00&nbsp;€`.

**Free apps**: the product page shows `Grátis · Compras integradas · Desenvolvida para iPad. Não verificada para macOS.` (Observa) and `Grátis · Compras integradas · Desenvolvida para iPhone. Não verificada para macOS.` (LiftLog); bytes `Gr\xe1tis \xb7 Compras integradas \xb7 ...` (plain spaces around U+00B7). The lookup API (`lang=pt_pt`) returns `formattedPrice: "Gratuito"` for the same apps. So **the web page label is "Grátis"; the API label is "Gratuito"**. Do not use "Gratuito" for the store label.

**In-app purchase label**: `Compras integradas` (hero line and the Information row "Compras integradas — Sim"; JSON `"standard":"Compras integradas"`). Not "Compras na app".

**Get button**: `Obter` (raw `"title":"Obter"`, 15 to 36 hits per page, 0 "Descarregar"). Paid apps show the price on the button position instead of "Obter".

**Rating decimal**: comma. Things 3 `4,8` (aria-label "4,8 estrelas"; star bars "5 estrelas, 85%", NBSP before "estrelas"; heading `298 classificações`); a large app `4,6` with `425 mil classificações` (NBSP before "mil"). Apple counts are "classificações" (and "críticas" for written reviews), not "avaliações". Empty: "Esta aplicação não recebeu classificações ou críticas suficientes para apresentar uma descrição geral." (Mockly, Observa, LiftLog).

**Version dates**: "Versão: 3.25.3" with a relative stamp `-55 min`; older entries `-6 dias`; this year `2/11`, `22/10`, `24/03`, `4/06`, `29/10` (dd/mm, no year, day without leading zero, month with two digits); previous years `04/06/2025`, `29/10/2017` (dd/mm/yyyy, leading zero on the day). The lookup API returns ISO dates (`2026-11-19T11:07:35Z`).

**Web badge wording**: the product-page action button is "Obter" and the footer wording is "App Store e Privacidade". Apple's pt-PT badge artwork wording (below) is separate.

**Official localized "Download on the App Store" badge, Portugal** (Apple Marketing Tools, read from the rendered SVG 2026-11-19):
- App Store badge, line 1 `Descarregar na`, line 2 `App Store`. Source: https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/pt-pt (SVG title `Download_on_the_App_Store_Badge_PTPT_RGB_blk_100317`, 119.66 x 40; mirror https://toolbox.marketingtools.apple.com/api/v2/badges/download-on-the-app-store/black/pt-pt).
- Mac App Store badge, line 1 `Descarregar na`, line 2 `Mac App Store`. Source: https://tools.applemediaservices.com/api/badges/download-on-the-mac-app-store/black/pt-pt (SVG title `Download_on_the_Mac_App_Store_Badge_PTPT_RGB_blk_100317`, 156.10 x 40).
- Alt text for a link to it can follow Apple's wording: "Descarregar na App Store". (Brazilian pt-br badge wording is not recorded because pt-br is not a source; do not use it.)

**Page text conventions seen in the title and description**: `App <name> – App Store` and "Descarregue <name>, da autoria de <developer>, na App Store. Veja capturas de ecrã, classificações e críticas, sugestões de utilizadores e…". The store sections read "Classificações e críticas", "Novidades", "Histórico de versões", "Privacidade da app", "Acessibilidade", "Informação", "Partilha com a família", "Sugestões".

## Brazil vs Portugal differences seen

Verified Portugal forms (Apple Portugal pages) against the Brazilian forms a Portuguese-language writer tends to produce. The Brazilian column is a check list from general knowledge, not fetched from Apple Brazil (Brazilian pages were not a source). Anything on the left must not be replaced by the right.

| Apple Portugal (use) | Brazilian form to avoid (check list) |
|---|---|
| Definições (settings app) | Ajustes, Configurações |
| ecrã; ecrã principal; ecrã bloqueado | tela; tela de início; tela de bloqueio |
| Tempo de ecrã | Tempo de Uso (or Tempo de Tela) |
| Partilha com a família | Compartilhamento Familiar |
| modo de concentração (Concentração) | Foco, modo Foco |
| central de controlo; central de notificações | Central de Controle; Central de Notificações (capital) |
| modo de voo | modo Avião |
| Seguimento; "seguir a sua atividade" | Rastreamento; "rastrear" |
| aplicação (guides), app (articles, App Store) | aplicativo |
| ficheiro / Ficheiros | arquivo / Arquivos |
| fotografia / Fotografias | foto / Fotos |
| Câmara | Câmera |
| descarregar; "Obter" (button) | baixar; "Obter" (same word; the verb differs) |
| "Descarregar na App Store" (badge) | "Baixar na App Store" (recollection, not checked) |
| partilhar | compartilhar |
| palavra-passe | senha |
| telemóvel; auscultadores | celular; fones de ouvido |
| rato (Mac mouse) | mouse |
| utilizador; programador (developer) | usuário; desenvolvedor |
| Meteorologia (Weather app) | Clima |
| Lembretes (Reminders) | Lembretes (same word); Lista de Lembretes |
| iniciar sessão / terminar sessão | fazer login / sair |
| guardar | salvar |
| cópia de segurança | backup |
| carregar (to charge) | carregar (same) |
| "o seu / a sua", imperative "Toque" | "você", imperative "Toque" (same form) or "seu"; the verbal forms are the same, the explicit "você" is the difference |
| "a App Store", "o Apple Watch" | "a App Store", "o Apple Watch" (same genders) |
| Acordo Ortográfico forms in pt-PT: "ativar", "ação", "receção", "oxigénio", "frequência cardíaca" | "ativar", "ação", "recepção", "oxigênio" (accent changes: é vs ê) |
| "Estado de espírito"; "Seguimento do ciclo"; "Sinais Vitais"; "Atenção Plena"; "Preparação" (Apple Portugal's Health names) | check Brazilian Health names are not copied in (e.g. "Estado de Espírito" vs "Estado de Ânimo" in Spain, "Controle de Ciclo", "Sinais Vitais" shared) |
| "Assinatura" (subscription) | "Assinatura" (same word; not a Brazilianism in Apple's usage) |
| "Compras integradas" | "Compras no App" |
| "Classificações e críticas" | "Avaliações e comentários" |
| "Dados associados a si"; "Dados não recolhidos" | "Dados Vinculados a Você"; "Dados Não Coletados" |
| 9,99 € with NBSP; 30%; 4 digits without separator | R$ 9,99; 30%; "1.000" |

Brazilian wording seen on Portugal product pages is developer text, not Apple's, and is not a source: the Mockly pt-PT listing is written in Brazilian Portuguese ("Capturas de Tela", "arquivos", "aparelhos", "Ajustes", "você", "R$ 12,99" in an old release note), while LiftLog's listing is informal pt-PT with "tu" ("Abre o teu iPhone Duo"). Neither matches Apple's own register.
