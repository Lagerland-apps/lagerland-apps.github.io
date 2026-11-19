# Apple's own Italian names (it, Italy)

Part of the language sheet for Italian (`_i18n/it.md`, not yet written). Verified 2026-11-19 on Apple's Italy pages (source per row). Use these exactly; never invent an Apple name. Rows marked "not verified" have no Apple Italy page that names them.

Checked 2026-11-19 against Apple's live Italy pages: fetched directly with curl and `Accept-Language: it-IT`, raw HTML read for characters. Only `support.apple.com/it-it/...`, `www.apple.com/it/...` and `apps.apple.com/it/...` (page `lang="it"`, footer "Italia" on support pages, App Store prices in EUR) were used; the badge artwork came from Apple's marketing-tools API (`it-it` badge files). The iPhone, Apple Watch and Mac user guides on support.apple.com/it-it are for iOS 27, watchOS 27 and macOS 27.

## Key answers

1. **Register: tu.** Apple Italy addresses the reader with "tu" throughout. Counted on 111 pages and sections (iPhone, Apple Watch and Mac guide pages, support articles 118428, 118223, 108906, 102420, 105055, apple.com/it/health, apple.com/it/privacy, the Italian App Store page): "Tocca" 357 times, "Tocchi" 0; "Fai clic" 48, "Faccia clic" 0; "tuo/tua/tuoi/tue" 428; zero Lei imperatives ("Apra", "Vada", "Scelga", "Selezioni", "Prema") and no "Suo/Sua" for the reader. The user is also addressed with "puoi" (260). Apple Italy is gender-inclusive in the iOS 27 guide ("tuo figlio o tua figlia", "amici e amiche", "la persona responsabile della famiglia", "chi ha sviluppato l'app").
2. **App Store badge wording (Apple's Italian artwork, read from the rendered SVG, not translated):** "Download on the App Store" = **Scarica su / App Store** (two lines: "Scarica su" small, "App Store" large; file title `Download_on_the_App_Store_Badge_IT_RGB_blk_100317`). Mac variant = **Scarica su / Mac App Store** (`Download_on_the_Mac_App_Store_Badge_IT_RGB_blk_100317`). Source: https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/it-it and https://tools.applemediaservices.com/api/badges/download-on-the-mac-app-store/black/it-it. The artwork is outlined paths, so there is no text node; the words were read from the image rendered with rsvg-convert.
3. **Quote marks.** Italian guides AND support articles both use English-style curly double quotes “ ” (U+201C/U+201D) for UI labels, with **no space inside** and the **punctuation after** the closing mark ("Tocca “Tempo di utilizzo”, quindi tocca “Limiti di tempo”."; 961 “ against 0 « » on 111 pages). Italian guillemets « » are not used by Apple Italy for UI labels; the only « » hit is inside a developer's own App Store text (Tare: "funziona con «In famiglia»"), which is not Apple's wording. Single-word labels are bare and capitalised (Tocca Abbonamenti, Tocca Sfoglia, Tocca Sonno, Notifiche, Fotocamera). A quote inside a quote uses single curly marks: “Orari di ‘Tempo di utilizzo’”. **Menu paths** use ">" with NBSP (U+00A0) before it and a normal space after, labels bare: "vai in Impostazioni > Privacy e sicurezza > Tracciamento" (raw: `Privacy&nbsp;e sicurezza`), in the iPhone guide with a tiny Settings icon after the app name. Older articles use plain spaces ("Vai su Impostazioni > Accessibilità."). The verb is "Vai in Impostazioni", "Vai su Impostazioni" or "Vai nell’app Impostazioni".
4. **Numbers and dates.** Decimal comma ("11,3 MB", "12,9"), thousands separator a period ("100.000 volte al giorno"). **Percent: no space** ("al 30%", "al 200% e oltre"; 2 of 2 hits in running text, 0 spaced); the unit space before MB, GB, ore, giorni, anni, notti is mostly U+00A0 in articles and guides ("5 GB", "14 giorni", "13 notti") but a plain space in the App Store "Dimensioni 11,3 MB". Prices: `2,99 €` = comma, **U+00A0**, € (raw `2,99&nbsp;€`; the Italian App Store prints "Gratis" for free). Dates in prose: **"1 ottobre 2026"**, "18 settembre 2026", "30 aprile 2026" (cardinal day, no "º", no leading zero, lowercase month, no comma, no "del"); article footers: "Data di pubblicazione: 29 settembre 2026" (NBSP after the colon). App Store version dates: "27 ott", "9 ott" (short lowercase month, no period), relative "6 gg fa". Time in running text: 24-hour or bare hours with "alle": "Imposta una sveglia alle 7 del mattino", "dalle 11 alle 13", "alle 9" (examples in Calendar and Clock guides); an "HH:MM" form with a colon was not seen on the pages fetched. Durations: "24 ore", "da 24 a 48 ore", "1 ora" (NBSP).
5. **Gender and articles.** il Mac, l’iPhone, l’iPad, **l’Apple Watch** (masculine: "l’Apple Watch", "il tuo Apple Watch"), l’Apple TV; **la Dynamic Island** (feminine: "nella Dynamic Island"); **l’app** (feminine: "un’app", "le app", "l’app Salute"; 154 "l’app", 87 "un’app", 105 "le app", 0 "la app"); **App Store** after prepositions is mostly bare ("su App Store" 12, "da App Store" 7, "di App Store" 15) with the article only in article 118428 ("Nell’App Store, fai clic su…"). iPhone, iPad and Apple Watch are mostly bare after "su" ("su iPhone" 525, "su Apple Watch" 172, "sul Mac" 54, "sull’iPhone" 3). iCloud has no article ("su iCloud", "in iCloud"). "app" is the word (1037 "app"; "applicazione" only in 4 old-article spots); plural is invariable: "le app" (never "apps"). **Salute app = "l’app Salute"**; "iCloud Drive", "Face ID", "Touch ID", "Apple Pay", "AirDrop", "Siri", "Wi-Fi" (plain hyphen), "Bluetooth" stay English; "iOS 27" etc. with NBSP. Apple Italy puts U+2011 NON-BREAKING HYPHEN inside some English-style compounds ("acquisti in‑app" on the App Store page, "on‑device", "end‑to‑end", "USB‑C", "time‑lapse"), but writes "Acquisti in-app" with a plain hyphen in the Information row.
6. **Key names (Apple Italy):** Health app = **Salute** ("l’app Salute"), Apple Health = **Salute** (apple.com/it page title "Salute - Apple (IT)"; never "Apple Salute"); HRV = **variabilità della frequenza cardiaca (HRV)** (Apple Italy keeps "HRV"); resting heart rate = **“Battito cardiaco a riposo”** (Watch label) / frequenza cardiaca a riposo; sleep stages Awake/REM/Core/Deep = **Veglia / REM / Principale / Profondo** (also “Sonno profondo”); VO2 max = **VO2 max** (marketing) / VO2 massimo (article); Cardio Fitness = **tono cardiovascolare**; Workouts = **allenamenti** (app **Allenamento**); Screen Time = **“Tempo di utilizzo”**; Downtime / App Limits = not verified (iOS 27 guide: “Orari di ‘Tempo di utilizzo’”, “Limiti di tempo”); Focus = **full immersion** ("la full immersion Sonno", "una full immersion"); Sleep Focus = **full immersion Sonno**; Family Sharing = **“In famiglia”**; Home Screen = **schermata Home** (capital H); Lock Screen = **schermata di blocco**; widgets = **widget** (invariable); Live Activities = **attività in tempo reale**; Smart Stack = **raccolta smart** (“Raccolta smart”); StandBy = **StandBy** (kept English, "modalità StandBy"); Dynamic Island = **Dynamic Island**; Shortcuts = **Comandi Rapidi** (app "Comandi Rapidi", user shortcuts "comandi rapidi"); Wallet = **Wallet** (not translated; "Wallet di Apple"); Settings = **Impostazioni** (Mac: **Impostazioni di Sistema**); Sign in with Apple = **“Accedi con Apple”**; Apple Account = **Apple Account** (kept English, capital A; "ID Apple" not used); App Tracking Transparency = Apple's wording **"tracciamento"**: toggle **“Richiesta tracciamento attività”**, buttons **Consenti** and **Chiedi all'app di non eseguire il tracciamento**, path Impostazioni > Privacy e sicurezza > **Tracciamento**; IDFA = **identificativo per gli inserzionisti (IDFA)**; iCloud backup = **Backup iCloud** (switch label “Backup iCloud”), "backup su iCloud" in prose; Subscriptions path = **In Impostazioni, tocca il tuo nome. Tocca Abbonamenti. Tocca l'abbonamento. Tocca Annulla abbonamento.**; Request a refund = **Richiedere un rimborso** (article title) / **“Richiedere un rimborso”** (menu item, after “Vorrei”) on reportaproblem.apple.com; In-App Purchases = **Acquisti in-app** (store label; "acquisti in‑app" with U+2011 in the price line); "Data Not Collected" = **Dati non raccolti** (sub-line "Lo sviluppatore non raccoglie alcun dato da quest’app."); section name = **Privacy dell’app**; Get button = **Ottieni**; Game Center = **Game Center** (app **Apple Games**); Weather = **Meteo**; Calendar = **Calendario**; Reminders = **Promemoria**; Files = **File**; Photos = **Foto**; Camera = **Fotocamera**; Clock = **Orologio**.
7. **Dash and anglicism habits.** Apple Italy writes **almost no dashes in running text** (en dash only in ranges like "II–X" in a developer's text, 1 spaced en dash and 1 spaced em dash only inside developer app titles; the guides use commas, colons, semicolons and parentheses instead). Apple Italy keeps these English: **widget** (183 hits, invariable), **app** (1037), **feedback** (114, "feedback aptico"), **full immersion** (172, used as the Italian name of Focus), **backup** (65), **link**, **online/offline**, **smart** ("raccolta smart"), **screenshot** (on the App Store page: "Visualizza screenshot, valutazioni e recensioni"; in guides "scattando uno screenshot"), **privacy**, **email**, **tracker** / "tracking" (apple.com/it/privacy; guides prefer "tracciamento"). **Screen capture**: Apple writes "screenshot" for the picture and "Acquisire e registrare lo schermo" for the action; "schermata" (213) means a screen or view of an app ("la schermata Home", "la schermata di blocco", "La schermata Sonno"). **"Istantanea" is not used for screenshots** (2 hits, both "istantanea di backup" in an iCloud article). Apple also uses the Italian forms: "tocca", "tieni premuto", "scorri", "fai clic" (Mac), "scegli", "seleziona", "attiva/disattiva", "impostazioni", "di default" (not "predefinito" in prose: "di default", "attivo di default").

How Apple writes them in running text:
- **App names**: Apple writes "l’app" + capitalised name, no quotes, no italics: l’app Salute, l’app Fitness, l’app File, l’app Promemoria, l’app Impostazioni, l’app Orologio (not seen as such; "in Orologio"), l’app Diario, l’app Foto, l’app Comandi Rapidi, l’app Wallet, l’app Mappe, l’app Apple Games, l’app ECG, l’app Parametri Vitali, l’app Preparazione, l’app Attività, l’app Allenamento, l’app Sonno, l’app Mindfulness, l’app Rumore, l’app Livelli O₂, l’app Farmaci (Apple Watch), l’app Monitoraggio Ciclo, l’app Meteo (articles), l’app Calendario, l’app App Store ("Vai nell’app App Store"). So the word is **app**, never "applicazione" in current copy. The apps are often named without "l’app" too ("in Salute", "in Fitness", "in Calendario", "in Orologio", "su Wallet").
- **Features and multi-word setting labels** go in curly double quotes “ ” with no space inside: “Tempo di utilizzo”, “In famiglia”, “Non disturbare”, “Accedi con Apple”, “Backup iCloud”, “Sincronizza questo iPhone”, “Annulla abbonamento” (in the iPhone guide; bare "Annulla abbonamento" in article 118428), “Richiesta tracciamento attività”, “Dettagli Salute”, “Dati sanitari”, “Elenco di controllo Salute”, “Monitoraggio ciclo”, “Stato d’animo”, “Benessere mentale”, “Consumo adattivo”, “Risparmio energetico”, “Raccolta smart”, “Appunti condivisi”. 961 “ ” counted. Single-word labels are bare: Abbonamenti, Notifiche, Sfoglia, Riepilogo, Sonno, Farmaci, Amici, Siri, StandBy, Aspetto.
- **Capitalisation**: sentence style for most feature names; Apple Italy capitalises the Watch app and some marketing names: Monitoraggio Ciclo, Parametri Vitali, Centro di Controllo, Centro Notifiche, Comandi Rapidi, Battito Cardiaco (older text). Common nouns stay lowercase: la schermata di blocco, la schermata Home (capital H), la modalità scura, la modalità Aereo (capital A), le notifiche, una full immersion (lowercase f), la raccolta smart. "Apple Account" always capitalised.
- Apostrophes: guides and apple.com use the typographic ’ (U+2019: 1420 hits); older support articles (118428, 118223, 102420, 108906, 108350) use the straight ' (370 hits). Use ’ on the site, as the guides do.
- Inclusive wording in the iOS 27 guide: "la persona responsabile della famiglia", "amici e amiche", "tuo figlio o tua figlia", "un bambino o una bambina", "i familiari" and "membri della famiglia".

Punctuation and spacing (checked in raw bytes on the iPhone guide pages, Apple Watch guide pages, Mac guide pages, support articles 118428, 118223, 108906, 102420, 105055, 108350, 108971, apple.com/it/health, apple.com/it/privacy, apps.apple.com/it):
- UI quotes: “ ” (U+201C/U+201D), **no spaces inside, punctuation after the closing mark** ("Tocca “Tempo di utilizzo”,", "scegli “Richiedere un rimborso”."). Both guides and articles use them (see Key answer 3). « » is not Apple's mark here.
- Questions and exclamations: no space before "?" and "!" ("Vuoi scoprire di più?", "Utile?"). No space before ":" or ";".
- Apostrophes: typographic ’ in the guides (see above); never a straight ' on the site.
- Dashes: practically none in running text (see Key answer 7). A bare " – " or " — " is not Apple Italy's habit; use commas, colons, parentheses.
- Numbers: **decimal comma** (`11,3 MB`, `12,9`, `10,5 pollici`); **thousands separator is a period** (`100.000 volte al giorno`); value and unit separated by **U+00A0** in guides and articles (`5 GB`, `14 giorni`, `13 notti`, `24 ore`, `1 ora`, `15 minuti`), plain space in the App Store information row (`11,3 MB`); **percent has no space** (`30%`, `200%`; apple.com/it also writes "30 per cento" in words); `°C` with a plain space (`0 e 35 °C`).
- Currency: `2,99 €` = comma decimal, **U+00A0**, then € (checked raw: `<span>2,99&nbsp;€</span>` on the App Store page). Euro sign after the number.
- Dates: "1 ottobre 2026" (see Key answer 4). Footer: `Data di pubblicazione:&nbsp;1 ottobre 2026`.
- Product names: Apple's HTML puts **U+00A0 inside "Apple Watch", "App Store", "iCloud Drive", "Face ID", "Touch ID", "Apple Pay", "Apple Intelligence", "Apple Account", "Apple Games", "iPhone 15 Pro", "iOS 27", "Dynamic Island", "Liquid Glass", "Stage Manager", "Digital Crown", "Privacy e sicurezza"** (`Apple&nbsp;Watch`, `App&nbsp;Store`, `Privacy&nbsp;e sicurezza`) and in the App Store page title (`App&nbsp;Store` in `<title>`). Some plain spaces occur in older articles. Also NBSP after short words on apple.com marketing lines ("e&nbsp;il", "in&nbsp;cui"): typesetting, do not copy.
- Ordinals: "2ª generazione" (feminine ordinal sign, e.g. "iPhone SE (2ª generazione"), "terza generazione", "prima generazione".
- Time units: "da 24 a 48 ore", "ogni notte", "ultimi 14 giorni", "ultime 13 notti".
- Title/Description pattern of an app page: `<title>` = `‎App <name> - App Store` (LRM mark U+200E at the start, NBSP in "App Store"); description = "Scarica <name> di <developer> dall’App Store. Visualizza screenshot, valutazioni e recensioni, suggerimenti degli utenti e altre app…" (note "dall’App Store", with the article, unlike Spain's "en App Store").

Abbreviations: ig = iPhone user guide https://support.apple.com/it-it/guide/iphone/welcome/ios (table of contents), wg = Apple Watch user guide https://support.apple.com/it-it/guide/watch/welcome/watchos, mg = Mac user guide https://support.apple.com/it-it/guide/mac-help/welcome/mac, ah = https://www.apple.com/it/health/ (page title "Salute - Apple (IT)"), apv = https://www.apple.com/it/privacy/, ap = https://apps.apple.com/it/app/id6806255929 (Tare), ap2 = https://apps.apple.com/it/app/id6757438990 (Observa), sg = https://support.apple.com/it-it/guide/security/welcome/web. Article URLs are https://support.apple.com/it-it/NNNNNN. Guide pages: https://support.apple.com/it-it/guide/iphone/<id>/ios, https://support.apple.com/it-it/guide/watch/<id>/watchos, https://support.apple.com/it-it/guide/mac-help/<id>/mac.

## Health and fitness

| English | Italian (Italy) as Apple writes it | Source | Note |
|---|---|---|---|
| Health (app) | Salute; l’app Salute | https://support.apple.com/it-it/guide/iphone/iphcae7451f3/ios ; ah | Translated, never "Health". Tabs: Riepilogo, Condivisione, Sfoglia (older and most pages) / Esplora (some pages): the guide says "Sfoglia" 29 times and "Esplora" 6 times |
| Apple Health | Salute (page title "Salute - Apple (IT)"); "l’app Salute"; the page's hidden section heading reads "Apple app Salute" and its structured data name is "Apple Health" | ah | Apple Italy's visible copy says only "Salute" / "l’app Salute", never "Apple Salute". Developers' App Store text may still say "Apple Health" |
| Health data | dati sanitari; dati di Salute ("Eseguire il backup dei dati di Salute su iCloud"); "Visualizzare i dati sanitari"; “Dati in evidenza” | https://support.apple.com/it-it/guide/iphone/iphcae7451f3/ios ; https://support.apple.com/it-it/guide/iphone/iph11f1eb698/ios | "I tuoi dati sanitari in un unico posto" |
| Health profile | “Dettagli Salute” (Riepilogo > tua immagine o iniziali > “Dettagli Salute”); “Dettagli salute” (lowercase s) in the page title "Compilare la sezione “Dettagli salute”" | https://support.apple.com/it-it/guide/iphone/iphcae7451f3/ios ; https://support.apple.com/it-it/guide/iphone/iph08022b194/ios | Apple Italy is inconsistent on the capital |
| Health records | “Dati sanitari” (Riepilogo > tua immagine > “Dati sanitari”); guide section "Ottenere dati sanitari dalle strutture sanitarie"; page "Scaricare i dati sanitari su iPhone" | https://support.apple.com/it-it/guide/iphone/iphc30019594/ios | The feature is described as downloads from "strutture sanitarie"; "cartelle cliniche" is not on the page |
| Medical ID | **cartella clinica** ("Configurare e visualizzare la cartella clinica su Apple Watch"; "la tua cartella clinica nell’app Salute") | https://support.apple.com/it-it/guide/watch/apd58cd0b3f4/watchos | Apple Italy does not keep "Medical ID" |
| Health category (Summary pins) | Riepilogo (tab); “Dati in evidenza”; "elenco dei preferiti" ("Se hai aggiunto Sonno all'elenco dei preferiti, puoi accedervi dalla pagina Riepilogo"); “Elenco di controllo Salute”; Sfoglia | https://support.apple.com/it-it/108906 ; https://support.apple.com/it-it/guide/iphone/iphcae7451f3/ios ; https://support.apple.com/it-it/guide/watch/apd4e7713562/watchos | |
| Sleep (in Health) | Sonno (app Sonno on Apple Watch; Salute > Sfoglia > Sonno > "Sonno" again; “Configurare Sonno nell’app Salute”); guide section "Dare priorità al riposo" | https://support.apple.com/it-it/guide/iphone/iphaf56dceb4/ios ; https://support.apple.com/it-it/guide/iphone/iph72b370881/ios ; https://support.apple.com/it-it/108906 ; https://support.apple.com/it-it/guide/watch/crpxel1lvun9/watchos | Use "sonno" in prose |
| Sleep Focus | **full immersion Sonno** ("la full immersion Sonno ti aiuta a ridurre le distrazioni"; "Attivare o disattivare la full immersion Sonno"); Focus mode name: Sonno | https://support.apple.com/it-it/guide/iphone/iph7cdb86325/ios ; https://support.apple.com/it-it/guide/iphone/iph5c3f5b77b/ios ; ah ("abilitare automaticamente la full immersion Sonno") | Focus list: “Non disturbare”, “Nessun messaggio durante le chiamate”, Sonno, Personale, Lavoro (Guida also appears) |
| Sleep Score | **qualità del sonno** (“Qualità del sonno” feature; screen “Qualità sonno”); "un punteggio da 0 a 100"; scale: Molto scarsa 0-40, Scarsa 41-60, Accettabile 61-80, Buona 81-95, Molto buona 96+ | https://support.apple.com/it-it/guide/watch/apded441a669/watchos ; ah ("Dormito bene? Scoprilo con Qualità del sonno.") | Apple Italy says "qualità", not "punteggio del sonno" |
| Sleep apnea notifications | notifiche per le apnee notturne; “Notifiche sull’apnea notturna” (Elenco di controllo Salute); “Disturbi della respirazione” (Sfoglia > “Apparato respiratorio”) | https://support.apple.com/it-it/guide/watch/apd4e7713562/watchos | Page title: "Ricevere notifiche per le apnee notturne su Apple Watch" |
| Sleep stages Awake / REM / Core / Deep | **Veglia / REM / Principale / Profondo** (article 108906: "Veglia, REM, Principale o Profondo"); Watch guide: "fase del sonno (REM, Principale e Profondo)"; screen alt text: "svegli, e nelle fasi REM, Principale e “Sonno profondo”" | https://support.apple.com/it-it/108906 ; https://support.apple.com/it-it/guide/watch/crpxel1lvun9/watchos ; https://support.apple.com/it-it/guide/iphone/iph72b370881/ios | Word for stage: "fase". Core = "Principale". Awake is "Veglia" as a label and "risvegli" in prose |
| Heart Rate Variability (HRV) | **variabilità della frequenza cardiaca (HRV)**; "variabilità della frequenza cardiaca" (Parametri Vitali) | ah ("la variabilità della frequenza cardiaca (HRV)") ; https://support.apple.com/it-it/guide/watch/flx4gnzby346/watchos ; https://support.apple.com/it-it/guide/watch/apd15aa7ed96/watchos | Apple Italy keeps the English abbreviation HRV, not "VFC". Observa's own Italian store title uses "VFC" (developer text) |
| Resting heart rate | “Battito cardiaco a riposo” (Watch label; also “Media camminata”, Intervallo); "la frequenza a riposo" | https://support.apple.com/it-it/guide/watch/apda88aefe4c/watchos | In prose Apple writes "frequenza cardiaca" and "battito cardiaco" interchangeably |
| Heart rate | frequenza cardiaca; battito cardiaco; l’app **Battito** (Watch; "l’app Battito Cardiaco" in the Watch guide's intro); "pulsazioni" (marketing) | https://support.apple.com/it-it/guide/watch/apda88aefe4c/watchos ; ah | |
| Respiratory rate | frequenza respiratoria | https://support.apple.com/it-it/guide/watch/crpxel1lvun9/watchos ; https://support.apple.com/it-it/guide/watch/apd15aa7ed96/watchos | |
| Heart rate zones | zone di frequenza cardiaca (“Zona di frequenza cardiaca” during a workout) | https://support.apple.com/it-it/guide/watch/apd897dccddf/watchos ; ah | |
| ECG app | l’app ECG; elettrocardiogramma (ECG); “Elettrocardiogramma (ECG)” under Sfoglia > Cuore | https://support.apple.com/it-it/guide/watch/apdea4c50a57/watchos ; ah | |
| AFib History | “Cronologia fibrillazione atriale” (marketing: "la cronologia della fibrillazione atriale") | ah | |
| Irregular rhythm notifications | notifiche di ritmo cardiaco irregolare | ah | |
| Vitals app | l’app **Parametri Vitali** (title case); "metriche di salute notturne"; “Parametri notturni” | https://support.apple.com/it-it/guide/watch/apd15aa7ed96/watchos ; ah | "parametri vitali", not "segni vitali" |
| Readiness app (watchOS 27) | l’app **Preparazione**; "il punteggio di preparazione" (0 a 10); “Preparazione” ti dice quando riposare | https://support.apple.com/it-it/guide/watch/flx4gnzby346/watchos ; ah | Apple Watch Series 12 and Ultra 4 |
| Training Load | **“Carico allenamento”** (feature title) / "carico di allenamento" (prose); scale "da molto al di sotto a molto al di sopra" | https://support.apple.com/it-it/guide/watch/apde4c07a6cf/watchos ; ah | Page title: "Monitorare il carico di allenamento su Apple Watch" |
| Cardio Fitness | **tono cardiovascolare** ("livelli di tono cardiovascolare"; “Dati sul tono cardiovascolare aggiornati”) | https://support.apple.com/it-it/108790 ; ah | Not "fitness cardio" |
| VO2 max | **VO2 max** (marketing: `VO<sub>2</sub> max`); **VO2 massimo** (article 108790, `VO<sub>2</sub> massimo`; "intervallo di valori VO2 massimo compreso tra 14 e 65 mL/kg/min") | ah ; https://support.apple.com/it-it/108790 | |
| Cycle Tracking | **“Monitoraggio ciclo”** (guide, quoted) / **Monitoraggio Ciclo** (Apple Watch app, title case); "ciclo mestruale", "periodo fertile" | https://support.apple.com/it-it/guide/iphone/iph51a822b18/ios ; https://support.apple.com/it-it/guide/watch/apd26429adf0/watchos | |
| Mindfulness app | l’app **Mindfulness**; sessioni **Riflessione** e **Respirazione** | https://support.apple.com/it-it/guide/watch/apd371dfe3d7/watchos ; ah | |
| State of Mind | **“Stato d’animo”** (Sfoglia > “Benessere mentale” > “Stato d’animo”) | https://support.apple.com/it-it/guide/iphone/iph6a6decb13/ios ; ah | "Registrare il tuo stato d’animo" |
| Medications | **Farmaci** (Sfoglia > Farmaci; “Aggiungi un farmaco”); l’app Farmaci on Apple Watch | https://support.apple.com/it-it/guide/iphone/iph811670c81/ios ; https://support.apple.com/it-it/guide/watch/apd3dd24d78b/watchos | The thing = farmaci |
| Walking Steadiness | **stabilità della camminata** (“Notifiche sulla stabilità della camminata”) | https://support.apple.com/it-it/guide/iphone/iphff1bf03ed/ios | |
| Mobility | **Movimento** (Esplora > Movimento > “Notifiche sulla stabilità della camminata”). Note: the guide's "Mobilità" is the Accessibility section for motor needs | https://support.apple.com/it-it/guide/iphone/iphff1bf03ed/ios ; ig TOC | |
| Activity rings | anelli di Attività ("anelli Attività"); "chiudere gli anelli" | https://support.apple.com/it-it/guide/watch/apd3bf6d85a6/watchos ; https://support.apple.com/it-it/guide/iphone/ipha5dddb411/ios ; ah | Capital A when naming the app's rings |
| Move / Exercise / Stand rings | anello **Movimento** (rosso, calorie attive) / anello **Esercizio** (verde, minuti di esercizio) / anello **“In piedi”** (blu, quoted); wheelchair: “In piedi” becomes **“Pause attive”** | https://support.apple.com/it-it/guide/watch/apd3bf6d85a6/watchos ; ah ("Movimento, Esercizio e In piedi") | |
| Fitness app | l’app **Fitness** (iPhone and iPad; tabs Riepilogo, Condivisione and others) | https://support.apple.com/it-it/guide/iphone/ipha5dddb411/ios ; ah | English kept |
| Activity app (Apple Watch) | l’app **Attività** | https://support.apple.com/it-it/guide/watch/apd3bf6d85a6/watchos | |
| Workout app | l’app **Allenamento**; "un allenamento"; “Avviare un allenamento”; “Allenamenti” | https://support.apple.com/it-it/guide/watch/apdd16e8761a/watchos ; https://support.apple.com/it-it/guide/iphone/ipha5dddb411/ios | |
| Workouts (the plural) | allenamenti | same | |
| Stand hours | ore in piedi (and "minuti in piedi") | https://support.apple.com/it-it/guide/watch/apd3bf6d85a6/watchos | |
| Exercise minutes | minuti di esercizio | same | |
| Active energy / calories | calorie attive | same | |
| Flights climbed | piani di scale ("piani di scale" in the apple.com/it Fitness text) | ah | Not seen on a guide page |
| Steps | passi | https://support.apple.com/it-it/guide/iphone/ipha5dddb411/ios ; ah | |
| Headphone audio levels | livelli dell’audio delle cuffie; “Notifiche cuffie” (Salute > Sfoglia > Udito) | https://support.apple.com/it-it/guide/iphone/iph0596a9152/ios | |
| Noise / environmental sound | l’app **Rumore**; livelli di rumore | https://support.apple.com/it-it/guide/watch/apd00a43a9cb/watchos (title "Misurare i livelli di rumore con Apple Watch") ; ah | |
| Wrist temperature | temperatura del polso | https://support.apple.com/it-it/102674 ; https://support.apple.com/it-it/guide/watch/apd526d20feb/watchos | |
| Blood Oxygen | l’app **Livelli O₂** (with U+2082 subscript); "ossigeno nel sangue" in prose | https://support.apple.com/it-it/guide/watch/apdaf17aa5ef/watchos ; https://support.apple.com/it-it/guide/watch/apd15aa7ed96/watchos ; ah | |
| Apple Watch | l’Apple Watch (masculine: "il tuo Apple Watch", "l’Apple Watch"); mostly bare after "su" | https://support.apple.com/it-it/108906 ; ah ; wg | English kept |
| Apple Fitness+ | Apple Fitness+ | ah ("Meditazioni di Apple Fitness+") | English kept |
| Journal app | l’app **Diario** ("Scrivere sul diario"; "Creare un’annotazione di diario") | https://support.apple.com/it-it/guide/iphone/iph9824e83ce/ios ; ah | |

## System features

| English | Italian (Italy) as Apple writes it | Source | Note |
|---|---|---|---|
| Settings | l’app **Impostazioni**; **Impostazioni di Sistema** (Mac) | https://support.apple.com/it-it/guide/iphone/iphd6804774e/ios ; https://support.apple.com/it-it/guide/mac-help/mh15217/mac | "Vai nell’app Impostazioni su iPhone" |
| Screen Time | “**Tempo di utilizzo**” | https://support.apple.com/it-it/guide/iphone/iphbfa595995/ios | Quoted in the iOS 27 guide. Not "Tempo di utilizzo dello schermo" |
| Screen Time Schedules (iOS 27) | “Orari di ‘Tempo di utilizzo’”; "gli orari di “Tempo di utilizzo”" | same | Nested single quotes |
| Screen Time Limits | “Limiti di tempo” | same | Also “Gestisci il tempo di utilizzo”, “Condividi sui dispositivi”, “Attività app e siti web”, “Gestisci categorie” |
| Downtime / App Limits (iOS 26 and earlier) | not verified | iOS 27 guide replaced them; older versions not opened | |
| Screen Time weekly report | resoconto settimanale di “Tempo di utilizzo”; “Media giornaliera”; "attivazioni schermo e notifiche" | https://support.apple.com/it-it/guide/iphone/iphbfa595995/ios | |
| Screen Distance | “Distanza dallo schermo” | ah | Marketing page only |
| Focus | **full immersion** (lowercase; plural "le full immersion"); settings label “Full immersion” (Impostazioni > “Full immersion”); Control Center tile: “Full immersion” | https://support.apple.com/it-it/guide/iphone/iphd6288a67f/ios ; https://support.apple.com/it-it/guide/iphone/iph5c3f5b77b/ios | Apple Italy's term is not "Concentrazione" or "modalità di concentrazione". Modes: Guida, Personale, Sonno, Lavoro, “Non disturbare” |
| Do Not Disturb | “Non disturbare” | same | |
| Reduce Interruptions (Focus) | “Meno interruzioni” (uses Apple Intelligence; "full immersion “Meno interruzioni”") | https://support.apple.com/it-it/guide/iphone/iphd6288a67f/ios | |
| Focus Filter / link Focus to Lock Screen | "Collegare una full immersion alla schermata di blocco"; “Aggiungi filtro” | same | |
| Family Sharing | **“In famiglia”**; "un gruppo “In famiglia”"; "un gruppo di “In famiglia”"; "Configurare “In famiglia”"; "Condividere gli abbonamenti" | https://support.apple.com/it-it/guide/iphone/iph223f61318/ios ; https://support.apple.com/it-it/guide/iphone/iph6e7917d3f/ios ; https://support.apple.com/it-it/guide/iphone/iph4cd8953e2/ios ; ap | Never "Family Sharing" and never "Condivisione in famiglia" as the name |
| Family sharing label on the product page | Supporta > **In famiglia**: "Quando “In famiglia” è abilitato, potresti avere la possibilità di condividere alcuni acquisti in‑app e abbonamenti con il tuo gruppo familiare." | https://apps.apple.com/it/app/id6806255929 | Exact store text; the row heading is "Supporta" |
| Ask to Buy | **Chiedi di acquistare**; “Chiedi di acquistare” (quoted in the article) | https://support.apple.com/it-it/105055 | Article title: "Approvare gli acquisti e i download di tuo figlio o tua figlia con Chiedi di acquistare" |
| Parental controls | controllo parentale ("funzionalità di controllo parentale") | https://support.apple.com/it-it/guide/iphone/iphbfa595995/ios ; https://support.apple.com/it-it/guide/iphone/iph223f61318/ios | |
| Family Controls (framework) | not verified | developer pages are English; the user-facing feature is “Tempo di utilizzo” and controllo parentale | |
| In-App Purchases | **Acquisti in-app** (store label "Acquisti in-app"; price line "Acquisti in‑app" with U+2011); "acquisti in-app" in guides | https://apps.apple.com/it/app/id6806255929 ; https://support.apple.com/it-it/guide/iphone/iph4e3e7324f/ios | Not "acquisti integrati" |
| Subscriptions (manage) | "In Impostazioni, tocca il tuo nome. Tocca Abbonamenti. Tocca l'abbonamento. Tocca Annulla abbonamento." (Mac: "Nell’App Store, fai clic su [il tuo nome]... Fai clic su Abbonamenti... Fai clic su Annulla abbonamento.") | https://support.apple.com/it-it/118428 | Article title: "Annullare un abbonamento Apple". iPhone guide: "Tocca il tuo nome, quindi tocca Abbonamenti ... tocca un abbonamento, quindi tocca “Annulla abbonamento”" |
| Cancel subscription (button) | **Annulla abbonamento** (article, bare, sentence case); “Annulla abbonamento” (iPhone guide, quoted); “Annulla tutti i …” (older) ; "se compare un messaggio di scadenza con testo in rosso" | https://support.apple.com/it-it/118428 ; https://support.apple.com/it-it/guide/iphone/iph4e3e7324f/ios | Free trial tip in the article: "annulla l'abbonamento almeno 24 ore prima del termine del periodo di prova" |
| Apple Account (ex Apple ID) | **Apple Account** (kept English, capital A; NBSP inside); “Apple Account” as the settings row | https://support.apple.com/it-it/guide/iphone/iph76e54c61e/ios ; https://support.apple.com/it-it/118223 | Apple Italy does not write "ID Apple" or "account Apple" in the iOS 27 guide |
| iCloud | iCloud | https://support.apple.com/it-it/guide/iphone/iphde0f868fd/ios | English kept, no article |
| iCloud+ | iCloud+ ("Abbonarsi ad iCloud+") | https://support.apple.com/it-it/guide/iphone/iphde0f868fd/ios | |
| iCloud Drive | iCloud Drive | https://support.apple.com/it-it/guide/iphone/iphbbcf8827d/ios | |
| iCloud Photos | **Foto di iCloud** (guide: "conservare foto e video in Foto di iCloud"; "Eliminare le foto da Foto di iCloud") | https://support.apple.com/it-it/guide/iphone/iphde0f868fd/ios ; https://support.apple.com/it-it/108922 | |
| Sync this iPhone (iCloud Drive toggle) | “Sincronizza questo iPhone” (Impostazioni > [Il tuo nome] > iCloud > Drive) | https://support.apple.com/it-it/guide/iphone/iphbbcf8827d/ios | |
| iCloud sync | "tiene automaticamente aggiornati"; "sincronizzare con iCloud" | https://support.apple.com/it-it/guide/iphone/iphde0f868fd/ios | No fixed noun phrase |
| iCloud backup | **Backup iCloud** (switch label “Backup iCloud”); "backup su iCloud" (prose) | https://support.apple.com/it-it/guide/iphone/iphde0f868fd/ios ; https://support.apple.com/it-it/108922 | "backup" is the Italian word |
| Advanced Data Protection | **protezione avanzata dei dati** (lowercase; "La protezione avanzata dei dati per iCloud"); also "Protezione avanzata dati" as the setting label | https://support.apple.com/it-it/108756 ; https://support.apple.com/it-it/102651 | Article title: "Come attivare la protezione avanzata dei dati per iCloud" |
| Standard data protection | "protezione standard" / "protezione dei dati standard" | https://support.apple.com/it-it/102651 ; https://support.apple.com/it-it/108756 | |
| Data Protection (iOS file encryption) | **protezione dati** ("Panoramica della protezione dati"; "i dati relativi allo stato di salute utilizzano la protezione dei dati di default") | https://support.apple.com/it-it/guide/security/secf6276da8a/web | The Italian security guide is translated |
| Apple Push Notification service (APNs) | Servizio di notifiche push di Apple (APN) | https://support.apple.com/it-it/guide/security/aside/sec19eabb530/web | Apple Italy abbreviates "APN". For users: "notifiche" |
| Home Screen | **schermata Home** (capital H) | https://support.apple.com/it-it/guide/iphone/iphb8f1bf206/ios ; https://support.apple.com/it-it/guide/iphone/iphd2fc8ce30/ios | "Personalizzare la schermata Home" |
| Lock Screen | **schermata di blocco** | https://support.apple.com/it-it/guide/iphone/iph4d0e6c351/ios ; https://support.apple.com/it-it/102638 | Article 102638 also says "blocco schermo" once |
| Widgets | widget (invariable: "i widget", "un widget"); "galleria di widget"; “Aggiungi widget” | https://support.apple.com/it-it/guide/iphone/iphb8f1bf206/ios ; https://support.apple.com/it-it/guide/mac-help/mchl52be5da5/mac | English kept |
| Smart Stack | **raccolta smart** (“Raccolta smart”: "un insieme di widget ... riconoscibile dai puntini"); Watch: "Visualizzare i widget al momento giusto nella raccolta smart" | https://support.apple.com/it-it/guide/iphone/iphb8f1bf206/ios ; https://support.apple.com/it-it/guide/watch/apdecf142fb9/watchos | Not "Smart Stack" |
| Live Activities | **attività in tempo reale**; Settings: “Attività in tempo reale” | https://support.apple.com/it-it/guide/iphone/iph28f50d10d/ios ; https://support.apple.com/it-it/guide/watch/bz1vx4mwqbw9/watchos | Not "Live Activities" |
| Dynamic Island | Dynamic Island (feminine: "nella Dynamic Island") | https://support.apple.com/it-it/guide/iphone/iph28f50d10d/ios | English kept |
| StandBy | **StandBy** ("Utilizzare StandBy"; "modalità StandBy"; Impostazioni > StandBy) | https://support.apple.com/it-it/guide/iphone/iph878d77632/ios | Kept in English. Not translated |
| Control Center | **Centro di Controllo** (iPhone and Watch guides, capital C); "Centro di controllo" (Mac guide heading, lowercase c) | https://support.apple.com/it-it/guide/iphone/iph59095ec58/ios ; https://support.apple.com/it-it/guide/mac-help/mchlc9d0e1f2/mac ; https://support.apple.com/it-it/108350 | "Apri Centro di Controllo" with no article |
| Notification Center | **Centro Notifiche** | https://support.apple.com/it-it/guide/iphone/iph6534c01bc/ios ; https://support.apple.com/it-it/guide/mac-help/mchl52be5da5/mac | |
| Notifications | notifiche (“Notifiche tempestive” = Time Sensitive; “Riepilogo programmato”; “Recapito notifiche”; “Recapito immediato”) | https://support.apple.com/it-it/guide/iphone/iph7c3d96bab/ios | |
| Share Sheet / Share button | pulsante **Condividi**; "menu di condivisione" | https://support.apple.com/it-it/guide/iphone/iphc572ca489/ios | |
| AirDrop | AirDrop | https://support.apple.com/it-it/guide/iphone/iphcd8b9f0af/ios | English kept |
| Spotlight | Spotlight | https://support.apple.com/it-it/guide/iphone/iph3c511548/ios | English kept ("Eseguire le ricerche con Spotlight") |
| Siri | Siri; "di’ “Siri” o “Ehi Siri”"; Impostazioni > Siri | https://support.apple.com/it-it/guide/iphone/iph83aad8922/ios ; https://support.apple.com/it-it/105020 | |
| Apple Intelligence | Apple Intelligence | https://support.apple.com/it-it/guide/iphone/iphc28624b81/ios ; apv | English kept |
| Shortcuts (app) | l’app **Comandi Rapidi** (title case); "comandi rapidi" (user shortcuts); "Usare Comandi Rapidi per automatizzare le attività" | https://support.apple.com/it-it/guide/iphone/iph47e1c9d7d/ios ; https://support.apple.com/it-it/guide/watch/apd99050d435/watchos | Not "Scorciatoie" for the app; "scorciatoia da tastiera" is used for keyboard shortcuts |
| Universal Clipboard | **“Appunti condivisi”** ("gli appunti condivisi" in prose) | https://support.apple.com/it-it/guide/iphone/iph220ea8dca/ios | |
| Handoff | Handoff (Impostazioni > Generali > AirPlay e Continuità) | https://support.apple.com/it-it/guide/iphone/iphcec5d0a9d/ios | English kept |
| Picture in Picture | **Picture in Picture** ("la modalità PiP (Picture in Picture)") | https://support.apple.com/it-it/guide/iphone/iphcc3587b5d/ios | Kept in English |
| Airplane Mode | **modalità Aereo** (capital A) | https://support.apple.com/it-it/guide/iphone/iph59095ec58/ios ; https://support.apple.com/it-it/guide/watch/apdc22c9d320/watchos ("Usare la modalità Aereo") | |
| Low Power Mode | **“Risparmio energetico”** ("modalità di alimentazione"); iOS 27: “Consumo adattivo” | https://support.apple.com/it-it/guide/iphone/iphcab9aecd1/ios | Page title: "Prolunga la durata della batteria con le modalità di alimentazione su iPhone" |
| Dark Mode | **modalità scura** (lowercase; "Modalità scura" as the control); setting Impostazioni > Schermo e luminosità > Scuro | https://support.apple.com/it-it/108350 | "Interfaccia scura" is the App Store accessibility label |
| Appearance (iOS 27) | “Aspetto” (Impostazioni > Aspetto > “Dimensioni testo”, “Testo in grassetto”, Liquid Glass, “Zoom schermo”) | https://support.apple.com/it-it/guide/iphone/iphd6804774e/ios | |
| Accessibility | Accessibilità | https://support.apple.com/it-it/guide/iphone/iph3e2e4367/ios | |
| VoiceOver | VoiceOver | wg ; ig TOC | English kept |
| Larger Text (Dynamic Type setting) | “**Dimensioni testo**” (iOS 27, Impostazioni > Aspetto); “Testo più grande” (under “Zoom schermo”); “Schermo e dimensioni testo” (Accessibilità); App Store label: "Testo più grande" | https://support.apple.com/it-it/guide/iphone/iphd6804774e/ios ; ap | |
| Reduce Motion | **Riduci movimento** (Impostazioni > Accessibilità > Movimento > Riduci movimento); App Store label: "Movimento ridotto" | https://support.apple.com/it-it/111781 ; ap | |
| Offline | offline ("Scaricare le mappe offline") | ig TOC | Kept in English |
| Privacy & Security | **Privacy e sicurezza** (bare in paths: "Impostazioni > Privacy e sicurezza") | https://support.apple.com/it-it/guide/iphone/iph4f4cbd242/ios ; https://support.apple.com/it-it/guide/iphone/iph251e92810/ios | |
| App Tracking | **Tracciamento** (Impostazioni > Privacy e sicurezza > Tracciamento); toggle “Richiesta tracciamento attività” | https://support.apple.com/it-it/guide/iphone/iph4f4cbd242/ios ; https://support.apple.com/it-it/102420 | Apple Italy also writes "tracking" in marketing ("Ostacola il tracking") |
| Analytics share with developers | Impostazioni > Privacy e sicurezza > **Analisi e miglioramenti** > "Condividi dati iPhone e Watch"; “Condividi con gli sviluppatori di app” (older) | https://support.apple.com/it-it/108971 | Newer label not verified beyond the article |
| Background App Refresh | not verified | no it-it page found with the label (Apple writes "attività in background" only inside battery text) | |
| Restore purchases | Apple's phrases: "Ripristinare gli acquisti e gli elementi che hai eliminato"; "scaricare nuovamente gli elementi acquistati"; button “Scarica di nuovo” (iPhone guide) | https://support.apple.com/it-it/guide/iphone/iphfe205f2e5/ios ; https://support.apple.com/it-it/guide/iphone/iph4e3e7324f/ios | In-app StoreKit button label not documented on an Italy page |

## Built-in apps

| English | Italian (Italy) as Apple writes it | Source | Note |
|---|---|---|---|
| Reminders | **Promemoria** (l’app Promemoria) | https://support.apple.com/it-it/guide/iphone/iphc7880ecd6/ios ; ig TOC | |
| Calendar | **Calendario** (l’app Calendario) | https://support.apple.com/it-it/guide/iphone/iph3d110f84/ios | Event = "evento" |
| Files | **File** (l’app File) | https://support.apple.com/it-it/guide/iphone/iphbbcf8827d/ios | |
| Photos | **Foto** (l’app Foto) | ig TOC | |
| Camera | **Fotocamera** (l’app Fotocamera; “Controllo fotocamera”) | ig TOC (section "Fotocamera") | |
| Notes | Note | ig TOC | |
| Clock / Alarm | **Orologio** ("Impostare una sveglia in Orologio"); sveglia | https://support.apple.com/it-it/guide/iphone/iph2909d3a74/ios | |
| Games app | l’app **Apple Games**; Game Center | https://support.apple.com/it-it/guide/iphone/iph3aed54d2e/ios | English kept; TOC section "Games" |
| Wallet | **Wallet** (l’app Wallet; "Wallet di Apple") | https://support.apple.com/it-it/guide/iphone/iph9b7f53382/ios ; https://support.apple.com/it-it/guide/watch/apd16914b6d1/watchos ; apv ("Wallet e Apple Pay") | Not translated |
| Apple Pay | Apple Pay | https://support.apple.com/it-it/guide/iphone/iph9b7f53382/ios | English kept |
| Sign in with Apple | **“Accedi con Apple”** | https://support.apple.com/it-it/guide/iphone/iph238921d37/ios | |
| Passwords | Password (TOC section) | ig TOC | Not translated |
| Maps | Mappe | ig TOC | |
| Weather | **Meteo** (l’app Meteo) | https://support.apple.com/it-it/guide/iphone/iph1ac0b35f/ios | |
| Stocks | Borsa | ig TOC | |
| Messages / Mail | Messaggi / Mail | ig TOC | |
| Voice Memos | Memo Vocali (title case) | ig TOC ; wg TOC | |

## Devices and platforms

| English | Italian (Italy) as Apple writes it | Source | Note |
|---|---|---|---|
| iPhone, iPad, Mac | iPhone, iPad, Mac (l’iPhone, l’iPad, il Mac) | ap ; ig | |
| Apple Watch | l’Apple Watch | ap ; ah ; wg | |
| Apple Vision Pro | Apple Vision Pro (article 118428: "Annullare un abbonamento su Apple Vision Pro") | https://support.apple.com/it-it/118428 ; ap2 (compat label "Apple Vision") | App Store compatibility label says "Apple Vision" |
| iOS, iPadOS, macOS, watchOS, visionOS | unchanged ("Richiede iOS 18.0 o versioni successive.") | ap | |
| Designed for iPad / iPhone (on Mac) | "Progettata per iPad. Non verificata per macOS." (Observa) | https://apps.apple.com/it/app/id6757438990 | Apple writes the participle in the gender of "app" (feminine): "Progettata", "verificata". Copy exactly per page |
| Mac chip wording | "Richiede macOS 14.6 o versioni successive e un Mac con chip Apple M1 o versioni successive." | https://apps.apple.com/it/app/id6757438990 | |

## App Store and developer

| English | Italian (Italy) as Apple writes it | Source | Note |
|---|---|---|---|
| App Store | App Store (l’App Store / "nell’App Store" in articles; "su App Store", "da App Store" in guides; l’app App Store) | https://support.apple.com/it-it/guide/iphone/iphc90580097/ios ; https://support.apple.com/it-it/118428 | NBSP inside "App Store" |
| "Download on the App Store" badge | **Line 1: Scarica su / Line 2: App Store** | https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/it-it (SVG title "Download_on_the_App_Store_Badge_IT_RGB_blk_100317"; rendered with rsvg-convert and read 2026-11-19) | Copied from the artwork, not translated. The artwork is outlined paths, so there is no text node |
| "Download on the Mac App Store" badge | **Line 1: Scarica su / Line 2: Mac App Store** | https://tools.applemediaservices.com/api/badges/download-on-the-mac-app-store/black/it-it (rendered and read) | |
| App Privacy (section) | **Privacy dell’app** (section heading) | https://apps.apple.com/it/app/id6806255929 | "procedure per la tutela della privacy dell’app" in the text |
| Data Not Collected | **Dati non raccolti**; sub-line: "Lo sviluppatore non raccoglie alcun dato da quest’app." | https://apps.apple.com/it/app/id6806255929 | |
| Data Used to Track You | not verified (no sampled page with this label) | not fetched | |
| Data Linked to You | not verified | not fetched | |
| Data Not Linked to You | not verified | not fetched | |
| Purposes in the privacy label | not verified | not fetched | |
| Privacy nutrition label | not verified as a noun phrase; the store section is "Privacy dell’app" and the disclaimer is "Tali informazioni non sono state verificate da Apple." (help link: “Definizioni ed esempi sulla privacy”) | https://apps.apple.com/it/app/id6806255929 | "etichetta" is NOT on any Italy page fetched |
| Privacy Manifest | not verified | no it-it page | |
| App Store Connect | App Store Connect (English kept) | https://support.apple.com/it-it/guide/app-store-connect/welcome/web → 404 on it-it | not verified |
| TestFlight | TestFlight (English kept) | https://support.apple.com/it-it/guide/testflight/welcome/ios → 404 | not verified |
| Xcode, CloudKit, Feedback Assistant | English kept | no it-it developer pages | not verified |
| Universal Purchase | not verified | no it-it page | Do not invent a translation |
| App Tracking Transparency | Apple Italy article title: "Se un'app chiede di tracciare le tue attività"; buttons **Consenti** and **Chiedi all'app di non eseguire il tracciamento**; toggle “Richiesta tracciamento attività”; the feature itself: "La trasparenza sul tracciamento delle app" | https://support.apple.com/it-it/102420 ; https://support.apple.com/it-it/guide/iphone/iph4f4cbd242/ios | The ATT system prompt title is not on any Italy page fetched (not verified). Article defines "identificativo per gli inserzionisti (IDFA)" |
| Report a Problem (reportaproblem.apple.com) | Apple's article names the site: "Esegui l'accesso a reportaproblem.apple.com." The menu entry is “Vorrei” > “Richiedere un rimborso” (quoted in the article) | https://support.apple.com/it-it/118223 | |
| Refund request | **Richiedere un rimborso**; article "Richiedere un rimborso per app o contenuti acquistati da Apple"; steps: Esegui l'accesso a reportaproblem.apple.com > tocca o fai clic su “Vorrei” > “Richiedere un rimborso” > scegli il motivo > Avanti > scegli l'app > Invia; "Attendere da 24 a 48 ore" | https://support.apple.com/it-it/118223 | No refund promise |
| Purchase history | **Cronologia di acquisto** (App Store > tua immagine > “App e cronologia di acquisto” > “Cronologia di acquisto”) | https://support.apple.com/it-it/guide/iphone/iph4e3e7324f/ios | Singular "acquisto" |
| Re-download apps | “Le tue app”; “Scarica di nuovo” ("Visualizzare e scaricare di nuovo le app") | same | |
| Manage / cancel subscriptions (path) | Impostazioni > tuo nome > Abbonamenti > l'abbonamento > Annulla abbonamento | https://support.apple.com/it-it/118428 | |
| Price label | **Gratis** (price line "Gratis · Acquisti in‑app") | https://apps.apple.com/it/app/id6806255929 | |
| Get button | **Ottieni** (raw `"title":"Ottieni"`) | same | |

## Italian App Store product page labels

Copied from https://apps.apple.com/it/app/id6806255929 (Tare) and https://apps.apple.com/it/app/id6757438990 (Observa). Seller details on those pages are not reproduced.

| Label | Exact Italian text |
|---|---|
| Price line (free app with IAP) | `Gratis · Acquisti in‑app` (Observa adds `· Progettata per iPad. Non verificata per macOS.`). Separators are plain space, U+00B7 MIDDLE DOT, plain space; "in‑app" uses U+2011 NON-BREAKING HYPHEN in this line |
| Free | Gratis |
| Get button | Ottieni |
| Ratings section | Valutazioni e recensioni. Empty state: "L’app non ha ricevuto un numero sufficiente di valutazioni o recensioni per poter mostrare una panoramica." |
| Age rating | header chip: Classificazione per età, value "4+" with caption "Anni" (Observa "9+" "Anni"); Information row: Età "4+"; Observa adds Contiene: "Argomenti di salute o benessere" |
| Category | header chip and row: Categoria (Tare: Rompicapo; Observa: Salute e benessere) |
| Developer | header chip: **Sviluppatore**; Information row: **Fornitore** |
| Language | header chip: Lingua ("IT + 43"); Information row: Lingue ("Italiano e altre 43 lingue", then the full list; language names capitalised: Italiano, Arabo, Francese, Inglese) |
| Size | Dimensioni: `11,3 MB`, `92,7 MB` (plain space before MB in the Information row; the header chip shows "11,3" over "MB") |
| Compatibility | Compatibilità: "Richiede iOS 18.0 o versioni successive." / "Richiede iPadOS 18.0 o versioni successive." / Mac: "Richiede macOS 14.6 o versioni successive e un Mac con chip Apple M1 o versioni successive." / Apple Vision: "Richiede visionOS 1.3 o versioni successive." / Apple Watch: "Richiede watchOS 10.0 o versioni successive." (NBSP inside "macOS 14.6") |
| Info section heading | Informazioni |
| In-App Purchases | Acquisti in-app: "Sì", then one row per item (`Capitoli II–X 2,99 €`) |
| Accessibility | Accessibilità; "Funzioni supportate"; labels VoiceOver, Testo più grande, Interfaccia scura, "Differenzia non solo con il colore", "Contrasto sufficiente", "Movimento ridotto" |
| Family Sharing | Supporta > In famiglia |
| Privacy section | Privacy dell’app; "Dati non raccolti"; link “Definizioni ed esempi sulla privacy”; disclaimer "Tali informazioni non sono state verificate da Apple." |
| Privacy policy link | Informativa sulla privacy |
| Developer website | Sito web sviluppatore |
| Other sections | Novità (version "Versione 1.2 6 gg fa", "Cronologia versioni", version dates "27 ott", "9 ott"); Altro da <developer>; Potrebbero piacerti anche; Anteprime app e screenshot; Condividi; Supporto (footer); "Condizioni dei servizi internet"; "App Store e privacy"; "Avviso sui cookie"; "Mostra elenco" (country list) |
| Platform names in nav | iPhone, iPad, Mac, Watch, TV (nav tabs: Oggi, Giochi, App, Arcade, Cerca; "Piattaforma" menu) |
| Meta title / description | `‎App <name> - App Store` (U+00A0 inside "App Store"); "Scarica <name> di <developer> dall’App Store. Visualizza screenshot, valutazioni e recensioni, suggerimenti degli utenti e altre app…" |

In-app purchase price format: `2,99 €`. Comma decimal, then a **NO-BREAK SPACE (U+00A0)**, then €. Checked in the raw HTML (Tare "Capitoli II–X 2,99 €").

## Italian App Store category names

Read from the "Categoria" field of live apps.apple.com/it/app/id... pages on 2026-11-19 (sample app and ID in the last column). The `apps.apple.com/it/genre/...` pages were not tried.

| English category | Italian App Store category | Genre id |
|---|---|---|
| Business | Economia | 6000 |
| Utilities | Utility | 6002 |
| Productivity | Produttività | 6007 |
| Lifestyle | Stili e tendenze | 6012 |
| Health & Fitness | Salute e benessere | 6013 |
| Games | Giochi | 6014 |
| Finance | Finanza | 6015 |
| Education | Istruzione | 6017 |
| Books | Libri | 6018 |
| Developer Tools | Sviluppatori | 6026 |
| Graphics & Design | Grafica e design | 6027 |

Source: Apple's genres service `itunes.apple.com/WebObjects/MZStoreServices.woa/ws/genres?id=36&cc=it&l=it`, checked 2026-11-19 by the it.yml reviewer; matches the category lines on the Italian store pages in it-glossary.md. Apple has no separate Fitness category in Italy; the site keeps «Fitness» as its own label for the health/fitness split.

## Unverified (best guesses, not confirmed on an Apple Italy page)

| English | Best guess | Why unverified |
|---|---|---|
| Downtime / App Limits (iOS 26 and earlier) | none | Older iOS guide versions not opened; iOS 27 uses “Orari di ‘Tempo di utilizzo’” and “Limiti di tempo” |
| Privacy nutrition label (noun) | none | Not on any Apple Italy page fetched; the store uses "Privacy dell’app" |
| Data Used to Track You, Data Linked to You, Data Not Linked to You, the privacy purposes (third-party advertising, analytics, product personalization, app functionality) | none | No sampled Italian page carried these sections; only "Dati non raccolti" was seen |
| Privacy manifest, Universal Purchase, App Store Connect, TestFlight, Xcode, CloudKit, Feedback Assistant, Family Controls, Dynamic Type (developer term), StoreKit "Restore Purchases" button | English kept | developer.apple.com has no Italy pages; support.apple.com/it-it guides for App Store Connect and TestFlight return 404 |
| Background App Refresh | none | No Italy page with the label found |
| ATT system prompt title | none | Only the buttons and settings are documented |
| Analytics label (newest iOS) | "Analisi e miglioramenti" | Article 108971 names it in the iOS 10 steps; newest label not re-read |
| Sleep tab name on iPhone | "Sonno" (Sfoglia/Esplora > Sonno) | Apple's pages name the tab both "Sfoglia" and "Esplora" |
| Health "Explore" tab name | "Sfoglia" (29 hits) or "Esplora" (6 hits, guide pages on sleep and walking steadiness) | Apple's pages disagree; use "Sfoglia" |
| "HH:MM" time format | none | Only "alle 7 del mattino", "dalle 11 alle 13" and "alle 9" were seen; no colon time on the pages fetched |
| Health "Hearing" and "Heart" category names beyond the examples | "Udito" (Sfoglia > Udito), "Cuore" (Sfoglia > Cuore), "Apparato respiratorio" | Seen in steps only, not as a full category list |

## Added rows (same extra rows as the French, German and Spanish files)

| English | Italian as Apple writes it | Source | Note |
|---|---|---|---|
| Medications (inconsistency) | iPhone guide: "Tocca Sfoglia, quindi tocca Farmaci"; "Aggiungi farmaco" (first) vs "Aggiungi un farmaco" (later) on the same page | https://support.apple.com/it-it/guide/iphone/iph811670c81/ios ; https://support.apple.com/it-it/guide/iphone/iphcae7451f3/ios | Use "Farmaci" for the feature |
| Share With App Developers (Analytics) | Impostazioni > Privacy e sicurezza > Analisi e miglioramenti > Condividi dati iPhone e Watch | https://support.apple.com/it-it/108971 | |
| Delete data from iCloud (storage path) | Impostazioni > [tuo nome] > iCloud > … ("Gestire lo spazio di archiviazione su iCloud sul tuo dispositivo Apple"; "Eliminare le foto da Foto di iCloud"; "Ridurre le dimensioni del backup su iCloud") | https://support.apple.com/it-it/108922 | Exact tap-target not re-read |
| Cancel a subscription | iPhone: "Tocca Annulla abbonamento"; Mac and Windows: "Fai clic su Annulla abbonamento" | https://support.apple.com/it-it/118428 | Expired: "compare un messaggio di scadenza con testo in rosso" |
| Request a refund | reportaproblem.apple.com > “Vorrei” > “Richiedere un rimborso” | https://support.apple.com/it-it/118223 | |
| Camera app | **Fotocamera** (iOS 27 guide) | ig TOC | |
| Control Center on Mac | Centro di controllo (Mac: "fai clic sulla sua icona nella barra dei menu") | https://support.apple.com/it-it/guide/mac-help/mchlc9d0e1f2/mac | |
| Stage Manager | **Stage Manager** (kept in English; "scrivania" = desktop) | https://support.apple.com/it-it/guide/mac-help/mchl534ba392/mac | Not translated |
| Desktop widgets (Mac) | widget sulla scrivania; "Centro Notifiche" | https://support.apple.com/it-it/guide/mac-help/mchl52be5da5/mac | |
| System Settings | Impostazioni di Sistema (capital S on "Sistema") | https://support.apple.com/it-it/guide/mac-help/mh15217/mac ; mg TOC | |
| Calendar event / Reminders list | evento; promemoria; "elenchi" of reminders ("organizzare le attività in elenchi di cose da fare") | https://support.apple.com/it-it/guide/iphone/iphc7880ecd6/ios | |
| Smart folders | not verified | not fetched (the Italian "liste intelligenti" / "cartelle smart" strings were not found on the pages read) | |

## App Store privacy labels (verified 2026-11-19, Tier 1 review)

Source: https://apps.apple.com/it/app/id426826309 (Strava), checked against https://apps.apple.com/it/app/id570060128
(Duolingo) and https://apps.apple.com/it/app/id1489118195 (Good Sudoku); Safari UA, `Accept-Language: it-IT`. These
replace the "not verified" privacy-label rows above.

| English | Apple Italy |
|---|---|
| App Privacy (section) | Privacy dell’app |
| Data Used to Track You | Dati utilizzati per monitorarti (Apple's verb here is «monitorare», not «tracciare») |
| Data Linked to You | Dati collegati a te |
| Data Not Linked to You | Dati non collegati a te |
| Data Not Collected | Dati non raccolti |
| Purposes | Pubblicità di terze parti; Pubblicità o marketing dello sviluppatore; Analisi; Personalizzazione del prodotto; Funzionalità delle app; Altri scopi |
| Categories (types) | Salute e fitness (Salute, Fitness); Acquisti (Cronologia degli acquisti); Informazioni finanziarie (Informazioni di pagamento); Posizione (Posizione precisa, Posizione approssimativa); Informazioni di contatto (Indirizzo email, Nome, Numero di telefono); Contatti; Contenuti dell’utente (Foto o video, Assistenza clienti, Altri contenuti dell’utente); Cronologia delle ricerche; Identificativi (ID utente, ID dispositivo); Dati sull’utilizzo (Interazione con il prodotto, Dati sulla pubblicità, Altri dati sull’utilizzo); Diagnosi (Dati sui crash, Dati sulle prestazioni, Altri dati di diagnosi); Altri dati (Altri tipi di dati) |
| Keychain (Mac) | Portachiavi; app «Accesso Portachiavi»; portachiavi iCloud (support.apple.com/it-it/guide/keychain-access/kyca1083/mac) |
| Universal Clipboard | appunti condivisi |
| Share sheet | menu di condivisione |
| Apple's standard EULA | Contratto di Licenza per utenti finali per le Applicazioni concesse in licenza (“Contratto EULA Standard”) (apple.com/legal/internet-services/itunes/it/terms.html) |
| App Store "What's New" | Novità |
