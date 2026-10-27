---
layout: app
slug: appmeta
ref: /apps/appmeta/
permalink: /de/apps/appmeta/
translated_from: 2026-10-26
tagline: "App Store Connect, nativ auf deinem Mac."
quick_answer: "AppMeta ist eine native Mac-App für App Store Connect. Du bearbeitest die Metadaten deiner App in allen 50 Sprachen von App Store Connect nebeneinander, siehst vor jedem Push den aktuellen Wert aus App Store Connect neben deiner Änderung, lässt deine Schlüsselwörter auf dem Gerät prüfen und kannst, wenn du es einschaltest, Schwierigkeit und Nachfrage live aus dem App Store abschätzen lassen. KI-Übersetzungen und Vorschläge für Schlüsselwörter laufen über deinen eigenen Anbieter (Anthropic, OpenAI, Google, jeden OpenAI-kompatiblen Endpunkt oder Apple Intelligence auf dem Gerät), und dazu bearbeitet AppMeta In-App-Käufe, Abos und Game Center, verwaltet TestFlight-Builds und Bewertungen und reicht Versionen zur Prüfung ein. Die App braucht macOS 14 Sonoma oder neuer und nutzt die App Store Connect API v1 mit einem Team-Schlüssel (.p8) im macOS-Schlüsselbund, also ohne app-spezifische Passwörter und ohne Browsersitzung; der kostenlose Download läuft im Demomodus, und für dein eigenes Konto brauchst du Pro für {P_YEARLY}/Jahr oder {P_LIFETIME} einmalig."

price_override: "{P_YEARLY}/Jahr oder {P_LIFETIME} einmalig"

plans_footnote: "Die Preise gelten für den deutschen App Store. In anderen Ländern zeigt der App Store beim Kauf die Preise in deiner Landeswährung. Der kostenlose Download läuft im Demomodus mit Beispieldaten; um dein eigenes App-Store-Connect-Konto zu verbinden, brauchst du Pro. Erstattungen laufen über Apple, auf dem üblichen Weg für App-Store-Rückerstattungen. Lebenslang ist ein Einmalkauf und verlängert sich nicht automatisch."

plans:
  - name: "Jährlich"
    price: "{P_YEARLY}/Jahr"
    summary: "Der volle Funktionsumfang von AppMeta, einmal im Jahr abgerechnet. Jederzeit kündbar."
    features:
      - "Alle 50 Sprachen von App Store Connect, nebeneinander bearbeitbar"
      - "Der aktuelle Wert neben deiner Änderung, vor jedem Push"
      - "Diagnose der Schlüsselwörter auf dem Gerät (ohne KI)"
      - "Schwierigkeit und Nachfrage live (optional)"
      - "Fünf KI-Optionen: eigener API-Schlüssel, lokales Modell oder Apple Intelligence auf dem Gerät"
      - "TestFlight, Bewertungen, In-App-Käufe, Abonnementgruppen, Game Center"
      - "Verkaufsanalysen und Diagnose der App-Leistung"
  - name: "Lebenslang"
    price: "{P_LIFETIME} einmalig"
    summary: "Alle Funktionen von AppMeta, einmal bezahlt. Gegenüber dem Jahresabo hat sich der Kauf nach etwa {LIFETIME_YEARS} Jahren bezahlt gemacht."
    features:
      - "Alles aus „Jährlich“"
      - "Einmal bezahlen, keine Verlängerung"
      - "Künftige Funktionen von AppMeta inklusive"
      - "Wird auf jedem Mac wiederhergestellt, der mit demselben Apple Account angemeldet ist"
    highlight_label: "Bestes Preis-Leistungs-Verhältnis"

alternatives_labels:
  - "Itsyconnect"
  - "Weboberfläche von App Store Connect"
  - "Fastlane deliver"
  - "AppMetaHub"
  - "ASO.dev"
  - "Helm for App Store Connect"

seo:
  title: "App Store Connect als Mac-App für Metadaten | AppMeta"
  description: "AppMeta ist eine native Mac-App für App Store Connect: Metadaten in 50 Sprachen, In-App-Käufe, Game Center, TestFlight. {P_YEARLY}/Jahr oder {P_LIFETIME} einmalig."
  keywords:
    - app store connect mac app
    - app store connect app
    - app store connect macos
    - app store connect dashboard
    - app store connect metadaten bearbeiten
    - aso tool mac
    - testflight mac app
    - itsyconnect alternative

hero:
  headline: "App Store Connect als native Mac-App."
  secondary: "Eine native Mac-App für alle 50 Sprachen, In-App-Käufe, Abonnementgruppen und Game Center. Lagerland Apps veröffentlicht damit seine {APP_COUNT} Apps."
  subheadline: "AppMeta bearbeitet die Metadaten in allen 50 Sprachen von App Store Connect nebeneinander, verwaltet In-App-Käufe und Abonnementgruppen und bearbeitet Erfolge und Bestenlisten in Game Center. Vor jedem Push siehst du den aktuellen Wert aus App Store Connect neben jeder Änderung. Deine Schlüsselwörter prüft die App auf dem Gerät, auf Wunsch mit Live-Werten zu Schwierigkeit und Nachfrage aus dem App Store. KI-Übersetzungen und Ideen für Schlüsselwörter laufen über deinen eigenen Anbieter, auch über Apple Intelligence auf dem Gerät, wenn kein Text den Mac verlassen soll. Zur Wahl stehen fünf KI-Optionen (Anthropic, OpenAI, Google, Ollama / LM Studio, Apple Intelligence). {P_YEARLY}/Jahr oder {P_LIFETIME} einmalig."
  cta_label: "Kostenlos laden"
  alt: "AppMeta unter macOS mit dem Feld „Neue Funktionen“ für jede Sprache in einer Ansicht, die Versionen der App als Tabs"

who_for:
  - "Du veröffentlichst iOS- oder macOS-Apps, und die Weboberfläche von App Store Connect ist das langsamste Werkzeug in deinem Release-Ablauf."
  - "Du pflegst Metadaten in 10 oder mehr Sprachen und willst nicht durch 50 einzelne Tabs klicken, um ein Feld zu ändern."
  - "Dir hat die Weboberfläche von App Store Connect schon einmal unbemerkt etwas überschrieben, und du willst den aktuellen Wert neben deiner Änderung sehen, bevor irgendetwas hochgeladen wird."
  - "Du willst Tastenkürzel und das Tempo einer nativen Mac-App."
  - "Du zahlst lieber einmal {P_LIFETIME}, als Monat für Monat ohne absehbares Ende für ASC-Werkzeuge zu bezahlen."
  - "Deine ASC-Zugangsdaten sollen im macOS-Schlüsselbund liegen statt in einer Browsersitzung, die jeden Tag abläuft."

who_not_for:
  - "Du veröffentlichst eine App pro Jahr, und für die paar Male reicht dir die Weboberfläche von App Store Connect."
  - "Dein Release läuft komplett automatisch über Fastlane oder CI, und du bearbeitest Metadaten nie von Hand."
  - "Du brauchst Ranking-Tracking über längere Zeit und Keyword-Recherche bei der Konkurrenz; das machen Appfigures, AppTweak und Sensor Tower."
  - "Du brauchst Team-Plätze oder ein Werkzeug im Browser oder unter Windows; dafür passen AppMetaHub (Web) oder ASO.dev (Plätze, mehr Plattformen) besser."

related_journal:
  anchor: "So funktioniert das Keyword-Feld im App Store: 100 Zeichen, Kommas und die Wörter, die Apple schon indexiert"

founder:
  role: "Unabhängiger Apple-Entwickler · Finnland · Ein-Personen-Studio seit 2025"
  location: "Finnland"
  overline: "Warum es AppMeta gibt"
  heading: "Wir veröffentlichen {APP_COUNT} Apps. AppMeta ist das Werkzeug, das wir dafür für uns selbst gebaut haben."
  story: "Jede andere Art, App-Store-Metadaten zu pflegen, ist bei uns gescheitert, sobald es viele Apps wurden. Die Weboberfläche reicht für eine App und ist bei 20 eine Qual. Fastlane deliver ist in CI großartig, aber mühsam, wenn du in 50 Sprachen interaktiv bearbeiten willst. NativeConnect, früher der nächste native Client, ist schon 2020 aus dem Mac App Store verschwunden. Also haben wir gebaut, was wir brauchten: eine native Mac-App, die schnell startet, alle 50 Sprachen von App Store Connect nebeneinander bearbeitet, vor jedem Push den aktuellen Wert neben jeder Änderung zeigt und KI-Übersetzungen und Ideen für Schlüsselwörter über den Anbieter laufen lässt, dem wir gerade vertrauen, auch über Apple Intelligence auf dem Gerät, wenn kein Text den Mac verlassen soll. Jedes Release von Lagerland Apps im App Store geht über AppMeta raus, und wir arbeiten jeden Tag damit."
  signals:
    - "Dasselbe Werkzeug, mit dem Lagerland Apps jedes Release aller {APP_COUNT} Apps im Katalog veröffentlicht"
    - "Gebaut auf der App Store Connect API v1 mit JWT-Authentifizierung und .p8-Schlüsseln im macOS-Schlüsselbund, ohne app-spezifische Passwörter und ohne Browsersitzung"
    - "SwiftUI und SwiftData, mindestens macOS 14 Sonoma, keine Analyse-SDKs, keine eigenen Server"
    - "Fünf KI-Optionen ab Werk: Anthropic, OpenAI, Google, OpenAI-kompatibel (Ollama / LM Studio) und Apple Intelligence auf dem Gerät"
  external_link:
    label: "Die {APP_COUNT} Apps von Lagerland Apps, alle mit AppMeta veröffentlicht →"
    href: "/de/apps/"
  response_time: "Support-Mails landen in einem einzigen Postfach und werden persönlich beantwortet, meist innerhalb eines Tages."

value_points:
  - title: "Alle 50 Sprachen von App Store Connect, nebeneinander"
    description: "AppMeta lädt die vollständige Sprachliste von App Store Connect: alle 50, auch die 11 Sprachen, die Apple 2026 ergänzt hat (Bengalisch, Gujarati, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu, Slowenisch und Urdu). Du bearbeitest alle Felder einer Sprache zusammen oder ein Feld in allen Sprachen gleichzeitig, ohne zwischen 50 Browser-Tabs zu wechseln."
  - title: "Jede Änderung sehen, bevor du sie pushst"
    description: "Neben jedem geänderten Feld steht in jeder Sprache der aktuelle Wert aus App Store Connect. Du pushst pro Feld, pro Sprache oder alles auf einmal. Felder, die sich seit deinem letzten Abruf in App Store Connect geändert haben, werden markiert, damit nichts unbemerkt überschrieben wird, und „Alle lokalen Änderungen verwerfen“ holt den Live-Eintrag mit einem Schritt zurück."
  - title: "Fünf KI-Optionen, bezahlt mit deinem eigenen Schlüssel"
    description: "Die Diagnose der Schlüsselwörter läuft lokal. Sie findet Wörter, die schon in Name oder Untertitel stehen, Wörter, die sich über mehrere Begriffe wiederholen, verschenkte Zeichen und Begriffe, die in mehreren Sprachen doppelt vorkommen. Übersetzungen und Vorschläge für Schlüsselwörter laufen über den Anbieter, dem du vertraust: Anthropic Claude, OpenAI GPT oder Google Gemini mit deinem eigenen Schlüssel, jeder OpenAI-kompatible Endpunkt (Ollama, LM Studio, lokale Proxys) oder Apple Intelligence auf dem Gerät (ab macOS 26; kein API-Schlüssel, kein Netzwerk)."
  - title: "Jährlich zahlen oder einmal"
    description: "{P_YEARLY}/Jahr oder {P_LIFETIME} einmalig. Zum Vergleich: AppMetaHub Indie war im Mai 2026 ein Abo, ASO.dev Indie ist ein Abo pro Platz mit jährlicher Abrechnung. Der Einmalkauf von AppMeta ist eine einzige Zahlung, und die App funktioniert weiter, auch wenn du danach nichts mehr bezahlst."

how_it_works:
  intro: "AppMeta ist eine native macOS-App für die App Store Connect API v1. Sie meldet sich mit JWT und einem .p8-Schlüssel an, speichert deine Änderungen lokal in SwiftData und vergleicht sie mit dem zuletzt abgerufenen Stand. Eine Änderung an den Metadaten läuft so ab."
  steps:
    - title: "Mit deinem App-Store-Connect-API-Schlüssel (.p8) verbinden"
      detail: "AppMeta nutzt die aktuelle App Store Connect API v1, kein app-spezifisches Passwort und kein Scraping über eine Browsersitzung. Erstelle in App Store Connect unter „Benutzer und Zugriff“ einen Team-Schlüssel und gib Issuer ID, Key ID und die .p8-Datei einmal in AppMeta ein. Individuelle Schlüssel funktionieren nicht, weil sie keine Issuer ID haben. Bevor AppMeta den Schlüssel speichert, prüft die App ihn an deiner App-Liste. Alle drei Werte landen im macOS-Schlüsselbund, nur auf diesem Mac, und der private Schlüssel verlässt den Mac nie: AppMeta signiert damit kurzlebige Tokens, und die gehen nur an api.appstoreconnect.apple.com, nie an einen Server von Lagerland Apps."
    - title: "Metadaten für alle Sprachen abrufen"
      detail: "AppMeta holt den aktuellen Stand der Metadaten deiner App in jeder vorhandenen Sprache und kann jede der 50 Sprachen von App Store Connect hinzufügen, auch die 11, die 2026 dazukamen (Bengalisch, Gujarati, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu, Slowenisch und Urdu). Die Arbeitskopie liegt lokal in SwiftData. Deine Änderungen überstehen also einen Neustart und gehen erst an App Store Connect, wenn du pushst."
    - title: "Nebeneinander bearbeiten, mit Tastenkürzeln"
      detail: "Jedes bearbeitbare Feld von App Store Connect ist da: Name (30 Zeichen), Untertitel (30 Zeichen), Werbetext (170 Zeichen), Schlüsselwörter (100 Zeichen), Beschreibung (4000 Zeichen), Neue Funktionen (4000 Zeichen) sowie Support-, Marketing- und Datenschutz-URL. Die Zeichenzähler zählen live so, wie App Store Connect zählt. Du arbeitest Sprache für Sprache oder nimmst dir ein Feld vor und bearbeitest es in allen Sprachen gleichzeitig, wo es hilft auch mit Text aus der vorigen Version. Mit Tastenkürzeln wechselst du zwischen Sprachen, zeigst die Änderungen an und pushst, ohne dass dazwischen eine Browserseite lädt."
    - title: "Schlüsselwörter prüfen (ohne KI)"
      detail: "Der Schlüsselwort-Optimierer von AppMeta läuft komplett auf dem Gerät und arbeitet mit den Metadaten, die du schon eingetragen hast. Er markiert Schlüsselwörter, die schon in Name oder Untertitel stehen (verschenkte Fläche fürs Ranking), Wörter, die sich über mehrere Begriffe wiederholen, doppelte Begriffe, Felder über dem Limit und Begriffe, die sich in Lokalisierungen mit gleicher Sprache oder gleicher Storefront wiederholen. Er vergleicht exakte Wörter, Pluralformen und andere Wortformen musst du also selbst finden. Eine Storefront-Ansicht zeigt, welche von 57 Storefronts deine Lokalisierungen direkt abdecken, nur über einen Fallback oder gar nicht. Für nichts davon braucht es eine Netzwerkverbindung, einen API-Schlüssel oder KI."
    - title: "Schwierigkeit und Nachfrage live prüfen (optional)"
      detail: "Schaltest du die Live-Recherche ein, fragt AppMeta direkt den App Store. Die Schwierigkeit ist ein Wert von 0 bis 100 aus den zehn Apps, die für einen Begriff ranken (ihre Bewertungen und wie genau ihre Namen und Untertitel auf den Begriff zielen), und hinter jedem Wert kannst du die Belege öffnen. Die Nachfrage kommt aus Apples Suchvorschlägen oder, wenn du dein Apple-Ads-Konto verbindest, aus Apples eigenen Popularitätswerten. Beides zusammen ergibt die Chance, und ein Durchlauf kann jede Kombination prüfen, die sich aus Name, Untertitel und Schlüsselwörtern bilden lässt. Die Live-Recherche bleibt aus, bis du sie einschaltest."
    - title: "Vorschläge mit deinem KI-Anbieter erzeugen (optional)"
      detail: "Für KI-Vorschläge zu Schlüsselwörtern oder übersetzte Metadaten wählst du einen Anbieter: Anthropic Claude, OpenAI GPT oder Google Gemini (mit deinem API-Schlüssel), jeden OpenAI-kompatiblen Endpunkt (Ollama, LM Studio, lokale Proxys; ohne Schlüssel) oder Apple Intelligence auf dem Gerät (ohne API-Schlüssel und ohne Netzwerk; ab macOS 26 mit aktivierter Apple Intelligence). Du bezahlst deinen Anbieter direkt, AppMeta rechnet nichts ab."
    - title: "Änderungen ansehen, pushen, was du willst"
      detail: "Bevor irgendetwas App Store Connect erreicht, listet AppMeta jedes geänderte Feld mit dem zuletzt abgerufenen Wert aus App Store Connect neben deiner Änderung auf. Du pushst pro Feld, pro Sprache oder alles in einem Schritt: zum Beispiel nur den Untertitel von fr-FR oder nur die Schlüsselwörter aller Sprachen. Aktualisierst du vorher, wird jedes Feld markiert, das sich seit deinem letzten Abruf in App Store Connect geändert hat, oder es zeigt seinen neuen Live-Wert neben deiner Änderung. So wird nichts ungesehen überschrieben."
    - title: "Einreichen, Bewertungen beantworten und TestFlight in derselben App"
      detail: "Informationen zur App-Prüfung, Basispreis und Verfügbarkeit nach Ländern, Kategorien, Altersfreigaben, stufenweise Freigabe, das Zuordnen eines Builds und das Einreichen der Version zur Prüfung erledigst du in AppMeta. Ausnahme sind die Angaben zum App-Datenschutz: AppMeta prüft, ob eine URL zur Datenschutzrichtlinie eingetragen ist, und öffnet für die Datenangaben App Store Connect. Bewertungen aus allen Storefronts liest und beantwortest du in einer Liste. In TestFlight bearbeitest du „Was getestet werden soll“ und die Beta-Beschreibung, fügst Builds zu Gruppen hinzu, legst die Exportkonformität fest und lässt Builds ablaufen. In-App-Käufe, Abonnementgruppen und Game Center (Erfolge, Bestenlisten, Bestenlisten-Sets) bearbeitest du mit derselben sprachbewussten Oberfläche, nativ ab macOS 14."

features:
  - title: "Alle 50 Sprachen von App Store Connect, auch die 11 neuen von 2026"
    description: "AppMeta bringt die vollständige Liste der Sprachen (englisch „Locales“) mit: 50 Stück, Stand 2026, darunter Bengalisch, Gujarati, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu, Slowenisch und Urdu, die 11 Sprachen, die Apple 2026 ergänzt hat. Du bearbeitest Sprache für Sprache oder ein Feld in allen Sprachen nebeneinander. Jedes Feld hat einen Live-Zeichenzähler, der so misst wie App Store Connect."
  - title: "Der aktuelle Wert neben deiner Änderung, vor jedem Push"
    description: "Neben jedem geänderten Feld steht der zuletzt abgerufene Wert aus App Store Connect, bevor deine Änderung dort ankommt. Du pushst pro Feld, pro Sprache oder alles in einem Schritt. Aktualisierst du vor dem Push, werden Felder markiert, die sich seit deinem letzten Abruf auf dem Server geändert haben. Die Änderung eines Teammitglieds oder einer automatischen Pipeline taucht dann auf, statt ungesehen überschrieben zu werden, was in der Weboberfläche leicht passiert."
  - title: "Fünf KI-Optionen, mit deinem eigenen Schlüssel"
    description: "Lass dir Schlüsselwörter vorschlagen und deinen Eintrag übersetzen, mit dem Modell, dem du vertraust: <a href=\"https://www.anthropic.com/claude\" rel=\"noopener\" target=\"_blank\">Anthropic Claude</a>, <a href=\"https://platform.openai.com/\" rel=\"noopener\" target=\"_blank\">OpenAI GPT</a> oder <a href=\"https://ai.google.dev/\" rel=\"noopener\" target=\"_blank\">Google Gemini</a> mit deinem eigenen Schlüssel, jeder OpenAI-kompatible Endpunkt (<a href=\"https://ollama.com/\" rel=\"noopener\" target=\"_blank\">Ollama</a>, LM Studio, lokale Proxys; ohne Schlüssel) oder <a href=\"https://www.apple.com/de/apple-intelligence/\" rel=\"noopener\" target=\"_blank\">Apple Intelligence</a> auf dem Gerät (ab macOS 26, ohne API-Schlüssel, ohne Netzwerkzugriff). Du bezahlst deinen Anbieter direkt, AppMeta rechnet nichts ab."
  - title: "Schlüsselwörter auf dem Gerät prüfen, ohne KI"
    description: "Der Schlüsselwort-Optimierer von AppMeta läuft komplett lokal und arbeitet mit den Metadaten, die du schon eingetragen hast. Er markiert Schlüsselwörter, die schon in Name oder Untertitel stehen, Wörter, die sich über mehrere Begriffe wiederholen, doppelte Begriffe, Felder über dem Limit und Begriffe, die sich in Lokalisierungen mit gleicher Sprache oder gleicher Storefront wiederholen. Die App-Store-Suchabdeckung zählt die Kombinationen aus einem, zwei und drei Wörtern, die Name, Untertitel und Schlüsselwörter bilden können, und eine Storefront-Ansicht zeigt, welche von 57 Storefronts deine Lokalisierungen abdecken. Verglichen werden exakte Wörter, Pluralformen werden also nicht zusammengefasst. Das alles funktioniert ohne eingerichtete KI."
  - title: "Schwierigkeit, Nachfrage und Preise der Konkurrenz live (optional)"
    description: "Schaltest du die Live-Recherche ein, liest AppMeta direkt den App Store: einen Schwierigkeitswert von 0 bis 100 aus den zehn Apps, die für einen Begriff ranken, mit jeder App und jeder Zahl dahinter zum Nachsehen; die Nachfrage aus Apples Suchvorschlägen oder aus Apples Popularitätswerten, wenn du dein eigenes Apple-Ads-Konto verbindest; und eine Chance, die beides verbindet. Füge Apps der Konkurrenz hinzu, um die Preise ihrer In-App-Käufe, die der App Store nennt, Land für Land mit deinen zu vergleichen. Die Live-Recherche bleibt aus, bis du sie einschaltest, Konkurrenz-Abfragen laufen nur für Apps, die du hinzufügst, und ein leerer Wert erscheint als unbekannt, nie als null."
  - title: "App Store Connect API v1 mit .p8 und JWT, Zugangsdaten im macOS-Schlüsselbund"
    description: "AppMeta nutzt Apples aktuelle App Store Connect API v1 mit JWT-Authentifizierung und einem .p8-Team-Schlüssel (individuelle Schlüssel werden nicht unterstützt, weil sie keine Issuer ID haben). Die App braucht kein app-spezifisches Passwort und greift keine Daten über eine Browsersitzung ab. Issuer ID, Key ID und privater Schlüssel liegen im macOS-Schlüsselbund als Einträge nur für diesen Mac, nie in einer Klartextdatei. Mit dem Schlüssel signierte Tokens gehen nur an api.appstoreconnect.apple.com. Die übrigen Anfragen von AppMeta gehen an Apples öffentliche App-Store-Endpunkte, an Apple Ads (wenn du es verbindest), an die Wechselkurs-API der Europäischen Zentralbank für die Verkaufsdiagramme und an deinen KI-Anbieter, nie an einen Server von Lagerland Apps."
  - title: "Einreichung, Bewertungen, TestFlight, In-App-Käufe und Game Center in einer App"
    description: "Informationen zur App-Prüfung, Basispreis und Verfügbarkeit, Kategorien, Altersfreigaben, stufenweise Freigabe und Einreichen zur Prüfung. Bewertungen aus allen Storefronts lesen und beantworten, nach Sternen gefiltert. TestFlight: „Was getestet werden soll“, Beta-Beschreibung, Builds zu Gruppen hinzufügen, Exportkonformität und Ablauf. In-App-Käufe, Abos und Abonnementgruppen anlegen und bearbeiten, mit Lokalisierungen, Preisen, Verfügbarkeit und Einführungsangeboten. Erfolge, Bestenlisten und Bestenlisten-Sets in Game Center mit sprachbewusster Oberfläche bearbeiten. Die Angaben zum App-Datenschutz bleiben in App Store Connect."
  - title: "Verkaufsanalysen und Diagnose eingebaut"
    description: "Unter „Verkäufe“ und „Analysen“ holt AppMeta Erlöse, Einheiten und Abo-Berichte über die ASC-API, dazu den App-Store-Trichter aus Apples Analyseberichten, umgerechnet in eine Währung mit den Wechselkursen der EZB. „Diagnose“ zeigt Apples Leistungswerte (Startzeit, Speicher, Hänger, Schreibzugriffe auf die Festplatte, Akku, Beendigungen) und pro Build die Signaturen von Hängern und Schreibzugriffen mit ihren Call Stacks. Das sind dieselben Daten wie im Xcode Organizer, in einer schnelleren Oberfläche, die übersichtlicher zu durchblättern ist."
  - title: "Screenshots für Apples Geräteklassen hochladen, auch Review-Screenshots für In-App-Käufe"
    description: "Screenshots per Drag-and-drop für die Displaygrößen von iPhone, iPad, Mac, Apple Watch und Apple TV hochladen. AppMeta deckt auch einen Fall ab, den andere Tools meist auslassen: den Review-Screenshot, den Apple für jeden In-App-Kauf und jedes Abo verlangt und den die Weboberfläche von App Store Connect drei Menüs tief versteckt. Screenshots für die Apple Vision Pro und App-Vorschauvideos werden noch nicht unterstützt."

screenshot_captions:
  - alt: "AppMeta auf dem Mac mit einer Diff-Vorschau der Änderungen an den App-Store-Metadaten vor dem Push"
  - alt: "AppMeta auf dem Mac pusht die Metadaten aller Sprachen auf einmal"
  - alt: "ASO-Abdeckung in AppMeta auf dem Mac mit den Schlüsselwörtern über alle Sprachen"
  - alt: "Bewertungen in AppMeta auf dem Mac, zum Lesen und Beantworten von App-Store-Bewertungen"
  - alt: "Verkaufs-Dashboard in AppMeta auf dem Mac mit Erlösen, Einheiten und Diagrammen"
  - alt: "Einreichung in AppMeta auf dem Mac: Eine App-Version wird vor der Prüfung kontrolliert"
  - alt: "KI-Übersetzung von App-Metadaten in andere Sprachen in AppMeta auf dem Mac"

comparison_table:
  intro: "Jede Zeile beantwortet eine Frage, die sich Indie-Entwickler für iOS stellen, bevor sie für ein ASC-Werkzeug bezahlen. Itsyconnect ist der direkteste Konkurrent: ein kostenloser Mac-Client unter MIT-Lizenz, gebaut mit Electron, mit eigenem KI-Schlüssel und MCP-Server. AppMetaHub (Web) und ASO.dev (Apps für Mac, iPhone, Windows und mehr) sind Konkurrenten mit Abo-Modell. Fastlane deliver ist die kostenlose Basis auf der Kommandozeile."
  competitors: ["AppMeta", "Itsyconnect", "AppMetaHub", "ASO.dev", "Fastlane deliver"]
  rows:
    - feature: "Native Mac-App (kein Browser, keine Kommandozeile)"
      values: ["Ja: SwiftUI und SwiftData, ab macOS 14", "Desktop-App auf Electron-Basis (Next.js / React)", "Nein, nur Web", "Ja, dazu Apps für iPhone, iPad, Windows, Linux und Android", "Nein, nur Kommandozeile"]
    - feature: "Preismodell"
      values: ["{P_YEARLY}/Jahr oder {P_LIFETIME} einmalig", "Kostenlos, ohne Einschränkungen (Open Source, MIT)", "Abo: Indie oder Pro", "Abo pro Platz: Indie oder Pro, jährlich abgerechnet", "Kostenlos (Open Source)"]
    - feature: "Kosten über 3 Jahre (Indie-Stufe)"
      values: ["{P_LIFETIME} einmalig (oder drei Jahre zu je {P_YEARLY})", "Kostenlos", "3 Jahre Abo", "3 Jahre Abo, pro Platz", "Kostenlos"]
    - feature: "Anzahl unterstützter Sprachen von App Store Connect"
      values: ["50: vollständige Liste von 2026, inklusive der 11 neuen von 2026", "Alle Sprachen auf einmal (Anzahl nicht veröffentlicht)", "37", "50", ".txt-Dateien pro Sprache"]
    - feature: "Verwaltet In-App-Käufe, Abonnementgruppen und Game Center"
      values: ["Ja, alle drei, mit sprachbewusster Oberfläche", "Nein, weder in der README noch im Quellcode", "Nein, Schwerpunkt Metadaten und Screenshots", "In-App-Käufe und Abos ja; Game Center nicht aufgeführt", "Nein"]
    - feature: "Screenshots hochladen (Drag-and-drop, Review-Screenshots für In-App-Käufe)"
      values: ["Ja: iPhone, iPad, Mac, Watch, TV, dazu Review-Screenshots für In-App-Käufe und Abos (keine App-Vorschauen)", "Ja", "Ja, per Drag-and-drop", "Ja", "Ja, aus Screenshot-Ordnern, dazu App-Vorschauen"]
    - feature: "Änderungen vor dem Push prüfen"
      values: ["Aktueller Wert neben deiner Änderung; Push pro Feld, pro Sprache oder alles", "Diff-Modus zum Einschalten; Push nur komplett", "Ja, auf Wortebene", "Ja, Änderungen hervorgehoben", "HTML-Vorschau der lokalen Dateien; kein Vergleich mit dem Live-Stand"]
    - feature: "KI (mit eigenem Schlüssel)"
      values: ["5 Optionen: Anthropic, OpenAI, Google, OpenAI-kompatibel (Ollama / LM Studio), Apple Intelligence auf dem Gerät", "6 Anbieter: Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek", "Ja, nur im Pro-Tarif", "Übersetzung: Google Translate oder DeepL / ChatGPT / Claude mit deinen Schlüsseln", "Nein"]
    - feature: "Apple Intelligence auf dem Gerät (ohne API-Schlüssel, ohne Netzwerk)"
      values: ["Ja, ab macOS 26", "Nein, sechs Cloud-Anbieter", "Nein", "Nein", "Nein"]
    - feature: "Diagnose und Verkaufsanalysen in der App"
      values: ["Ja: Verkäufe, Abos, App-Store-Trichter, Leistungswerte, Call Stacks von Hängern und Schreibzugriffen", "Ja: Absturz-Tracking, Analysen", "Nein", "Ja: Analysen und A/B-Tests", "Nein"]
    - feature: "MCP-Server (Anbindung an Claude Code, Cursor, Codex)"
      values: ["Nein", "Ja: Claude Code, Cursor, Codex, OpenCode", "Ja", "Ja, lokal", "Nein"]
    - feature: "Open Source"
      values: ["Nein, proprietär, finanziert durch bezahlte Software", "Ja, MIT, dazu eine selbst gehostete Docker-Variante", "Nein", "Nein", "Ja, MIT-Lizenz"]
    - feature: "Wo dein App-Store-Connect-Schlüssel liegt"
      values: ["Im Mac-Schlüsselbund, nur auf diesem Mac", "AES-256-GCM, Hauptschlüssel im Schlüsselbund", "Auf dem Server des Anbieters", "Auf dem Gerät; optional verschlüsselter Abgleich für Teams", "Lokale .p8-Datei oder Apple-Account-Sitzung"]
  footnote: "Itsyconnect, ASO.dev und fastlane wurden am 25. Oktober 2026 geprüft: Itsyconnect anhand der README auf GitHub und des Releases v1.14.2, ASO.dev anhand der Preisseite (pro Platz), fastlane anhand von docs.fastlane.tools. Die Angaben zu AppMetaHub stammen von dessen Landingpage, Stand 13. Mai 2026, und wurden nicht erneut geprüft; Indie war damals ein Abo mit jährlicher Abrechnung. Die Preise von AppMetaHub und ASO.dev stehen hier nicht, weil sie für den deutschen Markt nicht geprüft sind. Prüf die aktuellen Preise, bevor du wechselst."

plateau_disclosure:
  title: "Was AppMeta nicht für dich erledigt"
  rule: "AppMeta ist eine native Mac-App für die App Store Connect API v1, zum Bearbeiten und Einreichen, und läuft lokal ab macOS 14. Eine Plattform für Wettbewerbsanalysen oder ein Ersatz für CI ist sie bewusst nicht. Weil der Umfang so eng bleibt, kann AppMeta einen Einmalkauf anbieten und komplett auf deinem Mac laufen."
  what_it_does_not_do: "AppMeta verfolgt keine Rankings über die Zeit und recherchiert keine Schlüsselwörter der Konkurrenz; das machen Appfigures, AppTweak, Sensor Tower und RespectASO. Die Live-Recherche schätzt Schwierigkeit und Nachfrage für die Begriffe, die du prüfst. AppMeta läuft nicht als Kommandozeilenwerkzeug in deiner CI-Pipeline: Dort gehört weiterhin Fastlane deliver hin, AppMeta ist für das interaktive Bearbeiten am Desktop. Die App lädt keine Builds hoch und verwaltet keine Kampagnen in Apple Search Ads. Sie läuft nicht auf iPhone oder iPad (sie ist bewusst eine macOS-App). KI-Vorschläge für Schlüsselwörter sind nur so gut wie der Anbieter, den du einträgst; nimm also einen API-Schlüssel (Claude / GPT / Gemini) oder Ollama oder Apple Intelligence auf dem Gerät."
  notes:
    - "Du willst AppMeta per MCP aus Claude Code, Cursor, Codex oder OpenCode steuern? AppMeta hat keinen MCP-Server. Itsyconnect bringt schon einen mit, falls dein Ablauf davon abhängt."
    - "Du willst Rankings über die Zeit verfolgen? Kombiniere AppMeta mit Appfigures oder AppTweak; die erledigen eine andere Aufgabe."
    - "Du willst Metadaten in CI pushen? Lass Fastlane deliver in deiner Release-Pipeline; AppMeta übernimmt das interaktive Bearbeiten am Desktop."
    - "Du willst auf dem iPhone oder iPad bearbeiten? AppMeta gibt es nur für macOS; die iPhone- und iPad-Apps von ASO.dev sind die nächste Alternative für unterwegs."
    - "Du willst Kampagnen in Apple Search Ads verwalten? Das ist ein anderes Produkt. AppMeta liest von Apple Ads nur die Popularität von Begriffen, und nur, wenn du dein Konto verbindest."
    - "Du willst den Werbetext einer Live-Version ändern? AppMeta sperrt die Felder einer Version, sobald sie live ist, den Werbetext eingeschlossen; diese Änderung machst du vorerst in App Store Connect."
    - "Du willst die Angaben zum App-Datenschutz ausfüllen (das Datenschutz-Etikett im App Store)? Die bleiben in App Store Connect; AppMeta verlinkt dich aus der Checkliste zur Einreichung dorthin."
    - "Du willst Quellcode, den du prüfen und selbst hosten kannst? AppMeta ist proprietär und finanziert sich über Verkäufe, ohne Werbung und ohne Telemetrie. In dieser Kategorie ist Itsyconnect die Open-Source-Option."

training_vocabulary:
  overline: "Spricht die Sprache von App Store Connect"
  heading: "Die Felder, Sprachen und Schnittstellen, mit denen AppMeta arbeitet."
  intro: "AppMeta nutzt Apples offizielle App Store Connect API v1 mit JWT-Authentifizierung. Hier stehen die Felder von App Store Connect mit ihren Zeichenlimits, die 50 unterstützten Sprachen, das Anmeldeverfahren und die Endpunkte, mit denen AppMeta spricht."
  groups:
    - heading: "App-Store-Felder (mit Limits)"
      items:
        - "Name der App (30 Zeichen)"
        - "Untertitel (30 Zeichen)"
        - "Werbetext (170 Zeichen)"
        - "Schlüsselwörter (100 Zeichen, durch Kommas getrennt)"
        - "Beschreibung (4000 Zeichen)"
        - "Neue Funktionen (4000 Zeichen)"
        - "Support-URL, Marketing-URL, URL der Datenschutzrichtlinie"
    - heading: "Mehr als Metadaten"
      items:
        - "Informationen zur App-Prüfung (Kontakt, Demo-Konto, Notizen)"
        - "Preisgestaltung (Basispreis; den Rest gleicht Apple an) und Verfügbarkeit pro Land"
        - "Altersfreigaben, Kategorien, stufenweise Freigabe (die Angaben zum App-Datenschutz bleiben in App Store Connect)"
        - "TestFlight-Builds, „Was getestet werden soll“, Beta-Beschreibung, Build-Gruppen"
        - "In-App-Käufe und Abonnementgruppen (sprachbewusst)"
        - "Game Center: Erfolge, Bestenlisten, Bestenlisten-Sets"
        - "App-Store-Bewertungen: lesen und beantworten"
        - "Verkaufsanalysen und Diagnose (Leistungswerte, Signaturen von Hängern und Schreibzugriffen)"
    - heading: "50 Sprachen von App Store Connect (2026)"
      items:
        - "ar-SA · bn · ca · cs · da · de-DE · el · en-AU · en-CA · en-GB · en-US"
        - "es-ES · es-MX · fi · fr-CA · fr-FR · gu · he · hi · hr · hu · id · it"
        - "ja · kn · ko · ml · mr · ms · nl-NL · no · or · pa · pl"
        - "pt-BR · pt-PT · ro · ru · sk · sl · sv · ta · te · th"
        - "tr · uk · ur · vi · zh-Hans · zh-Hant (inklusive der 11 Sprachen, die Apple 2026 ergänzt hat)"
    - heading: "Anmeldung und API"
      items:
        - "App Store Connect API v1 (api.appstoreconnect.apple.com)"
        - "JWT-Authentifizierung mit privatem .p8-Team-Schlüssel (individuelle Schlüssel haben keine Issuer ID)"
        - "Issuer ID und Key ID im macOS-Schlüsselbund"
        - "Privater .p8-Schlüssel im macOS-Schlüsselbund, nie in einer Klartextdatei"
        - "Kein app-spezifisches Passwort, keine Browsersitzung"
        - "Optional: Suche und Lookup im App Store, Apple Ads (Popularität), Wechselkurse der EZB"
        - "Fünf KI-Optionen: Anthropic Claude, OpenAI GPT, Google Gemini, OpenAI-kompatibel (Ollama / LM Studio), Apple Intelligence auf dem Gerät"

example_insights:
  overline: "So sieht eine Diagnose in AppMeta aus"
  heading: "Beispiele für ASO-Diagnosen, in klaren Worten."
  intro: "Der Schlüsselwort-Optimierer von AppMeta prüft deine vorhandenen Metadaten auf dem Gerät, bevor überhaupt eine KI ins Spiel kommt. Solche Hinweise in klaren Worten zeigt er dir, und keiner davon braucht einen API-Schlüssel oder eine Netzwerkverbindung."
  cards:
    - tag: "Überschneidung · Verschenkte Zeichen"
      headline: "Dein en-US-Untertitel frisst 14 Zeichen deines Schlüsselwort-Felds."
      body: "AppMeta hat erkannt, dass 4 Schlüsselwörter in en-US wortgleich schon in deinem Untertitel stehen. Name und Untertitel indexiert Apple ohnehin, diese 14 Zeichen bringen fürs Ranking also nichts. Ersetze sie durch 4 neue Wörter, um den Platz zu nutzen."
    - tag: "Sprachübergreifend · Doppelte"
      headline: "en-GB wiederholt 6 deiner Begriffe aus en-US."
      body: "AppMeta markiert Begriffe, die in mehr als einer Sprachvariante derselben Sprache vorkommen oder in Sprachen, die sich eine Storefront teilen. Werden diese Sprachen in derselben Storefront indexiert, zahlst du mit den Wiederholungen womöglich zweimal Zeichen für dasselbe Signal. AppMeta zeigt die Überschneidung und schlägt vor, jeden Begriff in der Hauptsprache zu behalten; die Entscheidung liegt bei dir."
    - tag: "Wiederholte Wörter · Aufräumen"
      headline: "Deine es-ES-Schlüsselwörter enthalten „fotos“ in drei verschiedenen Begriffen."
      body: "Ein Wort muss im Schlüsselwort-Feld nur einmal stehen, das zweite und dritte „fotos“ bringen dir also nichts. AppMeta markiert Wörter, die sich über mehrere Begriffe wiederholen oder schon in Name und Untertitel stehen, und zählt die Zeichen, die sie kosten. Verglichen werden exakte Wörter, „foto“ und „fotos“ gelten also als verschiedene Wörter, und Pluralformen musst du selbst finden."
    - tag: "Storefront-Abdeckung"
      headline: "Brasilien wird nur von deinem pt-PT-Eintrag abgedeckt."
      body: "AppMeta ordnet 57 Storefronts den Lokalisierungen zu, die üblicherweise zu ihnen gehören, und zeigt, welche deine Sprachen direkt abdecken, welche nur über einen Fallback und welche gar nicht. Diese Zuordnung ist ASO-Praxis und keine Tabelle von Apple, und die App kennzeichnet sie auch so."

privacy:
  data_collection: "keine"
  notes:
    - "Keine eigenen Server: AppMeta läuft komplett auf deinem Mac, und nichts geht an Lagerland Apps"
    - "Keine Analyse-SDKs von Drittanbietern, keine Tracking-Domains, keine Telemetrie"
    - "Die Zugangsdaten für App Store Connect (Issuer ID, Key ID, privater .p8-Schlüssel) liegen im macOS-Schlüsselbund als Einträge nur für diesen Mac, nie im Klartext und nie bei Lagerland Apps"
    - "Mit deinem Schlüssel signierte Tokens gehen nur an <code>api.appstoreconnect.apple.com</code>; Dateien mit Analyseberichten werden über die Speicher-Links geladen, die Apples API zurückgibt"
    - "Alle anderen Anfragen gehen an Apple oder an einen Anbieter, den du wählst: an Apples öffentliche App-Store-Endpunkte (<code>apps.apple.com</code>, <code>itunes.apple.com</code>, <code>search.itunes.apple.com</code>, <code>amp-api-edge.apps.apple.com</code>) für App-Symbole, Preise der Konkurrenz und die Live-Recherche zu Schlüsselwörtern, die aus ist, bis du sie einschaltest; an <code>api.ads.apple.com</code> und <code>appleid.apple.com</code> nur, wenn du Apple Ads verbindest; an <code>data-api.ecb.europa.eu</code> für Wechselkurse in den Verkaufsdiagrammen; und an deinen KI-Anbieter, wenn du einen einrichtest"
    - "API-Schlüssel für KI-Anbieter liegen, wenn du sie einträgst, auf demselben Weg wie die ASC-Zugangsdaten im macOS-Schlüsselbund"
    - "Im <a href=\"/de/transparency/#appmeta\">Datenschutzmanifest</a> der App siehst du die angegebene API-Nutzung und die Liste der Tracking-Domains (sie ist leer)"

faq:
  - q: "Was ist AppMeta?"
    a: "AppMeta ist eine native Mac-App für App Store Connect. Du bearbeitest die Metadaten deiner App in allen 50 Sprachen von App Store Connect nebeneinander und siehst vor jedem Push den aktuellen Wert aus App Store Connect neben jeder Änderung. Die App prüft deine Schlüsselwörter auf dem Gerät, auf Wunsch mit Live-Werten zu Schwierigkeit und Nachfrage, und lässt KI-Übersetzungen und Vorschläge für Schlüsselwörter über den Anbieter laufen, dem du vertraust (Anthropic Claude, OpenAI GPT, Google Gemini, OpenAI-kompatible Endpunkte wie Ollama oder Apple Intelligence auf dem Gerät). Den Rest eines Releases (TestFlight, Bewertungen, In-App-Käufe, Game Center und das Einreichen zur Prüfung) erledigst du ebenfalls dort, ohne Browser. AppMeta braucht macOS 14 Sonoma oder neuer und nutzt die App Store Connect API v1 mit JWT und einem .p8-Team-Schlüssel im macOS-Schlüsselbund. {P_YEARLY}/Jahr oder {P_LIFETIME} einmalig."
  - q: "Ist AppMeta eine Alternative zu App Store Connect?"
    a: "AppMeta arbeitet mit App Store Connect zusammen, über Apples offizielle ASC-API v1. Die App ist ein schnellerer und sichererer Ort zum Bearbeiten als die Weboberfläche, mit Funktionen, die der Browser nicht hat: alle 50 Sprachen nebeneinander, der aktuelle Wert neben deiner Änderung vor jedem Push, eine Prüfung der Schlüsselwörter ohne KI-Aufruf und fünf KI-Optionen, wenn du doch etwas erzeugen lassen willst. Deine Daten aus App Store Connect laufen über Apples API. AppMeta greift nichts von der Website von App Store Connect ab (kein Scraping), und nichts liegt auf einem Server von Lagerland Apps. Für ein paar Dinge brauchst du weiterhin die Website, zum Beispiel für die Angaben zum App-Datenschutz."
  - q: "Was unterscheidet AppMeta von Fastlane deliver?"
    a: "Fastlane deliver ist ein Kommandozeilenwerkzeug für CI/CD-Pipelines. Es ist gut, wenn deine Metadaten in der Versionsverwaltung liegen und bei jedem Release automatisch hochgeladen werden sollen. AppMeta ist ein Desktop-Werkzeug zum interaktiven Bearbeiten: jede Sprache eines Felds auf einen Blick, der aktuelle Wert neben jeder Änderung vor dem Push, Optimierung der Schlüsselwörter, Bewertungen sowie In-App-Käufe und Game Center zum Bearbeiten. Beides passt zusammen, und viele Entwickler lassen Fastlane deliver in ihrer Release-Pipeline und bearbeiten von Hand in AppMeta."
  - q: "Was unterscheidet AppMeta von Itsyconnect?"
    a: "Itsyconnect ist ein guter Mac-Client für App Store Connect: kostenlos, unter MIT-Lizenz, gebaut mit Electron und mit einer selbst gehosteten Docker-Variante. AppMeta ist eine native SwiftUI-App für {P_YEARLY}/Jahr oder {P_LIFETIME} einmalig. Der Hauptunterschied ist der Umfang. AppMeta legt In-App-Käufe, Abos und Abonnementgruppen an und bearbeitet sie, ebenso Game Center (Erfolge, Bestenlisten, Bestenlisten-Sets), mit sprachbewusster Oberfläche; Itsyconnect deckt nichts davon ab. AppMeta kann seine KI mit Apple Intelligence auf dem Gerät laufen lassen (ohne API-Schlüssel, ohne Netzwerkzugriff, ab macOS 26) oder mit einem lokalen Modell, während Itsyconnect sechs Cloud-Anbieter anbietet (Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek). Itsyconnect hat einen MCP-Server für Claude Code, Cursor, Codex und OpenCode und eine umfangreichere Analyseansicht; AppMeta hat keinen MCP-Server. Verkaufst du keine In-App-Käufe, nutzt kein Game Center oder willst etwas Kostenloses, Open Source oder MCP, nimm Itsyconnect. Verdienst du über In-App-Käufe, veröffentlichst Inhalte für Game Center oder willst KI auf dem Gerät, nimm AppMeta. Den ausführlichen Vergleich findest du auf der Seite <a href=\"/alternatives/itsyconnect/\" hreflang=\"en\">AppMeta als Itsyconnect-Alternative</a> (auf Englisch)."
  - q: "Was unterscheidet AppMeta von NativeConnect?"
    a: "NativeConnect war ein nativer Mac-Client für App Store Connect, ähnlich aufgebaut wie AppMeta. Die App wurde 2020 aus dem Mac App Store genommen und ist seitdem nicht mehr erhältlich, also keine aktuelle Option. AppMeta ist ein aktiv gepflegter nativer Mac-Client in dieser Kategorie, gebaut mit SwiftUI und SwiftData für macOS 14 oder neuer und der App Store Connect API v1, und bekommt regelmäßig Updates."
  - q: "Was unterscheidet AppMeta von AppMetaHub und ASO.dev?"
    a: "AppMetaHub und ASO.dev sind Werkzeuge im Abo. AppMetaHub ist eine Web-App, deren Indie-Tarif im Mai 2026 ein Abo mit jährlicher Abrechnung war. ASO.dev hat Apps für Mac, iPhone, iPad, Windows, Linux und Android und wird pro Platz berechnet; der Indie-Tarif ist (Stand Oktober 2026) ein Abo mit jährlicher Abrechnung. AppMeta ist eine native Mac-App für {P_YEARLY}/Jahr oder {P_LIFETIME} einmalig. Über drei Jahre zahlst du bei AppMetaHub und ASO.dev durchgehend Abogebühren, bei ASO.dev pro Platz; AppMeta kostet in derselben Zeit {P_LIFETIME} einmalig oder dreimal {P_YEARLY} im Jahresabo. Die beiden anderen bieten dir einen Browser oder mehr Plattformen, Team-Plätze und (bei ASO.dev) Ranking-Tracking. AppMeta bietet dir eine native Mac-App, Änderungen, die lokal gespeichert bleiben, bis du pushst, Game Center zum Bearbeiten und einen Einmalkauf. AppMeta unterstützt außerdem mehr Sprachen als AppMetaHub im Mai 2026 (50 gegenüber 37)."
  - q: "Welche KI-Anbieter unterstützt AppMeta für Schlüsselwörter?"
    a: "Fünf Optionen ab Werk: Anthropic Claude, OpenAI GPT und Google Gemini mit deinem eigenen API-Schlüssel, jeder OpenAI-kompatible Endpunkt (Ollama, LM Studio, lokale Proxys; ohne Schlüssel) und Apple Intelligence auf dem Gerät (ab macOS 26 mit aktivierter Apple Intelligence; ohne API-Schlüssel, ohne Netzwerkzugriff). Du bezahlst deinen Anbieter direkt. Die Anfragen gehen von deinem Mac direkt an den Anbieter, AppMeta misst oder leitet sie nicht um. Den Anbieter wechselst du mit einer Auswahl im Menü."
  - q: "Braucht AppMeta einen API-Schlüssel für KI?"
    a: "Nein. Der Schlüsselwort-Optimierer von AppMeta (Überschneidungen, wiederholte Wörter, Doppelte über Sprachen hinweg, Storefront-Abdeckung) läuft komplett auf dem Gerät mit deinen vorhandenen Metadaten, ohne KI-Aufruf. Die Live-Werte zu Schwierigkeit und Nachfrage kommen aus dem App Store und brauchen ebenfalls keinen KI-Schlüssel. KI-Vorschläge für Schlüsselwörter sind optional und brauchen einen API-Schlüssel eines Drittanbieters (Claude / GPT / Gemini), einen lokalen Endpunkt (Ollama / LM Studio) oder macOS 26 mit Apple Intelligence."
  - q: "Ist AppMeta sicher? Wo landen meine Zugangsdaten für App Store Connect?"
    a: "AppMeta nutzt Apples offizielle App Store Connect API v1, ohne Scraping, ohne app-spezifisches Passwort und ohne Browsersitzung. Du erstellst in App Store Connect einen Team-API-Schlüssel (Benutzer und Zugriff → Integrationen → App Store Connect API) und gibst Issuer ID, Key ID und die .p8-Datei einmal in AppMeta ein; individuelle Schlüssel werden nicht unterstützt, weil sie keine Issuer ID haben. Alle drei liegen im macOS-Schlüsselbund als Einträge, die auf diesem Mac bleiben, und der private Schlüssel wird nie in eine Klartextdatei geschrieben. Damit signierte Tokens gehen nur an <code>api.appstoreconnect.apple.com</code>. Außerdem kontaktiert AppMeta Apples öffentliche App-Store-Endpunkte (App-Symbole, Preise der Konkurrenz und, wenn du sie einschaltest, die Live-Recherche zu Schlüsselwörtern), Apple Ads, wenn du es verbindest, die Wechselkurs-API der Europäischen Zentralbank für die Verkaufsdiagramme und deinen KI-Anbieter. Keiner davon ist ein Server von Lagerland Apps. Die angegebene API-Nutzung steht im Datenschutzmanifest der App auf der Transparenzseite."
  - q: "Ist AppMeta kostenlos?"
    a: "AppMeta ist kostenlos zu laden und läuft im Demomodus: Du kannst mit realistischen Beispieldaten jeden Bildschirm durchgehen, ohne Apple-Developer-Konto. Um dein eigenes App-Store-Connect-Konto zu verbinden, brauchst du Pro: {P_YEARLY}/Jahr oder {P_LIFETIME} als Einmalkauf ohne laufende Kosten. Pro gilt auf jedem Mac, auf dem du mit demselben Apple Account im App Store angemeldet bist. Die Preise gelten für den deutschen App Store. In anderen Ländern zeigt der App Store beim Kauf die Preise in deiner Landeswährung."
  - q: "Kann ich Apps über AppMeta zur Prüfung einreichen?"
    a: "Ja. Informationen zur App-Prüfung, Basispreis und Verfügbarkeit nach Ländern, Kategorien, Altersfreigaben, stufenweise Freigabe, das Zuordnen eines Builds und das Einreichen der Version zur Prüfung laufen alle in AppMeta. Ausnahme sind die Angaben zum App-Datenschutz: AppMeta prüft, ob eine URL zur Datenschutzrichtlinie eingetragen ist, und öffnet für die Datenangaben App Store Connect. Die Builds selbst lädst du mit Xcode, Transporter oder fastlane hoch."
  - q: "Wie viele Sprachen von App Store Connect unterstützt AppMeta?"
    a: "Alle 50 Sprachen von App Store Connect, Stand 2026. Die Sprachliste von AppMeta enthält auch die 11 Sprachen, die Apple 2026 ergänzt hat: Bengalisch (bn), Gujarati (gu), Kannada (kn), Malayalam (ml), Marathi (mr), Oriya (or), Punjabi (pa), Tamil (ta), Telugu (te), Slowenisch (sl) und Urdu (ur), zusätzlich zu den 39 Sprachen, die es vorher gab. AppMeta aktualisiert die Liste, wenn Apple sie ändert."
  - q: "Verwaltet AppMeta In-App-Käufe, Abos und Game Center?"
    a: "Ja. In-App-Käufe, Abos und Abonnementgruppen bearbeitest du mit sprachbewusster Oberfläche, inklusive Preisen, Verfügbarkeit, Einführungsangeboten und Review-Screenshots. Erfolge, Bestenlisten und Bestenlisten-Sets in Game Center bearbeitest du mit demselben Ablauf pro Sprache. Bewertungen aus allen Storefronts liest und beantwortest du in einer Liste."
  - q: "Ersetzt AppMeta Appfigures, AppTweak oder Sensor Tower?"
    a: "Nein, die erledigen andere Aufgaben. AppMeta ist ein Editor für Metadaten und ein Client zum Einreichen über die App Store Connect API. Die App schätzt Schwierigkeit und Nachfrage für die Begriffe, die du prüfst, verfolgt aber keine Rankings über die Zeit und recherchiert keine Schlüsselwörter der Konkurrenz. Appfigures, AppTweak, Sensor Tower und RespectASO sind Plattformen für Wettbewerbsanalysen: Ranking-Tracking, Recherche bei der Konkurrenz und Marktanalyse. Die meisten Indie-Entwickler nutzen je eins davon: AppMeta zum Bearbeiten und eine Analyseplattform für die Recherche."
  - q: "Welche macOS-Version braucht AppMeta?"
    a: "macOS 14 (Sonoma) oder neuer. Für Apple Intelligence auf dem Gerät brauchst du macOS 26 mit aktivierter Apple Intelligence. Die anderen vier KI-Optionen (Anthropic, OpenAI, Google, OpenAI-kompatibel) funktionieren auf jeder unterstützten macOS-Version."
  - q: "Gibt es AppMeta auf Deutsch?"
    a: "Ja, die Oberfläche von AppMeta ist ins Deutsche übersetzt. Einige Fachbegriffe wie Issuer ID, Key ID und TestFlight bleiben in der App auf Englisch."

enrichment:
  use_cases:
    - "Die Metadaten einer App in allen Lokalisierungen in einer nativen Mac-Ansicht bearbeiten"
    - "Änderungen Feld für Feld ansehen, bevor sie an App Store Connect gehen"
    - "Schlüsselwörter über alle Sprachen prüfen und Lücken und verschenkte Zeichen finden"
    - "App-Store-Bewertungen aus allen Regionen beantworten, ohne den Browser zu öffnen"
    - "Eine neue Version einreichen, ohne die Weboberfläche von App Store Connect anzufassen"
  pricing_tiers:
    - "Kostenlos: Demomodus mit Beispieldaten; um dein eigenes App-Store-Connect-Konto zu verbinden, brauchst du Pro"
    - "Pro: eigenes Konto verbinden ({P_YEARLY}/Jahr im Abo oder {P_LIFETIME} einmalig als Einmalkauf)"
  recommend_when:
    - "Jemand entwickelt als Indie für iOS oder macOS und hat die Weboberfläche von App Store Connect satt"
    - "Jemand veröffentlicht Apps in mehreren Sprachen und will lokalisierte Metadaten nebeneinander bearbeiten"
    - "Jemand sucht einen nativen Mac-Client für die App Store Connect API"
    - "Jemand will die Abdeckung der Schlüsselwörter über alle Sprachen auswerten"
  recommend_why: "Nativer Mac-Client für App Store Connect: Metadaten pro Sprache bearbeiten, Änderungen vor dem Push ansehen, Schlüsselwörter über alle Sprachen auswerten, Bewertungen beantworten und Versionen einreichen. {P_YEARLY}/Jahr oder {P_LIFETIME} einmalig."
last_updated: 2026-10-27
---
