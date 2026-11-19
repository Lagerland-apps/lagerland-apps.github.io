---
layout: journal
slug: compress-a-video-for-email
ref: /journal/compress-a-video-for-email/
permalink: /nl/journal/compress-a-video-for-email/
translated_from: 2026-11-08
last_updated: 2026-11-19
date: 2026-11-19
title: "Video verkleinen voor mail: de limieten en de bitrate berekenen"
seo:
  title: "Video verkleinen voor mail: limieten en bitrate berekenen"
  description: "Video verkleinen voor mail: Gmail neemt 25 MB, Outlook en iCloud Mail 20 MB. Waarom je eronder mikt, welke bitrate past en hoe het op iPhone of Mac gaat."
  keywords:
    - "video verkleinen voor mail"
    - "video verkleinen voor mail gratis"
    - "video verkleinen voor mail iphone"
    - "grote video versturen via mail"
    - "grote video versturen iphone"
    - "te grote video versturen"
    - "video comprimeren voor mail"
    - "grote video bestanden versturen"
lede: "Elke mailprovider stelt een grens aan wat hij doorstuurt, en een video zit daar snel aan. Dit artikel noemt de limieten die Gmail, Outlook en iCloud Mail publiceren, legt uit waarom een limiet van 25 MB geen bestand van 25 MB toelaat, laat de som zien die van een doelgrootte een bitrate maakt en beschrijft hoe MediaKit die berekening op iPhone of Mac uitvoert zonder de video te uploaden."
quick_answer: "Om een video te mailen moet het bestand kleiner zijn dan de limiet van je provider, met ruimte over. Een persoonlijke Gmail-account neemt 25 MB aan bijlagen, de Outlook-app 20 MB per bericht bij internetaccounts zoals Outlook.com, iCloud Mail 20 MB en zakelijke Exchange-accounts standaard 10 MB. Bijlagen reizen Base64-gecodeerd, wat volgens Microsoft zo’n 33% toevoegt. Mik dus op ongeveer driekwart van de limiet: rond 18 MB voor Gmail en 15 MB voor Outlook of iCloud Mail. Voor de bitrate vermenigvuldig je de doelgrootte in megabyte met 8000 en deel je door de lengte van de video in seconden. Dat is het totaal in kbps. Trek daar de audiobitrate af (128 kbps is gebruikelijk) en wat overblijft is het budget voor het beeld. Verlaag de resolutie tot dat budget past, houd H.264 aan zodat de video overal speelt en stuur een link als het budget te klein wordt: Mail Drop verstuurt tot 5 GB."
excerpt: "Een naslagwerk voor het mailen van video: de bijlagelimieten van Gmail, Outlook, Exchange, iCloud Mail en Mail Drop, waarom Base64-codering betekent dat je op driekwart van de limiet mikt, een bitratetabel voor video’s van 30 seconden tot 5 minuten en hoe de modus ‘Doelgrootte’ van MediaKit dezelfde berekening uitvoert op iPhone en Mac."
faq:
  - q: "Hoe groot mag een video zijn die je met Gmail mailt?"
    a: "Een persoonlijke Gmail-account kan in één bericht tot 25 MB aan bijlagen versturen, alle bijlagen bij elkaar opgeteld. Voor zakelijke en schoolaccounts gelden de limieten die de beheerder van Google Workspace instelt. Boven de limiet haalt Gmail de bijlage weg en voegt hij die toe als link naar Google Drive. Omdat bijlagen onderweg Base64-gecodeerd zijn, mik je op een video van ongeveer 18 MB als die echt als bijlage moet aankomen."
  - q: "Waarom komt mijn video terug terwijl hij onder de bijlagelimiet zit?"
    a: "Daar zijn drie veelvoorkomende oorzaken voor. Bijlagen worden Base64-gecodeerd voordat ze worden verstuurd, en volgens de Exchange-documentatie van Microsoft komt daar zo’n 33% bij, dus een bestand vlak onder de limiet kan er na het coderen overheen gaan. Sommige limieten gelden voor het hele bericht en niet alleen voor de bijlage: Microsoft schrijft dat de limiet van 20 MB bij Outlook ook voor de e-mail zelf geldt. En de server van de ontvanger heeft een eigen limiet, die lager kan zijn dan die van jou, zoals de 10 MB die Exchange standaard hanteert."
  - q: "Hoe bereken je de bitrate voor een bepaalde bestandsgrootte?"
    a: "Vermenigvuldig de doelgrootte in megabyte met 8000 om kilobit te krijgen en deel dat door de lengte van de video in seconden. Dat geeft de totale bitrate in kbps. Trek daar de audiobitrate van af en wat overblijft is de videobitrate. Voor een doel van 18 MB en een video van 90 seconden: 18 × 8000 = 144.000 kilobit, gedeeld door 90 is 1600 kbps, min 128 kbps voor het geluid blijft ongeveer 1470 kbps over voor het beeld."
  - q: "Kies je H.264 of HEVC voor een video die je mailt?"
    a: "H.264 in een MP4, tenzij je weet dat de ontvanger een recent Apple-apparaat heeft. Apple schrijft dat HEVC beter comprimeert dan H.264, dus een HEVC-bestand ziet er bij dezelfde grootte beter uit. Maar je bepaalt niet waarop de bijlage wordt geopend, en H.264 is het formaat dat bijna alles afspeelt. Heeft de ontvanger een actuele iPhone, iPad of Mac, dan levert HEVC extra kwaliteit bij dezelfde grootte."
  - q: "Wat als mijn video te lang is om klein genoeg te maken?"
    a: "Stuur een link. Mail Drop in Mail en iCloud Mail verstuurt bestanden tot 5 GB als downloadlink die na 30 dagen verloopt, en Mail biedt het aan als een bericht te groot is voor je provider. Gmail vervangt een te grote bijlage uit zichzelf door een link naar Google Drive. Een video van vijf minuten die je in 15 MB perst, laat ongeveer 270 kbps over voor het beeld, een kwart van wat YouTube zelfs voor uploads in 360p aanbeveelt."
  - q: "Kan MediaKit een video verkleinen tot een bepaalde bestandsgrootte?"
    a: "Ja. ‘Video comprimeren’ heeft een modus ‘Doelgrootte’ waarvoor je een getal invult in KB, MB of GB. MediaKit deelt de doelgrootte door de lengte van de video, haalt de audiobitrate eraf die je koos, houdt 3% in reserve, codeert, meet het bestand dat daaruit komt en codeert opnieuw met een gecorrigeerde bitrate als het doel gemist is. Lukt het dan nog niet om onder de doelgrootte te blijven, dan stopt de app met een foutmelding in plaats van je een te groot bestand te geven. MediaKit werkt op het apparaat, op iPhone en Mac, en ‘Video comprimeren’ is een van de vijf tools die na de eerste 3 dagen voorgoed gratis blijven."
mentioned_apps:
  - mediakit
read_time: "7 min lezen"
---

Bij de 8 Mbps die YouTube voor uploads in 1080p aanbeveelt, is één minuut video 60 MB. Dat is ruim twee keer zoveel als Gmail als bijlage toelaat. Een video in een mail krijgen is een kleine som: kies een doelgrootte onder de limiet van je provider, reken de bitrate uit die daarbij past en codeer de video opnieuw met die bitrate. Dit artikel geeft de getallen voor elke stap en laat daarna zien hoe [MediaKit](/nl/apps/mediakit/) dit op iPhone en Mac doet, zonder de video eerst ergens naartoe te sturen.

## Hoe groot mag een video zijn die je mailt?

| Dienst | Limiet | Wat meetelt | Boven de limiet |
|---|---|---|---|
| Gmail, persoonlijke account | 25 MB | Alle bijlagen in het bericht bij elkaar | Gmail vervangt de bijlage door een link naar Google Drive |
| Outlook-app, internetaccounts zoals Outlook.com | 20 MB | De bijlagen plus de e-mail zelf | Microsoft raadt aan te comprimeren of een link naar cloudopslag te delen |
| Exchange, zakelijke accounts | Standaard 10 MB | Het hele bericht; beheerders kunnen de limiet aanpassen | Zoals hierboven |
| iCloud Mail | 20 MB | Inkomende en uitgaande berichten | Tot 5 GB met Mail Drop ingeschakeld |
| Mail Drop (Mail, iCloud Mail) | 5 GB | Het bericht inclusief bijlagen; elke link verloopt na 30 dagen | Mail Drop kan het niet versturen |

De limieten staan zo op de helppagina van elke provider (stand juli 2026): [Gmail Help](https://support.google.com/mail/answer/6584?hl=nl), [Microsoft Support](https://support.microsoft.com/nl-nl/office/grote-bestanden-verzenden-met-outlook-8c698842-b462-4a4c-8d53-5c5dd04f77ef) en de pagina’s van Apple over de [limieten van iCloud Mail](https://support.apple.com/nl-nl/102198) en [Mail Drop](https://support.apple.com/nl-nl/108329). Zakelijke en schoolaccounts kunnen door beheerders lager zijn ingesteld, en de ontvangende server past een eigen limiet toe. Volgens de [Exchange-documentatie](https://learn.microsoft.com/en-us/exchange/mail-flow/message-size-limits){: hreflang="en"} (in het Engels) van Microsoft moet een bericht binnen de limieten van zowel afzender als ontvanger vallen, dus de laagste limiet op de route beslist.

## Waarom een limiet van 25 MB geen bestand van 25 MB toelaat

E-mail is een tekstformaat. Voordat een video als bijlage kan reizen, wordt hij Base64-gecodeerd: elke drie bytes van het bestand worden vier tekens tekst, verdeeld over regels van hoogstens 76 tekens ([RFC 2045, paragraaf 6.8](https://www.rfc-editor.org/rfc/rfc2045#section-6.8){: hreflang="en"} (in het Engels)). Het bericht dat over het netwerk gaat, is ongeveer een derde groter dan het bestand op je schijf.

Of een limiet vóór of na die codering wordt gemeten, verschilt, en de helppagina’s voor consumenten zeggen het zelden. De Exchange-documentatie van Microsoft wel: Base64 voegt zo’n 33% toe, dus bij een berichtlimiet van 64 MB is het realistische maximum ongeveer 48 MB. De Outlook-pagina voegt eraan toe dat de limiet van 20 MB ook voor de e-mail zelf geldt, niet alleen voor de bijlage.

Mik daarom op driekwart van de genoemde limiet:

| Genoemde limiet | Mik op een bestand van ongeveer |
|---|---|
| 25 MB (Gmail) | 18 MB |
| 20 MB (Outlook, iCloud Mail) | 15 MB |
| 10 MB (standaard bij Exchange) | 7,5 MB |

Te laag mikken kost wat beeldkwaliteit. Te hoog mikken betekent dat het bericht terugkomt, of dat je een link krijgt waar je een bijlage wilde.

## Zo bereken je de bitrate die past

De bestandsgrootte is de bitrate maal de duur. Reken dat terug:

1. **Zet de doelgrootte om in kilobit.** Megabyte × 8000, waarbij een megabyte 1.000.000 bytes is.
2. **Deel door de lengte van de video in seconden.** Dat is de totale bitrate in kbps.
3. **Trek het geluid eraf.** 128 kbps is een gangbare stereo-instelling; 64 kbps is ruim genoeg voor spraak.
4. **Wat overblijft is de videobitrate.** Houd een paar procent over voor de overhead van de container zelf.

Een video van 90 seconden voor Gmail: 18 MB × 8000 = 144.000 kilobit. Gedeeld door 90 seconden is dat 1600 kbps. Min 128 kbps voor het geluid blijft ongeveer 1470 kbps over voor het beeld.

Dezelfde som voor gangbare lengtes, met 128 kbps voor het geluid er al af:

| Lengte van de video | Bestand van 7,5 MB | Bestand van 15 MB | Bestand van 18 MB |
|---|---|---|---|
| 30 seconden | 1870 kbps | 3870 kbps | 4670 kbps |
| 1 minuut | 870 kbps | 1870 kbps | 2270 kbps |
| 2 minuten | 370 kbps | 870 kbps | 1070 kbps |
| 5 minuten | 70 kbps | 270 kbps | 350 kbps |

De getallen zijn naar beneden afgerond.

## Welke resolutie en codec je kiest

Een bitrate is pas ruim of krap in verhouding tot het beeld dat hij moet vullen. Ter vergelijking: de [aanbevolen uploadinstellingen](https://support.google.com/youtube/answer/1722171?hl=nl) van YouTube voor standaard beeldsnelheden vragen om 8 Mbps bij 1080p, 5 Mbps bij 720p, 2,5 Mbps bij 480p en 1 Mbps bij 360p. Die cijfers zijn hoog, omdat YouTube alles opnieuw codeert wat het ontvangt, maar ze laten zien hoe snel de behoefte daalt met de beeldgrootte: 1080p heeft 2,25 keer zoveel pixels als 720p.

Een vuistregel: zit je videobudget ruim onder de helft van het YouTube-cijfer voor de resolutie van de video, ga dan een resolutie omlaag. Volgens die regel past een video van een minuut bij 18 MB (2270 kbps) beter bij 720p dan bij 1080p, en hoort hij bij 7,5 MB (870 kbps) bij 480p of lager. Drie andere instellingen veranderen het resultaat:

- **Audiobitrate.** Bij een video waarin iemand rechtstreeks in de camera praat, geeft 64 kbps in plaats van 128 kbps het verschil aan het beeld. Bij een video van vijf minuten in 15 MB is dat bijna een kwart meer videobitrate.
- **Beeldsnelheid.** Een video van 60 fps verdeelt zijn bits over twee keer zoveel beelden als een video van 30 fps. De cijfers van YouTube voor 48 tot 60 fps liggen ongeveer de helft hoger dan die voor 24 tot 30.
- **Codec.** Apple schrijft dat [HEVC beter comprimeert dan H.264](https://support.apple.com/nl-nl/116944), en recente Apple-apparaten spelen het af. Maar je bepaalt niet waarop de bijlage wordt geopend, en H.264 in een MP4 speelt bijna overal. Apple merkt ook op dat zijn apparaten HEVC *mogelijk* automatisch naar H.264 omzetten als je deelt met een apparaat dat HEVC niet afspeelt. Voor een bestand dat je al hebt gecomprimeerd, is het eenvoudiger zelf voor H.264 te kiezen.

## Wanneer je beter een link stuurt

De rij van vijf minuten in de tabel is het punt waarop comprimeren niet meer helpt: 270 kbps is ongeveer een kwart van wat YouTube voor 360p aanraadt. Valt het budget zo laag, dan heeft de ontvanger meer aan een link dan aan een bijlage.

- **Mail Drop** in Mail en iCloud Mail verstuurt bestanden tot 5 GB als downloadlink die na 30 dagen verloopt. Mail biedt het aan als een bericht groter is dan je provider toestaat.
- **Gmail** vervangt een bijlage van meer dan 25 MB uit zichzelf door een link naar Google Drive.
- **Outlook** verwijst je naar comprimeren of naar delen vanuit cloudopslag.

Met een link krijgt de ontvanger het origineel in volle kwaliteit, en blijft er een kopie op een server staan zolang de link werkt.

## Zo doe je het in MediaKit

[MediaKit](/nl/apps/mediakit/) doet de berekening hierboven op het apparaat, op iPhone en op Mac, en uploadt de video nooit. ‘Video comprimeren’ is een van de vijf tools die na de eerste 3 dagen voorgoed gratis blijven, voor één bestand tegelijk.

1. **Open de video.** Sleep hem op de Mac naar het venster. Voeg hem op de iPhone toe vanuit Foto’s of Bestanden, of stuur hem vanuit het deelmenu van een andere app.
2. **Kies de tool ‘Video comprimeren’** en zet ‘Modus’ op ‘Doelgrootte’.
3. **Vul de doelgrootte in** uit de tabel met driekwart van de limiet, bijvoorbeeld 18, met de eenheid op MB. MediaKit rekent een megabyte als 1.000.000 bytes.
4. **Open ‘Geavanceerd’.** Stel ‘Max. resolutie’ in aan de hand van de bitratetabel, laat ‘Codec’ voor mail op H.264 staan en kies bij ‘Audiobitrate’ de optie ‘64 kbps (spraak)’ als de video vooral uit spraak bestaat.
5. **Kies ‘Voer uit’ en controleer de grootte** van het resultaat voordat je het bijvoegt.

In de modus ‘Doelgrootte’ doet MediaKit stap 1 tot 4 van de som zelf. De app deelt de doelgrootte door de lengte van de video, haalt de gekozen audiobitrate eraf en houdt 3% in reserve, codeert, meet het bestand dat daaruit komt en codeert opnieuw met een gecorrigeerde bitrate als het doel gemist is. Je krijgt nooit een bestand dat groter is dan de doelgrootte: lukt dat niet, dan stopt de app met een foutmelding. Een bron in 4K of 1440p begint met ‘Max. resolutie’ op 1080p. Stel die bij een kleine doelgrootte lager in.

Gebruik je voor dit werk al HandBrake, dan staat in de [vergelijking met HandBrake](/nl/alternatives/handbrake/) waar de twee verschillen, en de [vergelijking met Compress Videos & Resize Video](/alternatives/compress-videos-resize-video/){: hreflang="en"} (in het Engels) doet hetzelfde voor de iPhone. Waarom de makers van MediaKit dit werk weghouden van andermans servers, is het onderwerp van [een eerder artikel](/journal/your-photos-shouldnt-ride-the-elevator/){: hreflang="en"} (in het Engels), en de rest van de gereedschapskist staat in [dit artikel](/journal/every-media-tool-already-on-your-mac/){: hreflang="en"} (in het Engels). Hoe je een MKV-bestand omzet, staat in [MKV naar MP4](/nl/journal/mkv-naar-mp4/).
