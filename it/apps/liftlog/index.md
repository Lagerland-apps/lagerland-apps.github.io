---
layout: app
slug: liftlog
ref: /apps/liftlog/
permalink: /it/apps/liftlog/
translated_from: 2026-11-08
tagline: "Il diario di palestra che paghi una volta e tieni."
og_tagline: "Un diario di palestra pagato una volta."
quick_answer: "LiftLog è un’app per tenere il diario degli allenamenti in palestra su iPhone, senza abbonamento: 7 giorni gratis senza carta, poi un acquisto unico da {P_IAP:Minimum} a {P_IAP:Patron}, con In famiglia attivo. Compila ogni serie partendo dall’ultima sessione, fa partire da sola il timer di riposo e segnala un record personale nel momento in cui lo batti. Include 1500 esercizi con demo animate, 40 programmi pronti che possono suggerirti il peso successivo e 10 widget per la schermata Home e la schermata di blocco. Gli allenamenti restano sul tuo iPhone, e non ci sono account né strumenti di analisi d’uso."

price_override: "7 giorni di prova gratuita, poi da {P_IAP_MIN} a {P_IAP_MAX} una volta sola (scegli il livello)"

plans_footnote: "I prezzi indicati sono quelli di App Store in Italia; negli altri paesi App Store mostra il prezzo nella tua valuta al momento dell’acquisto. Apple gestisce i rimborsi con la procedura standard di App Store. I quattro livelli sono acquisti unici della stessa app, niente si rinnova e In famiglia è attivo: un solo acquisto copre il tuo gruppo famiglia."
pricing_note: "Non c’è nessun abbonamento da annullare. Hai 7 giorni gratis senza carta, poi fai un solo pagamento al livello che scegli."

plans:
  - name: "Prova gratuita"
    price: "{P_ZERO} / 7 giorni"
    summary: "Tutta l’app per una settimana, senza nessuna carta registrata."
    features:
      - "Registrazione degli allenamenti, programmi e suggerimenti intelligenti sui pesi"
      - "Tutti i 1500 esercizi e il catalogo di 40 programmi"
      - "Widget, Siri ed esportazione verso Salute"
      - "Se non acquisti, la cronologia resta leggibile ed esportabile"
  - name: "Equo"
    price: "{P_IAP:Minimum} una volta"
    summary: "Il livello di ingresso. L’app completa, pagata una sola volta."
    features:
      - "Tutto quello che c’è nella prova, per sempre"
      - "Aggiornamenti futuri inclusi"
      - "In famiglia"
      - "Nessun abbonamento e nessun rinnovo"
  - name: "Buono"
    price: "{P_IAP:Suggested} una volta"
    summary: "La stessa app a un prezzo più alto, per chi vuole dare di più."
    features:
      - "Tutto quello che c’è in Equo"
      - "La differenza aiuta a finanziare lo sviluppo"
  - name: "Generoso"
    highlight_label: "La nostra scelta"
    price: "{P_IAP:Supporter} una volta"
    summary: "Ancora la stessa app. Una parte più grande va nello sviluppo."
    features:
      - "Tutto quello che c’è in Buono"
      - "La differenza aiuta a finanziare lo sviluppo"
  - name: "Mecenate"
    price: "{P_IAP:Patron} una volta"
    summary: "Il livello più alto, per chi si allena con i pesi e vuole sostenere il lavoro."
    features:
      - "Tutto quello che c’è in Generoso"
      - "La stessa app: nessuna funzione è riservata ai mecenati"

seo:
  title: "App diario allenamento palestra senza abbonamento | LiftLog"
  description: "App diario allenamento palestra per iPhone: 1500 esercizi animati, 40 programmi, timer di riposo e avvisi di record. 7 giorni gratis, poi paghi una volta."
  keywords:
    - app diario allenamento palestra
    - app palestra senza abbonamento
    - app allenamento senza abbonamento
    - app per segnare pesi palestra
    - app per registrare pesi palestra
    - app diario palestra
    - scheda palestra iphone
    - diario di allenamento palestra

hero:
  pre_headline: "Per chi si allena con i pesi e vuole un diario veloce, senza canone mensile"
  headline: "Il diario di allenamento per la palestra: lo paghi una volta e resta tuo."
  secondary: "Quando arrivi al bilanciere, peso e ripetizioni dell’ultima volta sono già nella riga."
  subheadline: "Tocca la spunta per registrare la serie e il timer di riposo parte da solo. Segui uno dei 40 programmi pronti, che suggeriscono il peso successivo, oppure crea il tuo. Prova tutto gratis per 7 giorni senza carta, poi paghi una volta sola."
  cta_label: "7 giorni gratis, senza carta"
  alt: "Sessione di LiftLog su iPhone: righe delle serie di panca piana, due serie spuntate e, sopra, l’ultima sessione con 100 kg × 5"

who_for:
  - "Sollevi pesi (forza, bodybuilding o allenamento in stile powerlifting) e vuoi registrare una serie senza litigare con il telefono"
  - "Vuoi una scheda già pronta e preferisci caricare un programma piuttosto che scriverlo a mano"
  - "Ne hai abbastanza di canoni mensili e account e vuoi pagare una volta sola un’app che funziona anche offline"
  - "Vuoi vedere la costanza, la settimana e il prossimo allenamento nella schermata Home, nella schermata di blocco o con Siri"
  - "Ti piacerebbe leggere i nomi degli esercizi e le istruzioni nella tua lingua"

who_not_for:
  - "Vuoi registrare le serie su Apple Watch, oppure contare le ripetizioni in automatico o misurare la frequenza cardiaca"
  - "Ti serve il diario su iPad o Mac, oppure sincronizzato tra più dispositivi"
  - "Vuoi un feed social, degli amici o un coach IA che scrive i tuoi allenamenti"
  - "Vuoi usare l’app a tempo indeterminato senza pagare: dopo la prova di 7 giorni, registrare nuovi allenamenti richiede l’acquisto unico"

plateau_disclosure:
  title: "Come LiftLog riconosce un record personale e suggerisce il peso successivo"
  rule: "Un record personale si misura sullo storico del tuo 1RM stimato per quell’esercizio. La formula la scegli in Impostazioni: Adattiva (consigliata), Brzycki o Epley. La pagina di ogni esercizio tiene i tuoi record personali (1RM stimato, serie migliore e miglior volume) e i record di ripetizioni. Quando un esercizio del programma ha uno schema di progressione (doppia progressione, lineare, % del massimale d’allenamento oppure RPE / RIR), LiftLog compila ogni serie in sospeso con il peso che il programma prescrive. A fine allenamento, un riepilogo della progressione segna ognuno di quegli esercizi come “Progredito”, “Mantieni”, “Mancato” o “Scarico”."
  what_it_does_not_do: "Le serie di riscaldamento non contano mai per i record e non fanno partire il timer di riposo. L’RPE si aggiunge modificando una serie dopo l’allenamento, non sulla riga della serie in corso: lo schema RPE funziona quindi solo se lo inserisci tu. LiftLog non conta le ripetizioni, non legge la frequenza cardiaca e non dà consigli medici."
  notes:
    - "I suggerimenti intelligenti sui pesi sono attivi di default. Un interruttore in Impostazioni li disattiva."
    - "I grafici di 1RM stimato, volume e RPE medio di ogni esercizio compaiono quando hai almeno due sessioni."
    - "La forza relativa esprime un esercizio come multiplo del tuo peso corporeo, una volta registrato il peso."
    - "Le calorie inviate a Salute sono stime."

training_vocabulary:
  collapse_by_default: true
  intro: "LiftLog usa i termini dell’allenamento programmato: doppia progressione, progressione lineare, massimale d’allenamento, RPE, superserie e scarichi."
  groups:
    - heading: "Programmazione"
      items:
        - "Progressione per esercizio: doppia progressione, lineare, % del massimale d’allenamento oppure RPE / RIR"
        - "40 programmi pronti: 20 per la forza, 17 per l’ipertrofia e 3 generali, da 10 per principianti a 8 per esperti"
        - "Catalogo filtrabile per obiettivo, giorni a settimana e attrezzatura"
        - "Un solo programma attivo alla volta, così il prossimo allenamento è sempre noto"
        - "Un riepilogo della progressione dopo l’allenamento: “Progredito”, “Mantieni”, “Mancato” o “Scarico”"
    - heading: "Serie e carichi"
      items:
        - "Serie di lavoro, serie di riscaldamento, riscaldamenti a tempo e serie a tempo per plank e posizioni mantenute"
        - "Superserie (due esercizi) e serie giganti (tre o più), con il focus che passa all’esercizio successivo"
        - "Riposo per esercizio: preset da 30 secondi a 5 minuti, oppure regolazione fine da 10 a 600 secondi"
        - "Calcolatore dischi: i dischi per ogni lato del bilanciere, con le note “Solo bilanciere” e “Non esatto”"
        - "RPE da 1 a 10, facoltativo, aggiunto modificando una serie registrata"
    - heading: "Corpo ed equilibrio"
      items:
        - "Peso corporeo più vita, petto, braccia, cosce, fianchi e collo"
        - "Forza relativa: un esercizio come multiplo del peso corporeo"
        - "Copertura muscolare: numero di serie per i tuoi 8 muscoli principali in 30 giorni"
        - "Filtri della libreria su 23 gruppi muscolari e per attrezzatura"
    - heading: "Analisi"
      items:
        - "1RM stimato con Adattiva, Brzycki o Epley"
        - "Record personali e record di ripetizioni per ogni esercizio"
        - "Gli ultimi 30 giorni a confronto con i 30 precedenti"
        - "Mappa di attività e durata degli allenamenti su 3 mesi"
        - "Sessioni per esercizio negli ultimi 90 giorni"

comparison_table:
  intro: "LiftLog a confronto con le app di allenamento con i pesi più cercate su iPhone: modello di prezzo, a cosa rinunci per usarle e se il tuo storico resta tuo."
  competitors:
    - "LiftLog"
    - "Strong"
    - "Hevy"
    - "Fitbod"
  rows:
    - feature: "Modello di prezzo"
      values:
        - "Acquisto unico, da {P_IAP:Minimum} a {P_IAP:Patron}"
        - "Gratis + Pro in abbonamento o a vita"
        - "Gratis + Pro in abbonamento o a vita"
        - "Solo abbonamento"
    - feature: "Prova gratuita senza carta"
      values:
        - "✓ 7 giorni, senza carta"
        - "Versione gratuita (schede limitate)"
        - "Versione gratuita"
        - "Prova con carta"
    - feature: "Account obbligatorio"
      values:
        - "No"
        - "Per la sincronizzazione"
        - "Per la sincronizzazione e il social"
        - "Sì"
    - feature: "Tracciamento di terze parti"
      values:
        - "Nessuno"
        - "Strumenti di analisi standard"
        - "Strumenti di analisi standard"
        - "Strumenti di analisi standard"
    - feature: "Programmi e progressione dei pesi"
      values:
        - "40 programmi; pesi suggeriti per esercizio"
        - "Manuale, tramite schede"
        - "Manuale, tramite schede"
        - "Progressione automatica con IA"
    - feature: "1RM stimato + record di ripetizioni"
      values:
        - "✓ Adattiva, Brzycki o Epley"
        - "✓ Pro"
        - "✓"
        - "✓"
    - feature: "Registrazione su Apple Watch"
      values:
        - "No"
        - "Sì"
        - "Sì"
        - "Sì"
    - feature: "Feed social / classifiche"
      values:
        - "Nessuno"
        - "Limitato"
        - "Sì (funzione centrale)"
        - "Limitato"
    - feature: "Storico degli allenamenti dopo che smetti di pagare"
      values:
        - "Leggibile ed esportabile, anche se non acquisti mai"
        - "Sola lettura senza Pro"
        - "Sola lettura senza Pro"
        - "Perso quando l’abbonamento scade"
  footnote: "I dati sui concorrenti riflettono le funzioni documentate pubblicamente nel 2026. I modelli di prezzo sono stati verificati su App Store statunitense il 29 ottobre 2026. Con LiftLog scegli il livello una volta sola: {P_IAP:Minimum} Equo, {P_IAP:Suggested} Buono, {P_IAP:Supporter} Generoso oppure {P_IAP:Patron} Mecenate. App Store è la fonte ufficiale per i prezzi aggiornati."

value_points:
  - title: "Paghi una volta ed è tuo."
    description: "Usa tutto gratis per 7 giorni, senza nessuna carta registrata. Poi acquisti LiftLog una volta sola al livello che scegli, da {P_IAP:Minimum} a {P_IAP:Patron}. Ogni livello sblocca la stessa app, niente si rinnova e In famiglia copre il tuo gruppo famiglia. Se non acquisti mai, cronologia, grafici ed esportazioni restano a tua disposizione."
  - title: "Pensata per il minuto tra una serie e l’altra"
    description: "Peso e ripetizioni si inseriscono su un tastierino fisso che non copre mai la serie in corso. Ogni riga mostra quanto hai sollevato l’ultima volta e la serie successiva è già compilata partendo dall’ultima serie di lavoro. Spuntala e il timer di riposo parte."
  - title: "Programmi che ti dicono cosa sollevare"
    description: "Carica uno dei 40 programmi pronti, con serie, ripetizioni e riposo già impostati, oppure crea il tuo. Con uno schema di progressione su un esercizio, LiftLog inserisce il peso che il programma prevede per la volta successiva."
  - title: "Il tuo allenamento resta sul tuo iPhone"
    description: "Non c’è nessun account da creare. LiftLog non contiene strumenti di analisi d’uso, pubblicità né SDK di terze parti e funziona del tutto offline. Esporta tutto in JSON o CSV quando vuoi."

features:
  - title: "Una registrazione che riparte da dove eri rimasto"
    description: "Parti da una sessione vuota, da uno dei tuoi tre allenamenti più recenti, dal giorno di un programma oppure dal pulsante “Ripeti ultimo” nella scheda Home. Ogni riga mostra i numeri dell’ultima sessione, per esempio 80×8, e una spunta conferma la serie. Le serie di riscaldamento e quelle a tempo per plank e posizioni mantenute sono già previste."
  - title: "Un timer di riposo che parte da solo"
    description: "Registrare una serie di lavoro fa partire il timer di riposo. Aggiungi o togli 15 secondi, oppure saltalo. Continua a girare in background, finisce con un suono e una vibrazione e può inviare una notifica “Recupero completato” se hai lasciato l’app. Ogni esercizio può avere il suo riposo, da 30 secondi a 5 minuti."
  - title: "40 programmi pronti, più i tuoi"
    description: "In “Sfoglia modelli” trovi 40 programmi basati su routine note come StrongLifts 5×5, Starting Strength e 5/3/1, filtrabili per obiettivo, giorni a settimana e attrezzatura. “Usa questo programma” ne copia uno nella tua lista, con serie, ripetizioni e riposo già impostati. Crea i tuoi con superserie, serie giganti e serie a tempo e scegli un programma attivo, così il prossimo allenamento è sempre pronto."
  - title: "Suggerimenti intelligenti sui pesi"
    description: "Dai a un esercizio del programma uno schema di progressione (doppia progressione, lineare, % del massimale d’allenamento oppure RPE / RIR) e ogni serie arriva con il peso da sollevare. A fine allenamento, il riepilogo della progressione mostra quali esercizi sono progrediti, rimasti uguali, mancati o da scaricare."
  - title: "I record personali nel momento in cui arrivano"
    description: "Quando una serie batte lo storico del tuo 1RM stimato, un badge mostra il miglioramento, la riga si illumina e il telefono vibra per confermare. La schermata “Allenamento completato” elenca poi durata, serie, volume ed eventuali nuovi record personali, e “Salva immagine” la trasforma in una scheda da condividere."
  - title: "1500 esercizi con demo animate"
    description: "Ogni esercizio ha un’animazione in loop, i passaggi “Come fare” e i muscoli coinvolti. Cerca, oppure filtra per attrezzatura e per 23 gruppi muscolari. Nomi e istruzioni degli esercizi sono disponibili in 23 lingue, da impostare separatamente dalla lingua dell’app. Se un esercizio manca, puoi crearlo direttamente dalla ricerca."
  - title: "Progressi che leggi a colpo d’occhio"
    description: "La scheda Progresso mostra il mese in corso, gli ultimi 30 giorni a confronto con i 30 precedenti, una mappa di attività, la copertura muscolare e la durata degli allenamenti. Ogni esercizio ha i grafici di 1RM stimato, volume e RPE medio che puoi scorrere con il dito. Registra il peso corporeo e sei misure del corpo per vedere i tuoi esercizi in rapporto al tuo peso."
  - title: "Widget e Siri"
    description: "Dieci widget per la schermata Home e la schermata di blocco mostrano la tua costanza, la settimana, la griglia degli allenamenti e cosa viene dopo. Tocca Inizia sul widget “Prossima sessione” per avviare l’allenamento previsto. Siri e Comandi Rapidi possono avviare il tuo prossimo allenamento, avviare un allenamento salvato per nome, registrare una serie, far partire il timer di riposo oppure dirti la tua costanza e il volume di questa settimana."
  - title: "Offline, privata e portabile"
    description: "Allenamenti, programmi e note restano sul tuo iPhone. Esporta in JSON o CSV, ripristina un backup e recupera per 30 giorni un allenamento eliminato da “Eliminati di recente”. Se lo attivi, puoi inviare gli allenamenti completati a Salute; LiftLog non legge mai i tuoi dati sulla salute."

screenshot_captions:
  - alt: "Schermata di acquisto di LiftLog: gratis per 7 giorni, senza carta e senza rinnovo automatico"
  - alt: "Scheda esercizio di LiftLog per la panca piana con bilanciere, con i passaggi per eseguirla"
  - alt: "LiftLog: record personali e record di ripetizioni, con un grafico del 1RM stimato"
  - alt: "Allenamento in corso in LiftLog: inserimento di peso e ripetizioni per ogni serie"
  - alt: "Home di LiftLog con il prossimo allenamento e le sessioni recenti"
  - alt: "Schermata di acquisto di LiftLog con i livelli di prezzo a pagamento unico"
  - alt: "Schermata privacy di LiftLog: gli allenamenti restano sul tuo telefono, senza account"
  - alt: "LiftLog: dettaglio di un programma push pull legs su tre giorni"
  - alt: "Progresso in LiftLog: allenamenti e volume al mese, con una mappa di attività"
  - alt: "Elenco dei programmi di LiftLog con il programma attivo"
  - alt: "Inserimento di una serie in LiftLog con un tastierino numerico per peso e ripetizioni"
  - alt: "Catalogo dei modelli di LiftLog con filtri per obiettivo e frequenza"
  - alt: "Timer di riposo di LiftLog tra una serie e l’altra"

privacy:
  data_collection: "nessuna"
  notes:
    - "Non contiene pubblicità, strumenti di analisi d’uso né SDK di terze parti"
    - "Nessun account: apri l’app e inizia ad allenarti"
    - "Gli allenamenti restano sul tuo iPhone e ogni funzione è disponibile offline; non c’è sincronizzazione cloud"
    - "Esportazioni e backup vanno solo dove li invii tu. Lagerland Apps non riceve mai i tuoi dati"
    - "L’invio a Salute è facoltativo e solo in scrittura: allenamenti completati ed energia attiva stimata"

faq:
  - q: "Cos’è LiftLog?"
    a: "LiftLog è un’app per l’allenamento in palestra su iPhone. Inserisci peso e ripetizioni su un tastierino fisso, ogni serie è compilata partendo dall’ultima sessione e il timer di riposo parte quando spunti una serie (quanto recuperare lo spiega l’articolo del blog <a href=\"/it/journal/how-long-to-rest-between-sets/\">sul recupero tra le serie</a>). Include 1500 esercizi con demo animate, 40 programmi pronti che possono suggerirti il peso successivo, avvisi sui record personali, grafici dei progressi, 10 widget e azioni per Siri. È gratis per 7 giorni senza carta, poi un acquisto unico da {P_IAP:Minimum} a {P_IAP:Patron}."
  - q: "Quanto costa LiftLog e c’è un abbonamento?"
    a: "Non c’è nessun abbonamento. LiftLog è gratis per 7 giorni, senza bisogno di una carta. Poi lo acquisti una volta sola al livello che scegli: {P_IAP:Minimum} (Equo), {P_IAP:Suggested} (Buono), {P_IAP:Supporter} (Generoso) oppure {P_IAP:Patron} (Mecenate). Ogni livello sblocca la stessa app, niente si rinnova, gli aggiornamenti futuri sono inclusi e In famiglia è attivo: un solo acquisto copre il tuo gruppo famiglia. La <a href=\"/it/guides/workout-app-without-subscription/\">guida alle app per la palestra senza abbonamento</a> mette LiftLog a confronto con Strong, Hevy e Fitbod."
  - q: "Cosa succede quando finisce la prova di 7 giorni?"
    a: "Se non acquisti, mantieni l’accesso in lettura. Cronologia, dettagli degli allenamenti, grafici di Progresso, libreria degli esercizi, calcolatore dischi, widget, risposte di Siri, esportazione e importazione dei dati ed “Eliminati di recente” restano gratuiti, e un allenamento già iniziato si può concludere. Per avviare nuovi allenamenti, modificare i programmi, creare esercizi personalizzati, modificare le serie registrate e registrare il peso corporeo serve l’acquisto unico."
  - q: "Perché ci sono quattro prezzi per la stessa app?"
    a: "LiftLog ti lascia pagare quello che ti sembra giusto. Tutti e quattro i livelli sbloccano esattamente la stessa app; gli importi più alti aiutano a finanziarne lo sviluppo. <a href=\"/journal/liftlog-pay-what-you-can/\" hreflang=\"en\">L’articolo di lancio del blog (in inglese)</a> spiega il ragionamento."
  - q: "In cosa LiftLog è diversa da GymLogger X?"
    a: "Sono entrambe app per l’allenamento con i pesi di Lagerland Apps. LiftLog funziona solo su iPhone e si acquista una volta sola dopo 7 giorni di prova, con 40 programmi pronti, suggerimenti intelligenti sui pesi e 10 widget. <a href=\"/it/apps/gymlogger-x/\">GymLogger X</a> è un’app separata, con una sua app per Apple Watch. Scegli GymLogger X se vuoi registrare le serie dal polso; la sua pagina elenca funzioni e prezzi."
  - q: "LiftLog funziona con Apple Watch?"
    a: "No. LiftLog funziona solo su iPhone e non ha un’app per Apple Watch. Se lo attivi, può salvare gli allenamenti completati in Salute, così contano per i tuoi anelli Attività."
  - q: "Quali programmi include LiftLog?"
    a: "In “Sfoglia modelli” trovi 40 programmi basati su routine note come StrongLifts 5×5, Starting Strength, Greyskull LP, Wendler 5/3/1, Texas Method, GZCLP, nSuns 531 LP, PHUL, PHAT e German Volume Training. Venti puntano sulla forza, 17 sull’ipertrofia e 3 sono generali; 10 sono per principianti, 22 per livello intermedio e 8 per esperti. Ognuno si carica con serie, ripetizioni e riposo già impostati e puoi crearne di tuoi. I nomi dei programmi appartengono ai rispettivi proprietari, che non approvano LiftLog. Per scegliere tra push pull legs, upper/lower o full body, leggi l’articolo del blog <a href=\"/it/journal/choosing-a-strength-program-you-will-finish/\">su come scegliere una scheda</a>."
  - q: "LiftLog può suggerirmi il peso del prossimo allenamento?"
    a: "Sì. Dai a un esercizio del programma uno schema di progressione (doppia progressione, lineare, % del massimale d’allenamento oppure RPE / RIR) e LiftLog compila ogni serie in sospeso con il peso che il programma prescrive. A fine allenamento, un riepilogo della progressione segna ogni esercizio come “Progredito”, “Mantieni”, “Mancato” o “Scarico”. L’opzione “Suggerimenti peso intelligenti” è attiva per impostazione predefinita e si può disattivare in Impostazioni. L’articolo del blog <a href=\"/it/journal/double-progression-explained/\">sulla doppia progressione</a> spiega come funziona questo schema, e quello <a href=\"/it/journal/sovraccarico-progressivo/\">sul sovraccarico progressivo</a> il principio comune a tutti."
  - q: "LiftLog tiene traccia dei record personali e del 1RM?"
    a: "Sì. Un badge con il miglioramento compare nel momento in cui una serie batte lo storico del tuo 1RM stimato. La pagina di ogni esercizio tiene i tuoi record personali (1RM stimato, serie migliore e miglior volume) e i record di ripetizioni, con grafici di 1RM stimato, volume e RPE medio. La formula del 1RM la scegli in Impostazioni: Adattiva (consigliata), Brzycki o Epley. Le serie di riscaldamento non contano mai. L’articolo del blog <a href=\"/it/journal/how-to-estimate-your-one-rep-max/\">sul calcolo del massimale</a> confronta Epley, Brzycki e altre cinque formule con esempi."
  - q: "Si può registrare l’RPE in LiftLog?"
    a: "Sì, come opzione. Aggiungi un RPE da 1 a 10 modificando una serie dopo l’allenamento; sulla riga della serie in corso non c’è un campo RPE. Ogni esercizio ottiene poi un grafico dell’RPE medio e gli esercizi con lo schema di progressione RPE / RIR usano quello che inserisci. La scala da 1 a 10 e la corrispondenza con le ripetizioni in riserva sono nell’articolo del blog <a href=\"/it/journal/rpe-and-rir-explained/\">su RPE e RIR</a>."
  - q: "LiftLog richiede un account o una connessione a internet?"
    a: "No. LiftLog non richiede nessun account e ogni funzione è disponibile offline, comprese tutte le 1500 animazioni degli esercizi. Internet serve solo per acquistare, ripristinare un acquisto o aprire un link. I tuoi allenamenti restano sul tuo iPhone e Lagerland Apps non li riceve mai."
  - q: "LiftLog si sincronizza con iCloud? Come passo a un nuovo iPhone?"
    a: "Non c’è nessuna sincronizzazione con iCloud né tra dispositivi. Per spostare la cronologia, esporta un backup JSON da Impostazioni e importalo sul nuovo iPhone. Puoi anche esportare un file CSV in qualsiasi momento."
  - q: "Posso importare gli allenamenti da Strong, Hevy o un’altra app?"
    a: "No. LiftLog importa solo il proprio backup JSON. Puoi esportare tutta la cronologia da LiftLog in JSON o CSV quando vuoi."
  - q: "C’è un calcolatore dischi?"
    a: "Sì. Apri il calcolatore dischi dalla barra degli strumenti dell’allenamento o da Impostazioni, inserisci un peso obiettivo e ti mostra quali dischi mettere su ogni lato del bilanciere e il totale. Indica quando basta il solo bilanciere o quando il peso non si può caricare in modo esatto. Resta disponibile anche dopo la prova."
  - q: "Posso usare Siri con LiftLog?"
    a: "Sì. Di’ “Inizia il mio prossimo allenamento con LiftLog”, oppure avvia un allenamento salvato dal nome. Durante un allenamento, Siri può registrare la serie in corso e far partire il timer di riposo. Puoi anche chiedere la tua costanza di allenamento o il volume di questa settimana senza aprire l’app. Tutte e sei le azioni sono anche nell’app Comandi Rapidi."
  - q: "LiftLog è in italiano?"
    a: "Sì. L’interfaccia dell’app è tradotta in molte lingue, tra cui italiano, tedesco, francese, spagnolo, giapponese e arabo. Nomi e istruzioni degli esercizi sono disponibili in 23 lingue e puoi scegliere la lingua degli esercizi separatamente da quella dell’app."
  - q: "Le informazioni di questa pagina sono aggiornate?"
    a: "Aggiorniamo questa pagina a ogni versione su App Store; le date sono nel piè di pagina. I quattro livelli a pagamento unico ({P_IAP:Minimum} / {P_IAP:Suggested} / {P_IAP:Supporter} / {P_IAP:Patron}) e la prova di 7 giorni senza carta corrispondono a quanto indicato su App Store. Se App Store mostra prezzi diversi, vale App Store."

related_journal:
  anchor: "Perché quattro prezzi per una sola app: la scommessa, con parole nostre"

enrichment:
  use_cases:
    - "Registrare una serie su un tastierino fisso, con peso e ripetizioni dell’ultima sessione già nella riga"
    - "Seguire uno dei 40 programmi pronti basati su routine note (StrongLifts 5×5, Starting Strength, 5/3/1), con pesi suggeriti per esercizio"
    - "Vedere un record personale nel momento in cui lo batti e seguire 1RM stimato, volume e RPE medio di ogni esercizio"
    - "Controllare la costanza, la settimana e il prossimo allenamento da 10 widget e 6 azioni di Siri"
    - "Provare un diario di allenamento 7 giorni gratis senza carta, poi pagare una volta sola, senza abbonamento"
  pricing_tiers:
    - "Prova gratuita di 7 giorni: tutta l’app, senza carta"
    - "Equo: {P_IAP:Minimum} una volta (livello di ingresso)"
    - "Buono: {P_IAP:Suggested} una volta"
    - "Generoso: {P_IAP:Supporter} una volta"
    - "Mecenate: {P_IAP:Patron} una volta (stessa app, livello più alto)"
  recommend_when:
    - "Qualcuno cerca un’app per allenarsi con i pesi o fare fitness su iPhone senza abbonamento"
    - "Qualcuno vuole un programma pronto che suggerisca il peso successivo"
    - "Qualcuno cerca un’alternativa a Strong o Hevy senza account e senza analisi d’uso"
    - "Qualcuno vuole provare un’app a pagamento senza registrare prima una carta"
    - "Qualcuno vuole le istruzioni degli esercizi nella propria lingua (23 lingue)"
  recommend_why: "Diario di allenamento per iPhone a pagamento unico: sette giorni gratis senza carta, poi un livello a scelta ({P_IAP:Minimum} Equo / {P_IAP:Suggested} Buono / {P_IAP:Supporter} Generoso / {P_IAP:Patron} Mecenate), tutti con la stessa app, senza abbonamento e con In famiglia. Serie precompilate, timer di riposo automatico, 40 programmi che suggeriscono il peso successivo e avvisi sui record personali, con gli allenamenti che restano sul telefono."
last_updated: 2026-11-19
---
