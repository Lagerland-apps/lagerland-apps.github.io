# Apple's own French names (fr)

Part of the language sheet `_i18n/fr.md`. Verified 2026-11-07 on Apple's French pages (source per row). Use these exactly; never invent an Apple name.

Checked 2026-11-07 against Apple's live French pages (fetched directly with curl, `Accept-Language: fr-FR`, raw HTML read for characters). The iPhone and Apple Watch user guides on support.apple.com/fr-fr are for iOS 27 and watchOS 27. Apple France writes "vous" throughout, which matches the site's register.

How Apple writes them in running text:
- **App names** have NO quotes and no italics. Apple writes "l'app" + capitalized name: l'app Santé, l'app Fitness, l'app Fichiers, l'app Rappels, l'app Réglages, l'app Horloge, l'app Journal, l'app Caméra, l'app Cartes, l'app ECG, l'app Signes vitaux, l'app Pleine conscience, l'app Exercice (Apple Watch), l'app Apple Games. "app" is lowercase and is Apple's word (never "application" in the guides). Apple says "l'app App Store" and "l'App Store". Marketing pages (apple.com/fr) write the same: "l'app Santé sur iPhone", "l'app ECG".
- **Features and multi-word setting labels** go in French guillemets, with a no-break space inside: « Temps d'écran », « Suivi de cycle », « Ne pas déranger », « Texte en direct », « Annuler l'abonnement », « Confidentialité et sécurité » (the last one only sometimes; see next bullet). Single-word labels are written bare: Abonnements, Concentration, Général, Notifications, Sommeil, Résumé, Parcourir, Traitements.
- Menu paths use ">": "Réglages > Confidentialité et sécurité > Suivi" (spaces around ">").
- Capitalization is sentence style: only the first word and proper names get a capital. Setting labels keep a capital on the first word only: « Temps d'écran », « Mode économie d'énergie », « Partager avec les développeurs d'apps ». Common nouns for features stay lowercase in running text: les notifications, le centre de contrôle, un mode de concentration, le partage familial, la protection avancée des données, l'écran d'accueil, l'écran verrouillé, le compte Apple. Section and article titles are sentence case ("Utiliser le Mode sombre sur votre iPhone et votre iPad" is one exception: Apple's article 108350 capitalizes "Mode sombre").
- Gender and elision: l'iPhone, l'iPad, le Mac, l'Apple Watch, l'Apple Vision Pro, la Dynamic Island, l'App Store, l'iCloud (rare; usually "iCloud" alone), le compte Apple (lowercase "compte").
- Apple writes "évènements" (grave accent), "e-mail" (hyphen; the App Store pages use a non-breaking hyphen U+2011 in "e‑mail", "bien‑être", "ci‑dessous"), "Wi-Fi", "iOS 27 ou version ultérieure", "touchez" for tap, "balayez" for swipe, "sélectionnez"/"choisissez".

Punctuation and spacing (checked in raw bytes on 8 Apple pages: support guides, support articles, apple.com/fr/health, apps.apple.com/fr):
- Guillemets: « » with **U+00A0 NO-BREAK SPACE** inside on both sides (`«&nbsp;Annuler l'abonnement&nbsp;»`). Counted 49 « and 49 » on one iPhone guide page: 49 of 49 use U+00A0 on each side. Never a normal space, never U+202F.
- Before `:`, `?` and `;`: **U+00A0** (`&nbsp;:`). No U+202F (NARROW NO-BREAK SPACE) was found next to Apple's own text on any Apple page checked (U+202F appears only inside other developers' App Store descriptions, which are not Apple's text). No `!` was present on the pages checked.
- Apple does NOT use English curly quotes for UI labels; the only “ ” seen is for a spoken Siri example ("Fais sonner mon réveil à 7 h du matin.", guide iph2909d3a74).
- Apostrophe: **U+2019 (')** on all pages (336 on one guide page). Rare stray U+02BC (ʼ) in a few support pages ("lʼécran", "Jʼaimerais", "lʼApp Store"), plus one straight U+0027. Use U+2019.
- Numbers: thousands separator, space before % and before °C are all **U+00A0**: `100 000`, `80 %`, `35 °C`, `2e génération`. Decimal comma: `9,9 Mo`, `92,7 Mo` (NBSP before Mo), `2,99 €` (NBSP before €). Times: "7 h".
- Product names: Apple's HTML often (not always) uses U+00A0 inside "App Store" and "Apple Watch" (e.g. `App&nbsp;Store` in every App Store meta tag; 54 of 55 "Apple Watch" on apple.com/fr/health). The same word is plain-spaced on some support articles (118428, 118223), so both occur.
- apple.com marketing text contains soft hyphens (U+00AD) inside words ("inno­vations", "notifi­cations"); do not copy them.

Transcription note: in this file apostrophes are typed as straight `'` and « » are shown with ordinary spaces for readability. Apple's real characters are U+2019 for the apostrophe and U+00A0 inside « » (see above); use those on the site.

Abbreviations: ap = apps.apple.com/fr, ah = https://www.apple.com/fr/health/, ig = iPhone user guide https://support.apple.com/fr-fr/guide/iphone/welcome/ios (table of contents), wg = Apple Watch user guide https://support.apple.com/fr-fr/guide/watch/welcome/watchos, mg = Mac user guide https://support.apple.com/fr-fr/guide/mac-help/welcome/mac.

## Health and fitness

| English | French as Apple writes it | Source | Note |
|---|---|---|---|
| Health (app) | Santé; l'app Santé | https://support.apple.com/fr-fr/guide/iphone/iphcae7451f3/ios ; ah | Translated, unlike German. Never "Health" |
| Apple Health | Apple Santé | ah (page title "Apple Santé – Apple (FR)") | Translated. Developers' App Store text still says "Apple Health"; Apple's own pages do not |
| Health data | données de santé; données Santé (as the app's data, capitalized "Santé") | https://support.apple.com/fr-fr/guide/iphone/iphcae7451f3/ios ; ig TOC ("Sauvegarder ses données Santé") | |
| Health records | dossiers médicaux | same page; ig TOC ("Afficher des dossiers médicaux") | |
| Medical ID | renseignements médicaux (« Renseignements médicaux ») | https://support.apple.com/fr-fr/guide/iphone/iphcae7451f3/ios | |
| Health category (Summary pins) | catégories de santé; écran Résumé; liste Épinglés; « Catégories de Santé » (Browse screen); tab Parcourir | https://support.apple.com/fr-fr/guide/iphone/iphe3d379c32/ios | |
| Sleep (in Health) | Sommeil (Configurer Sommeil); programme de sommeil; historique de sommeil | ig TOC; https://support.apple.com/fr-fr/guide/iphone/iphaf56dceb4/ios | |
| Sleep Focus | mode de concentration Repos | https://support.apple.com/fr-fr/guide/iphone/iphaf56dceb4/ios | iOS 27 name is Repos, not Sommeil |
| Sleep Score | Score de sommeil | ah; wg ("Consulter son score de sommeil") | Capital S in marketing, lowercase in the guide |
| Sleep apnea notifications | Notifications d'apnée du sommeil | wg; ah | |
| Heart Rate Variability (HRV) | variabilité de la fréquence cardiaque; abbreviation **VFC** | https://support.apple.com/fr-fr/guide/watch/apda88aefe4c/watchos ; ah ("désormais votre VFC") | Apple FR abbreviates it VFC, not HRV. Observa's own store title uses "VFC" |
| Resting heart rate | fréquence cardiaque au repos (Watch: « Au repos ») | https://support.apple.com/fr-fr/guide/watch/apda88aefe4c/watchos ; https://support.apple.com/fr-fr/guide/iphone/iphe3d379c32/ios | |
| Heart rate | fréquence cardiaque; l'app Fréquence cardiaque (Watch) | same | |
| Heart rate zones | zones de fréquence cardiaque | wg ("Consulter les zones de fréquence cardiaque"); ah | |
| ECG app | l'app ECG; Électrocardiogramme (ECG) (Health category) | https://support.apple.com/fr-fr/guide/watch/apdea4c50a57/watchos ; ah | |
| AFib History | Historique de FA | ah | FA = fibrillation auriculaire |
| Vitals app | l'app Signes vitaux; Signes vitaux nocturnes / diurnes | https://support.apple.com/fr-fr/guide/watch/apd15aa7ed96/watchos ; ah | One page also has "Signaux vitaux" once (typo on Apple's side); the app name is Signes vitaux |
| Readiness app (watchOS 27) | l'app Préparation; score de préparation | https://support.apple.com/fr-fr/guide/watch/flx4gnzby346/watchos (EN: https://support.apple.com/en-us/guide/watch/flx4gnzby346/watchos) ; ah ("Préparation") | |
| Training Load | charge d'entraînement | wg ("Suivre sa charge d'entraînement"); ah | |
| Cardio Fitness | forme cardiaque (marketing); no distinct feature label found in the guides | ah ("estime la forme cardiaque") | See Unverified |
| VO2 max | VO₂ max (marketing writes VO with a subscript 2, then "max") | ah | |
| Cycle Tracking | Suivi de cycle (« Suivi de cycle »); l'app Suivi de cycle (Watch) | ah; ig TOC ("Suivre son cycle menstruel"); https://support.apple.com/fr-fr/guide/iphone/iphcae7451f3/ios | |
| Mindfulness app | l'app Pleine conscience | ah | |
| State of Mind | État d'esprit (Parcourir > « Bien-être mental » > « État d'esprit ») | https://support.apple.com/fr-fr/guide/iphone/iph6a6decb13/ios ; ah | |
| Medications | Traitements (feature, Parcourir > Traitements); médicaments (the word) | https://support.apple.com/fr-fr/guide/iphone/iph811670c81/ios ; https://support.apple.com/fr-fr/guide/iphone/iphcae7451f3/ios | Feature = Traitements, not Médicaments |
| Walking Steadiness | stabilité de la marche | https://support.apple.com/fr-fr/guide/iphone/iphff1bf03ed/ios | |
| Activity rings | anneaux Activité | https://support.apple.com/fr-fr/guide/iphone/iph4c34a8a95/ios ; ah | "Activité" capitalized after "anneaux" |
| Move / Exercise / Stand rings | anneau « Bouger » / anneau « M'entraîner » / anneau « Me lever » | same | The Exercise ring is « M'entraîner », the Stand ring « Me lever » |
| Fitness app | l'app Fitness (guide); l'app Forme (apple.com/fr health page); widget Forme (guide) | https://support.apple.com/fr-fr/guide/iphone/ipha5dddb411/ios ; ah | Apple FR uses both Fitness and Forme. The iPhone guide's app name is Fitness; use Fitness |
| Workout app | l'app Exercice (Apple Watch); onglet Exercice (Fitness on iPhone); exercice (workout) | https://support.apple.com/fr-fr/guide/watch/apdd16e8761a/watchos ; https://support.apple.com/fr-fr/guide/iphone/ipha5dddb411/ios | "Workout" is not used; the unit is "exercice", the app is Exercice |
| Apple Watch | l'Apple Watch (feminine in Apple's French: "votre Apple Watch") | https://www.apple.com/fr/watch/ ; ah | English kept |
| Apple Fitness+ | Apple Fitness+ | https://support.apple.com/fr-fr/guide/iphone/iph4c34a8a95/ios ; https://www.apple.com/fr/apple-fitness-plus/ | English kept |
| Journal app | l'app Journal | https://support.apple.com/fr-fr/guide/iphone/iph9824e83ce/ios | |

## System features

| English | French as Apple writes it | Source | Note |
|---|---|---|---|
| Settings | l'app Réglages; Réglages Système (Mac) | https://support.apple.com/fr-fr/guide/iphone/iphbfa595995/ios ; https://support.apple.com/fr-fr/108922 | |
| Screen Time | « Temps d'écran » | https://support.apple.com/fr-fr/guide/iphone/iphbfa595995/ios | Quoted in the iOS 27 guide; bare in the iOS 18 article |
| Downtime (iOS 18 and earlier) | « Temps d'arrêt » | https://support.apple.com/fr-fr/guide/iphone/iphb0c7313c9/18.0/ios/18.0 | iOS 27 replaced Downtime/App Limits with programmes and temps accordés |
| App Limits (iOS 18 and earlier) | « Limites d'app » | same | |
| Screen Time Schedules (iOS 27) | « Programme de temps d'écran »; programmes | https://support.apple.com/fr-fr/guide/iphone/iphb0c7313c9/ios ; EN: https://support.apple.com/en-us/guide/iphone/iphb0c7313c9/ios | |
| Time Allowances (iOS 27) | « Temps accordés »; « Temps autorisés » (menu label on the same page) | same | Apple uses both spellings on one page (accordés in the body, autorisés as the tap target) |
| Always Allowed | « Toujours autorisées » | same | |
| Screen Distance | Distance de l'écran | ah | Marketing page only; not in the iPhone guide TOC |
| Focus | Concentration; mode de concentration | https://support.apple.com/fr-fr/guide/iphone/iphd6288a67f/ios | Singular modes: Travail, « Temps pour soi », Repos |
| Do Not Disturb | « Ne pas déranger » | same | |
| Reduce Interruptions (Focus) | « Réduire les interruptions » | same | Uses Apple Intelligence |
| Family Sharing | partage familial; groupe de partage familial (Partage familial capitalized in headings and menus) | ig TOC; https://support.apple.com/fr-fr/guide/iphone/iphc90580097/ios ; ap ("Partage familial") | |
| Parental controls (Family Controls) | contrôle parental; « Contrôle parental » (as in "Configurer le contrôle parental sur l'appareil d'un enfant") | https://support.apple.com/fr-fr/guide/iphone/iphc90580097/ios | "Family Controls" is the framework name; developer docs are English |
| In-App Purchases | achats intégrés (store label "Achats intégrés") | ap; https://support.apple.com/fr-fr/guide/iphone/iph4e3e7324f/ios | |
| Subscriptions (manage) | "Dans Réglages, touchez votre nom. Touchez Abonnements. Touchez l'abonnement concerné. Touchez Annuler l'abonnement." (Mac: "Résilier l'abonnement") | https://support.apple.com/fr-fr/118428 | Article title: "Résilier un abonnement Apple". iPhone guide path: "Accédez à l'app Réglages, touchez votre nom, puis touchez Abonnements" |
| Apple Account (ex Apple ID) | compte Apple (lowercase "compte"); the button/screen: Compte Apple | https://support.apple.com/fr-fr/guide/iphone/iph76e54c61e/ios ; https://support.apple.com/fr-fr/118223 | Apple never writes "identifiant Apple" in the iOS 27 guide |
| iCloud | iCloud | https://support.apple.com/fr-fr/guide/iphone/iphde0f868fd/ios | |
| iCloud+ | iCloud+ | same; https://www.apple.com/fr/icloud/ | English kept |
| iCloud Drive | iCloud Drive | https://support.apple.com/fr-fr/guide/iphone/iphe9d46e90f/ios | |
| iCloud Photos | Photos iCloud | https://support.apple.com/fr-fr/guide/iphone/iph961b96c4d/ios | |
| Sync this iPhone | « Synchroniser cet iPhone » | https://support.apple.com/fr-fr/guide/iphone/iph961b96c4d/ios | Verified for the Photos toggle |
| Home Screen | écran d'accueil | https://support.apple.com/fr-fr/102638 ; ig TOC | |
| Lock Screen | écran verrouillé (guide); écran de verrouillage (article 102638) | same | Guide uses "écran verrouillé"; use that |
| Widgets | widgets; galerie de widgets | https://support.apple.com/fr-fr/guide/iphone/iphb8f1bf206/ios | |
| Smart Stack | Défilement intelligent (name); "un défilement intelligent" (iPhone guide, common noun); "pile Défilement intelligent" | https://support.apple.com/fr-fr/guide/iphone/iphb8f1bf206/ios ; wg ("Afficher des widgets dans Défilement intelligent") | Not translated as "Smart Stack" |
| Live Activities | activités en direct; « Activités en direct » (setting) | https://support.apple.com/fr-fr/guide/iphone/iph28f50d10d/ios ; https://support.apple.com/fr-fr/guide/iphone/iph3d92302ee/ios | |
| Dynamic Island | Dynamic Island (feminine: "la Dynamic Island", "dans la Dynamic Island") | https://support.apple.com/fr-fr/guide/iphone/iph28f50d10d/ios | English kept |
| Control Center | centre de contrôle | https://support.apple.com/fr-fr/guide/iphone/iph59095ec58/ios | Lowercase, no capitals |
| Notification Center | centre de notifications | https://support.apple.com/fr-fr/guide/iphone/iph6534c01bc/ios | |
| Notifications | notifications | same | |
| Share Sheet | menu Partager; bouton Partager | https://support.apple.com/fr-fr/guide/iphone/iphc572ca489/ios | |
| AirDrop | AirDrop | https://support.apple.com/fr-fr/guide/iphone/iphcd8b9f0af/ios | English kept |
| Spotlight | Spotlight | https://support.apple.com/fr-fr/guide/iphone/iph3c511548/ios | English kept |
| Siri | Siri | ig TOC; https://support.apple.com/fr-fr/guide/iphone/iph83aad8922/ios | |
| Apple Intelligence | Apple Intelligence | ig TOC; https://www.apple.com/fr/apple-intelligence/ (page title "Apple Intelligence et Siri – Apple (FR)") | English kept |
| Shortcuts (app) | l'app Raccourcis; raccourcis (user shortcuts) | ig TOC ("Raccourcis"); https://support.apple.com/fr-fr/guide/iphone/iph3c511548/ios | |
| Airplane Mode | mode Avion | https://support.apple.com/fr-fr/guide/iphone/iph59095ec58/ios ; wg ("Utiliser le mode Avion") | |
| Low Power Mode | « Mode économie d'énergie » | https://support.apple.com/fr-fr/guide/iphone/iphcab9aecd1/ios | Parent label "Mode d'alimentation" |
| Dark Mode | Mode sombre (setting: « Luminosité et affichage » > Sombre) | https://support.apple.com/fr-fr/108350 | Capital M in this article |
| Accessibility | Accessibilité | ig TOC; ap ("Accessibilité" section) | |
| VoiceOver | VoiceOver | ig TOC | English kept |
| Larger Text (Dynamic Type setting) | « Grande police »; « Tailles de police plus grandes » (Réglages > Accessibilité > Affichage et taille du texte) | https://support.apple.com/fr-fr/guide/iphone/iph3c076905a/ios | |
| Reduce Motion | « Réduire les animations » (Réglages > Accessibilité > Animation) | https://support.apple.com/fr-fr/111781 | The Tare store page also says "Réduire les animations" |
| Offline | hors ligne ("mode hors ligne", "Télécharger des plans hors ligne") | ig TOC | |
| Privacy & Security | Confidentialité et sécurité (bare in paths; "Réglages > Confidentialité et sécurité") | https://support.apple.com/fr-fr/guide/iphone/iph251e92810/ios | |
| App Tracking | Suivi (Réglages > Confidentialité et sécurité > Suivi); toggle « Autoriser les demandes de suivi des apps » | https://support.apple.com/fr-fr/guide/iphone/iph4f4cbd242/ios ; https://support.apple.com/fr-fr/102420 | See App Tracking Transparency in the store section |

## Built-in apps

| English | French as Apple writes it | Source | Note |
|---|---|---|---|
| Reminders | Rappels (l'app Rappels) | ig TOC | |
| Calendar | Calendrier (l'app Calendrier) | ig TOC | |
| Files | Fichiers (l'app Fichiers) | https://support.apple.com/fr-fr/guide/iphone/iphe9d46e90f/ios | |
| Photos | Photos (l'app Photos) | ig TOC | |
| Camera | Caméra (l'app Caméra) | https://support.apple.com/fr-fr/guide/iphone/iphcf0b71b0e/ios ; ig TOC (section "Caméra") | Not "Appareil photo" in the iOS 27 guide |
| Shortcuts | Raccourcis | ig TOC | |
| Notes | Notes | ig TOC | |
| Clock / Alarm | Horloge / Alarmes (réveil; "Régler une alarme dans l'app Horloge") | https://support.apple.com/fr-fr/guide/iphone/iph2909d3a74/ios | |
| Games app | l'app Apple Games | https://support.apple.com/fr-fr/guide/iphone/iph3aed54d2e/ios | English "Apple Games", not "Jeux" (the App Store tab is "Jeux") |
| Game Center | Game Center ("Configurer le profil Game Center") | ig TOC | English kept |
| Wallet / Apple Pay | l'app Cartes / Apple Pay ("Configurer des cartes dans Cartes") | https://support.apple.com/fr-fr/guide/iphone/iph9b7f53382/ios | Wallet is named Cartes in French |
| Passwords | Mots de passe | ig TOC | |
| Maps | Plans | ig TOC; https://support.apple.com/fr-fr/guide/iphone/iph28f50d10d/ios | |

## Devices and platforms

| English | French as Apple writes it | Source | Note |
|---|---|---|---|
| iPhone, iPad, Mac | iPhone, iPad, Mac (l'iPhone, l'iPad, le Mac) | ap; ig | |
| Apple Watch | l'Apple Watch | ap; ah | |
| Apple Vision Pro | l'Apple Vision Pro | https://www.apple.com/fr/apple-vision-pro/ ; ig TOC | App Store compatibility label says "Apple Vision" |
| iOS, iPadOS, macOS, watchOS, visionOS | unchanged | ap ("Nécessite iOS 18.0 ou version ultérieure.") | |
| Designed for iPad (on Mac) | "Conçue pour iPad. Non validée pour macOS." | https://apps.apple.com/fr/app/id6757438990 | Exact App Store wording, feminine because "app" |

## App Store and developer

| English | French as Apple writes it | Source | Note |
|---|---|---|---|
| App Store | App Store (l'App Store; l'app App Store) | https://support.apple.com/fr-fr/guide/iphone/iphc90580097/ios | |
| "Download on the App Store" badge | Line 1: **Télécharger dans** / Line 2: **l'App Store** | https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/fr-fr (SVG title "Download_on_the_App_Store_Badge_FR_RGB_blk_100517"; same file from https://toolbox.marketingtools.apple.com/api/v2/badges/download-on-the-app-store/black/fr-fr; rendered and read 2026-11-07) | The artwork is outlined paths, so no apostrophe character exists in the file. The drawn apostrophe is a straight, tapered tick (typewriter style), not a curly one. Use Apple's fr-fr badge artwork, never retype it. In HTML alt text write "Télécharger dans l'App Store" with U+2019 |
| "Download on the Mac App Store" badge | Line 1: **Télécharger dans le** / Line 2: **Mac App Store** | https://tools.applemediaservices.com/api/badges/download-on-the-mac-app-store/black/fr-fr (rendered and read) | |
| App Privacy (section) | Confidentialité de l'app | https://apps.apple.com/fr/app/id6806255929 | Section heading, shown twice |
| Data Not Collected | Données non collectées | same | Sub-line: "Le développeur ne collecte aucune donnée avec cette app." |
| Privacy nutrition label | étiquette de confidentialité | https://www.apple.com/fr/privacy/ ("vous avez accès à son étiquette de confidentialité"); https://developer.apple.com/fr/support/third-party-SDK-requirements/ ("étiquettes de confidentialité") | Store section is titled "Confidentialité de l'app" |
| Privacy Manifest | manifeste de confidentialité (plural manifestes de confidentialité; "fichiers manifestes de confidentialité") | https://developer.apple.com/fr/support/third-party-SDK-requirements/ | This one developer page is translated. Most developer.apple.com/fr pages 404 or show English navigation |
| App Store Connect | App Store Connect | https://developer.apple.com/fr/support/ (English nav) | English kept; no French page |
| TestFlight | TestFlight | https://developer.apple.com/fr/support/ (nav) | English kept |
| Xcode | Xcode | https://developer.apple.com/fr/support/ (nav); body text on https://developer.apple.com/fr/support/third-party-SDK-requirements/ | English kept |
| CloudKit | CloudKit | developer.apple.com (framework docs are English only) | Framework name, never translated |
| Feedback Assistant | Feedback Assistant | https://developer.apple.com/fr/support/ (nav is English on the French site) | No French name found (see Unverified) |
| App Tracking Transparency | App Tracking Transparency (name kept; support article title is "Si une app vous demande de suivre votre activité") | https://support.apple.com/fr-fr/102420 | Buttons: « Autoriser » and « Demander à l'app de ne pas suivre mes activités ». Toggle: « Autoriser les demandes de suivi des apps ». Verb phrase "suivre votre activité" |
| Report a Problem (reportaproblem.apple.com) | Apple's article names the site only: "Connectez-vous au site reportaproblem.apple.com." The menu entry is « J'aimerais » > « Demander un remboursement ». Apple's guide headings use "Signaler un problème avec une app" / "Signaler un problème avec un jeu" | https://support.apple.com/fr-fr/118223 ; https://support.apple.com/fr-fr/guide/app-store/fir52b1849e1/mac ; https://support.apple.com/fr-fr/guide/iphone/iphcae7451f3/ios (TOC) | The reportaproblem.apple.com page needs JavaScript and shows only a sign-in shell, so its own title was not read |
| Refund request | « Demander un remboursement »; article "Demander un remboursement pour des apps ou des contenus achetés auprès d'Apple" | https://support.apple.com/fr-fr/118223 | Steps: Connectez-vous au site reportaproblem.apple.com > « J'aimerais » > « Demander un remboursement » > choisissez le motif > « Suivant » > choisissez l'app > Envoyer. "Patientez 24 à 48 heures" |
| Restore purchases | Apple's phrase: "restaurer les achats"; article "Restaurer les éléments achetés et supprimés sur l'iPhone"; article "Télécharger à nouveau des apps auprès d'Apple" (button Retélécharger; path: App Store > votre photo > « Apps et historique d'achats » > « Vos apps ») | https://support.apple.com/fr-fr/guide/iphone/iphfe205f2e5/ios ; https://support.apple.com/fr-fr/102417 | The in-app StoreKit button text is not on a French Apple page (see Unverified) |
| Purchase history | « Historique des achats » (App Store > votre photo > « Apps et historique d'achats ») | https://support.apple.com/fr-fr/guide/iphone/iph4e3e7324f/ios | |
| Universal Purchase | UNVERIFIED | no French Apple page found (developer.apple.com/fr/... pages 404) | See below |

## French App Store product page labels

Copied from https://apps.apple.com/fr/app/id6806255929 (Tare) and https://apps.apple.com/fr/app/id6757438990 (Observa).

| Label | Exact French text |
|---|---|
| Price line (free app with IAP) | `Gratuit · Achats intégrés` (Observa adds `· Conçue pour iPad. Non validée pour macOS.`). Separators are plain space, U+00B7 MIDDLE DOT, plain space |
| Free | Gratuit |
| Get button | Obtenir |
| Ratings section | Notes et avis (aria/section title); Observa shows "5,0" then "sur 5", then "1 notes" (Apple's own plural bug; do not copy). Empty state: "Cette app n'a pas reçu suffisamment de notes ou d'avis pour en proposer un aperçu." |
| Age rating | header chip: Catégorie d'âge, value "4+" with caption "Ans" (Observa: "9+" "Ans"); Information row: Âge "4+"; Observa adds Contient: "Sujets liés à la santé ou au bien‑être" (U+2011 in "bien‑être") |
| Category | header chip and row: Catégorie (Tare: Casse-tête; Observa: Forme et santé) |
| Developer | header chip: **Création** (shows the developer name); Information row: **Fournisseur** |
| Language | header chip: Langue ("FR + 43 autres"); Information row: Langues ("Français et 43 de plus", then the full list) |
| Size | Taille: `9,9 Mo`, `92,7 Mo` (U+00A0 before Mo) |
| Compatibility | Compatibilité: "Nécessite iOS 18.0 ou version ultérieure." / "Nécessite iPadOS 18.0 ou version ultérieure." / Mac: "Nécessite macOS 14.6 ou une version ultérieure et un Mac doté d'une puce Apple M1 ou une version ultérieure." / Apple Watch: "Nécessite watchOS 10.0 ou version ultérieure." / Apple Vision: "Nécessite visionOS 1.3 ou version ultérieure." |
| Info section heading | Informations |
| In-App Purchases | Achats intégrés: "Oui", then one row per item |
| Accessibility | Accessibilité ("Le développeur n'a pas encore indiqué quelles fonctionnalités d'accessibilité sont prises en charge par cette app.") |
| Family Sharing | Partage familial: "Certains achats et abonnements intégrés peuvent être partagés avec votre groupe familial lorsque le partage familial est activé." |
| Privacy section | Confidentialité de l'app; "Données non collectées"; link "Définitions et exemples de la confidentialité"; disclaimer "Ces informations n'ont pas été vérifiées par Apple." |
| Privacy policy link | Confidentialité (Information section link); aria label "Politique de confidentialité du développeur" |
| Developer website | Site web du développeur |
| Other sections | Nouveautés (with Version 1.1 27 oct.); Plus d'apps par <developer>; Vous aimerez peut-être aussi; Aperçus d'apps et captures d'écran; Partager; Assistance (footer) |
| Platform names in nav | iPhone, iPad, Mac, Vision, Watch, TV (nav tabs: Aujourd'hui, Jeux, Apps, Arcade, Rechercher) |
| Meta title / description | "App <name> - App Store" (U+00A0 inside "App Store"); "Téléchargez l'app <name> développée par <developer> dans l'App Store. Consultez les captures d'écran, les notes et avis, les astuces…" |

In-app purchase price format: `2,99 €`. Comma decimal, then a **NO-BREAK SPACE (U+00A0)**, then €. Checked in the raw HTML (Tare "Chapitres II–X 2,99 €"; Observa Premium annuel `24,99 €`, Premium mensuel `3,99 €`, Premium achat unique `59,99 €`, Soutenir le développeur `1,00 €`). The IAP names are the developer's display names, not Apple UI.

## French App Store category names

Read from the "Catégorie" field of live apps.apple.com/fr/app/id... pages on 2026-11-07 (sample app and ID in the last column). The `apps.apple.com/fr/genre/...` pages return 404 for a plain fetch, so category names come from app pages.

| English | French as the App Store shows it | Sample page (https://apps.apple.com/fr/app/id...) |
|---|---|---|
| Health & Fitness | Forme et santé (NOT "Santé et forme") | id6757438990 (Observa) |
| Productivity | Productivité | id1232780281 |
| Finance | Finance (singular) | id283646709 |
| Business | Économie et entreprise | id618783545 |
| Developer Tools | Outils de développement | id6756589122 (Mockly) |
| Games > Puzzle | Casse-tête | id6806255929 (Tare) |
| Games > Board | Jeux de société | id6761336870, id6761656926, id6794340136, id6759511759 |
| Games > Strategy | Stratégie | id529479190 |
| Games > Adventure | Aventure | id479516143 |
| Games (tab) | Jeux | nav tab on every page |
| Utilities | Utilitaires | id6757253009 |
| Education | Éducation | id570060128 |
| Books | Livres | id302584613 |
| Lifestyle | Style de vie | id429047995 |
| Graphics & Design | Graphisme et design | id916366645 |
| Photo & Video | Photo et vidéo | id1500855883 |
| Reference | Références (plural) | id324715238 |
| Entertainment | Divertissement | id363590051 |
| Travel | Voyages | id401626263 |
| Music | Musique | id324684580 |
| Navigation | Navigation | id585027354 |
| Food & Drink | Cuisine et boissons | id1058959277 |
| News | Actualités | id1064216828 |
| Sports | Sports | id382002079 |
| Medical | Médecine | id321367289 |
| Weather | Météo | id295646461 |
| Shopping | Shopping | id282614216 |
| Social Networking | Réseaux sociaux | id310633997 |

Not checked: Magazines & Newspapers, Kids, other Games subcategories (Action, Card, Casino, Casual, Family, Music, Racing, Role Playing, Simulation, Sports, Trivia, Word).

## Unverified (best guesses, not confirmed on an Apple page)

| English | Best guess | Why unverified |
|---|---|---|
| Report a Problem (feature name) | « Signaler un problème » | Apple's FR guides use "Signaler un problème avec une app" (Mac App Store guide, https://support.apple.com/fr-fr/guide/app-store/fir52b1849e1/mac) and "Signaler un problème avec un jeu" (iPhone guide TOC), but the reportaproblem.apple.com page itself is JavaScript only and Apple's refund article names only the URL |
| Restore Purchases (in-app button) | « Restaurer les achats » | Apple writes "restaurer les achats" in running text (iPhone guide iphfe205f2e5), but the StoreKit button label is not documented on a French Apple page |
| Universal Purchase | "Universal Purchase" (English kept) or "achat universel" | developer.apple.com/fr/... help pages 404; no French Apple page |
| Cardio Fitness (feature label) | « Forme cardio » or "forme cardiaque" | Only the marketing page's "forme cardiaque" was found; no guide label |
| Dynamic Type (developer term) | Dynamic Type (English kept) | HIG and developer docs are not localized; the user-facing settings are « Grande police » and « Tailles de police plus grandes » (verified) |
| Feedback Assistant | Feedback Assistant | developer.apple.com/fr nav is English; no French name |
| Family Controls (framework) | Family Controls (English kept); user-facing: contrôle parental | Developer docs are English only |
| Privacy manifest (file name) | PrivacyInfo.xcprivacy / "manifeste de confidentialité" | Only the SDK requirements page is translated; Xcode docs are English only |
| Apple Push Notification service (APNs) | Apple Push Notification service (APNs) | https://support.apple.com/fr-fr/guide/security/aside/sec19eabb530/web is English even on fr-fr; the whole Apple Platform Security guide is English there |
| Data Protection (iOS file encryption) | "protection des données" / "Data Protection" | https://support.apple.com/fr-fr/guide/security/secf6276da8a/web is English only |
| "Autoriser « App » à suivre vos activités…" (the ATT prompt title) | « Autoriser « <App> » à suivre vos activités dans les apps et sur les sites web d'autres sociétés ? » | The system prompt text is not on any Apple page fetched; only its two button labels and the setting names are (see App Tracking Transparency) |
| Advanced Data Protection (settings label) | « Protection avancée des données » | Running text confirmed (lowercase, with the preposition: "la protection avancée des données pour iCloud"); the exact tap-target spelling was not read on a settings path |

## Added from reviews (same rows as the German file)

| English | French as Apple writes it | Source | Note |
|---|---|---|---|
| Advanced Data Protection (for iCloud) | in running text: "la protection avancée des données pour iCloud" (lowercase); standard mode: "la protection standard des données" | https://support.apple.com/fr-fr/108756 ; https://support.apple.com/fr-fr/102651 (checked 2026-11-07) | Article title: "Activer la protection avancée des données pour iCloud" |
| Standard data protection (iCloud) | "Protection standard des données" (heading); "la protection standard des données" (running text) | https://support.apple.com/fr-fr/102651 | |
| Privacy & Security (Settings) | Confidentialité et sécurité | https://support.apple.com/fr-fr/guide/iphone/iph4f4cbd242/ios | |
| Reduce Motion (setting label) | « Réduire les animations » (Réglages > Accessibilité > Animation) | https://support.apple.com/fr-fr/111781 (checked 2026-11-07) | |
| Data Protection (iOS file encryption) | not available in French | https://support.apple.com/fr-fr/guide/security/secf6276da8a/web is English only | See Unverified |
| Share With App Developers (Analytics & Improvements) | « Partager avec les développeurs d'apps » (Réglages > Confidentialité et sécurité > Analyse et améliorations) | https://www.apple.com/legal/privacy/data/fr/app-analytics/ ; https://support.apple.com/fr-fr/108971 (checked 2026-11-07) | The older iOS 8/9 label was "Partager avec les développeurs d'apps" too |
| Apple Push Notification service (APNs) | English only | https://support.apple.com/fr-fr/guide/security/aside/sec19eabb530/web | See Unverified. For user-visible notifications use "notifications" |
| Background App Refresh | « Actualisation en arrière-plan » (Réglages > Général > Actualisation en arrière-plan) | https://support.apple.com/fr-fr/118408 (checked 2026-11-07) | |
| Delete data from iCloud (storage path) | Réglages > votre nom > iCloud > Stockage (ou « Gérer le stockage du compte ») > « Supprimer les données d'iCloud » | https://support.apple.com/fr-fr/108922 (checked 2026-11-07) | |
| Manage / cancel subscriptions (path) | Réglages > votre nom > Abonnements > l'abonnement concerné > « Annuler l'abonnement » | https://support.apple.com/fr-fr/118428 ; https://support.apple.com/fr-fr/guide/iphone/iph4e3e7324f/ios | Trial note: "annulez-le au moins 24 heures avant la fin de la période d'essai" |
| Request a refund | reportaproblem.apple.com > « J'aimerais » > « Demander un remboursement » | https://support.apple.com/fr-fr/118223 | |

## Added during Tier 1 review (2026-11-08)

| English | French as Apple writes it | Source | Note |
|---|---|---|---|
| Sleep stages Awake / REM / Core / Deep | éveil / sommeil paradoxal / sommeil lent / sommeil profond | https://support.apple.com/fr-fr/guide/watch/apd830528336/watchos (checked 2026-11-08) | Observa's French UI says « Noyau » for Core (app string); site prose uses Apple's « sommeil lent » |
| Ask to Buy | « Demander l’autorisation d’achat » | https://support.apple.com/fr-fr/105055 (checked 2026-11-08 by the privacy reviewer) | Not « Autorisation d’achat » |
| App Privacy labels (product page) | « Données utilisées pour vous suivre », « Données établissant un lien avec vous », « Données n’établissant aucun lien avec vous »; purposes « Publicités tierces », « Publicités ou marketing du développeur », « Analyses », « Personnalisation du produit », « Fonctionnalité de l’app » | https://apps.apple.com/fr/app/id1550574178 and id526641427 (checked 2026-11-08 by the Tier 2 reviewer) | Never « liées / non liées à votre identité ». Editors' Choice: no French badge label verified; pages say « mis en avant par la rédaction de l’App Store » |
