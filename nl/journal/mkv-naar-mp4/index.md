---
layout: journal
slug: mkv-naar-mp4
permalink: /nl/journal/mkv-naar-mp4/
local_only: true
last_updated: 2026-11-19
date: 2026-11-19
title: "MKV naar MP4: remuxen zonder kwaliteitsverlies, met VLC, online of MediaKit"
seo:
  title: "MKV naar MP4 converteren: VLC, online of MediaKit"
  description: "MKV naar MP4 op Mac of iPhone: remuxen zonder kwaliteitsverlies of hercoderen, gratis met VLC, via een online converter of op je apparaat met MediaKit."
  keywords:
    - "mkv naar mp4"
    - "mkv naar mp4 converteren"
    - "mkv naar mp4 gratis"
    - "mkv naar mp4 omzetten"
    - "mkv converteren naar mp4 gratis"
    - "mkv mp4 converter"
lede: "Een MKV-bestand is een container met video, geluid en ondertitels, dus een MKV naar MP4 omzetten kan neerkomen op een andere verpakking, zonder dat het beeld wordt aangeraakt. Dit artikel legt het verschil tussen remuxen en hercoderen uit, laat zien wat VLC kan, wat een online converter betekent voor een groot bestand en hoe MediaKit een MKV op de Mac en de iPhone opent, met de geluidsformaten die meegaan en die wegvallen."
quick_answer: "Om een MKV zonder kwaliteitsverlies naar MP4 om te zetten heb je een remux nodig: video en geluid gaan zonder hercodering in een MP4-container, en dat kan alleen met codecs die in MP4 passen. VLC is gratis en kan converteren (menu Media, Convert/Save). Een online converter vraagt je het hele bestand te uploaden. MediaKit remuxt een MKV op je apparaat, op de Mac en de iPhone: H.264, HEVC, AAC en AC-3 gaan ongewijzigd mee, maar DTS-, E-AC-3- en MP3-geluid vervalt, met een melding. ‘Converteer’ is de eerste 3 dagen gratis en daarna alleen met Pro; ‘Video comprimeren’ blijft gratis en maakt van een MKV een MP4 door te hercoderen."
excerpt: "MKV naar MP4 omzetten: wat een container is, remuxen of hercoderen, VLC en online converters voor een groot bestand, en hoe MediaKit een MKV op de Mac en de iPhone opent en converteert."
faq:
  - q: "Hoe zet je een MKV gratis om naar MP4?"
    a: "VLC is gratis en kan converteren: de VideoLAN-wiki beschrijft een wizard die je opent via het menu Media, opdracht Convert/Save. In MediaKit blijft de tool ‘Video comprimeren’ ook na de eerste 3 dagen gratis, één bestand tegelijk, en die maakt van een MKV een MP4. Omdat de tool hercodeert, is het geen conversie zonder kwaliteitsverlies. De tool ‘Converteer’, die remuxt, is de eerste 3 dagen gratis en daarna alleen beschikbaar met Pro."
  - q: "Kun je een MKV zonder kwaliteitsverlies naar MP4 omzetten?"
    a: "Ja, als de codecs het toelaten: een remux kopieert video en geluid zonder hercodering naar een nieuwe container. Zo remuxt MediaKit een MKV met H.264- of HEVC-video en AAC- of AC-3-geluid. DTS-, E-AC-3- of MP3-geluid uit een MKV vervalt, met een melding."
  - q: "Hoe zet je een MKV met VLC om naar MP4?"
    a: "De VideoLAN-wiki, die zelf zegt dat de pagina verouderd is, beschrijft een wizard die je opent via het menu Media, opdracht Convert/Save, waar je een videocodec, een audiocodec en een container kiest. Volgens de wiki kan transcoderen erg traag zijn en hoef je niet te transcoderen als de sporen al de gewenste codec hebben. Omdat de pagina verouderd is, geldt voor de precieze stappen de documentatie van je versie van VLC."
  - q: "Welke online converter kun je gebruiken voor een groot MKV-bestand?"
    a: "Elke online converter ontvangt het bestand op zijn servers voordat hij het omzet, dus een groot MKV-bestand moet je helemaal uploaden. Een conversie op je eigen apparaat, met VLC of MediaKit, voorkomt die upload."
  - q: "Hoe zet je een MKV om naar MP4 op de iPhone?"
    a: "MediaKit opent MKV-bestanden op de iPhone (iOS 17 of later) en heeft de tool ‘Converteer’, die MP4, MOV of M4V maakt. Kies voor een remux de optie ‘Origineel behouden (remux)’: MediaKit kopieert dan de H.264- of HEVC-video en het AAC- of AC-3-geluid zonder hercodering. DTS-, E-AC-3- of MP3-geluid vervalt, met een melding."
  - q: "Hoe zet je een MKV om naar MP4 op de Mac?"
    a: "Klik in de Finder met de rechtermuisknop op het MKV-bestand, kies ‘Open met’ en daarna MediaKit, dat in die lijst voor MKV-bestanden staat. Kies vervolgens ‘Converteer’, het formaat MP4 en ‘Origineel behouden (remux)’. MediaKit vereist macOS 14.6 of later."
mentioned_apps:
  - mediakit
read_time: "6 min lezen"
---

Een MKV-bestand is een container waarin videosporen, geluidssporen en ondertitels samen zitten. Een MKV naar MP4 omzetten kan daarom neerkomen op het verwisselen van de verpakking, zonder het beeld of het geluid opnieuw te coderen en dus zonder kwaliteitsverlies. Dat lukt alleen als de codecs in het bestand in een MP4-container passen. Daar zit het verschil tussen een conversie zonder verlies en een conversie die het bestand slechter maakt. Dit artikel begint bij dat verschil en vergelijkt daarna VLC, online converters en [MediaKit](/nl/apps/mediakit/).

## Wat is een MKV en wat is het verschil met MP4?

Het Matroska-project, dat het formaat ontwikkelt, schrijft op zijn site dat een container [geen compressieformaat voor video of audio is](https://www.matroska.org/what_is_matroska.html){: hreflang="en"} (in het Engels). Het noemt een container een envelop waarin meerdere audio-, video- en ondertitelstreams kunnen zitten, zodat je een hele film in één bestand kunt bewaren. Het project wil van Matroska ook het opensource-alternatief maken voor bestaande containers als AVI, MOV en MP4. MP4 is dus zelf ook een container.

Twee bestanden kunnen dus hetzelfde beeld en hetzelfde geluid hebben en alleen in de envelop verschillen. De envelop wisselen kan zonder aan de inhoud te komen. Wissel je van codec, dan moet je decoderen en daarna opnieuw coderen.

## Waarom een MKV niet altijd opent op je iPhone of Mac

Apple legt dat uit op een supportpagina over [mediabestanden die niet openen of afspelen](https://support.apple.com/nl-nl/102644). Apps van Apple zoals Foto’s, iMovie, Safari, Keynote en QuickTime Player werken met veel mediastructuren, maar oudere of gespecialiseerde structuren werken mogelijk niet zoals verwacht als je apparaat, het besturingssysteem of de app ze niet ondersteunt. Om een andere app te vinden die de structuur wel ondersteunt, stelt Apple voor te zoeken op de bestandsnaamextensie en noemt als voorbeelden .avi, .wmv en .mkv. Op een Mac kun je de structuur mogelijk herkennen door het bestand in de Finder te selecteren en op Command-I te drukken: het informatievenster toont dan soms ‘Soort: Matroska-videobestand’.

## Remuxen of hercoderen: wanneer verlies je niets?

Een remux zet de video- en geluidssporen van de ene container over naar de andere, zonder ze te decoderen. In MediaKit is dat de optie ‘Origineel behouden (remux)’ in de tool ‘Converteer’. Het bestand wordt niet opnieuw gecomprimeerd, dus het beeld blijft precies zoals het was.

Een remux werkt alleen als de MP4 de codecs van het bestand kan dragen. In MediaKit gaan H.264- en HEVC-video en AAC- en AC-3-geluid ongewijzigd mee. DTS-, E-AC-3- en MP3-geluid uit een MKV vervalt, met een melding: de video blijft, die geluidssporen niet. Heeft je film een DTS-spoor, lees dan de melding over vervallen geluid.

Hercoderen levert een nieuwe compressie op. Dat gebeurt als je naar een doelgrootte comprimeert of een andere codec kiest. Het is nuttig als een remux niet kan of als je een kleiner bestand wilt, maar het kost een deel van de kwaliteit.

## MKV naar MP4 met VLC

VLC is gratis. De [site van VideoLAN](https://www.videolan.org/vlc/){: hreflang="en"} (in het Engels) noemt het een gratis en opensource mediaspeler en rekent MKV tot de formaten die hij afspeelt. Voor het converteren beschrijft de VideoLAN-wiki, op een [pagina over transcoderen](https://wiki.videolan.org/Transcode/){: hreflang="en"} (in het Engels), een wizard die je opent via het menu Media, opdracht Convert/Save. De wizard vraagt om een videocodec, een audiocodec en een container. Op dezelfde pagina staat dat je niet hoeft te transcoderen als je invoersporen al de gewenste codec hebben. De schrijver denkt, maar weet het niet zeker, dat die optie in de interface ‘keep the original track’ heet. De wiki waarschuwt verder dat de pagina verouderd is en dat transcoderen erg traag kan zijn. Voor de precieze stappen geldt de documentatie van je versie van VLC.

Gebruik je VLC al op je computer, dan converteer je zonder iets uit te geven. De iPhone-versie van VLC behandelt dit artikel niet.

## Online converters en grote bestanden

Een online converter ontvangt je bestand op zijn servers, zet het om en stuurt het terug. Bij een groot MKV-bestand moet je het dus eerst helemaal uploaden, en de inhoud verlaat je apparaat. Twee pagina’s op deze site gaan dieper in op die afweging: het artikel over [HEIC-foto’s converteren zonder ze naar een server te sturen](/journal/your-photos-shouldnt-ride-the-elevator/){: hreflang="en"} (in het Engels) en de [vergelijking met CloudConvert](/alternatives/cloudconvert/){: hreflang="en"} (in het Engels).

## MKV naar MP4 met MediaKit

MediaKit is een app voor iPhone en Mac die op je apparaat werkt, dus het bestand gaat nergens naartoe. MediaKit is van Lagerland Apps, dat ook deze site maakt. De app opent MKV-bestanden rechtstreeks, omdat de app ze zelf uitpakt, en heeft nog meer videotools. Die staan in het artikel over [de mediatools van MediaKit op de Mac](/journal/every-media-tool-already-on-your-mac/){: hreflang="en"} (in het Engels).

Op de Mac (macOS 14.6 of later) klik je in de Finder met de rechtermuisknop op het MKV-bestand, kies je ‘Open met’ en daarna MediaKit, dat in die lijst voor MKV-bestanden staat. Je kunt het bestand ook op het MediaKit-icoon in het Dock slepen.

Op de iPhone (iOS 17 of later) open je MediaKit en kies je het bestand in de Bestanden-app.

Daarna doe je op beide apparaten hetzelfde:

1. Kies de tool ‘Converteer’.
2. Kies MP4 als uitvoerformaat (MOV en M4V kunnen ook).
3. Kies voor een remux ‘Origineel behouden (remux)’ als codec. De andere opties, H.264, HEVC en ProRes, hercoderen.
4. Tik of klik op ‘Voer uit’ en lees de melding over vervallen geluid, als die verschijnt.

Staat er in de melding dat geluid vervalt, dan zit dat spoor niet in de MP4. Was het je enige geluidsspoor, dan heeft het geconverteerde bestand geen geluid. Heb je dat spoor nodig, bewaar dan het origineel of gebruik een andere tool.

De tool ‘Video comprimeren’ accepteert ook een MKV. Bronnen in MP4, MOV en M4V behouden hun container en alle andere worden MP4. De tool hercodeert volgens een kwaliteitsinstelling of een doelgrootte. Dat is handig om een bestand kleiner te maken, maar het is geen conversie zonder verlies. Het artikel over [een video comprimeren om te mailen](/journal/compress-a-video-for-email/){: hreflang="en"} (in het Engels) legt de doelgrootte uitgebreid uit.

### Wat is gratis?

‘Video comprimeren’ is een van de vijf tools die zonder tijdslimiet gratis blijven, één bestand tegelijk. ‘Converteer’ werkt de eerste 3 dagen na installatie gratis, met één export per keer, en vraagt daarna Pro: {P_MONTHLY@mediakit} per maand, {P_YEARLY@mediakit} per jaar of {P_LIFETIME@mediakit} eenmalig (prijzen van de Nederlandse App Store). Zet je maar één bestand per jaar om, dan kan een gratis converter als VLC genoeg zijn.

## Welke methode past bij je?

De eerste keuze is die tussen remuxen en hercoderen. Wil je het beeld houden zoals het is, kies dan een optie die de sporen kopieert en controleer of er geen geluidsspoor wegvalt. Wil je een lichter bestand, dan hercodeer je en accepteer je wat verlies.

VLC en MediaKit sluiten elkaar niet uit. VLC is een gratis speler die een MKV al afspeelt zoals hij is, wat genoeg kan zijn als je de video alleen op een computer wilt bekijken. MediaKit past als het bestand een MP4, MOV of M4V moet worden op een iPhone of Mac, bijvoorbeeld om het in apps van Apple te openen.

| Wat je nodig hebt | Keuze |
|---|---|
| Eén bestand, gratis, op de computer | VLC |
| Een gevoelig of heel groot MKV-bestand, zonder upload | VLC of MediaKit |
| Een remux zonder hercodering, op de Mac of de iPhone | MediaKit, ‘Converteer’, ‘Origineel behouden (remux)’ |
| Een te zwaar bestand kleiner maken | MediaKit, ‘Video comprimeren’ |
