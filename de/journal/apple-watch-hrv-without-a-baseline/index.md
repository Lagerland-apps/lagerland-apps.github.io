---
layout: journal
slug: apple-watch-hrv-without-a-baseline
ref: /journal/apple-watch-hrv-without-a-baseline/
permalink: /de/journal/apple-watch-hrv-without-a-baseline/
translated_from: 2026-10-29
last_updated: 2026-10-29
date: 2026-10-29
title: "HRV der Apple Watch: Warum der Wert ohne Basislinie fast nichts sagt"
seo:
  title: "HRV Apple Watch: Warum die Werte allein wenig sagen"
  description: "HRV-Werte der Apple Watch: 42 ms können sehr gut oder alarmierend sein, und nur deine Basislinie sagt dir, was davon. So liest du deine HRV richtig."
  keywords:
    - "hrv apple watch werte"
    - "hrv apple watch gute werte"
    - "hrv apple watch normal"
    - "hrv baseline apple watch"
    - "herzfrequenzvariabilität apple watch"
    - "hrv richtig lesen"
    - "hrv tabelle"
lede: "Ein HRV-Wert von 42 ms auf der Apple Watch kann sehr gut, durchschnittlich oder alarmierend sein, und ohne Kontext weißt du nicht, was davon zutrifft. Für sich allein gehört die Zahl zu den am häufigsten falsch gelesenen Werten, die Gesundheitsgeräte für Verbraucher liefern. Dieser Beitrag zeigt, was die HRV dir sagt, was nicht und warum erst eine persönliche Basislinie den Wert brauchbar macht."
quick_answer: "Die rohe HRV (Herzfrequenzvariabilität, auf der Apple Watch als SDNN angegeben) bedeutet nur etwas im Vergleich mit deiner eigenen gleitenden Basislinie. Die absolute HRV unterscheidet sich zwischen Menschen um das 3- bis 10-Fache, je nach Alter, Geschlecht, Fitness, Körperhaltung, Messzeitpunkt und dem Handgelenk, an dem die Uhr sitzt. Lies die HRV deiner Apple Watch als prozentuale Abweichung von deinem eigenen Mittelwert der letzten Wochen; 60 Tage sind ein gutes Fenster. Vergleichst du deinen Wert mit dem eines Freundes, einem Bevölkerungsdurchschnitt oder einer Tabelle mit „Normalwerten“ aus dem Internet, führt dich das fast immer in die Irre."
excerpt: "Ein HRV-Wert von 42 ms ist für den einen Menschen ausgezeichnet und für den anderen alarmierend. Dieser Beitrag erklärt, warum sich absolute HRV-Werte zwischen Menschen um das 3- bis 10-Fache unterscheiden, warum erst deine persönliche Basislinie die HRV der Apple Watch brauchbar macht und wie du Trends so liest, wie es die Sportwissenschaft tut."
faq:
  - q: "Ist eine HRV von 42 ms gut oder schlecht?"
    a: "Das hängt ganz davon ab, wessen 42 ms es sind. Liegt deine Basislinie über 60 Tage bei 38 ms, sind 42 ms überdurchschnittlich und ein gutes Zeichen für deine Erholung. Liegt sie bei 80 ms, sind 42 ms die Hälfte deines Normalwerts und deuten wahrscheinlich auf deutlichen Stress, eine Krankheit oder angesammelte Trainingsbelastung hin. Derselbe absolute Wert ist im einen Körper eine gute Nachricht und im anderen eine schlechte. Deshalb vergleicht dich jede HRV-App, die etwas taugt, mit dir selbst."
  - q: "Warum unterscheidet sich die HRV der Apple Watch so stark von der eines Brustgurts?"
    a: "Die Apple Watch misst die HRV (SDNN) zu wechselnden Zeiten am Tag und nachts, wenn du dich nicht bewegst, und zwar optisch per Photoplethysmografie. Ein Brustgurt misst fortlaufend die elektrische Aktivität des Herzens. Das sind verschiedene Messungen unter verschiedenen Bedingungen, die absoluten Werte lassen sich also nicht aufeinander übertragen. Die Messungen, die deine Uhr über die Zeit an dir macht, lassen sich dagegen gut vergleichen. Dein Trend ist verlässlich; dein absoluter Wert, gelesen an einer Tabelle für Brustgurte, ist es nicht."
  - q: "Wie stark schwankt die HRV bei einem Menschen von Tag zu Tag?"
    a: "Stark. Schwankungen von 10 bis 25 % von einem Tag zum nächsten sind bei gesunden Erwachsenen normal, ein einzelner niedriger Wert bedeutet also fast nie etwas. Schau auf den gleitenden 7-Tage-Durchschnitt im Vergleich mit deiner Basislinie über 60 Tage. Die HRV eines einzelnen Tages ist größtenteils Rauschen."
  - q: "Warum sinkt die HRV im Winter?"
    a: "Herz und Kreislauf passen sich an die Jahreszeit an. Kälte, weniger Tageslicht, weniger Ausdauerbewegung und veränderter Schlaf verschieben das Gleichgewicht des autonomen Nervensystems in Richtung Sympathikus. Ein Rückgang um 10 bis 20 % im Winter ist häufig und nicht krankhaft. Einer der häufigsten Deutungsfehler ist, ihn als „Mit mir stimmt etwas nicht“ zu lesen, wenn er eigentlich bedeutet: „Meine HRV liegt im Winter niedriger.“"
  - q: "Zeigt die Apple Watch RMSSD, SDNN oder lnRMSSD an?"
    a: "SDNN. Apple Health speichert die HRV der Apple Watch als SDNN, die Standardabweichung der Abstände zwischen aufeinanderfolgenden Herzschlägen, in Millisekunden, und das ist der einzige HRV-Wert, den HealthKit bereitstellt. In der Sportwissenschaft werden oft RMSSD und sein natürlicher Logarithmus lnRMSSD genutzt. Das sind andere Berechnungen als SDNN, ein Wert der Apple Watch lässt sich also nicht einfach in einen davon umrechnen. Observa zeigt die SDNN, die Apple Health aufzeichnet, und vergleicht sie mit deiner eigenen Basislinie."
mentioned_apps:
  - observa
read_time: "7 Min. Lesezeit"
---

Die Apple Watch misst eine der aufschlussreichsten Zahlen, die ein Gesundheitsgerät für Verbraucher liefert, und kaum jemand nutzt sie richtig.

Öffne die App „Health“ und tippe auf Herzfrequenzvariabilität. Du siehst eine Reihe von Werten aus den letzten Wochen, vermutlich ein paar um 25, ein paar um 45, ein paar um 80, dazu ein Diagramm mit Spannweiten, das irgendwie aufschlussreich aussieht. Wenn du in der falschen Ecke des Internets gelandet bist, hast du vielleicht gelesen, die HRV „sollte“ über 50 ms liegen oder alles unter 30 sei „bedenklich“. Das hilft dir ungefähr so viel wie die Regel, deine „normale“ Körpertemperatur müsse 37 °C betragen, egal wer du bist. Die Zahl stimmt. Der Rahmen ist falsch.

## Was die HRV eigentlich misst

Die HRV, die Herzfrequenzvariabilität, ist die Schwankung der Zeit zwischen aufeinanderfolgenden Herzschlägen. Die Apple Watch gibt sie als SDNN an, also als Standardabweichung der Abstände zwischen aufeinanderfolgenden normalen Herzschlägen (der NN- oder RR-Intervalle), in Millisekunden. Höhere Werte bedeuten meist mehr Aktivität des parasympathischen Nervensystems („Ruhe und Verdauung“), niedrigere meist mehr sympathische Aktivität („Kampf oder Flucht“). Ein dauerhaft höherer Verlauf hängt mit kardiovaskulärer Fitness, guter Erholung und parasympathischer Dominanz zusammen.

So weit, so gut. Schwierig wird es, wenn dieselben Worte für zwei Menschen gelten, deren absolute Werte sich um den Faktor drei unterscheiden.

## Die Unterschiede zwischen Menschen sind riesig

Die absolute HRV gesunder Erwachsener reicht als SDNN ungefähr von 15 ms bis 150 ms, eine zehnfache Spanne. Diese Faktoren verschieben die persönliche Basislinie:

- **Alter.** Die meisten Langzeitstudien finden, dass die HRV ab 30 um etwa 0,5 bis 1 ms pro Jahr sinkt. Jemand mit 45 Jahren und 35 ms und jemand mit 25 Jahren und 70 ms können beide für ihr Alter eine völlig gesunde parasympathische Aktivität haben.
- **Geschlecht.** Im Schnitt ist die HRV bei erwachsenen Frauen etwas niedriger als bei Männern, allerdings ist die Streuung innerhalb jedes Geschlechts viel größer als der Unterschied zwischen ihnen.
- **Fitness.** Ausdauertrainierte Menschen haben in Ruhe oft eine um 50 bis 100 % höhere HRV als Untrainierte. Auch das lässt sich nicht einfach hochrechnen: Gut trainierte Sportlerinnen und Sportler liegen oft in Bereichen, die eine allgemeine Tabelle „erhöht“ nennen würde.
- **Körperhaltung.** Im Liegen ist die HRV höher als im Sitzen und im Sitzen höher als im Stehen.
- **Tageszeit.** Nachts höher, in aktiven Stunden niedriger.
- **Messmethode.** Die optische PPG-Messung der Apple Watch zu wechselnden Zeiten liefert andere Werte als ein Brustgurt oder ein EKG in Forschungsqualität, selbst bei derselben Person im selben Moment.

Die HRV gehört zu den Körperwerten, bei denen nur *deiner* etwas bedeutet. Deine 42 ms mit den 65 ms eines Freundes zu vergleichen, sagt dir nichts.

## Der richtige Rahmen: deine eigene Basislinie über 60 Tage

Verlässlich deuten kannst du nur HRV-Aussagen, die so aussehen:

- **„Meine HRV (SDNN) liegt heute X % über oder unter meinem eigenen gleitenden 7-Tage-Durchschnitt.“**
- **„Der Mittelwert dieser Woche liegt X % über oder unter meinem eigenen gleitenden 60-Tage-Durchschnitt.“**

Beide vergleichen dich mit dir selbst, und das hebt fast alle Störfaktoren von oben auf. Dein Alter und dein Geschlecht ändern sich in 60 Tagen nicht, deine Fitness ändert sich nicht dramatisch, und deine Uhr ist dieselbe Uhr. Was sich ändert, ist *das, was deine Physiologie diese Woche im Vergleich zum letzten Quartal bewegt hat*, und genau danach lohnt es sich zu fragen.

Sechzig Tage taugen aus drei Gründen als Fenster für die Basislinie. Das sind ungefähr zwei Menstruationszyklen, zyklische Schwankungen mitteln sich also heraus. Das Fenster deckt zwei typische Mesozyklen im Training ab, kurzfristige Anpassungen geben also nicht den Ton an. Und es liefert genug Wochenwerte ohne Überschneidung, damit eine Standardabweichung etwas aussagt; mit weniger Werten ist schon die Standardabweichung selbst verrauscht.

## Was ein einzelner niedriger Wert bedeutet und was nicht

Liegt deine HRV an einem Morgen 30 % unter deinem 7-Tage-Durchschnitt, heißt das: *Es ist etwas passiert.* Spätes Essen, Alkohol, schlechter Schlaf, ein stressiger Abend, eine beginnende Krankheit, hartes Training am Vortag oder ganz normales biologisches Rauschen von Tag zu Tag. Für sich allein sagt dir der Wert weder, dass du ruhen, noch, dass du hart trainieren, in Panik geraten oder dich freuen sollst.

Aussagekräftig ist erst ein *Muster*. Drei Tage in Folge mehr als eine Standardabweichung unter der Basislinie sind ein Signal. Ein einzelner Rückgang um 25 % nach einem bekannten Stressor sagt dir etwas über diesen Stressor, nicht über deine Gesundheit. Ein Rückgang um 25 % ohne erkennbaren Grund, der nach 72 Stunden nicht verschwunden ist, gehört abgeklärt, und zwar von einer Ärztin oder einem Arzt, nicht von einer App für Verbraucher.

Für Selbstexperimente halte ich diese Schwelle für ungefähr richtig: **mindestens 10 Beobachtungen unter gleichen Bedingungen in einem Fenster von 60 Tagen und mindestens eine Standardabweichung Abstand zwischen den Bedingungen**, bevor du ein Ergebnis für mehr als Rauschen hältst. Eine „Erkenntnis“ mit dünnerer Grundlage ist meist geraten.

## Warum die HRV im Winter sinkt (und anderes saisonales Rauschen)

Wenn du deine Apple Watch durch einen Winter auf der Nordhalbkugel trägst, rechne damit, dass deine HRV-Basislinie von Oktober bis Februar um 10 bis 20 % sinkt. Die üblichen Ursachen sind Kälte, weniger Tageslicht, weniger Ausdauerbewegung, mehr Zeit drinnen und veränderter Schlaf. Keine davon ist krankhaft, und alle drücken den Wert.

Einen Rückgang im Winter als „Mit mir stimmt etwas nicht“ zu lesen, ist einer der häufigsten Deutungsfehler. Richtig gelesen heißt er: „Meine HRV liegt im Winter niedriger, und das ist die neue Basislinie, an der ich Abweichungen messe.“ Die Basislinie soll wandern, denn deine Physiologie wandert mit der Welt.

## Was das in der Praxis bedeutet

Daraus folgen ein paar praktische Regeln:

1. **Vergleiche deinen Wert nie mit dem eines anderen.** Nicht mit dem eines Freundes, nicht mit dem eines Fremden auf Reddit, nicht mit einer Infografik zum „Normalbereich“. Vergleiche dich mit dir selbst.

2. **Verfolge Trends.** Der Wert eines einzelnen Tages ist größtenteils Rauschen. Der gleitende 7-Tage-Durchschnitt ist das Signal, und die Basislinie über 60 Tage ist der Rahmen, in dem du das Signal deuten kannst.

3. **Lies die HRV als Abweichung von deiner eigenen Basislinie.** Die HRV ist ungefähr log-normalverteilt, derselbe Abstand in Millisekunden bedeutet bei einer niedrigen Basislinie also mehr als bei einer hohen. Deutbar wird die heutige SDNN erst, wenn du sie als prozentuale Abweichung von deinem persönlichen gleitenden Mittelwert ausdrückst.

4. **Finde deine Stressoren.** Sinkt deine HRV regelmäßig nach späten Trainings, Alkohol oder langer Bildschirmzeit, kannst du daran etwas ändern. Sorgen machen sollte dir eher ein Rückgang, dessen Ursache du nicht kennst.

5. **Rechne mit saisonaler Drift.** Im Winter niedriger, im Sommer höher: Das ist normal. Eine Pandemie, eine Krankheit, Stress im Leben oder ein Baby verschieben die Basislinie ebenfalls. Behandle sie als beweglichen Bezugsrahmen.

[Observa](/de/apps/observa/) nimmt dir einen großen Teil davon ab. Die App zeigt deine HRV (SDNN) im Vergleich mit deinem eigenen üblichen Bereich, mit 7 Tagen Verlauf kostenlos und 30, 90 oder 365 Tagen mit Pro. Die HRV macht außerdem 25 % des täglichen Bereitschaftswerts aus, und „Warum dieser Wert?“ sagt dir in einfachen Worten, wenn deine HRV außerhalb deines üblichen Bereichs lag und den Wert bewegt hat. Die Auswertung läuft auf deinem Gerät, und Observa vergleicht *dich, heute, mit deinem eigenen Normalwert*. Bei der HRV ist das der einzige Vergleich, der sich lohnt.

## Kurz gesagt

- **Die absolute HRV unterscheidet sich zwischen gesunden Erwachsenen um das 3- bis 10-Fache.** Deinen Wert mit dem eines anderen zu vergleichen, ist sinnlos.
- **Nur deine eigene Basislinie, über Wochen aufgebaut, macht die HRV brauchbar.** Schwankungen von 10 bis 25 % von Tag zu Tag sind normal.
- **Trends zählen, einzelne Werte nicht.** Drei Tage in Folge mehr als eine Standardabweichung unter der Basislinie sind ein Signal. Ein Tag ist Rauschen.
- **Im Winter liegt die HRV niedriger als im Sommer.** Saisonale Drift ist normal, und sie für eine Krankheit zu halten, ist der häufige Fehler.
- **Lies die SDNN als Abweichung von deiner eigenen Basislinie.** Die HRV ist ungefähr log-normalverteilt; vergleiche jeden Tag prozentual mit deinem persönlichen Mittelwert statt mit festen Grenzen in Millisekunden.

Die Zahl stand schon immer in deiner App „Health“. Gefehlt hat eine Basislinie, an der du sie messen kannst. Warum wir Observa deshalb ums Deuten statt ums Messen gebaut haben, steht in [Apple-Health-Daten verstehen](/de/journal/your-apple-health-data-doesnt-mean-what-you-think/).
