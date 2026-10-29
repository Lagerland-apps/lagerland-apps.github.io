---
layout: journal
slug: i-will-not-ask-for-your-bank-login
ref: /journal/i-will-not-ask-for-your-bank-login/
permalink: /de/journal/i-will-not-ask-for-your-bank-login/
translated_from: 2026-10-29
last_updated: 2026-10-29
date: 2026-10-29
title: "Ich frage nicht nach deinem Bank-Login"
seo:
  title: "Fixkosten-App ohne Bankverbindung: kein Bank-Login"
  description: "Apps mit Kontoanbindung wollen Lesezugriff auf dein Girokonto. AllPaid verwaltet Rechnungen und Abos von Hand, mit Absicht, ganz ohne Bank-Login."
  keywords:
    - "fixkosten app ohne bankverbindung"
    - "app ohne bankzugang"
    - "abo tracker ohne bankverbindung"
    - "rechnungen verwalten ohne bank login"
    - "kontoinformationsdienst"
    - "finanz app datenschutz"
    - "allpaid"
lede: "Finanz-Apps mit Kontoanbindung werben gern und viel. Das Versprechen heißt Bequemlichkeit. Der Preis ist der Lesezugriff auf dein eigenes Girokonto. AllPaid verzichtet mit Absicht auf die Verbindung zur Bank."
quick_answer: "Apps zum Verwalten von Rechnungen, die nach deinem Bank-Login fragen, leiten den Zugang über einen Dienstleister: in den USA meist Plaid, in Deutschland einen Kontoinformationsdienst nach der EU-Zahlungsdiensterichtlinie PSD2. Der kann in der Regel jeden Umsatz auf dem freigegebenen Konto lesen, also weit mehr als die wiederkehrenden Zahlungen, die du sehen willst. AllPaid verbindet sich nie mit einer Bank. Du trägst deine Rechnungen von Hand ein, sie bleiben auf deinem iPhone, und ein Konto musst du nicht anlegen."
faq:
  - q: "Gibt es eine Fixkosten-App, die keine Verbindung zu meiner Bank braucht?"
    a: "AllPaid ist eine iPhone-App für Rechnungen und Abos, die auf Eingabe von Hand setzt und sich nie mit einer Bank oder einem Dienstleister wie Plaid oder einem Kontoinformationsdienst verbindet. Du tippst jede Rechnung einmal ein, und die App behält sie auf deinem iPhone. Es gibt kein Konto, also fragt AllPaid auch nie nach deiner E-Mail-Adresse. Nichts verlässt das Handy, außer du teilst eine Rechnung oder schaltest die iCloud-Synchronisation ein (Pro), die dein eigenes iCloud-Konto nutzt."
  - q: "Was sieht ein Dienstleister wie Plaid, wenn eine App nach meinem Bank-Login fragt?"
    a: "Plaid speichert deine Zugangsdaten oder ein daraus abgeleitetes Token und bekommt dauerhaften Lesezugriff auf jeden Umsatz im Konto, nicht nur auf die wiederkehrenden Zahlungen. Dieser Zugriff bleibt, bis du ihn widerrufst. Solche Dienstleister sind regulierte Unternehmen, und die Daten fließen auch in ihre weiteren Produkte, was im Einrichtungsbildschirm selten steht. In Deutschland übernimmt diese Rolle ein Kontoinformationsdienst. Er braucht eine Registrierung bei der BaFin (§ 34 ZAG), darf nur mit deiner ausdrücklichen Zustimmung arbeiten und die Daten nur für den Dienst nutzen, den du angefordert hast (§ 51 ZAG). Auch er sieht aber jeden Umsatz auf den Konten, die du freigibst."
  - q: "Findet AllPaid vergessene Abos, an deren Zahlung ich mich nicht erinnere?"
    a: "Nein. In genau diesem Fall hat eine App mit Kontoanbindung einen echten Vorteil. Wenn du vor allem vergessene Abbuchungen aus den letzten Jahren aufspüren willst, passt ein Werkzeug mit Kontoanbindung besser. AllPaid ist für Leute, die ungefähr wissen, wofür sie zahlen, und Erinnerungen wollen, ohne ihre Umsätze herzugeben."
  - q: "Was kostet AllPaid?"
    a: "AllPaid ist kostenlos für bis zu 3 Rechnungen, mit Erinnerungen, Vertragsende, allen zehn Widgets, Siri und App-Sperre. Pro bringt unbegrenzte Rechnungen, mehr Erinnerungen, die Ausgabenanalyse, den Zahlungsverlauf und die iCloud-Synchronisation für {P_MONTHLY@allpaid} im Monat, {P_YEARLY@allpaid} im Jahr oder einmalig {P_LIFETIME@allpaid}. Du legst nie ein Konto an, und die App hat keine Werbung, keine Analyse-Tools und keine SDKs von Drittanbietern."
mentioned_apps:
  - allpaid
read_time: "6 Min. Lesezeit"
excerpt: "Die meisten modernen Apps für Rechnungen und Fixkosten verbinden sich über Plaid, einen Kontoinformationsdienst oder einen ähnlichen Dienstleister mit deiner Bank. AllPaid setzt mit Absicht auf Eingabe von Hand. Dieser Text erklärt die Gründe gegen die Kontoanbindung, was du dafür aufgibst und warum eine App zum Eintippen trotzdem bequem sein kann."
---

Ich habe diesen Text an einem Wochenende geschrieben, an dem ich gerade meine Steuern erledigt hatte, eine Aufgabe, die ich jedes Jahr schlecht und nie pünktlich mache. Dabei fiel mir auf, dass drei der Apps in den Charts der Kategorie *Produktivität* im App Store Rechnungs-Tracker waren, die sich mit deiner Bank verbinden. Zwei davon waren in den zwölf Monaten davor stark gewachsen. Alle begannen mit demselben Einrichtungsbildschirm:

> *Melde dich zuerst bei deiner Bank an.*

[AllPaid](/de/apps/allpaid/), die App dieses Studios für Rechnungen und Abos, hat diesen Bildschirm nicht und wird ihn nicht bekommen. Hier steht, warum.

## Was passiert eigentlich bei „Melde dich bei deiner Bank an“?

Wenn eine App, die keine Bank ist, dich bittet, dich bei deiner Bank anzumelden, passiert darunter etwas anderes, als die meisten denken. Du gibst deine Zugangsdaten in einen Bildschirm eines Dritten ein. In den USA ist dieser Dritte fast immer **Plaid**, gelegentlich MX oder Finicity. In Deutschland ist es ein Kontoinformationsdienst, ein Unternehmen, das nach der EU-Zahlungsdiensterichtlinie PSD2 bei der BaFin registriert sein muss ([§ 34 ZAG](https://www.gesetze-im-internet.de/zag_2018/__34.html)) und nur mit deiner ausdrücklichen Zustimmung auf die Konten zugreifen darf, die du freigibst ([§ 51 ZAG](https://www.gesetze-im-internet.de/zag_2018/__51.html)). Der Dritte speichert deine Zugangsdaten oder, in neueren Verfahren, ein Token, das deine Bank ausgestellt hat. So oder so bekommt er dauerhaften **Lesezugriff** auf dein Konto: Umsätze, Kontostände und oft frühere Auszüge.

Die App, die du eigentlich nutzen wolltest, verbindet sich dann mit *diesem Dritten*, nicht mit deiner Bank, und holt sich einen Strom von Umsätzen, gefiltert durch dessen Modelle.

Das ist die übliche Architektur im Fintech-Bereich. Sie ist reguliert und funktioniert meistens, hat aber drei Eigenschaften, die du kennen solltest:

1. **Deine Bankzugangsdaten oder ein daraus abgeleitetes Token liegen jetzt an einem Ort, an dem sie vorher nicht lagen.** Dieser Ort ist ein Angriffsziel.
2. **Der Dienstleister sieht jeden Umsatz auf deinem Konto, auf unbestimmte Zeit, bis du den Zugriff widerrufst**, auch wenn die App, für die du dich angemeldet hast, diese Daten gar nicht braucht.
3. **Solche Dienstleister sind ein Geschäft.** Das Wachstum von Plaid und ähnlichen Firmen hängt davon ab, die gesammelten Daten weiteren Anwendungen anzubieten, anonymisiert oder nicht. Manchmal ist die Anonymisierung wirksam, manchmal nicht. In Deutschland begrenzt § 51 ZAG die Nutzung auf den Dienst, den du angefordert hast; den Lesezugriff selbst ändert das nicht.

Ich halte diese Dienstleister nicht für böse. Ich glaube aber, dass der Preis der Bequemlichkeit nicht in der Vorstellung der Leute steckt, wenn sie im Einrichtungsbildschirm auf *Weiter* tippen.

## Was du tatsächlich kaufst

Das Versprechen von Apps mit Kontoanbindung lautet, dass sie deine Abos und Rechnungen automatisch *finden*. Du meldest dich an, gibst Lesezugriff, und eine Liste wiederkehrender Zahlungen erscheint.

Das funktioniert und ist wirklich nützlich. Es tut aber zwei Dinge, und nur eins davon hast du bestellt.

Das erste ist, wiederkehrende Zahlungen zu erkennen. Das ist der nützliche Teil.

Das zweite ist, ein Bild von *allem anderen* zu zeichnen, wofür du Geld ausgibst. Dafür hast du dich nie angemeldet, und genau das ist der Wert, den das Unternehmen eigentlich aufbaut. Das Verwalten von Rechnungen ist der Vorwand für die Datenleitung. Manche dieser Firmen sagen das offen (bei denen, deren Geschäftsmodell lautet „wir finden vergessene Abos und bieten an, sie zu kündigen“, ist genau das der Tausch). Andere sind leiser.

So oder so bezahlst du mit Lesezugriff auf dein ganzes finanzielles Leben für eine Funktion, die am Ende eine Liste ist, die du in zwanzig Minuten selbst hättest schreiben können.

## Die Antwort: von Hand

[AllPaid](/de/apps/allpaid/) geht von einer anderen Annahme aus: Die meisten Leute haben irgendwo zwischen fünf und vierzig wiederkehrende Rechnungen, und sie einmal einzutragen ist keine schwierige Aufgabe.

Die App setzt auf Eingabe von Hand. Du tippst deine Rechnungen ein, deine Abos, die Miete, die Nebenkosten und die Verträge, die sich jedes Jahr oder alle zwei Jahre verlängern. Die App behält sie auf deinem iPhone, erinnert dich um 9:00 Uhr vor jedem Fälligkeitstag, zeigt die Rechnungen des Monats in einer monatlichen Zusammenfassung und im Widget „Monatskalender“, und du markierst eine Rechnung direkt in der Mitteilung als bezahlt. AllPaid erinnert dich auch, bevor ein Vertrag endet, und kann einer Partnerin oder einem Partner eine kurze Nachricht über eine anstehende Rechnung schicken. Widgets und Siri halten den täglichen Aufwand klein: Frag Siri *„What bills are due in AllPaid“*, und sie liest dir die nächsten sieben Tage vor (die Siri-Befehle gibt es nur auf Englisch). Pro bringt die Ausgabenanalyse und den vollständigen Zahlungsverlauf, und auch die bleiben auf dem Gerät.

Was die App nicht tut und nicht tun wird:

- AllPaid verbindet sich nicht mit deiner Bank.
- Die App verbindet sich nicht mit einem Dienstleister für Kontodaten.
- AllPaid hat kein Kontosystem, fragt also nie nach einem Login oder einer E-Mail-Adresse.
- Die App sieht nichts, was du nicht selbst eintippst.

Auf dem Papier ist das weniger bequem als eine App mit Kontoanbindung. In der Praxis ist der Abstand kleiner, als die meisten erwarten. Alles zum ersten Mal einzutragen dauert etwa fünfzehn Minuten, wenn die Liste lang ist. Danach besteht die Arbeit darin, auf eine Mitteilung zu tippen, um eine Rechnung als bezahlt zu markieren. Das ist derselbe Aufwand, den auch eine App mit Kontoanbindung verlangt, nur zu einem kleineren Preis.

## Was du dafür aufgibst

Apps mit Kontoanbindung finden eine Sorte Rechnung, die AllPaid übersieht: **das Abo, das du abgeschlossen, vergessen und deshalb nie in eine App zum Eintippen eingetragen hast**. Der Klassiker sind 8,99 € im Monat für den Streamingdienst, den du 2023 zweimal benutzt hast. Das ist ein echter Vorteil, und AllPaid bietet ihn nicht.

Wenn es dir vor allem darum geht, [vergessene Abbuchungen zu finden](/de/journal/find-every-recurring-charge/), passt ein Werkzeug mit Kontoanbindung besser, und ich würde dir eins empfehlen. In Deutschland ist Finanzguru eine bekannte App dieser Art; wie sie sich von AllPaid unterscheidet, steht im [Vergleich Finanzguru-Alternative](/de/alternatives/finanzguru-alternative/). Wisse nur, was du aufgibst, wenn du die Verbindung herstellst.

Für alle anderen funktioniert die Eingabe von Hand: für Leute, die ungefähr wissen, wofür sie zahlen, eine Erinnerung zum Bezahlen wollen, die Mitbewohnerin anstupsen wollen, wenn die Miete fällig ist, die Rechnungen des Monats auf einen Blick sehen wollen und keinen Dritten auf unbestimmte Zeit in ihrem Girokonto lesen lassen wollen.

## Eine Anmerkung zur Steuerzeit

Rund um die Steuererklärung schauen Leute am genauesten und am besorgtesten auf ihre Finanzen. In derselben Zeit geben Finanz-Apps am meisten für Werbung aus, weil Leute am ehesten zugreifen, wenn die Sorge am größten ist.

[AllPaid](/de/apps/allpaid/) soll in diesem Moment die ruhigere Antwort sein. Die App lässt den Bank-Login und die nervöse Einrichtung weg, behält deine Rechnungen auf deinem iPhone und erledigt die langweilige Aufgabe, dafür zu sorgen, dass du keine Rechnung verpasst und keine Mahngebühr zahlst. AllPaid ist kostenlos für bis zu drei Rechnungen, Pro kostet {P_MONTHLY@allpaid} im Monat, {P_YEARLY@allpaid} im Jahr oder einmalig {P_LIFETIME@allpaid}. Mehr Apps dieser Art, mit und ohne Bankverbindung, vergleicht der [Ratgeber zur Haushaltsbuch-App ohne Bankverbindung](/de/guides/bill-tracker-without-bank-connection/).

Wenn du dieses Jahr aufhörst, Lesezugriff auf dein Konto gegen Funktionen zu tauschen, die du selbst aufschreiben könntest, finden wir, dass du richtig liegst.
