---
layout: journal
slug: what-an-iphone-app-can-actually-block
ref: /journal/what-an-iphone-app-can-actually-block/
permalink: /de/journal/what-an-iphone-app-can-actually-block/
translated_from: 2026-10-29
last_updated: 2026-10-29
date: 2026-10-29
title: "Apps sperren auf dem iPhone: was eine App wirklich blockieren kann und was grundsätzlich nicht"
seo:
  title: "Apps sperren auf dem iPhone: was App-Blocker können"
  description: "Wie App-Blocker auf dem iPhone funktionieren: die drei Apple-Frameworks, warum die App-Auswahl nur Tokens liefert und warum sich jede Sperre umgehen lässt."
  keywords:
    - "apps sperren iphone"
    - "app blocker iphone"
    - "einzelne apps sperren iphone"
    - "bildschirmzeit oder app blocker"
    - "app blocker umgehen"
    - "instagram sperren iphone"
    - "family controls api"
    - "screen time api"
lede: "Keine iPhone-App eines Drittanbieters sperrt selbst etwas. Sie bittet iOS darum, über drei Apple-Frameworks mit klaren, veröffentlichten Grenzen. Diese Grenzen erklären, warum dein Blocker die gesperrten Apps nicht beim Namen kennt, warum Mitteilungen trotzdem ankommen und warum die ehrliche Antwort auf „Lässt sich das umgehen?“ immer Ja lautet."
quick_answer: "Auf dem iPhone sperrt keine App eines Drittanbieters selbst etwas. Sie bittet iOS darum, über drei Apple-Frameworks: FamilyControls (Erlaubnis und die App-Auswahl des Systems), ManagedSettings (legt die Sperre über die gewählten Apps) und DeviceActivity (Zeitpläne und Nutzungsgrenzen). Die Auswahl liefert nur undurchsichtige Tokens, der Blocker erfährt also nie, welche Apps du gewählt hast. Er kann Apps, ganze Kategorien und Websites in Safari sperren. Er kann keine Mitteilungen stummschalten, nicht auf deine anderen Geräte zugreifen und nicht weiterwirken, wenn du ihm in den Einstellungen die Erlaubnis entziehst. Jeder Blocker auf dem Gerät ist Reibung, und das einzig ehrliche Maß ist, wie lange der Weg hinaus dauert."
faq:
  - q: "Kann eine App Instagram auf dem iPhone sperren?"
    a: "Ja. Mit Apples Framework ManagedSettings kann eine App eines Drittanbieters die Instagram-App so sperren, dass beim Antippen ein Sperrbildschirm erscheint, statt dass sie startet, und sie kann instagram.com in Safari sperren, wenn du Webinhalte in die Auswahl aufnimmst. Was sie nicht kann: Mitteilungen von Instagram aufhalten, Instagram auf deinem iPad oder Laptop sperren oder verhindern, dass du dem Blocker in den Einstellungen die Erlaubnis entziehst, womit alle Sperren auf einmal fallen."
  - q: "Gibt es einen App-Blocker, den man nicht umgehen kann?"
    a: "Nicht auf deinem eigenen iPhone. Apple lässt den Widerruf mit Absicht in deiner Hand: Du kannst die Erlaubnis für Family Controls in den Einstellungen jederzeit zurückziehen, was die Tokens des Blockers ungültig macht und jede Sperre aufhebt. Ein Blocker kann verhindern, dass er gelöscht wird, und Reibung einbauen, etwa eine Rechenaufgabe oder eine Wartezeit, aber er kann sich nicht dauerhaft machen. Der einzige harte Fall ist ein Gerät, dessen Code für die Bildschirmzeit jemand anderes kennt, und das ist Kindersicherung, keine Selbstbeschränkung."
  - q: "Was ist die Family Controls API?"
    a: "FamilyControls ist das Apple-Framework, das den Zugang zur ganzen Screen Time API regelt. Es tut zwei Dinge: Es fragt nach der Erlaubnis, entweder im Einzelmodus (Selbstbeschränkung) oder im Kindmodus (ein Elternteil in der Familienfreigabe verwaltet ein minderjähriges Kind), und es zeigt den FamilyActivityPicker, die Systemoberfläche, in der du Apps, Kategorien und Websites auswählst. Zurück kommt eine FamilyActivitySelection aus undurchsichtigen Tokens. Wer das im App Store anbieten will, braucht eine eingeschränkte Berechtigung, die Apple auf Antrag vergibt."
  - q: "Funktionieren App-Blocker ohne Internetverbindung?"
    a: "Blocker auf Basis von Family Controls schon. Der Zustand der Sperren liegt in einem lokalen ManagedSettingsStore und wird von iOS selbst durchgesetzt, der Flugmodus ändert also nichts. DNS- und VPN-Filter sind das Gegenteil, denn sie sehen nur Netzwerkverkehr, tun also nichts gegen eine App, die offline läuft, oder gegen Inhalte, die schon auf dem Gerät zwischengespeichert sind, und wer das Profil in den Einstellungen ausschaltet, entfernt sie ganz. Offline zu funktionieren ist einer der deutlichsten Unterschiede zwischen beiden Ansätzen."
  - q: "Kann ein App-Blocker sehen, welche Apps ich gesperrt habe?"
    a: "Nein, und das erzwingt iOS; es ist nicht nur ein Versprechen der Entwickler. Apples Auswahl liefert Tokens, die Apples eigene Dokumentation als Darstellungen beschreibt, die die Identität einer Aktivität nicht preisgeben. Der Blocker speichert ein Token, gibt es an ManagedSettings zurück, um eine Sperre anzuwenden, und bekommt nie eine Bundle-ID oder einen Anzeigenamen. Er kann deine Auswahl weder protokollieren noch verkaufen noch verlieren, weil er sie nie hatte."
  - q: "Bildschirmzeit oder ein App-Blocker eines Drittanbieters?"
    a: "Die eingebaute Bildschirmzeit ist kostenlos, gilt auf allen Geräten mit demselben Apple Account, wenn du sie geräteübergreifend teilst, und lässt sich mit einem Code sperren, den jemand anderes kennt. Ihre Schwäche ist der Ausweg: dein eigener Code oder die Taste, mit der du ein Limit ignorierst. Ein Blocker eines Drittanbieters nutzt dieselbe Technik zur Durchsetzung, kann aber ändern, was das Entsperren kostet, und einen viel nützlicheren Sperrbildschirm zeigen. Viele fahren am besten mit beidem."
mentioned_apps:
  - earnlock
read_time: "15 Min. Lesezeit"
excerpt: "Eine iPhone-App eines Drittanbieters kann nicht sehen, was du öffnest, nicht dauerhaft im Hintergrund laufen und nicht über eine andere App zeichnen. Dieser Artikel zeigt, was die Screen Time API erlaubt, was das Design mit undurchsichtigen Tokens für Datenschutz und Produkt bedeutet und jeden Weg aus einer Sperre, nach Aufwand sortiert."
---

Frag die meisten, wie ein App-Blocker auf dem iPhone funktioniert, und du hörst ungefähr das: Der Blocker sitzt im Hintergrund, schaut zu, was du öffnest, und schlägt die Tür zu, sobald er Instagram entdeckt.

Nichts davon ist möglich. Eine iOS-App eines Drittanbieters kann nicht sehen, welche Apps du startest, kann nicht dauerhaft im Hintergrund laufen, um auf eine davon zu warten, und kann keinen einzigen Pixel über eine andere App zeichnen. Jeder Blocker im App Store bittet iOS, die Sperre für ihn zu übernehmen, über drei Frameworks, die Apple 2021 eingeführt und seitdem in kleinen Schritten erweitert hat.

Dieses Detail entscheidet, was dein Blocker kann, was er nie können wird, egal wie viel du zahlst, und wie genau du wieder herauskommst. Den letzten Teil zeigt kein Screenshot im App Store.

## Was sperrt auf dem iPhone eigentlich eine App?

Drei Frameworks, zusammen Screen Time API genannt, vorgestellt in der WWDC21-Session [Meet the Screen Time API](https://developer.apple.com/videos/play/wwdc2021/10123/){: hreflang="en"} (auf Englisch). Ein viertes, ManagedSettingsUI, bestimmt nur, wie der Sperrbildschirm aussieht. Die Dokumentation von Apple zu allen Frameworks unten ist auf Englisch.

| Framework | Seine eine Aufgabe | Die Typen, mit denen du arbeitest | Was es nicht kann |
|---|---|---|---|
| [FamilyControls](https://developer.apple.com/documentation/familycontrols){: hreflang="en"} | Erlaubnis einholen und den Nutzer Apps wählen lassen | `AuthorizationCenter`, [`FamilyActivityPicker`](https://developer.apple.com/documentation/familycontrols/familyactivitypicker){: hreflang="en"}, [`FamilyActivitySelection`](https://developer.apple.com/documentation/familycontrols/familyactivityselection){: hreflang="en"} | Deinem Code sagen, welche Apps gewählt wurden |
| [ManagedSettings](https://developer.apple.com/documentation/managedsettings){: hreflang="en"} | Die Beschränkung anwenden | `ManagedSettingsStore`, [`ShieldSettings`](https://developer.apple.com/documentation/managedsettings/shieldsettings){: hreflang="en"} (`.applications`, `.applicationCategories`, `.webDomains`), [`ApplicationSettings`](https://developer.apple.com/documentation/managedsettings/applicationsettings){: hreflang="en"} (`denyAppRemoval`) | Länger bestehen als die Erlaubnis, die sie geschaffen hat |
| [DeviceActivity](https://developer.apple.com/documentation/deviceactivity){: hreflang="en"} | Alles, was mit Zeit zu tun hat | `DeviceActivityCenter`, `DeviceActivitySchedule`, [`DeviceActivityEvent`](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent){: hreflang="en"}, `DeviceActivityMonitor` | Deinen Code dauerhaft laufen lassen; die Erweiterung wacht nur bei Ereignissen auf |
| [ManagedSettingsUI](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration){: hreflang="en"} | Den Sperrbildschirm gestalten | `ShieldConfigurationDataSource`, `ShieldActionDelegate` | Irgendetwas außer Titel, Untertitel, Symbol und bis zu zwei Tasten zeichnen |

In einer echten App ist der Ablauf kurz. Du fragst über `AuthorizationCenter.shared` nach der Erlaubnis, im Modus `.individual` zur Selbstbeschränkung oder `.child` für ein Elternteil in der Familienfreigabe. Du zeigst die Auswahl. Was zurückkommt, legst du in einem `ManagedSettingsStore` als `store.shield.applications` ab. Du registrierst einen Zeitplan bei `DeviceActivityCenter` und lässt iOS deine Erweiterung `DeviceActivityMonitor` an Intervallgrenzen und Nutzungsschwellen wecken, damit sie den Store ändern kann.

Zwei praktische Grenzen halten die Kategorie kleiner, als sie aussieht. Die Fähigkeit Family Controls fügt die Berechtigung [`com.apple.developer.family-controls`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls){: hreflang="en"} hinzu, und wer sie im App Store verteilen will, muss Apple darum bitten. Und die Erweiterung `DeviceActivityMonitor` ist kein Dienst, der ständig läuft: iOS weckt sie, gibt ihr ein kurzes Zeitfenster und legt sie wieder schlafen. Alles, was ein Blocker angeblich „dauerhaft“ tut, passiert in Momenten, die Apple wählt.

## Warum der Blocker nie erfährt, welche Apps du gewählt hast

Von allen Designentscheidungen der API hat diese die größten Folgen.

Die Oberfläche zur App-Auswahl ist der `FamilyActivityPicker`, und sie gehört Apple, nicht dem Entwickler. Sie läuft in einem eigenen Prozess, listet deine installierten Apps und liefert eine `FamilyActivitySelection` mit Mengen von Tokens zurück: `ApplicationToken`, `ActivityCategoryToken`, `WebDomainToken`. Apples Dokumentation zu [`Token`](https://developer.apple.com/documentation/managedsettings/token){: hreflang="en"} (auf Englisch) beschreibt es als Darstellung einer App oder Website, die ihre Identität nicht preisgibt, und die Seite zu `ApplicationToken` erklärt, der Zweck sei, Apps zu beschränken und zu filtern, ohne Zugriff auf persönliche Daten.

Ein Blocker hält also einen undurchsichtigen Datenblock in der Hand, den er an ManagedSettings zurückgibt, um eine Sperre zu errichten. Er bekommt nie eine Bundle-ID oder einen Anzeigenamen, und das Token lässt sich nicht zurückrechnen. Ein Token bedeutet auch nur für die App etwas, die es bekommen hat, und es verliert seine Gültigkeit in dem Moment, in dem du die Erlaubnis in den Einstellungen widerrufst, weil der Widerruf die Tokens der App zusammen mit ihrer Erlaubnis ungültig macht.

Für den Datenschutz heißt das: Eine App für Bildschirmzeit kann schlicht nicht protokollieren, dass du Grindr gesperrt hast, oder Trade Republic, oder die Lieblings-App deiner Ex. Sie hat nicht versprochen, es nicht zu tun; sie kann es nicht. Das ist Datenschutz durch Bauweise, und die stärkste Garantie dieser Art in allen Kategorien, in denen ich bisher Apps veröffentlicht habe.

Fürs Produkt ist es eine echte Abgabe, und jeder Entwickler in dieser Kategorie zahlt sie:

- Du kannst beim Einrichten kein „Sperr mit einem Tipp die üblichen Verdächtigen“ anbieten, weil du die Verdächtigen nicht benennen kannst.
- Du kannst in deinen eigenen Texten nicht sagen, welche Apps gerade gesperrt sind.
- Du kannst mit deinen eigenen Daten nicht prüfen, ob jemand überhaupt etwas ausgewählt hat, und so werden Supportanfragen („Es sperrt gar nichts“) zu angeleiteten Sitzungen mit Screenshots.

Diesen Tausch hat Apple gemacht, nicht der Entwickler, und ich finde, Apple hat richtig entschieden.

## Welcher Ansatz sperrt was?

Fünf Ansätze werden als „Apps sperren“ verkauft, und sie greifen auf ganz verschiedenen Ebenen ein. Der Preis zählt hier weniger als die Frage, wo jeder davon im System sitzt.

| Ansatz | Was er sperrt | Was er nicht sperren kann | Wie man ihn umgeht | Offline | Für wen er wirklich passt |
|---|---|---|---|---|---|
| **Eingebaute Bildschirmzeit** ([Apples Anleitung](https://support.apple.com/de-de/guide/iphone/iphbfa595995/ios)) | Zeitpläne und Nutzungszeiten für Apps und Kategorien (bis iOS 18 Auszeit und App-Limits), Altersfreigaben, Webinhalte; gilt auf deinen anderen Geräten, wenn du sie geräteübergreifend teilst | Nichts über Apples eigene Kategorien hinaus; keine eigene Bedingung fürs Entsperren | Dein eigener Code oder die Taste, mit der du ein Limit ignorierst | Ja | Alle, die sie noch nicht ausprobiert haben, denn sie ist kostenlos und deckt auch Mac und iPad ab |
| **Sperr-App auf Basis von Family Controls** (Opal, one sec, ScreenZen, Jomo, EarnLock) | Jede App oder Apple-Kategorie, die du auf diesem iPhone auswählst, dazu Websites in Safari bei Apps, die das unterstützen | Mitteilungen, andere Geräte und alles, nachdem du die Erlaubnis widerrufen hast | Der Notausgang, den die App mitbringt, danach der Widerruf der Erlaubnis in den Einstellungen | Ja, weil der Zustand lokal liegt und iOS ihn durchsetzt | Leute, die eine andere Bedingung fürs Entsperren wollen als „warten“ oder „Code eingeben“ |
| **DNS- oder VPN-Filter** ([NetworkExtension](https://developer.apple.com/documentation/networkextension){: hreflang="en"}, auf Englisch) | Domains und Verkehrsmuster, systemweit, auch in Apps, die du nicht ausgewählt hast | Alles im Mobilfunknetz, wenn das Profil aus ist, verschlüsseltes DNS innerhalb einer App oder einen Dienst, der sich ein CDN mit etwas teilt, das du brauchst | Das VPN in den Einstellungen ausschalten, ungefähr drei Tipps | Nein, es ist per Definition ein Netzwerkmechanismus | Ganze Klassen von Inhalten sperren (Werbung, Seiten für Erwachsene), keine bestimmte App |
| **Zweites Gerät oder Box** (einfaches Handy, Zeitschloss-Box, Bricks NFC-Tag) | Alles auf dem Gerät, das du zurücklässt | Jeden anderen Bildschirm im Haus | Den Gegenstand physisch holen | Ja | Leute, deren Problem eine Stunde an einem Ort ist: Schreibzeit, Abendessen, Schlaf |
| **Graustufen und Reibung** (Farbfilter, Fokus, Apps weg vom Home-Bildschirm) | Nichts; das Handy wird nur langweiliger und schwerer erreichbar | Alles, wenn du es wirklich willst | Drei Tipps in den Einstellungen oder Spotlight | Ja | Eher Gewohnheit als Zwang: Leute, die eine App ohne Grund öffnen und 40 Minuten bleiben |

Zwei Anmerkungen zur Tabelle. Ein DNS-Filter ist die einzige Zeile, die auch Apps erfasst, die du nicht aufgelistet hast. Das macht ihn zum richtigen Werkzeug, um Inhalte für Erwachsene zu sperren, und zum falschen für „halt mich zwischen 9 und 17 Uhr von X fern“. Und Apples eigene Prüfregeln engen die VPN-Zeile ein: [Richtlinie 5.4 der App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/){: hreflang="en"} (auf Englisch) verlangt, dass VPN-Apps `NEVPNManager` nutzen und von einem Entwickler stammen, der als Organisation angemeldet ist, und die Berechtigung für Inhaltsfilter vergibt Apple im Einzelfall. Deshalb gibt es so wenige davon.

## Kann eine App Instagram auf dem iPhone sperren?

Ja, mit drei Einschränkungen, die wichtiger sind als das Ja.

**Die App, und zwar richtig.** Wähl Instagram in der Auswahl, leg das Token in `store.shield.applications`, und beim Antippen des Symbols erscheint eine Sperre, statt dass die App startet. Die App öffnet sich nicht im Hintergrund, aktualisiert nicht und bekommt ihre fünf Sekunden nicht.

**Die Website, meistens.** `ShieldSettings.webDomains` deckt Safari ab. Wählst du in der Auswahl Webinhalte aus, verhält sich instagram.com in Safari wie die App. Wie gut das in Browsern anderer Anbieter und in Webansichten innerhalb von Apps greift, ist weniger vorhersehbar, und ich würde keinen Plan darauf bauen.

**Nicht die Mitteilungen.** Eine Sperre verhindert den Start. Sie verhindert nicht die Zustellung. Wenn dich ein Kennzeichen und ein Banner hineinziehen, repariert die Sperre die falsche Hälfte der Schleife, und ein Fokus ist das bessere Werkzeug, oder beides zusammen.

**Nicht deine anderen Bildschirme.** Der Store gilt nur auf dem Gerät. Dein iPad, dein Mac und der Arbeitslaptop bleiben unberührt. Family Controls gibt es auf macOS nicht in einer Form, die diese Mechanik unterstützt, also nutzt jede Sperr-App, die auch den Mac abdeckt, dort einen anderen Mechanismus.

## Gibt es einen App-Blocker, den man nicht umgehen kann?

Nein, nicht auf einem Gerät, das dir gehört und das du kontrollierst, und das ist Absicht. Könnte eine App eines Drittanbieters dein Handy dauerhaft beschränken, würde die erste bösartige App, die erscheint, eine Menge Handys lahmlegen, also lässt Apple den Ausgang in deiner Hand.

Einen Weg hinaus gibt es immer. Die nützliche Frage ist, wie lange er dauert und ob der Aufwand irgendwo Nutzen bringt. Hier ist die Leiter, die billigste Stufe zuerst.

| Weg hinaus | Ungefähr wie lange | Was es dich kostet | Merkt es die App? |
|---|---|---|---|
| Durchtippen oder eine Taste „Ich brauche das wirklich“, falls die App eine hat | 1 bis 2 Tipps, unter 5 Sekunden | Nichts | Ja, sie hat die Aktion ausgelöst |
| Einen Timer oder eine Atempause abwarten | 5 bis 60 Sekunden | Aufmerksamkeit, also genau das, was du schützen wolltest | Ja |
| Eine Hürde lösen: eine Rechenaufgabe, einen langen Satz abtippen | 20 bis 60 Sekunden | Konzentration, und darum geht es | Ja |
| Den Blocker löschen | ~10 Sekunden, außer `denyAppRemoval` ist gesetzt | Deine Einstellungen, deinen Verlauf, deine Serie | Nein, er ist weg |
| Family Controls in den Einstellungen widerrufen | ~15 Sekunden, wenn du den Weg kennst | Alle Sperren fallen auf einmal; die Tokens werden ungültig | Ja, [`authorizationStatus`](https://developer.apple.com/documentation/familycontrols/authorizationcenter/authorizationstatus){: hreflang="en"} lässt sich beobachten |
| Die Bildschirmzeit ganz ausschalten | ~20 Sekunden | Deine Limits und deinen Nutzungsverlauf | Ja |
| Das Gerät löschen und wiederherstellen | 30 Minuten und mehr | Alles | Nein |
| Jemand anderes kennt den Code für die Bildschirmzeit | Für dich nicht verfügbar | Selbstbestimmung, ein echter Preis, der sich manchmal lohnt | Entfällt |

Zwei Zeilen brauchen einen Kommentar. `ApplicationSettings.denyAppRemoval` gibt es wirklich: Ein Blocker kann das Löschen von Apps auf dem ganzen Gerät verhindern und schließt damit den billigsten Ausgang. Und der Widerruf lässt sich beobachten, eine App kann also ihren eigenen Erlaubnisstatus verfolgen und weiß sofort, wenn du gegangen bist. Ob sie damit mehr tun sollte, als es für dich festzuhalten, ist eine Designfrage mit einer offensichtlich falschen Antwort.

Lies die Leiter von oben nach unten, und „nicht umgehbar“ verliert jede Bedeutung. Was sich unterscheidet, ist, wie viele Sekunden zwischen dem Impuls und der App liegen und ob dir diese Sekunden etwas bringen.

## Was die API für das Design bedeutet

Ich habe vor einer Weile geschrieben, dass [die Kosten fürs Entsperren außerhalb der App liegen müssen](/journal/unlock-cost-outside-the-app/){: hreflang="en"} (auf Englisch): Kosten, die du selbst in der Software festlegst, kann dein Verlangen mitten im Verlangen neu verhandeln. Die API-Fakten oben führen dasselbe Argument auf der Ebene der Plattform. Der Widerruf ist immer etwa fünfzehn Sekunden entfernt, also ist die Mauer nicht das Produkt. Der Preis ist es.

Und dieser Preis sollte dort bezahlt werden, wo dein späteres Ich etwas davon hat. Warten besteht diesen Test nicht: Du zahlst mit Aufmerksamkeit, also genau dem, was du schützen wolltest, und bekommst nichts zurück. Bewegung besteht ihn, weil die Kosten im Rest deines Lebens landen.

Die anderen Designs sind deshalb nicht falsch. Mehrere sind gut für Probleme, die meins nicht löst:

**[one sec](/de/alternatives/one-sec/)** greift ein, *bevor* die App öffnet, mit einem Atemzug, einer Pause oder einer Frage. Wenn dein Daumen schneller ist als deine Absicht, passt das besser zu dir als eine harte Hürde, weil es den Reflex trifft. Eine Hürde, an der du dich schon vorbeigearbeitet hast, tut nichts gegen einen Reflex. one sec läuft außerdem auf Android, unsere Apps nicht.

**[Brick](/de/alternatives/brick/)** bringt einen physischen NFC-Tag ins Spiel, als einmaliger Kauf (63,95 € im Shop von Brick mit Lieferland Deutschland, geprüft am 29. Oktober 2026). Den Tag zu Hause zu lassen ist eine Verpflichtung, die du vom Sofa aus nicht rückgängig machen kannst, und es ist das einzige Design der Kategorie, bei dem die Reibung aus Material besteht statt aus Software, der du die Erlaubnis gegeben hast. Der Preis ist ein Gegenstand, den du kaufen, mitnehmen und verlieren kannst. [Unpluq](/de/alternatives/unpluq/) arbeitet nach demselben physischen Prinzip, kombiniert mit einem Abo.

**[ScreenZen](/de/alternatives/screenzen/)** ist kostenlos, mit Pausen, die immer länger werden, und kostenlos zu sein ist ein echter Vorteil, den EarnLocks Einmalkauf für {P_LIFETIME@earnlock} nicht aufwiegt. **[Opal](/de/alternatives/opal/)** und **[Jomo](/de/alternatives/jomo/)** sind ausgefeilter als wir, und Jomo deckt iPhone, iPad und Mac ab.

[EarnLock](/de/apps/earnlock/) nutzt genau dieselben drei Frameworks wie alle anderen und tut nichts, was Apple nicht veröffentlicht. Was die App ändert, ist der Preis: Die Apps, die du wählst, bleiben gesperrt, bis du ein tägliches Bewegungsziel erreichst, das sie aus Apple Health liest (Schritte in der kostenlosen Version, Bewegungsminuten oder aktive Kalorien mit Premium). Die Hälfte des Ziels öffnet sie für eine Stunde, das ganze Ziel bis Mitternacht. Ihr Sperrbildschirm ersetzt Apples allgemeinen Hinweis auf eine Beschränkung durch die Zahl, die noch fehlt. „noch 2026 Schritte bis zur Entsperrung“ sagt dir, wohin du gehst; ein Hinweis, dass diese App beschränkt ist, hält dich nur auf. Mit Premium liest die Apple-Watch-App ihre eigenen Health-Daten und zeigt, wie weit du noch vom Entsperren entfernt bist, während das iPhone die Sperre übernimmt. Welches Ziel du einstellen solltest, ist eine eigene Frage, beantwortet in [wie viele Schritte am Tag die Studien stützen](/de/journal/how-many-steps-a-day-to-aim-for/). Eine App zu sperren ist kostenlos; Premium kostet {P_MONTHLY@earnlock} im Monat, {P_YEARLY@earnlock} im Jahr oder einmalig {P_LIFETIME@earnlock}.

EarnLock hat dieselben Grenzen wie alles andere auf dieser Seite. Auch EarnLock sieht nicht, welche Apps du gesperrt hast. Die App hält keine Mitteilungen auf. EarnLock ist eine iPhone-App, mit einer Apple-Watch-App in Premium, und es gibt keine Version für iPad oder Mac. Die App hat eine Notentsperrung pro Tag, hinter einer Rechenaufgabe, mit Absicht, weil Leute ein Werkzeug ohne Ausgang löschen. Und wenn du in den Einstellungen ihre Erlaubnis widerrufst, fallen alle Sperren, und sie kann nichts dagegen tun. Dasselbe gilt für jede App auf Basis von Family Controls, die auf dieser Seite vorkommt, und es lohnt sich, das zu wissen, bevor du einem von uns Geld gibst. (Die Datenregeln dahinter, und hinter jeder anderen Lagerland-App, stehen auf der [Transparenzseite](/de/transparency/).)

## Kurz gesagt

- **Keine iPhone-App eines Drittanbieters sperrt selbst etwas.** Sie bittet iOS darum, über FamilyControls (Erlaubnis und Auswahl), ManagedSettings (die Sperre) und DeviceActivity (Zeitpläne und Schwellen).
- **Die Auswahl liefert undurchsichtige Tokens, keine App-Namen.** Dein Blocker kann nicht protokollieren, verkaufen oder verlieren, welche Apps du gewählt hast, weil iOS ihm die Namen nie gibt. Dieselbe Regel hindert ihn daran, dir eine empfohlene Liste vorzuschlagen.
- **Eine Sperre verhindert den Start, nicht die Mitteilung.** Sie deckt die App und über Web-Domains Safari ab. Sie deckt nicht dein iPad, deinen Mac oder das Banner, das dich hineingezogen hat.
- **Nichts ist unumgehbar, und das hat Apple so gewollt.** Family Controls in den Einstellungen zu widerrufen dauert etwa fünfzehn Sekunden und macht jede Sperre auf einmal ungültig. `denyAppRemoval` schließt den billigsten Ausgang; den letzten schließt nichts.
- **Vergleich also den Preis, nicht die Mauer.** Was sich unterscheidet, ist, was zwischen Impuls und App steht (ein Tipp, eine Wartezeit, ein physischer Tag oder eine Schrittzahl), und ob es dir danach besser geht, wenn du ihn bezahlst.
