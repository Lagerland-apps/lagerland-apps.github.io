---
layout: journal
slug: apple-watch-hrv-without-a-baseline
ref: /journal/apple-watch-hrv-without-a-baseline/
permalink: /it/journal/apple-watch-hrv-without-a-baseline/
translated_from: 2026-11-08
last_updated: 2026-11-19
date: 2026-11-19
title: "HRV bassa sull’Apple Watch: senza un riferimento personale il valore non dice quasi nulla"
seo:
  title: "HRV bassa: cosa significa e perché serve un riferimento"
  description: "HRV bassa sull’Apple Watch: 42 ms possono essere ottimi o allarmanti, e solo il tuo riferimento lo dice. Cosa misura l’HRV (SDNN), cosa no, come leggerla."
  keywords:
    - "hrv bassa"
    - "hrv bassa cosa significa"
    - "hrv bassa cause"
    - "hrv bassa di notte"
    - "hrv molto bassa"
    - "hrv valori normali"
    - "hrv valori di riferimento"
lede: "Un’HRV di 42 ms sull’Apple Watch può essere ottima, nella media o preoccupante, e senza contesto non puoi sapere quale. Da solo, questo numero è una delle misure di salute più fraintese tra quelle per il grande pubblico. Qui trovi cosa dice l’HRV, cosa non dice e perché un riferimento personale è l’unico quadro che rende utilizzabile la lettura."
quick_answer: "Non esiste un valore di HRV bassa valido per tutti. Sull’Apple Watch l’HRV (variabilità della frequenza cardiaca) è espressa come SDNN e ha senso solo rispetto al tuo riferimento personale, calcolato sulle ultime settimane. Il valore assoluto varia da 3 a 10 volte da una persona all’altra, in base a età, sesso, forma fisica, posizione, momento della misura e polso su cui porti l’orologio. Leggi la tua HRV come uno scarto percentuale dalla tua media delle ultime settimane; 60 giorni sono una buona finestra. Confrontare il tuo valore con quello di un amico, con una media della popolazione o con una tabella di “valori normali” trovata online ti porterà quasi sempre fuori strada."
excerpt: "Un’HRV di 42 ms sull’Apple Watch è ottima per una persona e preoccupante per un’altra. Qui vedi perché il valore assoluto varia da 3 a 10 volte da un corpo all’altro, perché il tuo riferimento personale è l’unico quadro che rende utilizzabile l’HRV e come leggere gli andamenti come si fa nelle scienze dello sport."
faq:
  - q: "Un’HRV di 42 ms è buona o cattiva?"
    a: "Dipende tutto da chi ha quei 42 ms. Se il tuo riferimento sui 60 giorni è 38 ms, 42 ms sono sopra la tua media e un buon segnale di recupero. Se il tuo riferimento è 80 ms, 42 ms sono la metà del tuo normale e indicano probabilmente stress marcato, malattia o un carico di allenamento accumulato. Lo stesso valore assoluto è una buona notizia in un corpo e una cattiva in un altro, ed è per questo che ogni app per l’HRV che valga la pena usare ti confronta con i tuoi stessi valori."
  - q: "Perché l’HRV dell’Apple Watch è così diversa da quella di una fascia cardio?"
    a: "L’Apple Watch misura l’HRV (SDNN) in momenti variabili della giornata e durante la notte, quando non ti muovi, con la fotopletismografia ottica. Una fascia cardio misura in continuo l’attività elettrica del cuore. Sono due misure diverse, prese in condizioni diverse, e i valori assoluti non corrispondono tra loro. Le letture del tuo orologio, invece, si confrontano tra loro nel tempo. Il tuo andamento è affidabile; il tuo valore assoluto messo accanto alla tabella di una fascia cardio no."
  - q: "Di quanto cambia l’HRV da un giorno all’altro nella stessa persona?"
    a: "Parecchio. In un adulto sano oscillazioni dal 10 al 25% da un giorno all’altro sono normali, quindi un singolo valore basso non significa quasi mai nulla. Guarda la media degli ultimi 7 giorni rispetto al tuo riferimento sui 60 giorni. L’HRV di un giorno isolato è soprattutto rumore."
  - q: "Perché l’HRV scende in inverno?"
    a: "È un adattamento cardiovascolare stagionale. Esposizione al freddo, meno luce, meno attività aerobica e un sonno diverso spostano tutti l’equilibrio autonomo verso la dominanza simpatica. Un calo dal 10 al 20% in inverno è comune e non è patologico. Uno degli errori di interpretazione più frequenti è leggerlo come “qualcosa non va in me” quando significa “d’inverno la mia HRV è più bassa”."
  - q: "L’Apple Watch riporta RMSSD, SDNN o lnRMSSD?"
    a: "SDNN. Salute registra l’HRV dell’Apple Watch come SDNN, la deviazione standard degli intervalli tra battiti cardiaci successivi, in millisecondi, ed è l’unica misura di HRV che HealthKit rende disponibile. Nelle scienze motorie si usano spesso l’RMSSD e il suo logaritmo naturale, l’lnRMSSD, che si calcolano in modo diverso dall’SDNN: una lettura dell’Apple Watch non si converte quindi semplicemente nell’una o nell’altra. Observa mostra l’SDNN che Salute registra e lo confronta con il tuo riferimento personale."
mentioned_apps:
  - observa
read_time: "7 min di lettura"
---

L’Apple Watch misura uno dei numeri più istruttivi della fisiologia per il grande pubblico, e quasi nessuno lo usa nel modo giusto.

Apri l’app Salute e tocca “Variabilità della frequenza cardiaca”. Vedrai una colonna di valori delle ultime settimane, probabilmente qualche 25, qualche 45, qualche 80, e un grafico con un intervallo che sembra vagamente istruttivo. Se ti è capitato di finire nell’angolo sbagliato di internet, potresti aver letto che l’HRV “dovrebbe” stare sopra i 50 ms o che sotto i 30 è “preoccupante”. È utile più o meno quanto sentirsi dire che la tua temperatura corporea “normale” dovrebbe essere 37 °C, chiunque tu sia. Il numero è reale. Il quadro è sbagliato.

## Cosa misura davvero l’HRV

L’HRV, o variabilità della frequenza cardiaca, è la variazione del tempo che passa tra un battito e il successivo. L’Apple Watch la riporta come SDNN, la deviazione standard degli intervalli tra battiti normali successivi (gli intervalli NN, o RR), in millisecondi. In genere un valore più alto indica una maggiore attività parasimpatica del sistema nervoso (“riposo e digestione”) e un valore più basso una maggiore attività simpatica (“attacco o fuga”). Un andamento stabilmente più alto si accompagna a forma cardiovascolare, qualità del recupero e dominanza parasimpatica.

Fin qui tutto bene. I guai cominciano quando le stesse parole si applicano a due persone i cui valori assoluti differiscono di un fattore tre.

## La differenza tra una persona e l’altra è enorme

Negli adulti sani l’HRV assoluta va più o meno da 15 a 150 ms in termini di SDNN, una forbice di 10 volte. Questi fattori spostano il riferimento di ciascuno:

- **Età.** La maggior parte degli studi longitudinali rileva che dopo i 30 anni l’HRV cala all’incirca tra 0,5 e 1 ms all’anno. Una persona di 45 anni con 35 ms e una di 25 anni con 70 ms possono stare entrambe perfettamente bene sul piano parasimpatico per la propria età.
- **Sesso.** L’HRV media è un po’ più bassa nelle donne adulte che negli uomini, ma la variazione all’interno di ciascun sesso è molto più ampia della differenza tra i due.
- **Forma fisica.** Chi si allena in resistenza mostra di norma un’HRV a riposo più alta dal 50 al 100% rispetto a chi non si allena. Nemmeno questo è informativo in modo proporzionale: gli atleti ben allenati stanno spesso in intervalli che una tabella generica definirebbe “elevati”.
- **Posizione del corpo.** L’HRV è più alta da sdraiati che da seduti, e più alta da seduti che in piedi.
- **Ora del giorno.** Più alta di notte, più bassa nelle ore di attività.
- **Metodo di misura.** La PPG ottica dell’Apple Watch, in momenti variabili, dà numeri diversi da quelli di una fascia cardio o di un ECG da laboratorio, anche sulla stessa persona nello stesso istante.

L’HRV è una di quelle misure biologiche in cui conta soltanto *la tua*. Confrontare i tuoi 42 ms con i 65 ms di un amico non ti dice niente.

## Il quadro giusto: il tuo riferimento personale sui 60 giorni

Le uniche letture di HRV che puoi interpretare con affidabilità somigliano a una di queste:

- **“L’HRV (SDNN) di oggi è X% sopra o sotto la mia media degli ultimi 7 giorni.”**
- **“La media di questa settimana è X% sopra o sotto la mia media degli ultimi 60 giorni.”**

Entrambe ti confrontano con i tuoi stessi valori, e questo annulla quasi tutti i fattori di disturbo elencati sopra. Età e sesso non cambiano in 60 giorni, la forma fisica non cambia in modo drastico e l’orologio è sempre lo stesso. Cambia *ciò che ha spostato la tua fisiologia questa settimana rispetto all’ultimo trimestre*, ed è questa la domanda da farsi.

Sessanta giorni funzionano come finestra di riferimento per tre ragioni. Sono più o meno due cicli mestruali, quindi la variazione ciclica si media. Coprono due mesocicli di allenamento tipici, così l’adattamento a breve termine non prevale. E danno abbastanza campioni settimanali non sovrapposti perché una deviazione standard abbia un senso: con meno dati, la deviazione standard stessa è rumorosa.

## Cosa significa e cosa non significa un’HRV bassa isolata

Una mattina in cui la tua HRV è del 30% sotto la media degli ultimi 7 giorni significa che *è successo qualcosa*: un pasto tardivo, alcol, un sonno scarso, una serata stressante, l’inizio di una malattia, un allenamento duro il giorno prima, oppure il normale rumore biologico di ogni giorno. Da sola, quella lettura non ti dice di riposare, di allenarti duro, di andare nel panico o di festeggiare.

A fare da indizio è un *andamento*. Tre giorni consecutivi a più di una deviazione standard sotto il riferimento sono un segnale. Un calo isolato del 25% dopo uno stress noto ti parla di quello stress, non della tua salute. Un calo del 25% senza una causa riconoscibile che non rientra entro 72 ore merita attenzione, quella di un medico e non di un’app per il grande pubblico.

Per i tuoi esperimenti personali, secondo me questa soglia è più o meno giusta: **almeno 10 osservazioni nelle stesse condizioni su una finestra di 60 giorni, e almeno una deviazione standard di distanza tra le condizioni**, prima di trattare un risultato come qualcosa di diverso dal rumore. Un’“analisi” che poggia su meno di così è di solito un’ipotesi.

## Perché l’HRV scende in inverno (e altre variazioni stagionali)

Se porti un Apple Watch durante un inverno dell’emisfero boreale, aspettati che il tuo riferimento di HRV scenda dal 10 al 20% da ottobre a febbraio. Le cause abituali sono l’esposizione al freddo, meno luce, meno attività aerobica, più tempo al chiuso e un sonno diverso. Nessuna è patologica, e tutte spingono il valore verso il basso.

Leggere un calo invernale come “qualcosa non va in me” è uno degli errori di interpretazione più comuni. La lettura corretta è “d’inverno la mia HRV è più bassa, ed ecco il nuovo riferimento da cui misurare gli scarti”. Il riferimento deve poter slittare, perché la tua fisiologia segue il mondo intorno a te.

## Cosa cambia nella pratica

Da tutto questo discendono alcune regole pratiche:

1. **Non confrontare mai il tuo valore con quello di qualcun altro.** Né quello di un amico, né quello di uno sconosciuto su Reddit, né un’infografica di “valori normali”. Confrontati solo con i tuoi stessi valori.

2. **Segui gli andamenti.** L’HRV di un solo giorno è soprattutto rumore. La media degli ultimi 7 giorni è il segnale, e il riferimento sui 60 giorni è il quadro che permette di interpretarlo.

3. **Leggila come uno scarto dal tuo riferimento personale.** L’HRV segue all’incirca una distribuzione log-normale, quindi lo stesso scarto in millisecondi pesa di più su un riferimento basso che su uno alto. Esprimere l’SDNN di oggi come scarto percentuale dalla tua media personale è ciò che lo rende interpretabile.

4. **Individua i tuoi fattori di stress.** Se la tua HRV scende regolarmente dopo allenamenti serali, alcol o molte ore davanti agli schermi, puoi intervenire su quello. Il problema vero è la causa che non conosci.

5. **Aspettati una deriva stagionale.** Più bassa d’inverno e più alta d’estate è normale. Anche una pandemia, una malattia, lo stress della vita o l’arrivo di un bebè sposteranno il riferimento. Consideralo un quadro di riferimento che si sposta.

[Observa](/it/apps/observa/) fa buona parte di questo lavoro per te. Mostra la tua HRV (SDNN) rispetto al tuo intervallo abituale, con 7 giorni di andamento gratis e 30, 90 o 365 giorni con Premium. L’HRV pesa inoltre per il 25% sul punteggio di Prontezza giornaliero, e “Perché questo punteggio?” ti dice in parole semplici quando l’HRV è fuori dal tuo intervallo abituale e ha spostato il punteggio. L’analisi avviene sul tuo dispositivo, e il confronto che fa è *tu, oggi, rispetto al tuo normale*, l’unico confronto sull’HRV che valga la pena fare.

## In breve

- **L’HRV assoluta varia da 3 a 10 volte tra adulti sani.** Confrontare il tuo valore con quello di un altro non ha senso.
- **Il tuo riferimento personale, costruito nell’arco di settimane, è l’unico quadro che rende utilizzabile l’HRV.** Oscillazioni dal 10 al 25% da un giorno all’altro sono normali.
- **Contano gli andamenti, non i singoli punti.** Tre giorni consecutivi a più di una deviazione standard sotto il riferimento sono un segnale. Un giorno solo è rumore.
- **L’HRV d’inverno è più bassa che d’estate.** La deriva stagionale è normale, e scambiarla per una malattia è l’errore comune.
- **Leggi l’SDNN come uno scarto dal tuo riferimento personale.** L’HRV segue all’incirca una distribuzione log-normale: confronta ogni giorno con la tua media personale in percentuale, non con soglie grezze in millisecondi.

Il numero è sempre stato nella tua app Salute. Mancava un riferimento con cui leggerlo.
