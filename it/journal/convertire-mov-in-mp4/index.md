---
layout: journal
slug: convertire-mov-in-mp4
permalink: /it/journal/convertire-mov-in-mp4/
local_only: true
last_updated: 2026-11-19
date: 2026-11-19
title: "Come convertire un MOV in MP4 su Mac e iPhone, con o senza ricodifica"
seo:
  title: "Convertire MOV in MP4 su Mac e iPhone con VLC o MediaKit"
  description: "Come convertire MOV in MP4 su Mac o iPhone con un remux o una ricodifica: perché QuickTime Player non basta, i passaggi in VLC e in MediaKit."
  keywords:
    - "convertire mov in mp4"
    - "convertire mov in mp4 gratis"
    - "convertire mov in mp4 mac"
    - "convertire mov in mp4 senza perdere qualità"
    - "convertire mov in mp4 con vlc"
    - "convertire mov in mp4 iphone"
lede: "MOV e MP4 sono due contenitori molto simili, e convertire l’uno nell’altro può ridursi a cambiare l’involucro senza ricomprimere immagine e audio. Qui trovi perché QuickTime Player sul Mac non esporta in MP4, quando basta un remux e quando serve una ricodifica, i passaggi in VLC e come convertire un MOV con MediaKit su Mac e su iPhone."
quick_answer: "Per convertire un MOV in MP4 senza ricomprimerlo serve un remux: video e audio passano in un contenitore MP4 senza essere ricodificati, e funziona solo se i codec sono compatibili con MP4. QuickTime Player non va bene, perché secondo Apple esporta i filmati come .mov e non come MP4. VLC è gratuito e converte dal menu Media, Convert/Save. MediaKit converte sul dispositivo, su Mac e su iPhone, con lo strumento Converti: scegli mp4 alla voce Contenitore e “Mantieni l’originale (remux)” alla voce Codec, che copia i flussi senza ricodificarli quando i codec sono compatibili. Converti funziona gratis nei primi 3 giorni, un file alla volta, poi serve Pro."
excerpt: "Convertire MOV in MP4: cosa cambia tra i due contenitori, perché QuickTime Player non esporta in MP4, remux o ricodifica, VLC e MediaKit su Mac e su iPhone."
faq:
  - q: "Come convertire MOV in MP4 gratis?"
    a: "VLC è gratuito e sa convertire: la sua documentazione descrive la procedura dal menu Media, Convert/Save. In MediaKit lo strumento Converti funziona gratis nei primi 3 giorni dopo l’installazione, con un’esportazione per esecuzione, e poi richiede Pro. Comprimi video resta gratuito, un file alla volta, ma ricodifica il video per alleggerirlo."
  - q: "Si può convertire MOV in MP4 senza perdere qualità?"
    a: "Dipende dai codec. Un remux copia video e audio in un nuovo contenitore senza ricodificarli, quindi non aggiunge una nuova compressione, ma funziona solo se i codec sono compatibili con MP4. In MediaKit è l’opzione “Mantieni l’originale (remux)” dello strumento Converti. Una ricodifica, invece, comprime di nuovo il contenuto, e una perdita di qualità è possibile."
  - q: "Come convertire MOV in MP4 su Mac?"
    a: "Con QuickTime Player non si può: secondo Apple esporta i filmati come filmato QuickTime (.mov), non come video MP4. Puoi usare VLC (Media, Convert/Save) oppure MediaKit: nel Finder fai clic con il tasto destro sul file, scegli “Apri con” e poi MediaKit, quindi lo strumento Converti, mp4 alla voce Contenitore e il codec. MediaKit richiede macOS 14.6 o successivo."
  - q: "Come convertire MOV in MP4 con VLC?"
    a: "Nella documentazione di VLC 3.0 la procedura è questa: Media, Convert/Save, Add, scegli il file, indica il file di destinazione, scegli un profilo di conversione dall’elenco Profile e fai clic su Start. Per sapere che codec contiene il file, la documentazione suggerisce di riprodurlo in VLC e aprire Tools, Codec Information."
  - q: "Come convertire MOV in MP4 su iPhone?"
    a: "MediaKit apre i video su iPhone (iOS 17 o successivo): invia il file all’app dal foglio di condivisione con “Invia a MediaKit” oppure sceglilo da Foto, poi apri lo strumento Converti e scegli mp4 alla voce Contenitore. Per un remux scegli “Mantieni l’originale (remux)” alla voce Codec. MediaKit lavora sul dispositivo, quindi il video non viene caricato su un sito."
mentioned_apps:
  - mediakit
read_time: "6 min di lettura"
---

MOV e MP4 sono due contenitori: involucri che racchiudono video, audio e a volte sottotitoli. Per questo convertire un MOV in MP4 può ridursi a cambiare l’involucro, senza ricodificare né l’immagine né l’audio. Succede solo se i codec contenuti sono compatibili con MP4, ed è questo che separa una conversione senza ricompressione da una che ricomprime il file. Sotto trovi il confronto tra QuickTime Player, VLC e [MediaKit](/it/apps/mediakit/), un’app di Lagerland Apps, lo studio che pubblica questo sito.

## Cosa cambia tra MOV e MP4

Il nome tecnico del formato MP4 è MPEG-4 Part 14. La [voce di Wikipedia in italiano](https://it.wikipedia.org/wiki/MPEG-4_Part_14) spiega che deriva da uno standard ISO che a sua volta si basa direttamente sul formato dei file QuickTime, quello dei .mov. Per questo la voce lo definisce “essenzialmente identico al formato QuickTime”, con in più il supporto formale per alcune caratteristiche MPEG.

Il contenitore, però, è solo l’involucro. Dentro ci sono un codec per il video e uno per l’audio, e anche da quelli dipende se un lettore o un’app riesce a leggere il file. Cambiare contenitore non tocca il contenuto; cambiare codec obbliga a decodificare e ricodificare.

## Perché QuickTime Player non esporta in MP4

Su Mac viene in mente subito QuickTime Player, ma la guida Apple per [esportare i filmati](https://support.apple.com/it-it/guide/quicktime-player/qtp20e395859/mac) dice che i filmati vengono esportati come filmato QuickTime (.mov) con codec H.264 o HEVC e che QuickTime Player non può esportarli come video MP4. Il menu Esporta propone risoluzioni diverse e, per 4K e 1080p, la scelta tra HEVC e H.264: cambia la codifica, non il contenitore.

## Remux o ricodifica

La documentazione di VLC definisce il [remux](https://docs.videolan.me/vlc-user/desktop/3.0/en/advanced/streaming/remuxing.html){: hreflang="en"} (in inglese) come l’operazione che prende i flussi già codificati e li mette in un contenitore diverso. Lo distingue dalla transcodifica, che invece ricodifica. Il remux cambia solo il contenitore, è molto più veloce perché non c’è nulla da codificare e lascia la dimensione del file quasi uguale.

La stessa pagina pone una condizione: poiché non si ricodifica, i codec originali devono essere compatibili con il nuovo contenitore, altrimenti il remux non riesce. Per sapere che codec contiene il tuo MOV, la documentazione suggerisce di riprodurlo in VLC e aprire Tools, Codec Information.

Una ricodifica, invece, comprime di nuovo il contenuto. È quello che succede quando comprimi fino a una dimensione di destinazione o passi a un altro codec. Serve quando il remux non è possibile o quando vuoi un file più piccolo, ma ricomprimendo si può perdere qualità.

## Se il problema è il codec, non il contenitore

A volte un video non si apre su un altro dispositivo per via del codec. Nella pagina sull’uso dei [file multimediali in formato HEIF o HEVC](https://support.apple.com/it-it/116944), Apple spiega che HEVC comprime meglio di H.264 e che sui dispositivi meno recenti il suo supporto può dipendere dalla risoluzione e dalla frequenza dei fotogrammi. Aggiunge che, nelle impostazioni dell’iPhone, alla voce Fotocamera, Formati, l’opzione “Più compatibile” registra i nuovi video in H.264. Se il problema è il codec, cambiare solo l’involucro può non bastare e serve una ricodifica.

## Convertire MOV in MP4 con VLC

VLC è gratuito. Il [sito di VideoLAN](https://www.videolan.org/vlc/){: hreflang="en"} (in inglese) lo presenta come un lettore multimediale open source. Per convertire, la [documentazione di VLC 3.0](https://docs.videolan.me/vlc-user/desktop/3.0/en/basic/tipsandtricks/index.html){: hreflang="en"} (in inglese) indica questi passaggi: scegli Media, Convert/Save, fai clic su Add e seleziona il file, indica il file di destinazione, scegli un profilo di conversione dall’elenco Profile e fai clic su Start. I nomi delle voci sono quelli della documentazione in inglese.

Il [wiki di VideoLAN sulla transcodifica](https://wiki.videolan.org/Transcode/){: hreflang="en"} (in inglese) descrive una procedura guidata che chiede un codec video, un codec audio e un contenitore. Fra i suoi esempi da riga di comando ce n’è uno che porta un file .mov in un MP4 ricodificandolo in H.264 (e ruotando l’immagine). Il wiki aggiunge che non serve transcodificare se i flussi di ingresso hanno già il codec che vuoi, avverte che la pagina non è aggiornata e ricorda che una transcodifica può essere molto lenta.

Per controllare il risultato, riproducilo in VLC e apri di nuovo Tools, Codec Information. Se usi già VLC, fa il lavoro sul computer senza spendere nulla.

## I convertitori online

Un convertitore online riceve il tuo file sui suoi server, lo converte e te lo rimanda. Con un video lungo significa caricarlo per intero prima di cominciare, e il contenuto lascia il tuo dispositivo. Due pagine di questo sito approfondiscono il compromesso: l’articolo su [cosa succede ai tuoi file in un convertitore online](/journal/your-photos-shouldnt-ride-the-elevator/){: hreflang="en"} (in inglese) e il [confronto con CloudConvert](/it/alternatives/cloudconvert/).

## Convertire MOV in MP4 con MediaKit

MediaKit è un’app per iPhone e Mac che lavora sul dispositivo: il file non viene mandato da nessuna parte. Lo strumento Converti porta un video in MP4, MOV o M4V, con H.264, HEVC o ProRes come codec. ProRes viene scritto in .mov, quindi per ricodificare in MP4 restano H.264 e HEVC. Gli altri strumenti video compaiono nell’articolo sugli [strumenti multimediali che il Mac ha già](/journal/every-media-tool-already-on-your-mac/){: hreflang="en"} (in inglese).

Su Mac (macOS 14.6 o successivo), nel Finder fai clic con il tasto destro sul file MOV, scegli “Apri con” e poi MediaKit.

Su iPhone (iOS 17 o successivo) invia il file a MediaKit dal foglio di condivisione, con “Invia a MediaKit”. Puoi anche scegliere il video da Foto e salvare il risultato in Foto.

In entrambi i casi:

1. Scegli lo strumento Converti.
2. Alla voce Contenitore scegli mp4.
3. Per un remux, alla voce Codec scegli “Mantieni l’originale (remux)”: i flussi passano nel nuovo contenitore senza essere ricodificati, quando i codec sono compatibili. Le altre opzioni ricodificano.
4. Tocca Esegui (sul Mac, fai clic).

Per alleggerire un video c’è Comprimi video, che ricodifica in base a un preset di qualità o a una dimensione di destinazione: serve a ridurre il peso più che a cambiare il contenitore. L’articolo su come [comprimere un video per l’email](/journal/compress-a-video-for-email/){: hreflang="en"} (in inglese) spiega la dimensione di destinazione. Se preferisci un programma gratuito e open source per il computer, leggi il [confronto con HandBrake](/it/alternatives/handbrake/): il suo sito lo presenta come disponibile per Windows, Mac e Linux e tra i contenitori indica .MP4, .MKV e WebM. Se il file di partenza è un MKV, c’è l’articolo su come [convertire MKV in MP4](/it/journal/convertire-mkv-in-mp4/).

### Cosa è gratuito

Comprimi video è uno dei cinque strumenti che restano gratuiti senza limiti di tempo, un file alla volta. Converti funziona gratis nei primi 3 giorni dopo l’installazione, con un’esportazione per esecuzione; poi serve Pro: {P_MONTHLY@mediakit}/mese, {P_YEARLY@mediakit}/anno o {P_LIFETIME@mediakit} a vita. I prezzi indicati sono quelli di App Store in Italia; negli altri paesi App Store mostra il prezzo nella tua valuta al momento dell’acquisto. Per un solo file all’anno, uno strumento gratuito come VLC è sufficiente.

## Quale metodo scegliere

Decidi prima tra remux e ricodifica. Se vuoi tenere l’immagine così com’è, cerca un’opzione che copi i flussi e controlla che i codec siano compatibili con MP4. Se vuoi un file più leggero, la ricodifica è la strada normale, con una possibile perdita di qualità.

| Esigenza | Strada |
|---|---|
| Un file, senza spendere, sul computer | VLC |
| Un video riservato o molto lungo, senza caricarlo | VLC o MediaKit |
| Un remux senza ricodificare, su Mac o iPhone | MediaKit, Converti con “Mantieni l’originale (remux)” |
| Alleggerire un file troppo pesante | MediaKit, Comprimi video |
| Esportare in MP4 da QuickTime Player | Non è possibile: esporta solo .mov |
