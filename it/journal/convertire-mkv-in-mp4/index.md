---
layout: journal
slug: convertire-mkv-in-mp4
permalink: /it/journal/convertire-mkv-in-mp4/
local_only: true
last_updated: 2026-11-19
date: 2026-11-19
title: "Come convertire MKV in MP4 senza ricodificare: remux, VLC e MediaKit"
seo:
  title: "Convertire MKV in MP4 con VLC, remux o MediaKit"
  description: "Convertire MKV in MP4 su Mac o iPhone: remux o ricodifica, i passaggi in VLC, il limite dei convertitori online e come farlo con MediaKit."
  keywords:
    - "convertire mkv in mp4"
    - "convertire mkv in mp4 con vlc"
    - "convertire mkv in mp4 senza perdere qualità"
    - "convertire mkv in mp4 mac"
    - "app per convertire mkv in mp4"
lede: "Un file MKV è un contenitore, e convertirlo in MP4 può ridursi a cambiare l’involucro, senza ricodificare immagine e audio. L’articolo spiega la differenza tra remux e ricodifica, cosa si può fare con VLC, cosa comporta un convertitore online con un file grande e come MediaKit apre un MKV su Mac e su iPhone, con i formati audio che passano e quelli che vengono scartati."
quick_answer: "Per convertire un MKV in MP4 senza ricodificare serve un remux: video e audio vengono copiati in un contenitore MP4 così come sono, e funziona solo se i codec sono compatibili con MP4. VLC è gratuito e converte dal menu Media, Convert/Save, mentre un convertitore online ti obbliga a caricare l’intero file. MediaKit fa il remux sul dispositivo, su Mac e su iPhone, con l’opzione “Mantieni l’originale (remux)” dello strumento Converti, ma scarta l’audio DTS, E-AC-3 e MP3 e ti avvisa. Converti è gratuito nei primi 3 giorni, poi serve Pro; Comprimi video resta gratuito, ma ricodifica."
excerpt: "Convertire MKV in MP4: cos’è un contenitore, remux o ricodifica, VLC e i convertitori online con un file grande, e come MediaKit apre e converte un MKV su Mac e su iPhone."
faq:
  - q: "Come convertire MKV in MP4 gratis?"
    a: "VLC è gratuito e sa convertire: la sua documentazione descrive la procedura da Media, Convert/Save. In MediaKit lo strumento Comprimi video resta gratuito dopo i primi 3 giorni, un file alla volta, e porta un MKV in MP4; però ricodifica, quindi non è una conversione senza ricompressione. Converti, che può fare il remux, è gratuito nei primi 3 giorni e poi richiede Pro."
  - q: "Si può convertire MKV in MP4 senza perdere qualità?"
    a: "Sì, se i codec lo permettono: un remux copia video e audio in un nuovo contenitore senza ricodificarli, quindi non aggiunge una nuova compressione. MediaKit lo fa con l’opzione “Mantieni l’originale (remux)” dello strumento Converti. L’audio DTS, E-AC-3 o MP3 di un MKV, invece, viene scartato con un avviso: quelle tracce non finiscono nell’MP4."
  - q: "Come convertire MKV in MP4 con VLC?"
    a: "Nella documentazione di VLC 3.0 la procedura è: Media, Convert/Save, Add, scegli il file, indica il file di destinazione, scegli un profilo di conversione dall’elenco Profile e premi Start. Il wiki di VideoLAN, che avverte di essere una pagina non aggiornata, descrive una procedura guidata in cui si scelgono un codec video, un codec audio e un contenitore, e dice che una transcodifica può essere molto lenta e che non serve se i flussi hanno già il codec che vuoi. Nessuna delle due pagine dice quale profilo faccia un remux: per sapere che codec contiene il risultato, riproducilo in VLC e apri Tools, Codec Information."
  - q: "Un convertitore online va bene per un MKV molto grande?"
    a: "Un convertitore online riceve il file sui suoi server, lo converte e te lo rimanda: con un MKV grande significa caricarlo per intero prima di cominciare, e il contenuto lascia il tuo dispositivo. Per un file grande una conversione sul dispositivo evita il caricamento: vanno bene VLC o MediaKit. Secondo la documentazione di VLC, inoltre, un remux è molto più veloce di una transcodifica."
  - q: "Come convertire MKV in MP4 su iPhone?"
    a: "MediaKit apre i file MKV su iPhone (iOS 17 o successivo): invia il file all’app dal foglio di condivisione con “Invia a MediaKit”, scegli lo strumento Converti e mp4 alla voce Contenitore. Per un remux scegli “Mantieni l’originale (remux)” alla voce Codec: l’audio DTS, E-AC-3 o MP3 viene scartato con un avviso."
  - q: "Come convertire MKV in MP4 su Mac?"
    a: "Nel Finder fai clic con il tasto destro sul file MKV, scegli “Apri con” e poi MediaKit. Scegli Converti, poi mp4 alla voce Contenitore e “Mantieni l’originale (remux)” alla voce Codec. MediaKit richiede macOS 14.6 o successivo. QuickTime Player non serve a questo: secondo Apple non può esportare i filmati come video MP4."
mentioned_apps:
  - mediakit
read_time: "7 min di lettura"
---

Un file MKV è un contenitore: racchiude flussi di video, audio e sottotitoli. Per questo convertire un MKV in MP4 può ridursi a cambiare l’involucro, senza ricodificare né l’immagine né l’audio. Succede solo se i codec contenuti sono compatibili con MP4, ed è questo che separa una conversione senza ricompressione da una che ricomprime il file. L’articolo segue questo filo e poi confronta VLC, i convertitori online e [MediaKit](/it/apps/mediakit/), un’app di Lagerland Apps, lo studio che pubblica questo sito.

## Cos’è un MKV e in cosa si differenzia da un MP4

Il progetto Matroska, che mantiene il formato, precisa sul suo sito che un contenitore [non è un formato di compressione video o audio](https://www.matroska.org/what_is_matroska.html){: hreflang="en"} (in inglese). Lo descrive come un involucro che può contenere molti flussi audio, video e di sottotitoli, così da conservare un film intero in un solo file. Tra i contenitori esistenti di cui Matroska vuole essere l’alternativa open source cita anche MP4, che quindi è a sua volta un contenitore.

Due file possono avere la stessa immagine e lo stesso audio e distinguersi solo per l’involucro. Cambiare involucro non tocca il contenuto; cambiare codec obbliga a decodificare e ricodificare.

## Perché un MKV non sempre si apre su iPhone o Mac

Lo spiega Apple in una pagina di supporto sui [file multimediali che non si aprono](https://support.apple.com/it-it/102644): app come Foto, iMovie, Safari, Keynote e QuickTime Player funzionano con molti formati, ma quelli meno recenti o specifici potrebbero non funzionare come previsto se il dispositivo, il sistema o l’app non li supportano. Tra le estensioni da cercare per trovare un’altra app che supporti il formato Apple cita .mkv, insieme a .avi e .wmv. Su Mac la stessa pagina dice che il Finder può mostrare “Tipo: File video Matroska”: seleziona il file e premi Comando-I.

Per il Mac c’è un dato in più nella guida di QuickTime Player a [esportare i filmati](https://support.apple.com/it-it/guide/quicktime-player/qtp20e395859/mac): i filmati vengono esportati come filmato QuickTime (.mov) con codec H.264 o HEVC e QuickTime Player non può esportarli come video MP4. Se cerchi come convertire MKV in MP4 su Mac, quell’app non è la strada.

## Remux o ricodifica: quando non si ricomprime niente

La documentazione di VLC definisce il [remux](https://docs.videolan.me/vlc-user/desktop/3.0/en/advanced/streaming/remuxing.html){: hreflang="en"} (in inglese) come l’operazione che prende i flussi già codificati e li mette in un contenitore diverso. Lo distingue dalla transcodifica, che invece ricodifica. Il remux cambia solo il contenitore, è molto più veloce perché non c’è nulla da codificare e lascia la dimensione del file quasi uguale.

La stessa pagina pone la condizione: poiché non si ricodifica, i codec originali devono essere compatibili con il nuovo contenitore, altrimenti il remux non riesce. In MediaKit questa è l’opzione “Mantieni l’originale (remux)” dello strumento Converti: i flussi passano nel nuovo contenitore senza essere ricodificati. L’audio DTS, E-AC-3 e MP3 di un MKV però viene scartato, con un avviso: il video resta, quelle tracce audio no.

Una ricodifica, invece, comprime di nuovo il contenuto. È quello che succede quando comprimi fino a una dimensione di destinazione o passi a un altro codec. Va bene quando il remux non è possibile o quando vuoi un file più piccolo, ma ricomprimendo si può perdere qualità.

## Convertire MKV in MP4 con VLC

VLC è gratuito. Il [sito di VideoLAN](https://www.videolan.org/vlc/){: hreflang="en"} (in inglese) lo presenta come un lettore multimediale libero e open source e tra i formati che riproduce cita MKV. Per convertire, la [documentazione di VLC 3.0](https://docs.videolan.me/vlc-user/desktop/3.0/en/basic/tipsandtricks/index.html){: hreflang="en"} (in inglese) indica questi passaggi: scegli Media, Convert/Save, premi Add e seleziona il file, indica il file di destinazione, scegli un profilo di conversione dall’elenco Profile e premi Start. I nomi delle voci sono quelli della documentazione in inglese.

Il [wiki di VideoLAN sulla transcodifica](https://wiki.videolan.org/Transcode/){: hreflang="en"} (in inglese) descrive una procedura guidata che chiede un codec video, un codec audio e un contenitore. Aggiunge che non serve transcodificare se i flussi di ingresso hanno già il codec che vuoi; il suo autore pensa, senza esserne sicuro, che nell’interfaccia questa opzione si chiami “keep the original track”. Il wiki avverte anche che la pagina non è aggiornata e che una transcodifica può essere molto lenta.

Nessuna delle due pagine dice quale profilo dell’elenco faccia un remux, quindi non si può dare per certo che la procedura guidata lo faccia per impostazione predefinita. Per sapere che codec contiene il tuo file, la documentazione di VLC suggerisce di riprodurlo e aprire Tools, Codec Information.

Se usi già VLC, fa il lavoro sul computer senza spendere nulla. Il suo uso su iPhone resta fuori da questo articolo.

## I convertitori online e i file grandi

Un convertitore online riceve il tuo file sui suoi server, lo converte e te lo rimanda. Con un MKV grande significa caricarlo per intero prima di cominciare, e il contenuto lascia il tuo dispositivo. Due pagine di questo sito approfondiscono il compromesso: l’articolo su [cosa succede ai tuoi file in un convertitore online](/journal/your-photos-shouldnt-ride-the-elevator/){: hreflang="en"} (in inglese) e il [confronto con CloudConvert](/it/alternatives/cloudconvert/).

Con un file grande il remux conviene: secondo la documentazione di VLC è molto più veloce di una transcodifica e lascia la dimensione quasi invariata.

## Convertire MKV in MP4 con MediaKit

MediaKit è un’app per iPhone e Mac che lavora sul dispositivo: il file non viene mandato da nessuna parte. Apre direttamente i file MKV, perché li scompatta da sé. I suoi altri strumenti video compaiono nell’articolo sugli [strumenti multimediali che il Mac ha già](/journal/every-media-tool-already-on-your-mac/){: hreflang="en"} (in inglese).

Su Mac (macOS 14.6 o successivo), nel Finder fai clic con il tasto destro sul file MKV, scegli “Apri con” e poi MediaKit.

Su iPhone (iOS 17 o successivo) invia il file a MediaKit dal foglio di condivisione, con “Invia a MediaKit”.

In entrambi i casi:

1. Scegli lo strumento Converti.
2. Alla voce Contenitore scegli mp4 (ci sono anche mov e m4v).
3. Per un remux scegli “Mantieni l’originale (remux)” alla voce Codec. H.264, HEVC e ProRes sono le altre opzioni, e ricodificano.
4. Tocca Esegui (sul Mac, fai clic) e leggi l’eventuale avviso sull’audio scartato.

Se compare un avviso su una traccia audio scartata (DTS, E-AC-3 o MP3), quella traccia non c’è nell’MP4: se ti serve, tieni l’originale o usa un altro strumento.

Anche Comprimi video accetta un MKV. Ricodifica in base a un preset di qualità o a una dimensione di destinazione: serve ad alleggerire un file, ma non è una conversione senza ricompressione. L’articolo su come [comprimere un video per l’email](/journal/compress-a-video-for-email/){: hreflang="en"} (in inglese) spiega la dimensione di destinazione. Se invece vuoi un programma gratuito e open source con le impostazioni dell’encoder a vista, leggi il [confronto con HandBrake](/it/alternatives/handbrake/): il suo sito lo presenta come disponibile per Windows, Mac e Linux e tra i contenitori indica .MP4, .MKV e WebM.

### Cosa è gratuito

Comprimi video è uno dei cinque strumenti che restano gratuiti senza limiti di tempo, un file alla volta. Converti funziona gratis nei primi 3 giorni dopo l’installazione, con un’esportazione per esecuzione, poi serve Pro: {P_MONTHLY@mediakit}/mese, {P_YEARLY@mediakit}/anno o {P_LIFETIME@mediakit} a vita. I prezzi indicati sono quelli di App Store in Italia; negli altri paesi App Store mostra il prezzo nella tua valuta al momento dell’acquisto. Se converti un solo file all’anno, uno strumento gratuito come VLC basta.

## Quale metodo scegliere

Decidi prima tra remux e ricodifica. Se vuoi tenere l’immagine così com’è, cerca un’opzione che copi i flussi e controlla che non scarti nessuna traccia audio. Se vuoi un file più leggero, ricodificare è normale, e allora una perdita di qualità è possibile.

VLC e MediaKit non si escludono. VLC resta un lettore gratuito che legge già l’MKV così com’è, e può bastare se vuoi solo guardarlo su un computer. MediaKit serve quando il file deve finire in MP4, MOV o M4V su un iPhone o su un Mac, per esempio per aprirlo nelle app di Apple.

| Esigenza | Strada |
|---|---|
| Un file, senza spendere, sul computer | VLC |
| Un MKV riservato o molto grande, senza caricarlo | VLC o MediaKit |
| Un remux senza ricodificare, su Mac o iPhone | MediaKit, Converti con “Mantieni l’originale (remux)” |
| Alleggerire un file troppo pesante | MediaKit, Comprimi video |
