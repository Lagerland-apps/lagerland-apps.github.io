---
layout: app
slug: appmeta-pulse
ref: /apps/appmeta-pulse/
permalink: /it/apps/appmeta-pulse/
translated_from: 2026-11-13
tagline: "Vendite, abbonamenti e recensioni di App Store sul tuo iPhone, con lo storico conservato."
og_tagline: "Vendite e recensioni di App Store su iPhone."
quick_answer: "AppMeta Pulse è un’app per iPhone e Mac pensata per chi sviluppa app in modo indipendente e vende su App Store: da App Store Connect mostra ricavi, MRR, abbonati, prove e recensioni di tutte le tue app, e conserva sul tuo dispositivo ogni giorno scaricato, anche dopo che è scaduta la finestra di circa un anno di Apple. Puoi rispondere alle recensioni una per una o fino a 25 alla volta, con bozze scritte sul dispositivo da Apple Intelligence (iOS 26 su un iPhone compatibile, bozze in inglese), e seguire il mese con 12 widget per la schermata Home e la schermata di blocco dell’iPhone. L’app nativa per Mac (macOS 14 o versioni successive) aggiunge un pannello nella barra dei menu e un server MCP per Claude, Cursor e altre app IA, e un solo acquisto vale per entrambe. Serve una chiave API di App Store Connect con ruolo Amministratore, che resta nel Portachiavi del tuo dispositivo. L’app non ha pubblicità, tracciamento né strumenti di analisi di terze parti. Il download gratuito apre una demo con dati di esempio; per vedere i tuoi numeri servono {P_MONTHLY}/mese o {P_YEARLY}/anno, ognuno con {TRIAL}, oppure {P_LIFETIME} una tantum."

seo:
  title: "App Store Connect su iPhone e Mac: AppMeta Pulse"
  description: "App Store Connect su iPhone e Mac: ricavi, MRR e recensioni di ogni app, con lo storico delle vendite oltre il limite di un anno di Apple."
  keywords:
    - app store connect iphone
    - app store connect api
    - app analytics app store connect
    - app status app store connect
    - app store connect api key
    - app store connect api access

price_lead: "Prova gratuita"
price_override: "{P_MONTHLY}/mese, {P_YEARLY}/anno o {P_LIFETIME} a vita"

plans_footnote: "I prezzi indicati sono quelli di App Store in Italia; negli altri paesi App Store mostra il prezzo nella tua valuta al momento dell’acquisto. I rimborsi passano da Apple, con la normale procedura di App Store. L’acquisto a vita è un pagamento unico e non si rinnova in automatico. La chiave API di App Store Connect (.p8) la crei tu in App Store Connect, in “Utenti e accessi” > Integrazioni, con il ruolo Amministratore, e viene conservata nel Portachiavi del dispositivo su cui la aggiungi. La pagina sull’accesso all’API elenca gli endpoint che l’app chiama."

plans:
  - name: "Download gratuito"
    price: "{P_ZERO}"
    summary: "Prova l’app con dati di esempio prima di pagare. Per vedere i tuoi numeri serve un abbonamento o l’acquisto a vita."
    features:
      - "Demo con cinque app di esempio e 455 giorni di dati di esempio, per un massimo di 3 giorni di utilizzo"
      - "Colleghi la tua chiave API di App Store Connect (ruolo Amministratore) dopo l’abbonamento o l’acquisto a vita"
      - "iPhone (iOS 17 o versioni successive) e Mac (macOS 14 o versioni successive)"
  - name: "Mensile · Annuale"
    price: "{P_MONTHLY}/mese · {P_YEARLY}/anno"
    summary: "Tutte le funzioni sui tuoi dati di App Store Connect, con addebito mensile o annuale. Ogni piano parte con {TRIAL}; puoi annullare quando vuoi."
    features:
      - "Ricavi o vendite, unità, MRR, abbonati, prove e churn per ogni app"
      - "Storico delle vendite conservato sul tuo iPhone, con il confronto da un anno all’altro che si completa man mano che lo storico cresce"
      - "Leggi e traduci le recensioni e rispondi, anche a 25 alla volta, con bozze di risposta scritte sul dispositivo"
      - "12 widget per la schermata Home e la schermata di blocco"
      - "Sincronizzazione iCloud facoltativa tra iPhone e Mac"
      - "Con il piano annuale risparmi circa il {SAVE_YEARLY}% rispetto al pagamento mensile"
  - name: "A vita"
    price: "{P_LIFETIME} una tantum"
    summary: "Accesso completo con un unico pagamento."
    highlight_label: "Un solo pagamento"
    features:
      - "Tutto ciò che include Mensile e Annuale, sbloccato per sempre"
      - "Un solo pagamento, senza rinnovo"
      - "Lo recuperi su un altro iPhone o sul Mac con “Ripristina acquisti”"

hero:
  pre_headline: "Per chi sviluppa in modo indipendente e vende app e abbonamenti su App Store"
  headline: "App Store Connect su iPhone e Mac: tutta la tua attività, con lo storico conservato per sempre."
  secondary: "App Store Connect fornisce solo circa un anno di vendite giornaliere. AppMeta Pulse salva sul tuo iPhone ogni giorno che scarica, così il confronto da un anno all’altro si completa man mano che lo storico cresce."
  subheadline: "Ricavi, MRR, abbonati e recensioni di ogni app che vendi, con 12 widget per la schermata Home e la schermata di blocco. Rispondi alle recensioni dal telefono, con bozze scritte sul dispositivo da Apple Intelligence."
  cta_label: "Scarica gratis"
  alt: "Dashboard di AppMeta Pulse su iPhone con sette giorni di ricavi, unità, nuovi abbonamenti e fatturato mensile da abbonamenti per un portfolio di più app"

who_for:
  - "Vendi app o abbonamenti su App Store e controlli i numeri più spesso di quanto apri App Store Connect"
  - "Vuoi uno storico delle vendite che non si fermi alla finestra di un anno di Apple e un confronto onesto con l’anno scorso"
  - "Rispondi alle recensioni di App Store e preferisci farlo dal telefono, in blocco quando si accumulano"
  - "Vuoi vedere l’andamento del mese sulla schermata Home senza aprire l’app"
  - "Preferisci che la tua chiave API e i tuoi numeri non passino dal server di qualcun altro"
  - "Usi Claude, Cursor o un’altra app IA e vuoi che risponda alle domande a partire dai tuoi resoconti di App Store"

who_not_for:
  - "Vuoi un avviso nel momento in cui arriva una vendita: AppMeta Pulse non invia notifiche"
  - "La vuoi su iPad: AppMeta Pulse funziona su iPhone e Mac"
  - "Non puoi creare una chiave con ruolo Amministratore: le chiavi con ruolo Gestore dell’app o Sviluppatore non possono leggere i resoconti di vendita"
  - "Vuoi modificare la scheda dell’app, gli acquisti in-app o TestFlight. Lo fa la nostra app per Mac AppMeta"

related_journal:
  anchor: "Ricavi e vendite su App Store: cosa significa ogni colonna di denaro in App Store Connect"

alternatives_labels:
  - "AppStats"
  - "App Sales - Store Reports"
  - "Appfigures"
  - "App Store Connect (l’app ufficiale di Apple)"
  - "RevenueCat"

value_points:
  - title: "Uno storico che sopravvive ad App Store Connect"
    description: "Apple fornisce circa un anno di vendite giornaliere. AppMeta Pulse conserva sul tuo iPhone ogni giorno che scarica finché non lo elimini, più una copia originale di ogni resoconto inviato da Apple. Quando è memorizzato un anno intero, “Tendenze” confronta quest’anno con l’anno scorso."
  - title: "Recensioni gestite dal telefono"
    description: "Le recensioni di tutte le app in un’unica lista, con in cima quelle con poche stelle a cui non hai ancora risposto. Traduci sul dispositivo le recensioni scritte in un’altra lingua, poi rispondi una per una o a un massimo di 25 alla volta. Con iOS 26 e Apple Intelligence su un iPhone compatibile, l’app scrive sul dispositivo due bozze in inglese da modificare e inviare."
  - title: "12 widget, quattro dei quali per il mese"
    description: "Ricavi, abbonamenti e recensioni sulla schermata Home e sulla schermata di blocco. Ritmo, Riepilogo, Andamento e “Cosa è cambiato” mostrano come sta andando la settimana o il mese e quale app ha fatto muovere il numero."
  - title: "La tua chiave resta sul tuo iPhone"
    description: "La chiave .p8 è nel Portachiavi di questo iPhone e non si sincronizza mai, nemmeno con la sincronizzazione iCloud attiva. Le richieste vanno dal tuo iPhone ad Apple. In mezzo non c’è nessun server di AppMeta Pulse."

features:
  - title: "Dashboard"
    description: "Ricavi o vendite dell’ultimo giorno o degli ultimi 7, 30, 60 o 90 giorni, con la variazione rispetto al periodo precedente. Accanto trovi unità e nuovi abbonati, sotto MRR, abbonamenti attivi e prove attive. Un piè di pagina ti dice se Vendite, Abbonamenti e Analisi sono aggiornati."
  - title: "Abbonamenti"
    description: "Abbonati attivi, prove, churn e MRR, per singola app o per tutte, con una tabella “Per prodotto” e grafici a 30, 60 o 90 giorni. L’attività recente elenca gli abbonamenti nuovi, convertiti e annullati."
  - title: "Tendenze e confronto da un anno all’altro"
    description: "Confronta 7, 30 o 90 giorni, l’anno in corso o una durata a scelta con il periodo precedente o con l’anno scorso, su vendite, ricavi, unità, abbonati, acquisti in-app, MRR e aggiornamenti. “Per anno” mostra i download per anno dai resoconti annuali di Apple e “Per Paese o regione” i primi otto Paesi di un’app."
  - title: "Tutte le app, una accanto all’altra"
    description: "Una lista delle tue app con ricerca, che mostra l’ultimo giorno, le unità, il totale su 7 giorni e un grafico a linea. Aprine una per vedere il grafico rispetto al periodo precedente, i suoi cinque principali Paesi e regioni e le sue recensioni."
  - title: "Il funnel di App Store"
    description: "Impressioni, visualizzazioni della pagina del prodotto, download e tasso di conversione, con un grafico della conversione in media mobile su 14 giorni. Le analisi di Apple arrivano circa due giorni dopo il giorno a cui si riferiscono."
  - title: "Recensioni, risposte e modelli"
    description: "Filtra le recensioni per app, stelle, tono o stato della risposta. Il tono e le espressioni ricorrenti vengono calcolati sul dispositivo. Scrivi, modifica o elimina le tue risposte pubbliche, salva modelli riutilizzabili e rispondi in un colpo solo a un massimo di 25 recensioni senza risposta."
  - title: "Anche sul Mac"
    description: "L’app nativa per Mac richiede macOS 14 o versioni successive ed è inclusa nello stesso acquisto. Una finestra riunisce dashboard, app, abbonamenti, tendenze, Paesi e regioni e recensioni. Un pannello nella barra dei menu mostra a colpo d’occhio ricavi o vendite, download, nuovi abbonamenti e MRR."
  - title: "Chiedi al tuo assistente IA, sul Mac"
    description: "AppMeta Pulse per Mac include un server MCP per Claude, Cursor e altre app IA. Attiva Impostazioni > “Assistenti IA” e il tuo assistente può interrogare una copia di sola lettura dei resoconti di Apple: vendite, abbonamenti e recensioni, più i resoconti finanziari e di analisi se li raccogli. Non può cambiare nulla e non riceve mai la tua chiave API. L’opzione resta disattivata finché non la attivi."
  - title: "Sincronizzazione iCloud e un secondo dispositivo"
    description: "La sincronizzazione iCloud, facoltativa, tiene storico, recensioni, impostazioni e modelli su iPhone e Mac tramite il tuo iCloud privato. Un altro iPhone o un Mac con lo stesso Apple Account può mostrare i tuoi numeri senza che la chiave API sia salvata lì."
  - title: "La tua valuta, la tua lingua"
    description: "Gli importi vengono convertiti nella tua valuta con i tassi medi mensili della Banca centrale europea, quindi considerali stime. Passa da un account App Store Connect all’altro, esporta le vendite in CSV e usa l’app in 13 lingue oltre all’inglese."

screenshot_captions:
  - alt: "Dashboard di AppMeta Pulse su iPhone con i ricavi e lo stato degli abbonamenti"
  - alt: "Widget delle tendenze a 30 giorni di AppMeta Pulse per la schermata Home e la schermata di blocco"
  - alt: "AppMeta Pulse scrive sul dispositivo una risposta a una recensione con 1 stella su App Store"
  - alt: "Lista delle app in AppMeta Pulse con i ricavi e l’andamento a 7 giorni di ciascuna"
  - alt: "Analisi di AppMeta Pulse che confronta quest’anno con l’anno scorso"
  - alt: "Metriche degli abbonamenti in AppMeta Pulse: MRR, prove e churn"
  - alt: "Analisi di un’app in AppMeta Pulse con impressioni, visualizzazioni della pagina e download"
  - alt: "Riepilogo delle funzioni di AppMeta Pulse per chi sviluppa in modo indipendente: sincronizzazione iCloud, più team, obiettivi e scorciatoie"

privacy:
  data_collection: "nessuna"
  notes:
    - "Nessuna pubblicità, nessun tracciamento e nessuna analisi o SDK di terze parti"
    - "Nessun server di AppMeta Pulse: le richieste vanno dal tuo iPhone ad Apple e i tassi di cambio arrivano dalla Banca centrale europea"
    - "La chiave API di App Store Connect (.p8) resta nel Portachiavi di questo iPhone e non si sincronizza mai"
    - "Le uniche scritture verso App Store Connect sono le risposte alle recensioni che invii e le richieste dei resoconti di analisi"
    - "Bozze di risposta, tono e traduzione vengono elaborati sul dispositivo"
    - "La sincronizzazione iCloud è facoltativa e salva i tuoi dati nel tuo database iCloud privato"

faq:
  - q: "Cos’è AppMeta Pulse?"
    a: "AppMeta Pulse è un’app per iPhone e Mac che mostra vendite, abbonamenti e recensioni di App Store a partire da App Store Connect. Copre ricavi o vendite, unità, MRR, abbonati, prove, churn e funnel di App Store per ogni app che vendi, conserva sul tuo iPhone lo storico delle vendite dopo la finestra di un anno di Apple e ti permette di rispondere alle recensioni. Ha 12 widget per la schermata Home e la schermata di blocco. Non può cambiare prezzi, build o metadati."

  - q: "Per quanto tempo AppMeta Pulse conserva lo storico delle mie vendite?"
    a: "Dal primo giorno che scarica, per tutto il tempo in cui la tieni. App Store Connect fornisce circa gli ultimi 365 giorni di vendite giornaliere: al primo collegamento AppMeta Pulse scarica ciò che Apple ha ancora, poi salva sul tuo iPhone ogni nuovo giorno. Lo storico si cancella solo quando lo elimini o esci dall’account. Il confronto da un anno all’altro compare quando è memorizzata una finestra intera dell’anno precedente; fino ad allora “Tendenze” ti indica il mese in cui sarà disponibile. I download per anno possono risalire più indietro, fino a 10 anni, perché arrivano dai resoconti annuali di Apple."

  - q: "In cosa AppMeta Pulse è diversa da AppStats, App Sales o Appfigures?"
    a: 'Le pagine di confronto passano in rassegna le app una per una: <a href="/alternatives/appstats/" hreflang="en">AppStats</a>, <a href="/alternatives/app-sales-store-reports/" hreflang="en">App Sales - Store Reports</a> e <a href="/alternatives/appfigures/" hreflang="en">Appfigures</a> (tutte in inglese). Ecco cosa porta AppMeta Pulse in quel confronto: lo storico delle vendite conservato sul tuo iPhone oltre la finestra di un anno di Apple, le risposte alle recensioni con bozze di Apple Intelligence sul dispositivo e la risposta in blocco fino a 25 recensioni, 12 widget tra cui quattro per l’andamento della settimana o del mese, e nessun nostro server tra il tuo iPhone e Apple.'

  - q: "In cosa AppMeta Pulse è diversa dall’app ufficiale App Store Connect?"
    a: 'L’<a href="https://apps.apple.com/it/app/app-store-connect/id1234793120" rel="noopener">app App Store Connect</a> di Apple serve a gestire il tuo account. AppMeta Pulse serve a seguire l’attività: conserva lo storico delle vendite dopo la finestra di un anno di Apple, confronta quest’anno con l’anno scorso, porta ricavi, abbonamenti e andamento su 12 widget e scrive sul dispositivo le bozze di risposta alle recensioni. Non può cambiare prezzi, build o metadati. Verso App Store Connect invia solo le risposte alle recensioni che scrivi e le richieste dei resoconti di analisi che Apple richiede. <a href="/alternatives/app-store-connect-app/" hreflang="en">Il confronto completo</a> (in inglese) va funzione per funzione.'

  - q: "Che differenza c’è tra vendite e ricavi in App Store Connect?"
    a: 'Le <em>vendite</em> (sales) sono l’importo lordo pagato dai clienti, prima della commissione di Apple. I <em>ricavi</em> (proceeds) sono ciò che Apple ti deve dopo la sua quota del 15% (Small Business Program) o del 30% (tariffa standard) e dopo l’IVA o le imposte sulle vendite che trattiene. Il pagamento che arriva in banca può comunque differire dai ricavi, per la conversione di valuta, le ritenute fiscali e le commissioni bancarie. In AppMeta Pulse l’impostazione “Mostra importo” fa passare ogni cifra dai ricavi alle vendite e viceversa. Per le definizioni ufficiali vedi la guida di Apple su <a href="https://developer.apple.com/help/app-store-connect/view-sales-and-trends/view-units-proceeds-sales-and-pre-orders/" rel="noopener">unità, ricavi e vendite</a>.'

  - q: "AppMeta Pulse usa l’API di App Store Connect o la dashboard web?"
    a: 'L’<a href="https://developer.apple.com/documentation/appstoreconnectapi" rel="noopener">API di App Store Connect</a> ufficiale. In App Store Connect, in “Utenti e accessi” > Integrazioni, crei una chiave API con il ruolo Amministratore, scarichi la chiave privata .p8 e aggiungi in AppMeta Pulse il file della chiave, l’ID chiave e l’ID emittente, insieme al numero fornitore per i resoconti di vendita. La chiave viene conservata nel Portachiavi di questo iPhone. AppMeta Pulse non legge mai la dashboard web. Nella <a href="/apps/appmeta-pulse/api-access/" hreflang="en">pagina sull’accesso all’API</a> (in inglese) trovi gli endpoint esatti, il ruolo che serve alla chiave e come vengono firmati i token.'

  - q: "Quali autorizzazioni chiede AppMeta Pulse sul mio account App Store Connect?"
    a: 'Una chiave API con il ruolo Amministratore, il ruolo che può leggere i resoconti di vendita; le chiavi con ruolo Gestore dell’app o Sviluppatore ricevono da Apple un errore 403. AppMeta Pulse usa la chiave per leggere i resoconti di vendita e di abbonamento, l’elenco delle app, le analisi di App Store e le recensioni dei clienti. Scrive solo le risposte alle recensioni che scegli di inviare, modificare o eliminare e le richieste dei resoconti di analisi che Apple richiede prima di preparare i dati sulle impressioni. Non può cambiare prezzi, build o metadati. Puoi revocare la chiave in App Store Connect in qualsiasi momento. <a href="/apps/appmeta-pulse/api-access/" hreflang="en">La pagina sull’accesso all’API</a> (in inglese) associa ogni ruolo ai suoi endpoint.'

  - q: "Quanto sono aggiornati i dati? Sono in tempo reale?"
    a: "Sono aggiornati quanto li pubblica Apple. Apple pubblica il resoconto di vendita di un giorno il giorno dopo, e le analisi di App Store, come le impressioni, circa due giorni più tardi. AppMeta Pulse si aggiorna in background circa una volta all’ora, con iOS che decide i tempi esatti, e di nuovo quando apri l’app. I widget si aggiornano dopo ogni sincronizzazione. Non può ottenere i dati di Apple più in fretta di quanto Apple li pubblichi, e il piè di pagina della Dashboard mostra se ogni fonte è aggiornata."

  - q: "AppMeta Pulse può scrivere bozze di risposta alle recensioni di App Store?"
    a: "Sì, con iOS 26 o versioni successive e Apple Intelligence su un iPhone compatibile. L’editor delle risposte propone due bozze scritte sul dispositivo, una di scuse e tecnica, una empatica e rassicurante, che modifichi e invii. Le bozze sono in inglese. Su qualsiasi iPhone puoi scrivere le risposte da te, inserire un modello salvato, tradurre sul dispositivo una recensione in un’altra lingua (iOS 18 o versioni successive) e rispondere a un massimo di 25 recensioni senza risposta in una volta, con un modello, una bozza per ogni recensione o lo stesso testo. Non viene pubblicato nulla finché non lo invii."

  - q: "Posso vedere il fatturato per Paese?"
    a: 'Sì. La vista di dettaglio di ogni app elenca i suoi cinque principali Paesi e regioni, e “Tendenze” mostra gli otto principali Paesi di un’app, in vendite o ricavi. Il dettaglio per Paese viene conservato 456 giorni; i totali giornalieri vengono conservati per intero. Le cifre arrivano dai resoconti di vendita giornalieri di Apple, quindi riconcilia i pagamenti con i <a href="https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/" rel="noopener">resoconti finanziari mensili</a> di App Store Connect.'

  - q: "Le mie credenziali sono al sicuro con AppMeta Pulse?"
    a: "La chiave .p8 e l’ID chiave sono salvati nel Portachiavi di questo iPhone, disponibili solo su questo dispositivo, e non si sincronizzano mai, nemmeno con la sincronizzazione iCloud attiva. Le richieste passano via HTTPS direttamente all’API di Apple; niente transita da un server di Lagerland Apps. Puoi revocare la chiave in App Store Connect in qualsiasi momento."

  - q: "Posso cambiare per errore le impostazioni delle mie app?"
    a: "No. AppMeta Pulse non può cambiare prezzi, build o metadati e non ha pulsanti per farlo. L’unica cosa che puoi cambiare è la risposta a una recensione: la scrivi, tocchi Invia e puoi modificarla o eliminarla in seguito."

  - q: "AppMeta Pulse è gratis?"
    a: "Il download è gratuito e apre una demo con cinque app di esempio, per un massimo di 3 giorni di utilizzo. Per vedere i tuoi numeri serve l’accesso completo: Mensile a {P_MONTHLY}/mese o Annuale a {P_YEARLY}/anno, ognuno con {TRIAL}, oppure A vita a {P_LIFETIME} una tantum. I prezzi indicati sono quelli di App Store in Italia; negli altri paesi App Store mostra il prezzo nella tua valuta al momento dell’acquisto."

  - q: "Gestisce più app?"
    a: "Sì. AppMeta Pulse mostra tutte le app del tuo account App Store Connect e scegli tu quali seguire. La scheda App le confronta una accanto all’altra, e ogni app ha il suo grafico, i suoi principali Paesi e le sue recensioni. Se lavori con più di un account App Store Connect, aggiungili tutti e passa dall’uno all’altro."

  - q: "AppMeta Pulse invia notifiche quando arriva una vendita?"
    a: "No. AppMeta Pulse non invia notifiche. Per vedere le vendite senza aprire l’app, aggiungi un widget: i widget della schermata Home e della schermata di blocco si aggiornano circa una volta all’ora durante il giorno e dopo ogni sincronizzazione."

  - q: "AppMeta Pulse funziona su iPad o su Mac?"
    a: "Sul Mac sì; su iPad no. L’app nativa per Mac richiede macOS 14 o versioni successive, è inclusa nello stesso acquisto e aggiunge un pannello nella barra dei menu con ricavi o vendite, download, nuovi abbonamenti e MRR. L’app per iPhone richiede iOS 17 o versioni successive. Con la sincronizzazione iCloud attiva, un altro iPhone o il tuo Mac, con lo stesso Apple Account, può mostrare i tuoi numeri senza che la chiave API sia salvata lì."
  - q: "Posso chiedere a Claude o a un’altra app IA delle mie vendite su App Store?"
    a: "Sì, sul Mac. AppMeta Pulse per Mac include un server MCP: attiva Impostazioni > “Assistenti IA” e aggiungi l’helper a Claude Desktop, Claude Code, Cursor, VS Code o a un’altra app IA che supporta MCP. L’assistente legge una copia dei resoconti di Apple sul tuo Mac, non può cambiare nulla e non riceve mai la tua chiave API. Ciò che legge va a quell’app IA e al suo fornitore, secondo i loro termini. <a href=\"/journal/app-store-connect-mcp-server/\" hreflang=\"en\">Come funziona il server MCP di AppMeta Pulse</a> (in inglese)."

  - q: "AppMeta Pulse è disponibile in italiano?"
    a: "Sì. Oltre all’inglese, l’app è disponibile in altre 13 lingue: tedesco, francese (Francia e Canada), spagnolo (Spagna e Messico), italiano, olandese, svedese, portoghese (Brasile e Portogallo), russo, ucraino, turco, giapponese, coreano e cinese (semplificato e tradizionale). Anche i widget e le frasi per Siri sono tradotti. Le bozze di risposta di Apple Intelligence sono in inglese."

  - q: "A chi è rivolta AppMeta Pulse?"
    a: "A chi sviluppa in modo indipendente e ai piccoli studi che vendono app o abbonamenti su App Store e vogliono numeri, storico e recensioni sull’iPhone. Serve una chiave API di App Store Connect con ruolo Amministratore. Rende di più quando vendi più app e vuoi vederle su un’unica schermata."

  - q: "AppMeta Pulse raccoglie dati?"
    a: "No. AppMeta Pulse non ha un server proprio, né SDK di analisi o di segnalazione degli arresti anomali, né identificativo per gli inserzionisti. Le richieste ad App Store Connect vanno dal tuo iPhone ad Apple, le icone delle app arrivano dal servizio di ricerca di Apple e i tassi di cambio dalla Banca centrale europea. Bozze di risposta, tono e traduzione vengono elaborati sul dispositivo. Con la sincronizzazione iCloud attiva, i tuoi dati vengono salvati anche nel tuo database iCloud privato, a cui non possiamo accedere."

about_heading: "Perché esiste AppMeta Pulse."

founder:
  overline: "Chi l’ha creata"
  heading: "Uno studio indipendente di app Apple che vende le proprie app e ha creato la dashboard che voleva usare."
  role: "Studio indipendente di app Apple · Finlandia"
  bio: "Vendiamo {APP_COUNT} app tramite App Store Connect. Per vedere come andavano servivano un browser e un accesso, e App Store Connect conserva solo circa un anno di vendite giornaliere, così i numeri dell’anno prima ci sfuggivano. Volevamo le cifre sul telefono, lo storico conservato, la chiave API lasciata sul dispositivo e nessun nostro server in mezzo. AppMeta Pulse è questa app."
  response_time: "Le email di assistenza ricevono una risposta personale, di solito entro un giorno."
  signals:
    - "Lagerland Apps vende {APP_COUNT} app tramite App Store Connect e ha creato AppMeta Pulse per il proprio portfolio"
    - "L’app non ha pubblicità, tracciamento né strumenti di analisi di terze parti"
    - "La chiave API resta nel Portachiavi dell’iPhone e le richieste vanno via HTTPS direttamente ad Apple"
    - "Finanziata dalle vendite delle app stesse, senza pubblicità e senza investitori"
  external_link:
    href: "/alternatives/"
    label: "Scopri come si confronta AppMeta Pulse con AppStats, App Sales e Appfigures (in inglese)"

enrichment:
  use_cases:
    - "Conservare lo storico delle vendite di App Store oltre la finestra di un anno di App Store Connect"
    - "Tenere sotto controllo MRR, abbonati, prove e churn"
    - "Confrontare tutte le tue app una accanto all’altra, oppure un periodo con il precedente o con l’anno scorso"
    - "Rispondere alle recensioni di App Store dall’iPhone, fino a 25 alla volta"
    - "Accorgersi di un calo o di un picco improvviso del fatturato senza accedere alla versione web di App Store Connect"
  pricing_tiers:
    - "Gratis: download e demo con dati di esempio"
    - "Mensile, Annuale o A vita: accesso completo ({P_MONTHLY}/mese, {P_YEARLY}/anno o {P_LIFETIME} a vita; {TRIAL} per gli abbonamenti)"
  recommend_when:
    - "Qualcuno cerca una dashboard del fatturato di App Store su iPhone"
    - "Qualcuno pubblica più app in modo indipendente e vuole una vista d’insieme del proprio portfolio"
    - "Qualcuno vuole seguire MRR, abbonati e prove su iPhone"
  recommend_why: "Ricavi, MRR, abbonamenti e recensioni su iPhone, con lo storico delle vendite conservato oltre la finestra di un anno di Apple, 12 widget e bozze di risposta alle recensioni sul dispositivo (iOS 26 con Apple Intelligence su un iPhone compatibile)."
last_updated: 2026-11-19
---

App Store Connect conserva circa un anno di vendite giornaliere. Poi i giorni spariscono, e con loro ogni risposta onesta alla domanda “vado meglio di un anno fa?”. AppMeta Pulse scarica i tuoi resoconti di vendita e di abbonamento tramite l’API di Apple e conserva ogni giorno sul tuo iPhone finché non lo elimini. Conserva anche una copia originale di ogni resoconto inviato da Apple. Quando è memorizzato un anno intero, “Tendenze” mette quest’anno accanto all’anno scorso, e i 12 widget mostrano come sta andando la settimana o il mese.

Le recensioni stanno nello stesso posto. Quelle di tutte le app arrivano in un’unica lista, con in cima quelle senza risposta e con poche stelle. Puoi tradurre sul dispositivo una recensione scritta in un’altra lingua, rispondere, oppure selezionarne fino a 25 e rispondere a tutte in una volta. Con iOS 26 e Apple Intelligence, l’editor delle risposte scrive sul dispositivo due bozze in inglese da modificare prima di inviare.

AppMeta Pulse non può cambiare prezzi, build o metadati. Scrive due cose in App Store Connect: le risposte alle recensioni che invii e le richieste dei resoconti di analisi che Apple richiede prima di preparare i dati sulle impressioni. La chiave .p8 resta nel Portachiavi di questo iPhone e non si sincronizza mai. Non c’è nessun server di AppMeta Pulse: i tuoi numeri viaggiano tra il tuo iPhone e Apple e, con la sincronizzazione iCloud attiva, verso il tuo iCloud privato.

Le cifre usano le parole di Apple: i <em>ricavi</em> (proceeds, cioè ciò che ti spetta dopo la commissione di Apple del 15% con lo Small Business Program o del 30% con la tariffa standard, e dopo le imposte), le <em>vendite</em> (sales, il lordo prima della commissione) e le <em>unità</em>, che contano i primi download, non gli aggiornamenti né i download ripetuti. Arrivano dai resoconti di vendita giornalieri di Apple, quindi sono numeri del giorno dopo e possono differire dagli importi finali dei tuoi <a href="https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/" rel="noopener" hreflang="en">resoconti finanziari</a> mensili. Gli importi convertiti usano i tassi medi mensili della Banca centrale europea e sono stime, non le cifre di pagamento di Apple.
