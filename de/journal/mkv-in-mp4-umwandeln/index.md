---
layout: journal
slug: mkv-in-mp4-umwandeln
local_only: true
permalink: /de/journal/mkv-in-mp4-umwandeln/
last_updated: 2026-11-08
date: 2026-11-08
title: "MKV in MP4 umwandeln: verlustfrei per Remux, mit VLC, HandBrake oder MediaKit"
seo:
  title: "MKV in MP4 umwandeln: VLC, HandBrake oder MediaKit"
  description: "MKV in MP4 umwandeln am Mac oder iPhone: per Remux ohne Qualitätsverlust oder neu codiert, kostenlos mit ffmpeg, VLC und HandBrake oder mit MediaKit."
  keywords:
    - "mkv in mp4 umwandeln"
    - "mkv in mp4 umwandeln kostenlos"
    - "mkv in mp4 umwandeln mac"
    - "mkv in mp4 umwandeln vlc"
    - "mkv in mp4 umwandeln handbrake"
    - "mkv auf iphone abspielen"
    - "mkv in mp4 ohne qualitätsverlust"
lede: "Eine MKV-Datei ist ein Container, also eine Hülle für Video, Ton und Untertitel. Wer sie in MP4 umwandelt, muss deshalb oft nur die Verpackung wechseln und kann Bild und Ton unangetastet lassen. Dieser Beitrag erklärt den Unterschied zwischen Remux und Neucodierung, zeigt die kostenlosen Wege mit VLC, HandBrake und ffmpeg, ordnet Online-Konverter ein und beschreibt, wie MediaKit eine MKV-Datei auf Mac und iPhone umwandelt."
quick_answer: "Um MKV in MP4 umzuwandeln, ohne Qualität zu verlieren, brauchst du einen Remux: Video und Ton werden unverändert in einen MP4-Container kopiert, was nur klappt, wenn die Codecs zu MP4 passen. Kostenlos geht das zum Beispiel mit ffmpeg (Option -c copy); VLC und HandBrake wandeln über Menüs um; HandBrake codiert das Video dabei laut seiner Dokumentation immer neu. Ein Online-Konverter verlangt, dass du die ganze Datei hochlädst. MediaKit macht den Remux auf dem Gerät, am Mac und am iPhone: H.264, HEVC, AAC und AC-3 werden übernommen, DTS-, E-AC-3- und MP3-Ton fällt weg, mit Hinweis. „Konvertieren“ ist nach der Testphase Pro; „Video komprimieren“ bleibt kostenlos, codiert aber neu."
excerpt: "MKV in MP4 umwandeln: was ein Container ist, Remux oder Neucodierung, die kostenlosen Wege mit VLC, HandBrake und ffmpeg, Online-Konverter bei großen Dateien und wie MediaKit MKV auf Mac und iPhone verarbeitet."
faq:
  - q: "Wie kann ich MKV kostenlos in MP4 umwandeln?"
    a: "Mit ffmpeg, VLC oder HandBrake, alle drei sind kostenlos. ffmpeg kopiert die Streams auf Wunsch unverändert (-c copy), laut seiner Dokumentation ohne Decodieren und ohne Qualitätsverlust. VLC und HandBrake arbeiten mit Menüs und Voreinstellungen. In MediaKit bleibt „Video komprimieren“ dauerhaft kostenlos und macht aus einer MKV-Datei eine MP4-Datei, codiert dabei aber neu, ist also kein verlustfreier Remux. Der Remux-Weg über „Konvertieren“ gehört nach der kostenlosen Testphase zu Pro."
  - q: "Geht MKV in MP4 umwandeln ohne Qualitätsverlust?"
    a: "Ja, wenn die Codecs in den MP4-Container passen: Ein Remux kopiert Video und Ton in einen neuen Container, ohne sie neu zu codieren. MediaKit remuxt MKV-Dateien mit H.264- oder HEVC-Video und AAC- oder AC-3-Ton. DTS-, E-AC-3- oder MP3-Ton in einer MKV-Datei kann MediaKit dabei nicht übernehmen; er fällt weg, und die App weist darauf hin."
  - q: "Wie wandle ich MKV mit VLC in MP4 um?"
    a: "Das Wiki von VideoLAN beschreibt einen Assistenten unter Medien beziehungsweise „Media“, dort „Convert/Save“, in dem du Videocodec, Audiocodec und Container wählst. Die Seite warnt selbst, dass sie veraltet ist und ein Transcodieren sehr langsam sein kann. Schau deshalb in die Dokumentation deiner VLC-Version; die genauen Schritte können abweichen."
  - q: "Wie wandle ich MKV mit HandBrake in MP4 um?"
    a: "HandBrake öffnet MKV-Dateien und schreibt MP4 oder MKV; die meisten Voreinstellungen erzeugen laut Dokumentation MP4. Die Voreinstellungen arbeiten mit Videocodecs wie H.264, H.265, AV1 oder VP9, und die Dokumentation sagt ausdrücklich, dass HandBrake Video immer umwandelt und nie unverändert durchreicht. Das ist sinnvoll, wenn die Datei kleiner werden soll, aber es ist kein verlustfreier Remux."
  - q: "Wie spiele ich MKV auf dem iPhone ab?"
    a: "Apple erklärt auf seiner Support-Seite, dass ältere oder spezielle Formate nicht überall laufen, und nennt .mkv als Beispiel für eine Endung, zu der du eine andere App suchen kannst. Du hast zwei Wege: eine Player-App, die MKV abspielt (VideoLAN führt iOS als Plattform von VLC auf), oder die Datei in MP4 umwandeln. MediaKit öffnet MKV auf dem iPhone und wandelt per „Konvertieren“ um."
  - q: "Wie wandle ich MKV am Mac in MP4 um?"
    a: "Klicke im Finder mit der rechten Maustaste auf die MKV-Datei, wähle „Öffnen mit“ und dann MediaKit. Danach wählst du „Konvertieren“, als Ausgabeformat MP4 und als Codec „Original behalten (Remux)“. MediaKit braucht macOS 14.6 oder neuer."
mentioned_apps:
  - mediakit
read_time: "7 Min. Lesezeit"
---

Eine MKV-Datei ist ein Container: eine Hülle, in der Video-, Ton- und Untertitelspuren liegen. MKV in MP4 umzuwandeln heißt deshalb nicht zwingend, das Video neu zu berechnen. Wenn die Codecs im Inneren zu MP4 passen, genügt ein **Remux**: Die Spuren wandern unverändert in einen neuen Container, ohne Qualitätsverlust. Passen sie nicht, bleibt nur die **Neucodierung**, und die kostet Qualität. Dieser Beitrag geht beide Wege durch und vergleicht VLC, HandBrake, ffmpeg, Online-Konverter und [MediaKit](/de/apps/mediakit/).

## Was ist eine MKV-Datei, und worin unterscheidet sie sich von MP4?

Das Matroska-Projekt, das das Format pflegt, schreibt auf seiner Website: Matroska sei [kein Kompressionsformat für Video oder Ton](https://www.matroska.org/what_is_matroska.html){: hreflang="en"} (auf Englisch). Es beschreibt Matroska als Hülle, die viele Ton-, Video- und Untertitelspuren aufnehmen kann, sodass ein ganzer Film in einer Datei liegt. MP4 führt das Projekt unter den bestehenden Containern auf, zu denen Matroska eine offene Alternative sein will. MP4 ist also ebenfalls ein Container.

Zwei Dateien können dadurch dasselbe Bild und denselben Ton enthalten und sich nur in der Hülle unterscheiden. Die Hülle zu wechseln geht, ohne den Inhalt anzufassen. Einen anderen Codec zu wählen heißt dagegen: decodieren und neu codieren.

## Warum spielt das iPhone oder der Mac MKV nicht immer ab?

Apple beschreibt in einem Support-Artikel, [was du tun kannst, wenn sich Mediendateien nicht öffnen lassen](https://support.apple.com/de-de/102644): Apps wie Fotos, iMovie, Safari, Keynote und QuickTime Player unterstützen viele Formate, ältere oder spezielle Formate laufen aber unter Umständen nicht, wenn Gerät, Betriebssystem oder App sie nicht unterstützen. Als Beispiel für eine Endung, nach der du eine passende App suchen kannst, nennt Apple unter anderem .mkv. Ob MKV unterstützt wird, sagt der Artikel nicht ausdrücklich.

Am Mac siehst du das Format einer Datei, wenn du sie im Finder auswählst und Befehlstaste-I drückst. Als Beispiel nennt Apple im selben Artikel die Angabe „Art: Matroska-Videodatei“.

## Remux oder Neucodierung: wann geht nichts verloren?

Ein Remux kopiert die Video- und Tonspuren aus einem Container in den anderen, ohne sie zu decodieren. Die Dokumentation von ffmpeg nennt das [Stream Copy](https://ffmpeg.org/ffmpeg.html){: hreflang="en"} (auf Englisch): Da nichts decodiert oder codiert werde, sei es sehr schnell und ohne Qualitätsverlust. Dieselbe Seite nennt auch die Grenze: Es kann scheitern, etwa wenn dem Ziel-Container Angaben fehlen, die in der Quelle nicht vorhanden sind. Filter wie Skalieren oder Zuschneiden gehen beim Kopieren ebenfalls nicht.

Eine Neucodierung erzeugt dagegen eine neue Kompression. Sie ist richtig, wenn die Datei kleiner werden soll oder ein Codec nicht in MP4 passt, aber sie kostet einen Teil der Bildqualität. Wie du die Zielgröße dafür berechnest, steht im Beitrag [Video für E-Mail komprimieren](/de/journal/compress-a-video-for-email/).

## MKV in MP4 umwandeln mit ffmpeg

ffmpeg ist ein kostenloses Kommandozeilenprogramm. Der Remux ist ein einziger Befehl, in dem `-c copy` die Spuren unverändert übernimmt:

```
ffmpeg -i film.mkv -c copy film.mp4
```

Ohne weitere Angaben wählt ffmpeg laut Dokumentation automatisch je eine Spur pro Art aus, also etwa ein Video und eine Tonspur; weitere Spuren holst du mit der Option `-map` dazu. Das ist der schnellste Weg, wenn du das Terminal nicht scheust. Klappt es nicht, liegt es oft an einem Codec oder einer Spur, die MP4 nicht aufnimmt (siehe die Einschränkung oben); dann hilft nur Neucodieren oder das Weglassen der betroffenen Spur.

## MKV in MP4 umwandeln mit VLC

VLC ist kostenlos. [VideoLAN](https://www.videolan.org/vlc/){: hreflang="en"} (auf Englisch) beschreibt es als freien, quelloffenen Multimedia-Player für viele Plattformen, nennt iOS unter den Plattformen und MKV unter den Formaten. Zum Umwandeln beschreibt das [VideoLAN-Wiki](https://wiki.videolan.org/Transcode/){: hreflang="en"} (auf Englisch) einen Assistenten: im Menü „Media“ den Punkt „Convert/Save“ wählen, dann Videocodec, Audiocodec und Container festlegen. Dort steht auch, dass die Seite veraltet ist und ein Transcodieren sehr langsam sein kann. Die Schritte in deiner VLC-Version können deshalb anders aussehen; schau in ihre Dokumentation.

Wer VLC ohnehin nutzt, kommt damit ohne Kosten ans Ziel. Und wenn du die Datei nur ansehen willst, genügt oft schon der Player: VLC spielt MKV direkt ab.

## MKV in MP4 umwandeln mit HandBrake

HandBrake nennt sich [kostenlos, quelloffen und für Windows, Mac und Linux erhältlich](https://handbrake.fr/){: hreflang="en"} (auf Englisch). Es öffnet [MKV als Quellformat](https://handbrake.fr/docs/en/latest/technical/source-formats.html){: hreflang="en"} (auf Englisch) und schreibt laut Dokumentation der [Voreinstellungen](https://handbrake.fr/docs/en/latest/technical/official-presets.html){: hreflang="en"} (auf Englisch) wahlweise MP4 oder MKV; die meisten Voreinstellungen erzeugen MP4. Die Voreinstellungen arbeiten mit Videocodecs wie H.264, H.265, AV1 oder VP9. Unter den Dingen, die HandBrake nicht kann, nennt die Seite [Über HandBrake](https://handbrake.fr/docs/en/latest/introduction/about.html){: hreflang="en"} (auf Englisch) ausdrücklich, Video ohne Umwandlung durchzureichen: Das Video wird immer neu codiert. Das passt, wenn du die Datei zugleich verkleinern willst. Für einen reinen Containerwechsel ohne Verlust sind ffmpeg und MediaKit der direktere Weg. Surround-Ton reichen die Voreinstellungen laut Dokumentation durch, wo das möglich ist.

## Online-Konverter und große Dateien

Ein Online-Konverter lädt deine Datei auf seine Server, wandelt sie dort um und gibt sie dir zurück. Bei einer großen MKV-Datei heißt das: erst alles hochladen, und der Inhalt verlässt dein Gerät. Ob das für dich passt, hängt vom Video ab. Den Unterschied zwischen Upload und Umwandlung auf dem Gerät zeigen die Vergleiche mit [CloudConvert](/de/alternatives/cloudconvert/) und [Convertio](/de/alternatives/convertio/).

## MKV in MP4 umwandeln mit MediaKit

MediaKit ist eine App für iPhone und Mac, die auf dem Gerät arbeitet: Die Datei wird nirgends hochgeladen. MKV-Dateien öffnen sich direkt, MediaKit entpackt sie selbst.

**Am Mac** (macOS 14.6 oder neuer) klickst du im Finder mit der rechten Maustaste auf die MKV-Datei, wählst „Öffnen mit“ und dann MediaKit. Die App steht für MKV in dieser Liste. Du kannst die Datei auch auf das Dock-Symbol ziehen.

**Am iPhone** (iOS 17 oder neuer) wählst du das Video in MediaKit aus der App „Dateien“ oder aus Fotos aus oder schickst es aus einer anderen App über das Menü „Teilen“.

Dann geht es auf beiden Geräten gleich weiter:

1. Wähle das Werkzeug „Konvertieren“.
2. Wähle als Ausgabeformat MP4 (MOV und M4V gibt es auch).
3. Wähle beim Codec „Original behalten (Remux)“. H.264, HEVC und ProRes sind die anderen Optionen und codieren neu.
4. Wähle „Ausführen“ und lies einen möglichen Hinweis zum Ton.

H.264- und HEVC-Video sowie AAC- und AC-3-Ton werden dabei unverändert übernommen. DTS-, E-AC-3- und MP3-Ton in einer MKV-Datei kann MediaKit nicht übernehmen: Die Spur fehlt dann in der MP4-Datei, und die App zeigt einen Hinweis. Hat dein Film eine DTS-Spur, bewahre die Originaldatei auf. WebM unterstützt MediaKit nicht.

Das Werkzeug „Video komprimieren“ nimmt ebenfalls MKV-Dateien an. Quellen in MP4, MOV und M4V behalten ihren Container, andere werden zu MP4. Es codiert nach Qualitätsstufe oder Zielgröße neu. Das ist nützlich, um eine Datei zu verkleinern, aber kein verlustfreier Remux.

### Was kostet das?

„Video komprimieren“ gehört zu fünf Werkzeugen, die dauerhaft kostenlos bleiben, jeweils ein Export auf einmal. Alle anderen Werkzeuge, auch „Konvertieren“ für Video, sind Pro. Nach dem ersten Start gibt es eine kostenlose Testphase mit allen Werkzeugen, ohne Zahlungsangabe. Wandelst du nur gelegentlich eine Datei um, genügt ein kostenloses Programm wie ffmpeg, VLC oder HandBrake.

## Welcher Weg passt?

Entscheide zuerst: Remux oder Neucodierung? Willst du das Bild unverändert lassen, brauchst du eine Option, die Spuren kopiert, und musst prüfen, dass keine Tonspur wegfällt. Willst du die Datei verkleinern, ist Neucodieren normal, und du nimmst einen Verlust in Kauf.

| Was du brauchst | Weg |
|---|---|
| Verlustfreier Remux am Computer, kostenlos | ffmpeg mit `-c copy` |
| Eine Datei umwandeln und neu codieren, kostenlos | VLC oder HandBrake |
| Große oder private MKV-Datei, ohne Upload | ffmpeg, VLC, HandBrake oder MediaKit |
| Remux am Mac oder iPhone ohne Terminal | MediaKit: „Konvertieren“ mit „Original behalten (Remux)“ (Pro) |
| Datei verkleinern | „Video komprimieren“ in MediaKit (kostenlos) oder HandBrake |

Weitere Videowerkzeuge von MediaKit stehen auf der [App-Seite](/de/apps/mediakit/). Wenn du Videos am iPhone vor allem verkleinern willst, vergleicht die Seite [Compress Videos & Resize Video](/de/alternatives/compress-videos-resize-video/) die Möglichkeiten.
