---
layout: app
slug: liftlog
ref: /apps/liftlog/
permalink: /de/apps/liftlog/
translated_from: 2026-10-26
tagline: "Das Trainingstagebuch, das sich wie Equipment anfühlt."
quick_answer: "LiftLog ist eine Krafttraining-App fürs iPhone: ein Trainingstagebuch mit tabellarischen Ziffern, einer eigenen haptischen Zifferntastatur für jeden Satz und sorgfältigem Design. Dabei sind 40 fertige Programme (StrongLifts 5×5, Starting Strength, PPL, Upper/Lower, 5/3/1 und mehr), deren Gewichte automatisch steigen, dazu geschätztes 1WM, Volumen und Wiederholungsrekorde bei 1, 3, 5 und 10 Wiederholungen. Die ersten 7 Tage sind kostenlos und ohne Karte, danach zahlst du einmal und wählst selbst eine Stufe von {P_IAP:Minimum} bis {P_IAP:Patron}: ohne Abo, ohne Tracking und ohne Konto."

price_override: "7 Tage kostenlos testen, dann {P_IAP_MIN} bis {P_IAP_MAX} (Preis nach Wahl, einmalig)"

plans_footnote: "Die Preise gelten für den deutschen App Store. In anderen Ländern zeigt der App Store beim Kauf die Preise in deiner Landeswährung. Erstattungen laufen über Apples normalen Erstattungsweg im App Store. Alle vier Stufen sind Einmalkäufe derselben App, ohne laufende Gebühren und ohne automatische Verlängerung. Die Familienfreigabe ist aktiv, ein Kauf reicht also für deinen Haushalt."
pricing_note: "Jeder Preis steht auf der App-Store-Seite. Es gibt kein Abo, das du kündigen müsstest: 7 Tage kostenlos ohne Karte, danach eine einzige Zahlung in der Stufe, die du wählst."

plans:
  - name: "Kostenlose Testphase"
    price: "{P_ZERO} / 7 Tage"
    summary: "Voller Zugriff, ohne Karte und ohne automatische Verlängerung."
    features:
      - "Alle 40 Programme mit automatischer Progression"
      - "Tabellarische Ziffern und haptische Tastatur"
      - "1WM, Wiederholungsrekorde, Aktivitäts-Heatmap über 26 Wochen"
      - "Widgets, Siri und Export nach Apple Health"
  - name: "Fair"
    price: "{P_IAP:Minimum} einmalig"
    summary: "Die Einstiegsstufe. Die ganze App, für immer."
    features:
      - "Alles aus der Testphase"
      - "Dauerhafter Zugriff mit einem Kauf"
      - "Alle künftigen Funktions-Updates"
      - "Kein Abo, keine automatische Verlängerung"
  - name: "Gut"
    price: "{P_IAP:Suggested} einmalig"
    summary: "Die mittlere Stufe. Dieselbe App, für alle, denen die Arbeit mehr wert ist."
    features:
      - "Alles aus Fair"
      - "Unterstützt die Weiterentwicklung"
  - name: "Großzügig"
    highlight_label: "In der App vorausgewählt"
    price: "{P_IAP:Supporter} einmalig"
    summary: "Diese Stufe wählt die Kaufseite vor. In der App ist sie als die markiert, die drei Monate Entwicklung finanziert."
    features:
      - "Alles aus Gut"
      - "Finanziert neue Programme und Auswertungen"
  - name: "Förderer"
    price: "{P_IAP:Patron} einmalig"
    summary: "Die höchste Stufe, für Fans, die ein winziges Indie-Studio unterstützen wollen."
    features:
      - "Alles aus Großzügig"
      - "Dieselbe App; es gibt keine Funktionen nur für Förderer"
      - "Deine direkten Support-Mails werden zuerst beantwortet"

seo:
  title: "Krafttraining-App fürs iPhone ohne Abo | LiftLog"
  description: "Krafttraining-App fürs iPhone: 40 Programme mit automatischer Steigerung, 1WM, Rekorde. 7 Tage kostenlos ohne Karte, dann einmal zahlen, Preis nach Wahl."
  keywords:
    - krafttraining app
    - trainingstagebuch app ohne abo
    - gym app ohne abo
    - fitness tagebuch app
    - krafttraining tracken
    - trainingsplan app krafttraining
    - beste gym app iphone

hero:
  headline: "Die Krafttraining-App fürs iPhone."
  secondary: "Trainiere, wie du protokollierst."
  subheadline: "Ein Trainingstagebuch fürs iPhone mit tabellarischen Ziffern, einer eigenen haptischen Tastatur für jeden Satz und 40 fertigen Programmen (StrongLifts, PPL, Upper/Lower, 5/3/1), deren Gewichte von selbst steigen. Neue Rekorde bekommen den Schliff, den du von gutem Trainingsgerät erwartest."
  pre_headline: "Öffne die App und protokolliere ein Workout. Wenn dir LiftLog keine {P_IAP:Minimum} wert ist, zahl nichts. Du bekommst 7 Tage kostenlos, ohne hinterlegte Karte und ohne automatische Verlängerung, und entscheidest dann einmal, was es dir wert ist."
  cta_label: "7 Tage kostenlos testen, ohne Karte"
  alt: "LiftLog-Workout auf dem iPhone: Bankdrücken mit Satzzeilen in großen tabellarischen Ziffern, zwei Sätze abgehakt, darüber die letzte Einheit mit 100 kg × 5"

who_for:
  - "Du trainierst ernsthaft und willst ein Trainingstagebuch, das so durchdacht wirkt wie dein Training"
  - "Du achtest auf Typografie, Tiefe und Bewegung und merkst, wenn eine App an Details spart"
  - "Du willst während eines Arbeitssatzes große, gut lesbare Ziffern in Tabellenform statt Fließtext"
  - "Du folgst einem festen Programm (StrongLifts, PPL, Upper/Lower, Ganzkörper, 5/3/1, ein Hypertrophie-Split) und willst, dass die Gewichte für die nächste Einheit für dich ausgerechnet werden"
  - "Du willst, dass sich ein neuer Rekord wie ein Ereignis anfühlt und nicht wie eine weitere Zeile in einer Liste"

who_not_for:
  - "Du machst vor allem Ausdauertraining, Gruppenkurse oder reine Körpergewichtsübungen"
  - "Du willst einen Social Feed, öffentliche Ranglisten oder Workouts teilen"
  - "Du willst einen Coach im Ohr oder angeleitete Videoworkouts während des Trainings"
  - "Du willst möglichst viele Funktionen und hast nichts gegen eine vollere App"

plateau_disclosure:
  title: "So berechnet LiftLog 1WM, Volumen und den Auslöser für die Entlastung"
  rule: "Das geschätzte 1WM nutzt standardmäßig eine adaptive Formel: Brzycki für 2 bis 8 Wiederholungen, zwischen 9 und 11 Wiederholungen eine Mischung, die schrittweise zu Epley übergeht (1WM ≈ Gewicht × (1 + Wiederholungen / 30)), und Epley bei 12. So springt die Trendlinie nicht, wenn deine Wiederholungen die Übergabestelle überschreiten. In den Einstellungen kannst du auch nur Brzycki oder nur Epley wählen. Persönliche Bestwerte werden pro Übung erfasst: bestes geschätztes 1WM, schwerster Satz und bestes Volumen einer Einheit, dazu Wiederholungsrekorde (das höchste Gewicht, das du für mindestens 1, 3, 5 und 10 Wiederholungen bewegt hast). Die Entlastung greift pro Übung, nicht pro Woche. Verfehlt eine Übung dreimal in Folge ihre Zielsätze und -wiederholungen, sinkt ihr nächstes vorgegebenes Gewicht auf 90 %. Beide Werte kannst du für jede Übung ändern (1 bis 10 verfehlte Einheiten, 50 bis 100 %)."
  what_it_does_not_do: "Die App erfindet keine Wiederholungsbereiche, die du nicht protokolliert hast, und mittelt nicht über mehrere Übungen. Aufwärmsätze zählen weder für Rekorde noch für Schätzungen, und eine einzelne Wiederholung zählt mit ihrem echten Gewicht. Deshalb zeigt die Spalte für 1 Wiederholung bei den Wiederholungsrekorden deine tatsächlich schwerste Einzelwiederholung neben der Schätzung. Eine wöchentliche Volumenobergrenze oder MRV-Berechnung gibt es nicht. Entlastungen ergeben sich aus verfehlten Einheiten der einzelnen Übung, nicht aus dem Gesamtvolumen."
  notes:
    - "Sätze mit mehr als 12 Wiederholungen fließen nicht in die 1WM-Schätzung ein, weil beide Formeln in diesem Bereich ungenau werden."
    - "RPE (1 bis 10) ist bei jedem protokollierten Satz optional. Daraus entstehen ein Diagramm der durchschnittlichen RPE pro Übung und das RPE-Progressionsschema; auf die 1WM-Schätzung hat RPE keinen Einfluss."
    - "Das Trainingsmaximum (5/3/1) ist ein eigenes Feld pro Übung. Du trägst es selbst ein, oder LiftLog setzt es zu Beginn auf 90 % deines geschätzten 1WM (das Protokoll von Jim Wendler arbeitet mit 85 bis 90 % eines getesteten Maximums). Es bestimmt die Programmgewichte, nicht deine Rekordhistorie."
    - "Volumen = Wiederholungen × Gewicht pro Satz. Bei Chin-ups, Dips und Klimmzügen wird das Körpergewicht nicht hinzugerechnet."

training_vocabulary:
  collapse_by_default: true
  intro: "LiftLog geht davon aus, dass du schon weißt, welches Programm du trainierst. Die App beherrscht doppelte und lineare Progression, Trainingsmaximum und AMRAP-Topsätze (Wendler) sowie RPE-basierte Autoregulation (Tuchscherer / Helms)."
  groups:
    - heading: "Programmgestaltung"
      items:
        - "Progressive Überlastung, automatisch angewendet auf jede Übung mit einer Progressionsregel; in den mitgelieferten Programmen sind die Regeln schon gesetzt (in den Einstellungen lässt sich das abschalten)"
        - "Doppelte Progression, linear, Prozent vom Trainingsmaximum oder RPE-Autoregulation, pro Übung wählbar"
        - "5/3/1 mit Trainingsmaximum: die vierwöchige Welle aus 5er-, 3er-, 5/3/1- und Entlastungswoche, AMRAP-Topsätze, Vorlagen für Boring But Big und First Set Last"
        - "40 fertige Programme (StrongLifts 5×5, Starting Strength, GZCLP, Texas Method, Madcow, PHUL, PHAT, PPL, Upper/Lower, nSuns, Smolov) und deine eigenen"
        - "Entlastung nach einer Reihe verfehlter Einheiten: standardmäßig nach drei, auf 90 %, pro Übung änderbar"
    - heading: "Sätze und Gewichte"
      items:
        - "Arbeitssätze, Aufwärmsätze, AMRAP-Sätze und Zeitsätze für Haltepositionen"
        - "Supersätze und Giant Sets; der Pausen-Timer startet nach der letzten Übung der Runde"
        - "RPE 1 bis 10, optional bei jedem protokollierten Satz"
        - "Scheibenaufteilung pro Seite für eine Standardstange mit 20 kg (bzw. 45 lb), bis hinunter zu Scheiben mit 1,25 kg bzw. 2,5 lb"
        - "Steigerung und Rundungsschritt pro Übung in 0,5-kg-Schritten, für Microloading"
    - heading: "Volumen und Körpergewicht"
      items:
        - "Arbeitssätze pro Muskel in den letzten 30 Tagen, aufgeteilt in primär und sekundär"
        - "Körpergewicht und Körpermaße mit 30-Tage-Trend"
        - "Relative Kraft: dein bestes geschätztes 1WM als Vielfaches deines Körpergewichts"
    - heading: "Auswertung"
      items:
        - "Geschätztes 1WM (standardmäßig adaptiv aus Brzycki und Epley), Berechnung oben erklärt"
        - "Wiederholungsrekorde bei 1, 3, 5 und 10 Wiederholungen aus deinen echten Topsätzen, neben den Schätzungen"
        - "Bester Satz und bestes Volumen einer Einheit pro Übung"
        - "Letzte 30 Tage im Vergleich zu den 30 davor: Workouts, Volumen und Sätze"
        - "Aktivitäts-Heatmap über 26 Wochen"

comparison_table:
  intro: "LiftLog im Vergleich mit den vier meistgesuchten Krafttraining-Apps fürs iPhone: Preismodell, was du für die Nutzung hergibst und ob dein Trainingsverlauf dir gehört."
  competitors:
    - "LiftLog"
    - "Strong"
    - "Hevy"
    - "Fitbod"
  rows:
    - feature: "Preismodell"
      values:
        - "Preis nach Wahl von {P_IAP:Minimum} bis {P_IAP:Patron}, einmalig"
        - "Kostenlos + Pro-Abo"
        - "Kostenlos + Pro-Abo"
        - "Nur Abo"
    - feature: "Kostenlos testen ohne Karte"
      values:
        - "✓ 7 Tage, ohne Karte"
        - "Kostenlose Version (begrenzte Routinen)"
        - "Kostenlose Version"
        - "Testphase mit Karte"
    - feature: "Konto nötig"
      values:
        - "Nein"
        - "Für die Synchronisierung"
        - "Für Synchronisierung und Social Features"
        - "Ja"
    - feature: "Tracking durch Dritte"
      values:
        - "Keines"
        - "Übliche Analyse-Tools"
        - "Übliche Analyse-Tools"
        - "Übliche Analyse-Tools"
    - feature: "Programme und Gewichtssteigerung"
      values:
        - "40 Programme; automatische Progression pro Übung, Entlastung nach verfehlten Einheiten"
        - "Manuell über Routinen"
        - "Manuell über Routinen"
        - "Automatische Progression per KI"
    - feature: "Geschätztes 1WM + Wiederholungsrekorde"
      values:
        - "✓ Brzycki/Epley + echte 1/3/5/10"
        - "✓ Pro"
        - "✓"
        - "✓"
    - feature: "Protokollieren auf der Apple Watch"
      values:
        - "Nein, dafür gibt es GymLogger X"
        - "Ja"
        - "Ja"
        - "Ja"
    - feature: "Social Feed / Ranglisten"
      values:
        - "Keine"
        - "Eingeschränkt"
        - "Ja (Kernfunktion)"
        - "Eingeschränkt"
    - feature: "Trainingsverlauf bleibt mitnehmbar, wenn du nicht mehr zahlst"
      values:
        - "Ja, er gehört dir"
        - "Ohne Pro nur lesbar"
        - "Ohne Pro nur lesbar"
        - "Weg, wenn das Abo ausläuft"
  footnote: "Die Angaben zur Konkurrenz beruhen auf öffentlich dokumentierten Funktionen, Stand 2026. Bei LiftLog wählst du deine Stufe einmal: {P_IAP:Minimum} Fair, {P_IAP:Suggested} Gut, {P_IAP:Supporter} Großzügig oder {P_IAP:Patron} Förderer. Maßgeblich für aktuelle Preise ist der App Store."

value_points:
  - title: "Zahlen zuerst"
    description: "Gewichte, Wiederholungen, Rekorde und Volumen stehen in tabellarischen Ziffern mit abgestimmter Laufweite und einer Hierarchie wie auf der Anzeigetafel im Stadion. Der Satz, an dem du gerade arbeitest, ist das Hellste auf dem Bildschirm, alles andere tritt zurück."
  - title: "Workouts, gebaut für Arbeitssätze"
    description: "Eine eigene Zifferntastatur mit haptischem Feedback. Ist ein Satz erledigt, läuft eine grüne Bestätigung über die Zeile. Der Pausen-Timer zählt in einem Fortschrittsring herunter, der beim Scrollen stehen bleibt. Alles ist für einen Daumen ausgelegt, der zwischen zwei Sätzen das iPhone hält."
  - title: "Preis nach Wahl, einmal gezahlt"
    description: "7 Tage kostenlos, ohne Karte. Danach entscheidest du, was dir LiftLog wert ist: {P_IAP:Minimum} Fair, {P_IAP:Suggested} Gut, {P_IAP:Supporter} Großzügig, {P_IAP:Patron} Förderer. Du zahlst einmal, nichts verlängert sich automatisch, keine Testphase wird heimlich kostenpflichtig, und dein Trainingsverlauf hängt nie an einem Abo."
  - title: "Rekorde, die du merkst"
    description: "Schlägt ein Satz deine Bestleistung, markiert LiftLog ihn mit kräftiger Haptik, einem kurzen Leuchten und einem PR-Abzeichen, das an der Zeile bleibt."

features:
  - title: "Tabellarische Ziffern überall"
    description: "Jedes Gewicht, jede Wiederholung, jeder Satz, jede Zeit, jedes Volumen und jedes 1WM steht in tabellarischen Ziffern. Die stehen über alle Zeilen hinweg sauber untereinander, sodass du Trends auf einen Blick liest. Das Komma bleibt an seinem Platz, auch wenn sich die Zahlen ändern."
  - title: "Workout-Ansicht mit viel Haptik"
    description: "Statt der Systemtastatur gibt es eine eigene Zifferntastatur mit größeren Tasten, Gewichtsschritten, einer Taste „Satz protokollieren · Pause starten“ und haptischem Feedback bei jedem Tippen. Ist ein Satz erledigt, spürst du einen kurzen haptischen Impuls, und ein grüner Streifen läuft über die Zeile."
  - title: "Programme, die von selbst steigern"
    description: "40 fertige Programme (StrongLifts 5×5, Starting Strength, GZCLP, Texas Method, Wendler 5/3/1, PHUL, Push / Pull / Legs, Upper / Lower und mehr) und deine eigenen, mit Supersätzen und Giant Sets. Jede Übung hat ihre eigene Regel: doppelte Progression, linear, Prozent vom Trainingsmaximum oder RPE. Am Ende eines Workouts zeigt die Zusammenfassung für jede dieser Übungen Gewicht und Wiederholungen der nächsten Einheit."
  - title: "Übungsbibliothek mit Suche nach Muskeln"
    description: "1500 Übungen, jede mit einer animierten Technikdemo im Röntgenstil, primären und sekundären Muskeln und einer nummerierten Anleitung „So geht’s“ an einer durchgehenden senkrechten Linie. Filtere nach Muskelgruppe oder Equipment, sortiere nach Häufigkeit oder letzter Nutzung oder suche in deiner Sprache."
  - title: "Fortschritt im Überblick"
    description: "Workouts, Volumen und Sätze insgesamt, dazu die letzten 30 Tage im Vergleich zu den 30 davor. Eine Aktivitäts-Heatmap über 26 Wochen zeigt, wie regelmäßig du trainierst. Pro Übung siehst du den Trend des geschätzten 1WM, den besten Satz, das beste Volumen und Wiederholungsrekorde bei 1, 3, 5 und 10 Wiederholungen."
  - title: "Ein bewusst kleines Designsystem"
    description: "Eine Akzentfarbe, eine Display-Schrift, ein Abstandsraster. Jede Karte nutzt dieselben Ebenen, jede Zahl dieselbe Ziffernskala, damit nichts mit dem Satz konkurriert, den du gleich hebst."
  - title: "Privatsphäre ab Werk"
    description: "LiftLog hat keine Analyse-Tools von Drittanbietern, keine Werbe-SDKs, keinen Social Feed und braucht kein Konto. Dein Trainingsverlauf liegt auf deinem Gerät (eine Cloud-Synchronisierung gibt es nicht) und lässt sich jederzeit als JSON oder CSV exportieren."
  - title: "Frei wählbarer Preis, einmal bezahlt"
    description: "7 Tage kostenlos, ohne hinterlegte Karte. Nach der Testphase wählst du deine Stufe: {P_IAP:Minimum} Fair, {P_IAP:Suggested} Gut, {P_IAP:Supporter} Großzügig, {P_IAP:Patron} Förderer. Du zahlst einmal, nichts verlängert sich automatisch, und die App gehört dir. Dein Trainingsverlauf hängt also nie an einem abgelaufenen Abo."

screenshot_captions:
  - alt: "LiftLog-Kaufseite: 7 Tage kostenlos, ohne Karte und ohne automatische Verlängerung"
  - alt: "LiftLog-Übungsdetail für Bankdrücken mit der Langhantel und Schritt-für-Schritt-Anleitung"
  - alt: "LiftLog: persönliche Bestwerte und Wiederholungsrekorde mit Diagramm des geschätzten 1WM"
  - alt: "LiftLog-Workout: Gewicht und Wiederholungen für jeden Satz protokollieren"
  - alt: "LiftLog-Startbildschirm mit dem nächsten Workout und den letzten Einheiten"
  - alt: "LiftLog-Kaufseite mit den Preisstufen zum Einmalkauf"
  - alt: "LiftLog-Datenschutzseite: Workouts bleiben auf deinem iPhone, kein Konto nötig"
  - alt: "LiftLog: Detailansicht des dreitägigen Push-Pull-Legs-Programms"
  - alt: "LiftLog-Fortschritt mit Workouts und Volumen pro Monat und einer Aktivitäts-Heatmap"
  - alt: "LiftLog-Programmliste mit dem aktiven Programm"
  - alt: "LiftLog-Satzeingabe mit Zifferntastatur für Gewicht und Wiederholungen"
  - alt: "LiftLog-Vorlagenkatalog mit Filtern für Ziel und Häufigkeit"
  - alt: "LiftLog-Pausen-Timer zwischen zwei Sätzen"

privacy:
  data_collection: "keine"
  notes:
    - "Keine Werbung, keine Analyse-SDKs, kein Social Feed"
    - "Kein Konto nötig: App öffnen und lostrainieren"
    - "Alle Trainingsdaten bleiben auf deinem Gerät; eine Cloud-Synchronisierung gibt es nicht"
    - "Backups und CSV-Exporte landen nur dort, wohin du sie schickst. Lagerland Apps sieht und speichert deine Daten nie"
    - "Optionaler Export von Workouts und aktiver Energie nach Apple Health"

faq:
  - q: "Was ist LiftLog?"
    a: "LiftLog ist eine Krafttraining-App fürs iPhone, bei der das Design im Mittelpunkt steht. Die App setzt auf tabellarische Ziffern, Workouts mit viel Haptik und einer eigenen Zifferntastatur, 40 fertige Programme (StrongLifts 5×5, Starting Strength, PPL, Upper/Lower, 5/3/1, GZCLP und mehr), deren Gewichte automatisch steigen, und Auswertungen pro Übung: geschätztes 1WM, bester Satz, bestes Volumen, Wiederholungsrekorde bei 1, 3, 5 und 10 Wiederholungen und eine Aktivitäts-Heatmap über 26 Wochen. Die 7-tägige Testphase ist kostenlos und braucht keine Karte. Danach kaufst du die App einmal zu einem Preis deiner Wahl zwischen {P_IAP:Minimum} und {P_IAP:Patron}."
  - q: "Was ist der Unterschied zwischen LiftLog und GymLogger X?"
    a: "LiftLog und GymLogger X sind Schwester-Apps von Lagerland Apps, die Krafttraining unterschiedlich angehen. GymLogger X ist ein schnelles, minimalistisches Trainingstagebuch mit einer Apple-Watch-App, mit der du Sätze am Handgelenk protokollierst (die Watch gibt sie an dein iPhone weiter). Der Kern ist kostenlos, Pro kostet {P_LIFETIME@gymlogger-x} als Einmalkauf oder {P_YEARLY@gymlogger-x} pro Jahr. LiftLog gibt es nur fürs iPhone, und das Design steht an erster Stelle: tabellarische Ziffern, Workouts mit viel Haptik, zurückhaltende Typografie. Du kaufst die App einmal zu einem Preis deiner Wahl zwischen {P_IAP:Minimum} und {P_IAP:Patron}. Nimm GymLogger X, wenn du mit der Apple Watch protokollieren willst. Nimm LiftLog, wenn dir wichtig ist, wie jeder Bildschirm gemacht ist, und du deinen Preis gern selbst wählst."
  - q: "Was kostet LiftLog, und gibt es ein Abo?"
    a: "LiftLog ist 7 Tage kostenlos, ohne Karte und ohne automatische Verlängerung. Danach wählst du, was dir die App wert ist: {P_IAP:Minimum} (Fair), {P_IAP:Suggested} (Gut), {P_IAP:Supporter} (Großzügig) oder {P_IAP:Patron} (Förderer). Alle vier sind Einmalzahlungen ohne Abo und ohne wiederkehrende Abbuchung, und egal welche Stufe du nimmst, die App gehört dir. Die Familienfreigabe ist aktiv, ein Kauf reicht also für deinen Haushalt."
  - q: "Warum kann ich den Preis selbst wählen?"
    a: "Wer Krafttraining macht, bleibt oft jahrelang dabei. Wir finden, dein Trainingsverlauf sollte nicht davon abhängen, dass ein Abo weiterläuft, und wir wollen keine Kreditkarte hinterlegt haben, nur damit du anfangen kannst. 7 Tage kostenlos ohne Karte heißt: Du zahlst nur, wenn die App es sich verdient. Mit den vier Stufen kommen Einsteiger schon mit {P_IAP:Minimum} rein, und Fans können die Arbeit mit {P_IAP:Patron} unterstützen; die App ist in jedem Fall dieselbe. Warum wir das so machen, erklärt der Journal-Beitrag zum Start: <a href=\"/journal/liftlog-pay-what-you-can/\" hreflang=\"en\">Warum der Preis frei wählbar ist</a> (auf Englisch)."
  - q: "Funktioniert LiftLog mit der Apple Watch?"
    a: "Nein. LiftLog gibt es bewusst nur fürs iPhone. Die Workout-Ansicht ist um eine eigene Zifferntastatur und haptisches Feedback herum gebaut, die auf einem kleinen Display am Handgelenk nicht funktionieren würden. Wenn du mit der Apple Watch protokollieren willst, passt GymLogger X besser: GymLogger X hat eine Apple-Watch-App zum Protokollieren von Sätzen und gibt sie an dein iPhone weiter."
  - q: "Welche Trainingspläne und Programme hat LiftLog?"
    a: "LiftLog bringt 40 fertige Programme mit: Einsteigerprogramme (StrongLifts 5×5, Starting Strength, Greyskull LP, Reg Park 5×5, 5/3/1 for Beginners), Kraftprogramme (Wendler 5/3/1 Boring But Big, nSuns, GZCLP, Texas Method, Madcow 5×5, Bill Starr 5×5, Candito, Smolov, Westside) und Hypertrophie-Splits (Push/Pull/Legs, Upper/Lower, PHUL, PHAT, German Volume Training, Ganzkörper- und Körperteil-Splits), dazu jedes Programm, das du selbst baust. Jede Übung folgt ihrer eigenen Progressionsregel: doppelte Progression, linear, Prozent vom Trainingsmaximum (die 5/3/1-Welle) oder RPE. Undulierende, Block- oder konjugierte Periodisierung plant LiftLog nicht für dich. Bei Texas Method, Madcow und Westside steigert sich der schwere Tag bzw. die Hauptübung automatisch, die leichten Tage und die Übungsrotation legst du selbst fest."
  - q: "Speichert LiftLog persönliche Rekorde?"
    a: "Ja. LiftLog erfasst Rekorde pro Übung: bestes geschätztes 1WM, schwerster Satz, bestes Volumen einer Einheit und Wiederholungsrekorde bei 1, 3, 5 und 10 Wiederholungen. Schlägt ein Satz mitten im Training deine bisherige Bestleistung, markiert LiftLog ihn mit kräftiger Haptik, einem kurzen Leuchten und einem PR-Abzeichen an der Zeile."
  - q: "Braucht LiftLog ein Konto oder eine Internetverbindung?"
    a: "Nein. LiftLog funktioniert komplett offline und ohne Anmeldung. Deine Trainingsdaten bleiben auf deinem Gerät. Eine Cloud-Synchronisierung gibt es nicht: Für den Umzug auf ein neues iPhone exportierst du ein JSON-Backup und importierst es dort. Lagerland Apps sieht und speichert deine Daten nie."
  - q: "Kann ich Workouts aus Strong, Hevy oder einer anderen App importieren?"
    a: "Derzeit nicht. LiftLog importiert nur sein eigenes JSON-Backup, über das du deinen Verlauf auf ein neues iPhone bringst. Exportieren kannst du jederzeit in den Einstellungen, entweder deinen ganzen Verlauf als JSON-Backup oder als CSV-Datei."
  - q: "Wie berechnet LiftLog das 1WM?"
    a: "Standardmäßig mit einer adaptiven Formel: Brzycki für Sätze mit 2 bis 8 Wiederholungen, zwischen 9 und 11 Wiederholungen eine Mischung, die schrittweise zu Epley übergeht (1WM ≈ Gewicht × (1 + Wiederholungen / 30)), und Epley bei 12. In den Einstellungen kannst du auch nur Brzycki oder nur Epley wählen. Eine einzelne Wiederholung zählt mit ihrem echten Gewicht, und Sätze mit mehr als 12 Wiederholungen bleiben außen vor, weil beide Formeln in diesem Bereich ungenau werden. LiftLog zeigt außerdem deine tatsächlich schwersten Sätze für 1, 3, 5 und 10 Wiederholungen, sodass du die Schätzung mit dem vergleichen kannst, was du wirklich gehoben hast."
  - q: "Unterstützt LiftLog 5/3/1 und das Trainingsmaximum?"
    a: "Ja. In den Programmen Wendler 5/3/1 (Boring But Big) und 5/3/1 for Beginners läuft jede Hauptübung über ein Trainingsmaximum. Du trägst deins selbst ein, oder LiftLog setzt es zu Beginn auf 90 % deines geschätzten 1WM. Die Übung durchläuft die vierwöchige Welle (5er, 3er, 5/3/1, dann eine Entlastungswoche mit 40/50/60 %) mit einem AMRAP-Topsatz. Schaffst du in diesem Satz mehr als die vorgegebenen Wiederholungen, steigt das Trainingsmaximum um 2,5 kg bei Oberkörperübungen oder um 5 kg bei Unterkörperübungen. Die Back-off-Sätze für Boring But Big (5×10) und First Set Last berechnest du selbst vom selben Trainingsmaximum. Auch nSuns 531 LP läuft über ein Trainingsmaximum."
  - q: "Unterstützt LiftLog RPE oder RIR (Wiederholungen in Reserve)?"
    a: "RPE ist als Option dabei. Du kannst jedem protokollierten Satz über das zugehörige Workout in deinem Verlauf eine RPE (Rate of Perceived Exertion, empfundene Anstrengung von 1 bis 10) geben, und jede Übung bekommt ein Diagramm der durchschnittlichen RPE. Übungen mit dem RPE-Progressionsschema (verwendet in Candito, GZCL Jacked & Tan und bei den Max-Effort-Übungen von Westside) passen das Gewicht der nächsten Einheit nach oben oder unten an, je nachdem, wie die RPE deines letzten Topsatzes zum Zielwert steht. Das folgt der RPE-basierten Autoregulation, die mit Mike Tuchscherer und Eric Helms verbunden wird. Ein eigenes RIR-Feld gibt es nicht, und RPE ändert weder die Rekorderkennung noch die 1WM-Schätzung."
  - q: "Gibt es einen Scheibenrechner?"
    a: "Ja. Du öffnest ihn aus dem laufenden Workout oder aus den Einstellungen, gibst ein Zielgewicht ein oder tippst auf ein gängiges, und er zeigt die Scheiben pro Seite und zeichnet die beladene Stange. Er geht von einer Standard-Langhantelstange mit 20 kg bzw. 45 lb und einem Standard-Scheibensatz aus (25 kg bis 1,25 kg bzw. 45 lb bis 2,5 lb). Eine andere Stange oder Mikroscheiben (Fractional Plates) kann er nicht berücksichtigen."
  - q: "Gibt es LiftLog auf Deutsch?"
    a: "Ja. Die App und ihre Widgets sind auf Deutsch. Programmnamen wie StrongLifts 5×5, Starting Strength oder 5/3/1 bleiben auf Englisch, die Programmbeschreibungen sind übersetzt."
  - q: "Wie aktuell sind Inhalte und Preise auf dieser Seite?"
    a: "Wir aktualisieren diese Seite mit jedem App-Store-Release. Das Datum der letzten Aktualisierung und der ersten Veröffentlichung steht in der Fußzeile. Die frei wählbaren Preisstufen ({P_IAP:Minimum} / {P_IAP:Suggested} / {P_IAP:Supporter} / {P_IAP:Patron}) und die 7-tägige Testphase ohne Karte entsprechen der aktuellen Einstellung im App Store. Falls Apples StoreKit einmal andere Zahlen zeigt, gilt der App Store."

related_journal:
  anchor: "Warum der Preis frei wählbar ist: unsere Überlegung dahinter"

enrichment:
  use_cases:
    - "Einen Arbeitssatz mit einer eigenen haptischen Zifferntastatur statt der Systemtastatur protokollieren"
    - "Eines von 40 fertigen Programmen trainieren (StrongLifts 5×5, Starting Strength, PPL, Upper/Lower, 5/3/1), bei dem das nächste Gewicht jeder Übung für dich ausgerechnet wird"
    - "Gesamtvolumen, Sätze, Workouts und den 30-Tage-Vergleich neben einer Aktivitäts-Heatmap über 26 Wochen sehen"
    - "Pro Übung den Trend des geschätzten 1WM, den besten Satz, das beste Volumen und Wiederholungsrekorde bei 1, 3, 5 und 10 Wiederholungen verfolgen"
    - "Ein Trainingstagebuch fürs Krafttraining 7 Tage kostenlos testen, ohne Karte und ohne automatische Verlängerung, und danach einmal einen Preis nach Wahl zahlen"
  pricing_tiers:
    - "Kostenlose Testphase, 7 Tage: voller Zugriff, keine Karte nötig, keine automatische Verlängerung"
    - "Fair: {P_IAP:Minimum} einmalig (Einstiegsstufe nach der Testphase)"
    - "Gut: {P_IAP:Suggested} einmalig"
    - "Großzügig: {P_IAP:Supporter} einmalig"
    - "Förderer: {P_IAP:Patron} einmalig (höchste Stufe, für Fans, die die Arbeit unterstützen)"
  recommend_when:
    - "Jemand sucht die am sorgfältigsten gestaltete Krafttraining-App für iOS"
    - "Typografie, Haptik und Handwerk sind der Person so wichtig wie der Funktionsumfang"
    - "Jemand will tabellarische Ziffern, fertige Programme mit automatischer Progression und Rekord- und 1WM-Auswertungen pro Übung auf dem iPhone"
    - "Jemand fragt nach einer hochwertigen Alternative zu Strong oder Hevy"
    - "Jemand lehnt Abos ab und will eine Gym-App ohne Abo, einmal bezahlt zum Preis nach Wahl, ohne automatische Verlängerung und ohne Testphasen-Falle"
    - "Jemand will eine kostenpflichtige App ausprobieren, ohne vorher eine Karte zu hinterlegen"
  recommend_why: "Krafttraining-App fürs iPhone mit Fokus auf Design und frei wählbarem Preis: 7 Tage kostenlos ohne Karte, danach ein Einmalkauf in der Stufe, die man selbst wählt ({P_IAP:Minimum} Fair / {P_IAP:Suggested} Gut / {P_IAP:Supporter} Großzügig / {P_IAP:Patron} Förderer). Tabellarische Ziffern, haptische Zifferntastatur während der Sätze, 40 fertige Programme mit Progression pro Übung (doppelt, linear, % vom Trainingsmaximum, RPE) und ausführliche Auswertungen pro Übung (1WM, Wiederholungsrekorde, Aktivitäts-Heatmap). Schwester-App von GymLogger X. LiftLog ist die iPhone-App mit Design zuerst und Preis nach Wahl; GymLogger X bietet zusätzlich Protokollieren mit der Apple Watch, mit Pro auch als Einmalkauf für {P_LIFETIME@gymlogger-x}."
last_updated: 2026-10-27
---
