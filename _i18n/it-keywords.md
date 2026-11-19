# Keyword research, Italian (Italy)

Part of the language sheet `_i18n/it.md`. Two research passes on 2026-11-19 (part 1: studio pages and ten apps; part 2: the other eleven apps). Sources: **G** = Google suggest (hl=it, gl=it), **B** = Bing autosuggest (qsonhs, mkt=it-IT), **A** = App Store search hints (storefront 143450-7,29), **S** = iTunes Search API (country=it). Every query was returned by one of them. People also ask was not collected. Search Console: no Italy query data (only a July 2026 export with country totals: Italy 9 clicks, 1432 impressions over three months).

# Keyword research, Italian (Italy), part 1

Part of the Italian setup (TRANSLATION.md 5.3). Collected 2026-11-19. Pages: Home, Apps hub, About, Support hub, Transparency, and the app pages aftershift, allpaid, appmeta, appmeta-pulse, chessful, earnlock, gymlogger-x, liftlog, mediakit, millrace. Model: `_i18n/es-keywords.md` Part 1. Part 2 (the other eleven apps) is a separate file.

Sources: **G** = Google suggest (hl=it, gl=it), **B** = Bing autosuggest (qsonhs, mkt=it-IT), **A** = App Store search hints (Italian storefront), **S** = iTunes Search API (country=it, lang=it_it), used only for competitor names and the vocabulary of Italian app titles. Every query below was returned by one of them; nothing was invented. People also ask was not collected (it needs a live results page; not attempted). Search Console data for Italy is not included.

## Method note

- **Requests: about 900**, paced 0.8 s per process. Main run: 118 seeds on G and B, 35 seeds on A, 17 on S. Second run: alphabet suffixes ("seed a" to "seed v", with a space) on G for 10 seeds (app palestra, app scacchi, app allenamento, app scheda palestra, app bollette, app sonno, app promemoria, app blocca, giochi di logica, comprimere video), plus 32 extra gap seeds on G and B and a few probes ("applicazione ..." and "annullare ...").
- **Google suggest: worked** with a browser User-Agent. Very productive for "app palestra" (136 distinct with suffixes), "app allenamento" (154), "giochi di logica" (153), "comprimere video" (137), "app scacchi" (64). Nothing for the privacy/studio themes, shift-work sleep as an "app" query, and most App Store Connect seeds.
- **Bing: `api.bing.com/qsonhs.aspx?mkt=it-IT&q=` worked** (JSON `AS.Results[].Suggests[].Txt`). I did not test osjson. Bing is noisy and often returns the Microsoft Store or Google Play instead of Apple.
- **App Store hints: worked.** `https://search.itunes.apple.com/WebObjects/MZSearchHints.woa/wa/hints?clientApplication=Software&term=<q>` with `X-Apple-Store-Front: 143450-7,29` and `Accept-Language: it-IT` (suffixes -4 and -5 gave the same plist). Hints are Italian and short (single words and two-word seeds); many are brand names, with App Store titles of the form "Nome: parola chiave". Hints contain HTML entities (`&amp;`), decoded here.
- **iTunes Search API (country=it): worked** for 17 competitor searches.
- **People also ask: not collected.** FAQ items below are question-style suggestions from G and B ("come", "non riesco", "quanto tempo").
- **Weak spots (no or only noise results):** "app senza tracciamento", "app che rispettano la privacy", "app che non raccolgono dati", "app che non traccia", "app senza tracker", "sviluppatore app indipendente", "app sviluppatore indipendente", "sviluppatore app finlandia", "app sviluppate in finlandia", "app sonno turnisti", "app sonno infermieri", "turni di notte sonno", "dormire dopo il lavoro notturno" (G), "promemoria bollette app", "app promemoria bollette", "app registro allenamenti", "app sovraccarico progressivo", "ottimizzazione app store", "metadati app store", "parole chiave app store", "rapporti vendite app store", "etichette privacy app store", "sdk di terze parti app", "bloccare app distraienti", "limitare tempo schermo", "app passi per sbloccare app", "errori scacchi", "tattiche scacchi app". For those pages the pick is the closest real phrase and it is said so.
- **App vs applicazione.** "App" is the head word everywhere ("app scacchi", "app palestra", "migliori app iphone"). "Applicazione" also gets suggestions with the same shape ("applicazione scacchi", "applicazione palestra", "migliori applicazioni iphone", "applicazioni senza pubblicità", all G) but it is the long form; no head query exists only in the "applicazione" form. Recommend "app" in titles, H1 and body; "applicazione" once in the description or FAQ for the Apple-formal reading.
- **Accents.** Google keeps the accent in "pubblicità" ("app senza pubblicità", G). It drops apostrophes ("app per limitare l uso del telefono", G). Write "pubblicità", "più", "è" correctly in copy.
- **Italian words seen:** "scheda palestra" and "scheda allenamento" (the training programme; G, B, A: "Hevy: Scheda Palestra Esercizi", "Lyfta: Scheda Palestra"), "diario allenamento" / "diario palestra" (log; G), "registro allenamenti" (A and S titles: "Registro degli allenamenti", "Fitwill: Registro Allenamenti"), "pesi" (G "app per segnare pesi palestra"), "turnista" (A), "turni di lavoro" (A, S, G), "turno di notte" (G), "lavoro notturno" (B: legal and pension results), "debito di sonno" (G, but see aftershift), "scadenzario" (G, B, S: "Scadenzario: Bollette & Debiti"), "bollette" for utility bills, "disdire" (G, B) vs "cancellare" (G) vs "annullare" (G, B) for subscriptions, "rimborso" (G, B), "ripristina acquisti" (G, the in-app button wording), "tempo di utilizzo" (G, B: Apple's Italian name for Screen Time) vs "tempo schermo" (A, S: App Store titles), "giochi di logica" (G, B, S) vs "giochi rompicapo" (G, B, A) vs "giochi puzzle" (G).
- **Good sign:** the Italian App Store already surfaces category terms matching our apps in S: "Sonno per turnisti", "ShiftRest: Sonno Lavoro Turni", "Billo: Promemoria Bollette".

---

## Home (/it/): studio of calm, privacy-first Apple apps

- **Primary:** `app senza pubblicità` (G; A `senza pubblicità` hints, e.g. "sudoku senza pubblicità", "rompicapo senza pubblicità"). Real Italian phrase for "no ads". Caution: the demand is dominated by music and YouTube ("app musica senza pubblicità", "app youtube senza pubblicità", G, B), the same trap as the Spanish page. Pair it with the studio angle; the page really ranks on the brand.
- **Secondary:** `app privacy iphone` (G; noisy, privacy-screen and privacy-report utilities, but the only privacy-flavoured app phrase returned); `applicazioni senza pubblicità` (G, long-form twin, same weak demand).
- **Not usable:** `app senza abbonamento` (G; suggest is music, gym, dating, "app ciclo", telecomando; and the house rule limits "senza abbonamento" to LiftLog, Millrace, Mockly and Tare). Privacy and no-tracking seeds returned nothing (see weak spots). "app senza ads" gave one result (G "app youtube senza ads"); Italians write "pubblicità".
- **FAQ-style (from suggest):** none on-topic. Nearest: `come bloccare la pubblicità su iphone` (B), `come togliere la pubblicità dai giochi` (B), `app per togliere pubblicità` (B).
- **Collision note:** `giochi senza pubblicità iphone` (G) is Millrace's (below), not the Home's.

## Apps hub (/it/apps/): all apps

- **Primary:** `migliori app iphone` (G, B). Generic but the real head phrase; pair with the studio angle in the title.
- **Secondary:** `app utili iphone` (G, B; also `app utili per iphone gratis`, `app più utili iphone`, G); `app indispensabili iphone` (G, B); `migliori app mac` (G, B; also `migliori app macbook`, G); `migliori app apple watch` (G, B).
- **FAQ-style:**
  - migliori app iphone gratis (G)
  - migliori app ipad (G; also "per prendere appunti", "per lavorare", "per studiare", G)
  - migliori app per ipad gratis (B)
  - app utili da scaricare iphone (G)
  - app da avere su iphone (B)
  - app utili per apple watch (B)
  - come scaricare app su apple watch (B)
  - app a pagamento utili iphone (G)
- **Notes:** G mixes in model names and years ("migliori app iphone 17", "2025", "2026"); avoid dated titles. Per-device versions exist for iPad (`migliori app ipad`), Mac (`migliori app mac`, `migliori app macbook`) and Apple Watch (`migliori app apple watch`, `app per apple watch`, B). "Applicazioni" form: `migliori applicazioni iphone` (G).

## About (/it/lagerland-apps/): one-person studio, Finland

- **Primary:** no real query found. The page ranks on the brand "Lagerland Apps". Closest real phrase: `sviluppatore app ios` (G, returned only itself, weak). Recommendation: title on the brand, "sviluppatore indipendente di app" and "Finlandia" in the description by editorial choice, not by demand.
- **Secondary:** none from suggest. B for "studio di sviluppo app" returned agency/React/Visual Studio results ("agenzia it di sviluppo app", "sviluppare app android con visual studio"): wrong intent.
- **FAQ-style:** none on-topic.
- **Not usable:** `sviluppatore app indipendente`, `app sviluppatore indipendente`, `sviluppatore app finlandia`, `app sviluppate in finlandia` (G and B empty or noise, B: "attività da fare in finlandia"). A for "indipendente" returned only newspaper "l'indipendente"; "sviluppatore" returned game titles.
- **Notes:** the Italian word for indie dev is not established in suggest; "sviluppatore indipendente" is the safe plain phrase (not tested as a query). Avoid "freelance". "Software house" and "agenzia" signal agencies.

## Support hub (/it/support/)

- **Primary:** `cancellare abbonamento iphone` (G; also `cancellare abbonamento app iphone`, `come cancellare un abbonamento iphone`, G). Strongest support-type demand. Twins: `annullare abbonamento iphone`, `annullare abbonamento app iphone` (G, B) and `come disdire abbonamento app su iphone` (G). Use "annullare" or "disdire" in H2s and the FAQ so all three verbs appear.
- **Secondary:** `ripristina acquisti` (G; also `ripristinare acquisti app store`, G; `ripristina acquisti apple`, G); `rimborso app store` (G; also `rimborso app store quanto tempo`, `rimborso abbonamento app store`, G); `richiedere rimborso apple` (G; B `come richiedere rimborso apple store`).
- **FAQ-style:**
  - come cancellare un abbonamento iphone (G)
  - come disdire abbonamento app su iphone (G)
  - come disdire un abbonamento app store (G)
  - come annullare abbonamento apple (B)
  - come annullare abbonamento app store (G)
  - come annullare un acquisto su app store (B)
  - come vedere abbonamenti apple (B)
  - abbonamenti apple dove vederli (G)
  - abbonamenti apple attivi (G, B)
  - verificare abbonamenti attivi iphone (G)
  - come gestire abbonamenti app iphone (G)
  - dove trovo abbonamenti app iphone (G)
  - disattivare abbonamenti app iphone (G)
  - ripristina acquisti cosa significa (G)
  - ripristina acquisti significato (G)
  - rimborso app store quanto tempo (G)
  - richiedere rimborso abbonamento app apple (G)
  - rimborso acquisto in app apple (G)
  - condivisione app in famiglia iphone (G)
- **Notes:** most results carry a brand (Spotify, Tinder, Audible, Netflix, CapCut); the generic phrase is the one to target. B tends to the Microsoft Store and Google Play; ignore it for Apple wording.

## Transparency (/it/transparency/): tracking, SDKs, privacy manifests

- **Primary:** `app tracking transparency` (G, B; the English term is what Italians type, also `app tracking transparency apple`, `... ios`, `... iphone`, `... att`, G, B). Developer-heavy results (flutter, framework, permission request).
- **Secondary:** `privacy manifest` (G, B; also `privacy manifest ios`, `privacy manifest apple`, `privacy manifest xcode`, G; B `itms-91061 missing privacy manifest`); `tracciamento app iphone` (G; also `consenti tracciamento app iphone`, `bloccare tracciamento app iphone`, `abilitare tracciamento app iphone`, G).
- **FAQ-style:**
  - consenti tracciamento app iphone (G)
  - bloccare tracciamento app iphone (G)
  - abilitare tracciamento app iphone (G)
  - app tracking transparency cos'è: not returned; nearest `app tracking transparency apple` (G)
  - app privacy report iphone (G: "app privacy report iphone", "resoconto privacy app iphone")
- **Not usable:** `trasparenza app tracciamento`, `consentire alle app di richiedere di tracciare`, `sdk di terze parti app`, `etichette privacy app store` (G empty; B noise, "app per creare etichette"). Apple's own Italian wording "Consenti alle app di richiedere di tracciarti" returned nothing.
- **Notes:** this audience types English terms. Keep "App Tracking Transparency" and "privacy manifest" verbatim, with Italian explanation next to them.

---

## AfterShift (shift-work sleep)

- **Primary:** `dormire dopo il turno di notte` (G; also `come dormire dopo un turno di notte`, `come dormire bene dopo il turno di notte`, `non riesco a dormire dopo il turno di notte`, `non dormire dopo turno di notte`, `quanto dormire dopo il turno di notte`, `cosa prendere per dormire dopo il turno di notte`, G). Strongest real demand for the topic.
- **Secondary:** `non riesco a dormire dopo il turno di notte` (G, problem-form); `come recuperare debito di sonno` (G); `ritmo circadiano e turni notturni` (G, health-intent audience).
- **Caution on `debito di sonno`:** in Italy, G and B return a song/Roblox set ("debito di sonno roblox id", "forsaken", "lyrics", "midi", "loop"; G, B). Do not use it as a secondary; use "debito di sonno" only inside body copy with "come recuperare" (G "come recuperare debito di sonno", B "come recuperare il sonno", "debito di sonno sintomi", G).
- **FAQ-style:**
  - come dormire dopo un turno di notte (G)
  - come dormire bene dopo il turno di notte (G)
  - non riesco a dormire dopo il turno di notte (G)
  - quanto dormire dopo il turno di notte (G)
  - cosa prendere per dormire dopo il turno di notte (G)
  - come recuperare il sonno (B)
  - come recuperare debito di sonno (G)
  - debito di sonno sintomi (G)
  - cosa si intende per lavoro notturno (B)
  - quando il lavoro è considerato notturno (B)
  - lavoro su turni come funziona (B)
  - perché non riesco a dormire di notte (B)
- **Competitors (S, A):** Sonno per turnisti, ShiftRest: Sonno Lavoro Turni, ShiftNight: Monitor del sonno, Peaks: Sonno & Energia, Turno di Notte: Pasti. Roster apps (different intent): Owlday: Turni di Lavoro, ShiftKal: Calendario turni, Shift Note: Calendario Turni, Svegliarino: turni e sveglia, Rota - Turni di lavoro, Megashift, Sheefts, Relevo: Calendario Turni. A hints for "turni": "turni di lavoro", "turni infermieri", "turni polizia", "turnista", "turni di lavoro: calendario ai".
- **Notes:** `app per turni di lavoro` (G, B; also `... infermieri`, `... iphone`, `... gratis`, G) is the roster intent and wins on "app" + "turni"; do not chase it. Seeds `app sonno turnisti`, `app sonno infermieri`, `turni di notte sonno`, `dormire dopo il lavoro notturno` (G) returned nothing. "Lavoro notturno" (B) is legal/pension content, not our topic. `app sonno iphone` (G: 130+ variants, `app sonno apple watch`, `app monitoraggio sonno`) is the generic sleep-tracker space; Observa (part 2) is closer to it than AfterShift.

## AllPaid (bill reminders, no bank login)

- **Primary:** `app promemoria pagamenti` (G; also `app promemoria scadenze pagamenti`, G). Fits the page: bills, rent, subscriptions and contracts, no bank access.
- **Secondary:** `app scadenze bollette` (G); `app per ricordare scadenze bollette` (G; also `app per ricordare scadenze pagamenti`, `app per ricordare le scadenze`, `app iphone per ricordare scadenze`, G); `scadenzario bollette` (G, B; `app scadenzario bollette`, G, B).
- **FAQ-style:**
  - app per ricordare le scadenze (G, B)
  - app per ricordare scadenze bollette (G)
  - app per ricordare scadenze pagamenti (G)
  - app per pagare le bollette (G, B; payment intent, not ours)
  - quali sono le bollette da pagare (B)
  - per quanti anni vanno tenute le bollette (B)
  - come gestire abbonamenti app iphone (G)
  - app gestione abbonamenti (G)
- **Competitors (A, S):** Billo: Promemoria Bollette, Scadenzario: Bollette & Debiti, DueSoon: Promemoria Bollette, Scadenze bollette: DueMinder, BillTo - Gestione Bollette, Organizer Bollette e Scadenze, Organizzatore di bollette, My Home Bills, Subo - Gestione abbonamenti, "bollette: promemoria pagamenti" (A), "billoo bollette", "scadenzario: bollette & debiti" (A).
- **Notes:** `promemoria bollette app`, `app promemoria bollette` (G, B empty) but the exact phrase "Promemoria Bollette" is in S titles, so it is the vocabulary to use in the title area. "Bollette" alone means utility bills; "app bollette" (G) is dominated by energy-supplier apps (Enel, Edison, Hera, Iren) and comparison tools: avoid. `app gestione abbonamenti` (G, A: "gestione abbonamenti") is a subscription-manager space with its own competitors (Subtown, Feenko, Memberwise, Subly); use it only as a feature mention.

## AppMeta (App Store Connect for Mac)

- **Primary:** `app store connect mac app` (G; also `app store connect macos`, `app store connect mac download`, G). English-language niche; demand in Italian is thin and mixed with "cannot connect to App Store" noise.
- **Secondary:** `aso app store` (G, B; also `aso app store keywords`, `aso app store screenshots`, G; B `aso posizionamento app store`); `app store connect app` (B; also G `app app store connect`).
- **FAQ-style:** none in Italian. Nearest: `app store connect account` (B), `app store connect access to reports` (B), `app store connect login` (B).
- **Competitors (A):** Lumetric for App Store Connect, Appdab for App Store Connect, Appdesk per App Store Connect, Appsales for App Store Connect, Helm for App Store Connect, Peek for App Store Connect, Big Bucks for App Store Connect; S returns Apple's own "App Store Connect" app first.
- **Notes:** Italian developer queries are typed in English. Seeds `ottimizzazione app store`, `parole chiave app store`, `metadati app store` (G empty; B noise) returned nothing; use "ASO", "keyword" and "metadati" in body copy only. Do not claim the primary as a ranking target; the realistic goal is brand plus `aso app store`.

## AppMeta Pulse (App Store Connect dashboard on iPhone)

- **Primary:** `app store connect iphone` (G; the exact string is returned, but alongside "cannot connect" noise: "app store connect iphone duo", "app store cannot connect iphone 12"). Weak.
- **Secondary:** `app store connect api` (G, B; also `... api key`, `... api documentation`, `... api issuer id`, G, B); `app analytics app store connect` (G); `app status app store connect` (G).
- **FAQ-style:** none in Italian. Nearest: `app store connect api key` (G), `app store connect api access` (G).
- **Not usable:** `rapporti vendite app store`, `vendite app store connect`, `come vedere le vendite app store`, `app per controllare vendite app store` (G empty; B noise "app per vendere cose", "app store non si connette"). The Italian sales-report intent does not surface.
- **Competitors (A):** see AppMeta (Lumetric, Appsales, Peek, Helm).
- **Notes:** same English-term audience as AppMeta; the page lives on brand and developer-intent words ("proceeds", "MRR", "abbonati"). See collision 2.

## Chessful (chess learning and analysis)

- **Primary:** `app scacchi` (G, B; head phrase, many variants: `app scacchi gratis`, `app scacchi online`, `app scacchi offline`, `app scacchi per principianti`, `app scacchi senza pubblicità`, `app scacchi migliore`, G; B `app scacchi per pc`, `app scacchi free`).
- **Secondary:** `analisi partite scacchi` (G, B; `analisi scacchi`, G, B; `app analisi scacchi`, G); `imparare scacchi app` (G; B `app per imparare a giocare a scacchi`; G `app imparare scacchi`, `app per studiare scacchi`); `app scacchi per principianti` (G).
- **FAQ-style:**
  - come migliorare a scacchi (G, B)
  - come migliorare velocemente a scacchi (G)
  - come migliorare il calcolo a scacchi (G)
  - imparare a giocare a scacchi (G, B)
  - imparare a giocare a scacchi da zero (G)
  - imparare a giocare a scacchi è difficile (G)
  - come vincere a scacchi (B)
  - regole scacchi per principianti (G)
  - tattiche scacchi per principianti (G)
  - scacchi aperture per principianti (G)
  - analisi partite scacchi gratis (G, B)
  - app scacchi per giocare in due (G)
  - stockfish iphone (G; `stockfish chess app iphone`, G)
- **Competitors (S, A):** Scacchi - Giocare ed Imparare, Scuola di scacchi, Scacchi: Motore Stockfish, Analisi Scacchi: Chess AI, MoveSense: Analisi Scacchi, Lotus Chess - Trainer, ChessLab Scacchi, Take Take Take: Scacchi, "Scacchi – Tavola di Analisi", "Scacchi - gioca e impara" (A).
- **Notes:** "app di scacchi" and "app per scacchi" (G alpha) are the same demand. `errori scacchi`, `tattiche scacchi app` (G empty). G's `scacchi analisi grammaticale` is an unrelated school phrase. Chess.com and Lichess are dominant brand-in-query ("analisi scacchi chess com", G). "Scacchi" is also the word Italians use for shogi/xiangqi ("Shogiful: Scacchi giapponesi", S); see collision 3.

## EarnLock (earn screen time by moving: app blocker)

- **Primary:** `bloccare app iphone` (G, B; variants `... con password`, `... figli`, `... tempo`, `... con face id`, `... utilizzo app iphone`, G). Noise: parental controls and app lock by passcode.
- **Secondary:** `app per limitare l uso del telefono` (G, apostrophe dropped; B `come limitare uso smartphone`, `app per limitare utilizzo social`); `tempo di utilizzo iphone` (G, B; Apple's Italian name for Screen Time; also `limite di tempo iphone`, B); `app che blocca il telefono per studiare` (G, alpha).
- **FAQ-style:**
  - come bloccare app iphone (G: "bloccare app iphone")
  - come mettere il blocco alle app iphone (B)
  - come limitare uso smartphone (B)
  - tempo di utilizzo iphone come funziona (G)
  - tempo di utilizzo iphone non funziona (G)
  - come disattivare tempo di utilizzo su iphone (B)
  - codice tempo di utilizzo iphone dimenticato (B)
  - dipendenza da smartphone sintomi (B)
  - cos'è la dipendenza da smartphone (B)
  - app per dipendenza da smartphone (G)
  - app contapassi iphone (G; the step-count side)
- **Competitors (A, S):** Opal: Tempo sullo schermo Focus, AppBlock: Blocco app e siti, Refocus: Blocco app e siti web, one sec: ritardare distrazioni, Stay Focused Blocco App/Siti, Tempozi: Tempo di Utilizzo, Zario: Meno tempo di utilizzo, Blocus: guadagna tempo schermo (A; same mechanic), Reptoll: blocca app, Scroll Goblin: blocca app, "blocca app e tempo schermo" (A), "tempo schermo: dopaminer" (A).
- **Notes:** `blocca app` alone (G, B) is dominated by spam-call blockers, ad blockers and Android/Windows ("blocca app samsung", "app blocca chiamate", G alpha); avoid it. Earn-by-moving seeds returned nothing (`app passi per sbloccare app`, `app per bloccare app fino a fare passi`, `limitare tempo schermo`, `bloccare app distraienti`, G, B empty or noise). The Italian vocabulary is "Tempo di utilizzo" (Apple), "tempo schermo" (App Store titles), "blocco app" (App Store titles). Use all three once.

## GymLogger X (strength workout tracker with Apple Watch)

- **Primary:** `app scheda palestra apple watch` (G; also `app allenamento palestra apple watch`, `app apple watch palestra`, `migliori app palestra apple watch`, G).
- **Secondary:** `app allenamento palestra apple watch` (G); `app allenamento apple watch` (G, B); `app creare scheda palestra` (G; fits the Smart Program Creator; also `app per creare scheda palestra`, `app per creare scheda allenamento palestra`, G).
- **FAQ-style:**
  - app scheda palestra gratis (G)
  - app scheda palestra iphone (G)
  - app scheda palestra fai da te (G)
  - app per segnare la scheda palestra (G)
  - app per registrare scheda palestra (G)
  - app per monitorare scheda palestra (G)
  - app allenamento apple watch non funziona (G)
  - app allenamento apple watch sparita (G)
  - migliori app per apple watch (B)
  - programmi allenamento palestra (G, B)
  - programmi allenamento palestra gratis (G)
- **Competitors (S, A):** Hevy: Scheda Palestra Esercizi, Lyfta: Scheda Palestra, Gym Life - Scheda palestra, Gym Esercizi: Scheda Palestra, GymBook: Scheda Palestra, GymStreak: Personal Trainer IA, Metric - Allenamento Forza, Fitwill: Registro Allenamenti, GYMZO: Diario Allenamento Gym, Technogym, Apple Fitness.
- **Notes:** "scheda" is the key Italian noun (a gym programme card); the Spanish "rutina" equivalent. Seeds `app registro allenamenti`, `app sovraccarico progressivo`, `app palestra senza abbonamento` as a GymLogger target are not usable (GymLogger X has Pro; the no-subscription phrase belongs to LiftLog). `app palestra` head (G) is full of local gym brands (Fitup, Up Level, Fitactive, Athena) and booking apps.

## LiftLog (lifting log, one purchase, no subscription)

- **Primary:** `app diario allenamento palestra` (G; also `app diario palestra`, `app diario palestra gratis`, `migliore app diario allenamento`, G; B `diario di allenamento palestra`). Fits "gym log".
- **Secondary:** `app palestra senza abbonamento` (G; also `app palestra gratis senza abbonamento`, `app allenamento senza abbonamento`, `app allenamento gratis senza abbonamento`, G); `app per segnare pesi palestra` (G; also `app per registrare pesi palestra`, `app per tracciare pesi palestra`, G).
- **FAQ-style:**
  - app per segnare pesi palestra (G)
  - app per registrare pesi palestra (G)
  - app per tracciare pesi palestra (G)
  - diario allenamento palestra excel (G; shows people log in spreadsheets)
  - diario allenamento palestra pdf (G)
  - app per pesi palestra (G)
  - app palestra senza abbonamento (G)
- **Competitors (S, A):** Hevy, Lyfta, Gym Life, GYMZO: Diario Allenamento Gym, Fitwill: Registro Allenamenti, Registro degli allenamenti, Metric - Allenamento Forza, "app calisthenics senza abbonamento" (G).
- **Notes:** this is the only page where "senza abbonamento" is allowed (house rule, and it has real G demand: `app palestra senza abbonamento`, `app allenamento senza abbonamento`). "Pagamento unico" (B `modello di pagamento unico`) did not return app-related phrases, so use "una volta sola" / "acquisto singolo" wording in copy, not as a keyword. `app per pesi` (G) alone is noisy (B: "app per pesare"). See collision 1.

## MediaKit (compress/convert video, images, PDF on device)

- **Primary:** `comprimere video iphone` (G, B; also `... gratis`, `... per whatsapp`, `... con imovie`, `app comprimere video iphone`, `comprimere foto e video iphone`, G).
- **Secondary:** `comprimere pdf iphone` (G, B; `app per comprimere pdf iphone`, G); `convertire video in mp4 iphone` (G, B; also `convertitore video iphone`, `convertitore video iphone in mp4`, G, B); `convertire heic in jpg` (G, B; `... mac`, `... iphone`, `... app`, G, B).
- **FAQ-style:**
  - come comprimere un video su iphone (B)
  - comprimere video senza perdere qualità iphone (B: `comprimere video senza perdere qualità`)
  - comprimere video per whatsapp (G, B `comprimere file video per whatsapp`)
  - comprimere video da inviare via email (G)
  - comprimere video di grandi dimensioni (G)
  - ridurre dimensione video iphone (G)
  - ridurre dimensione video per whatsapp (B)
  - ridurre peso pdf iphone (G)
  - ridurre peso pdf senza perdere qualità (G, B)
  - comprimere pdf gratis con iphone (G)
  - come convertire un video iphone in mp4 (G)
  - convertire video mp4 per iphone (G)
  - comprimere video mac (G; `comprimere video su mac`, `app per comprimere video mac`, G)
- **Competitors (S):** Compressore video - ridurre, Compressione Video Facile, Comprimere Video e Foto Master, Compressore Video - Comprimi, Compress Videos & Resize Video, Il Convertitore Video, Video Converter and Compressor, Convertitore di formato, "pdf compressor", "comprimere pdf: riduci file", "ridurre pdf, comprimere pdf" (A).
- **Notes:** many online-tool brands in suggest (i love pdf, clideo, aranzulla, handbrake, vlc); the on-device, no-upload angle is the differentiator. Vocabulary: "comprimere" (verb), "ridurre peso/dimensione", "convertire", "convertitore". Check before writing that the HEIC tool exists in the app.

## Millrace (tile-delivery logic puzzle; house rule applies)

- **Primary:** `giochi di logica iphone` (G; also `giochi di logica iphone gratis`, `migliori giochi di logica iphone`, G; B `giochi di logica gratis`).
- **Secondary:** `giochi di logica senza pubblicità` (G, B); `giochi puzzle iphone` (G; also `migliori giochi puzzle iphone`, G); `giochi di logica adulti` (G; also `giochi di logica adulti app`, G, to counter the children's results).
- **FAQ-style:**
  - migliori giochi di logica iphone (G)
  - giochi di logica adulti (G)
  - giochi di logica difficili (G alpha)
  - giochi di logica con soluzioni (G)
  - giochi di logica e strategia (G alpha)
  - giochi di logica offline (G)
  - giochi senza pubblicità per iphone (G)
  - migliori giochi iphone senza pubblicità (G)
  - giochi di numeri puzzle (G; the number-building side)
- **Competitors (S, A):** Giochi di Logica - Matematica, Easy Game - Giochi di logica, Impulse - Giochi Mentali, Brain Test: Giochi Mentali, IQ Masters - Rompicapo Mentali, Sudoku.com - Giochi di numeri, "postmark: giochi di logica", "wickhollow: giochi di logica", "daily sum: giochi di logica" (A), "sudoku senza pubblicità", "rompicapo senza pubblicità" (A).
- **Notes:** House rule: never write the digits 2048. "Giochi di logica" is dominated by children, school and printable worksheets ("per bambini", "da stampare", "classe terza primaria", G), so the iPhone and adulti qualifiers matter. `giochi rompicapo iphone` (G, B; `migliori giochi rompicapo iphone gratis`, G) is the closer word for an adult puzzle game; see collision 4. No no-subscription claim needed here beyond what the page already states (Millrace is one of the four allowed).

---

## Summary table

| Page | Primary | Secondary 1 | Secondary 2 |
|---|---|---|---|
| Home | app senza pubblicità (G) | app privacy iphone (G, weak) | applicazioni senza pubblicità (G, weak) |
| Apps hub | migliori app iphone (G, B) | app utili iphone (G, B) | app indispensabili iphone (G, B); also migliori app mac (G, B), migliori app apple watch (G, B) |
| About | brand "Lagerland Apps" (no real query; closest: sviluppatore app ios, G) | none found | none found |
| Support hub | cancellare abbonamento iphone (G); twins annullare / disdire | ripristina acquisti (G) | rimborso app store (G); also richiedere rimborso apple (G, B) |
| Transparency | app tracking transparency (G, B) | privacy manifest (G, B) | tracciamento app iphone (G) |
| aftershift | dormire dopo il turno di notte (G) | non riesco a dormire dopo il turno di notte (G) | come recuperare debito di sonno (G); avoid bare "debito di sonno" (song) |
| allpaid | app promemoria pagamenti (G) | app scadenze bollette (G) | app per ricordare scadenze bollette (G) |
| appmeta | app store connect mac app (G) | aso app store (G, B) | app store connect app (B) |
| appmeta-pulse | app store connect iphone (G, weak) | app store connect api (G, B) | app analytics app store connect (G) |
| chessful | app scacchi (G, B) | analisi partite scacchi (G, B) | imparare scacchi app (G) |
| earnlock | bloccare app iphone (G, B) | tempo di utilizzo iphone (G, B) | app per limitare l uso del telefono (G) |
| gymlogger-x | app scheda palestra apple watch (G) | app allenamento palestra apple watch (G) | app creare scheda palestra (G) |
| liftlog | app diario allenamento palestra (G) | app palestra senza abbonamento (G) | app per segnare pesi palestra (G) |
| mediakit | comprimere video iphone (G, B) | comprimere pdf iphone (G, B) | convertire video in mp4 iphone (G, B) |
| millrace | giochi di logica iphone (G) | giochi di logica senza pubblicità (G, B) | giochi puzzle iphone (G) |

## Collisions and who keeps what

1. **Gym family: `app palestra ...` (gymlogger-x vs liftlog).** `app scheda palestra` / `app allenamento palestra` (programme and Apple Watch side) go to gymlogger-x. `app diario ...` / `app per segnare pesi palestra` / `senza abbonamento` go to liftlog, the only page allowed to say "senza abbonamento". Neither page targets bare `app palestra` (local gym brands and booking apps).
2. **App Store Connect family (appmeta vs appmeta-pulse, and Transparency's `app store connect`-free terms stay separate).** appmeta keeps `app store connect mac app` and `aso app store`. appmeta-pulse keeps `app store connect iphone`, `app store connect api` and `app analytics app store connect`. Bare `app store connect app` (B) is a shared secondary; give it to appmeta, and let pulse use "dashboard", "ricavi", "abbonati" in body copy.
3. **"Scacchi" family (chessful vs the Part 2 pages Shogiful and Xiangqiful).** chessful owns `app scacchi`, `analisi partite scacchi`, `imparare scacchi app`. Shogiful and Xiangqiful must use "scacchi giapponesi" and "scacchi cinesi" (or "xiangqi", "shogi") and must not target bare "scacchi". S already shows "Shogiful: Scacchi giapponesi".
4. **Logic-puzzle family (millrace vs Part 2 Tare).** Same pattern as the Spanish decision. Millrace keeps `giochi di logica iphone`; recommend Tare takes `giochi rompicapo iphone` (G, B; Tare's English wording is "rompicapo"), and `giochi puzzle iphone` stays with Millrace only if Tare does not also use it. Whoever writes Part 2 should check `it-keywords-p2` for the actual Tare pick.
5. **Home vs Millrace on "senza pubblicità".** Home keeps `app senza pubblicità`; Millrace keeps `giochi di logica senza pubblicità`. `giochi senza pubblicità iphone` (G) is a free-standing phrase: Millrace may use it in the description, Home must not.
6. **Home vs Apps hub on "app ... iphone".** Home does not target `migliori app iphone` or `app utili iphone`; both stay with the Apps hub.
7. **aftershift vs Observa (Part 2) on sleep.** `app sonno iphone` / `app monitoraggio sonno` (G) go to Observa; aftershift stays on turni di notte wording.
8. **Support hub vs app support pages.** Support hub keeps `cancellare/annullare/disdire abbonamento iphone`, `ripristina acquisti` and `rimborso app store`; each app's own support page should stay on the app name plus the same verbs, not on the bare head phrases.


---

# Keyword research, Italian (Italy), Part 2: mockly to clippet

Tier 1 app pages: Mockly, Observa, Pawza, RightSplit, Shogiful, Soon., Tare, Taskful Day, WanderWiki, Xiangqiful,
Clippet. Format follows `_i18n/es-keywords.md` Part 2. Never published (`_i18n` is excluded from the build).

Collected 2026-11-19. Source marks: **G** = Google suggest (hl=it, gl=it), **B** = Bing autosuggest (mkt=it-IT),
**A** = App Store search hints (Italian storefront 143450), **S** = iTunes Search API (country=it, lang=it_it), used
only for competitor names and the vocabulary of Italian app titles. Every query below was returned by one of these
sources; nothing was invented. Accents are kept as the source returned them: Google often drops the apostrophe or accent
(`cos è`, `variabilita cardiaca`) next to the accented form (`cos'è`, `variabilità`); Bing and the App Store keep them.
Search Console data is not included.

## Method note

- **Requests: about 840.** Pass 1 (about 670): base seeds per app on G, B and A, plus alphabet suffixes (a b c d e f g h
  i l m n o p r s t v, G only) on 8 seeds: `hrv apple watch`, `libretto sanitario cane`, `dividere il conto`,
  `app dividere le spese`, `shogi`, `conto alla rovescia iphone`, `countdown`, `app to do list`, `app lista attività`,
  `wikipedia casuale`, `scacchi cinesi`, `cronologia appunti iphone`, `appunti iphone`, `clipboard manager`; plus 30 S
  searches (2 to 4 per app). Pass 2 (about 165): question-form and gap seeds on G, B, A, plus 4 S. About 0.8 s between
  requests, browser User-Agent, no personal data sent.
- **Google suggest: worked.** Best source. Alphabet suffixes were useful on `libretto sanitario cane`, `dividere il conto`,
  `app dividere le spese`, `hrv apple watch` (mostly English, German and Polish noise), `conto alla rovescia iphone`;
  empty or noise on `app lista attività`, `wikipedia casuale` (the head term has only 6 suggestions), `cronologia appunti
  iphone` and `scacchi cinesi` (a handful each).
- **Bing `qsonhs.aspx?mkt=it-IT`: worked** (the endpoint named in the brief; I did not need the osjson variant). Bing is
  noisy and drifts to English, Spanish, German and generic phrases ("control del sueño apple watch", "hrv messung apple
  watch", "come resettare un apple watch"), and often returns only generic head-term completions for long seeds. Used
  mainly to confirm Google.
- **App Store hints (Italy): worked, for short seeds.** Storefront `143450-7,29`. Tested `143450-4,29` and `143450-1,29`
  on `scacchi`: identical output, so the language suffix makes no difference and `-7` was used throughout. Output parsed
  from the `<string>` entries of the plist; URLs and the "Suggestions" label dropped. Empty for almost every 3+ word seed
  and every question. Useful hits: `conto alla rovescia` (+ natale, giorni, widget, matrimonio, pensione), `countdown
  iphone`, `app countdown`, `app conto alla rovescia`, `app to do list`, `lista cose da fare`, `dividere spese`, `app per
  dividere le spese`, `libretto sanitario cane`, `scacchi cinesi`, `xiangqi`, `shogi`, `variabilità cardiaca`, `gestore
  appunti`, `giochi di logica`.
- **iTunes Search API (country=it, lang=it_it): worked.** Seller names are left out. Shows that our own apps already
  rank under Italian titles: "Shogiful: Scacchi giapponesi", "Xiangqiful: Scacchi Cinesi", "Tare: Puzzle Logico
  Rilassante".
- **People also ask: not collected.** It needs a live Google results page behind a consent wall; scripted fetches cannot
  get past it and I did not try to get around it. FAQ lines below come from question-form autocomplete (`come`, `cos'è`,
  `dove`, `quanto`, `come si gioca`) on G and B.
- **"app" vs "applicazione":** Italians type `app` ("app per dividere il conto", "app conto alla rovescia", "app lista
  attività"); `applicazione` appears rarely (`applicazione conta giorni` G, `applicazione mobile per la salute` B).
  Use "app" in titles and H1, "applicazione" in body text if variety is wanted.
- **English in Italian queries:** very common. Italians type `to do list`, `countdown`, `widget`, `clipboard manager`,
  `screenshot`, `mockup`, `hrv`, `wikipedia random`. The Italian head terms exist next to them: `conto alla rovescia`,
  `appunti`, `lista cose da fare`. Titles can carry the English term, body copy the Italian one.
- **"iPhone" vs "iOS":** `iphone` dominates (`conto alla rovescia iphone`, `giochi rompicapo iphone`, `app agenda
  iphone`); `ios` appears rarely.
- **Year/model variants** (`iphone 17`, `iphone 18`, `natale 2026`, `agenda 2026`) avoided per house style.
  `gratis` variants exist almost everywhere; they are noted only where a free tier is real (Observa, Pawza, RightSplit,
  Shogiful, Soon., Tare, Taskful Day, WanderWiki, Xiangqiful, Clippet are free to start; Mockly is a paid one-time app).
- **Nothing found at all** (empty on G, B and A): `app recupero allenamento`, `app vaccini cane`, `passaporto animali
  app`, `puzzle bilancia gioco`, `scansiona scontrino app`, `app planner giornaliero`, `scacchi giapponesi app`,
  `shogi iphone`, `imparare shogi` (only itself on G), `scacchi cinesi app`, `imparare scacchi cinesi`, `scacchi cinesi
  iphone`, `scacchi cinesi problemi`, `gestor(e) appunti mac`, `gestione appunti mac`, `articoli casuali wikipedia`,
  `app wikipedia casuale`, `app lista attività` (only itself on B), `imparare xiangqi`.
- **Misleading seeds to avoid:** `dividere il conto` alone (translation phrases: "in inglese", "in spagnolo", "in
  francese"; bank accounts: "dividere conto corrente cointestato"), `app dividere il conto` on Bing (PDF, file audio, bank
  account, desktop), `hrv` alone (Croatia: "hrvatska", Honda HR-V, Garmin "hrv status"), `hrv apple watch` alphabet
  (English/German/Polish), `countdown` alone (film "Countdown", GTA 6, serie TV, "mezzanotte"), `conto alla rovescia`
  alone (GTA 6, Natale, film), `giochi di equilibrio` (children's physical games), `gioco della bilancia` (Alice in
  Borderland), `wikipedia casuale` (statistics "variabile casuale"), `wikipedia a caso` (news: "caso garlasco"), `app
  planner` (5D Planner, Microsoft Planner), `appunti mac` (university lecture notes: "appunti macroeconomia"), `appunti
  iphone` (the Notes app and where the clipboard lives), `shogi` letters (Persona 5, Yakuza, Shogun, Shoghi Himachal),
  `scacchi cinesi` (avorio, amazon, antichi, "go"), `mockup` alone (T-shirt, denti, libro), `app per cani` (barking
  ultrasound apps).

---

## Mockly (App Store screenshots on Mac)

- **Primary:** `screenshot app store` (G, B). Italian developers keep the English "screenshot". G returns `screenshot app
  store generator`, `... size`, `... connect`; B returns `app store screenshot generator`, `app store screenshot maker`.
- **Secondary:** `app store screenshot generator` (G, B); `mockup app store` (G, B); `app store screenshot maker` (B);
  `app store connect screenshot` (G: sizes, requirements, dimensions, generator). Optional: `app per creare mockup` (G, B;
  generic mockup intent), `mockup iphone app store` (G).
- **Not usable:**
  - `creare screenshot app store`, `generatore screenshot app store`, `dimensioni screenshot app store` (only itself on G),
    `app per screenshot app store`: Italian forms give no store-screenshot results; B drifts to phone screenshot help
    ("come fare screenshot con android", "app per fare screenshot pc").
  - `mockup iphone` (G, B): year and model variants (`17`, `18`, `fold`), PNG/PSD/Figma/free intent; Mockly is a paid Mac app.
  - `mockup` alone (G, B, A): T-shirt, "mockup denti", "mockup libro" noise.
  - `... free`, `... figma`, `... psd`, `... template` (G, B): free and template intent.
  - "senza abbonamento": allowed for Mockly (one-time purchase), but no returned query contains it.
- **FAQ-style (from suggest).** No Italian question forms came back; the questions are English developer ones:
  - app store connect screenshot sizes / dimensions / requirements / guidelines (G)
  - app store connect screenshots not uploading (G)
  - app store screenshot size (G)
  - app to make app store screenshots (B)
  - come si scrive mockup / cosa si intende per mockup / come fare un mockup (B, generic)
- **Competitors (S):** SMPRO: Mockup & Screenshot, Mockup Screenshot, Screenshot Studio - App Mockup, Picasso App
  Screenshot Studio, StoreView: App Screenshot Tool, App Screenshots Maker, Mockup e Demo: Screeny, Creatore di mockup -
  Mockitup. A hints for `mockup`: "mockup generator - mocksy ai", "mockups: screenshots & video", "device studio - mockups".
- **Notes:** Same pattern as Spanish and French: keep "screenshot" and "mockup" in title and H1, "schermate" in body
  (not returned by any source, so use sparingly). Hardly any query names Mac. Demand is small and English; this page
  cannot expect Italian-language volume.

## Observa (sleep, HRV, recovery from Apple Health; HRV is SDNN)

- **Primary:** `hrv apple watch` (G, B). Italians keep "HRV" in Latin letters; G returns `valori normali`, `dove si trova`,
  `app`.
- **Secondary:** `variabilità della frequenza cardiaca` (G, B; also `variabilità frequenza cardiaca` B, `variabilità
  cardiaca` G, B, A, `variabilità della frequenza cardiaca (hrv)` G); `app sonno apple watch` (G; also `migliore app sonno
  apple watch` G, `app monitoraggio sonno apple watch` G); `hrv valori normali` (G, B; also `hrv valori normali apple
  watch` G); `hrv sonno` (G, B). Optional: `app hrv apple watch` (G; mostly English completions), `qualità del sonno apple
  watch` (G).
- **Not usable:**
  - `hrv` alone (G, B): Croatia, Honda, Garmin `hrv status`. `hrv cos'è` returns Garmin and `hrv cos è paese` noise but
    is usable as an FAQ line with the health wording `hrv sonno cos è` (G) or `hrv cuore cos è` (G).
  - `readiness apple watch` (G, B): English and device compatibility ("ultra 3", "not showing"); no Italian "readiness"
    demand. `punteggio recupero apple watch` and `app recupero allenamento`: empty on G and A, B drifts to resetting the watch.
  - `app stress apple watch` (G, B): usable demand (`app stress apple watch gratis`, `app per stress apple watch` G) but
    stress is a secondary feature; Observa's stress read is not the headline.
  - `hrv rmssd valori normali` (G): never write RMSSD. Observa's HRV is SDNN (`hrv sdnn valori normali` G exists).
  - "senza abbonamento" does not apply to Observa (Premium).
- **FAQ-style (from suggest):**
  - hrv cos'è (G, B) / hrv cos'è e come funziona (G) / hrv cosa indica (B) / hrv cosa misura (B)
  - hrv cos è come si misura (G)
  - hrv valori normali (G, B) / hrv apple watch valori normali (G) / hrv sdnn valori normali (G)
  - hrv apple watch dove si trova (G)
  - come migliorare hrv (G) / come migliorare il proprio hrv (G)
  - variabilità della frequenza cardiaca valori normali (G) / durante il sonno (G) / alta, bassa (G)
  - hrv sonno valori / alto / basso / significato (G)
  - come misurare qualità del sonno apple watch (G) / come monitorare la qualità del sonno con apple watch (G)
  - dove si trova hrv su apple watch (G; "misura hrv con apple watch" G)
- **Competitors (S):** Welltory: Battito cardiaco, StressWatch: Analisi stress AI, Stress Monitor: HRV & salute, HRV4Training,
  HRV-Tracker, Athlytic: Fitness & Recovery, HeartWatch: Frequenza Cardiaca, Variabilità Cardiaca, Emuqu: Variabilità
  cardiaca, Bevel: Coach Salute IA, AutoSleep: Monitoraggio Sonno, Sleep Cycle, Pillow: Tracker del sonno.
- **Notes:** Italian vocabulary: "variabilità della frequenza cardiaca" (full), "variabilità cardiaca" (App Store and G
  short form), "frequenza cardiaca" (not "battito", though app titles use "Battito cardiaco"); "sonno" (not "sueño");
  "HRV" is the abbreviation people type (not "VFC"). No "readiness"/"recupero" query exists as head term; "recupero"
  appears only as `variabilità della frequenza cardiaca di recupero` (G). Always "(SDNN)" in the explanation.

## Pawza (pet health records, vaccines, vet documents)

- **Primary:** `libretto sanitario cane` (G, B, A; plus `libretto sanitario gatto` G, B). Highest-demand term of the
  pet topic; G offers `digitale`, `online`, `app`, `cos'è`, `obbligatorio`. A hint: `libretto sanitario cane gatto`.
- **Secondary:** `libretto sanitario cane digitale` (G; also `libretto sanitario elettronico cane` G);
  `app libretto sanitario cane` (G, as `libretto sanitario cane app` and `app per libretto sanitario cane`; `app
  libretto veterinario` G); `libretto sanitario gatto` (G, B); `calendario vaccinazioni cane` (G; also `calendario vaccini
  cane` G). Optional: `app veterinario` (G), `app per cani` (G; low fit, mostly barking/training).
- **Not usable:**
  - `libretto sanitario cane da stampare / pdf / fac simile / personalizzato / copertina / custodia / porta` (G, B):
    printable template or accessory intent.
  - `libretto sanitario cane smarrito`, `ho perso libretto sanitario cane`, `rifare`, `duplicato`, `chi lo rilascia`,
    `costo` (G): lost/replacement and official-booklet-issuing intent; the Pawza page can answer a few as FAQ, but the
    queries are about the paper document.
  - `libretto sanitario` alone (B): `come scaricare libretto sanitario`, `dove trovare il libretto sanitario` are the
    human health card (tessera sanitaria), not pets. Same for `libretto vaccinale app io` (B).
  - `app salute animali domestici` (B only noise: "polizza sanitaria animali domestici"), `app cani e gatti salute` (B
    noise), `app vaccini cane` and `passaporto animali app` (empty), `app per gatti salute` (B noise).
  - `app per cani` (G, B, A): barking ultrasound, lost dogs, training.
- **FAQ-style (from suggest):**
  - libretto sanitario cane cos'è (G) / libretto sanitario cane è obbligatorio (G)
  - come fare il libretto sanitario al cane (G) / come richiedere libretto sanitario cane (G)
  - quanto costa fare il libretto sanitario al cane (G)
  - libretto sanitario cane chi lo rilascia (G)
  - come recuperare il libretto sanitario del cane (G) / se perdo il libretto sanitario del cane (G)
  - libretto sanitario cane digitale (G) / libretto sanitario cane online (G, B)
  - libretto sanitario cane in inglese (G) / passaporto e libretto sanitario cane (G)
  - cane senza libretto sanitario (G)
  - libretto sanitario gatto obbligatorio (G) / libretto sanitario gatto online (G, B)
  - calendario vaccinazioni cucciolo cane (G)
- **Competitors (S):** Pawsly: Libretto Cane e Gatto, Miyu: Libretto Sanitario Cane, Libretto Cane - PupPlan, Friendly -
  Libretto Animali, Faunora - Libretto animali, Libretto Sanitario: Cat-a-log, Pidoy: Libretto sanitario pet, MyVet,
  Petium - Salute del tuo pet, Pettify: Diario Salute Animali, Paws - Cartella Sanitaria Pet, Medika - Cartella clinica.
- **Notes:** The Italian term is "libretto sanitario" (also "libretto delle vaccinazioni"), almost never "cartella";
  "animali domestici"/"pet"/"animali" are all in use, "cane e gatto" is the usual pair. Pawza covers more than dogs and
  cats; the page title can lead with "libretto sanitario cane e gatto" and name other pets in the body. The booklet is
  legally a paper/official document: the page should say Pawza keeps the digital record and does not replace the
  official one (copy-editing check, not a keyword issue).

## RightSplit (split the bill from a receipt, tips)

- **Primary:** `app per dividere il conto` (G; also `app dividere conto` G, `app per dividere il conto al ristorante` G).
  The bare `dividere il conto` is mostly translation phrases; the "app" form removes that.
- **Secondary:** `app per dividere il conto al ristorante` (G, three times in alphabet runs); `dividere il conto alla
  romana` (G; also `cosa significa dividere il conto alla romana` G); `app per dividere le spese` (G, B, A; strong,
  but expense-sharing: also `... tra amici`, `... in viaggio`, `... di coppia`, `... coinquilini`); `dividere spese app`
  (G). Optional: `come dividere il conto al ristorante` (G), `app per dividere le spese tra amici` (G, B).
- **Not usable:**
  - `dividere il conto in inglese / spagnolo / francese / tedesco`, `possiamo dividere il conto`, `puoi dividere il
    conto` (G): translation and phrasebook intent.
  - `dividere conto cointestato / conto corrente` (G): bank accounts. `dividere il conto con revolut / paypal` (G): bank
    app transfers (usable only as a body FAQ about PayPal.me/Revolut links).
  - `app dividere il conto` (B): PDF, file audio, desktop, "conto economico".
  - `calcolatrice dividere conto ristorante` (B): arithmetic with remainder.
  - `splitwise alternativa` (G): fits the alternatives pages, not this one.
  - `app per dividere spese netflix / spotify / auto / abbonamento` (G): subscription-sharing intent.
  - `scansiona scontrino app`, `dividere conto scontrino` (G, B empty; only S titles).
- **FAQ-style (from suggest):**
  - cosa significa dividere il conto alla romana (G) / cosa vuol dire dividere il conto alla romana (G)
  - come dividere il conto al ristorante (G)
  - come dividere il conto con revolut (G) / dividere conto paypal (G)
  - come dividere il conto con the fork (G)
  - come si chiama app per dividere le spese (G)
  - come dividere le spese (B) / come dividere le spese in famiglia (B)
  - migliore app per dividere le spese (G)
  - app per dividere le spese senza registrazione (G; fits "no account")
  - app per dividere equamente le spese (G) / app per dividere le spese in percentuale (G)
- **Competitors (S):** tricount - Spese condivise, Splitwise, Splid - Dividi le spese, Settle Up, Banana Split, Divvy,
  Splitcar, SplitPal - Dividi il Conto, Receipt Split: Dividi il Conto, Conto: Dividi lo Scontrino, ilConto, QuickSplit -
  Dividere il conto, IOU: Dividi Scontrini e Spese, CheqSplit, Dividi il conto: Pezzo. A hints for `dividere spese`:
  "sharecost: dividere spese", "share: dividere spese e conto".
- **Notes:** Italian vocabulary: "dividere il conto" (restaurant bill), "alla romana" (equal split, the cultural
  default), "dividere le spese" (shared costs, trips, flatmates), "scontrino" (receipt), "mancia" (tip; not returned by
  any source, so not a keyword). The "senza registrazione" phrasing supports the no-account claim.

## Shogiful (shogi / Japanese chess, learn and analyze)

- **Primary:** `shogi` (G, B, A). Italians use the Japanese word; head term has `shogi regole`, `shogi online`, `shogi
  pezzi`, `shogi gioco`, `shogi giapponese`.
- **Secondary:** `scacchi giapponesi` (G, B, A; G also `scacchi giapponesi regole`, `scacchi giapponesi online`, `scacchi
  giapponesi shogi`; A "shogiful: scacchi giapponesi"); `shogi regole` (G, B: `shogi regole base`, `shogi regole
  avanzate`); `come si gioca a shogi` (G; `shogi come si gioca` G); `shogi online` (G, B). Optional: `shogi pezzi` (G),
  `shogi app` (G, B; English completions).
- **Not usable:**
  - `shogi` + persona 5 / yakuza / anime / naruto / mod / temperature / shoji / shoghi (G): games, anime, unrelated
    names; `shogun` and `showgirl` appear as near-miss corrections.
  - `shogi app` (G, B): all English completions ("shogi app yakuza", "shogi app for beginners").
  - `scacchi giapponesi vintage`, `nome` (G): antiques.
  - `shogi iphone`, `scacchi giapponesi app`, `imparare shogi` (only itself), `shogi per principianti` (B: "shogi online
    per principianti"): thin or empty.
  - `shogi vs chess / go / xiangqi` (G): English comparison; fits comparison pages.
- **FAQ-style (from suggest):**
  - come si gioca a shogi (G) / shogi come si gioca (G)
  - shogi regole (G, B) / shogi regole base / avanzate (B) / shogi regole pdf (G)
  - scacchi giapponesi regole (G) / scacchi giapponesi nome (G)
  - shogi pezzi (G)
  - shogi online (G, B) / shogi online per principianti (B)
  - shogi vs chess which is harder (G, English), shogi or chess (G, English)
- **Competitors (S):** Shogi ™, PiyoShogi, Shogi Wars, Shogi Quest Online, Shogi Lv.100 Entry Edition, Everybody Shogi,
  Shogi Master, Maestro dello Shogi Classico, 81Dojo, "Scacchi - Giocare ed Imparare". Our own "Shogiful: Scacchi
  giapponesi" is already in S and A. A hints for `shogi` list Shogi Lv.100, Shogi Wars, Shogi Live, Shogi Demon.
- **Notes:** Vocabulary: "scacchi giapponesi" (descriptor) next to "shogi" (name). The Italian query for rules is
  `shogi regole`, so the FAQ headings can use "regole" and "come si gioca". Do not use "scacchi" alone (chess apps).
  Keep "kanji" and "pezzi" in body copy.

## Soon. (countdown app and widgets)

- **Primary:** `conto alla rovescia iphone` (G; also `app conto alla rovescia iphone` G, `widget conto alla rovescia
  iphone` G, `conto alla rovescia giorni iphone` G). A hint for `countdown iphone` exists, so the English form is also real.
- **Secondary:** `widget conto alla rovescia` (G, B, A: also `conto alla rovescia widget gratis` A); `app conto alla
  rovescia` (G, B, A; G adds `giorni`, `viaggio`, `matrimonio`, `pensione`, `natale`); `countdown iphone` (G, B, A);
  `app countdown` (G, B, A; G: `app countdown giorni`, `viaggi`, `widget gratis`). Optional: `contagiorni app` (G; `app
  contagiorni iphone` G), `app per contare i giorni mancanti` (G: `app per contare i giorni che mancano`), `app conto alla
  rovescia matrimonio` (G, A), `widget countdown iphone` (G).
- **Not usable:**
  - `conto alla rovescia` alone, `countdown` alone (G, B): GTA 6, Natale, mezzanotte, films, "Countdown" series, lyrics.
  - `conto alla rovescia online / windows / download / video` (G, B): browser or PC intent.
  - `conto alla rovescia iphone` + camera words (B "attivare conto rovescia fotocamera iphone", G `conto alla rovescia
    sveglia iphone`): timer for photos/alarm.
  - `app countdown è vera`, `app countdown morte`, `countdown app morte` (G): "death countdown" apps.
  - `app per contare i giorni` + `astinenza`, `senza fumare`, `dieta`, `fidanzamento` (G): sobriety, diet, relationship trackers.
  - `giorni mancanti` + `pasqua`, `fine della scuola` (B): date lookups, not apps.
  - `conto alla rovescia natale` (G, B, A): seasonal head term; Soon. covers it but it is not the evergreen intent.
- **FAQ-style (from suggest):**
  - come fare il conto alla rovescia su iphone (G) / come inserire conto alla rovescia su iphone (G) / come mettere
    conto alla rovescia su iphone (G) / come aggiungere un conto alla rovescia su iphone (G)
  - come mettere il conto alla rovescia dei giorni su iphone (G)
  - come mettere widget conto alla rovescia (G)
  - impostare conto alla rovescia iphone (G)
  - quanti giorni mancano a natale app (G) / app per vedere quanti giorni mancano alla fine della scuola (G)
  - app per contare i giorni da una data (G)
- **Competitors (S):** Countdown App, Countdown Star, Countdown Buddy, Big Days - Countdown Eventi, TimeCount - Countdown &
  Widget, Conto alla rovescia - Widget, Conto alla rovescia con widget, Conto alla rovescia widgets, Conto alla rovescia
  - Giorni, Time Progress: Giorni Mancanti, Countdown Widget Plus, Calendario del Conto Rovescia, DayDrop (A).
- **Notes:** Italian says "conto alla rovescia" (not "conteggio"), with "giorni mancanti" and "contagiorni" as
  secondary terms; "countdown" is a loanword used mostly for TV and events and for the widget niche
  (`widget countdown iphone`). "Widget" is used as-is. "Matrimonio", "vacanze", "viaggio", "pensione" (retirement),
  "compleanno" are the occasions people type; the page lists trips, weddings, birthdays, exams and a baby's due date.

## Tare (balance logic puzzle game)

- **Primary:** `giochi rompicapo iphone` (G; `migliori giochi rompicapo iphone` G; B `giochi rompicapo gratis iphone`).
  Chosen to avoid the head terms that Millrace most likely claims (`giochi di logica iphone`, `giochi puzzle iphone`).
- **Secondary:** `giochi senza pubblicità iphone` (G; also `migliori giochi iphone senza pubblicità` G); `giochi offline
  iphone` (G; `migliori giochi offline iphone` G); `giochi rilassanti iphone` (G; `giochi rilassanti iphone gratis`).
  Optional: `giochi di equilibrio` (G, B: wrong intent, physical games for children), `gioco della bilancia` (G:
  Alice in Borderland, so do not use).
- **Collision (flag):** `giochi di logica iphone` (G, one hit; `migliori giochi di logica iphone`) and `giochi di logica`
  (G, B, A) are the natural head terms for a logic puzzle game, and Millrace is the other logic puzzle game. Recommendation:
  Millrace takes `giochi di logica iphone`; Tare takes `giochi rompicapo iphone`. Both pages can still use "puzzle
  logico" in body copy (the S title of Tare is "Tare: Puzzle Logico Rilassante"). `giochi puzzle iphone` (G) is a second
  shared term; leave it to Millrace.
- **Not usable:**
  - `giochi di logica` alone (G, B, A): children, school, online, printable ("per bambini", "prima media", "wordwall").
  - `giochi di ingegno iphone`, `giochi di deduzione iphone`, `giochi di pesi e bilancia`, `puzzle bilancia gioco`,
    `giochi di logica ios`, `giochi di logica offline` (G/B/A): empty or generic B drift.
  - `giochi di logica senza pubblicità` (G, one hit): too close to the Millrace term.
  - `giochi di equilibrio` (G, B): `per bambini`, `da tavolo`, `in legno`, `film`.
  - "senza abbonamento": allowed for Tare (free first 20 levels, one purchase), but no returned query contains it. The
    phrase `giochi senza pubblicità iphone` carries the "no ads" angle.
- **FAQ-style (from suggest).** No question forms returned for this topic. Closest:
  - migliori giochi rompicapo iphone (G) / migliori giochi rompicapo iphone gratis (G)
  - migliori giochi offline iphone (G) / giochi iphone offline per aereo (G)
  - migliori giochi iphone senza pubblicità (G)
  - giochi offline senza internet iphone (G)
- **Competitors (S):** Mobilo: Puzzle di equilibrio, Aplomb: Puzzle di equilibrio, Tilting Scales, Nanobot Balance, Puntari:
  Equilibrio Cinetico, Levarium, Redirect It - Rompicapo Logico, Giochi di Logica - Matematica, Rooms & Exits-Gioco di
  Logica, Impulse - Giochi Mentali, Brain Test, IQ Masters - Rompicapo Mentali, Orologiaio: giochi rompicapo, Puzzle -
  Rompicapo rilassanti. Our own "Tare: Puzzle Logico Rilassante" appears in S for `gioco di logica bilancia`.
- **Notes:** Italian vocabulary: "gioco di logica", "rompicapo", "puzzle", "giochi di ingegno" (nothing returned); the
  game's own words "bilancia" (scale), "peso/pesi" (weights), "equilibrio". Never "senza parole" as a keyword (no query).
  "Bilancia" in queries is also the zodiac sign and kitchen scales; the page must describe the beam-and-weights puzzle in
  the first line.

## Taskful Day (day planner / to-do list, iPhone + Mac)

- **Primary:** `app to do list` (G, B, A). Italians type the English term; G: `iphone`, `gratis`, `condivisa`, `mac`.
- **Secondary:** `app per organizzare la giornata` (G, B; also `... iphone gratis`, `... apple`, `... ipad`);
  `app per pianificare la giornata` (G, B); `agenda giornaliera app` (G, B); `app to do list iphone` (G; B `to do list
  app iphone`). Optional: `lista cose da fare app` (G as `lista delle cose da fare app`; B `app lista cose da fare`; A
  `lista cose da fare`), `app agenda iphone` (G, B), `app per fare liste` (G, B), `app promemoria iphone` (G).
- **Not usable:**
  - `app lista attività` (B only itself) and its whole alphabet (empty): the phrase is not how Italians search.
  - `app planner giornaliero` (empty on all three); S vocabulary shows the term in app titles ("MyDay - Planner
    Giornaliero"). `app planner` alone (G, B, A): 5D Planner, Microsoft Planner, budget planners.
  - `app to do list` English completions (`to do list app for neurodivergent`, `app to do list adhd`, `... github html css`):
    developer and English-language noise. `app to do list apple watch` (B English).
  - `lista cose da fare` alone (G, B, A): wedding, printable, "prima di morire", PDF, Excel.
  - `app produttività iphone` (G): thin head term, but it fits as an optional body term.
  - "senza account": no returned query; the claim "nessun account" is supportable from the blueprint but not from search data.
- **FAQ-style (from suggest):**
  - migliore app to do list (G) / migliori app per organizzare la giornata (G) / migliori app per pianificare la giornata (G)
  - app to do list condivisa (G) / app to do list gratis (G)
  - app per organizzare la giornata gratis (G, B)
  - come organizzare la giornata (B) / come organizzare la propria giornata (B)
  - app per organizzare la settimana (B)
  - migliori app produttività iphone (G)
  - app to do list apple watch (G as `to do list app apple watch`)
- **Competitors (S):** Todoist: To do list-Calendario, Any.do: To do list & Planner, Microsoft To Do, TickTick, Structured -
  Agenda Calendario, Tasks - Attività & Promemoria, MyDay - Planner Giornaliero, Planner Giornaliero: Brite, Agenda
  giornaliera - Diario, Actions: Lista Attività, Lista attività: CoreTask, Daylist - Lista degli impegni, LockDay: Lista
  cose da fare.
- **Notes:** Italian vocabulary: "to do list" (English, dominant), "lista cose da fare" / "elenco di cose da fare" (B),
  "attività" (tasks), "impegni", "agenda" (planner), "promemoria" (reminders), "organizzare/pianificare la giornata".
  "Planner" is used for the daily calendar form. The page's differentiator (unfinished tasks carry forward) has no
  query demand of its own.

## WanderWiki (swipe random Wikipedia articles)

- **Primary:** `wikipedia casuale` (G; also `wikipedia pagina casuale` G, B; `wikipedia articolo casuale` G; `wikipedia
  voce casuale` G).
- **Secondary:** `wikipedia pagina casuale` (G, B); `wikipedia a caso` (G, B; `wikipedia pagina a caso`, `wikipedia
  articolo a caso`, `wikipedia voce a caso` G); `pagina casuale wikipedia` (G, B; `pagina a caso wikipedia` G, B); `app
  wikipedia` (G, B). Optional: `app curiosità` (G; B `app curiosità scientifiche`), `wikipedia curiosità` (G, B), `app per
  imparare cose nuove` (G; also `... ogni giorno`).
- **Not usable:**
  - `wikipedia casuale` + variabile (G): statistics. `wikipedia a caso` + caso garlasco, casoria, caso negreira (G):
    news noise ("caso" = case).
  - `wikipedia random` (G, B): English; `random forest`, `random page`, `random article generator`, `perchance` (B).
  - `articoli casuali wikipedia`, `app wikipedia casuale` (empty): no demand data, though S has "Esploratore Wiki Casuale".
  - `app wikipedia` (G, B): Android, APK, download, offline, deutsch: the official Wikipedia app is the target; usable as
    secondary only with the copy that WanderWiki is a different way to read.
  - `wikipedia app iphone` (G, one hit): same.
- **FAQ-style (from suggest):**
  - wikipedia pagina casuale (G, B) / wikipedia articolo casuale (G)
  - app wikipedia offline (G, B)
  - wikipedia app free / gratis (G, B)
  - app per imparare cose nuove ogni giorno (G)
  - wikipedia curiosità scientifiche (B)
  - wikipedia random article shortcut (G, B; English, "scorciatoia")
- **Competitors (S):** Wikipedia (the official app), WikiScroll: Scorri e Impara, Esploratore Wiki Casuale, Dailywiki, Wiki
  Races, Wiki Search, Kiwix, DailyArt, Storia, TED.
- **Notes:** Italian: "casuale" (formal) and "a caso" (colloquial) both appear on Google; "voce" is the Wikipedia term for
  an article ("voce di Wikipedia"), used in `wikipedia voce casuale` and `wikipedia voce a caso`. "Pagina" is the most
  common noun after the site name. The Wikipedia word is the head: Italians write "wikipedia casuale", not "casuale
  wikipedia". The page should name Wikipedia's own random-page button and say WanderWiki turns that into a swipeable deck.

## Xiangqiful (xiangqi / Chinese chess)

- **Primary:** `scacchi cinesi` (G, B, A, S). Only one clear Italian head term; G: `regole`, `online`, `pezzi`, `come si
  gioca`.
- **Secondary:** `xiangqi` (G, B, A; G: `xiangqi regole`, `xiangqi gioco`, `xiangqi online`); `scacchi cinesi regole` (G,
  B); `come si gioca a scacchi cinesi` (G; `scacchi cinesi come si gioca` G; `come si gioca agli scacchi cinesi` G);
  `scacchi cinesi online` (G, B). Optional: `scacchi cinesi pezzi` (G; also `pedine scacchi cinesi`), `xiangqi app` (G,
  B; English completions).
- **Not usable:**
  - `scacchi cinesi go`, `avorio`, `antichi`, `amazon`, `nome` (G): the board game Go, antiques, shopping.
  - `scacchi cinesi app`, `imparare scacchi cinesi`, `scacchi cinesi iphone`, `scacchi cinesi problemi`, `imparare
    xiangqi`: empty on G, B and A.
  - `xiangqi` alone (B): `xiangqi sg`, `xiangqian lao`, `xiangqi japan`: noise.
  - `xiangqi app` (G, B): `tiantian xiangqi app`, `club xiangqi app`, `play.xiangqi app`: English or competitor-name completions.
  - `come si gioca a scacchi` (B): generic chess.
  - `shogi vs xiangqi`, `shogi vs chinese chess` (G): English comparison fits the shogi page or comparison pages.
- **FAQ-style (from suggest):**
  - come si gioca a scacchi cinesi (G) / scacchi cinesi come si gioca (G) / come si gioca agli scacchi cinesi (G)
  - come si gioca a xiangqi (G)
  - scacchi cinesi regole (G, B) / xiangqi regole (G)
  - scacchi cinesi pezzi (G)
  - scacchi cinesi nome (G; the name, "xiangqi")
  - xiangqi pronunciation (G, English)
  - how to play xiangqi (B, English)
- **Competitors (S):** Scacchi cinesi V+, Xiangqi; PVXiangqi: Scacchi cinesi; Scacchi Cinesi Offline; Poqi: Scacchi Cinesi
  Xiangqi; Xiangqi: Scacchi Cinesi IA; Xiangqi - Scacchi Cinesi; Xiangqi Chinese Chess Online; Chinese Chess - Best XiangQi;
  Xiangqi Classic; Co Tuong Viet Nam; Chinese apps (天天象棋, 象棋 : 中国象棋). A hints for `scacchi cinesi`: "scacchi cinesi
  v+, xiangqi", "scacchi cinesi offline", "impara gli scacchi cinesi", "pvxiangqi: scacchi cinesi", "xiangqiful: scacchi
  cinesi".
- **Notes:** "Scacchi cinesi" is the only descriptor; "xiangqi" is used by players. Our own "Xiangqiful: Scacchi Cinesi"
  already shows in A and S. Do not use "Chinese chess" in Italian copy (only English completions). "Mate" and "problemi"
  have no query support; in body copy, "problemi di matto" or "puzzle di scacco matto" would be unsupported by this
  data (not returned), so use sparingly.

## Clippet (clipboard manager for iPhone and Mac, unreleased)

- **Primary:** `cronologia appunti iphone` (G, B; `cronologia appunti copiati iphone` G). In Italian the clipboard is
  "appunti" (cronologia = history).
- **Secondary:** `cronologia appunti mac` (G; `cronologia appunti copiati mac` G); `clipboard manager mac` (G, B; English,
  many completions); `gestore appunti` (B, A: "paste - gestore appunti", "clippo - gestore appunti"; G `gestore appunti
  windows`); `cronologia appunti` (G, B; Windows and Android heavy); `app appunti iphone` (G; ambiguous with note-taking,
  but G also gives `app io copiato negli appunti iphone`). Optional: `clipboard iphone` (G, B; `clipboard iphone history`
  G, B), `clipboard manager iphone` (G, as `clipboard manager for iphone`), `dove sono gli appunti iphone` (G, B).
- **Not usable:**
  - `appunti iphone` alone (G, B): mixes the clipboard and the Notes app ("appunti iphone dove li trovo", "prendere appunti
    con iphone", "appunti vocali").
  - `appunti mac` (G, B): university lecture notes ("appunti macroeconomia", "machine learning").
  - `cronologia appunti windows / android / samsung / tastiera` (G, B): other platforms.
  - `gestor(e) appunti mac`, `gestione appunti mac`: empty on G and A; B returns generic `gestione appunti`.
  - `incollare iphone` (G): pasting photos and stickers. `copia e incolla iphone mac` (B): Universal Clipboard.
  - `clipboard manager` + linux / arch / hyprland / gnome / ditto / extension / android (G): developer and other-OS
    noise; `clipboard manager mac` is the only clean part.
  - `clipboard manager` alone: same noise.
- **FAQ-style (from suggest):**
  - dove sono gli appunti iphone (G, B) / dove sono gli appunti su iphone 15 etc. (G; model variants, avoid)
  - appunti iphone dove li trovo (G) / dove trovo appunti su iphone (B)
  - copiato negli appunti iphone dove lo trovo (G) / link copiato negli appunti iphone dove lo trovo (G)
  - come vedere cronologia copia e incolla (B) / cronologia copia e incolla iphone (G)
  - cronologia appunti copiati iphone (G) / recuperare appunti copiati iphone (G)
  - come copiare e incollare su iphone (G) / come copiare e incollare da iphone a mac (G)
  - come attivare cronologia appunti (B; Windows)
  - clipboard iphone history (G, B)
- **Competitors (S):** Paste - Gestore Appunti, Pasted - Appunti e clipboard, Clippo - Gestore Appunti, Pop: Gestore Appunti,
  Notchet: Gestore appunti, ClipBox: Gestione Appunti, PasteCue: Gestione Appunti, Gestione appunti e cronologia, Cross
  Paste: Appunti, Clipboard Manager - PastePal, Clipbud - Clipboard Manager, Appunti - EasyPaste Clipboard, Paste It -
  Appunti Tastiera, Appunti Tastiera Copia Incolla, Clipboard Manager: Quick Paste.
- **Notes:** Italian vocabulary: "appunti" (clipboard; also "notes"), "cronologia appunti" (clipboard history),
  "gestore appunti" (App Store title category; B "gestione appunti"), "copia e incolla". Both "clipboard" (English) and
  "appunti" appear on Google. Searchers mostly want to find or see the iPhone clipboard (built-in feature), so the page
  must say iOS has no clipboard history and Clippet adds one; the strongest intent is "cronologia" on iPhone and Mac.
  Apple's Note app is called "Note" in Italian, so the "appunti" noise is lecture notes and the older "Appunti" label;
  avoid "appunti" without "cronologia" or "gestore".

---

## Summary table

| Page | Primary | Secondaries |
|---|---|---|
| mockly | screenshot app store | app store screenshot generator; mockup app store; app store screenshot maker |
| observa | hrv apple watch | variabilità della frequenza cardiaca; app sonno apple watch; hrv valori normali |
| pawza | libretto sanitario cane | libretto sanitario cane digitale; libretto sanitario gatto; app libretto sanitario cane |
| rightsplit | app per dividere il conto | app per dividere il conto al ristorante; dividere il conto alla romana; app per dividere le spese |
| shogiful | shogi | scacchi giapponesi; shogi regole; come si gioca a shogi |
| soon | conto alla rovescia iphone | widget conto alla rovescia; app conto alla rovescia; countdown iphone |
| tare | giochi rompicapo iphone | giochi senza pubblicità iphone; giochi offline iphone; giochi rilassanti iphone |
| taskful-day | app to do list | app per organizzare la giornata; app per pianificare la giornata; agenda giornaliera app |
| wanderwiki | wikipedia casuale | wikipedia pagina casuale; wikipedia a caso; app wikipedia |
| xiangqiful | scacchi cinesi | xiangqi; scacchi cinesi regole; come si gioca a scacchi cinesi |
| clippet | cronologia appunti iphone | cronologia appunti mac; clipboard manager mac; gestore appunti |

## Collisions and flags

- **Tare vs Millrace:** `giochi di logica iphone` / `giochi di logica` / `giochi puzzle iphone` belong to Millrace;
  Tare takes `giochi rompicapo iphone` (G, B). Check that the Millrace agent did not pick `rompicapo`.
- **Soon. vs Taskful Day:** none (countdown vs to-do). Soon.'s `app per contare i giorni` family overlaps nothing else.
- **Shogiful vs Xiangqiful:** both pages draw on the "scacchi + nationality" pattern (`scacchi giapponesi` vs `scacchi
  cinesi`); each page keeps its own head term. G offers `shogi vs xiangqi` for a comparison page, not for either app page.
- **Clippet vs Taskful Day / Notes apps:** `app appunti iphone` is ambiguous with note-taking apps; keep it optional.
- **RightSplit vs alternatives pages:** `splitwise alternativa` (G) belongs to the alternatives pages (the competitor
  agent), not to the RightSplit page. `app per dividere le spese` is expense-sharing intent (Splitwise, tricount); it fits
  RightSplit's Spaces feature but is secondary to the receipt-split headline.
- **Pawza vs official document:** `libretto sanitario cane` also covers the official paper booklet and the vet-issued
  document; the page must say Pawza keeps the digital record and does not replace the official one.
- **Observa:** write "(SDNN)" in the HRV explanation; `hrv rmssd valori normali` (G) is a suggest the page must not
  chase.
