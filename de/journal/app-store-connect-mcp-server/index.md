---
layout: journal
slug: app-store-connect-mcp-server
ref: /journal/app-store-connect-mcp-server/
permalink: /de/journal/app-store-connect-mcp-server/
translated_from: 2026-11-13
last_updated: 2026-11-13
date: 2026-11-13
title: "Ein MCP-Server für App Store Connect, der deinen API-Schlüssel nie sieht"
seo:
  title: "MCP-Server für App Store Connect: Claude zum Umsatz fragen"
  description: "Frag Claude, Cursor oder andere KI-Apps nach deinen App-Store-Verkäufen. AppMeta Pulse für Mac liefert die Berichte per MCP, ohne deinen API-Schlüssel."
  keywords:
    - "app store connect mcp"
    - "app store connect mcp server"
    - "mcp server app store connect"
    - "claude app store umsatz"
    - "ki assistent app store verkäufe"
    - "claude desktop mcp server"
    - "cursor mcp server"
    - "appmeta pulse"
lede: "AppMeta Pulse läuft jetzt auch auf dem Mac, und die Mac-App bringt einen MCP-Server mit. Schaltest du ihn ein, beantworten Claude, Cursor oder eine andere KI-App mit MCP-Unterstützung Fragen aus deinen eigenen Berichten von App Store Connect. Das Hilfsprogramm, das diese Berichte bereitstellt, hat keinen Netzwerkzugriff und sieht deinen API-Schlüssel nie. Dieser Beitrag zeigt, wie das funktioniert, was der Assistent lesen kann und was nicht, und wie es sich von den anderen Wegen unterscheidet, App Store Connect mit einer KI-App zu verbinden."
quick_answer: "Ein MCP-Server für App Store Connect lässt eine KI-App wie Claude oder Cursor deine Daten aus dem App Store lesen und Fragen dazu beantworten. AppMeta Pulse für Mac (ab macOS 14) bringt einen mit. Schalte unter Einstellungen › KI-Assistenten den Zugriff ein, dann hält die App eine schreibgeschützte SQLite-Kopie der Berichte, die sie aus App Store Connect geladen hat, und ein mitgeliefertes Hilfsprogramm stellt sie den KI-Apps bereit, die du verbindest. Das Hilfsprogramm hat keinen Netzwerkzugriff, kann nichts ändern und sieht deinen API-Schlüssel nie. Die Funktion bleibt aus, bis du sie einschaltest, und gehört zum vollen Zugriff von AppMeta Pulse (Abo oder Lebenslang)."
faq:
  - q: "Gibt es einen MCP-Server für App Store Connect?"
    a: "Ja, mehrere. Open-Source-Server wie der App Store Connect MCP Server von JoshuaRileyDev und asc-mcp laufen auf deinem Computer und rufen Apples API mit deinem Schlüssel auf. Appfigures bietet einen MCP-Server für die Daten in deinem Appfigures-Konto. AppMeta Pulse für Mac bringt einen mit, der eine schreibgeschützte Kopie der von Pulse geladenen Berichte bereitstellt, über ein abgeschottetes Hilfsprogramm ohne Netzwerkzugriff, das deinen API-Schlüssel nie sieht."
  - q: "Kann Claude meine Verkäufe aus App Store Connect lesen?"
    a: "Ja, über einen MCP-Server. Schalte in AppMeta Pulse für Mac unter Einstellungen › KI-Assistenten den Zugriff ein und füge das Hilfsprogramm in Claude Desktop oder Claude Code hinzu, mit der Einrichtung, die dir die Einstellungsseite kopiert. Danach kann Claude deine Verkäufe, Abos und Bewertungen abfragen und in normalen Worten antworten."
  - q: "Bekommt die KI-App meinen API-Schlüssel für App Store Connect?"
    a: "Nein. Der .p8-Schlüssel bleibt im Schlüsselbund von AppMeta Pulse, und das Hilfsprogramm, das deine Berichte bereitstellt, hat keinen Zugriff auf den Schlüsselbund. In der Konfiguration der KI-App steht nur der Pfad zum Hilfsprogramm auf deinem Mac, ohne Schlüssel, Token oder Vendor Number."
  - q: "Kann der Assistent meine Apps, Preise oder meinen Store-Eintrag ändern?"
    a: "Nein. Das Hilfsprogramm nimmt pro Abfrage eine schreibgeschützte SQLite-Anweisung an, arbeitet mit einer Kopie deiner Berichte und hat keinen Netzwerkzugriff. App Store Connect erreicht es also gar nicht."
  - q: "Verlassen meine Daten meinen Mac?"
    a: "AppMeta Pulse schickt nichts an die KI-App oder ihren Anbieter. Was die KI-App über das Hilfsprogramm liest, um dir zu antworten, geht an diese App und, bei einem Cloud-Modell, an ihren Anbieter, nach deren Bedingungen. Das ist derselbe Weg wie bei allem, was du selbst in einen Chat einfügst."
  - q: "Läuft der MCP-Server auch auf dem iPhone?"
    a: "Nein. Er gehört zu AppMeta Pulse für Mac. Ein Kauf gilt für die iPhone- und die Mac-App, und die iPhone-App verweist unter „Hilfe & FAQ“ auf die Funktion am Mac."
mentioned_apps:
  - appmeta-pulse
read_time: "7 Min. Lesezeit"
excerpt: "AppMeta Pulse für Mac bringt einen MCP-Server für Claude, Cursor und andere KI-Apps mit. Wie er eine schreibgeschützte Kopie von Apples eigenen Berichten über ein abgeschottetes Hilfsprogramm ohne Netzwerkzugriff und ohne API-Schlüssel bereitstellt, was der Assistent lesen kann und wie er sich von anderen MCP-Servern für App Store Connect unterscheidet."
---

Wer Apps im App Store verkauft, will meistens eine einfache Frage zu den eigenen Zahlen stellen und eine einfache Antwort bekommen. Welche Länder sind in diesem Quartal gewachsen? Wie viele Erstattungen gab es letzten Monat? Hat die Preisänderung die Probeabos gebremst? App Store Connect hat die Daten, verteilt auf Berichtsdateien, die du erst herunterladen, entpacken und zusammenführen musst, bevor sie irgendetwas beantworten.

[AppMeta Pulse](/de/apps/appmeta-pulse/) läuft jetzt auch auf dem Mac, und die Mac-App bringt einen MCP-Server mit. Diese Arbeit kann also eine KI-App für dich erledigen. Der Assistent liest dieselben Berichtsdateien, die du auch selbst herunterladen könntest, und der Teil von Pulse, der sie bereitstellt, erreicht weder das Internet noch deinen API-Schlüssel.

## Was ist ein MCP-Server?

MCP, das [Model Context Protocol](https://modelcontextprotocol.io/){: hreflang="en"} (auf Englisch), ist ein offener Standard, den Anthropic im November 2024 veröffentlicht hat, um KI-Apps mit Werkzeugen und Daten zu verbinden. Ein MCP-Server bietet ein paar benannte Werkzeuge an. Die KI-App entscheidet, wann sie eines aufruft, und liest, was zurückkommt. Claude Desktop, Claude Code, Cursor und VS Code unterstützen MCP-Server.

Für App Store Connect heißt das: Du stellst eine Frage in normalen Worten, und der Assistent holt sich die Zeilen, die er braucht. Du musst keine Berichte mehr exportieren und in einen Chat einfügen.

## Wie funktioniert der MCP-Server von AppMeta Pulse?

1. Öffne in AppMeta Pulse für Mac Einstellungen › KI-Assistenten und schalte „KI-Assistenten dürfen deine Berichte lesen“ ein. Bevor irgendetwas passiert, erklärt ein Hinweis, was du damit erlaubst.
2. Der Mac baut eine SQLite-Kopie der Berichte, die Pulse geladen hat: Apples Zeilen und Spalten so, wie sie angekommen sind, nichts umgerechnet oder aufsummiert. Pulse aktualisiert die Kopie, wenn neue Berichte eintreffen.
3. Die Kopie liegt in einem Ordner, den nur die App und ihr Hilfsprogramm teilen. Das Hilfsprogramm ist eine kleine, abgeschottete App (Sandbox) in AppMeta Pulse. Es kann diesen Ordner lesen und sonst nichts: Es hat weder Netzwerkzugriff noch Zugriff auf den Schlüsselbund oder auf die eigenen Daten der App.
4. Du fügst das Hilfsprogramm in deiner KI-App hinzu. Die Einstellungsseite hat Zeilen, die dir die Einrichtung kopieren: einen Befehl für Claude Code, eine JSON-Konfiguration für Claude Desktop, Cursor und VS Code oder den Pfad zum Hilfsprogramm.
5. Die KI-App startet das Hilfsprogramm auf deinem Mac und spricht über Standardeingabe und Standardausgabe mit ihm.

Die Konfiguration, die deine KI-App speichert, enthält den Pfad zum Hilfsprogramm und sonst nichts. Ein API-Schlüssel, ein Token oder eine Vendor Number steht nicht darin, weil das Hilfsprogramm nie eines davon braucht.

Das Hilfsprogramm bietet vier Werkzeuge an:

| Werkzeug | Was es tut |
|---|---|
| `describe_data` | Ein Leitfaden zur Kopie: wie die Tabellen aufgebaut sind, welche Fehler du vermeiden solltest und welche Spalten jede Tabelle hat, unter Apples eigenen Spaltennamen |
| `data_coverage` | Welche Berichte in der Kopie liegen und welche Tage sie abdecken, damit der Assistent einen fehlenden Tag von einem Tag ohne Verkäufe unterscheiden kann |
| `query` | Führt eine schreibgeschützte SQLite-Anweisung aus, mit bis zu 5.000 Zeilen, 60 KB und etwa 10 Sekunden pro Aufruf |
| `list_accounts` | Die Teams in App Store Connect, deren Berichte auf diesem Mac geteilt werden |

## Was kann der Assistent lesen?

Standardmäßig enthält die Kopie:

- Verkaufsberichte (täglich, wöchentlich, monatlich und jährlich)
- Abo-Berichte und Abo-Ereignisse
- Kundenbewertungen
- Die Listen deiner Apps und In-App-Käufe

Schaltest du „Mehr Berichte sammeln“ ein (Einstellungen › Daten), behält Pulse zusätzlich Finanzberichte, Berichte zu Abonnenten, Angebotscodes und Win-back-Angeboten, Analytics-Berichte aus dem App Store wie Downloads, Nutzung, Sitzungen sowie Installationen und Löschungen und deine Store-Einstellungen: Preise, Verfügbarkeit, Versionen und den Text deines Store-Eintrags. App Store Connect führt keinen Verlauf der Store-Einstellungen, deshalb speichert Pulse jedes Mal eine neue Kopie einer Seite, wenn sie sich ändert.

Der Assistent bekommt Apples Berichte so, wie Apple sie liefert. Er bekommt nichts, was Pulse berechnet, etwa MRR, und auch nicht deinen API-Schlüssel oder deine Einstellungen. Der Leitfaden in `describe_data` erklärt ihm, wie er Apples Dateien richtig liest: nach Berichtshäufigkeit filtern, damit ein Verkauf nicht viermal gezählt wird, verschiedene Währungen nie zusammenzählen, Erstattungen als Zeilen mit negativen Einheiten behandeln und bei jeder Zahl sagen, aus welcher Tabelle und von welchen Tagen sie stammt.

Solange die Funktion eingeschaltet ist, füllt Pulse auch Lücken in der Kopie. Es lädt jeden täglichen Verkaufs-, Abo- und Abo-Ereignis-Bericht erneut, den Apple noch anbietet (etwa das letzte Jahr), und jeden Jahresbericht der letzten zehn Jahre, den es noch nicht als Apples Originaldatei hat. In den Einstellungen siehst du, was noch fehlt. Pulse behält jede Datei, sobald es sie hat. Ab dem Tag, an dem du anfängst, wächst die Kopie also weiter, auch wenn Apple die älteren Tage nicht mehr anbietet.

## Was kann er nicht?

- **Etwas ändern.** Das Abfragewerkzeug nimmt eine schreibgeschützte Anweisung an und arbeitet auf einer Kopie. Das Hilfsprogramm kann diese Kopie nicht verändern und erreicht App Store Connect nicht.
- **Deinen API-Schlüssel sehen.** Der .p8-Schlüssel bleibt im Schlüsselbund von AppMeta Pulse, und das Hilfsprogramm hat keinen Zugriff auf den Schlüsselbund.
- **Ohne dich laufen.** Die Funktion ist aus, bis du sie einschaltest. Schaltest du sie aus oder endet dein voller Zugriff, wird die Kopie gelöscht. Die Kopie wird nicht mit iCloud synchronisiert und ist in keinem Backup enthalten.

AppMeta Pulse schickt nichts an deine KI-App oder ihren Anbieter. Die Zeilen, die der Assistent liest, um dir zu antworten, gehen allerdings an diese KI-App und, bei einem Cloud-Modell, an ihren Anbieter, nach deren Bedingungen. Das ist derselbe Weg, den ein Bericht nimmt, wenn du ihn selbst in einen Chat einfügst.

## Wie unterscheidet er sich von anderen MCP-Servern für App Store Connect?

Pulse ist nicht der einzige Weg, App Store Connect mit einer KI-App zu verbinden, und die anderen passen zu anderen Aufgaben:

- **Open-Source-Server** wie der [App Store Connect MCP Server von JoshuaRileyDev](https://mcpservers.org/servers/JoshuaRileyDev/app-store-connect-mcp-server){: hreflang="en"} und [asc-mcp](https://pypi.org/project/asc-mcp/){: hreflang="en"} (beide auf Englisch) laufen auf deinem Computer und rufen Apples API live mit deinem Schlüssel auf. Manche können weit mehr als Berichte, etwa TestFlight oder App-Metadaten verwalten, und der Schlüssel, den sie haben, kann das auch.
- **[Appfigures](https://appfigures.com/products/cli-ai){: hreflang="en"}** (auf Englisch) bietet einen MCP-Server für die Daten in deinem Appfigures-Konto, mit Marktdaten wie Rankings und Daten zur Konkurrenz.
- **Gehostete Anbindungen** wie [die von Truto](https://truto.one/blog/connect-app-store-connect-to-claude-analyze-sales-user-reviews/){: hreflang="en"} (auf Englisch) geben dir einen MCP-Endpunkt, der App Store Connect von deren Servern aus aufruft.

Der Server von AppMeta Pulse kann bewusst weniger. Er liest nur, arbeitet mit Apples eigenen Berichtsdateien und läuft auf deinem Mac, mit einem Hilfsprogramm, das das Netzwerk nicht erreicht. Soll dein Assistent auch deinen Store-Eintrag bearbeiten oder Builds ausliefern können, passt ein Open-Source-Server besser.

## Fragen, die sich lohnen

Die Kopie enthält die rohen Zeilen der Berichte, deshalb funktionieren Fragen wie diese:

- Welche Länder sind beim Erlös in diesem Quartal im Vergleich zum selben Quartal im Vorjahr am stärksten gewachsen?
- Welcher Anteil der neuen Abos im letzten Monat hat mit einem kostenlosen Probeabo begonnen, pro App?
- Wie viele Erstattungen hatte jede App in den letzten 90 Tagen?
- Worüber beschweren sich die Bewertungen mit einem und zwei Sternen in diesem Monat am häufigsten?
- Was stand im März in meinem Store-Eintrag? (Nur wenn „Mehr Berichte sammeln“ damals schon eingeschaltet war.)

Rechnen muss der Assistent selbst. Bitte ihn, dir das SQL zu zeigen, das er ausgeführt hat, und zu jeder Zahl den Bericht und die Tage zu nennen. Eine Frage zum Vorjahresvergleich klappt erst, wenn die Kopie beide Jahre enthält.

## Was brauchst du?

- Einen Mac mit macOS 14 oder neuer und AppMeta Pulse für Mac. Ein Kauf gilt für die iPhone- und die Mac-App.
- Vollen Zugriff: ein Abo oder Lebenslang ({P_MONTHLY@appmeta-pulse} im Monat, {P_YEARLY@appmeta-pulse} im Jahr oder einmalig {P_LIFETIME@appmeta-pulse}).
- Berichte auf dem Mac, entweder über einen eigenen API-Schlüssel für App Store Connect mit der Rolle „Admin“ oder per iCloud-Synchronisierung von einem Gerät, das einen hat.
- Eine KI-App, die MCP-Server unterstützt, etwa Claude Desktop, Claude Code, Cursor oder VS Code.

Nutzt du AppMeta Pulse schon auf dem iPhone, installier die App auf deinem Mac, schalte die KI-Assistenten ein und füge die Einrichtung in deine KI-App ein. Auf der [Seite von AppMeta Pulse](/de/apps/appmeta-pulse/) steht, was die App sonst noch kann, und mit [der Anleitung zur MRR-Berechnung für App-Store-Abos](/journal/how-to-calculate-mrr-for-app-store-subscriptions/){: hreflang="en"} (auf Englisch) prüfst du jede MRR-Zahl, die dir ein Assistent nennt.
