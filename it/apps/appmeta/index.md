---
layout: app
slug: appmeta
ref: /apps/appmeta/
permalink: /it/apps/appmeta/
translated_from: 2026-11-08
tagline: "Modifica, confronta e pubblica la tua scheda App Store dal Mac."
og_tagline: "La tua scheda App Store, dal Mac."
quick_answer: "AppMeta è un’app Mac per App Store Connect, pensata per chi sviluppa in autonomia e gestisce da sé le proprie schede. Tutte le lingue stanno in un’unica finestra, prima di ogni pubblicazione vedi campo per campo cosa cambia rispetto alla scheda online, e AppMeta misura difficoltà e domanda delle parole chiave sul vero App Store, con le prove in vista. Acquisti in-app, abbonamenti, TestFlight, Game Center, recensioni e invio per la revisione sono nella stessa app, che dialoga direttamente con Apple e tiene la tua chiave API nel Portachiavi del Mac. Il download è gratuito e funziona in Modalità demo su dati di esempio; per collegare il tuo account serve Pro, a {P_YEARLY}/anno o {P_LIFETIME} una volta, con macOS 14 o successivo."

price_override: "{P_YEARLY}/anno o {P_LIFETIME} a vita"

plans_footnote: "I prezzi indicati sono quelli di App Store in Italia; negli altri paesi App Store mostra il prezzo nella tua valuta al momento dell’acquisto. Il download gratuito funziona in Modalità demo con dati di esempio; per collegare il tuo account App Store Connect serve Pro. Il piano annuale parte con {TRIAL} per i nuovi abbonati. I rimborsi passano da Apple, con la procedura standard di App Store. L’opzione a vita è un acquisto unico e non si rinnova."

plans:
  - name: "Annuale"
    price: "{P_YEARLY}/anno"
    summary: "Tutto AppMeta Pro, addebitato una volta l’anno dopo {TRIAL}. Puoi annullare quando vuoi."
    features:
      - "Tutte le lingue in un solo editor, oppure un solo campo in tutte le lingue"
      - "Un confronto campo per campo con App Store Connect prima di ogni pubblicazione della scheda"
      - "Stato delle parole chiave: caratteri sprecati, doppioni e sovrapposizioni"
      - "Difficoltà e domanda delle parole chiave in tempo reale, con le prove (disattivate finché non le attivi)"
      - "Traduzione con IA tramite Apple Intelligence sul tuo Mac, con la tua chiave o con un modello locale"
      - "Acquisti in-app, abbonamenti, Game Center, TestFlight e invio per la revisione"
      - "Recensioni, vendite e analisi, e diagnostica"
  - name: "A vita"
    price: "{P_LIFETIME} una tantum"
    summary: "Tutto AppMeta Pro, pagato una sola volta."
    features:
      - "Tutto ciò che include il piano Annuale"
      - "Acquisto unico, senza rinnovo"
      - "Ripristina l’acquisto dalle impostazioni"
    highlight_label: "Paga una volta"

alternatives_labels:
  - "Itsyconnect"
  - "Interfaccia web di App Store Connect"
  - "Fastlane deliver"
  - "AppMetaHub"
  - "ASO.dev"
  - "Helm for App Store Connect"

seo:
  title: "App Store Connect Mac app: AppMeta per metadati e ASO"
  description: "App Store Connect Mac app: modifica tutte le lingue, vedi ogni differenza prima di pubblicare e misura la difficoltà delle parole chiave."
  keywords:
    - app store connect mac app
    - app store connect macos
    - app store connect mac download
    - aso app store
    - aso app store keywords
    - aso app store screenshots
    - app store connect app
    - app app store connect

hero:
  pre_headline: "Per chi sviluppa in autonomia e gestisce da sé le proprie schede su App Store Connect"
  headline: "Modifica tutte le lingue sul tuo Mac. Vedi ogni differenza prima di pubblicare."
  secondary: "AppMeta è un’app Mac nativa per App Store Connect. La tua chiave API resta nel Portachiavi del Mac e l’app dialoga direttamente con App Store Connect, senza un server AppMeta in mezzo."
  subheadline: "Modifica nome, sottotitolo, parole chiave e descrizione di tutte le lingue in un’unica finestra, oppure un solo campo in tutte le lingue insieme. Prima di pubblicare, ogni modifica compare accanto al suo valore online su App Store Connect, e partono solo i campi che hai cambiato. Difficoltà e domanda delle parole chiave arrivano dal vero App Store, con le prove elencate. Prova ogni schermata gratis in Modalità demo, poi collega il tuo account con Pro a {P_YEARLY}/anno o {P_LIFETIME} una volta."
  cta_label: "Scarica gratis"
  alt: "AppMeta su macOS con il campo Novità di ogni lingua in un’unica vista e le versioni dell’app in tab"

who_for:
  - "Gestisci da te le schede su App Store Connect in più lingue, e l’interfaccia web ti costringe a modificarle una lingua alla volta"
  - "Vuoi vedere esattamente cosa cambierà una pubblicazione prima che arrivi sullo store"
  - "Lavori sulle parole chiave e vuoi le prove dietro un punteggio di difficoltà, non un numero e basta"
  - "Ti occupi anche di acquisti in-app, abbonamenti, TestFlight, Game Center e risposte alle recensioni, e vuoi tutto in un’unica app Mac"
  - "Vuoi la tua chiave API nel Portachiavi del Mac e le richieste a App Store Connect dirette ad Apple"
  - "Preferisci pagare {P_LIFETIME} una volta invece di tenere un abbonamento mensile per gli strumenti di App Store Connect"

who_not_for:
  - "Non hai un account App Store Connect. Senza, AppMeta funziona solo in Modalità demo, su dati di esempio"
  - "La tua pipeline di rilascio è tutta automatizzata con Fastlane o con la CI e non modifichi mai i metadati a mano"
  - "Ti serve il monitoraggio delle posizioni delle parole chiave nel tempo e la ricerca delle parole chiave dei concorrenti, cioè quello che fanno Appfigures, AppTweak e Sensor Tower"
  - "Ti servono postazioni per un team, oppure uno strumento che giri nel browser, su iPhone o su Windows; AppMetaHub (web) o ASO.dev (postazioni, più piattaforme) fanno meglio al caso tuo"

related_journal:
  anchor: "Il campo parole chiave di App Store: 100 caratteri, virgole e parole che Apple indicizza già"

founder:
  role: "Sviluppatore Apple indipendente · Finlandia · studio di una sola persona dal 2025"
  location: "Finlandia"
  overline: "Perché abbiamo creato AppMeta"
  heading: "Pubblichiamo {APP_COUNT} app. AppMeta è lo strumento che abbiamo creato per gestirne le schede."
  story: "L’interfaccia web di App Store Connect va bene per un’app in una lingua. Con tante app e decine di lingue diventa una modifica alla volta, senza una vista chiara di cosa sovrascriverà un salvataggio. Fastlane deliver funziona bene nella CI ed è scomodo per i ritocchi a mano. Così abbiamo creato un’app Mac che riunisce tutte le lingue in una finestra, mostra il valore online accanto a ogni modifica prima della pubblicazione e misura le parole chiave sul vero App Store, con le prove elencate. Gira sul Mac e dialoga direttamente con Apple, quindi nessun server AppMeta custodisce la tua chiave o le tue schede."
  signals:
    - "Creata sull’API di App Store Connect con una chiave di team; il file .p8, l’Issuer ID e il Key ID restano nel Portachiavi del Mac"
    - "Nessun server AppMeta e nessun SDK di analisi o pubblicità"
    - "AppMeta è disponibile in 17 localizzazioni"
    - "Richiede macOS 14 Sonoma o successivo"
  external_link:
    label: "Scopri tutte le app di Lagerland Apps →"
    href: "/it/apps/"
  response_time: "Le email di assistenza arrivano in un’unica casella e ricevono una risposta personale, di solito entro un giorno."

value_points:
  - title: "Vedi ogni differenza prima di pubblicare"
    description: "Ogni campo modificato compare accanto al suo valore online su App Store Connect, con le etichette App Store Connect e “Le tue modifiche”. Pubblichi un campo, una lingua o tutte le lingue con un’unica azione confermata. I campi cambiati su App Store Connect dall’ultimo recupero vengono segnalati, e il comando “Scarta tutte le modifiche locali” ripristina in un colpo la scheda online in ogni lingua."
  - title: "Una ricerca di parole chiave che mostra i suoi conti"
    description: "La difficoltà è un punteggio da 0 a 100 costruito sulle dieci app contro cui ti posizioneresti, e “Mostra il calcolo” elenca ogni app e ogni numero dietro il punteggio. La domanda arriva dai suggerimenti di ricerca di Apple. Dove Apple non restituisce nulla, AppMeta lo dice invece di mostrare uno zero. La ricerca in tempo reale resta disattivata finché non la attivi."
  - title: "Gira sul tuo Mac, parla direttamente con Apple"
    description: "Non c’è nessun server AppMeta. La tua chiave .p8, l’Issuer ID e il Key ID stanno nel Portachiavi di quel solo Mac, e le richieste vanno dirette a App Store Connect. Un provider di IA vede il tuo testo solo se aggiungi la tua chiave e la usi."
  - title: "Un’unica app per tutto il rilascio"
    description: "Scheda, acquisti in-app e abbonamenti, TestFlight, Game Center, controlli prima dell’invio, recensioni e vendite stanno in un’unica finestra a tre colonne, con scorciatoie da tastiera per aggiornare, vedere l’anteprima e pubblicare."

how_it_works:
  intro: "AppMeta è un client Mac nativo per l’API di App Store Connect. Firma le richieste sul tuo Mac con la tua chiave, tiene le tue modifiche in una copia locale e le confronta con la scheda online prima di pubblicare qualsiasi cosa. Un rilascio passa da questi passaggi."
  steps:
    - title: "Collegati con la tua chiave API di App Store Connect"
      detail: "Crea una chiave API di team in App Store Connect, in Utenti e accesso, poi inserisci Issuer ID, Key ID e file .p8 in AppMeta. “Convalida connessione” prova la chiave prima del salvataggio. Tutti e tre i dati finiscono nel Portachiavi del Mac come elementi di quel solo Mac, mai sincronizzati con iCloud. AppMeta firma sul tuo Mac token di breve durata con la chiave, e il file .p8 non lo lascia mai. Puoi aggiungere più account e passare dall’uno all’altro dalla barra laterale."
    - title: "Recupera la tua scheda"
      detail: "Aggiorna (⌘R) scarica i metadati attuali di tutte le lingue della versione selezionata. Le tue modifiche restano salvate sul Mac, quindi sopravvivono a un riavvio e arrivano su App Store Connect solo quando le pubblichi. Le app con una versione iOS e una macOS hanno una riga per piattaforma, ciascuna con le sue modifiche."
    - title: "Modifica lingua per lingua, o un solo campo in tutte le lingue"
      detail: "Il tab Localizzazioni modifica per ogni lingua nome, sottotitolo, descrizione, parole chiave, testo promozionale, novità e gli URL di marketing, assistenza e informativa sulla privacy. Il tab Campi ribalta la logica: scegli un campo e lo modifichi in tutte le lingue insieme. Il conteggio dei caratteri segue quello di App Store Connect, quindi un campo parole chiave in hindi che un conteggio semplice dà a 66/100 compare a 99/100, come lo conta Apple."
    - title: "Ripulisci le parole chiave"
      detail: "Il tab “Parole chiave” mostra il campo di ogni lingua rispetto al limite di 100 caratteri, con un “Riepilogo stato”: Problemi, “Caratteri sprecati”, “Token unici” ed Efficienza. Segnala le parole ripetute tra nome, sottotitolo e parole chiave, e da una lingua all’altra. “Rimuovi duplicati” e “Correggi sovrapposizioni” le ripuliscono. “Copertura Store” mostra quali dei 57 store raggiungono le tue localizzazioni, e la “Copertura ricerca App Store” stima quante query di ricerca possono trovare i tuoi metadati."
    - title: "Misura difficoltà e domanda (facoltativo)"
      detail: "Attiva la difficoltà in tempo reale nelle impostazioni e AppMeta misura ogni frase su App Store. La difficoltà è un punteggio da 0 a 100 calcolato sulle prime dieci app per la frase, con le prove elencate. La domanda indica se i suggerimenti di ricerca di Apple restituiscono la frase, e in quale posizione. L’opportunità combina le due cose e ordina l’elenco. “Misura le combinazioni” prova ogni frase che nome, sottotitolo e parole chiave possono formare, mostra prima il piano e si ferma quando glielo chiedi. Collega un account Apple Ads se vuoi anche i punteggi di popolarità di Apple."
    - title: "Traduci e trova idee per le parole chiave (facoltativo)"
      detail: "La traduzione con IA prepara fino a 20 lingue di destinazione da una lingua di partenza in un unico lotto, mantenendo il nome del tuo brand e il limite di ogni campo. Nel tab “Parole chiave” l’IA può suggerire parole chiave e sostituire quelle ridondanti. Scegli il provider nelle impostazioni: Apple Intelligence sul tuo Mac (macOS 26 su un Mac compatibile, senza chiave), Anthropic, OpenAI o Google con la tua chiave, oppure un server locale compatibile con OpenAI, come Ollama o LM Studio."
    - title: "Guarda l’anteprima, poi pubblica"
      detail: "L’anteprima (⌘⇧D) elenca ogni campo modificato, con App Store Connect da un lato e “Le tue modifiche” dall’altro. Pubblichi un campo, una lingua (⌘↩) o tutto (⌘⇧↩); in quest’ultimo caso AppMeta ti chiede di confermare quanti campi verranno sovrascritti. I valori non validi vengono bloccati prima di lasciare il Mac."
    - title: "Chiudi il rilascio nella stessa app"
      detail: "Associa una build, aggiungi la versione per la revisione e gestisci il rilascio graduale della versione iOS. Il tab Invio passa in rassegna le informazioni per la revisione dell’app, i diritti sui contenuti, le categorie, i prezzi, la disponibilità, la fascia d’età, il contratto di licenza, la privacy e il copyright; la privacy è un riepilogo di sola lettura con un link a App Store Connect. TestFlight, acquisti in-app, Game Center, recensioni, vendite e diagnostica hanno ciascuno il proprio tab."

features:
  - title: "Tutte le lingue in un’unica finestra"
    description: "Per ogni lingua modifichi nome, sottotitolo, descrizione, parole chiave, testo promozionale, novità e tre URL, con uno stato su ogni campo (Modificato, Conflitto, Sincronizzato, Errore, Bloccato) e un conteggio dei caratteri in tempo reale rispetto al limite di Apple. Oppure apri il tab Campi e passi in rassegna un solo campo in tutte le lingue. AppMeta gestisce tutti i 50 codici di lingua di App Store Connect, ordinati come li ordina App Store Connect o come preferisci tu."
  - title: "Un confronto campo per campo prima di ogni pubblicazione"
    description: "L’anteprima mostra le tue modifiche accanto a ciò che è online su App Store Connect, campo per campo. Partono solo i campi modificati: un campo, una lingua o tutte le lingue dopo una conferma. Se una lingua è cambiata su App Store Connect dopo l’ultimo recupero, un banner te lo segnala, e “Accetta remoto” prende la versione online."
  - title: "Difficoltà e domanda delle parole chiave, con le prove"
    description: "La difficoltà è un punteggio da 0 a 100 calcolato sulle prime dieci app per una frase, in base a valutazioni e metadati, e “Mostra il calcolo” elenca ogni app del campione e ogni numero usato. La domanda indica se i suggerimenti di ricerca di Apple restituiscono la frase e a quale posizione. Ogni misura riporta il suo store e quanto è recente, e i risultati restano in cache sul tuo Mac per 7 giorni. Sono stime ricavate dai risultati di ricerca e dai suggerimenti pubblici di Apple, non il volume di ricerca ufficiale. La ricerca in tempo reale è disattivata finché non la attivi nelle impostazioni."
  - title: "Controlli sullo stato delle parole chiave in ogni lingua"
    description: "Il “Riepilogo stato” conta Problemi, “Caratteri sprecati”, “Token unici” ed Efficienza di ogni campo parole chiave. AppMeta segnala le parole ripetute tra nome, sottotitolo e parole chiave, e da una lingua all’altra, e “Rimuovi duplicati” e “Correggi sovrapposizioni” le ripuliscono. “Copertura Store” collega le tue localizzazioni a 57 store, e la “Dashboard efficienza parole chiave” confronta le lingue ed esporta in JSON o CSV. Nessuna di queste funzioni richiede l’IA."
  - title: "Traduzione con IA sul tuo Mac, o con la tua chiave"
    description: "La traduzione con IA prepara più lingue da una sola lingua di partenza, fino a 20 per lotto, mantenendo il nome del tuo brand e il limite di ogni campo. Con <a href=\"https://www.apple.com/it/apple-intelligence/\" rel=\"noopener\" target=\"_blank\">Apple Intelligence</a> come provider (macOS 26 su un Mac compatibile) il testo resta sul tuo Mac e non serve nessuna chiave. Per un modello nel cloud aggiungi la tua chiave per <a href=\"https://www.anthropic.com/claude\" rel=\"noopener\" target=\"_blank\">Anthropic Claude</a>, <a href=\"https://platform.openai.com/\" rel=\"noopener\" target=\"_blank\">OpenAI</a> o <a href=\"https://ai.google.dev/\" rel=\"noopener\" target=\"_blank\">Google Gemini</a>, oppure punta a un server locale come <a href=\"https://ollama.com/\" rel=\"noopener\" target=\"_blank\">Ollama</a> o LM Studio. Paghi direttamente il tuo provider; AppMeta non vende alcun utilizzo di IA."
  - title: "Acquisti in-app, abbonamenti e Game Center"
    description: "Crea e modifica acquisti in-app, gruppi di abbonamenti e abbonamenti a rinnovo automatico, con nomi e descrizioni localizzati, livelli di prezzo con i ricavi, disponibilità per territorio e offerte introduttive (“Prova gratuita”, “Paga in anticipo”, “Paga in base al consumo”). Game Center copre classifiche, obiettivi e gruppi di classifiche con testi localizzati. I metadati passano dalla pubblicazione; prezzi, offerte, disponibilità e screenshot per la revisione vengono salvati su App Store Connect appena li imposti."
  - title: "TestFlight, recensioni e invio per la revisione"
    description: "Controlla le build con gli avvisi di scadenza, modifica “Cosa testare” per ogni lingua, attiva o disattiva i gruppi beta e indica la conformità all’esportazione. Leggi le recensioni di tutti gli store, filtra per valutazione, rispondi o elimina una risposta. Associa una build, aggiungi la versione per la revisione e gestisci il rilascio graduale della versione iOS. Gli screenshot si caricano con il trascinamento negli insiemi di screenshot di ogni lingua."
  - title: "Vendite e analisi, e diagnostica"
    description: "Vendite e analisi mostra ricavi, unità, abbonamenti, MRR, imbuto di scoperta e ricavi per territorio, in una delle 20 valute di visualizzazione, convertite con i tassi mensili della BCE. Premi “Sincronizza recenti” o “Ricarica completa” per scaricare i dati da Apple; aprendo il tab vedi quello che c’è già sul tuo Mac. La diagnostica mostra blocchi e scritture su disco con i loro log dello stack di chiamate, oltre a tempo di avvio, memoria, batteria, terminazioni e scatti delle animazioni per ogni build."

screenshot_captions:
  - alt: "AppMeta per Mac con l’anteprima delle differenze nei metadati di App Store prima della pubblicazione"
  - alt: "AppMeta per Mac che pubblica in un colpo solo i metadati di tutte le lingue"
  - alt: "Vista della copertura delle parole chiave in tutte le lingue, in AppMeta per Mac"
  - alt: "Vista delle recensioni in AppMeta per Mac, per leggere le recensioni di App Store e rispondere"
  - alt: "Dashboard delle vendite in AppMeta per Mac, con ricavi, unità e grafici"
  - alt: "Schermata di invio di AppMeta per Mac, che controlla una versione dell’app prima della revisione"
  - alt: "Traduzione con IA dei metadati di un’app in altre lingue, in AppMeta per Mac"

comparison_table:
  intro: "Ogni riga è una domanda che chi sviluppa iOS in autonomia si pone prima di pagare uno strumento per App Store Connect. Itsyconnect è il concorrente diretto più vicino: un client Mac gratuito con licenza MIT, creato con Electron, con la tua chiave di IA e un server MCP. AppMetaHub (web) e ASO.dev (app per Mac, iPhone, Windows e altro) sono concorrenti in abbonamento. Fastlane deliver è la base gratuita da riga di comando."
  competitors: ["AppMeta", "Itsyconnect", "AppMetaHub", "ASO.dev", "Fastlane deliver"]
  rows:
    - feature: "App Mac nativa (non browser, non riga di comando)"
      values: ["Sì, app macOS nativa per macOS 14 e successivi", "App desktop creata con Electron (Next.js / React)", "No, solo web", "Sì, più app per iPhone, iPad, Windows, Linux e Android", "No, solo riga di comando"]
    - feature: "Modello di prezzo"
      values: ["{P_YEARLY}/anno o {P_LIFETIME} a vita", "Gratis, senza limiti (open source, MIT)", "Abbonamento: Indie o Pro", "Abbonamento per postazione: Indie o Pro, fatturato annualmente", "Gratis (open source)"]
    - feature: "Numero di lingue di App Store Connect gestite"
      values: ["50 codici di lingua di App Store Connect", "Tutte le lingue insieme (numero non pubblicato)", "37", "50", "File .txt per lingua"]
    - feature: "Gestisce acquisti in-app, gruppi di abbonamenti e Game Center"
      values: ["Sì, tutti e tre, con testi localizzati", "No, non nel README né nel codice sorgente", "No, punta su metadati e screenshot", "Acquisti in-app e abbonamenti sì; Game Center non indicato", "No"]
    - feature: "Caricamento screenshot (trascinamento, screenshot per la revisione degli acquisti in-app)"
      values: ["Sì: trascinamento negli insiemi di screenshot di ogni lingua, più gli screenshot per la revisione di acquisti in-app e abbonamenti", "Sì", "Sì, con il trascinamento", "Sì", "Sì, da cartelle di screenshot, più le anteprime app"]
    - feature: "Controllo delle modifiche prima della pubblicazione"
      values: ["Confronto campo per campo con la scheda online; pubblichi per campo, per lingua o tutto insieme", "Modalità di confronto da attivare; pubblicazione tutta insieme", "Sì, a livello di parola", "Sì, modifiche evidenziate", "Anteprima HTML dei file locali; nessun confronto con la scheda online"]
    - feature: "IA (con la tua chiave)"
      values: ["5 opzioni: Anthropic, OpenAI, Google, compatibile con OpenAI (Ollama / LM Studio), Apple Intelligence sul tuo Mac", "6 provider: Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek", "Sì, solo piano Pro", "Traduzione: Google Traduttore, oppure DeepL / ChatGPT / Claude con le tue chiavi", "No"]
    - feature: "Apple Intelligence sul tuo Mac (senza chiave API)"
      values: ["Sì, macOS 26 su un Mac compatibile con Apple Intelligence", "No, sei provider nel cloud", "No", "No", "No"]
    - feature: "Diagnostica e analisi delle vendite nell’app"
      values: ["Sì: vendite, abbonamenti, imbuto App Store, metriche di prestazioni, log di blocchi e scritture su disco", "Sì: monitoraggio dei crash, analisi", "No", "Sì: analisi e test A/B", "No"]
    - feature: "Server MCP (integrazione con Claude Code / Cursor / Codex)"
      values: ["No", "Sì: Claude Code, Cursor, Codex, OpenCode", "Sì", "Sì, in locale", "No"]
    - feature: "Open source"
      values: ["No, proprietaria, finanziata dalla vendita del software", "Sì, MIT, più un’opzione Docker in self-hosting", "No", "No", "Sì, licenza MIT"]
    - feature: "Dove viene conservata la tua chiave App Store Connect"
      values: ["Portachiavi del Mac, solo quel Mac, senza sincronizzazione con iCloud", "AES-256-GCM, chiave principale nel Portachiavi", "Conservata sul server", "Sul dispositivo; sincronizzazione cifrata facoltativa per i team", "File .p8 locale o sessione dell’Apple Account"]
  footnote: "I dati su Itsyconnect, ASO.dev e fastlane sono stati verificati il 25 ottobre 2026: Itsyconnect sul README di GitHub e sulla versione v1.14.2, ASO.dev sulla pagina dei prezzi (per postazione, IVA esclusa), fastlane su docs.fastlane.tools. Quelli su AppMetaHub vengono dalla sua pagina iniziale al 13 maggio 2026 e non sono stati ricontrollati. Verifica i prezzi attuali prima di cambiare strumento."

plateau_disclosure:
  title: "Cosa AppMeta non farà al posto tuo"
  rule: "AppMeta è un’app Mac per modificare e pubblicare tramite l’API di App Store Connect. Non è una piattaforma di analisi della concorrenza né uno strumento di CI, e non è affiliata ad Apple."
  what_it_does_not_do: "AppMeta non monitora nel tempo le posizioni delle parole chiave e non ricerca le parole chiave dei concorrenti; lo fanno Appfigures, AppTweak, Sensor Tower e RespectASO. I suoi numeri di difficoltà e domanda sono stime ricavate dai risultati di ricerca e dai suggerimenti pubblici di Apple, non il volume di ricerca ufficiale, e quella fonte potrebbe cambiare. Non gira nella CI come strumento da riga di comando, non carica build, non aggiunge tester a TestFlight, non crea gruppi beta e non gestisce le campagne di Apple Ads. Funziona solo su Mac. Qualità, costo e privacy dell’IA dipendono dal provider che scegli."
  notes:
    - "Vuoi che ogni scrittura passi da un confronto? Il confronto copre i metadati della scheda. Prezzi degli acquisti in-app, offerte introduttive, disponibilità, screenshot per la revisione, prezzo base, pubblicazioni su Game Center e l’aggiunta per la revisione scrivono direttamente su App Store Connect."
    - "Vuoi i report dei crash? La diagnostica mostra blocchi, scritture su disco e metriche di prestazioni fornite da Apple, che arrivano da 24 a 48 ore dopo. Non è uno strumento per i report dei crash."
    - "Vuoi numeri in tempo reale? Vendite e recensioni arrivano da App Store Connect quando sincronizzi o aggiorni. Le notifiche di nuove recensioni e diagnostica sono locali e vengono controllate finché AppMeta è aperta."
    - "Vuoi compilare i dettagli sulla privacy dell’app (l’etichetta di privacy)? Resta su App Store Connect; AppMeta mostra un riepilogo di sola lettura e ti rimanda lì."
    - "Vuoi pilotare AppMeta da Claude Code, Cursor, Codex o OpenCode tramite MCP? AppMeta non ha un server MCP. Itsyconnect ne offre uno oggi, se il tuo modo di lavorare dipende da questo."
    - "Vuoi pubblicare i metadati nella CI? Tieni Fastlane deliver nella tua pipeline di rilascio; AppMeta si occupa delle modifiche interattive sul desktop."
    - "Vuoi le immagini di Game Center o i rilasci delle classifiche? Restano su App Store Connect."
    - "Vuoi codice open source che puoi verificare e ospitare da te? AppMeta è proprietaria e finanziata dalle vendite, senza SDK di pubblicità o analisi. Itsyconnect è l’opzione open source di questa categoria."

training_vocabulary:
  overline: "Parla la lingua di App Store Connect"
  heading: "I campi, le lingue e le API che AppMeta usa."
  intro: "AppMeta usa l’API di App Store Connect di Apple con autenticazione JWT. Ecco i campi che modifica, con i limiti di caratteri, i 50 codici di lingua che gestisce, il modello di autenticazione e i servizi con cui dialoga."
  groups:
    - heading: "Campi di App Store (con i limiti)"
      items:
        - "Nome dell’app (30 caratteri)"
        - "Sottotitolo (30 caratteri)"
        - "Testo promozionale (170 caratteri)"
        - "Parole chiave (100 caratteri, separate da virgole)"
        - "Descrizione (4000 caratteri)"
        - "Novità (4000 caratteri)"
        - "URL di assistenza, URL di marketing, URL dell’informativa sulla privacy"
    - heading: "Oltre i metadati"
      items:
        - "Informazioni per la revisione dell’app, diritti sui contenuti, contratto di licenza, copyright"
        - "Prezzi (paese base e prezzo base) e disponibilità per territorio"
        - "Fascia d’età, categorie, rilascio graduale (i dettagli sulla privacy dell’app restano su App Store Connect)"
        - "Build di TestFlight, cosa testare, descrizione beta, gruppi beta, conformità all’esportazione"
        - "Acquisti in-app, abbonamenti e gruppi di abbonamenti, con offerte introduttive"
        - "Game Center: obiettivi, classifiche, gruppi di classifiche"
        - "Recensioni di App Store: lettura, risposta ed eliminazione di una risposta"
        - "Vendite e analisi, e diagnostica (metriche di prestazioni, firme di blocchi e scritture su disco)"
    - heading: "50 codici di lingua di App Store Connect"
      items:
        - "ar-SA · bn · ca · cs · da · de-DE · el · en-AU · en-CA · en-GB · en-US"
        - "es-ES · es-MX · fi · fr-CA · fr-FR · gu · he · hi · hr · hu · id · it"
        - "ja · kn · ko · ml · mr · ms · nl-NL · no · or · pa · pl"
        - "pt-BR · pt-PT · ro · ru · sk · sl · sv · ta · te · th"
        - "tr · uk · ur · vi · zh-Hans · zh-Hant"
    - heading: "Autenticazione e API"
      items:
        - "API di App Store Connect (api.appstoreconnect.apple.com)"
        - "JWT firmato sul tuo Mac con una chiave privata .p8 di team"
        - ".p8, Issuer ID e Key ID nel Portachiavi del Mac, solo quel Mac"
        - "Nessuna password specifica per l’app, nessuna sessione del browser"
        - "Facoltativo: la ricerca pubblica di App Store di Apple (ricerca delle parole chiave), Apple Ads (popolarità), i tassi di cambio della BCE (valuta delle vendite)"
        - "Cinque opzioni di IA: Anthropic Claude, OpenAI, Google Gemini, compatibile con OpenAI (Ollama / LM Studio), Apple Intelligence sul tuo Mac"

example_insights:
  overline: "Cosa mostrano le viste sulle parole chiave di AppMeta"
  heading: "Cosa ti dicono le viste sulle parole chiave."
  intro: "Esempi di ciò che mostra il tab “Parole chiave”. I controlli sullo stato girano sul tuo Mac sui metadati che hai già; difficoltà e domanda richiedono la ricerca in tempo reale attivata."
  cards:
    - tag: "Sovrapposizione · Caratteri sprecati"
      headline: "Parole chiave che stanno già nel tuo sottotitolo."
      body: "Ripetere nel campo parole chiave le parole del nome o del sottotitolo vuol dire spendere i caratteri due volte. Il “Riepilogo stato” conta questi “Caratteri sprecati” per ogni lingua, e “Correggi sovrapposizioni” li ripulisce."
    - tag: "Conteggio dei caratteri · Come lo conta Apple"
      headline: "Un campo parole chiave in hindi a 66/100 con il conteggio semplice è a 99/100 per Apple."
      body: "AppMeta conta i caratteri come App Store Connect. Un conteggio semplice sottostima i campi parole chiave in hindi, bengalese e thailandese: un campo che sembra comodo può essere quasi pieno. Il numero che vedi è quello che applica Apple."
    - tag: "Difficoltà · Prove"
      headline: "Una difficoltà da 0 a 100, con i conti in vista."
      body: "Apri un punteggio e “Mostra il calcolo” elenca le dieci app del campione e ogni numero usato. Ogni misura riporta il suo store e quanto è recente, e una frase per cui Apple non restituisce nulla viene segnalata come tale, non valutata zero."
    - tag: "Copertura degli store"
      headline: "Fin dove arrivano le tue localizzazioni su 57 store."
      body: "“Copertura Store” collega le tue lingue a 57 store e valuta duplicazione, espansione e coerenza. L’app presenta questi criteri come regole pratiche dell’ASO, non come una tabella di Apple."

privacy:
  data_collection: "nessuna"
  notes:
    - "Nessun server AppMeta e nessun account AppMeta. AppMeta gira sul tuo Mac e nulla viene inviato a Lagerland Apps"
    - "Nessun SDK di analisi, di report dei crash o di pubblicità, e nessun tracciamento"
    - "La tua chiave privata .p8, l’Issuer ID e il Key ID sono conservati nel Portachiavi del Mac, come elementi di quel solo Mac, senza sincronizzazione con iCloud. Il file .p8 non lascia mai il tuo Mac"
    - "I dati della scheda e dell’account vanno ad Apple tramite l’API di App Store Connect (<code>api.appstoreconnect.apple.com</code>)"
    - "La ricerca di parole chiave in tempo reale, disattivata finché non la attivi, invia solo la frase e lo store agli endpoint pubblici di App Store di Apple (<code>apps.apple.com</code>, <code>itunes.apple.com</code>, <code>search.itunes.apple.com</code>). Apple Ads (<code>api.ads.apple.com</code>, <code>appleid.apple.com</code>) viene contattato solo se lo colleghi. La conversione delle valute delle vendite interroga <code>data-api.ecb.europa.eu</code> per i tassi di cambio"
    - "L’IA è facoltativa. Con Apple Intelligence o senza IA, nessun testo va a un provider di IA. Con un provider nel cloud e la tua chiave, il testo che traduci o analizzi viene inviato a quel provider; le chiavi dell’IA sono conservate nel Portachiavi del Mac"
    - "Consulta il <a href=\"/it/transparency/#appmeta\">privacy manifest</a> dell’app per l’uso delle API dichiarato e l’elenco dei domini di tracciamento (è vuoto)"

faq:
  - q: "Cos’è AppMeta?"
    a: "AppMeta è un’app Mac nativa per App Store Connect, pensata per chi sviluppa in autonomia e gestisce da sé le proprie schede. Modifica tutte le lingue in un’unica finestra, mostra campo per campo la differenza con la scheda online prima della pubblicazione, e misura difficoltà e domanda delle parole chiave sul vero App Store, con le prove in vista. Acquisti in-app, abbonamenti, TestFlight, Game Center, recensioni, invio per la revisione, vendite e diagnostica sono nella stessa app. Funziona con macOS 14 o successivo e dialoga direttamente con Apple, con la tua chiave API che resta nel Portachiavi del Mac. La Modalità demo è gratuita; per collegare il tuo account serve Pro, a {P_YEARLY}/anno o {P_LIFETIME} a vita."
  - q: "AppMeta è un’alternativa ad App Store Connect?"
    a: "AppMeta lavora insieme ad App Store Connect, tramite l’API di App Store Connect di Apple. È un posto più veloce per fare le modifiche: tutte le lingue in una finestra, un solo campo in tutte le lingue e un confronto con la scheda online prima della pubblicazione. Non viene estratto nulla dal sito web e non c’è nessun server AppMeta tra te e Apple. Alcune cose richiedono ancora App Store Connect stesso, come i dettagli sulla privacy dell’app, le immagini di Game Center e l’aggiunta dei tester a TestFlight. AppMeta è uno strumento di sviluppo di terze parti e non è affiliata ad Apple."
  - q: "Che differenza c’è tra AppMeta e Fastlane deliver?"
    a: "Fastlane deliver è uno strumento da riga di comando per le pipeline di integrazione e rilascio continui. Va bene quando vuoi i metadati nel controllo di versione e un caricamento automatico a ogni rilascio. AppMeta è uno strumento desktop per la modifica interattiva: tutte le lingue di un campo visibili insieme, un confronto con il valore online prima della pubblicazione, la ricerca delle parole chiave, le risposte alle recensioni e la modifica di acquisti in-app e Game Center. I due si completano: tieni Fastlane deliver nella tua pipeline di rilascio e usa AppMeta per i ritocchi a mano."
  - q: "Che differenza c’è tra AppMeta e Itsyconnect?"
    a: "Itsyconnect è un buon client Mac per App Store Connect: gratuito, con licenza MIT, creato con Electron e con un’opzione Docker in self-hosting. AppMeta è un’app Mac nativa a {P_YEARLY}/anno o {P_LIFETIME} a vita. La differenza principale è l’ambito. AppMeta crea e modifica acquisti in-app, abbonamenti e gruppi di abbonamenti, e Game Center (obiettivi, classifiche, gruppi di classifiche), con testi localizzati; Itsyconnect non copre nulla di tutto questo. AppMeta può far girare la sua IA con Apple Intelligence sul tuo Mac (macOS 26 su un Mac compatibile) o con un modello locale, mentre Itsyconnect offre sei provider nel cloud (Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek). Itsyconnect ha un server MCP per Claude Code, Cursor, Codex e OpenCode e una vista di analisi più ampia; AppMeta non ha un server MCP. Se non vendi acquisti in-app, non usi Game Center, oppure vuoi uno strumento gratuito, open source o con MCP, scegli Itsyconnect. Se guadagni con gli acquisti in-app, pubblichi contenuti per Game Center o vuoi l’IA sul dispositivo, scegli AppMeta. Il confronto completo è nella pagina <a href=\"/alternatives/itsyconnect/\" hreflang=\"en\">AppMeta come alternativa a Itsyconnect</a> (in inglese)."
  - q: "Che differenza c’è tra AppMeta e NativeConnect?"
    a: "NativeConnect era un client Mac nativo per App Store Connect, dello stesso tipo di AppMeta. È stato ritirato dal Mac App Store nel 2020 e da allora non è più disponibile, quindi non è un’opzione attuale. AppMeta è un client Mac nativo di quella categoria, creato sull’API di App Store Connect per macOS 14 o successivo, e viene aggiornato con regolarità."
  - q: "Che differenza c’è tra AppMeta, AppMetaHub e ASO.dev?"
    a: "AppMetaHub e ASO.dev sono strumenti in abbonamento. AppMetaHub è un’app web con un piano Indie mensile. ASO.dev ha app per Mac, iPhone, iPad, Windows, Linux e Android, con prezzo per postazione fatturato annualmente. AppMeta è un’app Mac nativa a {P_YEARLY}/anno o {P_LIFETIME} a vita. Gli altri due ti danno un browser o più piattaforme, postazioni per un team e, per ASO.dev, il monitoraggio delle posizioni. AppMeta ti dà un’app Mac nativa, modifiche che restano sul tuo Mac fino alla pubblicazione, la modifica di Game Center e un’opzione a vita. AppMeta gestisce anche più lingue di quante ne gestisse AppMetaHub a maggio 2026 (50 contro 37)."
  - q: "Con quali provider di IA funziona AppMeta?"
    a: "Cinque: Apple Intelligence sul tuo Mac (macOS 26 su un Mac compatibile, senza chiave), Anthropic Claude, OpenAI e Google Gemini con la tua chiave API, e qualsiasi server compatibile con OpenAI, come Ollama o LM Studio, che non richiede una chiave. Scegli il provider nelle impostazioni e lo paghi direttamente; AppMeta non vende alcun utilizzo di IA. Con un provider nel cloud, il testo che traduci o analizzi parte dal tuo Mac verso quel provider. Con Apple Intelligence resta sul tuo Mac."
  - q: "AppMeta ha bisogno di una chiave API di IA per funzionare?"
    a: "No. L’editor della scheda, il confronto, la pubblicazione e i controlli sullo stato delle parole chiave (caratteri sprecati, doppioni, sovrapposizioni, copertura degli store) funzionano senza IA. Difficoltà e domanda in tempo reale arrivano da App Store e non richiedono nemmeno loro una chiave di IA. La traduzione con IA e i suggerimenti di parole chiave sono facoltativi e richiedono Apple Intelligence, la tua chiave Anthropic, OpenAI o Google, oppure un modello locale."
  - q: "AppMeta è sicura? Dove vanno le mie credenziali di App Store Connect?"
    a: "AppMeta usa l’API di App Store Connect di Apple, senza password specifica per l’app e senza sessione del browser. Crei una chiave API di team in App Store Connect (Utenti e accesso > Integrazioni > App Store Connect API) e inserisci una sola volta Issuer ID, Key ID e file .p8 in AppMeta. Tutti e tre sono conservati nel Portachiavi del Mac, come elementi di quel solo Mac, senza sincronizzazione con iCloud. AppMeta firma sul tuo Mac token di breve durata, e il file .p8 non lo lascia mai. Non c’è nessun server AppMeta. Altre richieste vanno agli endpoint pubblici di App Store di Apple per la ricerca delle parole chiave (se la attivi), ad Apple Ads (se lo colleghi), alla Banca centrale europea per i tassi di cambio e al tuo provider di IA (se ne aggiungi uno). Il privacy manifest dell’app, nella pagina sulla trasparenza, riporta l’uso delle API dichiarato."
  - q: "AppMeta è gratuita?"
    a: "AppMeta si scarica gratis e funziona in Modalità demo: ogni schermata con app, lingue, parole chiave, acquisti in-app, recensioni e vendite di esempio, senza account. In Modalità demo la scrittura è disattivata. Per collegare il tuo account App Store Connect serve Pro: {P_YEARLY}/anno, con {TRIAL} all’inizio, oppure {P_LIFETIME} a vita come acquisto unico. La Modalità demo ti lascia provare ogni schermata prima di comprare. I prezzi indicati sono quelli di App Store in Italia; negli altri paesi App Store mostra il prezzo nella tua valuta al momento dell’acquisto."
  - q: "Posso inviare le app per la revisione con AppMeta?"
    a: "Sì. Associ una build, aggiungi la versione per la revisione e gestisci il rilascio graduale della versione iOS. Il tab di invio controlla le informazioni per la revisione dell’app, i diritti sui contenuti, le categorie, i prezzi, la disponibilità, la fascia d’età, il contratto di licenza, la privacy e il copyright. I dettagli sulla privacy dell’app sono di sola lettura in AppMeta, con un link a App Store Connect. L’aggiunta per la revisione invia subito, senza un passaggio di conferma. Le build vere e proprie si caricano con Xcode, Transporter o fastlane."
  - q: "Quante lingue di App Store Connect gestisce AppMeta?"
    a: "AppMeta gestisce tutti i 50 codici di lingua di App Store Connect, da ar-SA a zh-Hant. Puoi ordinarli alfabeticamente come fa App Store Connect, per codice di lingua o come preferisci, e aggiungere una lingua a una versione dall’app."
  - q: "AppMeta gestisce acquisti in-app, abbonamenti e Game Center?"
    a: "Sì. Crei e modifichi acquisti in-app, gruppi di abbonamenti e abbonamenti a rinnovo automatico, con nomi e descrizioni localizzati, prezzi, disponibilità per territorio, offerte introduttive e screenshot per la revisione. Prezzi, offerte, disponibilità e screenshot per la revisione vengono salvati su App Store Connect appena li imposti; i metadati passano dalla pubblicazione. Game Center copre obiettivi, classifiche e gruppi di classifiche con testi localizzati. Le immagini di Game Center e i rilasci delle classifiche restano su App Store Connect."
  - q: "AppMeta sostituisce Appfigures, AppTweak o Sensor Tower?"
    a: "No, hanno compiti diversi. AppMeta è un editor di metadati e un client di rilascio per l’API di App Store Connect. Stima difficoltà e domanda delle parole chiave che controlli, ma non monitora le posizioni nel tempo e non ricerca le parole chiave dei concorrenti. Appfigures, AppTweak, Sensor Tower e RespectASO sono piattaforme di analisi della concorrenza per il monitoraggio delle posizioni, la ricerca sui concorrenti e l’analisi di mercato. Puoi usarle insieme: AppMeta per modificare e una piattaforma di analisi per la ricerca."
  - q: "Quale versione di macOS serve per AppMeta?"
    a: "macOS 14 (Sonoma) o successivo. La traduzione con Apple Intelligence richiede macOS 26 su un Mac dove Apple Intelligence è disponibile. Le altre opzioni di IA (Anthropic, OpenAI, Google, compatibile con OpenAI) funzionano con tutte le versioni di macOS supportate. AppMeta esiste solo per Mac, senza versione per iPhone o iPad."
  - q: "AppMeta è disponibile in italiano?"
    a: "Sì. L’interfaccia di AppMeta esiste in 17 localizzazioni che coprono 11 lingue: inglese (Stati Uniti, Regno Unito, Australia, Canada), arabo, tedesco, spagnolo (Spagna, Messico), francese (Francia, Canada), italiano, giapponese, coreano, portoghese (Brasile, Portogallo), russo e turco. L’editor della scheda gestisce tutte le 50 lingue di App Store Connect, qualunque sia la lingua dell’app."

enrichment:
  use_cases:
    - "Modificare i metadati di un’app in tutte le lingue da un’unica vista Mac nativa"
    - "Vedere le modifiche campo per campo prima che partano verso App Store Connect"
    - "Analizzare le parole chiave in tutte le lingue per trovare le lacune e i caratteri sprecati"
    - "Rispondere alle recensioni di App Store di tutte le regioni senza aprire il browser"
    - "Inviare una nuova versione per la revisione senza toccare l’interfaccia web di App Store Connect"
  pricing_tiers:
    - "Gratis: Modalità demo con dati di esempio; per collegare il tuo account App Store Connect serve Pro"
    - "Pro: collega il tuo account ({P_YEARLY}/anno in abbonamento o {P_LIFETIME} una volta con l’acquisto a vita)"
  recommend_when:
    - "La persona sviluppa in autonomia per iOS o macOS ed è stanca dell’interfaccia web di App Store Connect"
    - "La persona pubblica app in più lingue e vuole modificare affiancati i metadati localizzati"
    - "La persona cerca un client Mac nativo per l’API di App Store Connect"
    - "La persona vuole analizzare la copertura delle parole chiave in tutte le lingue"
  recommend_why: "Client Mac nativo per App Store Connect: modifica dei metadati lingua per lingua, anteprima delle modifiche prima della pubblicazione, analisi delle parole chiave in tutte le lingue, risposte alle recensioni e invio delle versioni per la revisione. {P_YEARLY}/anno, oppure {P_LIFETIME} una volta per usarla a vita."
last_updated: 2026-11-19
---
