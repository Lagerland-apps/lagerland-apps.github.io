# European Portuguese glossary per app (pt-PT, Portugal)

Part of the language sheet `_i18n/pt.md`. Extracted 2026-11-19 from each app's string catalogs (read-only, locale `pt-PT`; every catalog also carries `pt-BR`, ignored) and its Portuguese App Store listing (apps.apple.com/pt and the iTunes lookup API, country=pt). UI strings are verbatim: use them on the site exactly, except where a note flags them as defective (Brazilian vocabulary, missing accents, English left in). Store prices are reference only: the site prints prices from the catalog.

**Mockly** has no European Portuguese interface (pt-BR only): its page never says it is in Portuguese (Portugal). **GymLogger X** supports European Portuguese (owner, 2026-11-19: Portugal devices get its base `pt.json`), but that text is still largely Brazilian (2737 of 2923 strings equal pt-BR; recounted «você» 24, «salvar» 23, lower than the batch-2 counts below): quote nouns and labels only.



Part of the language sheet for Portuguese (Portugal). Extracted 2026-11-19 from each app's string catalogs (read-only, locale `pt-PT`) and its Portuguese App Store listing (apps.apple.com/pt and the iTunes lookup API, country=pt). Portuguese UI strings are verbatim from the catalogs: use them exactly on the site, except where a note says the app string is defective (Brazilian vocabulary, English left in, inconsistent). Store prices here are reference only: the site prints prices from the catalog / master file.

## Portuguese glossary, batch 1: aftershift, allpaid, appmeta, appmeta-pulse, chessful

Method (checked 2026-11-19). Read-only extraction from each app's source catalogs under `~/Downloads/` (xcstrings parsed as JSON with `python3 -I`; AfterShift's legacy `.lproj/*.strings` and `.stringsdict` converted with `plutil`). "total" = translatable keys (`shouldTranslate: false` and blank keys excluded; stale keys are counted, the non-stale figure is given in brackets where it differs); "pt-PT" = keys whose `pt-PT` value exists with state `translated` (or plural/substitution variations, or a translated stringSet). Every catalog carries BOTH `pt-PT` and `pt-BR` values (no bare `pt`), so locale `pt-PT` is used throughout and the `pt-BR` values were used only to measure how much of `pt-PT` is a copy of Brazilian text (see Flags 1). Portuguese values are copied verbatim (apostrophes, quotes, dashes and capitalization as in source). Chessful's `.claude/worktrees/*` catalog copies are build clones and were excluded. App Store data: iTunes lookup API (`country=pt&lang=pt_pt`) plus the raw `serialized-server-data` JSON of `apps.apple.com/pt/app/id<ID>` (Safari UA, `Accept-Language: pt-PT`; the bare URL answers 301, follow redirects; one 429 on AllPaid cleared after a 35 s pause; all five Portuguese pages were read). Prices keep the NBSP before `€` and are reference only. The listing page also prints the seller's personal name and address; deliberately not copied.

Register counts are regexes on pt-PT values and are approximate. Definitions: **tu** = a value with tu/teu/tua/te/ti/contigo or -s verb forms ("tens", "podes", "queres", "estás", "és") or a tu imperative at the start of the value ("Toca", "Adiciona", "Escolhe", "Experimenta"); **formal (você/3rd person)** = "você", "o seu / a sua / os seus / as suas" addressing the user, or a subjunctive imperative at the start ("Toque", "Adicione", "Escolha", "Desbloqueie"); **impersonal infinitive** = value starting with "Adicionar", "Restaurar", "Guardar", "Eliminar" and similar. Chessful's chess-piece "o seu rei / a sua torre" hits were removed from the formal count. An imperative ending in -a can also be a 3rd-person description ("Adiciona ao separador… " = "Adds to the tab…" in AppMeta toggles); those are counted as tu and are why the AppMeta / Pulse tu figures are an upper bound.

### Register verdict (decides the site's formality)

| App (catalog) | values | tu | formal (você / 3rd) | impersonal infinitive | Verdict |
|---|---|---|---|---|---|
| AfterShift (`Localizable.strings`) | 1484 | **261** (214 with tu/teu/tens/podes etc.) | 3 | 93 | **tu**, consistent |
| AfterShift widget | 15 | 5 | 0 | 0 | tu |
| AllPaid (all 4 catalogs) | 681 | 7 | **57** | 45 | **formal** ("Adicione", "a sua primeira conta"), with Brazilian "você" in 6 values |
| AppMeta | 2282 | 14 (13 only tu; mostly 3rd-person "Adiciona…") | **220** | 192 | **formal**; no tu pronouns at all |
| AppMeta Pulse (main + widget) | 1674 | 23 (17 only tu, 3rd-person "Adiciona…") | **183** | 138 | **formal** ("Desbloqueie o AppMeta Pulse", "o seu dispositivo") |
| Chessful `Localizable` | 2146 | **207** | **107** | 73 | **mixed**: coach feedback and paywall restore are tu, onboarding, paywall CTAs and empty states are formal |
| Chessful `Lessons` | 3649 | **1113** | 3 | 7 | **tu** |

Summary: **two apps write tu (AfterShift, Chessful lessons), two write formal você-form without "você" (AppMeta, AppMeta Pulse), AllPaid is formal with a few Brazilian "você" leaks, and Chessful's UI mixes both.** The Spanish sheet found "all tú" and the Spanish site writes tú, so the Portuguese site needs an explicit decision: tu would match AfterShift, Chessful lessons and the AfterShift / Chessful store texts (`O teu dia começa quando o turno acaba.`, `Perdeste o jogo e não sabes que jogada o decidiu.`); AllPaid, AppMeta and Pulse store texts are formal (`O AllPaid lembra-se por si.`, `Edite cada idioma da ficha da sua app…`). Quoting UI strings verbatim into a tu page therefore flips register for AllPaid, AppMeta, Pulse and half of Chessful: quote the noun (term), not the sentence, for those apps. Examples are given per app below.

---

### 1. AfterShift (`aftershift`, source `shiftworkersleep/`, ID 6757163182)

### Portuguese coverage
- Main app, legacy `.lproj` (no xcstrings): `en.lproj/Localizable.strings` 1484 keys, `pt-PT.lproj/Localizable.strings` 1484 keys, 0 missing, 0 extra, 21 values identical to English ("Premium", "REM", product names). → **100 %**. `pt-BR.lproj` is a separate full set (771 of 1484 values identical between the two, normal for short words). `Localizable.stringsdict` present for pt-PT (4 plural keys: `plural.hours` "%d hora/horas", `plural.days` "%d dia/dias", `plural.daysRemaining` "%d dia restante/dias restantes", `plural.naps` "%d sesta/sestas").
- `pt-PT.lproj/AppShortcuts.strings`: 16 Siri/Shortcuts phrases, all in Portuguese (Portugal forms): "Quando é o meu próximo turno no ${applicationName}", "Qual é o meu próximo turno no ${applicationName}", "Próximo turno no ${applicationName}", "Pergunta ao ${applicationName} quando volto a trabalhar", "Registar sono no ${applicationName}", "Regista o meu sono no ${applicationName}", "Aponta as minhas horas de sono no ${applicationName}", "Diz ao ${applicationName} que dormi", "Prontidão para o turno no ${applicationName}", "Verifica a minha prontidão no ${applicationName}", "Como estou para o turno no ${applicationName}", "Pergunta ao ${applicationName} se estou bem para o turno", "Quando devo dormir no ${applicationName}", "Qual é a minha janela de sono no ${applicationName}", "Próxima janela de sono no ${applicationName}", "Pergunta ao ${applicationName} a que horas devo dormir". Contraction "no ${applicationName}" (not "em"): correct for pt-PT.
- Widget `shiftworkersleepWidget/Localizable.xcstrings`: 15 / 15 → 100 % (seven gallery names and descriptions).
- InfoPlist: `pt-PT.lproj/InfoPlist.strings` has 2 keys: `CFBundleDisplayName` ("AfterShift") and `NSHealthShareUsageDescription` ("O AfterShift lê os teus dados de sono do Apple Saúde para calcular a dívida de sono e a recuperação entre turnos."). **English-only:** `NSCalendarsUsageDescription` and `NSCalendarsFullAccessUsageDescription` are build settings with no localization ("AfterShift reads your calendar events…"), so the calendar permission prompt is English on a Portuguese device.
- Paywall (`paywall.*`) translated.
- **Verdict: app is in European Portuguese: yes** (clean pt-PT: "ecrã", "telemóvel", "sesta", "partilha", "guardar", "subscrição", "detetada"; no "você", no "tela", no gerund "estar fazendo"; one English permission prompt).

### Register (AfterShift)
tu: 261 of 1484 (e.g. "Faz uma sesta das %@ às %@.", "Ativa o acesso ao sono nas Definições para importar os teus dados.", "Tenta definir um lembrete para o teu limite de cafeína", "Toca em "Importar" para recuperar um evento.", "Partilha com a tua família — até 5 membros", Siri "Pergunta ao…", "Diz ao…", "Verifica a minha prontidão"). Formal: 3 hits (all false positives: "Consigo fazer sestas" is first person, "o seu horário" refers to a shift). Impersonal infinitive for buttons: "Exportar relatório", "Registar consumo de cafeína", "Adicionar técnica", "Editar turno", "Enviar feedback", "Restaurar compras". Widget: 5 of 15 tu ("O teu estado de prontidão num relance."). The Siri phrases mix tu imperatives and neutral infinitives, both fine.

### Glossary
| English term on site | English UI string (key) | pt-PT UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Today (screen / tab) | Today (`tab.today`) | Hoje | |
| Coach (screen) | Coach (`tab.coach`, `coach.title`) | Guia | not "Coach": the tab is "Guia" |
| Roster (shift calendar) | Roster (`tab.roster`) | Turnos | widget `widget.gallery.roster.name` also "Turnos"; running text uses "escala" (16 values: "Importa a tua escala" `onboarding.calendar.title`, `settings.shiftTypes.hint` "…que a tua escala precisar"); the store text also says "A tua escala, já preenchida" |
| Settings | Settings (`tab.settings`) | Definições | |
| Shift Recovery Score | Shift Recovery Score (`recovery.shiftRecoveryScore`) | Pontuação de recuperação por turnos | |
| Sleep Score | Sleep Score (`sleepScore.title`) | Pontuação de sono | `sleepScore.unlock` = "Desbloquear pontuação de sono" |
| Readiness | Readiness (`readiness.title`; widget `widget.gallery.readiness.name`) | Estado de prontidão | **Flag:** `shiftChange.readiness` "Readiness" = "Nível de recuperação"; `readiness.locked` = "Recuperação bloqueada"; `intent.readiness.title` "Shift Readiness" = "Prontidão para o turno"; `swap.headline.improved` = "A prontidão deve melhorar". The store text also says "Estado de prontidão". Use "Estado de prontidão" |
| On-call | On-call (`sleepScore.onCall`) | De prevenção | `schedule.irregular` = "Irregular/De prevenção"; `coach.onCall.title` = "Modo de recuperação de prevenção"; "prevenção" used in 29 values; the store text says "De prevenção" too (Portugal's word for being on call) |
| Naps | Naps (`naps.title`) / Nap (`nap.label`) | Sestas / Sesta | `today.logNap` "Log Nap" = "Registar sesta"; stringsdict "%d sesta/sestas"; 59 values, consistent, never "soneca" |
| Nap window | Optional nap window (`notification.napWindow.title`) | Janela de sesta opcional | `insight.notification.napWindow.title` = "Janela de sesta" |
| Sleep window | Sleep window (`notification.sleepWindow.title`) | Janela de sono | `intent.sleepWindow.title` = "Próxima janela de sono" |
| Sleep Timing | Sleep Timing (`timing.title`) | Horários de sono | `paywall.free.sleepTiming` = "Horários de sono entre turnos" |
| Sleep debt | Sleep debt trend (`debtTrend.title`); widget Sleep Debt | Tendência de dívida de sono | widget `widget.gallery.sleepDebt.name` = "Dívida de sono" (19 values with "dívida", consistent) |
| Sleep stages Awake / Core / Deep / REM | `stages.awake/core/deep/rem` | Acordado / Leve / Profundo / REM | `stages.sleepStages` = "Fases do sono"; Core → "Leve" is the app's own choice, check against Apple Saúde's Portuguese stage labels before the site relies on it |
| Time in bed | Time in bed (`timing.timeInBed`) | Tempo na cama | |
| Fragmentation | Fragmentation (`continuity.fragmentation`) | Fragmentação | `paywall.premium.fragmentation` = "Análise de fragmentação e continuidade" |
| Caffeine timing | Caffeine timing (`coach.caffeine.title`) | Horário da cafeína | `technique.caffeineTiming.title` also "Horário da cafeína"; **Flag:** `caffeine.header` "Caffeine Timing" = "Consumo de cafeína" (means consumption); `caffeine.trend.excellent` = "Excelente horário de cafeína nas últimas 2 semanas" |
| Caffeine cut-off | Caffeine cutoff (`notification.caffeineCutoff.title`) | Limite de cafeína | consistent ("o teu limite de cafeína") |
| Wind-down reminder | Wind down (`notification.windDown.title`) | Relaxamento | **Flag, three forms:** `insight.notification.windDown.title` "Wind-down time" = "Hora de relaxar"; `playbook.step.windDown.title` = "Abranda — body scan, luzes baixas." (English "body scan" left in); "rotina de relaxamento" in insights |
| Calendar shift import | Import from calendar (`roster.calendarImport`) | Importar do calendário | `onboarding.calendar.title` = "Importa a tua escala" |
| Calendar sync (Premium) | Calendar Sync (`calendar.sectionTitle`) | Sincronização do calendário | `calendar.upgradeAutoSync` = "Upgrade: sincronização automática, vários calendários e horas extra" (English "Upgrade" left in, 4 values: "Faz upgrade…"); `paywall.premium.calendarSync` = "Sincronização automática do calendário e controlo de horas extra" |
| Overtime | Overtime: (`nextShift.overtime`) | Hora extra: | singular here, plural "horas extra" elsewhere; `nextShift.overtime.addOneHour` = "Adicionar 1 hora extra" |
| Add a shift | Add shift (`roster.addShift`, `today.addShift`) | Adicionar turno | "Adicionar" consistently (14 values), no "Agregar"-style leak |
| Shift types | Day / Evening / Night / Off (`shift.day/evening/night/off`) | Dia / Tarde / Noite / Folga | `settings.shiftTypes` = "Tipos de turno" |
| Shift change | Shift change impact (`shiftChange.title`) | Impacto da mudança de turno | `insight.shiftChange.title` = "Mudança de turno"; `overtime.extended` = "Turno alterado de %@ para %@ (+%d min)." ("mudança" vs "alterado") |
| Repeating rotation | Repeating rotation (`roster.rotation`) | Ciclo de turnos recorrente | `rotation.presets` "Common rotations" = "Ciclos comuns". **Flag:** `roster.tapToAdd` = "Toca em + para adicionar um turno" (drops "or set up a repeating rotation") |
| Three-shift (day → evening → night) | Three-shift rotation (`rotation.preset.threeShift`) | Três turnos | |
| 4-on-4-off | 4 on / 4 off (`rotation.preset.fourOnFourOff`) | 4 x 4 | |
| 4-on-3-off | 4 on / 3 off (`rotation.preset.fourOnThreeOff`) | 4 x 3 | |
| 2 days / 2 nights | `rotation.preset.ddnn` | 2 dias / 2 noites | |
| Panama (2-2-3) | `rotation.preset.panama` | Panamá (2-2-3) | |
| Fixed nights / days | `rotation.preset.fixedNights/fixedDays` | Noites fixas / Dias fixos | sub: "Cinco dias, fins de semana de folga" |
| Trends | Trends (`trends.title`) | Tendências | `today.section.trends` "Trends & Insights" = "Tendências e insights" |
| Do this now (playbook) | Do this now (`playbook.cardKicker`) | Faz isto agora | tu imperative; widget `widget.label.doThisNow` same |
| Techniques | Techniques (`library.title`) | Técnicas | |
| Export / PDF report | Export Sleep Report (`settings.exportReport`) | Exportar relatório de sono | "relatório" consistent (8 values), correct pt-PT; `export.title` "RELATÓRIO DE SONO AFTERSHIFT" |
| Live Activity / Lock Screen | Shift countdown on Lock Screen (`liveactivity.settings.title`) | Contagem do turno no ecrã bloqueado | "ecrã" 10 values |
| Widgets: Next Shift, Shift Plan, Rhythm, Sleep Debt, Roster, Readiness, Sleep Graph | `widget.gallery.*.name` | Próximo turno, Plano do turno, Ritmo, Dívida de sono, Turnos, Estado de prontidão, Gráfico de sono | descriptions in tu: "Contagem decrescente em direto até ao teu próximo turno." |
| Apple Health | (Apple Health) | Apple Saúde | 20 values "Apple Saúde" + "Saúde"; never "Apple Health" |
| Family Sharing | Share with your family — up to 5 members (`paywall.premium.familySharing`) | Partilha com a tua família — até 5 membros | |
| Siri / Shortcuts | AppShortcuts phrases | see coverage section | |

### Paid tier names in the pt-PT UI (AfterShift)
- Title: **AfterShift Premium** (`paywall.premiumTitle`); `paywall.continuePremium` "Continuar Premium"; `paywall.tryPremium` "Experimenta o AfterShift Premium"; `paywall.unlockForever` "Desbloquear Premium para sempre". The word "Pro" never appears (0 values). Site term: Premium.
- Periods: Mensal / Anual / Vitalício (`paywall.monthly/yearly/lifetime`); `paywall.month` mês, `paywall.year` ano; `paywall.payOnce` "Paga uma única vez"; `paywall.lifetimeDisclosure` "Compra única. Sem subscrição. Todas as funcionalidades Premium, para sempre." **Flag:** `paywall.bestValue` "Melhor valor" is a calque of "Best value" (AppMeta uses "Melhor relação qualidade-preço").
- Trial: `paywall.startTrial` "Iniciar teste grátis de 7 dias"; `paywall.7dayTrial` "Teste grátis de 7 dias"; `settings.trialActive` "Teste grátis ativo"; `paywall.noChargeToday` "Sem cobrança hoje. Não serás cobrado se cancelares antes do fim do teste." "Teste grátis" is AfterShift's trial word (also "período de teste").
- Restore: `paywall.restorePurchases` "Restaurar compras".

### Portuguese App Store listing (checked 2026-11-19)
- Name: **AfterShift: Sono & Turnos** (English: "AfterShift: Sleep & Shift Work"; keeps the ampersand).
- Subtitle: **Recuperação, sestas e fadiga** (direct translation of "Recovery, naps & fatigue").
- Category: **Saúde e fitness**. Price "Gratuito" with in-app purchases. Languages: 34 (the lookup lists `PT`; the Portuguese page labels it "Português"). Minimum iOS 17.6.
- IAPs (page): `Premium compra única 44,99 €` · `Apoiar o programador 1,00 €` · `Premium anual 29,99 €` · `Premium mensal 3,99 €`. Store IAP names use "Premium" like the app.
- Description (store, tu): "O teu dia começa quando o turno acaba." Uses "escala" ("A tua escala, já preenchida"), "Estado de prontidão", "Apple Saúde", "De prevenção", "Todas as sestas contam", "Reconhece palavras de turno em 13 idiomas".

---

### 2. AllPaid (`allpaid`, source `billreminder/`, ID 6757253009)

### Portuguese coverage
- Main `Localizable.xcstrings`: 494 / 494 → **100 %** (non-stale 464 / 464; 22 values identical to English: "Pro", "Streaming", brand names).
- `InfoPlist.xcstrings`: 3 / 3 → 100 % (`NSFaceIDUsageDescription` "Exigir Face ID ou Touch ID para abrir a app.", an infinitive; the display names are the brand).
- Widget `billreminderWidget/Localizable.xcstrings`: 57 / 58 → 98.3 % (only `%lld` untranslated, format-only). `billreminderWidgetShared/Widget.xcstrings`: 130 / 130 → 100 %.
- **Not localized:** Siri App Shortcut phrases (`Services/AppIntents/BillsDueIntent.swift`: "What bills are due in \(.applicationName)", "Show my bills in \(.applicationName)", "Bills due this week in \(.applicationName)"): no `AppShortcuts.xcstrings` / `.strings` exists, so the spoken phrases are English only. The intent title ("Bills Due This Week" → "Contas esta semana") and description are translated; the phrases are not. Do not promise Portuguese Siri phrases on the page.
- **Verdict: app is in European Portuguese: partial.** The vocabulary is mostly pt-PT ("ecrã", "Definições", "Partilhar conta", "Gerir anexos", "Pesquisar contas", "Lembretes", "Compra única", "Sincronização do iCloud") but 357 of the 494 main-catalog `pt-PT` values are identical to `pt-BR`, and Brazilian forms leak in: "você" ×6 ("Você nunca mais vai esquecer uma conta.", "Vamos lembrar você antes do vencimento.", "Você acompanha %lld contas", "Você pagou 5 contas em dia", "e lembra você na hora certa.", "Acompanhe cada pagamento que você fez."), "Assinatura(s)" for Subscription(s) ×5 ("Assinaturas", "Gerenciar assinatura", "Sem assinatura"), "Gerenciar", "Compartilhar e suporte", "estresse", "recurso Pro", "Moradia", "seu histórico", "sua mente", "na hora certa". The same file has the pt-PT forms ("Gerir subscrição", "Partilhar a app com amigos"): the catalog is half pt-PT, half Brazilian.

### Register (AllPaid)
formal 57 of 681 across all catalogs ("Adicione a sua primeira conta", "AllPaid regista as suas contas", "Veja meses anteriores com Pro.", "Pergunte mais tarde", "Feche o AllPaid completamente e abra novamente", widget "Veja a sua próxima conta no ecrã de bloqueio.", "Escolha quanto tempo à frente…"); tu 7, all 3rd-person descriptions ("Abre definições da app…", "Mostra contas a pagar nos próximos 7 dias", "Termina hoje") and none with a tu pronoun; "Cancele quando quiser", "Mude para Pro", "Experimente o Pro grátis"; plus impersonal infinitives ("Adicionar conta", "Cancelar", "Restaurar compras"). The Brazilian "você" values are also formal-register. Verdict: formal.

### Glossary
| English term on site | English UI string | pt-PT UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Bills | Bills | Contas | "conta(s)" throughout, never "fatura(s)"; `Recurring Bills` = "Contas recorrentes"; ambiguous with "conta" = account (the app uses "a sua conta iCloud") |
| Add a bill | Add Bill | Adicionar conta | |
| Mark paid | Mark as paid / Mark paid | Marcar como pago / Marcar como paga | **Flag:** masculine vs feminine for the same action; `Mark as renewed` = "Marcar como renovado" |
| Paid | Paid | Paga | feminine; `paid` = "pagas" |
| Undo | Undo | Desfazer | distinct from Cancel = "Cancelar" |
| Snooze (notification) | Remind in 2 hours / Remind tomorrow | Lembrar em 2 horas / Lembrar amanhã | no single "Snooze" string |
| Monthly calendar | Monthly Calendar | Calendário mensal | |
| Total due | Total due | Total a vencer | |
| Upcoming | Upcoming / Coming Up / Coming up | Em breve / Próximas contas / Em breve | `Next Bill` = "Próxima conta" |
| Reminders | Reminders | Lembretes | |
| Multiple reminders per bill (Pro) | Multiple reminders per bill | Vários lembretes por conta | "Vários lembretes por contrato é uma funcionalidade Pro." (uses "funcionalidade" here, "Recurso Pro" elsewhere) |
| Due-day reminder | Due-day reminders | Lembretes no dia do vencimento | "Vence hoje", "Vence amanhã" |
| Spending analytics (Pro) | Spending Analytics / Spending overview | Análise de gastos / Resumo de gastos | `Analytics` alone = "Análise" |
| Category breakdown | By category | Por categoria | |
| Monthly trends | Monthly trend | Tendência mensal | |
| Full payment history | Full payment history / Payment History | Histórico completo de pagamentos / Histórico de pagamentos | "Mude para Pro para ver seu histórico completo de pagamentos." drops the article (BR "seu") |
| Unlimited bills | Unlimited bills | Contas ilimitadas | |
| iCloud Sync | iCloud Sync | Sincronização do iCloud | other pt-PT forms in the sheet use "do iCloud" |
| Search / Sort / Notes / Share | Search bills / Sort by / Notes / Share bill | Pesquisar contas / Ordenar por / Notas / Partilhar conta | pt-PT; but `Share & Support` = "Compartilhar e suporte" (BR) |
| Billing cycles | Weekly / Bi-weekly / Quarterly / Semi-annual / Custom | Semanal / Quinzenal / Trimestral / Semestral / Personalizado | "Quinzenal" = roughly every 15 days, same note as Spanish "Quincenal" |
| Categories (examples) | Streaming / Subscriptions / Utilities / Housing / Insurance | Streaming / Assinaturas / Serviços essenciais / Moradia / Seguros | **Flag:** "Assinaturas" and "Moradia" are Brazilian (pt-PT: "Subscrições", "Habitação"); "Serviços essenciais" is acceptable pt-PT for Utilities |
| Contracts | Contract / Contracts / Contract ends | Contrato / Contratos / Fim do contrato | `Contract ending soon` = "Contrato a terminar em breve"; `%@ contract ends in %lld days.` plural = "O contrato de %1$@ termina em %2$lld dia." |
| Auto-pay | Auto-pay | Pagamento automático | |
| Documents attached to the bill | Manage attachments / DataVault | Gerir anexos / DataVault | `DataVault` left as product name |
| App lock (Face ID) | App Lock | Bloqueio da app | `App Locked` = "App bloqueada" ("app" masculine/feminine drift: "da app", "App bloqueada") |
| Family Sharing | Share with up to 5 family members / via Family Sharing | Partilhe com até 5 familiares / via Partilha com Família | the Apple term is "Partilha em Família" in pt-PT iOS; here "Partilha com Família" |
| Widgets: Next Bill, Horizon, Paid Rhythm (+ Recurring Bills, Week Ahead, Month Progress, Monthly Calendar) | widget names | Próxima conta, Horizonte, Ritmo de pagamentos (+ Contas recorrentes, Semana pela frente, Progresso do mês, Calendário mensal) | |
| Free tier | Free plan | Plano gratuito | `Free plan allows up to 3 bills…` = "O plano gratuito permite até 3 contas. Mude para Pro para contas ilimitadas."; `Free: 1` = "Grátis: 1"; "Os utilizadores gratuitos podem anexar 1 documento por conta" |
| Pro | Pro / AllPaid Pro / Upgrade to Pro | Pro / AllPaid Pro / Mudar para Pro | `Unlock AllPaid Pro` = "Desbloquear AllPaid Pro"; `Start Pro` = "Iniciar Pro" |
| Lifetime | Lifetime / Buy Lifetime Access | Vitalício / Comprar acesso vitalício | store IAP says "compra única"; `One-time purchase` = "Compra única" |
| 7-day free trial | Try Pro free for 7 days | Teste Pro grátis por 7 dias | `Start free trial` = "Iniciar teste gratuito"; `Try Pro free for %@` = "Experimente o Pro grátis durante %@" (two different phrasings) |
| Restore Purchases | Restore Purchases | Restaurar compras | |

### Paid tier names in the pt-PT UI (AllPaid)
Pro (`Pro`, `AllPaid Pro`); Mensal / Anual / Vitalício (`Lifetime`); `Upgrade to Pro` = "Mudar para Pro" (another phrase: "Atualize para Pro" in one string); `Unlock` = "Desbloquear", `Unlock AllPaid` = "Desbloquear AllPaid"; trial "Teste Pro grátis por 7 dias" / "Experimente o Pro grátis durante %@"; "Cancele quando quiser" / "Cancele quando quiser. Sem cobrança até o fim do período de teste." (**Flag:** "até o fim" is the Brazilian form, pt-PT "até ao fim"); lifetime disclosure "O pagamento será cobrado no seu ID Apple como compra única. Sem assinatura, sem cobranças recorrentes." (**Flag:** "ID Apple" and "assinatura"); restore "Restaurar compras". Family Sharing: "Partilhe com até 5 familiares".

### Portuguese App Store listing (checked 2026-11-19)
- Name: **AllPaid – Gestão de Contas** (English: "AllPaid – Bill Tracker"; en dash).
- Subtitle: **Pague no prazo, sem stress** (formal imperative; English "Pay on time, stress-free"). Note "stress" here but "estresse" in the app.
- Category: **Utilitários** (the lookup also lists "Gastronomia e bebidas" as a second genre). Price "Gratuito" with in-app purchases. 34 languages. Minimum iOS 17.0; the store text says "AGORA NO IPHONE, IPAD E MAC".
- IAPs: `AllPaid Pro compra única 29,99 €` · `AllPaid Pro anual 14,99 €` · `AllPaid Pro mensal 1,99 €`.
- Description (store, formal): "Nunca mais esqueça uma conta." The store text is clean pt-PT ("telemóvel que tem no bolso", "ecrã grande", "O AllPaid lembra-se por si", "ecrã principal", "Sincronização do iCloud"): the store listing is better Portuguese than the app UI.

---

### 3. AppMeta (`appmeta`, source `metabuilder/`, ID 6758547802, macOS)

### Portuguese coverage
- `metabuilder/Localizable.xcstrings`: 2282 / 2300 translatable keys → **99.2 %** (non-stale 2247 / 2265, also 99.2 %). The 18 keys without `pt-PT` are all format-only or symbol strings (` "%@"`, `(%lld %@)`, `%`, `%@ — %@`, `%@ — %@ (%@)`, `%@ %@ %@`, `%lld %@`, `$` and similar). 69 values identical to English (product names, "Pro", "TestFlight", "Issuer ID", "Key ID").
- No InfoPlist.xcstrings, no widgets, no extensions, no permission prompts; display name "AppMeta" is a brand name.
- **Verdict: app is in European Portuguese: yes**, with a Brazilian layer: 1285 of 2282 `pt-PT` values equal `pt-BR` (56 %), and 35 values leak Brazilian forms ("você" ×7 incl. the pronoun used as UI label "You" = "Você", "Você: —", "você cria-a", "chave que gerou você mesmo"; "está limitando as solicitações", "Quem está ranqueando agora", "Buscar a dificuldade real", "está salvo" ×2, "Ótimo" ×2, "E-mail" ×3 where pt-PT writes "email" or "e-mail" both ok, "recurso"). Mostly pt-PT otherwise ("ecrã", "ficheiro", "Capturas de ecrã", "subscrições", "utilizador", "Gerir").

### Register (AppMeta)
formal 220 of 2282, no tu pronoun anywhere (0 of "tu/teu/tua/tens/podes"). Formal examples: "Adicione um concorrente através do URL da App Store ou do Apple App ID…", "Adicione a chave pública no Apple Ads", "Peça à IA para sugerir até 10 novas palavras-chave…", "Utilizar a sua própria chave de API", "Pague uma vez, é seu para sempre", "Ligue o Apple Ads nas Definições para ter um número". Values that look like tu ("Adiciona ao separador Palavras-chave os números de popularidade…", "Verifica se a Apple sugere cada frase…", "Adiciona dados reais de concorrência…") are 3rd-person descriptions of a toggle. Impersonal infinitives for buttons: "Adicionar", "Adicionar todas", "Enviar", "Atualizar". Verdict: formal / impersonal.

### Glossary
| English term on site | English UI string | pt-PT UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Locales | Locales | Idiomas | **Flag:** lowercase `locale` = "região", `locales` = "regiões"; running text also uses "localização" (45 values: "%1$lld localização(ões) com erros de validação") and "localidade" (31 values: "%1$lld localidade%2$@"); "idioma" 83 values is the dominant form |
| Metadata | Metadata | Metadados | lowercase "metadados" |
| Name / Subtitle / Promotional Text / Description / What's New | same | Nome / Subtítulo / Texto promocional / Descrição / Novidades | |
| Keywords | Keywords | Palavras-chave | 70 values, consistent (hyphenated) |
| Keyword Optimizer | Keyword Optimizer | Otimizador de palavras-chave | `Keyword Opportunities` = "Oportunidades de palavras-chave"; `Keyword Efficiency Dashboard` = "Painel de eficiência de palavras-chave" |
| Difficulty / Demand / Opportunity | same | Dificuldade / Procura / Oportunidade | |
| Search coverage | App Store Search Coverage / Coverage | Cobertura de pesquisa na App Store / Cobertura | |
| Preview changes (diff) | Preview Changes | Pré-visualizar alterações | `Diff previews and sync simulation` = "Pré-visualização de diferenças e simulação de sincronização"; the store text keeps "diff" ("Nada é enviado antes de ver o diff") |
| Push | Push / Push All / Push Changes | Enviar / Enviar tudo / Enviar alterações | **Flag:** `Submit` = "Enviar" too, so Push and Submit collide (34 values with "Enviar", 0 "Publicar"); the store text: "PRIMEIRO O DIFF, DEPOIS O ENVIO" |
| Refresh | Refresh | Atualizar | |
| Bulk actions | Bulk Actions / Bulk Copy | Ações em lote / Cópia em massa | "em lote" vs "em massa" in the same pair |
| AI translation | AI Translation / Translate | Tradução por IA / Traduzir | |
| AI provider | Provider / Default Provider | Fornecedor / Fornecedor predefinido | `Use Your Own API Key` = "Utilizar a sua própria chave de API" |
| AI credits | AI Credits / Buy Credits / Starter Pack / Pro Pack | Créditos de IA / Comprar créditos / Pacote Starter / Pacote Pro | |
| Apple Intelligence | Apple Intelligence | Apple Intelligence | |
| Submit for review | Submit for Review | Enviar para revisão | |
| App Review Information | App Review Information | Informações de Revisão da Aplicação | "Informações de Análise da App" in another value; capital R/A |
| Phased release / Age rating / Availability / Pricing | same | Lançamento em fases / Classificação etária / Disponibilidade / Preços | `Release to All` = "Lançar para todos" |
| Reviews / Ratings | Reviews / Ratings / Rating | Avaliações / Avaliações / Classificação | **Flag:** Reviews and Ratings both "Avaliações" (36 values), Rating = "Classificação"; the store listing and Pulse say "Críticas" for reviews |
| TestFlight / What to Test | same | TestFlight / O que testar | |
| In-App Purchases / Subscription Groups | same | Compras integradas / Grupos de subscrições | "Compras integradas" is the Apple pt-PT term |
| Game Center Achievements / Leaderboards | Achievements / Leaderboards | Conquistas / Tabelas de classificação | |
| Sales and Analytics | Sales / Analytics | Vendas / Análises | `Click Sales and Trends` = "Clique em Sales and Trends" (English product label left); "Análises" for Analytics |
| Diagnostics | Diagnostics | Diagnósticos | **Flag:** `Signatures` = "Assinaturas", `%lld new diagnostic signature` = "nova assinatura de diagnóstico": "assinatura" is correct for signature but sits beside "subscrição" (50 values) for Subscription, so keep the two apart |
| Screenshots | Screenshots | Capturas de ecrã | |
| Issuer ID / Key ID | same | Issuer ID / Key ID | both left English (Pulse translates: "ID do emissor", "ID da chave") |
| Territories | Territories | Territórios | |
| Dashboard | Dashboard | Painel | |
| Demo mode | Demo Mode / Demo (Free) | Modo de demonstração / Demonstração (grátis) | |
| Pro | Pro / AppMeta Pro / Unlock Pro | Pro / AppMeta Pro / Desbloquear Pro | `Unlock AppMeta Pro` = "Desbloquear o AppMeta Pro" (article), `Upgrade to Pro` = "Mudar para Pro" |
| Yearly / Lifetime | Yearly / Lifetime | Anual / Vitalício | `Auto-renews yearly` = "Renova automaticamente todos os anos"; `Most popular` = "Mais popular"; `Best Value` = "Melhor relação qualidade-preço"; `Pay once, own forever` = "Pague uma vez, é seu para sempre" |
| Restore Purchases | Restore Purchases | Restaurar compras | `Manage Subscription` = "Gerir subscrição" |
| Add | Add | Adicionar | 0 "Agregar" |
| App / application | (app) | aplicação / app | **Flag:** "aplicação" 116 values vs "app" 157 values mixed |

### Paid tier names in the pt-PT UI (AppMeta)
**AppMeta Pro** (`Pro`, `AppMeta Pro`); periods "Anual" and "Vitalício"; no monthly plan; `Free Trial` = "Período de teste gratuito" (an analytics label, no trial in the app); `Demo (Free)` = "Demonstração (grátis)". Paywall verbs: "Desbloquear o AppMeta Pro", "Mudar para Pro".

### Portuguese App Store listing (checked 2026-11-19)
- Name: **AppMeta for App Store Connect** (identical to English, not translated).
- Subtitle: **ASO, metadados e críticas** (English "Metadata & ASO Tools").
- Category: **Utilitários**. Mac only (`kind` = `mac-software`, minimum macOS 14.0). 11 languages (AR, EN, FR, DE, IT, JA, KO, PT, RU, ES, TR).
- IAPs: `AppMeta Yearly 19,99 €` · `AppMeta Compra única 34,99 €` (**flag:** "Yearly" display name not localized in the Portuguese store; "Compra única" has a capital C).
- Description (store, formal): "Edite cada idioma da ficha da sua app na App Store no Mac e veja cada alteração ao lado do que está publicado." Store text uses "ficha", "idioma", "críticas", "envio", "diff"; the in-app vocabulary says "Avaliações", "Enviar", "Aplicação".

---

### 4. AppMeta Pulse (`appmeta-pulse`, source `metabuilder_phone/`, ID 6758788164)

### Portuguese coverage
- Main `metabuilder_phone/Localizable.xcstrings`: 1418 / 1418 → **100 %** (non-stale 1415 / 1415; 47 values identical to English).
- `AppShortcuts.xcstrings` (Siri phrases): 3 / 3 keys carry a translated `pt-PT` stringSet: "Abrir ${applicationName} | Mostrar a receita de hoje em ${applicationName} | Vendas de hoje em ${applicationName}"; "Mostrar o Analytics em ${applicationName} | Conversão da App Store em ${applicationName}"; "Mostrar assinantes em ${applicationName} | Assinaturas ativas em ${applicationName}". Siri phrases ARE in Portuguese, but the third set is Brazilian ("assinantes", "assinaturas") where the main catalog says "subscritores" and "subscrições"; and the phrases use "em ${applicationName}" where the pt-BR set uses "no ${applicationName}" (pt-PT would also use "no").
- Widget `AppMetaPulseWidget/Localizable.xcstrings`: 256 / 256 → **100 %**.
- No InfoPlist.xcstrings; display names "AppMeta Pulse" / "AppMeta Pulse Widget" are brand names; no permission prompts.
- **Verdict: app is in European Portuguese: yes** (clean pt-PT in the UI: "ecrã", "Descarregamentos", "Terminar sessão", "secretária" for desktop, "subscrições", "Definições", "Livro-razão"). 651 of 1418 values equal `pt-BR` (46 %, mostly short words). Leaks are few: the 3 Siri phrases, "Falha ao assinar o JWT" / "chave de assinatura" (correct sense), `Lifetime` = "Vitalícia" (feminine), "Experimentar grátis".

### Register (AppMeta Pulse)
formal 183 of 1674 (main + widget): "Desbloqueie o AppMeta Pulse", "Pergunte ao seu assistente de IA", "Escolha um período mais longo para ver a tendência.", "Ligue a sua conta da App Store Connect…", "Fixe as principais métricas da App Store na secretária…", "Mostre métricas da App Store no seu ecrã principal", "o seu dispositivo", "Sincronize o seu arquivo", widget "Desbloqueie o AppMeta Pulse para ver…". tu 23 (17 only tu): all 3rd-person toggle descriptions ("Adiciona de hora a hora os relatórios financeiros…", "Obtém em cada atualização…", "Mantém o se…") plus one-word "Ativa". No tu pronoun. Impersonal infinitives for buttons ("Adicionar conta", "Sincronizar agora", "Desbloquear métricas"). Verdict: formal, same as AppMeta.

### Glossary
| English term on site | English UI string | pt-PT UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Dashboard | Dashboard | Painel | `7-Day Dashboard` = "Painel de 7 dias"; `Start` = "Início" is the date-range picker label, not a tab |
| Apps | Apps | Apps | `By app` = "Por app" |
| Analytics | Analytics | Analytics | left English (AppMeta says "Análises"; AllPaid "Análise") |
| Reviews | Reviews | Críticas | `Reply` = "Resposta"; `Reply to this review` = "Responder a esta crítica"; `AI draft per review` = "Rascunho de IA por crítica"; AppMeta says "Avaliações" |
| Settings | Settings | Definições | |
| Proceeds | Proceeds | Rendimentos | distinct from Revenue = "Receita" (unlike the Spanish app); widget short form "RENDIM."; `Net` = "Saldo" |
| Sales | Sales | Vendas | |
| Units | Units | Unidades | widget "UNID." |
| Revenue | Revenue | Receita | the store subtitle says "Receitas" |
| MRR | MRR | MRR | |
| Active subscriptions | Active Subscriptions / Active Subs | Subscrições ativas / Subscr. ativas | `Subscription Status` = "Estado das subscrições"; `Subscriptions` = "Subscrições" |
| Trials | Trials / Active Trials | Experim. / Experim. ativos | abbreviation; long form "Períodos experimentais" (widget: "Períodos experimentais, subscritores ativos e MRR"); `Billed yearly · Free trial included` = "Faturação anual · Período experimental gratuito incluído" |
| Trial-to-paid conversion | Trial → Paid / Conversion | Exper. → pago / Conversão | |
| Churn | Monthly Churn / Churn /mo | Churn mensal / Churn/mês | English "Churn" left in |
| Cancellations | Cancels / Cancelled | Canceladas / Canceladas | **Flag:** `Cancels` and `Cancelled` collide |
| New subscriptions | New Subs / New Subscriptions | Novas subscr. / Novas subscrições | widget "NOVAS" |
| Downloads / Impressions / Product page views | Downloads / Impressions / Product Page Views | Descarregamentos / Impressões / Visualizações da página | pt-PT "descarregamentos" |
| Top territories | Top Territories | Principais territórios | |
| Trend comparison | Compare / Previous period / Last year / Custom Range | Comparar / Período anterior / Ano passado / Período personalizado | |
| Goals | Goals / Monthly Goal | Objetivos / Objetivo mensal | |
| iCloud sync | iCloud Sync | Sincronização do iCloud | |
| AI review reply drafts | Draft suggestions / AI draft per review | Sugestões de rascunho / Rascunho de IA por crítica | |
| Reply templates | Templates | Modelos | |
| Display currency | Convert to your preferred currency | Converter para a moeda preferida | `Currency` = "Moeda" |
| Funnel | Funnel | Funil | |
| Demo mode | Try with sample data / Demo Mode | Experimentar com dados de exemplo / Modo de demonstração | same as AppMeta |
| Widgets | Home Screen widgets | Widgets do ecrã principal | `Proceeds (Lock Screen)` = "Rendimentos (Ecrã bloqueado)"; "Widgets na secretária e um painel na barra de menus"; new widgets: "Ritmo, Livro-razão, Forma e O que mudou" |
| AI assistant (MCP) | Ask your AI assistant | Pergunte ao seu assistente de IA | |
| Year over year | Year-over-year | Comparação ano a ano | |
| Paywall bullets | Full access to revenue & subscription metrics / All future updates included | Acesso completo às métricas de receita e subscrições / Todas as atualizações futuras incluídas | |
| Pro (site plan name) | no UI string | n/a | the app never says "Pro"; gating is "Desbloqueie o AppMeta Pulse" |
| Monthly / Yearly / Lifetime | Monthly / Yearly / Lifetime | Mensal / Anual / Vitalícia | `One-time purchase · Use forever` = "Compra única · Utilize para sempre"; `Best Value` = "Melhor valor"; `Billed monthly` = "Faturação mensal" |
| Free trial | Start Free Trial | Experimentar grátis | |
| Restore Purchases | Restore Purchase / Restore Purchases | Restaurar compra / Restaurar compras | **Flag:** paywall singular vs Definições plural |
| Issuer ID / Key ID | same | ID do emissor / ID da chave | translated here, left English in AppMeta |
| Sign out | Sign Out | Terminar sessão | pt-PT |

### Paid tier names in the pt-PT UI (Pulse)
No tier name: the whole app is gated. Strings: "Desbloqueie o AppMeta Pulse", "Desbloquear acesso vitalício" (`Unlock Lifetime Access`), `Subscribe` = "Subscrever"; periods Mensal / Anual / Vitalícia; trial "Experimentar grátis"; restore "Restaurar compra" (paywall) and "Restaurar compras" (settings). The store IAP names use "Acesso vitalício / anual / mensal".

### Portuguese App Store listing (checked 2026-11-19)
- Name: **AppMeta Pulse: Vendas de apps** (English "AppMeta Pulse: App Sales & MRR").
- Subtitle: **Receitas e críticas com IA** (English "Revenue & AI Review Replies").
- Category: **Empresas** (English: Business). Price "Gratuito" with in-app purchases. Minimum iOS 17.0; the description says "agora também no Mac". 15 languages.
- IAPs: `AppMeta Pulse Acesso vitalício 14,99 €` · `AppMeta Pulse Acesso anual 6,99 €` · `AppMeta Pulse Acesso mensal 0,99 €`.
- Description (store, formal): "As suas vendas na App Store, o MRR e as críticas no iPhone, e agora também no Mac." Uses "críticas", "Receitas", "servidor MCP", "Apple Intelligence".

---

### 5. Chessful (`chessful`, source `Chessful/`, ID 6761336870)

### Portuguese coverage
- `Localizable.xcstrings`: 2146 / 2146 → **100 %** (non-stale 2113 / 2113; 73 values identical to English: "Stockfish", "Expert", notation).
- `Lessons.xcstrings`: 3649 / 3649 → 100 % (15 identical).
- `InfoPlist.xcstrings`: 2 / 2 → 100 % (`CFBundleDisplayName` / `CFBundleName` "Chessful", no permission prompts).
- No widget, watch, App Intents or AppShortcuts catalogs.
- **Verdict: app is in European Portuguese: yes.** Chess vocabulary is genuine pt-PT ("lance" 362, "peça", "tabuleiro", "dama", "roque", "cravada", "garfo", "afogamento", "xeque-mate", "fila / coluna", "ecrã", "ficheiro PGN", "Definições", "Partilha"); only 27 % of the Lessons `pt-PT` values equal `pt-BR`, which is the largest real divergence in this batch (Localizable 58 %). Few Brazilian leaks: "Todos os recursos desbloqueados", "salvar/salvo" (~6), "Ótimo", "até o fim", "legal" in "legal moves" (correct sense), "Rating" kept English.

### Register (Chessful)
- `Lessons`: tu 1113 of 3649 ("Quando estás à frente…", "Pergunta sempre: o que joga o meu adversário?", "Diz sempre primeiro a coluna, depois a fila.", "Ativa a tua torre", "Dá-lhe um nome antes de jogares"); formal 3.
- `Localizable`: tu 207 ("Luta pela atividade das peças.", "%@ é a tua principal área para trabalhar.", "Podes reclamar o empate.", "Já és subscritor? Restaurar compras", "Já usaste os puzzles gratuitos de hoje.", "Faz o roque cedo", "Analisa 100 partidas") vs formal 107 ("Analise a sua primeira partida", "Desbloqueie todo o seu potencial", "Veja as suas fraquezas diminuírem", "Treine as suas fraquezas", "Escolha a sua cor", "Cancele quando quiser", "Toque em Analisar para avaliar os seus lances com o Stockfish.", "Partilhe com a sua família", "Inicie sessão para competir nas tabelas de classificação", "Conclua 10 sessões"). The paywall mixes both in adjacent strings ("Desbloqueie todo o seu potencial", "Cancele quando quiser" vs "Já és subscritor? Restaurar compras"). Verdict: tu in lessons and coach feedback, formal in UI chrome and paywall. A site written in tu matches lessons; quote UI strings as nouns.

### Glossary
| English term on site | English UI string | pt-PT UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Dashboard (tab) | Dashboard | Painel | `Home`/first tab string "Início" also exists (1 value) |
| Play (tab) | Play | Jogar | |
| Analysis (tab) | Analysis | Análise | |
| Training (tab) | Training | Treino | `Today's Training` = "Treino de hoje" |
| Learn (tab) | Learn | Aprender | |
| Progress | Progress | Progresso | |
| Game review | Game Review | Revisão | `Review Game` = "Rever jogo"; `Analyze Game` = "Analisar jogo"; `Analyze All` = "Analisar tudo" |
| Accuracy | Accuracy | Precisão | |
| Key moments | Key Moments | Momentos-chave | |
| Blunder / Mistake / Inaccuracy | same | Erro grave / Erro / Imprecisão | clean three-level scale; `Brilliant` = "Brilhante"; `Best move` = "Melhor lance"; `Great move` = "Excelente lance"; `Good move` = "Bom lance" |
| Better move | See the better move / Best move | Melhor lance | "lance" 362 values vs "jogada" 9, "movimento" 0: consistent pt-PT |
| Train your weaknesses | Train Your Weaknesses | Treine as suas fraquezas | formal; `Weaknesses` = "Fraquezas" (18 values "fraquezas / pontos fracos") |
| Skills (5 dimensions) | Skills | Competências | |
| Tactics / Defense / Positional / Openings / Endgames | same | Tática / Defesa / Posicional / Aberturas / Finais | |
| Opening repertoire | Opening Repertoire | Repertório de aberturas | |
| 40 AI opponents | 40 unique opponents | 40 oponentes únicos | levels Beginner / Intermediate / Advanced / Master = Iniciante / Intermédio / Avançado / Mestre; "adversário" 129 values in text ("oponente" 2) |
| Import games | Import Games | Importar partidas | **Flag:** "partida" 142 values vs "jogo" 62 for game ("Analisar jogo", "Rever jogo", "Novo jogo", `New Game` = "Novo jogo", but "Importar partidas") |
| Weekly comparison / Weakness trends | same | (see catalog) | |
| Rating / Elo | Rating | Rating | **Flag:** "rating" 22 values left English; `%lld ELO` all caps (3 values) while the store text says "Elo"; `Rating` also "Classificação" in AppMeta |
| Achievements | Achievements | Conquistas | `33 conquistas em cinco categorias.` in text |
| Leaderboards | (leaderboards) | tabelas de classificação | |
| 3D board | 3D Board / Board Style | Tabuleiro 3D / Estilo do tabuleiro | `Classic 2D` = "Clássico 2D" |
| Puzzles | puzzle(s) | Puzzles | 42 values "puzzles", "problemas" only 2 (clean, unlike the Spanish app); `15 000 puzzles em 53 temas` in the store text |
| Back-rank | Back-Rank Weakness / Missed Back-Rank Mate | Mate do corredor perdido | **Flag, three forms:** "mate na fila de fundo" 75 values, "última fila" 11, "corredor" 16 (the store text says "Mate do corredor perdido"); pick "mate do corredor" (store, key) or "mate na fila de fundo" (lessons) |
| Fork | A fork | Garfo | "Um garfo é quando uma peça ataca duas peças inimigas" (66 values, never "forquilha"); `Skewer` = "Skewer (espeto)" (English kept in parentheses), "espeto" 10 |
| Pin | A pin | Cravada | "cravada" 66 values |
| Hanging piece | Hung piece | Peça pendurada | |
| Free | Free Plan | Plano gratuito | |
| Pro (site) | Chessful Premium / Upgrade to Premium | app: Premium ("Chessful Premium", "Atualizar para Premium"); store: **Pro** ("Chessful Pro anual") | owner decision 2026-11-08: the site says **Pro**; the app UI still says Premium (8 values; "Forçar Pro (debug)" is a debug string) until the app fix (Kanban) |
| Monthly / Yearly / Lifetime | same | Mensal / Anual / Vitalício | `Purchase Lifetime` = "Comprar vitalício" |
| Free trial | Start Free Trial | Teste grátis | `%@ free trial` = "%@ de teste grátis"; `Subscribe Now` = "Subscrever agora"; stale 3-day strings ("Teste grátis de 3 dias, depois renova automaticamente", "$3,33/mês · 3 dias grátis") remain in the catalog but are unused; the trial is 1 week (master), so the site uses the {TRIAL} token |
| Restore Purchases | Restore Purchases | Restaurar compras | `Already subscribed? Restore Purchases` = "Já és subscritor? Restaurar compras" |
| Hint / Resign / New game | Hint / Resign / New Game | Dica / Desistir / Novo jogo | |
| Stockfish | Stockfish | Stockfish | "Analisar com o Stockfish" (article "o"), "A analisar com o Stockfish…" (pt-PT "a" + infinitive progressive, not the Brazilian gerund) |
| Apple ID | Apple ID | ID Apple / Apple ID | `There are no previous purchases to restore on this Apple ID.` = "Não há compras anteriores para restaurar neste ID Apple." and "neste Apple ID" in another; mixed |

### Paid tier names in the pt-PT UI (Chessful)
App: **Premium** ("Chessful Premium", "Atualizar para Premium", "Premium. Abre o ecrã de subscrição."); periods Mensal / Anual / Vitalício; "Teste grátis" (trial length via StoreKit at runtime). Store IAP names: **Chessful Pro mensal / anual / compra única** plus tips "Oferecer um café" / "Apoiante" / "Grande apoio". Owner decision 2026-11-08: the paid tier is **Pro** on the site.

### Portuguese App Store listing (checked 2026-11-19)
- Name: **Chessful: Treinar & Analisar** (English "Chessful: Train & Analyze"; infinitive, so no register issue).
- Subtitle: **Xadrez: táticas e puzzles** (English "Chess tactics, puzzles, coach").
- Category: **Jogos** (lookup genres "Jogos", "Tabuleiro"). Price "Gratuito" with in-app purchases. Minimum iOS 18.0. 33 languages.
- IAPs: `Chessful Pro anual 17,99 €` · `Chessful Pro mensal 2,99 €` · `Grande apoio 9,99 €` · `Apoiante 5,99 €` · `Oferecer um café 1,99 €` · `Chessful Pro compra única 29,99 €`.
- Description (store, tu): "Perdeste o jogo e não sabes que jogada o decidiu. O Chessful sabe." Store text uses "jogo" and "jogada" for game and move where the app says "partida" and "lance", plus «Mate do corredor perdido», "15 000 puzzles em 53 temas", "96 finais", "156 lições interativas", "Percebe o que correu mal".

---

### Cross-app terms (this batch)
| Concept | Values seen | Recommendation |
|---|---|---|
| Restore Purchases | Restaurar compras (all five); Pulse paywall "Restaurar compra" | consistent except Pulse paywall |
| Lifetime | Vitalício (AfterShift, AllPaid, AppMeta, Chessful), Vitalícia (Pulse); store IAPs: "compra única" (AfterShift, AllPaid, AppMeta, Chessful), "Acesso vitalício" (Pulse) | "Vitalício" |
| Monthly / Yearly | Mensal / Anual (all) | consistent |
| Unlock | Desbloquear (all five); "Desbloqueie" formal | consistent verb |
| Free trial | "Teste grátis" (AfterShift, Chessful), "Teste gratuito" (AllPaid), "Período de teste gratuito" (AppMeta label), "Experimentar grátis" (Pulse), "Período experimental" (Pulse long) | no single term: "teste grátis" is the most common; flag |
| Subscription | Subscrição / Subscrever (AfterShift, AppMeta, Pulse, Chessful); AllPaid Brazilian "Assinatura(s)" 5 values; AppMeta Brazilian "assinatura" only for diagnostic signatures (correct) | "subscrição" |
| Reviews | Avaliações (AppMeta), Críticas (Pulse, both store listings for AppMeta/Pulse) | choose "críticas" for Pulse, flag AppMeta |
| Ratings | Classificação (AppMeta, Pulse), Avaliações (AppMeta Ratings), Rating (Chessful) | note |
| Analytics | Análises (AppMeta), Analytics (Pulse), Análise (AllPaid, Chessful tab) | choose per app |
| Dashboard | Painel (AppMeta, Pulse, Chessful) | consistent "Painel" |
| iCloud Sync | Sincronização do iCloud (AllPaid, Pulse) | consistent |
| Free tier | Plano gratuito (AllPaid, Chessful) | consistent |
| Add | Adicionar (all) | consistent, no Brazilian "adicionar" difference |
| Report | relatório (AfterShift) | consistent |
| In-app purchases | Compras integradas (AppMeta), "Compras integradas" in the store page | consistent |
| Settings | Definições (all five) | consistent |
| Screen | ecrã (all five), never "tela" | consistent |
| Phone | telemóvel (AfterShift, AllPaid store); "dispositivo" in Pulse | no "celular" anywhere |
| Apple ID | "ID Apple" (AllPaid, Chessful) / "Apple ID" (Chessful, AfterShift "teu Apple ID") | pick "Apple ID" for the site |
| Family Sharing | Partilha com a tua família (AfterShift), Partilha com Família (AllPaid) | Apple's pt-PT term is "Partilha em Família" |
| Formality | tu (AfterShift, Chessful lessons), formal (AllPaid, AppMeta, Pulse), mixed (Chessful UI) | decide once; see Register verdict |
| App | "app" (AfterShift, AllPaid, Pulse, Chessful), "aplicação" 116 + "app" 157 (AppMeta) | "app" |

### Flags
1. **pt-PT is partly a copy of pt-BR in three apps.** Share of `pt-PT` values identical to `pt-BR` (excluding values identical to English): AllPaid main catalog 357 of 494 (72 %), AppMeta 1285 of 2282 (56 %), AppMeta Pulse 651 of 1418 (46 %), Chessful Localizable 1238 of 2146 (58 %), Chessful Lessons 985 of 3649 (27 %), AfterShift 771 of 1484 (52 %, but its sample shows genuine pt-PT forms). High overlap on short words is normal; the leaks below are the real defects.
2. **AllPaid uses Brazilian forms in `pt-PT`:** "você" ×6, "Assinatura(s)" ×5, "Gerenciar assinatura", "Compartilhar e suporte", "estresse", "Moradia", "recurso Pro", "seu histórico", "sua mente", "na hora certa", "até o fim do período de teste". App-side string fix (not on Kanban here; add to `ISSUES.md` if the owner agrees). Site: never quote those strings; use "subscrição", "partilhar", "habitação", "funcionalidade", "stress" (the store uses "stress").
3. **AppMeta leaks:** "você" ×7 (including the UI label `You` = "Você"), "está limitando", "ranqueando", "Buscar", "salvo" ×2, "Ótimo" ×2; "Locales" = "Idiomas" but lowercase "locale" = "região" and running text has "localização" 45 / "localidade" 31; Push and Submit are both "Enviar"; Reviews and Ratings are both "Avaliações"; "aplicação" 116 vs "app" 157; `Issuer ID` / `Key ID` left English and `Click Sales and Trends` → "Clique em Sales and Trends"; store IAP name "AppMeta Yearly" not localized and "AppMeta Compra única" has a capital C.
4. **AppMeta Pulse leaks:** the Siri phrase set `Show subscribers in ${applicationName}` is Brazilian ("Mostrar assinantes em ${applicationName}", "Assinaturas ativas em ${applicationName}") while the main catalog says "subscritores" / "subscrições"; the paywall says "Restaurar compra" and settings "Restaurar compras"; `Lifetime` = "Vitalícia" (feminine, others masculine "Vitalício"); `Cancels` and `Cancelled` both "Canceladas"; "Churn" and "Analytics" left English; Pulse says "Críticas" for Reviews (store too) but AppMeta says "Avaliações". Proceeds ("Rendimentos") and Revenue ("Receita") are kept distinct here, unlike Spanish.
5. **AfterShift term variants:** readiness ("Estado de prontidão" 8, "Nível de recuperação", "Recuperação bloqueada", "Prontidão para o turno"), caffeine timing ("Horário da cafeína", "Consumo de cafeína"), wind-down ("Relaxamento", "Hora de relaxar", "Abranda — body scan"), roster ("Turnos" vs "escala" ×16), overtime singular "Hora extra:" vs "horas extra", "Upgrade" left English ×4 ("Faz upgrade"), "body scan" left English, "Melhor valor" calque, `roster.tapToAdd` drops "or set up a repeating rotation". The site must pick one term per concept.
6. **Chessful term mixes:** "mate do corredor" (key and store) vs "mate na fila de fundo" (75 lessons) vs "última fila" (11); "partida" 142 vs "jogo" 62 for game; store text says "jogada" and "jogo" where the app says "lance" and "partida"; "rating" left English (22) and "ELO" all caps vs "Elo" in store; "ID Apple" vs "Apple ID"; "Skewer (espeto)" keeps the English term; the app UI still says Premium while the site and store say Pro (Kanban item); stale 3-day trial strings remain in the catalog. Register mixes tu and formal inside the UI (Register verdict).
7. **Missing Portuguese:** AllPaid Siri phrases are English-only (no AppShortcuts localization; `BillsDueIntent.swift`), AfterShift's calendar permission prompts (`NSCalendarsUsageDescription`, `NSCalendarsFullAccessUsageDescription`) are English-only build settings, AppMeta has 18 untranslated format-only keys (no user impact), AllPaid widget has 1 (`%lld`). No missing accents were found in any catalog (a regex for "nao / voce / sao / tambem / configuracao / ecra" returned 0 hits in all five).
8. **Register decides the site:** the Portuguese site must choose between tu (matches AfterShift, Chessful lessons and two store texts) and formal você-form without "você" (matches AllPaid, AppMeta, Pulse and their store texts). Any "você" in the app strings (AllPaid, AppMeta) is Brazilian and must not be quoted. The AllPaid store subtitle "Pague no prazo, sem stress" and the AppMeta/Pulse store texts are formal.
9. **Store listings:** every Portuguese listing is genuine pt-PT and mostly better than the in-app text (AllPaid especially). Names: "AfterShift: Sono & Turnos", "AllPaid – Gestão de Contas", "AppMeta for App Store Connect" (untranslated), "AppMeta Pulse: Vendas de apps", "Chessful: Treinar & Analisar". Prices must still come from `MASTER-prices.csv`; the store prices above are reference only (AllPaid Pro 29,99 / 14,99 / 1,99 €; Chessful Pro 29,99 / 17,99 / 2,99 €; AfterShift Premium 44,99 / 29,99 / 3,99 €; AppMeta 34,99 / 19,99 €; Pulse 14,99 / 6,99 / 0,99 €).

---

## Portuguese (Portugal) glossary, batch 2: earnlock, gymlogger-x, liftlog, mediakit, millrace

Method (checked 2026-11-19, nothing modified outside this file): coverage counted with `python3 -I` over each app's `.xcstrings` catalogs (`strings` → key → `localizations.pt-PT` → `stringUnit` / `variations` / `stringSet`, keys with `shouldTranslate: false` and blank keys excluded; a key counts as translated when every unit is in state `translated`). Worktrees (`.claude/worktrees`), `build*`, DerivedData, `.build` and Pods were ignored. **Locale code used: `pt-PT`.** Every catalog of EarnLock, LiftLog, MediaKit and Millrace carries both `pt-PT` and `pt-BR` columns; `pt-BR` is quoted only where it shows what a Brazilian string would be ("pt-BR would be"). **GymLogger X is the exception: it has no `.xcstrings`, no `pt-PT` UI table, and its `pt.json` is Brazilian Portuguese** (see section 2). Values are copied verbatim from the catalogs (plural variations shown as `one:` / `other:` / `many:`), with each catalog's own punctuation and capitalisation. The Spanish glossary `_i18n/es-glossary.md` (batch 2) was the row checklist (same terms, same order); each app's English page `_apps/<slug>.md` was read to confirm the features. `pt-PT` and `pt-BR` strings are identical for roughly half the keys in every catalog (neutral wording), so identity alone proves nothing: the verdicts below rest on European-only markers (`ecrã`, `ficheiro`, `guardar`, `partilhar`, `Definições`, `registar`, `subscrição`, `estás a fazer`, `tu` forms) against Brazilian-only markers (`tela`, `arquivo` for file, `salvar`, `excluir`, `gerenciar`, `assinatura`, `você`, `está fazendo`). App Store data: iTunes lookup API (`country=pt&lang=pt_pt`) plus the raw `serialized-server-data` JSON of `https://apps.apple.com/pt/app/id<ID>` (Safari User-Agent, `Accept-Language: pt-PT`; the first request of each batch answered 429 or a 301 and was retried with `-L` after a pause until 200). The seller block was not copied. Prices are reference only. The master file `MASTER.md` / `MASTER-prices.csv` was not consulted (out of scope).

Register is counted two ways on every app: (a) strings with an unambiguous tu pronoun or tuteo verb (`teu`, `tua`, `teus`, `tuas`, `ti`, `contigo`, `tens`, `podes`, `queres`, `estás`, `vais`, `consegues`, `Mexe-te`), against strings with `seu`/`sua`/`você`/`quer`; (b) imperative forms at the start of a string or sentence: tu (`Toca`, `Adiciona`, `Escolhe`, `Regista`) against formal 3rd person (`Toque`, `Adicione`, `Escolha`, `Registe`) against the impersonal infinitive used on buttons (`Adicionar`, `Restaurar compras`, `Cancelar`). Hits were reviewed by hand; the numbers are rough.

Headline flags for the whole batch:
- **GymLogger X is NOT in European Portuguese.** Its `pt` table (the one a Portuguese device gets) is Brazilian: `você` (66 strings), `seu`/`sua` without article (107), `salvar` (39), `excluir` (21), `registrar` (25), `assinatura` (11), `gerenciar` (8), `Configurações`, `Treinamento`, gerunds (`está recebendo`, 26 strings). Only 186 of 2,923 main-app strings (6.4%) differ from `pt-BR`, and the Siri-free InfoPlist permission prompts are the only block that is clearly written for Portugal. The pt-PT locale exists in the app only for exercise names (`exerciseOnlyLocales`). Do not quote its UI as Portuguese-Portugal, and do not call the app "in Portuguese (Portugal)" on the site.
- **The other four apps are genuinely European Portuguese**: EarnLock, LiftLog, MediaKit and Millrace use `ecrã`, `ficheiro`, `guardar`, `partilhar`, `registar`, `Definições`, `subscrição`, `estás a bloquear`, `programador`, `rácio`, `cronómetro`, `Anular`. Residual Brazilian leaks are few (listed per app).
- **Register differs by app, so the site cannot use one pronoun for quotes.** EarnLock, LiftLog (UI) and Millrace use **tu**; **MediaKit uses formal 3rd person (`o seu`, `Escolha`, `Converta`, 0 tu pronouns)**; GymLogger X uses Brazilian `você`. EarnLock and LiftLog also keep formal pockets (permission prompts, Watch app, Siri answers, a few settings sentences).
- **LiftLog's tier `Patron` is `Patrocinador` in the app but `Mecenas` in the store** (Fair `Justo`, Good `Bom` and Generous `Generoso` match). One decision needed for the tier names.
- **MediaKit translates the bare word `Free` as `Livre`** (while `Free tier` is `Plano gratuito`), and uses the Brazilian `Assine o Pro`.
- **Trial vocabulary is not shared**: `período grátis` / `Avaliação gratuita` (EarnLock), `Período experimental` (LiftLog), `Teste grátis` (MediaKit, GymLogger X). Decide one site word.
- **`Ajustes` leaks into EarnLock (5 strings) and LiftLog (1)** next to `Definições` (6 each); `Ajustes` is the Brazilian / Spanish iOS word.
- All five store names differ from the English ones; GymLogger X's store name `GymLogger X: Treino Tracker` mixes Portuguese and English and its store IAP `Support the developer` is untranslated.
- Millrace: never write the number of the former name in anything on the site; no string of the Portuguese catalog contains it.

---

### 1. EarnLock (earnlock, source `EarnScreen`, ID 6771099230, has an Apple Watch app)

#### Portuguese coverage

| Catalog | Keys | `pt-PT` present | `pt-PT` translated | % |
|---|---|---|---|---|
| EarnScreen/EarnScreen/Localizable.xcstrings (main app) | 620 | 620 | 620 | 100% |
| EarnScreen/EarnScreen/AppShortcuts.xcstrings | 9 | 9 | 9 | 100% |
| EarnScreen/EarnScreen/InfoPlist.xcstrings | 5 | 3 | 0 (all 3 `needs_review`) | 0% translated, 60% present |
| EarnScreenLiveActivity/Localizable.xcstrings (widgets + Live Activity) | 148 | 148 | 148 | 100% |
| EarnScreenShield/Localizable.xcstrings | 6 | 6 | 6 | 100% |
| EarnScreenWatchComplications/Localizable.xcstrings | 13 | 13 | 13 | 100% |
| watchkitapp Watch App/Localizable.xcstrings | 28 | 28 | 28 | 100% |
| watchkitapp Watch App/InfoPlist.xcstrings | 4 | 2 | 0 (both `needs_review`) | 0% translated, 50% present |
| EarnScreenDeviceActivity, EarnScreenShieldAction | 0 | n/a | n/a | empty catalogs |

All Localizable catalogs together: 815 keys, 815 translated (100%). 415 of the 833 pt-PT values (50%) are identical to `pt-BR` (neutral wording); 13 are identical to English (numbers, `kcal`, `min`, `Premium`, `Mono`, `Instagram`, the brand and the copyright line). Every catalog also carries the `pt-BR` column in parallel.

English-only or unreviewed: the three permission prompts (HealthKit read, HealthKit write, Photo Library add) have Portuguese text but are `needs_review`: `O EarnLock lê os teus passos, minutos ativos e energia ativa da app Saúde para acompanhar o progresso rumo ao objetivo que desbloqueia as tuas apps bloqueadas. Estes dados nunca saem do teu dispositivo.` / `O EarnLock apenas lê os teus dados de atividade — não escreve nada na app Saúde. A Apple exige esta permissão porque a framework HealthKit consegue tecnicamente escrever dados.` / `Permite guardar um cartão de marco na tua fototeca. O EarnLock nunca lê as tuas fotografias.` `CFBundleDisplayName` and `CFBundleName` have no `pt-PT` entry (the name stays "EarnLock"). Siri / App Shortcuts phrases are Portuguese and `translated` (see the glossary).

**Verdict: app is in European Portuguese: yes** (100% of every Localizable catalog, widgets, Live Activity, shield, Watch, complications and Siri phrases; only the permission prompts are `needs_review`; zero Brazilian vocabulary except `Ajustes`).

Register (detail): of 829 strings, **about 187 are tu** (112 have a tu pronoun or tuteo verb: `Mais %@ %@ e vais desbloquear %@.`, `Apps que estás a bloquear`, `Com o que queres ganhar tempo de ecrã?`; the rest are tu imperatives: `Toca para fazer upgrade`, `Escolhe quanto histórico mostrar`, `Adiciona mais com o Premium`, `Mexe-te um pouco para desbloquear esta app`). **About 14 are formal / 3rd person** (+4 mixed): `Permita o acesso à Saúde para continuar.`, `Permita o acesso ao Tempo de ecrã para continuar.`, `Autorize no iPhone e volte aqui.` and `Abra o EarnLock no iPhone` (Watch), `Quer uma meta que se ajusta sozinha? Ative o Adaptativo quando quiser nos Ajustes.`, `Pode voltar a mudar o que regista depois de %@.`, `O seu histórico de metas aparecerá aqui.`, `A sua meta sobe 3%% … se for você a reduzir …`, `Precisa de histórico do Tempo de ecrã`. **About 80 are impersonal infinitives** (buttons: `Adicionar apps`, `Apagar esta reflexão?`, `Comprar Vitalício`, `Repor dados locais`, `Contactar suporte`, `Continuar`). Decision for the site: **tu** (`tu`/`teu`), with infinitive on buttons. No `você` except the one `se for você a reduzir`.

Wording flags:
- Settings is `Definições` (6 strings) but `Ajustes` in 5 (`Ajustes → Tempo de ecrã → EarnLock`, `Atualiza o iOS em Ajustes → Geral → Atualização de Software`, `… nos Ajustes`): Brazilian / Spanish iOS word inside a pt-PT app.
- Goal is `objetivo` (41 strings) and `meta` (11: `Meta diária, últimos 14 dias`, `A sua meta sobe 3%% …`). Pick one for the site (the English page says "goal").
- Family Sharing is `Partilha com a família` and `grupo Família Apple`; Apple's pt-PT name is `Partilha em Família` (MediaKit and GymLogger X use it).
- Lock Screen widget title is `EarnLock — Ecrã Bloqueado` (calque of "locked screen"; Apple pt-PT: `Ecrã de Bloqueio`).
- Apple Health is `Apple Saúde` (12 strings) and `app Saúde` (4): mixed; Apple's app is `Saúde`.
- `fototeca` (permission text) is not Apple's pt-PT word (`Fotografias`, "biblioteca de fotografias").
- English left in: `cooldown` (`saltar o cooldown de 24 h`, while another string says `Saltar tempo de espera`), `Shadow Mode` in one error string (`Não foi possível seguir o Shadow Mode`), `upgrade` (`fazer upgrade`, 4 strings).
- Shadow Mode is `Modo Sombra` (capital S) but the weeks are `semana sombra` (lowercase).
- Siri phrase `Quão perto estou de desbloquear no ${applicationName}`: `Quão` is formal / stiff in speech; the neighbouring phrase says `A que distância estou de desbloquear`.
- Trial wording mixes `Iniciar período grátis`, `7 dias grátis, depois %@/ano` and `Avaliação gratuita de 7 dias; depois, %@/mês` (semicolon and comma for the same offer); `grátis` (4) and `gratuito` (4) are both used.
- Streak is `Sequência` everywhere (consistent; it is also the word in the other apps).

#### Glossary


| English term on site | English UI string (key) | pt-PT UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Free (tier) | `Free forever for one app. Go further with Premium.`; `Free plan locks 1 app. Tap to upgrade.`; `Free locks one app. Premium has no limit.` | `Grátis para sempre numa app. Mais longe com o Premium.`; `O plano gratuito bloqueia 1 app. Toca para fazer upgrade.`; `O gratuito bloqueia uma app. Premium sem limite.` | No standalone "Free" string. The app says `grátis` (4 strings) and `gratuito` (4 strings) interchangeably. pt-BR would be: `De graça para sempre, em um app. Mais longe com o Premium.` ; `O plano gratuito bloqueia 1 app. Toque para fazer upgrade.`. |
| Premium | `Premium` | `Premium` | Not translated. |
| Monthly | `Monthly` | `Mensal` | Combined label `Premium · Mensal`. |
| Yearly | `Yearly` | `Anual` | Combined label `Premium · Anual`. |
| Lifetime | `Lifetime` | `Vitalício` | `Vitalício` (adjective used as the tier name). Combined label `Premium · Vitalício`; the store IAP name is `EarnLock Premium compra única`. |
| Get Premium (button) | `Get Premium` | `Obter Premium` | Impersonal verb, no pronoun. `Get Lifetime` is `Comprar Vitalício`, `Subscribe` is `Subscrever`, `See Premium` is `Ver Premium`. pt-BR would be: `Assinar Premium`. |
| Start free trial (button) | `Start free trial` | `Iniciar período grátis` | `período grátis`; the same offer is `Avaliação gratuita` in another string and `Período experimental` in LiftLog, `Teste grátis` in MediaKit and GymLogger X. pt-BR would be: `Começar período grátis`. |
| 7-day free trial | `7-day free trial, then %@/year`; `7-day free trial, then %@/month` | `7 dias grátis, depois %@/ano`; `Avaliação gratuita de 7 dias; depois, %@/mês` | Two patterns for one offer: `7 dias grátis, depois …/ano` and `Avaliação gratuita de 7 dias; depois, …/mês` (semicolon plus comma). |
| Restore Purchases | `Restore Purchases` | `Restaurar compras` |  |
| Today tab (site says "Home screen") | `Today`; `Go to Today` | `Hoje`; `Ir para Hoje` |  |
| Insights tab | `Insights` | `Análises` | `Análises` (GymLogger X pt-BR says `Insights`). |
| Insights Day / Week / Month | `Day`; `Week`; `Month` | `Dia`; `Semana`; `Mês` |  |
| Settings tab | `Settings` | `Definições` | `Definições` is Apple's pt-PT word (6 strings), but 5 strings say `Ajustes` (`Ajustes → Tempo de ecrã → EarnLock`, `Ativa o Adaptativo … nos Ajustes`), which is the Brazilian / Spanish iOS word. Inconsistent inside the app. |
| Shadow Week | `Run another Shadow Week`; `No Shadow Weeks yet`; `Compared with your previous Shadow Week.` | `Fazer outra semana sombra`; `Ainda não há semanas sombra`; `Em comparação com a tua semana sombra anterior.` | Feature name = `semana sombra` (lowercase) and `Modo Sombra` (capitalised S). One error string keeps English: `Não foi possível seguir o Shadow Mode`. pt-BR would be: `Em comparação com sua semana sombra anterior.`. |
| Enable real blocking | `Enable real blocking` | `Ativar bloqueio real` |  |
| Reflect (button) | `Reflect` | `Refletir` |  |
| Reflection (noun) | `Reflection summary`; `Reflections this month` | `Resumo de reflexões`; `Reflexões deste mês` |  |
| Reflection prompt | `What were you hoping to find?` | `O que esperavas encontrar?` | tu (imperfect `esperavas`, no pronoun). pt-BR would be: `O que você esperava encontrar?`. |
| Reflection answers | `Boredom`; `Anxiety`; `FOMO`; `Habit`; `Other` | `Tédio`; `Ansiedade`; `FOMO`; `Hábito`; `Outro` |  |
| Smart Schedules | `Smart Schedules`; `Smart schedules` | `Horários inteligentes`; `Horários inteligentes` | `Horários inteligentes`; pt-BR would say `Programações` / `Agendas`. |
| Goal tiers Light / Standard / Challenge | `Light`; `Standard`; `Challenge` | `Leve`; `Padrão`; `Desafio` |  |
| Default schedules | `Work hours`; `Evenings`; `Weekends`; `Sleep` | `Horário de trabalho`; `Noites`; `Fins de semana`; `Sono` |  |
| Daily goal | `Daily goal` | `Objetivo diário` | Mixed `objetivo` (41 strings) and `meta` (11 strings: `Meta diária, últimos 14 dias`, `A sua meta sobe 3%% …`). pt-BR would be: `Meta diária`. |
| Adaptive goal | `Adaptive` | `Adaptativo` |  |
| Steps | `Steps` | `Passos` |  |
| Active minutes | `Active minutes` | `Minutos ativos` | `ativos`, not `de atividade`. |
| Active energy / calories | `Active calories` | `Calorias ativas` |  |
| "2,026 steps until unlock" (shield) | `%@ until unlock`; `1,247 steps until unlock` | `%@ até desbloquear`; `1.247 passos até desbloquear` | Shield button `Earn it` is `Conquista` (tu imperative), title `Earn your way in` is `Conquista o acesso`. Thousands separator in the catalog example is a point (`1.247`); pt-PT normally prints a space (`1 247`). |
| Emergency unlock | `Emergency unlock` | `Desbloqueio de emergência` |  |
| Partial unlock | `Partial unlock` | `Desbloqueio parcial` |  |
| Rest day | `Rest day`; `Weekly rest day` | `Dia de descanso`; `Dia de descanso semanal` |  |
| Streak | `Streak`; `Current streak` | `Sequência`; `Sequência atual` | `Sequência` (pt-PT and pt-BR agree). |
| Streak shields | `Streak shields`; `Shield saved your streak` | `Escudos de sequência`; `O escudo salvou a tua sequência` | pt-BR would be: `Escudo salvou sua sequência`. |
| Most-attempted blocked app | `Most attempted blocked app today` | `App bloqueada mais tentada hoje` | pt-BR would be: `App bloqueado mais tentado hoje`. |
| Screen time saved (estimate) | `Screen time saved (estimated)` | `Tempo de ecrã poupado (estimativa)` | `Tempo de ecrã` is the term everywhere (21 strings, 0 `tela`). pt-BR would be: `Tempo de tela economizado (estimado)`. |
| Screen Time (Apple feature) | `Allow Screen Time access` | `Permitir acesso ao Tempo de ecrã` | Apple pt-PT: `Tempo de Ecrã`. The app writes `Tempo de ecrã` (lowercase e) consistently. pt-BR would be: `Permitir acesso ao Tempo de Uso`. |
| Apple Health | `Apple Health` | `Apple Saúde` | `Apple Saúde` (12 strings) and `app Saúde` (4 strings) are mixed; Apple's own app is the `Saúde` app. `Apple Health needed` is `Apple Saúde necessário`. |
| Locked apps | `Locked apps` | `Apps bloqueadas` | `app` is feminine (`uma app bloqueada`, 83 strings with `app`/`apps`, 0 `aplicação`); pt-BR uses masculine `um app`. pt-BR would be: `Apps bloqueados`. |
| Family Sharing | `Family Sharing supported — Premium unlocks for up to five family members in your` | `Compatível com a Partilha com a família — o Premium é desbloqueado para até cinco membros do teu grupo Família Apple.` | Written `Partilha com a família` and `grupo Família Apple`. MediaKit and GymLogger X write `Partilha em Família`, which is Apple's pt-PT feature name: use that on the site and fix the app string. |
| Activity heatmap | `Activity heatmap` | `Mapa de calor de atividade` |  |
| Best week / best month | `Best week`; `BEST MONTH` | `Melhor semana`; `MELHOR MÊS` |  |
| Goal cooldown | `Premium can bypass the 24h cooldown on lowering once per week.` | `O Premium pode saltar o cooldown de 24 h ao reduzir uma vez por semana.` | `cooldown` left in English (`saltar o cooldown de 24 h`); another string says `Saltar tempo de espera`. |
| App icons | `Midnight`; `Ember`; `Mono` | `Meia-noite`; `Brasa`; `Mono` |  |
| Focus session | `Focus session` | `Sessão de foco` | `Sessão de foco` (store name also says `Foco`). |
| Milestone card | `Next milestone`; `A quiet milestone.` | `Próximo marco`; `Um marco discreto.` |  |
| Widgets (Live Activity catalog) | `EarnLock — Contributions` | `EarnLock — Contribuições` | Lock Screen widget is `EarnLock — Ecrã Bloqueado` (calque of "Locked screen"; Apple pt-PT says `Ecrã de Bloqueio`). `Pick apps` is `Escolhe apps` (tu). |
| Apple Watch app | `Apple Watch app` | `App para Apple Watch` | `App para Apple Watch` (no article before Apple Watch). |
| Shield (lock screen, partial block) | `Earn your way in`; `Earn it`; `Move a little to unlock this app`; `%@ until unlock` | `Conquista o acesso`; `Conquista`; `Mexe-te um pouco para desbloquear esta app`; `%@ até desbloquear` | tu imperatives. Shield catalog: 6 keys, all translated. |
| Emergency math gate | `Solve to continue` | `Resolve para continuar` | tu. |
| Siri / App Shortcuts phrases | `What's my goal in ${applicationName}`; `How close am I to unlocking in ${applicationName}`; `How far am I from unlocking in ${applicationName}`; `Lock my apps in ${applicationName}`; `Start a focus session in ${applicationName}` | `Qual é o meu objetivo no ${applicationName}`; `Quão perto estou de desbloquear no ${applicationName}`; `A que distância estou de desbloquear no ${applicationName}`; `Bloquear as minhas apps no ${applicationName}`; `Iniciar uma sessão de foco no ${applicationName}` | 9 phrases, all pt-PT (`apps`, `no ${applicationName}`). `Quão` is stiff in speech (the neighbouring phrase says `A que distância`). |
| Apple Watch app strings | `Open EarnLock on iPhone`; `Authorize on iPhone, then return here.`; `Open the app on iPhone to upgrade.`; `Walk to start tracking`; `Logged. Take a breath.` | `Abra o EarnLock no iPhone`; `Autorize no iPhone e volte aqui.`; `Abre a app no iPhone para fazer upgrade.`; `Caminha para começar o registo`; `Registado. Respira fundo.` | The Watch app mixes formal (`Abra`, `Autorize`) and tu (`Abre`, `Caminha`, `Respira`) in neighbouring strings. |


#### Paid tier names in the pt-PT UI

`Premium` (tier), `Mensal` / `Anual` / `Vitalício`, combined labels `Premium · Mensal`, `Premium · Anual`, `Premium · Vitalício`, `Premium · Partilhado contigo`; buttons `Obter Premium`, `Comprar Vitalício`, `Iniciar período grátis`, `Ver Premium`, `Subscrever`; `Restaurar compras`; `Gerir subscrição`, `Gerir subscrições no ID Apple`; product name `EarnLock Premium`; family line `Tens acesso Premium completo através da compra de um familiar.`

#### Portuguese App Store listing (fetched 2026-11-19)

- Name: **EarnLock: Bloquear Apps e Foco** (English: "EarnLock: App Blocker & Focus"). Differs. Page title: "App EarnLock: Bloquear Apps e Foco – App Store".
- Subtitle: **Domina o teu tempo de ecrã** (English: "Your steps unlock screen time"). Differs; tu.
- IAP as shown (reference): `EarnLock Premium compra única 22,99 €` · `EarnLock Premium anual 9,99 €` · `EarnLock Premium mensal 1,99 €`.
- Languages: "Português e mais 32". Category: **Produtividade**. Requires iOS 17.0 or later; age 9+. `formattedPrice` (lookup API): `Gratuito` (the Spanish store says `Gratis`).

---

### 2. GymLogger X (gymlogger-x, source `GymLogger`, ID 6755734580)

The app does not use `.xcstrings`. Text comes from JSON tables (`GymLogger/GymLogger/Localizations/<code>.json`, `GymLoggerWidget/Localizations/<code>.json`, `GymLoggerWatch Watch App/Localizations/<code>.json`) plus `GymLogger/<code>.lproj/InfoPlist.strings`. **Which file is Portugal?** There are `pt.json` and `pt-BR.json` (and `pt.lproj` / `pt-BR.lproj`); **there is no `pt-PT.json`**. In `LanguageEnums.swift` `pt-PT` is declared as an exercise-only locale (`exerciseOnlyLocales = [.portuguesePT]`: it ships `ExerciseTranslations.pt-PT.json` but no UI table) and `LocalizationManager.baseLanguage(of:)` maps `pt-PT` to base `pt`; `detectDeviceLanguage()` also falls back from `pt-PT` to `pt`. So a device set to Portuguese (Portugal) gets **`pt.json`** for the UI, and `pt.json` is what is quoted below. Comparison with `pt-BR.json`: main app 2,737 of 2,923 values identical (186 differ), widget 98 of 115 identical (17 differ), Watch 97 of 98 identical (1 differs). The 186 differing strings are the only European ones (e.g. `Definições do painel`, `A analisar treinos…`, `Partilha em Família incluída`, `Rácio de carga de treino`, `Ignorar` where pt-BR says `Pular`, `Seguinte` where pt-BR says `Avançar`). There is no App Shortcuts / Siri phrase provider in the project.

#### Portuguese coverage

| Catalog | Keys (en) | `pt` present | % | identical to English | identical to pt-BR |
|---|---|---|---|---|---|
| Localizations/pt.json (main app) | 2923 | 2923 | 100% | 103 | 2737 (93.6%) |
| GymLoggerWidget/Localizations/pt.json | 115 | 115 | 100% | 4 | 98 |
| GymLoggerWatch Watch App/Localizations/pt.json | 98 | 98 | 100% | 8 | 97 |
| GymLogger/pt.lproj/InfoPlist.strings | 4 keys | 4 | yes | display name "GymLogger X" | differs from pt-BR.lproj (pt-PT style) |
| Localizations/ExerciseTranslations.pt-PT.json | exercises, equipment, difficulty, muscles, muscleGroups | present | not selectable as UI language | n/a | mixes tu with Brazilian verbs |

No missing keys, no empty values. **Verdict: app is in European Portuguese: NO.** The key set is 100% filled, but the text a Portuguese user sees is Brazilian Portuguese; only the two permission prompts (`pt.lproj/InfoPlist.strings`) and 186 strings are European. Siri phrases: not applicable.

Register: **no consistent register; mostly Brazilian `você`-style.** Strings with `você`/`seu`/`sua`/`quer`: 241 (`Você tem séries inacabadas. Tem certeza de que deseja finalizar este treino?`, `Mostra sua semana atual e o próximo treino.`, `Pague uma vez, seu para sempre.`); formal-type imperatives `Selecione`, `Toque`, `Crie`, `Registre`, `Continue`, `Veja`, `Desbloqueie`: several hundred (`Selecione um treino para começar`, `Toque em 'Adicionar exercício' para começar.`). Strings with a tu pronoun or tuteo verb: 43 (`Os teus melhores exercícios vão aparecer aqui após algumas sessões com peso.`, `Treinaste este grupo com demasiada frequência`, `Escolhe um CSV em que cada linha é um exercício`), all inside the 186-string European overlay. Impersonal infinitive buttons: about 450 (`Cancelar`, `Pular descanso`, `Finalizar treino?`, `Continuar`). The site cannot quote this UI as tu or as European.

Defects (app-side; do not copy these into the site):
- **Brazilian vocabulary leaks** (count of strings): `treino`/`treinos` is shared with pt-PT; Brazilian-only: `você` 66, `seu`/`sua` without article 107, `salvar`/`salvo` 39, `registrar` 25, `excluir` 21, `pular` 19, `ótimo` 12, `arquivo` for file 12, `assinatura` 11, `desempenho` 14, `compartilhar` 8, `gerenciar` 8, `rastrear` 7, `tela` 4, `usuário` 4, `Configurações` 4, `aplicativo` 2, `celular` 1; progressive gerund `está/estão + -ndo` in 26 strings (`A parte superior está recebendo mais atenção`, `Você está treinando pesado`); `ct` spellings `detectado`, `Detecção`.
- **Program Creator without accents:** 95 of the 195 `creator_*` values longer than 14 characters have no accented character, and 46 strings in the app contain a known unaccented Portuguese word: `Lesoes e Reabilitacao`, `Duracao da Sessao`, `Nivel de Treino`, `Nao-binario`, `Estilo de Periodizacao`, `Ondulatoria (DUP)`, `Todas as repeticoes atingidas — adicione peso na proxima sessao`. The same screens use Brazilian `Seu Perfil` and `Seus programas`.
- `ai_coach` = `Coach IA` (the English site page says there is no language model and no chat bot; check before using it as a feature name).
- Apple Health: 11 strings say English `Apple Health` (`Salvo no Apple Health`), the InfoPlist says `Apple Saúde`.
- Mixed rest-timer words: `Temporizador de descanso` (watch label) and `Timer de descanso por frequência cardíaca` (settings).
- `Push / Pull` English in splits; `The Golden Six` untranslated; `Pro` kept.
- Store IAP `Support the developer` is English on the Portuguese store.

#### Glossary


| English term on site | English UI string (key) | pt-PT UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Free | `free` | `Grátis` |  |
| Pro | `widget_pro`; `gymlogger_pro` | `Pro`; `GymLogger X Pro` |  |
| Pro Monthly | `paywall_plan_monthly` | `Mensal` |  |
| Pro Annual | `paywall_plan_yearly`; `paywall_yearly_pro` | `Anual`; `Pro Anual` | The app says "Yearly" = `Anual`, not "Annual". |
| Lifetime | `paywall_plan_lifetime`; `paywall_lifetime_pro`; `paywall_lifetime_access` | `Vitalício`; `Pro Vitalício`; `ACESSO VITALÍCIO` | `Vitalício`. Store IAP is `GymLogger X Pro compra única`. |
| Restore Purchases | `restore_purchases` | `Restaurar compras` | `restore_purchases` = `Restaurar compras` but `paywall_restore` = `Restaurar Compras` (Title Case). |
| Start free trial | `paywall_start_trial`; `paywall_trial_text` | `Iniciar Teste Grátis`; `1 semana de teste grátis` | Brazilian-neutral. The trial is 1 week. `Teste` vs `período experimental` (LiftLog) vs `Avaliação` (EarnLock). |
| Tabs: Home / Training / Progress / Settings | `home_title`; `training_title`; `progress`; `settings` | `Início`; `Treinamento`; `Progresso`; `Configurações` | `Treinamento` and `Configurações` are Brazilian (pt-PT: `Treino`, `Definições`); `settings` identical in pt-BR. |
| Smart Program Creator | `paywall_tile_program_creator` | `Smart Program Creator — feito para você` | English name kept; `para você` is the Brazilian pronoun. |
| Plateau detection | `plateau_detection` | `Detecção de platô` | `Detecção` / `detectado` use the pre-2009 / Brazilian `ct` spelling (pt-PT AO90: `deteção`, `detetado`). `platô` is the Brazilian form (pt-PT usage: `patamar` or `plateau`). |
| Estimated 1RM | `analytics_estimated_1rm` | `1RM estimado` |  |
| Deload week | `insert_deload_week` | `Inserir semana de descarga` | `Descarga`; one coach insight keeps English `deload`. |
| Periodization types: linear / DUP / block / wave | `creator_periodization_linear` / `_dup` / `_block` / `_wave` | `Linear` / `Ondulatoria (DUP)` / `Por Blocos` / `Ondas` | `creator_periodization` = `Estilo de Periodizacao`. Unaccented (`Ondulatoria`, `Periodizacao`): app bug. |
| Splits: Full Body / Upper-Lower / PPL / Push-Pull / Arnold / Bro | `creator_split_full_body` / `_upper_lower` / `_ppl` / `_push_pull` / `_arnold` / `_bro` | `Corpo inteiro` / `Superior / Inferior` / `Push / Pull / Pernas` / `Push / Pull` / `Split Arnold` / `Bro split` | English `Push / Pull` kept. Descriptions in the same screen are unaccented (`Divisao em dois com pernas distribuidas`, `Peito/Costas, Ombros/Bracos`). |
| Balance cards | `muscle_balance`; `front_back_balance`; `upper_lower_balance` | `Equilíbrio muscular`; `Frontal / Posterior`; `Superior / Inferior` |  |
| Program library | `programs`; `example_programs` | `Programas`; `Programas de exemplo` |  |
| The Golden Six | `arnold_golden_six_name` | `The Golden Six` |  |
| Rest timer | `watch_a11y_rest_timer` | `Temporizador de descanso` | `Temporizador` (watch label) and `Timer de descanso por frequência cardíaca` (settings): two words for one thing; LiftLog says `Cronómetro de descanso`. |
| Templates | `templates`; `workout_templates` | `Modelos`; `Modelos de treino` | `Modelos` (pt-PT and pt-BR agree here; ES says `Plantillas`). |
| Superset / Giant set | `superset`; `giant_set` | `Supersérie`; `Série gigante` | `Supersérie` in GymLogger X, `Superset` (English) in LiftLog. |
| Warm-up set | `warmup_set`; `mark_as_warmup` | `Série de aquecimento`; `Marcar como aquecimento` |  |
| Sets / Reps | `sets`; `reps` | `Séries`; `Repetições` |  |
| Personal records | `personal_records`; `prs` | `Recordes pessoais`; `Recordes` | `Recordes pessoais` / `Recordes` (pt-PT also accepts `recordes`). |
| Rep-max table | `analytics_rep_max_table` | `Tabela de repetições máximas` |  |
| Strength progress | `analytics_strength_progress` | `Progresso de força` |  |
| Next Move card | `analytics_next_move_label` | `Próximo passo` |  |
| Training load ratio | `analytics_acwr_title` | `Rácio de carga de treino` | The one place in the sheet where `pt` was visibly localised for Portugal: `Rácio` (pt-BR `Razão`). |
| Set volume vs MEV / MAV / MRV | `analytics_set_volume` | `Volume de séries` |  |
| Muscle heatmap | `muscle_heatmap` | `Mapa de calor muscular` |  |
| Readiness / fatigue / recovery | `home_fatigue`; `home_recovery` | `Nível de fadiga`; `Recuperação` |  |
| Plate calculator | `plate_calculator` | `Calculadora de discos` | `discos` is the PT-PT word for weight plates (pt-BR `anilhas`): one of the few pt-PT-specific gym words. |
| Weekly summary | `weekly_summary_title` | `Resumo semanal` |  |
| Custom exercises | `create_custom_exercise` | `Criar exercício personalizado` |  |
| Import a coach's spreadsheet program | `import_program`; `import_from_spreadsheets` | `Importar programa`; `Planilhas (CSV)` | `Planilhas` is Brazilian (pt-PT `Folhas de cálculo`). |
| Apple Health export | `health_saved_to_health` | `Salvo no Apple Health` | `Apple Health` (English, 11 strings) in the app; the InfoPlist says `Apple Saúde`. `Salvo` is Brazilian (pt-PT `Guardado`). |
| Start workout | `start_workout` | `Iniciar treino` |  |
| Family Sharing | `paywall_family_sharing_title` | `Inclui Partilha em Família` | `Partilha em Família` (this one is pt-PT, from the 186-string overlay). pt-BR would be: `Inclui Compartilhamento Familiar`. |
| iCloud sync | `icloud_sync` | `Sincronização iCloud` |  |
| Paywall wording (Pro) | `paywall_cta_start_trial`; `paywall_cta_yearly`; `paywall_headline`; `paywall_lifetime_description`; `paywall_no_subscription` | `Teste grátis`; `Continuar com anual`; `Treine com clareza, não por tentativa.`; `Pague uma vez, seu para sempre. Sem renovação.`; `Sem assinatura` | Brazilian register (`Treine`, `Pague`, `seu`, `assinatura`). The whole paywall is pt-BR text. |
| Tier wording: subscription | `subscription_active`; `manage_subscription` | `Assinatura ativa`; `Gerenciar assinatura` | Brazilian (`assinatura`, `gerenciar`); pt-PT `Subscrição` / `Gerir subscrição` appears in only 4 strings. |
| Coach / insight sentences | `coach_consistency_gap_message`; `unfinished_sets_warning` | `Já faz um tempo desde seu último treino. Mesmo uma sessão curta hoje ajudará a manter seu progresso.`; `Você tem séries inacabadas. Tem certeza de que deseja finalizar este treino?` | `você`, `seu` without article, `Tem certeza`: Brazilian. |
| Permission prompts (InfoPlist.strings, `pt.lproj`) | `NSHealthShareUsageDescription`; `NSHealthUpdateUsageDescription` | `O GymLogger lê a sua frequência cardíaca e calorias para fornecer informações sobre treinos e acompanhar o seu progresso físico.`; `O GymLogger guarda os seus treinos concluídos no Apple Saúde para manter os seus anéis de atividade e histórico completos.` | These two ARE European-style (`a sua`, `guarda`, `Apple Saúde`), formal. The `pt-BR.lproj` file says `sua`, `salva`. So the permission prompts are pt-PT while the UI is not. |


#### Paid tier names in the pt UI

`Pro` (tier), `Mensal` / `Anual` / `Vitalício`, `Pro Anual`, `Pro Vitalício`, `ACESSO VITALÍCIO`; buttons `Teste grátis`, `Iniciar Teste Grátis`, `Continuar com anual`, `Continuar com mensal`, `Desbloquear Pro Vitalício`, `Comprar acesso vitalício`, `Continuar com a versão gratuita`; `Restaurar Compras` / `Restaurar compras`; `Gerenciar assinatura`; `Sem assinatura`; `1 semana de teste grátis`; `Pagamento único`; `MAIS POPULAR`, `MELHOR VALOR`; `Inclui Partilha em Família`; `Economize 17%` (Brazilian verb).

#### Portuguese App Store listing (fetched 2026-11-19)

- Name: **GymLogger X: Treino Tracker** (English: "GymLogger X: Workout Tracker"). Differs: `Tracker` is left English.
- Subtitle: **Treino de Força e Registo** (English: "Strength Training & Gym Log"). Differs; `Registo` is the pt-PT noun (pt-BR `Registro`), so the store listing is European while the app is not.
- IAP as shown (reference): `GymLogger X Pro compra única 44,99 €` · `Support the developer 1,00 €` (untranslated) · `GymLogger X Pro anual 19,99 €` · `GymLogger X Pro mensal 1,99 €`.
- Languages: "Português e mais 33". Category: **Saúde e fitness**. Requires iOS 17.6 or later; age 9+. The Portuguese store page also lists `Português` as a language, which the app delivers in Brazilian form.

---

### 3. LiftLog (liftlog, source `CoreLift`, ID 6760043411)

#### Portuguese coverage

| Catalog | Keys | `pt-PT` present | `pt-PT` translated | % |
|---|---|---|---|---|
| CoreLift/CoreLift/Resources/Localizable.xcstrings (main app) | 990 | 980 | 980 | 99.0% |
| CoreLift/CoreLift/Resources/AppShortcuts.xcstrings | 6 | 6 | 6 (stringSet, 3-4 phrasings each) | 100% |
| CoreLift/CoreLift/Resources/InfoPlist.xcstrings | 4 | 2 | 2 | 50% (both Health permission texts are Portuguese; `CFBundleDisplayName` / `CFBundleName` have no entry, so the name is "LiftLog") |
| LiftLogWidgets/Resources/WidgetLocalizable.xcstrings | 137 | 137 | 137 | 100% |

The 10 main-app keys without `pt-PT`: ` / %lld` and `%@` (symbols only) and eight real English words that are user-visible in the Portuguese app: `Average`, `Best`, `Best run`, `By month`, `By weekday`, `min`, `Sessions in run`, `Weekly avg` (same eight as in Spanish; the widget catalog does translate them). Identical to English: 72 distinct values, almost all program names (`StrongLifts 5×5`, `nSuns`, `Smolov`, `PHAT`), `Reps` / `reps`, `Superset`, `Volume`, `Total`, `Core`, `Linear`. 731 of the 1,137 pt-PT values (64%) are identical to `pt-BR`.

Siri: the App Shortcuts phrases are Portuguese (see glossary), but the Siri hint in Localizable tells users to say the English phrases (`Diga “Start my next workout with LiftLog” para começar uma sessão, …`).

Permission texts name the app **LiftLog**, formal: `O LiftLog nunca lê os seus dados de saúde da Apple Saúde. Apenas guarda os seus treinos de força concluídos para que contem para os seus anéis de atividade.` / `O LiftLog guarda os seus treinos de força concluídos na Apple Saúde para que contem para os seus anéis de atividade. Nunca lê os seus dados de saúde.`

**Verdict: app is in European Portuguese: yes** (99.0% main app, 100% widgets and Shortcuts; 8 English fallbacks; markers: `Registar` 37 strings, `eliminar`/`apagar` 30, `guardar` 12, `ficheiro` 6, `Definições` 6, `cronómetro` 10, `telemóvel` 1; Brazilian leftovers: 1 `assinatura`, 1 `gerenciar`, 1 `Ajustes`, 1 `seu` without article).

Register (detail): of 1,125 strings, **about 116 are tu** (60 with a tu pronoun or tuteo verb: `Conclui treinos para veres o teu progresso e o mapa de atividade.`, `Paga o que achares justo.`, `Podes editá-la ou apagá-la como qualquer programa que crias tu.`, `Costumas treinar por esta hora — pronto para o treino de hoje?`, imperatives `Toca duas vezes para marcar como incompleto`, `Seleciona o nível …`, `Apaga todos os dados e começa do zero.`). **About 24 are formal / 3rd person** (+5 mixed): the Siri dialog answers (`Não consigo ler os seus dados do LiftLog. Abra a app uma vez e pergunte novamente.`, `A sua próxima série é por tempo. Registe-a no LiftLog.`, `O seu treino está em pausa. Retome-o primeiro no LiftLog.`), the HealthKit permission texts (`os seus`), `Defina o máximo de treino`, `Defina um peso inicial`, `Registe peso e medições`, `Ainda sem sequência — ainda não registou o seu primeiro treino.`, `A sua mensagem é lida por uma pessoa.`. **About 180 are impersonal infinitives** (`Adicionar exercício`, `Apagar`, `Iniciar treino`, `Restaurar compras`, `Editar`, `Remover`). Decision for the site: **tu**; the formal pockets are Siri answers and permission prompts.

Wording flags:
- **Tier `Patron`: app `Patrocinador`, store `Mecenas`** (the others match).
- `Back` (main and widget catalogs) is `Voltar` where a body-part label is meant; the uppercase neighbour `BACK` is `COSTAS`.
- `Rest Timer` = `Cronómetro de descanso` (a stopwatch; GymLogger X says `Temporizador`); the Siri phrase says `Iniciar o meu cronómetro de descanso`.
- `PR` badge = `RP`, an abbreviation nobody uses; `Rep PRs` = `Recordes de repetições`.
- `Reps` stays English in the label while `repetições` is used elsewhere.
- Old product name: 4 pt-PT strings still say **CoreLift** (`Ativa-as para o CoreLift em Definições › Notificações.`, `Seleciona um ficheiro de cópia CoreLift (.json) para importar.`); the English source has it 5 times.
- App name gender: `O LiftLog` (14 strings) vs `A LiftLog` (4: `A LiftLog é uma compra única`).
- Apple Health is `Apple Saúde` / `da Apple Saúde` (feminine) here and `app Saúde` in EarnLock.
- `Ajustes` (1 string: `Podes alterar a qualquer momento em Ajustes.`) vs `Definições` (6).
- Trial wording `Período experimental` (differs from EarnLock `período grátis`).

#### Glossary


| English term on site | English UI string (key) | pt-PT UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Free trial | `Free Trial`; `Free for 7 days.` | `Período experimental`; `Grátis durante 7 dias.` | `Período experimental` (also `Trial expired` = `Período expirado`). pt-BR would be: `Teste gratuito` ; `Grátis por 7 dias.`. |
| Tier: Fair | `Fair` | `Justo` | Same as the store IAP (`Acesso completo · Justo`). |
| Tier: Good | `Good` | `Bom` | `Bom`. Same as the store IAP (`Acesso completo · Bom`). |
| Tier: Generous | `Generous` | `Generoso` | Same as the store IAP. |
| Tier: Patron | `Patron` | `Patrocinador` | **The app says `Patrocinador`; the store IAP is `Acesso completo · Mecenas`.** The tier names need one decision for the site. |
| Full access | `Full Access` | `Acesso total` | pt-BR would be: `Acesso completo`. |
| One-time purchase / no subscription | `One-time purchase`; `No subscription` | `Compra única`; `Sem subscrição` | `subscrição` (pt-PT); pt-BR `assinatura`. One BR leftover: 1 string says `assinatura`. pt-BR would be: `Sem assinatura`. |
| Restore Purchases | `Restore Purchases` | `Restaurar compras` |  |
| Tabs: Home / Exercises / Programs / Progress / Settings | `Home` / `Exercises` / `Programs` / `Progress` / `Settings` / `History` | `Início` / `Exercícios` / `Programas` / `Progresso` / `Definições` / `Histórico` | `Workouts` = `Treinos`, `Today` = `Hoje`. pt-BR Settings would be `Ajustes`. |
| Log set key | `Log set · start rest`; `Log Set` | `Registar série · iniciar descanso`; `Registar série` | Verb `Registar` is pt-PT (pt-BR `Registrar`). pt-BR would be: `Registrar série · iniciar descanso` ; `Registrar série`. |
| Rest timer | `Rest Timer`; `Rest timer` | `Cronómetro de descanso`; `Cronómetro de descanso` | `Cronómetro` (a stopwatch) is the app's word; GymLogger X says `Temporizador`. pt-BR would be: `Cronômetro de descanso` ; `Cronômetro de descanso`. |
| Estimated 1RM | `Estimated 1RM`; `Est. 1RM` | `1RM estimado`; `1RM est.` |  |
| Rep PRs | `Rep PRs`; `PR` | `Recordes de repetições`; `RP` | `PR` badge is `RP`, an abbreviation nobody uses. |
| Personal bests | `Personal Bests`; `New Personal Bests`; `Personal record` | `Recordes pessoais`; `Novos recordes pessoais`; `Recorde pessoal` | pt-BR: `Novos recordes`. |
| Best set / Best volume | `Best Set`; `Best Volume` | `Melhor série`; `Melhor volume` |  |
| Activity heatmap | `Complete workouts to see your progress and activity heatmap.` | `Conclui treinos para veres o teu progresso e o mapa de atividade.` | pt-BR would be: `Conclua treinos para ver seu progresso e o mapa de atividade.`. |
| Last 30 days | `Last 30 days` | `Últimos 30 dias` |  |
| Training Max | `Set a training max` | `Defina o máximo de treino` | `máximo de treino`, with the formal imperative `Defina` (not `Define`). |
| Double progression / Progression | `Double progression`; `Progression` | `Dupla progressão`; `Progressão` |  |
| Deload (trigger) | `Deload` | `Descarga` |  |
| Adaptive 1RM formula | `Adaptive (recommended)`; `1RM Formula` | `Adaptativa (recomendada)`; `Fórmula de 1RM` |  |
| Superset / Giant set | `Superset`; `Giant Set` | `Superset`; `Série gigante` | `Superset` stays English; `Série gigante` is Portuguese. |
| How To (exercise detail) | `How To` | `Como fazer` |  |
| Workout | `Workout` | `Treino` |  |
| Sets / Reps | `Sets`; `Reps` | `Séries`; `Reps` | `Reps` is English in the label; `repetições` is used elsewhere. |
| Streak | `Streak` | `Sequência` |  |
| Export (JSON / CSV) | `Export Data (CSV)`; `Export Data (JSON)` | `Exportar dados (CSV)`; `Exportar dados (JSON)` |  |
| Apple Health | `Apple Health` | `Apple Saúde` | `Apple Saúde` and `da Apple Saúde` in the permission texts; `Guarda … na Apple Saúde` (feminine). |
| Family Sharing | `Family Sharing` | `Partilha com a Família` | `Partilha com a Família`; Apple pt-PT: `Partilha em Família`. |
| Warm-up set | `Warm-up set %lld` | `Série de aquecimento %lld` |  |
| Siri & Shortcuts | `Siri & Shortcuts` | `Siri e Atalhos` | `Siri e Atalhos`. |
| Support | `Support`; `Funds 3 months of dev` | `Apoiar`; `Financia 3 meses de desenvolvimento` | `Apoiar`. |
| Siri / App Shortcuts phrases | `Start my next workout with ${applicationName}`; `What's my streak in ${applicationName}`; `Log my set in ${applicationName}`; `Start my rest timer in ${applicationName}`; `How much did I lift this week in ${applicationName}` | `Iniciar o meu próximo treino com ${applicationName}`; `Qual é a minha sequência no ${applicationName}`; `Registar a minha série no ${applicationName}`; `Iniciar o meu cronómetro de descanso no ${applicationName}`; `Quanto levantei esta semana no ${applicationName}` | 6 shortcuts, each with 3-4 phrasings, all pt-PT (`Registar`, `cronómetro`). `no ${applicationName}` uses masculine article (`O LiftLog`: 14 strings) but 4 strings write `A LiftLog` (`A LiftLog é uma compra única`). |
| Siri hint in Localizable | `Say “Start my next workout with LiftLog” to begin a session, …` | `Diga “Start my next workout with LiftLog” para começar uma sessão, ou pergunte “What’s my streak in LiftLog?” e …` | Tells Portuguese users to say the English phrases while the Shortcuts catalog has Portuguese ones. Formal imperative (`Diga`, `pergunte`). |
| Old product name | `Select a CoreLift backup file (.json) to import.`; `Turn them on for CoreLift in Settings › Notifications.` | `Seleciona um ficheiro de cópia CoreLift (.json) para importar.`; `Ativa-as para o CoreLift em Definições › Notificações.` | 4 pt-PT strings carry the old name CoreLift (the English source has it in 5). App-side text bug, same in every language. |
| Pay what feels fair | `Pay what feels fair.`; `One payment. Yours forever. Free for the next 7 days.` | `Paga o que achares justo.`; `Um pagamento. Teu para sempre. Grátis nos próximos 7 dias.` | tu. |
| Back (widget / body-part) | `Back` (main and widget catalogs); `BACK` | `Voltar`; `COSTAS` | `Back` as a body-part label is `Voltar` (the navigation word) where `Costas` is meant; the uppercase neighbour is right. |


#### Paid tier names in the pt-PT UI

LiftLog has no Pro/Premium and no subscription: it is a one-time purchase with four tiers that all unlock the same app: `Justo` / `Bom` / `Generoso` / `Patrocinador` (in-app) against `Justo` / `Bom` / `Generoso` / `Mecenas` (App Store IAP names); buttons `Desbloquear`, `Período experimental`, `Restaurar compras`; `Paga uma vez. Teu para sempre. Sem renovação.`; `Um pagamento. Teu para sempre. Grátis nos próximos 7 dias.`; `Sem cartão. Sem ciladas de teste. Sem renovação automática.` The only mismatch is Patron.

#### Portuguese App Store listing (fetched 2026-11-19)

- Name: **LiftLog: Treino Ginásio** (English: "LiftLog: Workout Gym Tracker"). Differs.
- Subtitle: **Séries, reps & força** (English: "Sets, reps & strength programs"). Differs (`reps` English, `&` kept).
- IAP as shown (reference): `Acesso completo · Justo 9,99 €` · `Acesso completo · Bom 22,99 €` · `Acesso completo · Generoso 39,99 €` · `Acesso completo · Mecenas 44,99 €`.
- Languages: "Português e mais 43". Category: **Saúde e fitness**. Requires iOS 17.6 or later; age 4+.

---

### 4. MediaKit (mediakit, source `ClearCut`, ID 6761451361)

#### Portuguese coverage

| Catalog | Keys | `pt-PT` present | `pt-PT` translated | % |
|---|---|---|---|---|
| ClearCut/MediaKit/Localizable.xcstrings (main app) | 2583 | 2583 | 2583 | 100% |
| ClearCut/MediaKit/AppShortcuts.xcstrings | 6 | 6 | 6 | 100% |
| ClearCut/MediaKit/InfoPlist.xcstrings | 26 | 23 | 23 | 88.5% (missing: `CFBundleDisplayName`, `CFBundleName`, `NSHumanReadableCopyright`) |
| ClearCut/MediaKitShareExtension/Localizable.xcstrings | 13 | 13 | 13 | 100% |

The InfoPlist entries are mostly document-type names (`Ficheiro de áudio`, `Arquivo de banda desenhada`, `E-book Kindle`, `Áudio Matroska`) and the Photo Library and Speech Recognition prompts. 1,503 of 2,628 pt-PT values (57%) are identical to `pt-BR`; about 94 distinct values are identical to English (codec and font names, platform presets such as `Spotify (−14 LUFS)`, file extensions, `Codec`, `Loudness`, `Fade`, `Crossfade`, `MediaKit Pro`).

**Verdict: app is in European Portuguese: yes** (100% of the UI, share extension and Shortcuts; markers: `ficheiro` 241 strings, `guardar` 64, `Definições` 28, `ecrã` 12, `partilhar` 8, `eliminar`/`apagar` 9, `subscrição` 9, `transferir` 6, `telemóvel` 4, progressive form `A processar`, `A converter`, `A adicionar`). Brazilian leftovers (rare): `descompactar` / `descompactado` / `descompactação` (18 strings; pt-PT `descomprimir`), `rastreamento` (3: `Sem telemetria ou rastreamento`), `tela` (1: `Desenhe uma assinatura na tela`), `Assine o Pro` (1), `Teste` for trial, `excluir` (4, as in "exclude"), and `Pague uma vez, seu para sempre`.

Register (detail): of 2,625 strings, **0 contain a tu pronoun** (`teu`, `tua`, `tens`, `podes`, `estás` all absent). **About 186 are formal 3rd person** (+2 mixed): `o seu`, `os seus ficheiros` (`Nada sobre os seus ficheiros sai do iPhone`), `Só lhe será pedido uma vez para esta pasta.`, `Desbloqueie o Pro para processar …`, `Escolha H.264 ou HEVC.`, `Converta-o primeiro para MP4`, `Verifique a sua ligação e tente novamente.`, `Arraste um ficheiro ou use as setas`, `cancele quando quiser nas Definições`, `A sua opinião honesta ajuda mesmo.`. About 30 strings start with a 3rd-person present verb that reads as a tool description and is ambiguous with tu (`Recorta imagens em dimensões personalizadas`, `Roda e inverte imagens`, `Abre as ferramentas de %@`, `Cria toques para iPhone (M4R)`), and about 390 are impersonal infinitives (`Comprimir vídeo`, `Converter imagem`, `Tentar novamente`, `Iniciar avaliação gratuita`). **Decision for the site: formal register (`o seu` / 3rd person or impersonal), not tu.** This differs from EarnLock, LiftLog and Millrace, and the site needs a policy for that app (translate quotes as formal, or paraphrase).

Wording flags:
- `Free` alone = **`Livre`** (wrong word for "free of charge"), `Free tier` = `Plano gratuito`, `Free forever` = `Grátis para sempre`, `Free — 5 tools available` = `Grátis — 5 ferramentas disponíveis`: three words for one idea.
- Trial: `Teste grátis de %@`, `%@ de avaliação grátis, depois %@`, `Teste Pro`, `3 dias de acesso Pro grátis incluídos`.
- `Make it Social` has two forms: `Pronto para redes` (menu / title) and the English `Make it Social` in 3 strings.
- Redact is `Censurar` (PDF) and `Ocultar retângulos` (same tool).
- `Archive` = `Arquivo` is correct pt-PT for a compressed archive (pt-BR `Arquivo compactado`) but `Arquivo` can be confused with "file"; the word for a file is `ficheiro`.
- `Ebook` = `E-book`. `Video` is `Vídeo` with accent (72+ strings).
- `fototeca` (Photo Library prompt) is not Apple's pt-PT word (`Fotografias`).
- English left in: `Fade`, `Crossfade`, `Loudness`, `Codec`, `Normal`, `Vocal`, `Remux`, platform names (fine).
- Family Sharing: `Compatível com a Partilha em Família` (correct pt-PT name, the only exact match across the five apps outside GymLogger X's paywall).
- No Mac or macOS term problems found (`este Mac` is masculine, consistent).

#### Glossary


| English term on site | English UI string (key) | pt-PT UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Pro | `Pro` | `Pro` | Not translated. |
| Pro · Monthly | `Monthly` | `Mensal` |  |
| Pro · Annual | `Annual` | `Anual` |  |
| Lifetime | `Lifetime` | `Vitalício` |  |
| Free trial (3 days) | `Every tool, 3 days free`; `%@ free trial`; `%@ free trial · %@/mo` | `Todas as ferramentas, 3 dias grátis`; `Teste grátis de %@`; `%@ de teste grátis · %@/mês` | Two words for the trial: `Teste grátis` and `avaliação grátis` (also `Teste Pro`). |
| Free tier (five tools stay free) | `Free tier`; `Free` | `Plano gratuito`; `Livre` | **`Free` alone is translated `Livre`** (means "unrestricted/free to move"), while `Free tier` is `Plano gratuito` and `Free forever` is `Grátis para sempre`. `Go Pro` = `Assine o Pro` (Brazilian imperative). |
| Tool (generic) | `Tool`; `Add a Tool to the Recipe` | `Ferramenta`; `Adicionar uma ferramenta à receita` |  |
| Recipes (chained tools) | `Recipes`; `Create a new multi-step recipe`; `Recipe Marketplace` | `Receitas`; `Criar uma nova receita de vários passos`; `Mercado de receitas` | `Mercado de receitas` for the marketplace; `catálogo do marketplace` also appears. |
| Make It Fit | `Make It Fit` | `Ajustar ao tamanho` | Tool-picker feature "Make It Social" (a different row on the site) has two forms in the app: `Pronto para redes` and `Make it Social` (English, 3 strings). |
| Video / Image Compress | `Compress`; `Compress Video`; `Compress Image` | `Comprimir`; `Comprimir vídeo`; `Comprimir imagem` |  |
| Image Resize | `Resize` | `Redimensionar` |  |
| Convert (audio, image...) | `Convert`; `Convert Image` | `Converter`; `Converter imagem` |  |
| Categories: Video / Audio / Image / PDF / Archive / Ebook | `Video` / `Audio` / `Image` / `PDF` / `Archive` / `Ebook` | `Vídeo` / `Áudio` / `Imagem` / `PDF` / `Arquivo` / `E-book` | `Arquivo` for a compressed archive is correct pt-PT (pt-BR `Arquivo compactado`); `ficheiro` is the word for a file (241 strings). |
| Batch processing | `Batch Processing` | `Processamento em lote` |  |
| Export presets | `Preset`; `Platform preset` | `Predefinição`; `Predefinição de plataforma` |  |
| Shortcuts actions | `Shortcuts & Siri` | `Atalhos e Siri` |  |
| Merge | `Merge`; `Merge PDFs` | `Juntar`; `Unir PDFs` | `Juntar` / `Unir` (pt-PT); pt-BR `Mesclar`. |
| Extract text / OCR | `Extract Text from Image`; `OCR` | `Extrair texto de imagem`; `OCR` |  |
| Remove background | `Remove background` | `Remover fundo` |  |
| AI upscale | `AI Upscale` | `Ampliação com IA` |  |
| Auto Subtitle | `Auto Subtitle`; `Auto Subtitle + Translate` | `Legendas automáticas`; `Legendas automáticas + tradução` | `Legendas automáticas` (pt-BR singular). |
| Transcribe | `Transcribe` | `Transcrever` |  |
| Strip EXIF metadata | `Strip Metadata` | `Remover metadados` | `Remover metadados`. |
| Reduce noise | `Noise Reduce`; `Denoise` | `Reduzir ruído`; `Reduzir ruído` |  |
| Normalize (EBU R128 / LUFS) | `Normalize loudness`; `EBU R128 loudness normalization` | `Normalizar a intensidade sonora`; `Normalização de intensidade sonora EBU R128` | pt-PT uses `intensidade sonora`; pt-BR `volume`. |
| Redact | `Redact PDF`; `Redact`; `Redact rectangles` | `Censurar PDF`; `Censurar`; `Ocultar retângulos` | `Censurar` (PDF) and `Ocultar retângulos`: two verbs. |
| Compare | `Compare`; `Compare Takes` | `Comparar`; `Comparar takes` |  |
| Smart Duplicate Finder | `Smart Duplicate Finder` | `Localizador inteligente de duplicados` | `duplicados` (pt-PT); pt-BR `duplicatas`. |
| Trim / Stabilize / Watermark / Crop / Rotate / Flip / Sign / Encrypt | `Trim` / `Stabilize` / `Watermark` / `Crop` / `Rotate` / `Flip` / `Sign` / `Encrypt` | `Aparar` / `Estabilizar` / `Marca de água` / `Recortar` / `Rodar` / `Inverter` / `Assinar` / `Encriptar` | pt-PT verbs (pt-BR `Cortar`, `Girar`, `Virar`, `Marca d'água`). `Encriptar` (pt-PT) next to `cifrado` for archives. |
| Drop a file in | `Drop a file to preview` | `Largue um ficheiro para pré-visualizar` | `Largue um ficheiro` (pt-PT verb `largar`; formal imperative). |
| Watch folder / Folder Automation | `Watch folder`; `Folder Automation` | `Pasta monitorizada`; `Automatização de pastas` | pt-BR would be: `Pasta monitorada` ; `Automação de pastas`. |
| Menu bar | n/a | no UI string |  |
| Settings | `Settings` | `Definições` | `Definições` (14 strings, 0 `Ajustes`). |
| Restore Purchases | `Restore Purchases` | `Restaurar compras` |  |
| Share extension | `Open in MediaKit`; `Send to MediaKit` | `Abrir no MediaKit`; `Enviar para o MediaKit` |  |
| Family Sharing | `Works with Family Sharing` | `Compatível com a Partilha em Família` | Apple pt-PT name; GymLogger X's paywall string uses it too. |
| Siri / App Shortcuts phrases | `Compress a video with ${applicationName}`; `Merge PDFs with ${applicationName}`; `Create a ZIP with ${applicationName}`; `Extract text from image with ${applicationName}` | `Comprimir um vídeo com o ${applicationName}`; `Unir PDFs com o ${applicationName}`; `Criar um ZIP com o ${applicationName}`; `Extrair texto de imagem com o ${applicationName}` | 6 phrases, one phrasing each, all pt-PT infinitive style (impersonal, no register). |
| Permission prompts (InfoPlist) | `NSPhotoLibraryAddUsageDescription`; `NSSpeechRecognitionUsageDescription` | `O MediaKit guarda os vídeos e as imagens processados na sua fototeca.`; `O MediaKit utiliza o reconhecimento de voz para transcrever áudio e vídeo em texto quando executa a ferramenta Transcrever.` | Formal (`sua`). `fototeca` is not the Apple pt-PT word (`Fotografias`); same word in EarnLock. |
| Trial / paywall lines | `Go Pro for unlimited access + batch processing.`; `Pay once, own forever`; `Free forever` | `Assine o Pro para acesso ilimitado + processamento em lote.`; `Pague uma vez, seu para sempre`; `Grátis para sempre` | `Assine` / `Pague` are formal imperatives; `Assine` is the Brazilian verb (pt-PT `Subscreva`). |
| Rating prompt | `MediaKit is built by an independent developer. Your honest take genuinely helps.` | `O MediaKit é feito por um programador independente. A sua opinião honesta ajuda mesmo.` | Formal, `programador` (pt-PT). |


#### Paid tier names in the pt-PT UI

`MediaKit Pro` / `Pro` (tier), `Mensal` / `Anual` / `Vitalício` (`Pro · Mensal`, `Pro · Anual`), `Plano gratuito` (free tier), `Livre` (bare Free), `Teste grátis de %@`, `3 dias de acesso Pro grátis incluídos`, `Compra única, nunca expira`, `Pagamento único, cobrado uma só vez. Sem subscrição, sem renovação automática.`, `Gerir subscrição`, `Restaurar compras` / `Restaurar compra`, `Pro necessário`, `Ferramenta Pro`.

#### Portuguese App Store listing (fetched 2026-11-19)

- Name: **MediaKit Comprimir e Converter** (English: "MediaKit: Compress & Convert"). Differs (no colon, `e` for the ampersand).
- Subtitle: **Vídeo, Áudio, Imagem, PDF, ZIP** (English: "Video, Audio, Image, PDF & ZIP"). Differs.
- IAP as shown (reference): `MediaKit Pro anual 24,99 €` · `MediaKit Pro compra única 44,99 €` · `MediaKit Pro mensal 4,99 €`.
- Languages: "Português e mais 11". Category: **Utilitários**. Requires iOS 17.0 or later; age 4+.

---

### 5. Millrace (millrace, source `thegame`, ID 6759511759; house rule: the former name and its number are never written on the site)

#### Portuguese coverage

| Catalog | Keys | `pt-PT` present | `pt-PT` translated | % |
|---|---|---|---|---|
| thegame/thegame/Localizable.xcstrings (only catalog) | 333 | 333 | 333 | 100% |

Only three strings are identical to English (`Extras`, `Game Center`, `Puzzles`). 137 of 333 (41%) are identical to `pt-BR`. No widget, Watch app, App Shortcuts or `InfoPlist.xcstrings`. No pt-PT string contains the former name's number (checked programmatically). The catalog uses plural categories `one`, `other` and `many` (pt-PT `many`: `%lld de peças a chegar`).

**Verdict: app is in European Portuguese: yes** (100%; `Definições`, `subscrição`, `programador`, `Anular`, `Puzzle`, `Joga`, `Contactar o suporte`, `Iniciar sessão no Game Center`, `Resolvido em %lld jogadas`; zero Brazilian vocabulary).

Register (detail): of 333 strings, **about 50 are tu** (26 with a tu pronoun or tuteo verb: `Resta-te %lld anulação.`, `Restam-te %lld anulações.`, `Mantém a tua peça %@ em segurança no canto.`, `Grátis · sempre teu`, `Toca em qualquer tema para o pré-visualizares grátis no teu tabuleiro`, `Faz parte de %@ · %lld temas`, `Joga diariamente para ganhar anulações grátis.`, `O que tornaria o Millrace melhor para ti?`). **3 are formal**: `Anula a sua última jogada`, `Deslize para cima, baixo, esquerda ou direita para mover as peças` (VoiceOver hint) and `Apoie o programador`; the Freeplay description also says `Combine peças enquanto conseguir`. **About 56 are impersonal infinitives** (`Desbloquear tudo`, `Mover para a esquerda`, `Contactar o suporte`, `Desafiar um Amigo`). Decision for the site: **tu**.

Wording flags:
- Undo is `Anular` (noun `Anulação`, `Fichas de Anulação`), consistent with the store IAPs (`10 Anulações`).
- Merge has three verbs: `Junta` / `Junção` (7), `combina` / `Combine` (6), `fundir` (1).
- Title Case in sentence-style labels: `Sequência Atual`, `Sequência Mais Longa`, `Recompensas de Sequência`, `Desafio Diário`, `Efeitos Sonoros`, `Restaurar Compras`, `Pacote de Autor 1`: English capitalisation, not Portuguese style.
- `Proezas` for achievements (Game Center) is unusual; pt-BR says `Conquistas`; check Apple's pt-PT wording before quoting.
- `Vibração` for haptics; `Jogo Livre` for Freeplay; `Treinador` for the Coach.
- Store subtitle `64 níveis com uma só entrada` (the English subtitle says "one inlet").
- Register mix: tu in game text, formal in `Apoie o programador`, `Anula a sua última jogada` and the VoiceOver hint.

#### Glossary


| English term on site | English UI string (key) | pt-PT UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Chapter: Warm-up | `Warm-up` | `Aquecimento` |  |
| Chapter: Tactics | `Tactics` | `Táticas` |  |
| Chapter: Pressure | `Pressure` | `Pressão` |  |
| Chapter: Precision | `Precision` | `Precisão` |  |
| Chapter: Deep Water | `Deep Water` | `Águas Profundas` |  |
| Chapter: Mastery | `Mastery` | `Maestria` |  |
| Level | `Level %lld` | `Nível %lld` |  |
| Puzzle | `Puzzles`; `Next puzzle`; `Puzzle not solved` | `Puzzles`; `Próximo puzzle`; `Puzzle não resolvido` | `Puzzle(s)` stays English-in-Portuguese (identical to the English key and accepted in pt-PT); pt-BR `quebra-cabeça`. |
| Freeplay | `Freeplay` | `Jogo Livre` | `Jogo Livre`. |
| Hint | `Hint` | `Dica` |  |
| The Coach | `Coach`; `Coaching notes` | `Treinador`; `Notas do treinador` | `Treinador` (also `Treinador` for Coach card). |
| Daily board / daily challenge | `Daily Challenge`; `Daily challenge`; `Daily` | `Desafio Diário`; `Desafio diário`; `Diário` | Title Case in one string (`Desafio Diário`), sentence case in the other. |
| Undo | `Undo` | `Anular` | `Anular` is Apple's pt-PT word and the noun in the paywall (`10 Anulações`). Not a bare verb (unlike ES `deshacer`). |
| Daily streak | `Current Streak`; `Longest Streak`; `Streak Rewards` | `Sequência Atual`; `Sequência Mais Longa`; `Recompensas de Sequência` | Title Case (`Sequência Atual`, `Recompensas de Sequência`) is English capitalisation. |
| Personal best | `Personal Best`; `Best`; `NEW BEST` | `Recorde Pessoal`; `Melhor`; `NOVO RECORDE` | `Melhor` alone for "Best". |
| Move budget / moves left | `%lld moves left`; `No moves left` | `one: %lld jogada restante; other: %lld jogadas restantes`; `Sem jogadas` |  |
| Target cell | `Row %lld, column %lld, empty. This is the target cell.` | `Linha %1$lld, coluna %2$lld, vazia. Esta é a célula-alvo.` | `célula-alvo` (hyphenated). |
| Inlet | `Tiles arrive here.` | `As peças chegam aqui.` | The word "inlet" has no UI string; the arrival cell is `Chegada` (`Arrival 1` = `Chegada 1`). The store subtitle renders it as `uma só entrada`. |
| Tile | `%lld tiles arriving` | `many: %lld de peças a chegar; one: %lld peça a chegar; other: %lld peças a chegar` | Portuguese word = `peça` (feminine). `many:` plural category exists in pt-PT (`%lld de peças`). |
| Blocked | `Blocked` | `Célula bloqueada` | `Célula bloqueada` (accessibility label). |
| Theme / themes | `Theme`; `Themes` | `Tema`; `Temas` |  |
| Theme packs | `Designer Pack 1`; `Designer Pack 2`; `Summer Pack`; `Winter Pack` | `Pacote de Autor 1`; `Pacote de Autor 2`; `Pacote de Verão`; `Pacote de Inverno` | `Pacote de Autor` (pt-BR `Pacote Designer`). |
| Complete Collection | `Complete collection` | `Coleção completa` |  |
| Classic (free theme) and theme names | n/a | no catalog entries | Theme names are not in the catalog. |
| Support the Developer (tip) | `Support the Developer` | `Apoie o programador` | Formal imperative (`Apoie`), unlike the tu strings elsewhere in the game. `programador` is pt-PT. |
| Game Center leaderboards / achievements | `Leaderboards`; `Achievements` | `Classificações`; `Proezas` | `Proezas` for achievements is unusual (pt-BR `Conquistas`; check Apple's pt-PT Game Center wording before quoting). |
| Settings: Haptics / Sound Effects / Music | `Haptics` / `Sound Effects` / `Music` | `Vibração` / `Efeitos Sonoros` / `Música` | `Vibração` for haptics (check against Apple's pt-PT wording); Title Case `Efeitos Sonoros`. |
| Settings | `Settings` | `Definições` | `Definições`. |
| No subscription | `One-time purchases. No subscription. No ads, ever.` | `Compras únicas. Sem subscrição. Sem anúncios, nunca.` | `subscrição`. |
| Restore Purchases | `Restore Purchases` | `Restaurar Compras` | Title Case `Restaurar Compras` (other apps use `Restaurar compras`). |
| Arrival cell | `Arrival 1`; `Row %lld, column %lld, empty. Tiles arrive here.` | `Chegada 1`; `Linha %1$lld, coluna %2$lld, vazia. As peças chegam aqui.` | The word "inlet" is not in the catalog (arrival cell = `Chegada`); store subtitle: `uma só entrada`. |
| Merge | `Merges two %@ tiles.`; `Column Merge`; `First Merge`; `Merge as long as you can. No goal, no move limit.` | `Junta duas peças %@.`; `Junção em Coluna`; `Primeira Junção`; `Combine peças enquanto conseguir. Sem objetivo, sem limite de jogadas.` | Three verbs for merge (`juntar` 7 strings, `combinar` 6, `fundir` 1); the Freeplay description is formal (`Combine … conseguir`) among tu strings. |
| Score | `Score`; `Best Score`; `Average Score`; `Best Tile` | `Pontuação`; `Melhor Pontuação`; `Pontuação Média`; `Melhor Peça` | Title Case. |
| Coach card tips | `Keep your big tiles together in one row, in size order.`; `Clear small tiles early — a full board has nowhere to go.` | `Mantém as tuas peças grandes juntas na mesma linha, por ordem de tamanho.`; `Junta as peças pequenas cedo — um tabuleiro cheio não tem para onde ir.` | tu. |
| Undo tokens / bundles | `Undo Tokens`; `10 Undos`; `Get Undos`; `Use an undo?` | `Fichas de Anulação`; `10 Anulações`; `Obter Anulações`; `Usar uma anulação?` | `Anulação(ões)` noun, same as the store IAPs (`10 Anulações`, `50 Anulações`, `200 Anulações`). |


#### Paid tier names in the pt-PT UI

Millrace has no paid tier or subscription: it is free with optional purchases. In the UI: `Compras únicas. Sem subscrição. Sem anúncios, nunca.`; theme packs `Pacote de Autor 1`, `Pacote de Autor 2`, `Pacote de Verão`, `Pacote de Inverno`; `Coleção completa`; undo bundles `10 Anulações`, `50 Anulações`, `200 Anulações` (`Obter Anulações`, `Adicionar 50 Anulações`); tip `Apoie o programador`; `Desbloquear Todos os Temas`; `Restaurar Compras`.

#### Portuguese App Store listing (fetched 2026-11-19)

- Name: **Millrace: Puzzle de peças** (English: "Millrace: Tile Delivery Puzzle"). Differs. Page title: "App Millrace: Puzzle de peças – App Store".
- Subtitle: **64 níveis com uma só entrada** (English: "64 forged levels, one inlet"). Differs.
- IAP as shown (reference): `Coleção Completa 6,99 €` · `50 Anulações 2,99 €` · `Pacote de Inverno 1,99 €` · `Apoie o programador 1,99 €` · `200 Anulações 6,99 €` · `10 Anulações 0,99 €` · `Pacote de Autor 2 1,99 €` · `Pacote de Autor 1 1,99 €` · `Pacote de Verão 1,99 €`. The in-app names match the store names.
- Languages: "Português e mais 33". Category: **Tabuleiro** (English storefront: "Board"). Requires iOS 18.0 or later; age 4+.

---

## Cross-app terms

| Concept | Value in each app |
|---|---|
| Restore purchases | "Restaurar compras" in all five (Millrace and GymLogger X's paywall key also "Restaurar Compras", Title Case) |
| Settings | "Definições" in EarnLock (6), LiftLog (6), MediaKit (14), Millrace (3); **"Ajustes" leaks into EarnLock (5) and LiftLog (1)**; GymLogger X says "Configurações" (4), "Ajustes" (4) |
| Free | "Grátis" / "gratuito" (EarnLock, LiftLog, Millrace, GymLogger X); MediaKit "Plano gratuito" and bare "Livre" |
| Lifetime | "Vitalício" in EarnLock, GymLogger X ("Pro Vitalício", "ACESSO VITALÍCIO"), MediaKit; store IAPs use "compra única" in all three |
| Monthly / Yearly | "Mensal" / "Anual" in all subscription apps (GymLogger X "Yearly" = "Anual", MediaKit "Annual" = "Anual") |
| Free trial | "período grátis" / "Avaliação gratuita" (EarnLock), "Período experimental" (LiftLog), "Teste grátis" (MediaKit, GymLogger X "Teste Grátis"); three words |
| Subscription | "subscrição" (EarnLock, LiftLog, MediaKit, Millrace); **"assinatura" in GymLogger X (11) and 6 MediaKit strings that mean signature/subscription** |
| Upgrade | "fazer upgrade" (EarnLock, 5), "Obter Premium", "Assine o Pro" (MediaKit), "Desbloquear Pro Vitalício" (GymLogger X) |
| Unlock | "Desbloquear" (infinitive) in buttons; "Desbloqueie" (formal) in MediaKit; "Desbloqueia" (tu) in EarnLock |
| Premium tier name | "Premium" (EarnLock), "Pro" (GymLogger X, MediaKit); no Pro in LiftLog or Millrace |
| Add | "Adicionar" / "Adiciona" in all (never "Agregar") |
| Save | "guardar" in EarnLock, LiftLog, MediaKit; **"salvar" in GymLogger X (39)** |
| Record / log | "Registar" (LiftLog 37, EarnLock 12); **"Registrar" in GymLogger X (25)** |
| Streak | "Sequência" in EarnLock, LiftLog, Millrace, GymLogger X |
| Personal best | "Recorde pessoal" / "Recordes pessoais" (LiftLog, GymLogger X, Millrace "Recorde Pessoal"); LiftLog badge "RP" |
| Sets / Reps | "Séries" in LiftLog and GymLogger X; "Reps" in LiftLog (English) vs "Repetições" in GymLogger X |
| Superset / Giant set | "Superset" (LiftLog) / "Supersérie" (GymLogger X); "Série gigante" in both |
| Deload | "Descarga" in LiftLog and GymLogger X |
| Rest timer | "Cronómetro de descanso" (LiftLog) vs "Temporizador de descanso" (GymLogger X) |
| Workout | "Treino" (all) |
| Heatmap | "Mapa de calor de atividade" (EarnLock), "Mapa de calor muscular" (GymLogger X), "mapa de atividade" (LiftLog) |
| Apple Health | "Apple Saúde" (EarnLock, LiftLog, GymLogger X permission prompts), "app Saúde" (EarnLock, 4), "Apple Health" (GymLogger X in-app, 11) |
| Screen Time | "Tempo de ecrã" (EarnLock, 21 strings, no "tela") |
| Family Sharing | "Partilha em Família" (MediaKit, GymLogger X), "Partilha com a família" (EarnLock), "Partilha com a Família" (LiftLog); Apple pt-PT name is "Partilha em Família" |
| Lock Screen | "Ecrã Bloqueado" (EarnLock widget title); Apple pt-PT "Ecrã de Bloqueio" |
| Siri & Shortcuts | "Siri e Atalhos" (LiftLog), "Atalhos e Siri" (MediaKit): word order differs |
| Photo Library | "fototeca" in EarnLock and MediaKit permission prompts |
| App | "app" / "apps" feminine (EarnLock "uma app bloqueada", LiftLog "a mesma app"), 83 / 9 / 21 strings; "aplicação" only in LiftLog (1), Millrace (1: `Reiniciar a aplicação`), GymLogger X (9, plus "aplicativo" 2); none in MediaKit |
| File | "ficheiro" (MediaKit 241, LiftLog 6); "arquivo" means archive in MediaKit and file in GymLogger X (12) |
| Goal | "objetivo" (EarnLock 41, GymLogger X 9) and "meta" (EarnLock 11, GymLogger X 8) |
| Developer | "programador" (EarnLock 1, LiftLog 3, MediaKit 5, Millrace 4) |
| Register | tu: EarnLock, LiftLog (UI), Millrace; formal 3rd person: MediaKit; Brazilian você: GymLogger X |
| Store title punctuation | no colon for MediaKit; colon kept for the other four |

## Flags

App-side string bugs (also belong in ISSUES.md after review by the main session)
1. **GymLogger X, no European Portuguese (P-G1):** the `pt` table is Brazilian (você 66, seu/sua 107, salvar 39, registrar 25, excluir 21, assinatura 11, gerenciar 8, gerunds 26, Configurações, Treinamento). `pt-PT` is declared as an exercise-only locale and falls back to `pt`. Only 186 of 2,923 strings differ from `pt-BR`. App-side fix (a real `pt-PT.json` table, or stop offering Portuguese as "Portugal"); the site must not claim the app is in Portuguese (Portugal).
2. **GymLogger X, missing accents (P-G2):** 95 of 195 `creator_*` values and 46 strings overall (`Lesoes e Reabilitacao`, `Duracao da Sessao`, `Nao-binario`, `Ondulatoria`, `Estilo de Periodizacao`). Same defect in Spanish.
3. **GymLogger X, English left in:** store IAP `Support the developer`; `Apple Health` 11 strings; `Push / Pull`; `The Golden Six`; `Timer de descanso`; store name `Treino Tracker`.
4. **LiftLog, tier name mismatch (P-L1):** `Patrocinador` in the app against `Mecenas` on the store (Spanish glossary has the same kind of mismatch with `Bien`/`Bueno`).
5. **LiftLog, English fallbacks (P-L2):** 8 keys without `pt-PT` (`Average`, `Best`, `Best run`, `By month`, `By weekday`, `min`, `Sessions in run`, `Weekly avg`); the Siri hint tells Portuguese users to say English phrases; `Back` = `Voltar` where `Costas` is meant; 4 strings still say `CoreLift`; `A LiftLog` against `O LiftLog`.
6. **EarnLock, `Ajustes` / `Ecrã Bloqueado` / `Partilha com a família` / `fototeca`:** European-style wording problems (Apple pt-PT terms are `Definições`, `Ecrã de Bloqueio`, `Partilha em Família`, `Fotografias`); `cooldown`, `Shadow Mode` and `upgrade` left English; the three permission prompts and both Watch prompts are `needs_review`; display names missing in InfoPlist.
7. **MediaKit, `Livre` and `Assine o Pro` (P-M1):** bare `Free` is `Livre`; Brazilian imperative `Assine`; `descompactar`, `rastreamento`, `tela`; two trial words; `Make it Social` in two forms; `fototeca`; InfoPlist display name missing.
8. **Millrace:** `Proezas` for achievements; Title Case; `Combine` / `Anula a sua` formal among tu strings; store subtitle `uma só entrada` (English "one inlet").

Register
9. **No single register across the five apps.** tu: EarnLock (187 strings), LiftLog UI (116), Millrace (50). Formal 3rd person: MediaKit (186; 0 tu pronouns). Brazilian você: GymLogger X (241 strings with seu/sua/você). EarnLock and LiftLog contain formal pockets (permission prompts, Watch app, Siri answers, a few settings sentences). The site writes tu for EarnLock, LiftLog and Millrace quotes; quote MediaKit formally or paraphrase; do not quote GymLogger X UI strings as European Portuguese.

Terminology inconsistencies that decide site wording
10. Trial word (3 forms), Settings (`Definições` against `Ajustes`), goal (`objetivo` against `meta`), rest timer (`Cronómetro` against `Temporizador`), Family Sharing (3 spellings, Apple pt-PT is `Partilha em Família`), Apple Health (`Apple Saúde` / `app Saúde` / `Apple Health`), Lifetime (`Vitalício` in the UI, `compra única` on the store), Superset (`Superset` against `Supersérie`), Siri word order, Free (`Grátis`, `gratuito`, `Livre`).
11. English page words that have no Portuguese UI string: `Home screen` (the tab is `Hoje` in EarnLock), `Dynamic Island`, `Live Activity`, `Deep Focus`, MediaKit's menu bar, Millrace theme names.

Store listing notes
12. All five Portuguese store names differ from the English ones; EarnLock, LiftLog, MediaKit, Millrace and GymLogger X subtitles differ too. GymLogger X's subtitle `Treino de Força e Registo` is European (`Registo`) while its app is not. Millrace's category is `Tabuleiro` (Board), EarnLock `Produtividade`, GymLogger X and LiftLog `Saúde e fitness`, MediaKit `Utilitários`.
13. The lookup API's `formattedPrice` for the free download is `Gratuito`; the raw store page shows no price word. IAP names are quoted from the page; prices are reference only (master file is the source).
14. The seller name shown on the store pages is the owner's personal name and was not copied anywhere.

## Portuguese (Portugal) glossary, batch 3: mockly, observa, pawza, rightsplit, shogiful

Method (checked 2026-11-19). Read-only. Counts come from `python3 -I` scripts over every `.xcstrings` in each app's source folder (build, DerivedData and `.claude/worktrees` copies excluded; the RightSplit worktree `splitit/.claude/worktrees/widget-suite-v3/` holds stale duplicates of its four catalogs and was ignored): `strings` → key → `localizations` → `pt-PT` → `stringUnit` (state, value), `variations` (plural forms) or `stringSet`. Blank keys and `shouldTranslate: false` keys are excluded. "Translated" = state `translated`, a `variations` block, or a `stringSet`; `needs_review` is counted apart. The catalogs carry BOTH `pt-PT` and `pt-BR` (Mockly is the exception, see below). Values are copied verbatim from the `pt-PT` entries. App Store data comes from the iTunes lookup API (`country=pt&lang=pt_pt`) plus `curl -L` of `https://apps.apple.com/pt/app/id<ID>` with a Safari User-Agent and `Accept-Language: pt-PT`, parsed from the raw `serialized-server-data` JSON (HTTP 429 came back on the first passes; the pages were read after retries with pauses, and all five returned 200 in the end). Prices use a NO-BREAK SPACE before the euro sign and are reference only; `MASTER.md` / `MASTER-prices.csv` is the source for prices, platforms, trials and Family Sharing. The seller line on the store pages carries the owner's personal name and address; they are deliberately not copied.

**How pt-PT relates to pt-BR in these catalogs.** In each catalog the `pt-PT` value is identical to the `pt-BR` value for a large share of the strings: Observa 4661 of 7588 (61%), Pawza 646 of 1326 (49%), RightSplit 677 of 948 (71%), Shogiful 3380 of 3751 (90%). Where they differ, the pt-PT text is real European Portuguese (Definições, ecrã, registar, partilhar, guardar, eliminar, a + infinitive). Where they are identical, the text is neutral wording (many identical strings are fine, e.g. "Sono profundo") or Brazilian wording that leaked in (see flags). Treat Shogiful's pt-PT as a lightly edited Brazilian text, Observa's as mixed, and Pawza's and RightSplit's as largely European.

## Summary

| App | Main catalog `pt-PT` | Extensions / other catalogs | InfoPlist / permissions | Register | Verdict |
|---|---|---|---|---|---|
| Mockly | **No `pt-PT`, no `pt`.** Only `pt-BR`: 333/333 (100%) | none | InfoPlist 4/4 in `pt-BR` only | você / seu (pt-BR) | **no: the app is NOT in European Portuguese** (Brazilian only) |
| Observa | 6684/6684 have a value; 6672 translated (99.8%), 12 `needs_review` | Watch 477/477, Widgets 403/403, AppShortcuts 15/15 (10 translated, 5 `needs_review`) | app 5/5, watch 5/5 | formal (o seu, Desbloqueie, Veja, Toque); tu in 49 strings | **partial** (European base, Brazilian leaks) |
| Pawza | 1322/1322 (100%; key `%@` is format-only) | AppShortcuts 4/4; no widget catalog (widgets share the main one) | **none**: no InfoPlist catalog, camera and photo texts are English build settings | **tu** (150 strings), formal in 32 | **yes** (permission prompts in English) |
| RightSplit | 499/499 (100%) | Widgets 376/376, Share 3/3, SplititKit 65/65 | InfoPlist 5/5 | mixed: formal 98 strings, tu 21 | **yes** (mixed register) |
| Shogiful | 3751/3751 (100%) | none | InfoPlist 0/2 (English-only catalog; the app requests no permissions) | formal and Brazilian "você" (690 strings; 255 with "você"), tu in 56 | **partial** (about 90% identical to pt-BR) |

Register verdict for the site: no single register exists in the apps. Pawza says **tu**; Observa and RightSplit say **o seu / Desbloqueie / Veja** (formal, third person); Shogiful mixes Brazilian "você" with a few "tu" achievement strings; the Portuguese store descriptions of Observa, Pawza, RightSplit and Shogiful are all formal ("diz-lhe", "o seu", "Não precisa de registo"), with only a few stray tu forms. The Spanish site writes tu. Decide the Portuguese site's register explicitly (see Flags F1); quoting UI strings verbatim will not be consistent.

Cross-app flags for the whole batch are at the end ("Cross-app terms" and "Flags").

---

### 1. Mockly (`mockly`, source `AppScreenMaker/`, ID 6756589122, macOS)

### Portuguese coverage

- `Resources/Localizable.xcstrings`: 333 keys; `localizations` holds `de, en, es-ES, es-MX, fr, ja, ko, pt-BR, tr, zh-Hans`. **There is no `pt-PT` and no plain `pt`. Only `pt-BR`**, 333/333 translated (100%). `InfoPlist.xcstrings` 4/4 in `pt-BR` only. No other catalog, no `.lproj`, no `.strings` files. The Xcode project's `knownRegions` list only `en` and `Base` (catalog languages are not listed there).
- **The app is NOT in European Portuguese.** A Mac set to Portugal Portuguese gets either the Brazilian UI (if macOS falls back from pt-PT to pt-BR, not verified here) or English. Every Mockly string below is Brazilian Portuguese, not usable as pt-PT UI wording.
- `Models/SupportedLocales.swift` lists `pt` → ASC code `pt-BR` "Portuguese (Brazil)" and `pt-pt` → ASC code `pt-PT` "Portuguese (Portugal)". These are the **output** locales the app can build screenshots for in App Store Connect, not UI languages; a page can say Mockly exports pt-PT screenshots, but must not imply the interface is in pt-PT.
- Register of the pt-BR UI: **você / seu** (25 of 337 values with "você", "seu", "sua", "Obtenha"-style imperatives; 0 tu). Example: "Isso vai remover sua chave %@. Você pode adicionar uma nova a qualquer momento."
- Brazilian vocabulary (all of it, because the whole catalog is pt-BR): `Salvar` (8), `tela` in "capturas de tela" (5), `arquivo(s)` (8), "Excluir credenciais", "Provedor", "Câmera", "Borda", "Prancheta" (artboard), "Pacotes" (packs), "Gerenciar", "app" (12), "desenvolvedores".
- No extensions, no Siri phrases, no widgets, no permission prompts.
- **Verdict: app is in European Portuguese: no** (Brazilian Portuguese only).

Flags
- **M1 (locale):** pt-BR only. Anything the Portuguese site says about the interface must be written from the English UI, not from these strings. Add a `pt-PT` localization to the app, or accept that Portugal users see Brazilian text.
- **M2 (store name is Brazilian):** the Portuguese (Portugal) store name is "Mockly: Capturas de Tela". "Tela" is Brazilian; European Portuguese says "ecrã" ("capturas de ecrã"). The store description is entirely Brazilian too ("Você terminou o app", "capturas de tela", "SEU APP"; 24 você/seu hits, 0 tu). The store pt listing is therefore the pt-BR text served to the PT storefront.
- **M3 (translation packs):** the app sells translation credit packs ("Pacotes de tradução", "Créditos de tradução") next to bring-your-own-key. The Portuguese store page lists no in-app purchases, so the packs may not be live. The site only says "your own key". Check before the Portuguese page says anything about packs (same issue as the Spanish glossary, M2).
- **M4 (language count):** the Portuguese store subtitle is "50 Idiomas, Um Só Fluxo". The app itself ships in 10 languages. The site mixes "50 languages" and "39"; pick one number.
- **M5 (upload verb):** `Upload to App Store Connect` → "Enviar para o App Store Connect" (pt-BR "Enviar"; pt-PT would also say "Enviar" or "Carregar"; "Enviando capturas de tela…" uses the Brazilian gerund).
- **M6 (preset):** `Preset` → "Predefinição" (fine in both varieties; Spanish had "Ajuste").
- Missing in the UI: no strings for "Templates", "Bulk Import", "Panorama", "Realistic / Clay / UI Only", "Metal".

### Glossary

The table gives the pt-BR value (the only one that exists) and the European Portuguese equivalent a writer would use. The last column states whether the pt-BR value is acceptable in pt-PT as it stands.

| English term on site | English UI string (key) | pt-BR UI string (catalog, verbatim; there is no pt-PT) | Note |
|---|---|---|---|
| Upload to App Store Connect | `Upload to App Store Connect` | Enviar para o App Store Connect | acceptable; the pt-PT article is usually "a App Store Connect" or no article |
| App Store Connect credentials | `App Store Connect Credentials` | Credenciais do App Store Connect | `API Credentials` → "Credenciais da API"; `Delete Credentials` → "Excluir credenciais" (BR; pt-PT "Eliminar") |
| Issuer ID / Key ID / .p8 key | `Issuer ID` / `Key ID` / `Import .p8 File` | ID do emissor / ID da chave / Importar arquivo .p8 | "arquivo" is BR; pt-PT "ficheiro" |
| API key (bring your own) | `API Key` / `Own API Key` | Chave de API / Chave de API própria | |
| AI translation | `AI Translation` | Tradução com IA | feature name |
| AI Translate (button) | `AI Translate` | Traduzir com IA | |
| Translate All | `Translate All` | Traduzir tudo | |
| Bulk translations | `Bulk Translations` | Traduções em massa | |
| AI integration | `AI Integration` | Integração de IA | |
| Provider | `Provider` / `Default Provider` | Provedor / Provedor padrão | BR; pt-PT "Fornecedor" / "predefinido" |
| Localization panel | `Localizations` | Localizações | |
| Languages / locales | `Languages` / `Target Languages` / `Source Language` | Idiomas / Idiomas de destino / Idioma de origem | |
| Add language | `Add Language` | Adicionar idioma | |
| Linked to source | `Linked to source` | Vinculado à origem | "Vinculado" is BR-leaning; pt-PT "Ligado à origem" |
| Device models | `Devices` / `Device Style` / `Model` | Dispositivos / Estilo do dispositivo / Modelo | |
| Artboard | `Artboard` / `Artboards` | Prancheta / Pranchetas | Adobe pt-PT says "Mesa de trabalho" |
| Export | `Export` | Exportar | |
| Save images | `Save Images` | Salvar imagens | BR; pt-PT "Guardar imagens" |
| Text overlays / captions | `Text Block` / `Text Blocks` | Bloco de texto / Blocos de texto | |
| Copy Style | `Copy Style` | Copiar estilo | |
| CSV import/export | `Import CSV` / `Export CSV` | Importar CSV / Exportar CSV | |
| Do not translate | `Do not translate` | Não traduzir | |
| Pages / Layers / Background | `Pages` / `Layers` / `Background` | Páginas / Camadas / Fundo | |
| Gradient / Shadow / Border | `Gradient` / `Shadow` / `Border` | Gradiente / Sombra / Borda | "Borda" BR; pt-PT "Contorno" or "Limite" |
| Camera / Lighting | `Camera` / `Lighting` | Câmera / Iluminação | "Câmera" BR; pt-PT "Câmara" |
| Perspective / Orthographic | `Perspective` / `Orthographic` | Perspectiva / Ortográfica | pre-AO90 "Perspectiva" kept: pt-PT after the 1990 agreement writes "Perspetiva" |
| Projection | `Projection` | Projeção | |
| Rotation / Scale / Offset | `Rotation` / `Scale` / `Offset` | Rotação / Escala / Deslocamento | |
| Device overflow | `Device Overflow` | Estouro do dispositivo | "Estouro" BR; pt-PT "Excesso" / "Transbordo" |
| New Project | `New Project` | Novo projeto | |
| macOS Keychain | `Translation credits never expire. Your API key is stored in the macOS Keychain.` | Os créditos de tradução nunca expiram. Sua chave de API fica armazenada no Acesso às Chaves do macOS. | Keychain = "Acesso às Chaves" (BR macOS term; pt-PT macOS says "Acesso a Porta-chaves") |
| Translation packs (IAP) | `Translation Packs` / `Translation Credits` | Pacotes de tradução / Créditos de tradução | M3; `Buy More` → "Comprar mais" |
| Restore Purchases | `Restore Purchases` | Restaurar compras | |
| Powered by Claude | `Powered by Claude for high-quality screenshot localization.` | Com tecnologia Claude para localização de capturas de alta qualidade. | |
| Screenshots | `%lld screenshot%@ for %lld language%@` | %1$lld captura%2$@ de tela para %3$lld idioma%4$@ | "captura de tela" BR; pt-PT "captura de ecrã" |
| Templates / Render styles / Percentage layout | no UI string | no UI string | |

Paid tier names: Mockly is a paid app (one-time), with no tiers. The only purchase UI is the translation-pack sheet: "Pacotes de tradução", "Comprar mais", "Restaurar compras", "Pacotes avulsos. Sem assinaturas. Feito para desenvolvedores." (BR: "assinaturas", "desenvolvedores"; pt-PT "subscrições", "programadores"). No free trial.

### Portuguese App Store listing (https://apps.apple.com/pt/app/id6756589122, read 2026-11-19)

- Name: **Mockly: Capturas de Tela** (localized, Brazilian wording; English "Mockly: Screenshot Maker"; no space before the colon)
- Subtitle: **50 Idiomas, Um Só Fluxo** (English "50 Languages, One Workflow")
- Category: **Ferramentas de programação** (English "Developer Tools")
- Price: **14,99 €** (paid app, Mac only; no in-app purchases listed)
- Idiomas: "Português, Alemão, Chinês simplificado, Coreano, Espanhol, Francês, Inglês, Japonês, Turco" (9 listed; "Português" is the pt-BR localization)
- Compatibility: "Requer o macOS 14.0 ou posterior." Size 34,9 MB.
- Description register: você / seu (24 hits, 0 tu), Brazilian vocabulary.

---

### 2. Observa (`observa`, source `HealthLogger/`, ID 6757438990)

### Portuguese coverage

- Main `HealthLogger/Localizable.xcstrings`: 6684 keys, all 6684 with a `pt-PT` value; 6672 translated or plural variations (99.8%); 12 `needs_review` (the same 12 `insight_signal_*` labels as in Spanish). 41 locales; `pt-PT` and `pt-BR` both exist.
- Watch `ObservaWatch/Localizable.xcstrings`: 477/477 translated. Widgets `ObservaWidgets/Localizable.xcstrings`: 403/403 translated.
- `AppShortcuts.xcstrings`: 15/15 have a `pt-PT` value: 10 translated, 5 `needs_review` ("Registar o meu check-in matinal no ${applicationName}", "Registar água no ${applicationName}", "Qual foi a minha pontuação de sono no ${applicationName}?", "Qual é a minha prontidão no ${applicationName}?", and the `stringSet` "Devo treinar hoje segundo o ${applicationName}?" / "Devo treinar hoje no ${applicationName}?"). The Siri phrases address the app in the first person ("Posso treinar hoje segundo o ${applicationName}?", "Como dormi segundo o ${applicationName}?", "Como está a minha recuperação no ${applicationName}?"), so register does not matter for them.
- `InfoPlist.xcstrings` (app and watch) 5/5 each: `NSHealthShareUsageDescription` "O Observa lê os seus dados de saúde para mostrar análises de sono, coração, atividade e recuperação. Todos os dados são processados no seu dispositivo e nunca são carregados."; `NSHealthUpdateUsageDescription` "O Observa guarda registos relacionados com saúde na Apple Saúde para que os seus dados fiquem num só lugar."; `NSSiriUsageDescription` "O Observa usa a Siri para que possa pedir a sua pontuação de prontidão ou de sono e registar hidratação ou o check-in matinal por voz." All formal.
- Register: **formal (o seu / Desbloqueie / Veja / Toque)**. Of 7589 values: 1609 formal, 49 tu, 7 mixed in one string, 5924 neutral/impersonal. Formal imperatives dominate: "Desbloqueie" 121, "Veja" 74, "Toque" 31, "Acompanhe" 28, "Compreenda" 18, "Adicione", "Tente", "Observe". tu forms appear in about 22 main-catalog strings (the check-in and Siri replies "Feito — registei a tua manhã como %@.", "Começa a relaxar para a janela de sono desta noite.", "Toca para veres porquê e o que costuma ajudar.", "O que tornaria o Observa ideal para ti?", "Uma subscrição cobre todo o teu grupo da Partilha com a Família.", "Adiciona anotação da janela de ovulação ao contexto do ciclo") and 0 in the Watch and widget catalogs. Explicit "você" in 6 strings (Brazilian leak).
- Brazilian leaks (strings that read as pt-BR, not pt-PT): "você" 6 ("Você acorda cedo naturalmente e se sente mais alerta…"), "Seu/Sua" without article at the start of a sentence 60 ("Seu peso oscilou %@ esta semana.", "Sua pontuação de prontidão de %lld indica que seu corpo precisa de mais recuperação."), "estresse" 5 (pt-PT "stress" is used in 236 strings), "estágio(s)" 9 (`Sleep Stages` → "Estágios do sono" in the main catalog but "Fases do sono" in the widgets), "oxigênio" 4 ("Seu oxigênio no sangue de %@ está dentro da faixa normal…", next to pt-PT "oxigénio"), "faixa" 109 ("dentro da faixa de base", "faixa esperada"; pt-PT "intervalo", which the app also uses), "ótimo/ótima" 8, "teste grátis/gratuito" 2 (`Start Free Trial` → "Iniciar teste gratuito"; the same app's `onboarding_paywall_subheadline` says "avaliação gratuita"), the Brazilian progressive gerund "está recebendo", "estar contribuindo" 2 (pt-PT "está a receber", "estar a contribuir"), "celular" 1 (in "função celular", cellular, fine). The pt-PT markers are everywhere else: "ecrã" 13, "registar" 136, "partilh-" 29, "guardar" 23, "eliminar" 6, "Definições" 8, "a + infinitive" 154 ("A construir a sua referência"), "utilizador" 2, "equipa" 3.
- Spelling: one string has no accents or inverted forms, a real defect: `Your Sleep Quality score is built from four factors:…` → "A sua pontuacao de Qualidade do Sono e construida a partir de quatro fatores: Continuidade (35%) Quao ininterrupto foi o seu sono? Profundidade e Eficiencia (25%) Estava realmente a dormir? Restauracao (30%) O seu corpo recuper…" (same defect as the Spanish `es` text).
- **Verdict: app is in European Portuguese: partial.** The base is European (Definições, ecrã, registar, Apple Saúde in permissions), but about 90 strings carry clear Brazilian wording and the app mixes the two varieties inside single sentences.

**How the Portuguese UI labels HRV (house rule: Observa's HRV is SDNN from Apple Health, never RMSSD).**
- The UI term is **"VFC"** (keys `HRV` and `metric_label_hrv` → "VFC", about 205 strings; `Low HRV` → "VFC baixa"; `Advanced HRV` → "VFC avançada"); the long form is **"Variabilidade da frequência cardíaca"** (`Heart Rate Variability`, 11 strings). Gender is inconsistent: "da VFC" 7, "do VFC" 1 ("Vá além do VFC básico"). The English acronym **"HRV" survives in 19 strings** (`widget.title.hrv` → "HRV", `widget.desc.hrv` → "HRV com tendência de 7 dias.", "%@: %lld milissegundos HRV"; the store description also says "da HRV", "o HRV").
- **SDNN** appears only in explanatory sentences (3 strings): "O desvio padrão dos intervalos NN (SDNN) reflete a variabilidade global da sua frequência cardíaca de todas as fontes — simpáticas e parassimpáticas." and "Desvio padrão dos intervalos NN. Reflete a variabilidade global da frequência cardíaca de todas as fontes. Uma medida mais ampla que o RMSSD." There is no short "VFC (SDNN)" label.
- **RMSSD** appears in 19 strings, all in the Premium "Advanced HRV" feature (sleep-derived RMSSD estimates and the ECG path: `ECG-derived RMSSD & pNN50` → "RMSSD e pNN50 derivados do ECG", "Estado do RMSSD", "Tendências de RMSSD e equilíbrio autónomo", "O RMSSD mede a atividade do seu sistema nervoso parassimpático…", "A razão entre RMSSD e SDNN aproxima o equilíbrio…"). The headline HRV metric the app shows is "VFC" (SDNN from Apple Health). The site must never call the headline HRV RMSSD; RMSSD may only be named for the Advanced HRV / ECG feature.

Flags
- **O1 (tier name):** the app says **Premium** everywhere (paywall, Watch, widgets; one unrelated "Modo Pro"); the store IAPs are "Premium mensal / compra única / anual". Free tier is "Gratuito" (`onboarding_paywall_free`) or "nível gratuito".
- **O2 (readiness):** `Readiness` → "Prontidão" (162 strings), `Readiness Score` → "Pontuação de prontidão", `Moderate Readiness` → "Prontidão moderada", `Building baseline` Watch state "Prontidão %lld". Consistent (unlike Spanish).
- **O3 (baseline):** `Baseline` → "Linha de base" (149 strings) but "referência" in 38 (`Building your baseline` → "A construir a sua referência", `Building baseline` → "A construir referência", `Building Baseline` → "A criar linha de base", `edge_building_baseline_short` → "A construir linha de base"). Pick "linha de base".
- **O4 (sleep stages):** `Sleep Stages` → "Estágios do sono" (main catalog; "estágio" is Brazilian) but "Fases do sono" in the widgets (`widget.breakdown.sleepStages`) and 9 strings in all. `Core` (the Apple sleep stage) is translated three ways: "Essencial", "Principal %@" and "Sono básico baixo". Pick "fases do sono" and one word for Core.
- **O5 (resting heart rate):** "Frequência cardíaca de repouso" (66), "FC em repouso" and "FCR" (the `RHR` key); `Resting Heart Rate` is one string, "em repouso" appears in 84 sentences. Unit "bpm" kept (70); one `brpm` string reads "rpm".
- **O6 (training call):** the Watch complication and Siri use `Should I train today?` → "Devo treinar hoje?", complication title "Treinar hoje?", description "Treinar ou não hoje, num relance." The four verdicts `widget.train.verdict.*` are grammatically mixed: Push → "Intenso" (adjective), Maintain → "Manter" (infinitive), Recover → "Recupere" (formal imperative), Rest → "Descanso" (noun); the spoken forms are "Hoje parece um bom dia para forçar.", "…um dia de manutenção.", "…um dia mais leve.", "…um dia de descanso." The generic suggestions `readiness_suggestion_*` are "Treinar / Manter / Recuperar". Pick one form for the four calls before the page names them.
- **O7 (weekly reflection / check-in):** `Weekly Reflection` → "Reflexão Semanal"; `Morning Check-In` → "Check-in matinal" (23 strings, English kept) while the Siri permission and the Watch text also say "check-in". Consistent.
- **O8 (Apple Health name):** the UI keeps "Apple Health" (64 strings) but 6 strings and the HealthKit permission text say **"Apple Saúde"** ("Apple Saúde → Partilha → Apps") and 3 say "a app Saúde". One name needed.
- **O9 (best value / lifetime):** `Best Value` → "Melhor valor" (the pt-BR value is "Melhor custo-benefício"); `Lifetime` → "Vitalício"; `Unlock Lifetime Access` → "Desbloqueie Lifetime Access" (English left in, same as Spanish O8) next to `onboarding_paywall_lifetime_cta` → "Desbloquear acesso vitalício"; `Unlock HRV Trends` → "Desbloqueie HRV Trends". Imperative forms mix "Desbloqueie" (121), "Desbloquear" (20), "Desbloqueia" (a tu form, 0 here).
- **O10 (missing accents, real defect):** see Spelling above. Also `Your VO₂ Max…` explanation strings were checked in Spanish; not re-checked here.
- **O11 (store subtitle vs app):** the store subtitle says "Pontuação", the app "pontuação" (123). Consistent.
- **O12 (Siri `needs_review`):** 5 of 15 phrases are `needs_review`; Siri phrases need a final native check.
- `Moderate Debt` → "Défice moderado" while `Sleep Debt` → "Dívida de sono" (two words for one concept; the Spanish had the same split).
- "Check-in matinal", "Check-in" (Watch title) and "o teu check-in" show the tu/formal switch inside one feature.

### Glossary

| English term on site | English UI string (key) | pt-PT UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Sleep | `Sleep` | Sono | tab bar: Sleep, Recovery, Heart, Patterns, More |
| Tab: Recovery | `Recovery` | Recuperação | |
| Tab: Heart | `Heart` | Coração | |
| Tab: Patterns | `Patterns` | Padrões | |
| Tab: More | `More` | Mais | |
| HRV | `HRV` / `metric_label_hrv` | VFC | see HRV note; "HRV" left in 19 strings |
| Heart rate variability | `Heart Rate Variability` | Variabilidade da frequência cardíaca | |
| Advanced HRV | `Advanced HRV` | VFC avançada | RMSSD and pNN50 live here (ECG path), not in the headline metric |
| ECG-derived RMSSD & pNN50 | `ECG-derived RMSSD & pNN50` | RMSSD e pNN50 derivados do ECG | ECG path only |
| SDNN | `Standard Deviation of NN intervals (SDNN) reflects…` | O desvio padrão dos intervalos NN (SDNN) reflete a variabilidade global da sua frequência cardíaca… | explanatory text only |
| ECG | `ECG` / `ECG History` | ECG / Histórico de ECG | |
| Autonomic balance | `Autonomic Balance` | Equilíbrio autónomo | pt-BR "autônomo"; European "autónomo" |
| Sinus rhythm | `Sinus Rhythm` | Ritmo sinusal | |
| Readiness | `Readiness` | Prontidão | O2 |
| Readiness score | `Readiness Score` | Pontuação de prontidão | |
| Sleep Score | `Sleep Score` | Pontuação de sono | widget `widget.title.sleepScore` → "Pontuação do sono" (de / do) |
| Recovery score | `recovery score` | pontuação de recuperação | |
| Training call | `Should I train today?` | Devo treinar hoje? | Siri phrase "Posso treinar hoje segundo o ${applicationName}?" |
| Train today (Watch) | `watch.complication.train.title` | Treinar hoje? | tab `watch.tab.train` → "Treinar" |
| Push / Maintain / Recover / Rest | `widget.train.verdict.*` | Intenso / Manter / Recupere / Descanso | O6 |
| Why this score? | `why.action.title` | Porquê esta pontuação? | |
| Building your baseline | `Building your baseline` | A construir a sua referência | O3 |
| Resting heart rate | `Resting Heart Rate` / `RHR` | Frequência cardíaca de repouso / FCR | O5 |
| Sleep efficiency | `Sleep Efficiency` | Eficiência do sono | |
| Sleep stages | `Sleep Stages` | Estágios do sono | O4; widgets "Fases do sono" |
| Deep sleep / REM / Core / Awake | `Deep Sleep` / `REM Sleep` / `Core` / `Awake` | Sono profundo / Sono REM / Essencial / Acordado | Core inconsistent (O4) |
| Sleep debt | `Sleep Debt` | Dívida de sono | `Moderate Debt` → "Défice moderado" |
| Adjust Sleep | `Adjust Sleep` | Ajustar sono | `Sleep Source` → "Fonte de sono" |
| Heart-rate dip | `Nocturnal Dip` | Queda noturna | pt-PT "noturna" is acceptable |
| Heart rate recovery | `Heart Rate Recovery` | Recuperação da frequência cardíaca | |
| Stress | `Stress` | Stress | pt-BR "Estresse"; 5 Brazilian leaks "estresse" remain |
| Today's Plan | `Today's Plan` | Plano de hoje | |
| Functional Age | `Unlock Functional Age` | Desbloquear idade funcional | label "idade funcional" |
| Chronotype | `Chronotype Analysis` | Análise de cronotipo | |
| Training load | `Training Load` | Carga de Treino | capital T inconsistent with sentence case elsewhere |
| Training Status / Load Trends | `Training Status` / `Load Trends` | Estado de Treino / Tendências de carga | pt-BR "Status de Treino" |
| Strain | `Strain` | Esforço | |
| Workouts / Personal Records / Workout Replay | `Workouts` / `Personal Records` / `Workout Replay` | Treinos / Recordes pessoais / Replay do Treino | "Recordes" is BR-leaning; pt-PT "Recordes" is also used |
| Energy | `Energy` / `Active Energy` | Energia / Energia ativa | |
| Personal baseline | `Baseline` / `Your baseline` | Linha de base / A sua linha de base | O3 |
| Confidence | `Confidence` | Confiança | |
| Insight cards | `Daily insights` / `Insights` | Análises diárias / Análises | widget `Insight` → "Análise"; `widget.title.smartInsight` → "Observação inteligente" |
| Weekly reflection | `Weekly Reflection` | Reflexão Semanal | |
| Long-term trends | `Long-Term Trends` | Tendências de longo prazo | |
| Morning check-in | `Morning Check-In` | Check-in matinal | complication title "Check-in" |
| Hydration | `Hydration` | Hidratação | |
| Apple Watch complications | `watch.complication.*.title` | Check-in / Hidratação / Métrica / Hoje / Treinar hoje? | descriptions: "O seu check-in matinal, a um toque.", "A água de hoje em relação ao seu objetivo.", "Treinar ou não hoje, num relance." |
| Widgets | `widget.title.*` | Central de saúde / Sinais cardíacos / Contexto diário / Pontuação de recuperação / Fases do sono / Dívida de sono / Fatores de stress | Config names Focus, Trend, Insight: "Foco", "Tendência", "Análise" |
| Widget bands | `widget.band.*` | Muito baixo / Baixo / Moderado / Bom / Alto | `widget.bandStatus.*` → "BAIXO" / "RAZOÁVEL" / "BOM" / "EXCELENTE" |
| Apple Health | `Apple Health` (in sentences) | Apple Health | O8: also "Apple Saúde", "app Saúde" |
| Premium tier | `Premium` / `Upgrade to Premium` / `Unlock Premium` | Premium / Atualizar para Premium / Desbloquear Premium | O1 |
| Monthly / Yearly / Lifetime | `Monthly` / `Yearly` / `Lifetime` | Mensal / Anual / Vitalício | |
| Unlock lifetime | `Unlock Lifetime Access` / `onboarding_paywall_lifetime_cta` | Desbloqueie Lifetime Access / Desbloquear acesso vitalício | O9 |
| Start free trial | `Start Free Trial` / `Start %@ Free Trial` | Iniciar teste gratuito / Iniciar %@ de teste grátis | "teste" BR-leaning; the app also says "avaliação gratuita" and "7 dias grátis" (`onboarding_paywall_free_trial_badge`) |
| Start plan | `Start Yearly Plan` | Iniciar plano anual | `onboarding_paywall_monthly_cta` → "Iniciar plano mensal" |
| Restore Purchases | `Restore Purchases` | Restaurar compras | |
| Free | `Free` / `onboarding_paywall_free` | Gratuito | |
| Best value | `Best Value` / `Best value` | Melhor valor | O9 |
| No subscription line | `onboarding_paywall_lifetime_disclosure` | Compra única. Sem subscrição. | pt-PT "subscrição" (store IAP uses "compra única") |
| Cancel anytime | `Cancel anytime.` | Cancele a qualquer momento. | formal |
| Family Sharing | `One subscription covers your whole Family Sharing group.` | Uma subscrição cobre todo o teu grupo da Partilha com a Família. | tu; Apple's pt-PT term is "Partilha em Família" (F5) |
| Menstrual cycle | `Cycle Context` / `Menstrual Cycle` | Contexto do ciclo / Ciclo menstrual | the English site page does not cover cycle tracking |

Paid tier names as the Portuguese UI shows them: **Premium**, labels **Mensal / Anual / Vitalício**, "Melhor valor", "Desbloquear Premium", "Atualizar para Premium", "Restaurar compras", "Iniciar teste gratuito", "Compra única. Sem subscrição.", "Cancele a qualquer momento." The store IAP names are "Premium mensal", "Premium anual", "Premium compra única" (UI says "Vitalício") and the tip "Apoiar o programador". A week of full access is given first (`onboarding_paywall_free_trial_badge` "7 dias grátis").

### Portuguese App Store listing (https://apps.apple.com/pt/app/id6757438990, read 2026-11-19)

- Name: **Observa: VFC & Recuperação** (English "Observa: HRV & Recovery Score"; the Portuguese name says "VFC"; no space before the colon)
- Subtitle: **Sono, Ciclo, Coach & Pontuação**
- Category: **Saúde e fitness** (English "Health & Fitness")
- Price: Gratuito. In-app purchases as shown: Premium mensal **3,99 €**, Premium compra única **59,99 €**, Premium anual **24,99 €**, Apoiar o programador **1,00 €**
- Idiomas: Português plus 33 others (34 listed)
- Compatibility: iOS 17.6, iPadOS 17.6, macOS 14.6 (M1), visionOS 1.3 and watchOS 10.0 (not re-read in full). Size 92,7 MB.
- Description register: **formal** ("diz-lhe quão preparado está", "o seu sono", "Toque em «Porquê?»", "pergunte «Devo treinar hoje?»"), 20 formal hits, 0 tu, no Brazilian words. It uses "HRV" with the article ("da HRV") while the name and the app say "VFC".

---

### 3. Pawza (`pawza`, source `PetCare/`, ID 6773507068)

### Portuguese coverage

- `PetCare/Localizable.xcstrings`: 1323 keys, 1322 with `pt-PT`, all translated (the one missing key is the format-only `%@`). 51 locales; `pt-PT` and `pt-BR` both exist. The widget target shares this catalog (no catalog of its own).
- `AppShortcuts.xcstrings`: 4/4 translated: "Registar ${kind} no ${applicationName}", "Registar o humor de ${pet} no ${applicationName}", "Registar cuidado de ${pet} no ${applicationName}", "Registar cuidado no ${applicationName}".
- **No `InfoPlist.xcstrings`.** The camera and photo-library permission texts are `INFOPLIST_KEY_NSCameraUsageDescription` / `INFOPLIST_KEY_NSPhotoLibraryUsageDescription` build settings in English only ("Pawza uses your camera to scan vet documents and take photos of your pets.", "Pawza needs photo access to import pictures of your pets and their documents."). The project's `knownRegions` include `pt-PT` and `pt-BR`; a Portuguese user still sees English prompts.
- Register: **tu** in Pawza's own text. Of 1332 values: 150 tu, 32 formal, 2 mixed in one string, 1148 neutral. tu imperatives: 71 ("Adiciona primeiro um animal", "Adiciona um nome para guardar.", "Escolhe o ícone da app…", "Importa…", "Regista…"); formal imperatives 23 ("Crie um resumo de saúde em PDF para partilhar", "Verifique novamente — a caligrafia é difícil de ler", "Ative o Apple Intelligence nas Definições…", "Introduza um número", "Escolha o animal e o tipo de cuidado…", "Tente novamente dentro de alguns minutos"). Two strings switch inside one sentence: "Adiciona o teu primeiro animal para começares a acompanhar a sua saúde." (tu then "a sua" for the animal; acceptable) and "Regista uma entrada de imediato. Toque sem soltar…". The store description, in contrast, is **formal** ("Doses, refeições e consultas do seu animal", "Toque em «Dado»", "lembra-o de repor"; 9 formal hits, 1 stray tu "repara").
- Brazilian vocabulary: almost none. "foto/fotos" 51 (pt-PT also uses "foto", fine; "fotografia" appears in `Profile photo` → "Fotografia de perfil"), "ótimo" 1, "faixa" 1, "tamanho" 5 (fine), "teste grátis/gratuito" 4 ("7 DIAS DE TESTE GRÁTIS", "Iniciar teste gratuito de 7 dias"; BR-leaning "teste"). pt-PT markers: "Definições" 13, "ficheiro" 15, "guardar" 48, "eliminar" 28, "partilh-" 13, "registar" 143, "ecrã" 1, "telemóvel" 3, "digitalizar" (scan), "Subscrever", "Humor", "Brevemente".
- Not-quite: `Apple Intelligence` is masculine in some strings ("O Apple Intelligence está ocupado", "Preencher com o Apple Intelligence") and feminine in others ("A Apple Intelligence acabou de te poupar 10 minutos", "Resumo da Apple Intelligence", store description "a Apple Intelligence preenche").
- **Verdict: app is in European Portuguese: yes** (permission prompts in English).

Flags
- **P1 (permission prompts):** camera and photo texts are English build settings; there is no `InfoPlist.xcstrings` (same defect in German, French and Spanish).
- **P2 (scan):** `Scan` → "Digitalizar" (and "digitalização/digitalizações"), consistent and European (pt-BR says "Escanear"; the store text says "Fotografe um documento"). Matches RightSplit "Digitalizar recibo".
- **P3 (records):** `Records` → "Registos" (143 "registar/registo" strings); the sitter document is a "Ficha do cuidador" (pt-BR "Ficha do pet sitter"); the care log is "Diário de cuidados" (Spanish "Registro de cuidados").
- **P4 (best value):** `Best value` → "Mais vantajoso" (Observa and RightSplit say "Melhor valor").
- **P5 (upgrade verb):** `Upgrade to Pawza Pro` → "Mudar para o Pawza Pro" next to `Unlock Pawza Pro` → "Desbloquear o Pawza Pro" and `Unlock AI auto-fill` → "Desbloqueia o preenchimento automático com IA" (tu). The brand takes an article ("o Pawza Pro", "o Pawza"), unlike Observa.
- **P6 (free):** `Free` → "Grátis" (Observa uses "Gratuito").
- **P7 (trial):** `Start 7-day free trial` → "Iniciar teste gratuito de 7 dias"; banner "7 DIAS DE TESTE GRÁTIS".
- **P8 (mood):** `Mood` → "Humor". **P9 (due):** `Due` → "Prazo", `Upcoming` → "Brevemente", `Overdue` → "Em atraso". **P10 (dog):** `Dog` → "Cão" (pt-BR "Cachorro"); store name "Saúde de Cães e Gatos".
- **P11 (Apple Intelligence gender):** see above.

### Glossary

| English term on site | English UI string (key) | pt-PT UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Pets | `Pets` | Animais | pt-BR "Pets" |
| Tab: Reminders | `Reminders` | Lembretes | |
| Tab: Settings | `Settings` | Definições | pt-BR "Ajustes" |
| Pet / Add pet | `Pet` / `Add Pet` | Animal / Adicionar animal | |
| Health records | `Records` | Registos | P3 |
| Vaccinations | `Vaccinations` / `Vaccines` | Vacinas / Vacinas | |
| Medications | `Medications` / `Medication` | Medicamentos / Medicamento | |
| Doses | `Doses` | Doses | |
| Vet visits | `Vet visits` | Consultas veterinárias | |
| Vet | `Vet` | Veterinário | `Emergency vet` → "Veterinário de urgência" |
| Weight / weight alerts | `Weight` / `Weight trend alerts` | Peso / Alertas de tendência do peso | |
| Symptoms | `Symptoms` | Sintomas | `Log Symptom` → "Registar sintoma" |
| Care log | `Care log` / `Log care` | Diário de cuidados / Registar cuidado | P3 |
| Walks | `Walks` | Passeios | |
| Mood | `Mood` | Humor | P8 |
| Feeding | `Feeding` / `Log food` | Refeições / Registar refeição | `Dry food` → "Ração seca" |
| Document scanning | `Scan a vet document` / `Scan` | Digitalizar um documento veterinário / Digitalizar | P2 |
| Import past records | `Import past records` | Importar registos anteriores | |
| AI auto-fill | `Unlock AI auto-fill` | Desbloqueia o preenchimento automático com IA | |
| AI summaries | `AI Summaries` / `AI summaries for every record` | Resumos com IA / Resumos com IA para cada registo | |
| Apple Intelligence | `Apple Intelligence summary` / `Fill with Apple Intelligence` | Resumo da Apple Intelligence / Preencher com o Apple Intelligence | P11 |
| Vet-visit PDF | `Vet Visit PDF` / `Vet visit PDF generator` | PDF da consulta veterinária / Gerador de PDF de consulta veterinária | |
| Since last vet visit | `Since last vet visit` | Desde a última consulta veterinária | |
| Emergency Card | `Emergency Card` | Cartão de emergência | `Emergency Info` → "Informações de emergência" |
| Lost Pet Kit | `Lost Pet Kit` / `Lost Pet Poster` | Kit de animal perdido / Cartaz de animal perdido | |
| ID tag / QR | `ID Tag QR Codes` | Códigos QR para a medalha | tag = "medalha" |
| Sitter Pack | `Sitter Pack` | Ficha do cuidador | `Make a sitter pack` → "Criar ficha do cuidador" |
| Photo gallery | `Unlimited photo gallery` | Galeria de fotos ilimitada | |
| Unlimited pets and scans | `Unlimited pets and scans` | Animais e digitalizações ilimitados | |
| Free / Pro | `Free` / `Pro` / `Pawza Pro` | Grátis / Pro / Pawza Pro | P6 |
| Unlock Pro | `Unlock Pawza Pro` / `Upgrade to Pawza Pro` | Desbloquear o Pawza Pro / Mudar para o Pawza Pro | P5 |
| Monthly / Yearly / Lifetime | `Monthly` / `Yearly` / `Lifetime` | Mensal / Anual / Vitalício | `Pro (Lifetime)` → "Pro (vitalício)", `Buy Lifetime — %@` → "Comprar vitalício — %@" |
| 7-day free trial | `Start 7-day free trial` | Iniciar teste gratuito de 7 dias | P7 |
| Subscribe | `Subscribe` | Subscrever | pt-BR "Assinar" |
| Best value | `Best value` | Mais vantajoso | P4 |
| Due / Upcoming | `Due` / `Upcoming` | Prazo / Brevemente | P9 |
| iCloud sync | `iCloud Sync: up to date.` | Sincronização do iCloud: atualizada. | |
| Syncing with iCloud | `Syncing with iCloud...` | A sincronizar com o iCloud… | |
| Restore Purchases | `Restore Purchases` | Restaurar compras | |
| Pro feature lock | `%@ is a Pro feature` | Funcionalidade Pro: %@ | |

Paid tier names as the Portuguese UI shows them: **Pawza Pro** (also "Pro"), labels **Mensal / Anual / Vitalício**, "Iniciar teste gratuito de 7 dias", "Restaurar compras", "Subscrever", "Mais vantajoso", "Funcionalidade Pro: %@". Store IAP names: "Pawza Pro anual", "Pawza Pro mensal", "Pawza Pro compra única".

### Portuguese App Store listing (https://apps.apple.com/pt/app/id6773507068, read 2026-11-19)

- Name: **Pawza: Saúde de Cães e Gatos** (English "Pawza: Pet Health & Records"; no space before the colon)
- Subtitle: **Boletim, vacinas e lembretes** ("boletim" is the Portuguese word for the vaccination booklet)
- Category: **Estilo de vida** (English "Lifestyle")
- Price: Gratuito. In-app purchases as shown: Pawza Pro anual **22,99 €**, Pawza Pro mensal **2,99 €**, Pawza Pro compra única **44,99 €**
- Idiomas: Português plus 43 others (44 listed)
- Compatibility: iOS 17.6 (iPhone), iPadOS 17.6, macOS 14.6 (M1). Size 39,7 MB.
- Description register: formal (9 hits "seu"/"tem", "lembra-o"); one stray tu imperative ("repara em tudo"). Uses "ecrã", "stock", "Controlar o stock".

---

### 4. RightSplit (`rightsplit`, source `splitit/`, ID 6757268612)

### Portuguese coverage

- Main `splitit/Localizable.xcstrings`: 499 keys, all 499 with `pt-PT` (plural variations included; 100%). 40 locales; `pt-PT` and `pt-BR` both exist.
- Widgets `splititWidgets`: 376/376. Share extension `splititShare`: 3/3. SplititKit package (`Sources/SplititKit/Resources`): 65/65.
- `InfoPlist.xcstrings`: 5/5 in `pt-PT`: `CFBundleDisplayName` "RightSplit", `CFBundleName` "splitit", camera "RightSplit usa a câmara para digitalizar recibos de restaurantes e dividir a conta.", contacts "RightSplit acede aos contactos para adicionar pessoas ao dividir a conta.", photo-library add "RightSplit guarda uma imagem na fototeca apenas quando o escolher." (formal "o escolher"). No `NSPhotoLibraryUsageDescription`.
- Register: **mixed**. Of 1022 values: 98 formal, 21 tu, 1 mixed in one string, 902 neutral. Formal imperatives 63 ("Adicione pelo menos 2 pessoas para dividir a conta", "Toque para enviar um lembrete.", "Abra", "Introduza", "Digitalize", "Agrupe", "Divida", "Escolha", "Arraste", "Feche o RightSplit no seletor de apps"); tu imperatives 16 ("Adiciona este cartão ao widget Paga-me.", "Toca para o registar e dividir.", "Abre o RightSplit pronto para dividir a conta.", "Começa", "lembra-te", "A tua parte da conta"). The widget catalog switches within itself ("Abre o RightSplit no seu Cartão Pay-Me." beside "Open RightSplit to start" → "Abra o RightSplit para começar"). The store description is formal ("Digitalize… envie a cada um a sua parte", "Não precisa de registo").
- Brazilian vocabulary: very little. "gorjeta" 23 (the correct word in Portugal too; "propina" in Portugal means tuition fee, never use it for a tip), "foto" 4, "conta" 25 (bill; fine), "assinalado" (checked, not "assinatura"). Brazilian forms found: "insira os itens manualmente" (`Try taking a clearer photo with good lighting,\nor enter items manually`, pt-PT "introduza"; the same app says "Introduza" elsewhere), "Seguir pagamentos" (`Track payments`, a calque, European "Acompanhar pagamentos"), "Enviar feedback" (English kept; Spanish says "comentarios"), "Divisão de bolso" (`Pocket Split`, literal). pt-PT markers: "ecrã" 6, "partilh-" 25, "guardar" 14, "eliminar" 2, "Definições" 3, "utilizador" 2 ("nome de utilizador"), "área de transferência" 3, "fototeca", "câmara", "contactos", "Digitalizar".
- **Verdict: app is in European Portuguese: yes** (register mixes formal and tu).

Flags
- **R1 (split):** "Dividir/divisão" throughout (`Split Receipt` → "Dividir recibo", `Split by items` → "Dividir por artigos", `Split Complete` → "Divisão concluída", `Pocket Split` → "Divisão de bolso"); "partilhar" is only share (`Text / WhatsApp share` → "Partilhar SMS / WhatsApp"; the site says iMessage/WhatsApp). `Shared dishes` → "Pratos partilhados". `Everyone's settled` → "Todos liquidados — não são necessárias transferências."
- **R2 (receipt vs bill):** `Receipt` → "Recibo" (57 strings), `Bill` → "Conta" (the restaurant bill; 25 "conta" strings). The store subtitle says "Recibo & despesas em grupo", consistent with the app (unlike the Spanish "ticket").
- **R3 (item word):** `Split by items` → "Dividir por artigos", `Add shared item` → "Adicionar artigo partilhado" (European "artigo"; pt-BR "item").
- **R4 (tax):** `Tax` → "Imposto" (1 string). A Portuguese restaurant bill carries "IVA"; "Imposto" reads generic. Check the Portuguese site copy.
- **R5 (best value):** `Best value` → "Melhor valor" (pt-BR "Melhor custo-benefício").
- **R6 (spaces / trips):** `Spaces` → "Espaços" (`New space` → "Novo espaço"), `Trips` → "Viagens". `Pinned space was removed` → "Espaço afixado removido".
- **R7 (settle):** `Settlement` → "Acerto", `Settle in` → "Acertar em", but `Everyone's settled` → "Todos liquidados"; `owes` → "paga", `owed` → "recebe", `Owed` → "Devido" (the heading "Devido" reads as "due", the opposite sense; check where it is shown).
- **R8 (tier name):** `Pro+` everywhere; `Pro+ Lifetime` → "Pro+ Vitalício" (capital V, differs from "vitalício" lower case in Pawza).
- **R9 (trial):** `%lld-day free trial` → "%lld dias grátis" (no "teste"). `paywall.trialThenBilled` → "%@ de teste, depois %@". Other tiers say "teste gratuito"; the trial wording differs per app (see Cross-app terms).
- **R10 (Pay Me):** `Pay Me` → "Paga-me" (tu; pt-BR "Me Pague"), `Pay-Me Card` → "Cartão Pay-Me", `Set up Pay Me` → "Configurar Pay Me", the per-person button is "Paga-me". The button is a tu command while most of the app is formal.
- **R11 (feedback):** `Send feedback` → "Enviar feedback" (English kept).
- `Free` → "Grátis". `Restore` → "Restaurar". `Track payments` → "Seguir pagamentos" (calque).

### Glossary

| English term on site | English UI string (key) | pt-PT UI string (verbatim) | Note |
|---|---|---|---|
| Scan receipt | `Scan Receipt` / `Scan receipt` | Digitalizar recibo | pt-BR "Escanear recibo"; R2 |
| Receipts | `Receipts` / `Receipt` | Recibos / Recibo | |
| Receipt language | `Receipt Language` | Idioma do recibo | |
| Item-level splits | `Split by items` | Dividir por artigos | R3 |
| Shared dishes | `Shared dishes` / `Add shared item` | Pratos partilhados / Adicionar artigo partilhado | |
| Equal splitting | `Equal splits & tip` | Divisão igual e gorjeta | R1 |
| Per person | `Per person` / `Adjust per person` | Por pessoa / Ajustar por pessoa | |
| Tip | `Tip` / `Tip included` | Gorjeta / Gorjeta incluída | correct pt-PT word |
| Tax | `Tax` | Imposto | R4 |
| Subtotal / Total | `Subtotal` / `Total` | Subtotal / Total | |
| Fair rounding | `Round fairly` | Arredondar com justiça | |
| Send totals / payment requests | `Send Payment Requests` | Enviar pedidos de pagamento | `Payment reminder` → "Lembrete de pagamento" |
| Pay-Me card / pay link | `Pay Me` / `Pay-Me Card` | Paga-me / Cartão Pay-Me | R10; link text "Adicionamos automaticamente valor, moeda e uma nota ao link." (pt-PT "ligação" is the formal word; the app says "link") |
| Payment methods | `Add payment method` / `Set up a payment handle first` | Adicionar método de pagamento / Configure primeiro uma forma de pagamento | "handle" = "método" or "forma de pagamento" |
| Text / WhatsApp share | `Text / WhatsApp share` | Partilhar SMS / WhatsApp | |
| Receipt photo | `Receipt photo` | Foto do recibo | `Take a photo of your restaurant bill` → "Tire uma foto da conta do restaurante" |
| Enter manually | `Enter Items Manually` | Introduzir artigos manualmente | `Add item manually` → "Adicionar artigo manualmente" |
| Paid | `Paid` | Pago | |
| Spaces | `Spaces` / `New space` | Espaços / Novo espaço | R6 |
| Trips | `Trips` / `Trips & shared expenses` | Viagens / Viagens e despesas partilhadas | |
| Balances / settle-up | `Balance` / `Settlement` / `Settle in` | Saldo / Acerto / Acertar em | R7 |
| Split history | `History` / `Unlimited split history` | Histórico / Histórico de divisões ilimitado | |
| Templates | `Templates` / `Split template` | Modelos / Modelo de divisão | pt-BR also "Modelos" |
| People | `People` | Pessoas | |
| Currency | `Currency` | Moeda | `Language & Currency` → "Idioma e moeda" |
| Free | `Free` | Grátis | |
| Pro+ | `Pro+` / `Unlock Pro+` / `Upgrade to Pro+` | Pro+ / Desbloquear Pro+ / Atualizar para Pro+ | |
| Pro+ yearly | `Pro+ Yearly` | Pro+ Anual | |
| Pro+ lifetime | `Pro+ Lifetime` / `Unlock Pro+ Lifetime` | Pro+ Vitalício / Desbloquear Pro+ Vitalício | R8; `Unlock Pro+ — Pay once` → "Desbloquear Pro+ — Pagamento único" |
| Free trial | `%lld-day free trial` | %lld dias grátis | R9 |
| Best value | `Best value` | Melhor valor | R5 |
| No subscriptions | `No subscriptions. No renewals.` | Sem subscrições. Sem renovações. | |
| Auto-renew line | `Auto-renews yearly until canceled.` | Renova automaticamente todos os anos até ser cancelado. | |
| Restore Purchases | `Restore Purchases` | Restaurar compras | `Pro+ restored successfully!` → "Pro+ restaurado com sucesso!" |

Paid tier names as the Portuguese UI shows them: **Pro+** (no plain "Pro"), **Pro+ Anual**, **Pro+ Vitalício**, "Desbloquear Pro+", "Atualizar para Pro+", "Pagamento único", "Restaurar compras", "Sem subscrições. Sem renovações.", "Renova automaticamente. Cancele quando quiser." Store IAP names: "RightSplit Pro+ Compra única", "RightSplit Pro+ anual".

### Portuguese App Store listing (https://apps.apple.com/pt/app/id6757268612, read 2026-11-19)

- Name: **RightSplit: Dividir e Gorjeta** (English "RightSplit: Bill Splitter Tip"; no space before the colon)
- Subtitle: **Recibo & despesas em grupo** (English "Scan & share group expenses")
- Category: **Utilitários** (English "Utilities")
- Price: Gratuito. In-app purchases as shown: RightSplit Pro+ Compra única **8,99 €**, RightSplit Pro+ anual **4,99 €**
- Idiomas: Português plus 33 others (34 listed)
- Compatibility: iPhone iOS 17.0, Mac macOS 14.0 (M1); no iPad line in the compatibility block (the Spanish glossary reads the same). Size 18,2 MB.
- Description register: formal ("Digitalize, toque em quem comeu o quê", "Não precisa de registo", "NO SEU IPHONE"; 18 formal hits, 0 tu).

---

### 5. Shogiful (`shogiful`, source `shogi/`, ID 6761656926)

### Portuguese coverage

- `Localization/Localizable.xcstrings`: 3751 keys, all 3751 with `pt-PT`, all translated (100%). 39 locales; `pt-PT` and `pt-BR` both exist and **are identical for 3380 of 3751 strings (90%)**. Most keys are semantic (`tab.play`, `paywall.plan.monthly`), so look up by key, not English text.
- `InfoPlist.xcstrings`: 0/2 (only `CFBundleDisplayName` "Shogiful" and `CFBundleName` "shogi", English-only; the app requests no permissions).
- No extensions or Siri phrases.
- Register: **formal with Brazilian forms**. Of 3751 values: 690 formal, 56 tu, 10 mixed in one string, 2995 neutral. Explicit "você" in 255 strings ("Você jogou", "Você encontrou seus primeiros erros", "Você concluiu os problemas gratuitos de hoje", "Tudo o que você precisa…"), "seu/sua/seus/suas" in 451 strings ("Seu lance", "seus erros", "suas notas"; Brazilian use without the article), formal imperatives about 98 ("Jogue uma partida…", "Toque em Analisar para avaliar seus lances com o YaneuraOu.", "Crie o hábito: confira todos os xeques"). tu forms are concentrated in the Game Center achievements and lessons, about 26 strings ("Analisa a tua primeira partida.", "Concluíste o escalão Avançado.", "Joga entre as 5 e as 7 da manhã.", "Revê vinte e cinco detalhes de erros.", `komaochi.starter.*.teaching`, "Gote não tem bispo — abre cedo a diagonal do teu bispo e desenvolve em torno do seu…"). The store description is formal pt-PT ("o seu treinador pessoal de shogi", "a correr no seu iPhone", "Há 40 adversários entre si e o topo da escada"; 12 formal hits, 0 tu).
- Brazilian vocabulary: **"lance" for move in 331 strings** ("Melhor lance", "Ótimo lance", "Seu lance"; the Portuguese chess and shogi word in Portugal is "lance" too but "jogada" is the common one; the glossary should pick one), "colocação/colocar" for drops (306 strings: "Exercícios de colocação", "Error de colocação" in Spanish; `board.drop.hint` → "Colocar %1$@ em %2$@"), "Trilha tsume" (`Tsume Trail`; pt-PT "percurso"), "Ateliê de castelos" (pt-PT "Ateliê" is also used), "arquivo" (4; `Codificação de arquivo não compatível`), "Salvar/salve" (13), "Excluir" (1), "teste grátis" (2: "Iniciar teste grátis", "Teste grátis de %lld dias"), "gerenciar" 1 ("Gerenciado pelo organizador da família"), "fato", "ótimo" 1, "rede" ("rede de mate" is a net, fine), the progressive gerund "está avaliando" is absent but "A analisar sua partida" mixes a European gerund form with a Brazilian possessive without article, "Não consegue" etc. pt-PT markers also present: "ficheiro" 3, "partilh-" 8, "guardar" 14, "eliminar" 2, "Definições" 11, "A avaliar", "está a avaliar" 17, "registar" 5, "ecrã" 0 (no screen word needed).
- **Verdict: app is in European Portuguese: partial.** 90% of the strings are identical to the Brazilian catalog, 255 strings say "você", and several visible labels are Brazilian ("MELHOR CUSTO-BENEFÍCIO", "Trilha tsume", "Gerenciado", "Salvar"). The store page text is European.

**Portuguese shogi terms the app uses**
- Pieces (keys `piece.*`): `King` → "Rei", `Rook` → "Torre", `Bishop` → "Bispo", `Gold General` → "General de ouro", `Silver General` → "General de prata", `Knight` → "Cavalo", `Lance` → "Lança", `Pawn` → "Peão". Promoted: `Dragon` (`piece.rook.promoted`) → "Dragão", `Horse` (`piece.bishop.promoted`) → "Bispo promovido".
- Promotion: `Promote?` (`promotion.title`) → "Promover?", `Promote` (`promotion.promote`) → "Promover" (the Spanish uses "Promocionar"). Pieces in hand: `board.hand.piece %lld` → "Peça capturada — %lld na mão", `interaction.accessibility.goteHand` → "Peças capturadas do adversário", `senteHand` → "Suas peças capturadas" (Brazilian "Suas").
- Drops: "colocação" / "colocar", plus two odd words: `gc.achievement.drop_checkmate.locked` → "Vence com um largamento que dá xeque-mate." and the achievement `gc.achievement.drop_checkmate.title` → "Descer o Pano". "Largamento" is not a Portuguese shogi term; the drop word the site should use is "colocação".
- Rules and game words: `Checkmate` → "Xeque-mate" (`game.result.checkmate`), `Check!` → "Xeque!" (`game.status.check`), `Resign` → "Desistir" (`game.resign`), result "Desistência", `Draw` is not in the catalog by key (searched), `Handicap` → "Handicap" (English kept, `kif.import.preview.handicap`), `Komaochi` → "Komaochi", `Sente` / `Gote` → "Sente" / "Gote" (also "shitate" / "uwate" in the handicap lessons), "tsume" lowercase, "joseki" (14) and "jōseki" with macron (6).
- Piece sets: `settings.pieceSet` → "Estilo de peças", `settings.pieceSet.western` → "Internacional", `settings.pieceSet.traditional` → "Tradicional (kanji)".
- Opponent tiers (`opponentTier.*`): Novice "Novato", Beginner "Iniciante", Casual "Casual", Club Player "Jogador de clube", Intermediate "Intermediário", Advanced "Avançado", Expert "Especialista", Master "Mestre".
- Skills (`skill.*`): Tactics "Tática", Defense "Defesa", Positioning "Posicionamento", Endgame "Final", Openings "Aberturas".

Flags
- **S1 (opponent words):** the eight tier names above; "Intermediário" and "Especialista" are pt-BR-leaning (pt-PT "Intermédio", "Perito"); the store description says "UMA ESCADA DE 40 ADVERSÁRIOS".
- **S2 (rating):** `Estimated Rating` → "Pontuação estimada" (`progress.estimatedRating` and `progress.rating` both); the Spanish also has "Nivel estimado" for Game Center; not re-checked here for the leaderboard key.
- **S3 (move word):** "lance" (331) vs "jogada" (4). Choose one for the site; "lance" is the app's word.
- **S4 (best value):** `paywall.bestValue` → **"MELHOR CUSTO-BENEFÍCIO"** (Brazilian; Observa and RightSplit use "Melhor valor", Pawza "Mais vantajoso").
- **S5 (Family Sharing):** `settings.premium.familyShared.title` → "Premium via Partilha entre Familiares" (5 strings) and the subtitle "Gerenciado pelo organizador da família — quem pode alterar ou cancelar a subscrição." Apple's Portuguese (Portugal) name for the feature is "Partilha em Família" (Observa says "Partilha com a Família"). Three variants across two apps.
- **S6 (promote):** `Promote` → "Promover"; the promoted bishop is "Bispo promovido" and the piece called `Horse` in English is not called "Cavalo promovido" (the knight is "Cavalo").
- **S7 (tier names):** `Shogiful Premium` with `Premium mensal / Premium anual / Premium vitalício` (lower-case "vitalício"); `Premium Active` → "Premium ativo", `Free Plan` → "Plano gratuito"; `Upgrade to Premium` → "Mudar para Premium".
- **S8 (restore/manage):** `Restore Purchases` → "Restaurar compras", `Manage subscription` → "Gerir subscrição" (European "Gerir", beside "Gerenciado" in the Family Sharing line).
- **S9 (tab):** `tab.dashboard` → "Início" (not "Painel"); `tab.training` → "Treino"; `tab.analysis` → "Análise"; `tab.progress` → "Progresso".
- **S10 (deep analysis):** `paywall.hero.deepAnalysis.title` → "Vá mais fundo" (the app has no "Deep Analysis" label, as in Spanish).
- **S11 (tsume trail):** `Tsume Trail` → "Trilha tsume" (pt-BR; pt-PT "Percurso tsume").
- **S12 (store subtitle):** "Shogi: tática e análise com IA" (matches the app's "Tática"). The store name "Shogiful: Xadrez japonês".

### Glossary

| English term on site | English UI string (key) | pt-PT UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Dashboard | `Dashboard` (`tab.dashboard`) | Início | S9 |
| Tab: Play | `Play` (`tab.play`) | Jogar | |
| Tab: Analysis | `Analysis` (`tab.analysis`) | Análise | |
| Tab: Training | `Training` (`tab.training`) | Treino | |
| Tab: Progress | `Progress` (`tab.progress`) | Progresso | |
| Premium | `Shogiful Premium` (`settings.premium.name`) | Shogiful Premium | |
| Premium · Monthly | `Premium Monthly` (`paywall.plan.monthly`) | Premium mensal | |
| Premium · Annual | `Premium Yearly` (`paywall.plan.yearly`) | Premium anual | |
| Lifetime | `Premium Lifetime` (`paywall.plan.lifetime`) | Premium vitalício | matches the store IAP name "Premium vitalício" |
| Upgrade | `Upgrade to Premium` (`settings.premium.upgrade`) | Mudar para Premium | S7; `Premium Active` → "Premium ativo", `Free Plan` → "Plano gratuito" |
| Family Sharing | `Premium via Family Sharing` (`settings.premium.familyShared.title`) | Premium via Partilha entre Familiares | S5 |
| Best value | `BEST VALUE` (`paywall.bestValue`) | MELHOR CUSTO-BENEFÍCIO | S4 |
| Start free trial | `Start Free Trial` (`paywall.startTrial`) | Iniciar teste grátis | `paywall.trial.compound.format` → "Teste grátis de %lld dias" |
| Tsume-shogi | `Tsume-Shogi: Forced Checkmate` (`concept.tsume-basics.title`) | Tsume: o xeque-mate forçado | |
| Tsume Trail | `Tsume Trail` (`module.tsumeTrail.title`) | Trilha tsume | S11 |
| Drop Drills | `Drop Drills` (`module.dropDrills.title`) | Exercícios de colocação | drops = "colocação" |
| Castle Atelier | `Castle Atelier` (`module.castleAtelier.title`) | Ateliê de castelos | |
| Joseki Lab | `Joseki Lab` (`module.josekiLab.title`) | Laboratório de jōseki | |
| Tesuji / Yose | `Tesuji Cards` / `Yose Trainer` | Cartas tesuji / Treinador yose | |
| Daily plan / assessment | `Daily Plan` / `Skill Assessment` | Plano diário / Teste de nível | |
| Lessons | `Lessons` (`hub.lessons.title`) | Lições | |
| Handicap play | `Handicap` / `Komaochi` | Handicap / Komaochi | `lesson.handicap.02.title` → "Handicap de lança (香落ち)" |
| Game review | `Game Review` (`analysis.review.title`) | Revisão da partida | |
| Deep analysis | `Go deeper` (`paywall.hero.deepAnalysis.title`) | Vá mais fundo | S10 |
| Piece sets | `International` / `Traditional (Kanji)` | Internacional / Tradicional (kanji) | |
| Piece style setting | `Piece Style` (`settings.pieceSet`) | Estilo de peças | |
| Pieces | `piece.*` | Rei, Torre, Bispo, General de ouro, General de prata, Cavalo, Lança, Peão | |
| Promoted pieces | `piece.rook.promoted` / `piece.bishop.promoted` | Dragão / Bispo promovido | |
| Promotion prompt | `Promote?` (`promotion.title`) | Promover? | buttons "Promover" / keep |
| Drop hint | `board.drop.hint` | Colocar %1$@ em %2$@ | |
| Pieces in hand | `board.hand.piece %lld` | Peça capturada — %lld na mão | |
| Opponent tiers | `opponentTier.*` | Novato, Iniciante, Casual, Jogador de clube, Intermediário, Avançado, Especialista, Mestre | S1 |
| Five skills | `skill.*` | Tática, Defesa, Posicionamento, Final, Aberturas | |
| Estimated rating | `Estimated Rating` | Pontuação estimada | S2 |
| Resign | `Resign` (`game.resign`) | Desistir | status "Desistiu", result "Desistência" |
| Checkmate / Check | `Checkmate` / `Check!` | Xeque-mate / Xeque! | |
| Restore Purchases | `Restore Purchases` (`paywall.restore`) | Restaurar compras | |
| Manage subscription | `Manage subscription` (`settings.premium.manage`) | Gerir subscrição | S8 |
| Move word | `Best Move` | Melhor lance | S3 |

Paid tier names as the Portuguese UI shows them: **Shogiful Premium** with plans **Premium mensal / Premium anual / Premium vitalício**, "MELHOR CUSTO-BENEFÍCIO", "Iniciar teste grátis", "Restaurar compras", "Gerir subscrição", "Premium via Partilha entre Familiares", "Plano gratuito", "Premium ativo".

### Portuguese App Store listing (https://apps.apple.com/pt/app/id6761656926, read 2026-11-19)

- Name: **Shogiful: Xadrez japonês** (English "Shogiful Learn & Analyze Shogi"; no space before the colon)
- Subtitle: **Shogi: tática e análise com IA** (English "Japanese Chess Tactics Trainer")
- Category: **Tabuleiro** (English "Board")
- Price: Gratuito. In-app purchases as shown: Premium anual **9,99 €**, Premium mensal **1,99 €**, Apoiador **5,99 €**, Apoio enorme **9,99 €**, Um café **1,99 €**, Premium vitalício **22,99 €** (the tip IAP names are "Apoiador", "Apoio enorme", "Um café")
- Idiomas: Português plus 32 others (33 listed)
- Compatibility: iOS 18.0, iPadOS 18.0, macOS 15.0 (M1). Size 149 MB.
- Description register: formal ("o seu treinador pessoal", "no seu iPhone ou iPad", "Há 40 adversários entre si e o topo da escada", "Jogue uma partida"; 12 formal hits, 0 tu). It names "501 problemas tsume", "UMA ESCADA DE 40 ADVERSÁRIOS" and "CADA LANCE, ANALISADO".

---

## Cross-app terms

| Concept | Value in each app |
|---|---|
| Restore purchases | "Restaurar compras" in all four pt-PT apps (consistent) |
| Settings | "Definições" in Observa (8), Pawza (12), RightSplit (3), Shogiful (11); the pt-BR value is "Ajustes" (2 leaks in Observa) |
| Free | "Gratuito" (Observa), "Grátis" (Pawza, RightSplit); "Plano gratuito" (Shogiful) |
| Best value | "Melhor valor" (Observa, RightSplit), "Mais vantajoso" (Pawza), "MELHOR CUSTO-BENEFÍCIO" (Shogiful, Brazilian) |
| Lifetime | "Vitalício" in all four ("Pro (vitalício)", "Pro+ Vitalício", "Premium vitalício"); store IAP names say "compra única" for Observa, Pawza and RightSplit |
| Monthly / Yearly | "Mensal" / "Anual" |
| Free trial | "Iniciar teste gratuito" (Observa), "Iniciar teste gratuito de 7 dias" (Pawza), "%lld dias grátis" (RightSplit), "Iniciar teste grátis" (Shogiful); Observa also says "avaliação gratuita" once. Apple's own pt-PT wording for a subscription trial is a separate check (not read here) |
| Upgrade | "Atualizar para Premium" (Observa), "Mudar para o Pawza Pro" (Pawza), "Atualizar para Pro+" (RightSplit), "Mudar para Premium" (Shogiful): two verbs |
| Unlock | "Desbloquear" (infinitive) in most buttons; "Desbloqueie" (formal imperative, Observa 121, RightSplit 4, Shogiful 3); "Desbloqueia" (tu imperative, Pawza 2) |
| Premium tier name | Observa "Premium", Shogiful "Premium", Pawza "Pro" / "Pawza Pro", RightSplit "Pro+" |
| Add | "Adicionar" / "Adicione" / "Adiciona" (all four; no "agregar") |
| Score | "pontuação" (Observa, Shogiful); store subtitle "Pontuação" |
| Scan | "Digitalizar" (Pawza, RightSplit); pt-BR has "Escanear" |
| Save | "Guardar" (all four); "Salvar" (13 in Shogiful, Brazilian) |
| Delete | "Eliminar" (all four); "Excluir" (1 in Shogiful, Mockly) |
| Share | "Partilhar" (all four); "compartilh-" (1 in Shogiful) |
| Family Sharing | "Partilha com a Família" (Observa), "Partilha entre Familiares" (Shogiful); Apple pt-PT: "Partilha em Família" |
| Tip | "Gorjeta" (RightSplit, Shogiful tip purchases are "Apoiador / Apoio enorme / Um café" and Observa "Apoiar o programador") |
| Apple Health | "Apple Health" (Observa UI); "Apple Saúde" in the HealthKit permission text |
| Coach | "Treinador" (Shogiful, Observa); "Coach" in Observa's store subtitle |
| Training | "Treino" (Observa, Shogiful); "Treinar hoje?" |
| Subscribe | "Subscrever" (Pawza), "subscrição" (Observa, RightSplit, Shogiful); pt-BR "Assinar" |
| Scan photo | "Foto" (Pawza, RightSplit), "fotografia" once in Pawza |
| App | "app" (Observa 22, Pawza 10, RightSplit 3, Shogiful 7); "aplicação" 1-2; "a app" |
| Screen | "ecrã" (Observa 13, Pawza 1, RightSplit 5); Mockly pt-BR "tela" |
| Locale code | `pt-PT` in four apps; **only `pt-BR` in Mockly** |
| Store title punctuation | no space before the colon in all five Portuguese names |
| Brand article | "o Observa", "o Pawza", "o RightSplit", "o YaneuraOu" (masculine article before app names) |

## Flags

Register (decides the site's formality)
- **F1 (no single register).** Pawza (in-app) is **tu**: 150 tu strings, 32 formal. Observa is **formal**: 1609 formal ("o seu", "Desbloqueie", "Veja", "Toque"), 49 tu. RightSplit is **mixed**: 98 formal, 21 tu, and the Pay-Me button "Paga-me" is a tu command. Shogiful is **formal with Brazilian "você"** in 255 strings plus about 26 tu achievement and lesson strings. Mockly (pt-BR) is "você / seu". The Portuguese store descriptions of Observa, Pawza, RightSplit and Shogiful are formal. The Spanish site writes tu; for Portuguese the majority of Lagerland's own text (Observa 1609, RightSplit, Shogiful, all store descriptions) is formal third person ("o seu", imperative "Toque", "Desbloqueie"), while Pawza alone is tu. Decide explicitly; the evidence leans formal except for Pawza.
- **F2 (tu and formal in one string).** Observa: "Ainda não há dados suficientes para análise avançada de VFC. Continue a usar o seu Apple Watch…" is formal, but "Mostra a consistência dos seus padrões de energia ao longo do tempo." mixes a tu verb with "dos seus". Pawza: "Regista uma entrada de imediato. Toque sem soltar para adicionar quantidade ou nota." (tu then formal). Shogiful: "Gote não tem bispo — abre cedo a diagonal do teu bispo e desenvolve em torno do seu longo…".

Brazilian vocabulary in pt-PT
- **F3 (Mockly is not European Portuguese at all).** Only `pt-BR` exists in the catalog and the store listing is Brazilian ("Capturas de Tela", "Você", "Salvar", "arquivo", "Provedor", "Câmera"). Add `pt-PT` to the app and a Portuguese store localization before a Portugal page quotes its strings (M1, M2).
- **F4 (Observa leaks).** Brazilian words and forms remain in Observa's pt-PT text: "você" 6, "Sua/Seu" sentence starts 60, "estresse" 5, "oxigênio" 4, "estágio(s)" 9, "faixa" 109, "ótimo/ótima" 8, "teste grátis" 2, "está recebendo", "estar contribuindo". Also the missing-accent "pontuacao" block (O10).
- **F5 (Family Sharing name).** Observa "Partilha com a Família", Shogiful "Partilha entre Familiares"; Apple's pt-PT name is "Partilha em Família". The site should use the Apple name; quote the app string only when naming an in-app label.
- **F6 (Shogiful is 90% pt-BR).** 3380 of 3751 pt-PT strings equal the pt-BR strings; visible Brazilian labels include "MELHOR CUSTO-BENEFÍCIO" (best value), "Trilha tsume", "Gerenciado pelo organizador da família", "Salvar", "arquivo", "Seu lance", "Você jogou". Report to the owner before the Portuguese Shogiful page quotes Shogiful UI strings (add to ISSUES.md after review).
- **F7 (free-trial wording).** "teste grátis / teste gratuito" is Brazilian-leaning; four different wordings across four apps (see Cross-app terms). The site's own trial text should use one pt-PT form (not decided by the apps).
- **F8 (tax / IVA).** RightSplit `Tax` → "Imposto"; a Portuguese bill shows "IVA" (R4).
- **F9 (tip word).** "Gorjeta" is correct for Portugal (RightSplit); never "propina" (tuition fee in Portugal). The Spanish "propina" is the opposite.

App-side string bugs (belong in ISSUES.md after review by the main session)
- **F10 (Observa missing accents).** `Your Sleep Quality score is built from four factors:…` has unaccented Portuguese ("pontuacao… e construida… Quao ininterrupto… Eficiencia… Restauracao… recuper…"). App-side fix; same string is also wrong in `es` / `es-MX`.
- **F11 (Observa English left in).** "Desbloqueie Lifetime Access" and "Desbloqueie HRV Trends" (English product names kept); "HRV" in 19 strings next to "VFC" (about 205).
- **F12 (Pawza permission prompts in English).** Camera and photo-library texts are English build settings, no `InfoPlist.xcstrings` (P1).
- **F13 (Mockly translation packs).** The app sells translation credit packs ("Pacotes de tradução") but the Portuguese store lists no in-app purchases (M3).

Terminology inconsistencies that decide site wording
- **F14 (Observa).** "Prontidão" (readiness, consistent) vs "Estado de Treino"; "linha de base" (149) vs "referência" (38); "Estágios do sono" vs "Fases do sono"; Core stage "Essencial" / "Principal" / "Sono básico"; resting heart rate "FC em repouso" / "Frequência cardíaca de repouso" / "FCR"; HRV "VFC" with "da VFC" (7) vs "do VFC" (1); the four training calls Push "Intenso", Maintain "Manter", Recover "Recupere", Rest "Descanso" (O6). The English site says "Premium"; the Portuguese app says "Premium".
- **F15 (Observa HRV rule).** House rule: HRV is SDNN from Apple Health, never RMSSD. In the Portuguese UI "VFC" is the headline metric; SDNN appears in 3 explanatory strings; RMSSD appears in 19 strings, all in the Premium Advanced HRV / ECG context ("RMSSD e pNN50 derivados do ECG"). The site may name RMSSD only for the Advanced HRV / ECG feature.
- **F16 (Shogiful).** "lance" (331) vs "jogada" (4); drops are "colocação" (and the odd "largamento" in one achievement and "Descer o Pano" as its title); rating "Pontuação estimada"; "Bispo promovido" is the promoted bishop and "Dragão" the promoted rook; `Promote` is "Promover" (Spanish "Promocionar"); "Handicap" kept in English; "Teste de nível" for the skill assessment; "Internacional" for the Western piece set.
- **F17 (RightSplit).** "Recibo" vs "Conta"; "Divisão" is the split word, "partilhar" is only share; "Todos liquidados" vs "Acerto/Acertar"; `Owed` → "Devido" heading (R7); `Pocket Split` → "Divisão de bolso" (literal); `Track payments` → "Seguir pagamentos".
- **F18 (Pawza).** "Registos" for health records, "Diário de cuidados" for the care log, "Ficha do cuidador" for the sitter document; `Best value` is "Mais vantajoso"; "O Apple Intelligence" vs "A Apple Intelligence"; `Free` is "Grátis" (Observa "Gratuito").
- **F19 (cross-app).** Two upgrade verbs ("Atualizar para" in Observa and RightSplit, "Mudar para" in Pawza and Shogiful) and four free-trial strings; three "unlock" forms (Desbloquear / Desbloqueie / Desbloqueia); three best-value strings; two "free" words. Decide one wording for the site's own paywall-style text and quote the app string verbatim when the page names an in-app button.

Store listing notes
- **F20 (store names).** Portuguese store names: Mockly "Mockly: Capturas de Tela" (Brazilian), Observa "Observa: VFC & Recuperação", Pawza "Pawza: Saúde de Cães e Gatos", RightSplit "RightSplit: Dividir e Gorjeta", Shogiful "Shogiful: Xadrez japonês". All five are localized (unlike Mockly's Spanish name, which is English) and none has a space before the colon. Subtitles: Mockly "50 Idiomas, Um Só Fluxo", Observa "Sono, Ciclo, Coach & Pontuação", Pawza "Boletim, vacinas e lembretes", RightSplit "Recibo & despesas em grupo", Shogiful "Shogi: tática e análise com IA".
- **F21 (store register).** The Portuguese store descriptions are formal ("Toque", "Digitalize", "o seu") for Observa, Pawza, RightSplit and Shogiful; Mockly's is Brazilian "Você / SEU".
- **F22 (Observa cycle).** The store subtitle says "Ciclo"; the English site page does not cover cycle tracking (fact gap, same as in the German, French and Spanish glossaries).
- **F23 (store prices).** Prices read from the Portuguese store pages: Observa Premium mensal 3,99 €, Premium anual 24,99 €, Premium compra única 59,99 €, Apoiar o programador 1,00 €; Pawza Pro mensal 2,99 €, anual 22,99 €, compra única 44,99 €; RightSplit Pro+ anual 4,99 €, compra única 8,99 €; Shogiful Premium mensal 1,99 €, anual 9,99 €, vitalício 22,99 €, Apoiador 5,99 €, Apoio enorme 9,99 €, Um café 1,99 €; Mockly 14,99 €. Reference only; the master file is the source.
- **F24 (seller).** The seller line on the store pages carries the owner's personal name and address; not copied anywhere.

## Portuguese (Portugal) glossary, part 4: soon, tare, taskful-day, wanderwiki, xiangqiful, clippet

Method. Extracted 2026-11-19, read-only, from each app's string catalogs under `~/Downloads/<source>/` (`.xcstrings` is JSON, parsed with `python3 -I`; `build`, `.build`, DerivedData, Pods and worktrees ignored; every catalog of each app found and counted, including widgets, Watch, Kit packages, InfoPlist and AppShortcuts). I counted keys with `shouldTranslate` not false and a non-blank key; a key counts as Portuguese only if every `localizations.pt-PT` string unit has state `translated` (plural and substitution variations included). **All six catalogs carry BOTH `pt-PT` and `pt-BR`; I used `pt-PT` only. No catalog has a bare `pt`.** pt-PT values are copied verbatim from the catalogs. No app has `.lproj` folders. Store pages were fetched on 2026-11-19 with curl: `https://itunes.apple.com/lookup?id=<ID>&country=pt&lang=pt_pt` and the raw page `https://apps.apple.com/pt/app/id<ID>` (Safari User-Agent, `Accept-Language: pt-PT`, read from the `serialized-server-data` JSON; page language tag `pt-PT`). No 429 this time. The seller's personal name and address on the store pages are deliberately not copied anywhere. Prices are reference only (the site prints prices from its catalog).

How "tu" versus "você/3rd person" was counted. For each pt-PT string (first plural variant) I flagged: **tu pronoun/verb markers** (teu, tua, teus, tuas, te, ti, contigo, tens, podes, queres, estás, precisas, sabes …); **formal markers** (seu, sua, seus, suas, você, vocês, lhe, lhes); **formal imperatives** as the first word (Toque, Adicione, Escolha, Abra, Veja, Ative, Selecione, Comece, Mantenha, Continue …); **tu imperatives** as the first word (Toca, Adiciona, Escolhe, Abre, Vê, Guarda …). Caveats: "seu/sua" sometimes just means "its/his" (counted anyway, so the formal pronoun count is an upper bound); tu imperatives are spelled like the 3rd-person present ("Abre o artigo" is a VoiceOver hint, not an address), so the tu-imperative count is also an upper bound and the pronoun counts are the firmer evidence; imperatives outside my word list are not counted (undercount for both). Per-string mixing (tu and formal inside one string) was 0 in five apps and 3 in Xiangqiful. A "tu vs formal" decision is needed per app; the portfolio does NOT speak with one voice (see Cross-app terms).

Cross-app summary:
- **All six apps ship a `pt-PT` locale at 99.7 to 100 % of keys.** Coverage is not the problem; quality and register are.
- The pt-PT text is real European Portuguese in Soon., Tare, Taskful Day, WanderWiki and Clippet (ecrã, telemóvel, ficheiro, guardar, partilhar, Definições, Gerir subscrição, "a carregar", "estar a + infinitivo"). **Xiangqiful is the exception: 74 % of its long strings (8+ words) are byte-identical to the pt-BR text** (against 2 to 33 % in the other apps), with Brazilian forms like "Assine", "habilidades", "deveria estar vencendo", "te dar xeque-mate", "está te segurando", "você". Verdict "partial" for that app.
- **Register is split.** Soon.'s main app, Soon.'s permission prompts and Clippet say **tu**; Tare, Taskful Day, WanderWiki and Xiangqiful say **você-form / 3rd person** ("o seu", "Toque", "Veja", "Adicione"). Soon.'s widgets and Taskful Day's insights/onboarding mix both. The store listings follow the same split (Soon. and Tare tu; Taskful Day, WanderWiki, Xiangqiful formal; Clippet's prepared listing tu).
- "Lifetime" is **Vitalício** in all six pt-PT catalogs (Brazilian catalogs also say Vitalício, but Taskful Day pt-BR keeps "Lifetime" in one string; pt-PT fixed it). "Restore purchases" is **Restaurar compras**, "Settings" **Definições** (only WanderWiki and Xiangqiful leak "Ajustes" once or twice), "Manage subscription" **Gerir subscrição**, "Subscription" **subscrição** (never "assinatura" in any pt-PT UI string; one Brazilian word in the store descriptions, see Flags).

---

### 1. Soon. (`soon`, source `countdown/`, ID 6757280643)

### Portuguese coverage (pt-PT)
| Catalog | keys | `pt-PT` translated | % |
|---|---|---|---|
| countdown/Localizable.xcstrings (main app, includes paywall) | 741 | 741 | 100 % |
| countdown/AppShortcuts.xcstrings (Siri and Spotlight phrases) | 13 | 13 | 100 % |
| countdown/InfoPlist.xcstrings | 6 | 5 | 83 % (only the stray key `Soon` is missing; display name, calendar and location permission texts are in Portuguese) |
| CountdownWidgets/Localizable.xcstrings | 184 | 182 | 98.9 % (missing only the format strings `%@ ` and `%@ %@`) |

Total 944 keys, 941 translated (99.7 %). Not in Portuguese: nothing user-visible. Widget gallery names stay English by design (`Soon · Ring`, `Soon · Timeline`, `Soon · StandBy`, `Soon · Hero` and the rest of the `Soon · …` names). Real pt-PT (22 strings differ from pt-BR in the headline vocabulary: ecrã, Gerir, Guardar, Pesquisar, Desporto, Concerto, contagem decrescente). **Verdict: app is in European Portuguese: yes** (with a handful of stray Brazilian words and a mixed register, see Flags).

### Glossary
| English term on site | English UI string (key) | pt-PT UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Home tab | `Home` | Início | |
| Plan tab | `Plan` | Plano | |
| Search tab | `Search` | Pesquisar | pt-BR "Buscar"; pt-PT verb "Pesquisar" is correct |
| Profile tab | `Profile` | Perfil | |
| Plan Mode | `Plan mode reminders` | Lembretes do modo planeamento | only UI string naming the mode, so the pt-PT name is **modo planeamento** (pt-BR "modo planejamento"). No standalone label |
| Premium | `Premium` | Premium | `Go Premium` → "Obter Premium" (pt-BR "Assinar Premium"); `Premium feature. Double tap to upgrade.` → "Funcionalidade Premium. Toca duas vezes para fazer upgrade."; `Open Soon. to upgrade to Premium.` → "Abra o Soon. para mudar para Premium." (formal, next to a tu string) |
| Free | `Free` | Gratuito | pt-BR "Grátis"; `1 week free` → "1 semana grátis" (both words occur) |
| Monthly / Annual | `Monthly` / `Yearly` | Mensal / Anual | app says "Yearly", not "Annual" |
| Lifetime | `Lifetime` | Vitalício | `One-time purchase` → "Compra única". The store IAP is "Premium compra única" |
| Free trial | `Free trial` | Período gratuito | pt-BR "Período grátis" |
| Restore purchases | `Restore Purchases` | Restaurar compras | |
| Countdown | `Countdown` | Contagem decrescente | pt-PT. Widgets use the short form "Contagem" (`Countdown` in the widget catalog). 59 strings say "decrescente", 0 say "regressiva" (the pt-BR word). `Add countdowns` → "Adicionar contagens" |
| Event / moment | `Event` / `Moment` / `Moments` | Evento / Momento / Momentos | both exist as separate keys. `Event Vibe` → "Ambiente do evento" (pt-BR "Clima do evento") |
| Memories | `Memories` / `Memory` | Memórias / Memória | |
| Reminders | `Reminders` | Lembretes | |
| Reflection mode | `Notes` | Notas | no UI string says "Reflection" |
| Daily notes | `Personalized daily notes` / `Weather & daily notes` | Notas diárias personalizadas / Tempo e notas diárias | |
| Weather | `Weather` / `Weather forecast` / `Smart weather forecast` | Tempo / Previsão meteorológica / Previsão meteorológica inteligente | FLAG: tab "Tempo" but 10 strings say "Meteorologia" ("Meteorologia %@", "Adicionar localização para meteorologia", "Atribuição Apple Meteorologia"), 2 keep English "Apple Weather" (`Weather data provided by Apple Weather` → "Dados meteorológicos fornecidos por Apple Weather"), and `Clothes for the weather` → "Roupa para o clima" (Brazilian "clima") |
| Calendar import | `Import from your calendar` / `Turn calendar events into countdowns` | Importar do seu calendário / Transformar eventos do calendário em contagens decrescentes | `Imported from Calendar` → "Importado do calendário". Note "seu" here against "teus" in the permission prompt |
| Recurring events | `Recurring countdowns` / `Repeat` | Contagens decrescentes recorrentes / Repetir | `Repeats yearly` → "Repete anualmente"; `Yearly on %@ %lld` → "Anualmente em %2$lld de %1$@" |
| Natural language search | `Search` | Pesquisar | |
| Timeline / checklist | `Timeline` / `Checklist` | Cronologia / Lista | consistent "cronologia" (9 strings); widget `TIMELINE` → "CRONOLOGIA" (pt-BR "Linha do tempo"). Checklist only "Lista". `We'll suggest a starter checklist and timeline for %@ events.` → "Vamos sugerir uma lista inicial e uma cronologia para eventos de %@." |
| Themes | `Theme` / `All themes unlocked` | Tema / Todos os temas desbloqueados | |
| Final Countdown | `Final Countdown` | Contagem decrescente final | |
| Widget styles | `Progress Rings` | Anéis de progresso | gallery names stay English |
| StandBy | `Soon · StandBy` | Soon · StandBy | |
| Lock Screen / Home Screen | `Keep on Lock Screen`; `Your countdown on Home Screen and Lock Screen.` | Manter no ecrã bloqueado; A tua contagem decrescente no ecrã inicial e no ecrã de bloqueio. | FLAG: three Home Screen forms ("Ecrã Principal" 5, "ecrã inicial" 2) and two Lock Screen forms ("ecrã bloqueado" 6, "ecrã de bloqueio" 1). Apple's pt-PT iOS terms are "Ecrã Principal" and "Ecrã de Bloqueio"; "ecrã bloqueado" is the odd one, also in `Remove this countdown from the Lock Screen.` → "Remover esta contagem decrescente do ecrã bloqueado." |
| Event types | `Trip` `Wedding` `Birthday` `Anniversary` `Concert` `Baby` `Exam` `Work` `Holiday` `Health` `Sport` | Viagem, Casamento, Aniversário, Aniversário, Concerto, Bebé, Exame, Trabalho, Feriado, Saúde, Desporto | pt-PT forms (pt-BR: Show, Bebê, Prova, Esporte). FLAG: `Birthday` and `Anniversary` both give "Aniversário" (pt-BR separates them: "Aniversário de relacionamento"). `Wedding` → "Casamento" |
| Baby mode | `Baby` | Bebé | |
| On This Day | `ON THIS DAY` | NESTE DIA | `Turn on On This Day reminders in Settings to receive these.` → "Ative os lembretes Neste Dia nas Definições para os receber." (formal) |
| Milestone | `Add milestone` | Adicionar marco | `Edit Milestone` → "Editar marco" |
| Streak (widget) | `Day streak` | Sequência de dias | |
| Count up | `days since` / `%lld days since` | dias atrás / %lld dias atrás | "dias atrás" in 11 strings against "há %lld dias" in 5; `%lld days since this moment` → "%lld dias desde este momento" |
| Pin | `Pin to top` | Fixar no topo | Clippet says "Afixar" for the same verb; Apple's pt-PT Notes/Messages wording is "Afixar" |
| iCloud sync | `iCloud Sync` | Sincronização do iCloud | Taskful Day: "Sincronização iCloud"; Clippet: "Sincronização do iCloud" |
| Save | `Save` | Guardar | pt-BR "Salvar" |
| Subscription | `Manage Subscription` | Gerir subscrição | `One-time tip. Not a subscription.` → "Gorjeta única. Não é uma subscrição." |
| Tips | `Widget Tip` / `Tips` / `TIP JAR` | Dica de widget / Dicas / GORJETA | the tip jar is "Gorjeta"; `Support the Developer` → "Apoiar o programador" (pt-BR "desenvolvedor") |

Top 10 for the site: Contagem decrescente; Momento; Evento; Modo planeamento; Ecrã Principal / Ecrã de Bloqueio; Cronologia; Lembretes; Memórias; Gerir subscrição; Vitalício.

Other flags:
- Permission prompts (verbatim, tu): calendar "O Soon. lê os teus eventos do calendário para que os possas transformar em contagens decrescentes. Nada é alterado ou partilhado."; location "A localização é utilizada para apresentar a previsão meteorológica dos teus eventos de contagem decrescente."
- Siri phrases (13) have no pronoun; mixed forms: "Adicionar uma contagem decrescente no ${applicationName}", "Criar…", "Abrir…" (infinitive) and "Mostra ${event} no ${applicationName}", "Mostra a minha próxima contagem decrescente…" (tu imperative); "Quantos dias faltam para ${event}", "O que se segue no ${applicationName}".
- Brazilian leftovers: "A cada %lld" / "A cada %lld meses" (15 strings; pt-PT "Todos os %lld meses"), "Roupa para o clima", "a cada dia" in `Forecasts and a fresh thought each day.` → "Previsões e um pensamento novo a cada dia."; English-ish "fazer upgrade" (2 strings).
- Register: see counts below.
- Pro/free wording: `Premium lets you choose events` → "O Premium permite-te escolher eventos" (tu); `Upgrade to Premium to receive On This Day reminders.` → "Mude para Premium para receber lembretes Neste Dia." (formal); `Faça upgrade para adicionar momentos ilimitados.` (formal).

### Register (pt-PT)
Strings flagged: tu markers 54, formal markers 34, tu-form first-word imperatives 53 (upper bound), formal first-word imperatives 28; 0 strings mix both.
- Main app (741): tu 44 / formal 13; imperatives tu 46 / formal 15. Examples tu: "Escolhe qual evento apresentar no teu widget.", "Dias até ao teu momento — sempre visível.", "O Premium permite-te escolher eventos", "Vê todas as tuas contagens em belos cartões empilhados." Examples formal: "Um lembrete suave no aniversário das suas memórias. Ative uma memória…", "Abra o Soon. para mudar para Premium.", "Ative os lembretes Neste Dia nas Definições para os receber.", "Importar do seu calendário".
- Widgets (182): tu 8 / formal 21; imperatives tu 7 / formal 13. Formal examples: "Escolha o evento que o controlo mostra.", "Adicione momentos para uma cronologia", "Mantenha premido para reconfigurar", "Um anel de progresso circular em contagem decrescente até ao seu momento." (tu examples: "Adiciona contagens para preencher este widget", "Abre a app para adicionar um momento".)
- InfoPlist permission prompts: tu (2 of 2).
- Verdict: **mixed within one app**; main app and permission prompts lean tu, widgets and subscription/upsell strings lean formal. The store listing description is tu ("Vê quantos dias faltam…", "sempre que pegas no iPhone", "Adiciona um momento e escolhe as cores", "prepara-te").

### Paid tier names in the pt-PT UI
Premium; plan labels Mensal / Anual / Vitalício; "Período gratuito" and "1 semana grátis"; "Restaurar compras"; "Obter Premium"; "Gerir subscrição". Store product names: "Premium mensal", "Premium anual", "Premium compra única", "Apoiar o programador".

### Portuguese App Store listing (checked 2026-11-19, https://apps.apple.com/pt/app/id6757280643)
- Name: **Soon. Dias Até Grandes Eventos** (US: "Soon. - Days Until Big Events")
- Subtitle: **Casamento, Viagem & Contagem** (US: "Wedding, Trip & Baby Countdown" per the earlier glossaries; FLAG: it drops "Bebé"/Baby and says "Contagem", not "Contagem decrescente"; and note this exact subtitle string also showed up in the page JSON of the other four apps' "more by developer" block, so it belongs to Soon.)
- In-app purchases (reference): `Apoiar o programador 1,00 €` · `Premium compra única 14,99 €` · `Premium mensal 1,99 €` · `Premium anual 9,99 €`
- Languages line: **Português e mais 35**
- Category: **Estilo de vida** (also "Utilitários"). Family Sharing: described as "Partilha entre Familiares" in the description
- Description register: tu ("Vê… pegas… prepara-te… Adiciona… escolhe"), text uses "ecrã principal", "ecrã bloqueado", "subscrição", "Vitalício". 2 626 characters.

---

### 2. Tare (`tare`, source `weightbalance/`, ID 6806255929)

### Portuguese coverage (pt-PT)
| Catalog | keys | `pt-PT` translated | % |
|---|---|---|---|
| weightbalance/Localizable.xcstrings (main app, the only catalog) | 121 | 121 | 100 % |

No InfoPlist.xcstrings and no permission prompts. 94 of 121 strings (78 %) are identical to pt-BR, but those are mostly short neutral strings; the visible pt-PT choices are real (grelha, Avaliar, Definições, A carregar, Partilhar, Dica, Termos de utilização, "Móbile"). **Verdict: app is in European Portuguese: yes.**

### Glossary
| English term on site | English UI string (key) | pt-PT UI string (verbatim) | Note |
|---|---|---|---|
| Chapter I…X | `Chapter %lld` | Capítulo %lld | |
| Unlock / buy chapters | `Open Chapters %lld to %lld` / `Buy Chapters %lld to %lld, %@` / `Buy Chapter %lld, %@` | Abrir os capítulos %1$lld a %2$lld / Comprar os capítulos %1$lld a %2$lld, %3$@ / Comprar o capítulo %1$lld, %2$@ | locked: "Capítulo %lld, não comprado" |
| Unlock text | `%@ more %lld chapters of handcrafted levels. Yours forever.` | Mais %1$@ %2$#@chapters@ de níveis feitos à mão. Seus para sempre. | FLAG: "Seus" is the Brazilian possessive (pt-PT "Teus"/"Vossos"/"São seus para sempre" depending on register); also word order "Mais %@ capítulos" puts the price before the count, check on screen |
| Restore purchases | `Restore purchases` | Restaurar compras | |
| Settings | `Settings` | Definições | |
| Hints | `Hints` / `Hint` | Dicas / Dica | (Xiangqiful also says "Dicas") |
| Three gold stars | `Marks` | Estrelas | no key says "gold" |
| Sound / Haptics | `Sound` / `Haptics` | Som / Vibração | |
| High contrast | `High contrast` | Contraste elevado | pt-BR says "Alto contraste" per other Apple wording; pt-PT Apple term is "Aumentar contraste" |
| Beam | `Beam %lld` | Haste %lld | **haste** (rod): "Haste %1$lld, suspensa na haste %2$lld, %3$@, entalhe %4$lld." The store listing also says "hastes". The arm: `%@ arm, notch %lld` → "Braço %1$@, entalhe %2$lld" |
| Hook / notch | `empty hook` / `notch` | gancho vazio / entalhe | `Every hook filled. Not balanced.` → "Todos os ganchos ocupados. Sem equilíbrio." |
| Weight | `%@, weight %lld` | %1$@, peso %2$lld | `hidden %@` → "%@, peso oculto". Weights are named by colour and shape: `cobalt kite` → "papagaio cobalto", `vermillion disc` → "disco vermelhão", `teal drop` → "gota verde-azulada", `soot ring` → "anel fuligem", `bone fan` → "leque osso", `plum lozenge` → "losango ameixa", `violet pebble` → "seixo violeta", `chrome lens` → "lente cromada", `terracotta crescent` → "meia-lua terracota", `leaf petal` → "pétala verde-folha" |
| Pans | (no key) | (none) | Tare has no pans |
| Picture cards | `Reference scale` | Balança de referência | VoiceOver wording ("Balança de referência, inclinada, lado esquerdo mais pesado.") |
| Shelf / tray | `Tray` / `Return to tray` | Tabuleiro / Voltar a pousar no tabuleiro | FLAG: "tabuleiro" is the tray here (and the board in Xiangqiful); `%@ returned to the tray.` → "%@ de volta no tabuleiro." |
| Balanced | `Balanced` / `balanced` | Em equilíbrio / em equilíbrio | `Balanced. Level complete.` → "Em equilíbrio. Nível concluído." |
| Mobile | `Mobile` | Móbile | the hanging sculpture, accented noun; no clash with "telemóvel" (phone), so no gloss needed |
| Play | `Play` | Jogo | noun |
| Level | `Level %lld` | Nível %lld | `Level %lld, solved` → "Nível %lld, resolvido" |
| Restart / Pause / Resume | `Restart level` / `Pause` / `Resume` | Recomeçar o nível / Pausa / Continuar | `Paused` → "Em pausa"; `Exit to grid` → "Voltar à grelha" |
| Chapter names | `The Hang`, `The Secret`, `The Cascade`, `The Exhibition`, `The Ledger`, `The Inventory`, `The Fulcrum`, `The Forgery`, `The Restoration`, `The Retrospective` | A Montagem, O Segredo, A Cascata, A Exposição, O Balanço, O Inventário, O Fulcro, A Fraude, O Restauro, A Antologia | Title Case in the catalog. "O Restauro" is pt-PT (pt-BR "A Restauração"); "A Fraude" for "The Forgery" (not "Falsificação") |
| Worlds | `Morning Sky`, `Twilight Meadow`, `Deep Sea`, `Evening Stars`, `Coral Reef`, `Firefly Forest`, `Polar Night`, `Rose Dawn`, `Summer Fields`, `Sunset Hills` | Céu da manhã, Prado ao crepúsculo, Mar profundo, Estrelas da noite, Recife de coral, Bosque dos pirilampos, Noite polar, Aurora rosada, Campos de verão, Colinas ao pôr do sol | `Canvas` → "Tela" (canvas painting; fine in pt-PT, not the Brazilian "screen"); `Automatic, each chapter its own world` → "Automático, cada capítulo com o seu mundo" |
| Share / rate | `Share Tare` / `Rate Tare` | Partilhar Tare / Avaliar Tare | pt-PT forms |
| Terms | `Terms of use` / `Privacy` | Termos de utilização / Privacidade | |
| Chapters (IAP) | store product | Capítulos II–X | settled name, matches the store |

Top 10 for the site: Capítulo; Haste; Entalhe; Gancho; Peso oculto; Dica; Em equilíbrio; Móbile; Nível; Estrelas.

### Register (pt-PT)
tu markers 0; formal markers 2 ("Seus para sempre", "com o seu mundo"); formal imperatives 4 (all VoiceOver hints "Toque duas vezes para ver o preço / ampliar / voltar a pousar / selecionar"); tu imperatives 0 (one "Abre" is the verb of the unlock sentence). Verdict: **formal / impersonal**, no tu anywhere. The store description, by contrast, is tu ("Pendura os pesos…", "Pendura… 200 níveis"; markers te/teu 3).

### Paid tier names in the pt-PT UI
No tier name: Tare is free with chapter packs. Sold as "Comprar os capítulos %1$lld a %2$lld, %3$@" and "Abrir os capítulos %1$lld a %2$lld"; the unlock text ends "Seus para sempre." Store IAP: **"Capítulos II–X"**. Locked levels: "Capítulo %lld, não comprado".

### Portuguese App Store listing (checked 2026-11-19, https://apps.apple.com/pt/app/id6806255929)
- Name: **Tare: Puzzle de Equilíbrio** (US: "Tare: Balance Logic Puzzle")
- Subtitle: **Jogo de Lógica e Pesos Ocultos** (US: "Brain Teaser & Hidden Weights"; Title Case)
- In-app purchase (reference): `Capítulos II–X 2,99 €`
- Languages line: **Português e mais 43**
- Category: **Puzzle** (also "Jogos", "Casual"). 4+. Description (2 094 characters) uses "hastes", "pesos", "níveis feitos à mão", tu

---

### 3. Taskful Day (`taskful-day`, source `TaskLogger/`, ID 6757345400; iPhone, iPad, Mac and a Watch target in the source)

### Portuguese coverage (pt-PT)
| Catalog | keys | `pt-PT` translated | % |
|---|---|---|---|
| TaskLogger/Localization/Localizable.xcstrings (main app) | 1427 | 1427 | 100 % |
| TaskfulDayKit/Sources/TaskfulDayKit/Resources/Localizable.xcstrings (shared package, Watch strings) | 114 | 112 | 98.2 % (missing `End focus session`, `Extend focus session`) |
| TaskLogger/InfoPlist.xcstrings | 7 | 7 | 100 % (calendar, Reminders, microphone, speech permission texts) |
| TaskLogger/AppShortcuts.xcstrings | 12 | 12 | 100 % |
| TaskLoggerWidgetsExtension Localizable + InfoPlist | 420 + 3 | 420 + 3 | 100 % |
| watchkitapp Watch App/AppShortcuts.xcstrings | 4 | 4 | 100 % |

Total 1987 keys, 1985 translated (99.9 %). Not in Portuguese: only the two Kit focus-session strings (they fall back to English on the Watch). Real pt-PT (Definições, Gerir subscrição, "a ser", "Atualizar", "Caixa de entrada", ecrã, ficheiro, registo). **Verdict: app is in European Portuguese: yes (two shared-package strings missing).**

### Glossary
| English term on site | English UI string (key) | pt-PT UI string (verbatim) | Note |
|---|---|---|---|
| Day Clock | `clock.title`, `pro.feature.clock_view` | Relógio do dia | `pro.feature.clock_view.desc` → "Visualize o seu dia num relógio de 24 horas." |
| Energy River | `river.title`, `pro.feature.energy_river` | Rio de Energia / Rio de energia | Title Case in the title key, sentence case in the Pro key. desc: "Veja o seu dia como uma linha do tempo fluindo calmamente." FLAG: "fluindo" is the Brazilian gerund (pt-PT "a fluir") and "linha do tempo" against the Soon. "Cronologia" |
| Day Map | `pro.feature.day_map` | Mapa do dia | picker/title `map.title` → "Mapa"; `map.subtitle` → "O teu tempo, à vista." |
| Focus Orbit / Focus Mode | `pro.feature.focus_orbit` | Modo de foco | FLAG: "foco" family (33 strings: "Foco", "Iniciar foco", "Sessão de foco", "Mudar foco") but also `focus.enter` → "Focar" (verb), "No que se tem focado", "esforço concentrado"/"concentra-se" in prose; no "Focus Orbit" label |
| Inbox | `inbox.list.title` / `inbox.title` | Caixa de entrada / Adicionar à caixa de entrada | consistent "Caixa de entrada" in all 9 strings (Spanish has two terms) |
| Today / Tomorrow | `inbox.chip.today` / `inbox.chip.tomorrow` | Hoje / Amanhã | `inbox.chip.later` → "Mais tarde"; `schedule.next_week` → "Próxima semana" |
| Tabs | `tab.tasks`, `tab.all_tasks`, `tab.analytics`, `tab.settings`, `tab.add` | Tarefas, Todas as tarefas, Análise, Definições, Adicionar | pt-BR: Análises, Ajustes |
| Insights / analytics | `analytics.insights.title` / `pro.feature.analytics` | Informações / Análises e estatísticas completas | pt-PT chose "Informações" for Insights (pt-BR leaves "Insights"); FLAG: 3 strings still say the English loanword ("Este insight é escolhido quando melhor corresponde…", "Os insights são reflexões, não julgamentos.") |
| Journal | `journal.title` | Diário | |
| Mood | `mood.timeline.title` / `journal.mood.prompt` | Humor / Como foi o seu dia? | formal prompt next to tu insight strings |
| Workspaces | `pro.feature.workspaces` | Múltiplos espaços de trabalho | |
| Carry forward | `today.carry_forward.title` / `today.carry_forward.button` / `settings.auto_carry_forward.title` / `pad.canvas.carry.title` | Adiar para hoje / Adiar para hoje / Mover tarefas pendentes para a frente / Transportar | FLAG: three verbs for one feature (Adiar, Mover … para a frente, Transportar); "Adiar" means postpone, the opposite nuance of "carry forward" |
| Voice capture | `voice.create_task` / `pro.feature.voice` | Criar tarefa / Entrada de voz mais inteligente | |
| iCloud sync | `settings.icloud_sync` | Sincronização iCloud | (Soon., Clippet: "Sincronização do iCloud") |
| Apple Reminders import | `settings.import_reminders` / `pro.feature.reminders` | Importar dos Lembretes / Reimportação de Lembretes | |
| Widgets (Pro) | `pro.widgets.unlock_all` / `widget.gallery.pro_widgets` | Desbloquear todos os widgets / Widgets Pro | |
| Pro | `pro.paywall.title` / `settings.pro.unlock` | Taskful Day Pro / Desbloquear Pro | |
| Free | `settings.pro.status.free` / `checklist.pro.limit.description` | Plano gratuito / A versão gratuita inclui 1 item por tarefa. Atualize para listas ilimitadas. | "plano gratuito" against "versão gratuita" (same as Spanish) |
| Monthly / Yearly / Lifetime | `pro.plan.monthly` / `.yearly` / `.lifetime` | Mensal / Anual / Vitalício | `pro.buy_lifetime` → "Comprar vitalício"; `pro.badge.one_time` → "Pagamento único"; `pro.terms.lifetime` → "Vitalício é uma compra única. Sem renovação." (pt-BR keeps "Lifetime"; pt-PT fixed it) |
| 7-day free trial | `pro.trial.badge` / `pro.start_trial` | Teste gratuito de 7 dias / Iniciar teste gratuito de 7 dias | pt-BR "teste grátis"; Clippet says "avaliação gratuita" for the same thing; Soon. "Período gratuito" |
| Restore purchases | `pro.restore` | Restaurar compras | |
| Schedule | `overview.schedule` / `form.section.schedule` | Agenda / Agenda | |
| Overdue / Later | `analytics.overdue` / `inbox.chip.later` | Atrasada / Mais tarde | singular "Atrasada" |
| Streak | `analytics.streaks.title` | Sequências | |
| Quick Add | `Quick Add` | Adicionar rapido | FLAG: missing accent ("rápido"), same as pt-BR and Spanish; `today.quick_add.placeholder` → "Adicionar tarefa..." |
| Natural-language capture | (placeholder text) | (see catalog) | not re-pulled |
| Manage subscription | `settings.pro.manage` | Gerir subscrição | `analytics.unlock_pro.hint` → "Abre opções de subscrição"; `Cancela a qualquer momento em App Store › Conta › Subscrições.` |

Top 10 for the site: Relógio do dia; Rio de Energia; Mapa do dia; Modo de foco; Caixa de entrada; Tarefas; Diário; Humor; Vitalício; Gerir subscrição.

Other flags:
- **Verification of the known issue (ISSUES.md line 1001, "pt-PT paywall 'subscrições'/'Vitalício' vs system 'Assinaturas'").** In the pt-PT catalog: "subscri-" appears in 7 strings and "Vitalício/vitalício" in 6; "assinatura/assinar/assine" appears in **0** pt-PT UI strings of any of the six apps' pt-PT locale except Xiangqiful (3 strings). The "Assinaturas" the issue cites is the **pt-BR** Apple system word; Apple's pt-PT iOS wording is "Subscrições" (Definições > Subscrições, App Store > Subscrições), so the pt-PT paywall is correct and consistent with the system and nothing needs to change in the app. The real inconsistency is the store description: Taskful Day's Portuguese description says "A assinatura é renovada automaticamente…" 3 times, while the app, the other apps' listings and Apple use "subscrição". Fix in ASC (pt-PT localization), not in the catalog.
- Brazilian leaks in the pt-PT catalog: "fluindo calmamente", "Considere cargas diárias menores" (comparatives/forms), "pra" appears 53 times inside words ("para" within longer words, not a leak); "Toque" imperatives (20) in a mixed register; keys English `Toca duas vezes`, see register.
- Permission prompts (verbatim, formal): calendar "Veja os eventos do seu calendário juntamente com as suas tarefas para ter todo o plano do dia num só lugar."; Reminders "O Taskful Day pode importar os seus Lembretes Apple para o ajudar a planear o dia num só local."; microphone "O Taskful Day usa o microfone para captar a sua voz e criar tarefas rapidamente."; speech "O Taskful Day usa reconhecimento de fala para transformar a sua voz em texto de tarefa."
- Siri phrases (12 + 4 Watch): no pronoun except "Quantas tarefas tenho no ${applicationName}", "O que devo fazer no ${applicationName}", "Lembrar-me em ${applicationName}"; "no ${applicationName}" vs "em ${applicationName}" (both preposition forms occur, e.g. "Adicionar tarefa em ${applicationName}" and "Criar tarefa no ${applicationName}")
- The paywall lists Day Clock, Day Map, Energy River and Focus Mode as Pro features; the site's Free tier says "All four visual day views" (same open check as the Spanish and French glossaries).

### Register (pt-PT)
Strings flagged: tu markers 15, formal markers 139, formal first-word imperatives 99, tu first-word imperatives 45 (upper bound; many are 3rd-person VoiceOver hints such as "Abre opções de subscrição"). Mixing inside a string 0.
- Main app (1427): formal 108 pron / 72 imp; tu 15 pron / 36 imp. Widgets (420): formal 26 / 22; tu 0 / 5. Kit (112): formal 1 / 4; tu 0 / 4. InfoPlist: formal 4 of 7 (all permission prompts).
- Examples formal: "Veja os eventos do seu calendário…", "Os seus dados aguardam", "Adicione mais tarefas para ver tendências", "Estarão lá quando estiver pronto.", "Atualize para listas ilimitadas.", "Toque duas vezes para expandir. Prima longamente e arraste para reagendar." Examples tu: "Os %@ têm sido os teus dias mais estáveis ultimamente.", "Sê gentil contigo.", "O teu tempo, à vista.", "Todas as funcionalidades Pro estão ativas nos teus primeiros 7 dias — grátis, sem cartão.", "Tu decides quando a mover.", "Toca para reveres ou desativares nas Definições."
- Verdict: **mostly formal (você-form with "o seu")**; tu only in the mood/insight copy, the trial banner and a few hints, so the same screen can address the user both ways. The store description is formal ("Planeie o dia que tem", "Teste todo o Pro grátis").

### Paid tier names in the pt-PT UI
"Taskful Day Pro"; plan labels Mensal / Anual / Vitalício; status "Plano gratuito"; "Iniciar teste gratuito de 7 dias"; "Restaurar compras"; "Desbloquear Pro"; "Gerir subscrição". Store products: "Taskful Day Pro mensal", "Taskful Day Pro anual", "Taskful Day Pro compra única", "Apoiar o programador".

### Portuguese App Store listing (checked 2026-11-19, https://apps.apple.com/pt/app/id6757345400)
- Name: **Taskful Day: Planeador** (US: "Taskful Day: Day Planner")
- Subtitle: **Lista Tarefas & Calendário** (US: "Calm Task Tracker & To-Do List"; FLAG: Title Case, no "de" between Lista and Tarefas, and it says "Calendário" whereas the Spanish says "Agenda")
- In-app purchases (reference): `Apoiar o programador 1,00 €` · `Taskful Day Pro compra única 44,99 €` · `Taskful Day Pro anual 29,99 €` · `Taskful Day Pro mensal 2,99 €`
- Languages line: **Português e mais 33**
- Category: **Produtividade** (also "Utilitários"). The lookup API lists Mac and Watch among supported devices (`MacDesktop`, `Watch4`). Description 3 146 characters, formal register, uses "assinatura" 3 times (Brazilian; see flag) and "ecrã", "Partilha com a família"

---

### 4. WanderWiki (`wanderwiki`, source `WanderWiki/`, ID 6758459119)

### Portuguese coverage (pt-PT)
| Catalog | keys | `pt-PT` translated | % |
|---|---|---|---|
| WanderWiki/Resources/Localizable.xcstrings (main app) | 425 | 425 | 100 % |
| WanderWikiWidget/Localizable.xcstrings | 129 | 129 | 100 % |

No InfoPlist.xcstrings and no AppShortcuts catalog; no permission texts. **Verdict: app is in European Portuguese: yes** (Brazilian traces: "rastreamento", "Ajustes" twice, Title Case, "Teu feedback").

### Glossary
| English term on site | English UI string (key) | pt-PT UI string (verbatim) | Note |
|---|---|---|---|
| Random | `random_mode` | Aleatório | |
| Browse | `browse_title` | Explorar | |
| For You | `for_you_mode` | Para Si | formal "si" (pt-BR "Para Você"); quoted «Para si» in running text. A tu site would write "Para ti" |
| Today in History | `Today in history` / `On This Day` | Hoje na história | both English terms give the same pt-PT; Soon. says "Neste Dia" for the same idea; `feature_history` → "Descubra o que aconteceu hoje na história" |
| On This Day categories | `Events` / `Births` / `Deaths` / `Holidays` | Acontecimentos / Nascimentos / Mortes / Feriados | "Acontecimentos" is pt-PT (pt-BR "Eventos") |
| Tabs | `feed_tab` / `profile_tab` / `settings` | Feed / Perfil / Definições | "Feed" English loanword (also in the pt-PT store text) |
| WanderWiki Plus | `unlock_premium` / `Premium feature` | Desbloquear Premium / Funcionalidade premium | no "Plus" string; tier is "Premium" |
| Monthly / Annual / Weekly / Lifetime | `monthly` / `yearly` / `weekly` / `lifetime` | Mensal / Anual / Semanal / Vitalício | `paywall_monthly_per_month` → "por mês"; `paywall_lifetime_own` → "Tenha o WanderWiki para sempre" |
| Best long-term value | `best_value` | Melhor Valor | Title Case; pt-BR "Melhor Oferta"; Xiangqiful uses "Melhor custo-benefício" |
| Free trial | `%lld-day free trial` / `Start %lld-Day Free Trial` | Teste gratuito de %lld dias / Iniciar Teste Gratuito de %lld Dias | Title Case on the button |
| Free articles per day | `%lld free articles left today` | Restam %lld artigos grátis hoje | |
| Restore purchases | `restore_purchases` | Restaurar Compras | Title Case here, sentence case in other apps |
| Saved | `saved` / `Saved` | Guardados | pt-BR "Salvos" |
| Liked list | `liked` / `like` | Com Gosto / Gosto | pt-BR "Curtidos/Curtir"; "Com Gosto" is awkward; `no_liked_articles_hint` → "Toque no coração nos artigos de que gosta" (formal) |
| Folders | `Folders` / `New folder` | Pastas / Nova pasta | |
| Read aloud | `Listen` | Ouvir | |
| Where Next | `Where next` | E a seguir? | pt-BR "E agora?" |
| Show less / hide | `Show less like this` / `Hide this article` | Mostrar menos deste tipo / Ocultar este artigo | |
| Reader themes | `Reader Theme` | Tema de leitura | |
| Search | `Search Wikipedia` | Pesquisar na Wikipédia | |
| Reading streak | `%lld-day streak` / `Streak reminder` | Sequência de %lld dias / Lembrete de sequência | `Don't break your streak` → "Não interrompa a sua sequência" |
| Widgets | `On This Day`, `Reading Year`, `Continue Reading`, `Got a Minute`, `Two Doors` | Hoje na história, Ano de leitura, Continuar a ler, Tem um minuto?, Duas portas | control `Surprise Me` → "Surpreenda-me" |
| On-device summaries | `AI summary: %@` | Resumo com IA: %@ | |
| 16 topics | `interest_*` | Ciência, … Cinema, Gastronomia, Espaço, Política | pt-PT "Cinema" (Spanish "Cine") |
| No ads | `feature_no_ads` / `onboarding_benefit_no_ads_title` | Experiência sem Anúncios / Sem anúncios. Sem ruído. | `tip_bullet_no_ads` → "Sem anúncios. Sem rastreamento. Sem investidores." FLAG: "rastreamento" is Brazilian, pt-PT "rastreio" |
| Offline reading | `Offline Reading` | Leitura offline | `Ready offline` → "Disponíveis offline" |
| Manage subscription | `manage_subscription` | Gerir Subscrição | Title Case |

Top 10 for the site: Aleatório; Explorar; Para Si; Hoje na história; Acontecimentos; Guardados; Sequência; Pastas; Resumo com IA; Leitura offline.

Other flags:
- `for_you_english_only` → "O feed personalizado está disponível apenas em inglês de momento." Possibly stale against the site's 17 editions (same flag as the other languages). `For You isn't available in %@ yet — showing Random.` → "«Para si» ainda não está disponível em %@ — a mostrar Aleatório."
- Weekly plan exists in the store ("WanderWiki semanal 0,99 €") and the app, and the site does not list it.
- Mixed vocabulary: "Definições" (settings) but "Abrir Ajustes" and "Ative as notificações nos Ajustes do iOS" (Brazilian/pt-BR system word, 2 strings).
- Title Case on buttons ("Restaurar Compras", "Gerir Subscrição", "Iniciar Teste Gratuito de %lld Dias"), a residue of the English source.

### Register (pt-PT)
tu markers 2, formal markers 36, formal imperatives 47, tu imperatives 5 (upper bound; "Abre o artigo", "Volta ao início do artigo" are VoiceOver hints). Formal examples: "Escolha uma categoria para começar um deslize infinito.", "Guarde artigos para ler offline.", "Todos os seus dados foram eliminados.", "Os seus dados precisaram de ser reiniciados…", "Cancele quando quiser.", "Não interrompa a sua sequência". tu examples (the only two): "O teu feedback molda mesmo a próxima versão", "A tua reação sincera molda o que construo". Verdict: **formal**, with two tu strings in the review-prompt copy. Store description formal ("Leia 20 por dia", "ajuda-o a dar com ele", "vai querer ler"); store name uses tu ("descobre e aprende"), so name and body disagree.

### Paid tier names in the pt-PT UI
"Premium" (button "Desbloquear Premium"); plan labels Mensal / Anual / Semanal / Vitalício; lifetime pitch "Tenha o WanderWiki para sempre"; "Melhor Valor"; "Restaurar Compras". Store products: "WanderWiki mensal", "WanderWiki anual", "WanderWiki semanal", "WanderWiki compra única", "Apoiar o programador".

### Portuguese App Store listing (checked 2026-11-19, https://apps.apple.com/pt/app/id6758459119)
- Name: **WanderWiki: descobre e aprende** (US: "WanderWiki: Swipe to Discover")
- Subtitle: **Factos, história, curiosidades** (US: "Daily facts, history & trivia"; "Factos" is the pt-PT spelling)
- In-app purchases (reference): `WanderWiki semanal 0,99 €` · `Apoiar o programador 1,00 €` · `WanderWiki compra única 29,99 €` · `WanderWiki anual 9,99 €` · `WanderWiki mensal 1,99 €`
- Languages line: **Português e mais 33**
- Category: **Ensino** (also "Referência"). Description 3 483 characters, formal register ("Leia", "vai querer ler"), uses "Wikipédia" (pt-PT accent), "subscrição", "Definições", "Partilha com a família"

---

### 5. Xiangqiful (`xiangqiful`, source `Xiangqi/`, ID 6794340136; iPhone, iPad, Mac, Game Center)

### Portuguese coverage (pt-PT)
| Catalog | keys | `pt-PT` translated | % |
|---|---|---|---|
| Xiangqi/Localization/Localizable.xcstrings (main app, includes the paywall) | 3273 | 3273 | 100 % |
| Xiangqi/Localization/InfoPlist.xcstrings | 2 | 2 | 100 % (display name only, stays "Xiangqiful") |

No widget or extension catalogs. Both `pt-PT` and `pt-BR` are present, but **2 703 of 3 275 strings (83 %), and 1 315 of 1 778 strings with 8+ words (74 %), are byte-identical to pt-BR.** Mixed signs: pt-PT choices in UI chrome ("Definições do tabuleiro", "Gerir subscrição", "ficheiro", "Registo da partida", "subscrição", "Inverter tabuleiro", "ecrã" in a few places, "estar a forçar") against Brazilian ones in the lesson and paywall text. **Verdict: app is in European Portuguese: partial.** Quantified Brazilian leaks:
- "Assine o Premium para analisá-la…" and "Assinar" / "Assinar mesmo assim" (3 strings; pt-PT "Subscreva"/"Subscrever")
- "habilidades" (24 strings: "Perfil de habilidades", "Radar de habilidades", "Avaliação de Habilidades"; pt-PT "competências")
- "estar + gerúndio" (4 strings: "deveria estar vencendo", "deveria estar direcionando o jogo"; pt-PT "a vencer")
- clitic before the verb in Brazilian order (6 strings: "O seu adversário precisa de dois lances para te dar xeque-mate", "Eles te atropelaram no tabuleiro", "está te segurando")
- "você" (3 strings), "salvar" (7 strings, chess sense "to save a piece"), "Fazer upgrade para o Premium", "Treinador" ok
- one wrong word: "Então as pretas afastam a ecrã" (the cannon's "screen" rendered with the unrelated pt-PT "ecrã"; the 6 "ecrã" strings are about the xiangqi screen piece, not a display)
- "xeque" pattern fine; "Trilhos do Cavalo" and "Trilho de Mate" are pt-PT/pt-BR neutral.

### Glossary
| English term on site | English UI string (key) | pt-PT UI string (verbatim) | Note |
|---|---|---|---|
| Tabs | `tab.dashboard`, `tab.play`, `tab.training`, `tab.analysis`, `tab.progress` | Início, Jogar, Treino, Análise, Progresso | |
| Game Review | `analysis.review.title` | Revisão da partida | |
| Analyze | `analysis.analyse` | Analisar | |
| Move grades | `classification.best/great/good/book/inaccuracy/mistake/blunder` | Melhor, Ótimo, Bom, Livro, Imprecisão, Erro, Erro grave | `Book` → "Livro" (opening book; Spanish "Teoría"); `Blunder` → "Erro grave" |
| Accuracy | `analysis.accuracy.title` | Precisão | |
| Estimated rating | `progress.estimatedRating` | Classificação estimada | |
| Skill profile / radar | `progress.radar.title` | Perfil de habilidades | FLAG: Brazilian "habilidades" (pt-PT "competências"); paywall "Radar de habilidades completo" |
| Weakness trends | `progress.weaknesses.title` | Tendências de fraquezas | |
| Five skills | `skill.category.tactics/defense/positioning/endgame/openings` | Táticas, Defesa, Posicionamento, Final, Aperturas → "Aberturas" | "Táticas" plural against "Tática" in module names |
| Phases | `phase.opening/middlegame/endgame` | Abertura, Meio-jogo, Final | but lesson track `endgame` → "Final de Jogo" (see flag) |
| Today's plan | `training.plan.title` | Plano de hoje | |
| Lessons / 8 tracks | `module.lessons.title`; `lesson.track.*.title` | Lições; Fundamentos, Aberturas, Defesa do Palácio, Táticas de Canhão, Técnica de Cavalo, Meio-jogo, Final de Jogo, Avançado | Title Case |
| Skill assessment | `module.skillAssessment.title` | Avaliação de Habilidades | Title Case + "Habilidades" |
| Drill modules | `module.tactics.title`, `cannonRange`, `horseTrails`, `palaceWorkshop`, `endgameStudio`, `openingLab`, `mateTrail`, `tacticCards`, `handicapHouse` | Pátio de Tática, Alcance do Canhão, Trilhos do Cavalo, Oficina do Palácio, Estúdio de Finais, Laboratório de Aberturas, Trilho de Mate, Cartas de Tática, Casa de Handicap | FLAG: Title Case; `cannonRange` is "Alcance do Canhão" (Spanish "Galería de Cañones") and `handicapHouse` is "Handicap" not "Hándicap" |
| Mate problems / puzzles | `training.kind.mate` / `progress.stat.puzzles` | Problema de mate / Problemas | |
| Coach hints | `paywall.benefit.coach` | Dicas ilimitadas do treinador durante a partida | "Dica" for hint (same as Tare) |
| Piece style (setting) | `board.pieceSet.title` / `.traditional` / `.western` / `.hybrid` | Peças / Tradicional / Ocidental / Híbrido | **setting `Pieces` → "Peças"** |
| Piece set (finish) | `board.pieceFinish.title` and values | Acabamento das peças; Marfim, Madeira Entalhada, Melamina de Clube, Jade, Seixo de Rio, Porcelana, Laca Dourada, Jacarandá e Latão | FLAG: `game.settings.pieceSet` (English "Piece set") is just "Peças", the same label as `board.pieceSet.title`, so the board-settings sheet loses the style/finish difference. Title Case |
| Characters | `board.charset.title` / `.traditional` / `.standard` | Caracteres / Tradicional / Simplificado | |
| Notation | `board.notation.title` / `.wxf` / `.chinese` | Notação de lances / WXF / Chinês | `game.settings.notation` → "Notação" |
| Boards | `board.theme.*` | Buxo, Jacarandá, Mesa de Pedra do Parque, Tapete de Clube, Rolo de Papel Xuan, Laca Vermelha e Ouro, Mármore e Jade; `board.3d.title` → "Tabuleiro 3D" | Boxwood = "Buxo" (pt-PT; Spanish "Boj"), Rosewood = "Jacarandá" (Spanish "Palisandro") |
| Flip board / New game | `game.toolbar.flip` / `mac.command.newGame` | Inverter tabuleiro / Nova Partida | |
| Premium | `settings.premium.upgrade` | Fazer upgrade para o Premium | `settings.premium.name` → "Xiangqiful Premium" |
| Free | `settings.premium.free` | Plano gratuito | |
| Monthly / Yearly / Lifetime | `paywall.plan.monthly` / `.yearly` / `.lifetime` | Mensal / Anual / Vitalício | consistent, unlike the Spanish app ("Vitalicio" vs "De por vida"): `settings.premium.lifetimeNoManage` → "Vitalício — nada para renovar, nada para cancelar" |
| Best value | `paywall.bestValue` | Melhor custo-benefício | WanderWiki: "Melhor Valor" |
| Start free trial | `paywall.startTrial` | Iniciar teste grátis | Taskful Day: "teste gratuito" |
| Restore purchases | `paywall.restore` | Restaurar compras | |
| Subscribe | `paywall.subscribe` (button text) | Assinar | not looked up by key: 3 strings "Assinar", "Assinar mesmo assim", "Assine o Premium para analisá-la…"; the settings strings say "subscrição" ("A subscrição é renovada automaticamente…", "Gerir subscrição", "Já tem uma subscrição") |
| Check / checkmate / stalemate | `game.status.check` / `game.reason.checkmate.win` / `gc.achievement.stalemate_win.title` | Xeque / Xeque-mate / Afogamento | stalemate = "afogamento" (xiangqi term: no legal move loses); perpetual check = "Xeque Perpétuo"; "perseguição perpétua" for the chase rule |
| Sides | `board.side.red` / `board.side.black` | Vermelho / Preto | |
| Palace / river | (text) | palácio / rio | "Defesa do Palácio", "Oficina do Palácio" |

**pt-PT piece names the app uses** (`piece.*`): General, Conselheiro (advisor), Elefante, Cavalo (horse), **Carruagem** (chariot; FLAG: the Brazilian/Wikipedia word, pt-PT chess calls the rook "torre" and xiangqi texts also use "carro"), Canhão (cannon), Soldado. Lower-case inline forms: general, conselheiro, elefante, cavalo, carruagem, canhão, soldado. The cannon's "screen" is "anteparo" (`lesson.track.cannonTactics.summary` → "Anteparos, baterias, e os padrões que eles criam"), though some strings use "ecrã" for it (the error above); the horse's "leg" is "perna" ("A regra da perna do cavalo").

Top 10 for the site: Xeque-mate; Afogamento; Carruagem; Canhão; Cavalo; Conselheiro; Palácio; Peças; Aberturas; Revisão da partida.

Other flags:
- Stale string: `paywall.benefit.opponents` ("Todos os 40 adversários, desbloqueados de uma só vez") is unused in code (per the German note); do not use it.
- Title-case module and track names ("Pátio de Tática", "Cartas de Tática", "Final de Jogo") carry over from English.
- `diagnostic.engine.nnueMissing` → "O ficheiro de avaliação do motor está ausente. Reinstale a app para jogar contra o computador." (pt-PT ficheiro/app, formal imperative).
- "partida" for game and "lance" for move are used consistently (278 strings with "lance"); "xadrez" appears in comparisons ("Esse é o hábito do xadrez").

### Register (pt-PT)
tu markers 9 (including false positives like the achievement title "Conhece-te a Ti Mesmo" and "te dar xeque-mate"), formal markers 275, formal imperatives 154, tu imperatives 19 (upper bound; mostly drill technique labels "Abre com xeques consecutivos", "Termina em xeque-mate", "Usa duas, o mesmo que uma bateria"). 3 strings mix both ("O seu adversário precisa de dois lances para te dar xeque-mate", "Eles te atropelaram… coloque as suas carruagens", "Veja qual das cinco habilidades está te segurando"). Verdict: **formal / você-form dominant** ("o seu", "Veja", "Analise", "Jogue o lance vencedor", "Escolha"), with a small tu pocket in the drill technique tags. The store subtitle ("Aprenda xiangqi: tática e IA") and description ("Não precisa de ler… ensina-lhe") are formal.

### Paid tier names in the pt-PT UI
"Xiangqiful Premium"; plan labels Mensal / Anual / Vitalício; "Plano gratuito"; "Iniciar teste grátis"; "Restaurar compras"; "Gerir subscrição". Store products: "Premium mensal", "Premium anual", "Premium vitalício", and tip items "Apoiador", "Apoio enorme", "Um café".

### Portuguese App Store listing (checked 2026-11-19, https://apps.apple.com/pt/app/id6794340136)
- Name: **Xiangqiful: Xadrez Chinês** (US: "Xiangqiful Learn Xiangqi & AI"; Title Case "Chinês")
- Subtitle: **Aprenda xiangqi: tática e IA** (US: "Chinese Chess Tactics Trainer"; formal)
- In-app purchases (reference): `Premium anual 9,99 €` · `Premium mensal 1,99 €` · `Apoiador 5,99 €` · `Apoio enorme 9,99 €` · `Um café 1,99 €` · `Premium vitalício 22,99 €`
- Languages line: **Português e mais 33**
- Category: **Tabuleiro** (also "Jogos"). The lookup API lists Mac among supported devices. Description 4 098 characters: "Sete novos tabuleiros e sete novos conjuntos de peças…", "80 lições grátis", formal, uses "telemóvel", "Definições", "subscrição" absent

---

### 6. Clippet (`clippet`, source `clipboard/`, ID 6829498729, NOT released)

Built from the English page `_apps/clippet.md`, the catalogs, and `~/Downloads/clipboard/marketing/aso/` (listing.json, purchases.json).

### Portuguese coverage (pt-PT)
| Catalog | keys | `pt-PT` translated | % |
|---|---|---|---|
| clipboard/Localizable.xcstrings (main app, paywall) | 638 | 638 | 100 % |
| clipboard/AppShortcuts.xcstrings (Siri and Spotlight) | 2 | 2 | 100 % |
| clipboard/InfoPlist.xcstrings | 7 | 7 | 100 % (permissions: contacts, Face ID, photo library, Reminders; plus the two file-type names) |
| ClipboardKit Localizable.xcstrings | 26 | 26 | 100 % |
| ClipboardKeyboard Localizable + InfoPlist | 104 + 1 | 104 + 1 | 100 % |
| ClipboardAction Localizable + InfoPlist | 1 + 1 | 1 + 1 | 100 % |
| ClipboardWidgets Localizable + InfoPlist | 63 + 1 | 63 + 1 | 100 % |
| ClipboardShare Localizable + InfoPlist | 28 + 1 | 28 + 1 | 100 % |
| ClipboardMacBridge Localizable.xcstrings | 19 | 19 | 100 % |

Total 892 keys, 892 translated (100 %). Only 36 % of strings equal pt-BR and only 2 % of long strings do: this is the most carefully localized pt-PT of the six. Plural categories include the `many` form ("%lld de elementos mais antigos estão ocultos"). **Verdict: app is in European Portuguese: yes.** Residual Brazil-neutral wording only: "Copia um PDF e ele aparece aqui" (12 strings use "ele aparece" for an item; pt-PT would say "aparece aqui"), "cobrança" in the prepared product descriptions ("Todas as funções Pro, cobrança mensal.").

Permission prompts (verbatim, tu): contacts "Guarda um número de telefone ou um cartão de visita de um elemento como novo contacto quando escolhes Adicionar aos Contactos."; Face ID "Permite ao Bloqueio da app desbloquear o Clippet por ti, para que só tu possas ver os teus elementos."; photo library "Guarda na tua fototeca a fotografia ou o vídeo de um elemento quando escolhes Guardar em Fotografias."; Reminders "Adiciona um lembrete à app Lembretes quando executas uma ação de lembrete que configuraste para um elemento."

### Glossary
| English term on site | English UI string (key) | pt-PT UI string (verbatim) | Note |
|---|---|---|---|
| Clipboard | `Clipboard Access` | área de transferência ("Acesso à área de transferência") | store name "Clippet: Área de Transferência" (Title Case in the prepared listing) |
| Clip | `Clip` / `Search Clips` | Elemento / Pesquisar elementos | pt-BR "Item"; plural variations ("%lld elemento mais antigo está oculto", …) |
| Library | (text) | biblioteca ("Sem o Clippet Pro, a biblioteca mostra os elementos afixados…") | the photo library is "fototeca" |
| Smart Actions | `Smart Actions` | Ações inteligentes | |
| Custom actions | `Custom Actions` | Ações personalizadas | |
| Boards | `Boards` / `New Board` / `Add to Board` | Quadros / Novo quadro / Adicionar ao quadro | **quadros** (Spanish "tableros") |
| Tags | `Tags` | Etiquetas | |
| Pin | `Pin` / `Pinned` | Afixar / Afixados | widget "Pinned Clips" → "Elementos afixados"; Soon. says "Fixar no topo" (inconsistent across the portfolio) |
| Quick Paste | `Quick Paste` | Colagem rápida | |
| Quick Add (widget) | `Quick Add` | Adição rápida | noun phrase; `Add Clip` → "Adicionar elemento" |
| Paste | `Paste` | Colar | |
| App Lock | `App Lock` | Bloqueio da app | `Face ID Lock` → "Bloqueio com Face ID" |
| iCloud Sync | `iCloud Sync` | Sincronização do iCloud | |
| Backup | `Backup` | Cópia de segurança | file type "Cópia de segurança do Clippet" (pt-BR "Backup") |
| Auto-delete | `Auto-Delete` | Apagar automaticamente | `Auto-Delete Sensitive Clips` → "Apagar automaticamente elementos sensíveis" |
| Menu bar | `Menu Bar` | Barra de menus | |
| Open at login | `Open at Login` | Abrir ao iniciar sessão | |
| Save to Clippet | `Save to Clippet` | Guardar no Clippet | |
| Clippet keyboard | `Clippet Keyboard` | Teclado do Clippet | |
| Quick Look | `Quick Look` | Vista rápida | pt-BR "Visualização Rápida" |
| Copy as plain text | `Copy as Plain Text` | Copiar como texto simples | |
| Search | `Search` | Pesquisar | |
| Settings | `Settings` | Definições | |
| Content types | `Link`, `Images`, `Videos`, `PDFs`, `Audio`, `Files`, `Code`, `Text` | Ligação, Imagens, Vídeos, PDF, Áudio, Ficheiros, Código, Texto | "Ligação" for Link (pt-BR keeps "Link"); the prepared keywords list both "ligação,link" |
| Sensitive | `sensitive content` | conteúdo sensível | |
| Older clips hidden | `%lld older clips are hidden` | plural variations ("%lld elemento mais antigo está oculto", …) | `See Older Clips` → "Ver elementos mais antigos"; `Not Now` → "Agora não" |
| Widgets | `Latest Clip`, `Pinned Clips`, `Add Clip`, `Recently copied` | Último elemento, Elementos afixados, Adicionar elemento, Copiados recentemente | |
| Free trial | `Start Free Trial` / `%lld days free` | Iniciar avaliação gratuita / plurals "%lld dia grátis", "%lld dias grátis" | "avaliação gratuita" here against "teste gratuito" in Taskful Day/WanderWiki/Xiangqiful and "período gratuito" in Soon. |
| Lifetime | `Lifetime` / `Buy Lifetime` | Vitalício / Comprar Vitalício | consistent; planned store product "Clippet Pro vitalício" |

Top 10 for the site: Área de transferência; Elemento; Ações inteligentes; Quadros; Etiquetas; Afixar; Colagem rápida; Bloqueio da app; Cópia de segurança; Vista rápida.

### Register (pt-PT)
tu markers 102, formal markers 1, tu imperatives 99, formal imperatives 0. Per catalog: main app 81 tu pron / 59 tu imp; Keyboard 12 / 23; Widgets 5 / 13; Kit 2 / 0; InfoPlist 2 / 4. Examples: "Permite o acesso total para ver os teus elementos", "Abre o Clippet e desbloqueia-o para veres aqui os teus elementos.", "Escreve para pesquisar os teus elementos", "Se o Touch ID não te reconhecer, podes introduzir a palavra-passe do Mac.", "Cancela-a em Gerir subscrição…". Verdict: **tu, fully consistent**, in-app, permission prompts and the prepared store listing ("Tudo o que copias", "Guarda ao longo do dia").

### Paid tier names in the pt-PT UI
**"Clippet Pro"**; "Obter o Clippet Pro" (purchase button); plan labels Mensal / Anual / Vitalício; "Iniciar avaliação gratuita"; "Restaurar compras"; "Gerir subscrição"; "Subscrever mensalmente", "Subscrever anualmente". Planned store product names (`marketing/aso/purchases.json`, pt-PT): "Clippet Pro mensal", "Clippet Pro anual", "Clippet Pro vitalício".

### Portuguese App Store listing
Not live: https://apps.apple.com/pt/app/id6829498729 returned HTTP 404 on 2026-11-19 and the lookup API (country=pt) returned no results. The prepared listing (`~/Downloads/clipboard/marketing/aso/listing.json`, pt-PT; unpublished, reference only):
- Name: **Clippet: Área de Transferência**
- Subtitle: **Copiar e colar com histórico**
- Promotional text: "Tudo o que copias, guardado. Textos, ligações, imagens, PDF e código voltam numa pesquisa no Clippet, um histórico da área de transferência para iPhone, iPad e Mac."
- Terms in the description: área de transferência; elemento; Ações inteligentes; "aplicação" (the description says "aplicação", the app UI says "app": FLAG, pick one); ficheiros; ligações; fototeca; "no iPhone, no iPad e no Mac". Register tu.
- Keywords pt-PT (iOS): teclado,gestor,copia,cola,texto,ligação,link,notas,excertos,widget,sincronizar,código,guardar,rápido
- Languages line and category: not available (page not live).

---

### Cross-app terms (pt-PT, as the apps write them)
- Settings = Definições (all six; WanderWiki "Ajustes" twice in sentences); Restore purchases = Restaurar compras (WanderWiki "Restaurar Compras"); Manage subscription = Gerir subscrição; subscription = subscrição (Xiangqiful paywall still says "Assinar/Assine" in 3 strings; Taskful Day's store description says "assinatura").
- Free = Gratuito (Soon.) / Plano gratuito (Taskful Day, Xiangqiful) / versão gratuita (Taskful Day body) / artigos grátis (WanderWiki); Free trial = Período gratuito (Soon.) / Teste gratuito (Taskful Day, WanderWiki) / Teste grátis (Xiangqiful) / Avaliação gratuita (Clippet). Four wordings for one concept; the site should choose "teste gratuito".
- Monthly / Yearly = Mensal / Anual; Weekly = Semanal (WanderWiki); **Lifetime = Vitalício in all six** (store products say "compra única" for Soon., Taskful Day, WanderWiki and "vitalício" for Xiangqiful, Clippet).
- Streak = Sequência (Soon., Taskful Day "Sequências", WanderWiki).
- Countdown = Contagem decrescente; Moment = Momento; Memory = Memória; On This Day = Neste Dia (Soon.) / Hoje na história (WanderWiki).
- Hint = Dica (Tare, Xiangqiful; Spanish "Pista"); Level = Nível; Chapter = Capítulo; Beam = Haste; Pin = Fixar (Soon.) / Afixar (Clippet).
- Add = Adicionar; Save = Guardar; Share = Partilhar; Search = Pesquisar; File = Ficheiro; Phone = telemóvel; app = app (Clippet store text "aplicação").
- Lock Screen = Ecrã de Bloqueio (preferred; Soon. also writes "ecrã bloqueado"); Home Screen = Ecrã Principal / ecrã inicial; menu bar = barra de menus; Quick Look = Vista rápida; photo library = fototeca; widget = widget; App Lock = Bloqueio da app; backup = cópia de segurança.
- Free-text register: tu in Soon. (main app, permission prompts, store text) and Clippet (everything); formal in Tare, Taskful Day, WanderWiki, Xiangqiful; mixed in Soon.'s widgets and Taskful Day's insights.

### Flags (app-side string bugs, register mixes, missing Portuguese)
1. **Register split, no single voice.** Counted across the six apps: tu markers 182 strings (Clippet 102, Soon. 54, Taskful Day 15, Xiangqiful 9, WanderWiki 2, Tare 0) against formal markers 487 (Xiangqiful 275, Taskful Day 139, WanderWiki 36, Soon. 34, Tare 2, Clippet 1). By number of apps: 2 tu (Soon. mostly, Clippet), 4 formal. The site (and the ES precedent: tu) needs a decision; the apps themselves do not give a single answer, and each app's wording should be checked before quoting a UI string.
2. **Soon. mixes tu and formal inside one catalog** (main app tu 44 / formal 13; widgets tu 8 / formal 21; permission prompts tu) and uses three terms for Lock Screen / Home Screen ("ecrã bloqueado" / "ecrã de bloqueio", "Ecrã Principal" / "ecrã inicial"), "Tempo" / "Meteorologia" / English "Apple Weather" for weather, and "Aniversário" for both Birthday and Anniversary. Brazilian leftovers: "A cada %lld" (15), "Roupa para o clima", "a cada dia".
3. **Xiangqiful's pt-PT is largely Brazilian text** (83 % of strings and 74 % of long strings identical to pt-BR; "Assine", "habilidades", "estar vencendo", clitic-before-verb, "você"; one string rendering the cannon "screen" with "ecrã"). Needs a proofread pass by a pt-PT speaker before any pt-PT site copy quotes its UI; the paywall "Assinar" strings are user-visible. Also three pt-PT forms for the same label ("Peças" for both the style and the finish setting).
4. **Taskful Day**: verified the known ISSUES.md item (line 1001): the pt-PT catalog is consistent on "subscrição" (7) and "Vitalício" (6) and uses no "assinatura"; Apple's pt-PT system word is "Subscrições"; the "Assinaturas" in the issue is the pt-BR wording. The inconsistency that exists is the **store description**, which says "assinatura" 3 times. Other: "Adicionar rapido" (missing accent), "Adiar para hoje" / "Transportar" / "Mover … para a frente" for carry forward, "fluindo" gerund, English "insight" in 3 strings, "foco" family (Focar / Foco / Modo de foco).
5. **WanderWiki**: "Para Si" (formal "si") with a store name that uses tu ("descobre e aprende"); Title Case residue ("Restaurar Compras", "Gerir Subscrição", "Melhor Valor"); "rastreamento" (Brazilian) and "Ajustes" in 2 strings; "Com Gosto" for Liked; the `for_you_english_only` string may be stale against the site's 17 editions; the weekly plan is not on the site.
6. **Tare**: "Seus para sempre" (Brazilian possessive) in the unlock text; formal "Toque duas vezes" hints but a tu store description; "tabuleiro" is the tray in the UI; chapter names Title Case; Tare has no pans.
7. **Lifetime/Vitalício is now consistent** (unlike Spanish): all six pt-PT catalogs say "Vitalício"; the store product names say "compra única" for Soon., Taskful Day, WanderWiki and "vitalício" for Xiangqiful, Clippet.
8. **Trial wording**: four terms (Período gratuito, Teste gratuito, Teste grátis, Avaliação gratuita); Pin: "Fixar" (Soon.) vs "Afixar" (Clippet, Apple's pt-PT term).
9. **Store listings**: subtitles in Title Case with no "de" ("Lista Tarefas & Calendário"), Soon.'s subtitle "Casamento, Viagem & Contagem" omits Bebé; names "Soon. Dias Até Grandes Eventos", "Tare: Puzzle de Equilíbrio", "Taskful Day: Planeador" (pt-PT "planeador"), "WanderWiki: descobre e aprende", "Xiangqiful: Xadrez Chinês". Descriptions use "ecrã", "subscrição" (except Taskful Day's "assinatura"), "Partilha com a família" (and "Partilha entre Familiares" in one block) for Family Sharing; the registers per listing: Soon./Tare tu, Taskful Day/WanderWiki/Xiangqiful formal, Clippet tu.
10. **Missing Portuguese**: only non-user-facing keys (`Soon` in InfoPlist, `%@ ` and `%@ %@` in Soon. widgets) and two Taskful Day Kit strings (`End focus session`, `Extend focus session`, fall back to English on the Watch). AppShortcuts/Siri catalogs exist and are 100 % Portuguese for Soon., Taskful Day (iPhone and Watch) and Clippet; Tare, WanderWiki and Xiangqiful have none. Tare, WanderWiki and Xiangqiful have no permission prompts to translate (Xiangqiful InfoPlist is just the display name).
11. **Clippet is unreleased**: the store page and the lookup API return nothing for pt; the pt-PT listing under `~/Downloads/clipboard/marketing/aso/` is the only Portuguese store source and is unpublished ("aplicação" in the description against "app" in the UI; "cobrança" in the product descriptions).
12. **Coverage correction to the Spanish glossary**: this run counted Clippet at 892 keys across 13 catalogs (638 main), consistent with the Spanish part.
