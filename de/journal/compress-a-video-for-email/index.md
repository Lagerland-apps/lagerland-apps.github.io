---
layout: journal
slug: compress-a-video-for-email
ref: /journal/compress-a-video-for-email/
permalink: /de/journal/compress-a-video-for-email/
translated_from: 2026-10-29
last_updated: 2026-10-29
date: 2026-10-29
title: "Video für E-Mail komprimieren: die Größenlimits und die Rechnung mit der Bitrate"
seo:
  title: "Video für E-Mail komprimieren: Limits und Bitrate"
  description: "Gmail nimmt 25 MB, Outlook, iCloud Mail, GMX und WEB.DE 20 MB. Wie viel Luft du lassen solltest, welche Bitrate passt und wie es auf iPhone und Mac geht."
  keywords:
    - "video komprimieren für email"
    - "video per mail verschicken zu groß"
    - "video per mail verschicken iphone"
    - "e-mail anhang größe limit"
    - "gmx anhang maximale größe"
    - "bitrate für dateigröße berechnen"
    - "mail drop größe"
    - "mediakit"
lede: "Jeder E-Mail-Anbieter begrenzt, was er transportiert, und ein Video stößt schnell an diese Grenze. Hier stehen die Limits, die Gmail, Outlook, iCloud Mail, GMX und WEB.DE angeben, warum ein Limit von 25 MB keine Datei mit 25 MB durchlässt, wie du aus einer Zielgröße die Bitrate berechnest und wie MediaKit diese Rechnung auf iPhone und Mac übernimmt, ohne den Clip hochzuladen."
quick_answer: "Um ein Video per E-Mail zu verschicken, machst du die Datei kleiner als das Limit deines Anbieters, mit etwas Luft. Privates Gmail nimmt 25 MB Anhänge an, die Outlook-App 20 MB pro Nachricht bei Internetkonten wie Outlook.com, iCloud Mail 20 MB, GMX FreeMail und WEB.DE FreeMail ebenfalls 20 MB und Exchange-Konten im Beruf standardmäßig 10 MB. Anhänge werden als Base64 kodiert verschickt, was laut Microsoft etwa 33 % aufschlägt. Plane deshalb mit etwa drei Vierteln des Limits: rund 18 MB bei Gmail und 15 MB bei 20 MB Limit. Für die Bitrate multiplizierst du die Zielgröße in Megabyte mit 8000 und teilst durch die Länge des Clips in Sekunden; das ist die Gesamtbitrate in kbit/s. Zieh die Audiobitrate ab (128 kbit/s sind üblich), der Rest bleibt fürs Bild. Senk die Auflösung, bis sie zu diesem Budget passt, bleib bei H.264, damit der Clip überall läuft, und schick einen Link, wenn das Budget zu knapp wird: Mail Drop überträgt bis zu 5 GB."
excerpt: "Eine Übersicht für Videos per E-Mail: die Anhangslimits von Gmail, Outlook, Exchange, iCloud Mail, GMX, WEB.DE und Mail Drop, warum du wegen der Base64-Kodierung mit drei Vierteln des Limits planen solltest, eine Bitrate-Tabelle für Clips von 30 Sekunden bis fünf Minuten und wie der Modus „Zielgröße“ von MediaKit dieselbe Rechnung auf iPhone und Mac erledigt."
faq:
  - q: "Wie groß darf ein Video bei Gmail höchstens sein?"
    a: "Mit einem privaten Gmail-Konto kannst du bis zu 25 MB Anhänge in einer Nachricht senden, alle zusammengezählt; für Konten von Arbeit oder Schule gelten die Limits, die ihr Google-Workspace-Administrator festlegt. Über dem Limit entfernt Gmail den Anhang und fügt stattdessen einen Google-Drive-Link ein. Weil Anhänge unterwegs Base64-kodiert sind, plane mit einem Video von etwa 18 MB, wenn es als echter Anhang ankommen soll."
  - q: "Warum kommt mein Video zurück, obwohl es unter dem Anhangslimit liegt?"
    a: "Dafür gibt es drei häufige Gründe. Anhänge werden vor dem Versand Base64-kodiert, und laut Microsofts Exchange-Dokumentation macht das die Nachricht etwa 33 % größer, sodass eine Datei knapp unter dem Limit nach der Kodierung darüber liegen kann. Manche Limits zählen die ganze Nachricht, nicht nur den Anhang; laut Microsoft gehört bei Outlook die E-Mail selbst zu den 20 MB dazu. Und der Server des Empfängers hat ein eigenes Limit, das niedriger sein kann als deins, etwa die 10 MB, die bei Exchange voreingestellt sind."
  - q: "Wie berechne ich die Bitrate für eine bestimmte Dateigröße?"
    a: "Multipliziere die Zielgröße in Megabyte mit 8000, um Kilobit zu erhalten, teile durch die Länge des Clips in Sekunden, um die Gesamtbitrate in kbit/s zu bekommen, und zieh dann die Audiobitrate ab. Der Rest ist die Videobitrate. Für 18 MB und einen Clip von 90 Sekunden: 18 × 8000 = 144.000 Kilobit, geteilt durch 90 sind das 1600 kbit/s, minus 128 kbit/s für den Ton bleiben etwa 1470 kbit/s fürs Bild."
  - q: "Soll ich für ein Video per E-Mail H.264 oder HEVC nehmen?"
    a: "H.264 in einer MP4-Datei, außer du weißt, dass der Empfänger ein aktuelles Apple-Gerät nutzt. Laut Apple komprimiert HEVC besser als H.264, eine HEVC-Datei sieht bei gleicher Größe also besser aus. Du bestimmst aber nicht, worauf der Anhang geöffnet wird, und H.264 spielt fast jedes Gerät ab. Nutzt der Empfänger ein aktuelles iPhone, iPad oder einen Mac, holst du mit HEVC bei gleicher Größe mehr Qualität heraus."
  - q: "Was tun, wenn das Video zu lang ist, um es klein genug zu bekommen?"
    a: "Schick einen Link. Mail Drop in Apple Mail und iCloud Mail verschickt Dateien bis 5 GB als Download-Link, der nach 30 Tagen abläuft, und Mail bietet es an, wenn eine Nachricht für deinen Anbieter zu groß ist. Gmail ersetzt einen zu großen Anhang von selbst durch einen Google-Drive-Link. Ein Clip von fünf Minuten, auf 15 MB gepresst, lässt dem Bild etwa 270 kbit/s, ein Viertel dessen, was YouTube schon für 360p-Uploads empfiehlt."
  - q: "Kann MediaKit ein Video auf eine bestimmte Dateigröße komprimieren?"
    a: "Ja. „Video komprimieren“ hat den Modus „Zielgröße“, der eine Zahl in KB, MB oder GB annimmt. MediaKit teilt die Zielgröße durch die Länge des Clips, zieht die gewählte Audiobitrate ab, hält 3 % zurück, kodiert, misst dann die geschriebene Datei und kodiert mit korrigierter Bitrate noch einmal, falls das Ziel verfehlt wurde. Kommt die App trotzdem nicht darunter, bricht sie mit einer Fehlermeldung ab, statt dir eine zu große Datei zu geben. Das läuft auf dem Gerät, auf iPhone und Mac, und „Video komprimieren“ ist eines der fünf Werkzeuge, die nach den ersten drei Tagen dauerhaft kostenlos bleiben."
mentioned_apps:
  - mediakit
read_time: "8 Min. Lesezeit"
---

Mit den 8 Mbit/s, die YouTube für 1080p-Uploads empfiehlt, ist eine Minute Video 60 MB groß. Das ist mehr als doppelt so viel, wie Gmail anhängt. Einen Clip in eine E-Mail zu bekommen, ist eine kleine Rechenaufgabe: ein Ziel unter dem Limit deines Anbieters wählen, die passende Bitrate ausrechnen und mit dieser Bitrate neu kodieren. Hier stehen die Zahlen für jeden Schritt, danach siehst du, wie [MediaKit](/de/apps/mediakit/) das auf iPhone und Mac erledigt, ohne den Clip vorher irgendwohin zu schicken.

## Wie groß darf ein Video per E-Mail sein?

| Dienst | Limit | Was gezählt wird | Über dem Limit |
|---|---|---|---|
| Gmail, privates Konto | 25 MB | Alle Anhänge der Nachricht zusammen | Gmail ersetzt den Anhang durch einen Google-Drive-Link |
| Outlook-App, Internetkonten wie Outlook.com | 20 MB | Die Anhänge plus die E-Mail selbst | Microsoft rät, zu komprimieren oder einen Cloud-Link zu teilen |
| Exchange, Konten im Beruf | standardmäßig 10 MB | Die ganze Nachricht; Administratoren können das ändern | Wie oben |
| iCloud Mail | 20 MB | Eingehende und ausgehende Nachrichten | Bis zu 5 GB, wenn Mail Drop eingeschaltet ist |
| GMX FreeMail | 20 MB | Dateianhänge, beim Senden und Empfangen | GMX ProMail erlaubt 50 MB, GMX TopMail 100 MB |
| WEB.DE FreeMail | 20 MB | Anhänge beim Versenden | Auf der Seite nicht angegeben |
| Mail Drop (Apple Mail, iCloud Mail) | 5 GB | Die Nachricht samt Anhängen; jeder Link läuft nach 30 Tagen ab | Mail Drop kann sie nicht senden |

Die Limits stehen so auf den Hilfeseiten der Anbieter: [Gmail-Hilfe](https://support.google.com/mail/answer/6584?hl=de), [Microsoft-Support](https://support.microsoft.com/de-de/office/senden-gro%C3%9Fer-dateien-mit-outlook-8c698842-b462-4a4c-8d53-5c5dd04f77ef) und Apples Seiten zu den [Grenzwerten von iCloud Mail](https://support.apple.com/de-de/102198) und zu [Mail Drop](https://support.apple.com/de-de/108329), geprüft im Juli 2026, sowie [GMX](https://www.gmx.net/mail/dateianhaenge/) und [WEB.DE](https://web.de/email/uebersicht/), geprüft am 29. Oktober 2026. Für Konten von Arbeit oder Schule können Administratoren niedrigere Werte festlegen, und der empfangende Server wendet sein eigenes Limit an. Laut Microsofts [Exchange-Dokumentation](https://learn.microsoft.com/de-de/exchange/mail-flow/message-size-limits) muss eine Nachricht in die Limits von Absender und Empfänger passen; das kleinste Limit auf dem Weg entscheidet also.

## Warum ein Limit von 25 MB keine Datei mit 25 MB durchlässt

E-Mail ist ein Textformat. Bevor ein Video als Anhang reisen kann, wird es Base64-kodiert: Aus je drei Bytes der Datei werden vier Textzeichen, aufgeteilt in Zeilen von höchstens 76 Zeichen ([RFC 2045, Abschnitt 6.8](https://www.rfc-editor.org/rfc/rfc2045#section-6.8){: hreflang="en"}, auf Englisch). Die Nachricht, die durchs Netz geht, ist etwa ein Drittel größer als die Datei auf deinem Gerät.

Ob ein Limit vor oder nach dieser Kodierung gemessen wird, ist unterschiedlich, und die Hilfeseiten für Privatkunden sagen es selten. Microsofts Exchange-Dokumentation sagt es: Base64 schlägt etwa 33 % auf, bei einem Limit von 64 MB pro Nachricht sind also realistisch etwa 48 MB drin. Die Outlook-Seite ergänzt, dass zu den 20 MB auch die E-Mail selbst gehört, nicht nur der Anhang.

Die Faustregel lautet deshalb: drei Viertel des angegebenen Limits.

| Angegebenes Limit | Plane mit einer Datei von etwa |
|---|---|
| 25 MB (Gmail) | 18 MB |
| 20 MB (Outlook, iCloud Mail, GMX FreeMail, WEB.DE FreeMail) | 15 MB |
| 10 MB (Exchange-Standard) | 7,5 MB |

Zu klein kostet ein wenig Bildqualität. Zu groß heißt: Die Mail kommt zurück, oder du bekommst einen Link, wo du einen Anhang wolltest.

## So rechnest du die passende Bitrate aus

Dateigröße ist Bitrate mal Dauer. Rechne rückwärts:

1. **Rechne das Ziel in Kilobit um.** Megabyte × 8000, wobei ein Megabyte 1.000.000 Bytes sind.
2. **Teile durch die Länge des Clips in Sekunden.** Das ist die Gesamtbitrate in kbit/s.
3. **Zieh den Ton ab.** 128 kbit/s ist eine übliche Stereo-Einstellung; für Sprache reichen 64 kbit/s.
4. **Der Rest ist die Videobitrate.** Lass ein paar Prozent für den Overhead des Containers übrig.

Ein Clip von 90 Sekunden für Gmail: 18 MB × 8000 = 144.000 Kilobit. Geteilt durch 90 Sekunden sind das 1600 kbit/s. Zieh 128 kbit/s für den Ton ab, und etwa 1470 kbit/s bleiben fürs Bild.

Dieselbe Rechnung für gängige Längen, jeweils nach Abzug von 128 kbit/s Ton:

| Länge des Clips | Datei mit 7,5 MB | Datei mit 15 MB | Datei mit 18 MB |
|---|---|---|---|
| 30 Sekunden | 1870 kbit/s | 3870 kbit/s | 4670 kbit/s |
| 1 Minute | 870 kbit/s | 1870 kbit/s | 2270 kbit/s |
| 2 Minuten | 370 kbit/s | 870 kbit/s | 1070 kbit/s |
| 5 Minuten | 70 kbit/s | 270 kbit/s | 350 kbit/s |

Die Werte sind abgerundet.

## Welche Auflösung und welcher Codec passen?

Ob eine Bitrate großzügig oder knapp ist, hängt vom Bild ab, das sie füllen muss. Zum Vergleich: YouTubes [empfohlene Upload-Einstellungen](https://support.google.com/youtube/answer/1722171?hl=de) verlangen bei normalen Bildraten 8 Mbit/s für 1080p, 5 Mbit/s für 720p, 2,5 Mbit/s für 480p und 1 Mbit/s für 360p. Diese Werte sind hoch, weil YouTube alles neu kodiert, was es bekommt, aber sie zeigen, wie schnell der Bedarf mit der Bildgröße sinkt: 1080p hat 2,25-mal so viele Pixel wie 720p.

Eine grobe Regel: Liegt dein Videobudget deutlich unter der Hälfte des YouTube-Werts für die Auflösung des Clips, geh eine Auflösung herunter. Nach dieser Regel ist ein einminütiger Clip mit 18 MB (2270 kbit/s) in 720p besser aufgehoben als in 1080p, und mit 7,5 MB (870 kbit/s) gehört er auf 480p oder darunter. Drei weitere Einstellungen verändern das Ergebnis:

- **Audiobitrate.** Bei einem Clip, in dem vor allem jemand spricht, gibt 64 statt 128 kbit/s die Differenz ans Bild weiter. Bei einem Clip von fünf Minuten mit 15 MB ist das fast ein Viertel mehr Videobitrate.
- **Bildrate.** Ein Clip mit 60 fps verteilt seine Bits auf doppelt so viele Bilder wie einer mit 30 fps. YouTubes Werte für 48 bis 60 fps liegen etwa um die Hälfte höher als die für 24 bis 30.
- **Codec.** Laut Apple [komprimiert HEVC besser als H.264](https://support.apple.com/de-de/116944), und aktuelle Apple-Geräte spielen es ab. Du bestimmst aber nicht, wo der Anhang geöffnet wird, und H.264 in einer MP4-Datei läuft fast überall. Apples Seite erwähnt auch, dass seine Geräte HEVC beim Teilen mit einem Gerät, das es nicht abspielen kann, *eventuell* in H.264 umwandeln; bei einer Datei, die du schon komprimiert hast, ist es einfacher, gleich H.264 zu wählen.

## Wann ein Link besser ist

In der Zeile für fünf Minuten hört Komprimieren auf, sinnvoll zu sein: 270 kbit/s sind etwa ein Viertel dessen, was YouTube für 360p empfiehlt. Wird das Budget so knapp, ist der Empfänger mit einem Link besser bedient als mit einem Anhang.

- **Mail Drop** in Apple Mail und iCloud Mail verschickt Dateien bis 5 GB als Download-Link, der nach 30 Tagen abläuft. Mail bietet es an, wenn eine Nachricht größer ist, als dein Anbieter erlaubt.
- **Gmail** ersetzt einen Anhang über 25 MB von selbst durch einen Google-Drive-Link.
- **Outlook** verweist dich darauf, die Datei zu komprimieren oder aus einem Cloudspeicher zu teilen.

Mit einem Link bekommt der Empfänger das Original in voller Qualität, und eine Kopie liegt auf einem Server, solange der Link gilt.

## So geht es in MediaKit

[MediaKit](/de/apps/mediakit/) erledigt die Rechnung oben auf dem Gerät, auf dem iPhone und auf dem Mac, und lädt den Clip nie hoch. „Video komprimieren“ ist eines der fünf Werkzeuge, die nach den ersten drei Tagen dauerhaft kostenlos bleiben, jeweils für eine Datei.

1. **Öffne den Clip.** Auf dem Mac ziehst du ihn ins Fenster. Auf dem iPhone fügst du ihn aus der App „Fotos“ oder der App „Dateien“ hinzu oder schickst ihn über das Menü „Teilen“ einer anderen App.
2. **Wähl das Werkzeug „Komprimieren“ für Video** und stell **Modus** auf **Zielgröße**.
3. **Gib das Ziel ein**, das dir die Drei-Viertel-Tabelle nennt, zum Beispiel 18, mit der Einheit MB. MediaKit rechnet ein Megabyte als 1.000.000 Bytes.
4. **Öffne „Erweitert“.** Stell **Max. Auflösung** nach der Bitrate-Tabelle ein, lass **Codec** für E-Mail auf H.264 und wähl unter **Audio-Bitrate** die Option **64 kbps (Sprache)**, wenn im Clip vor allem gesprochen wird.
5. **Starte das Komprimieren und prüf die Größe** des Ergebnisses, bevor du es anhängst.

Im Modus „Zielgröße“ erledigt MediaKit die Schritte eins bis vier der Rechnung selbst: Es teilt das Ziel durch die Länge des Clips, zieht die gewählte Audiobitrate ab und hält 3 % zurück, kodiert, misst dann die geschriebene Datei und kodiert mit korrigierter Bitrate noch einmal, falls das Ziel verfehlt wurde. Eine Datei über dem Ziel gibt dir die App nie: Kommt sie nicht darunter, bricht sie mit einer Fehlermeldung ab. Bei einer Quelle in 4K oder 1440p steht „Max. Auflösung“ anfangs auf 1080p; für ein kleines Ziel stellst du sie niedriger.

Nutzt du für diese Aufgabe schon HandBrake, zeigt der [Vergleich mit HandBrake](/alternatives/handbrake/){: hreflang="en"} (auf Englisch), wo sich die beiden unterscheiden, und der [Vergleich mit Compress Videos & Resize Video](/alternatives/compress-videos-resize-video/){: hreflang="en"} (auf Englisch) tut dasselbe fürs iPhone. Warum das Studio diese Arbeit von fremden Servern fernhält, steht in [einem früheren Beitrag](/journal/your-photos-shouldnt-ride-the-elevator/){: hreflang="en"} (auf Englisch), den ganzen Werkzeugkasten zeigt [dieser hier](/journal/every-media-tool-already-on-your-mac/){: hreflang="en"} (auf Englisch).
