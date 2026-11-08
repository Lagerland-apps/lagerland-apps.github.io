---
layout: journal
slug: what-an-iphone-app-can-actually-block
ref: /journal/what-an-iphone-app-can-actually-block/
permalink: /fr/journal/what-an-iphone-app-can-actually-block/
translated_from: 2026-10-29
last_updated: 2026-11-08
date: 2026-11-08
title: "Comment bloquer une app sur iPhone : ce qu’une app peut vraiment bloquer, et ce que le système lui interdit"
seo:
  title: "Comment bloquer une app sur iPhone : ce qui est possible"
  description: "Comment bloquer une app sur iPhone ? Les trois frameworks d’Apple, ce qu’un bloqueur peut bloquer et pourquoi aucun n’est impossible à contourner."
  keywords:
    - "comment bloquer une app sur iphone"
    - "bloquer une application iphone"
    - "bloquer une application iphone temporairement"
    - "contourner temps d’écran iphone"
    - "comment fonctionne un bloqueur d’applications"
    - "bloquer instagram sur iphone"
    - "temps d’écran ou bloqueur d’applications"
    - "family controls api"
lede: "Sur iPhone, aucune app tierce ne bloque quoi que ce soit par elle-même : elle demande à iOS de le faire, avec trois frameworks d’Apple aux limites nettes et publiées. Ces limites expliquent pourquoi votre bloqueur ne peut pas nommer les apps que vous avez bloquées, pourquoi les notifications arrivent quand même et pourquoi la réponse honnête à « peut-on le contourner ? » est toujours oui."
quick_answer: "Sur iPhone, une app tierce ne bloque rien elle-même : pour bloquer une app, elle demande à iOS de le faire, avec trois frameworks d’Apple. FamilyControls fournit l’autorisation et le sélecteur d’apps du système, ManagedSettings affiche l’écran de blocage sur les apps choisies et DeviceActivity gère les plannings et les seuils d’utilisation. Le sélecteur renvoie des jetons opaques : le bloqueur ne sait donc jamais quelles apps vous avez choisies. Il peut bloquer des apps, des catégories entières et des domaines web dans Safari. Il ne peut ni couper les notifications, ni agir sur vos autres appareils, ni résister au retrait de son autorisation dans Réglages. Tout bloqueur installé sur l’appareil n’est qu’une friction, et la seule mesure honnête est le temps qu’il faut pour en sortir."
excerpt: "Une app iPhone tierce ne peut ni voir ce que vous ouvrez, ni s’exécuter en continu en arrière-plan, ni s’afficher par-dessus une autre app. Cet article explique ce que l’API Screen Time permet, ce que la conception à jetons opaques implique pour la vie privée et pour le produit et toutes les façons de sortir d’un écran de blocage, classées selon l’effort."
faq:
  - q: "Une app peut-elle bloquer Instagram sur iPhone ?"
    a: "Oui. Avec le framework ManagedSettings d’Apple, une app tierce peut bloquer l’app Instagram : toucher son icône affiche un écran de blocage au lieu de la lancer. Elle peut aussi bloquer instagram.com dans Safari si vous incluez le contenu web dans la sélection. Elle ne peut pas empêcher les notifications d’Instagram d’arriver, ni bloquer Instagram sur votre iPad ou votre ordinateur portable, ni vous empêcher de retirer son autorisation dans Réglages, ce qui supprime tous les écrans de blocage d’un coup."
  - q: "Existe-t-il une app de blocage impossible à contourner ?"
    a: "Pas sur votre propre iPhone. Apple laisse volontairement la révocation à l’utilisateur : vous pouvez toujours retirer l’autorisation Family Controls dans Réglages, ce qui rend les jetons du bloqueur inutilisables et supprime tous les écrans de blocage. Un bloqueur peut empêcher sa propre suppression et ajouter une friction, comme un calcul ou un délai, mais il ne peut pas se rendre permanent. Le seul cas où la barrière tient est un appareil dont quelqu’un d’autre détient le code « Temps d’écran », et cela relève du contrôle parental, pas de l’autolimitation."
  - q: "Qu’est-ce que l’API Family Controls ?"
    a: "FamilyControls est le framework d’Apple qui conditionne l’accès à toute l’API Screen Time. Il fait deux choses : il demande l’autorisation à l’utilisateur, en mode individuel (autolimitation) ou en mode enfant (un parent du partage familial qui encadre un mineur), et il affiche FamilyActivityPicker, l’interface système où l’utilisateur choisit des apps, des catégories et des domaines web. Il renvoie une FamilyActivitySelection composée de jetons opaques. Pour le distribuer sur l’App Store, il faut une autorisation (entitlement) restreinte qu’Apple accorde sur demande."
  - q: "Un bloqueur d’applications fonctionne-t-il sans connexion internet ?"
    a: "Les bloqueurs Family Controls, oui. L’état des écrans de blocage est conservé en local dans un ManagedSettingsStore et appliqué par iOS lui-même : le mode avion ne change rien. Les filtres de contenu DNS ou VPN sont le cas inverse : ils ne voient que le trafic réseau, donc ils ne font rien contre une app qui fonctionne hors ligne ou contre un contenu déjà en cache sur l’appareil, et désactiver le profil dans Réglages les supprime purement et simplement. Le fonctionnement hors ligne est l’une des différences les plus nettes entre les deux approches."
  - q: "Un bloqueur d’applications peut-il voir quelles apps j’ai bloquées ?"
    a: "Non, et c’est iOS qui l’impose : ce n’est pas une simple promesse du développeur. Le sélecteur d’Apple renvoie des jetons, que la documentation d’Apple décrit comme des représentations qui ne révèlent pas l’identité d’une activité. Le bloqueur conserve un jeton, le renvoie à ManagedSettings pour appliquer un écran de blocage et ne reçoit jamais d’identifiant de bundle ni de nom affiché. Il ne peut ni consigner votre sélection, ni la vendre, ni la laisser fuiter, puisqu’il ne l’a jamais eue."
  - q: "Temps d’écran ou bloqueur d’applications tiers ?"
    a: "Temps d’écran, intégré à iOS, est gratuit, couvre tous les appareils connectés au même compte Apple quand « Partager entre les appareils » est activé et peut être verrouillé par un code que détient quelqu’un d’autre. Son point faible est la sortie : votre propre code, ou le bouton qui permet d’ignorer la limite. Un bloqueur tiers s’appuie sur la même mécanique d’application, mais peut changer ce que coûte le déverrouillage et afficher un écran de blocage bien plus utile. Beaucoup de personnes s’en sortent mieux en utilisant les deux."
mentioned_apps:
  - earnlock
read_time: "14 min de lecture"
---

Demandez à la plupart des gens comment fonctionne un bloqueur d’applications sur iPhone et vous obtiendrez une version de ceci : le bloqueur reste en arrière-plan, surveille ce que vous ouvrez et claque la porte dès qu’il repère Instagram.

Rien de tout cela n’est possible. Une app iOS tierce ne peut pas voir quelles apps vous lancez, ne peut pas s’exécuter en continu en arrière-plan pour en guetter une et ne peut pas dessiner un seul pixel par-dessus une autre app. Chaque bloqueur de l’App Store demande à iOS de faire le blocage à sa place, avec trois frameworks qu’Apple a lancés en 2021 et étendus petit à petit depuis.

Ce détail décide de ce que votre bloqueur peut faire, de ce qu’il ne fera jamais, quel que soit le prix payé, et de la façon exacte d’en sortir : c’est la partie que personne ne montre dans les captures d’écran de l’App Store.

## Qu’est-ce qui bloque vraiment une app sur un iPhone ?

Trois frameworks, qui forment ensemble l’API Screen Time, présentée lors d’une [session de la WWDC21, « Meet the Screen Time API »](https://developer.apple.com/videos/play/wwdc2021/10123/){: hreflang="en"} (en anglais). Un quatrième, ManagedSettingsUI, ne contrôle que l’aspect de l’écran de blocage.

| Framework | Sa seule fonction | Les types utilisés en pratique | Ce qu’il ne peut pas faire |
|---|---|---|---|
| [FamilyControls](https://developer.apple.com/documentation/familycontrols){: hreflang="en"} (documentation en anglais) | Obtenir l’autorisation et laisser l’utilisateur choisir des apps | `AuthorizationCenter`, [`FamilyActivityPicker`](https://developer.apple.com/documentation/familycontrols/familyactivitypicker){: hreflang="en"}, [`FamilyActivitySelection`](https://developer.apple.com/documentation/familycontrols/familyactivityselection){: hreflang="en"} | Indiquer à votre code quelles apps ont été choisies |
| [ManagedSettings](https://developer.apple.com/documentation/managedsettings){: hreflang="en"} | Appliquer la restriction | `ManagedSettingsStore`, [`ShieldSettings`](https://developer.apple.com/documentation/managedsettings/shieldsettings){: hreflang="en"} (`.applications`, `.applicationCategories`, `.webDomains`), [`ApplicationSettings`](https://developer.apple.com/documentation/managedsettings/applicationsettings){: hreflang="en"} (`denyAppRemoval`) | Survivre à l’autorisation qui l’a créée |
| [DeviceActivity](https://developer.apple.com/documentation/deviceactivity){: hreflang="en"} | Tout ce qui touche au temps | `DeviceActivityCenter`, `DeviceActivitySchedule`, [`DeviceActivityEvent`](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent){: hreflang="en"}, `DeviceActivityMonitor` | Exécuter votre code en continu : l’extension ne se réveille que sur des événements |
| [ManagedSettingsUI](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration){: hreflang="en"} | Définir l’aspect de l’écran de blocage | `ShieldConfigurationDataSource`, `ShieldActionDelegate` | Autre chose que dessiner un titre, un sous-titre, une icône et jusqu’à deux boutons |

Concrètement, la séquence est courte. On demande l’autorisation via `AuthorizationCenter.shared`, en mode `.individual` pour s’imposer des limites à soi-même ou en mode `.child` pour un parent du partage familial. On affiche le sélecteur. On place ce qu’il a renvoyé dans un `ManagedSettingsStore`, sous la forme `store.shield.applications`. On enregistre un planning avec `DeviceActivityCenter`, puis on laisse iOS réveiller l’extension `DeviceActivityMonitor` au début et à la fin des intervalles et aux seuils d’utilisation, pour qu’elle modifie le store.

Deux limites pratiques rendent la catégorie plus étroite qu’il n’y paraît. La capacité Family Controls ajoute l’autorisation (entitlement) [`com.apple.developer.family-controls`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls){: hreflang="en"}, et pour la distribuer sur l’App Store, il faut la demander à Apple. Et l’extension `DeviceActivityMonitor` n’est pas un démon : iOS la réveille, lui laisse un court créneau, puis la suspend. Tout ce qu’un bloqueur prétend faire « en continu » se produit aux moments choisis par Apple.

## Pourquoi le bloqueur ne sait jamais quelles apps vous avez choisies

De toutes les décisions de conception de l’API, c’est celle qui a le plus de conséquences.

L’interface de sélection d’apps est `FamilyActivityPicker`, et elle appartient à Apple, pas au développeur. Elle s’affiche hors du processus de l’app, liste vos apps installées et renvoie une `FamilyActivitySelection` qui contient des ensembles de jetons : `ApplicationToken`, `ActivityCategoryToken`, `WebDomainToken`. La documentation d’Apple sur [`Token`](https://developer.apple.com/documentation/managedsettings/token){: hreflang="en"} le décrit comme la représentation d’une app ou d’un site « qui ne révèle pas son identité », et la page d’`ApplicationToken` précise que l’objectif est de restreindre et de filtrer des apps sans accéder aux données personnelles de l’utilisateur.

Un bloqueur détient donc un bloc opaque, qu’il renvoie à ManagedSettings pour dresser un écran de blocage. Il ne reçoit jamais d’identifiant de bundle ni de nom affiché, et rien ne permet de remonter du jeton à l’app. Un jeton n’a en outre de sens que pour l’app qui l’a reçu, et il cesse de fonctionner dès que vous retirez l’autorisation dans Réglages, car la révocation invalide les jetons de l’app en même temps que sa permission.

Pour la vie privée, cela signifie qu’une app de temps d’écran ne peut physiquement pas consigner que vous avez bloqué Grindr, Robinhood ou l’app préférée de votre ex. Elle n’a pas promis de ne pas le faire : elle en est incapable. C’est une protection de la vie privée par construction, et la garantie de ce genre la plus forte de toutes les catégories où j’ai publié des apps.

Pour le produit, c’est une taxe bien réelle, que tous les développeurs de la catégorie paient :

- Impossible de proposer un parcours d’accueil « bloquez les suspects habituels » d’un seul toucher, puisque l’app ne peut pas nommer les suspects.
- Impossible de dire à l’utilisateur, dans ses propres textes, quelles apps sont actuellement bloquées.
- Impossible de vérifier à partir de ses propres données qu’un utilisateur a sélectionné quoi que ce soit, si bien que les demandes d’assistance (« ça ne bloque rien ») se transforment en séances guidées de captures d’écran.

C’est Apple qui a fait ce compromis, pas le développeur, et je pense qu’Apple a fait le bon choix.

## Quelle méthode bloque quoi ?

Cinq approches se vendent comme du « blocage d’apps », et elles interviennent à des niveaux complètement différents. Le prix compte moins ici que la place de chacune dans la pile logicielle.

| Approche | Ce qu’elle bloque | Ce qu’elle ne peut pas bloquer | Comment la contourner | Fonctionne hors ligne | À qui elle convient |
|---|---|---|---|---|---|
| **Temps d’écran, intégré à iOS** ([guide d’Apple](https://support.apple.com/fr-fr/guide/iphone/iphbfa595995/ios)) | Les limites de temps par app et par catégorie (« Temps accordés » sur iOS 27, « Limites d’app » sur iOS 18 et versions antérieures), les plages sans écran (« Programme de temps d’écran » sur iOS 27, « Temps d’arrêt » sur iOS 18 et versions antérieures), les classifications de contenu, le contenu web ; se synchronise entre vos appareils avec « Partager entre les appareils » | Rien au-delà des catégories d’Apple ; aucune condition de déverrouillage personnalisée | Votre propre code, ou le bouton qui permet d’ignorer la limite | Oui | À toute personne qui ne l’a pas encore essayé : c’est gratuit, et cela couvre aussi le Mac et l’iPad |
| **App à écran de blocage Family Controls** ([Opal](/fr/alternatives/opal/), [one sec](/fr/alternatives/one-sec/), [ScreenZen](/fr/alternatives/screenzen/), [Jomo](/fr/alternatives/jomo/), [EarnLock](/fr/apps/earnlock/)) | Toute app ou catégorie Apple que vous sélectionnez sur cet iPhone, plus les domaines web dans Safari pour les apps qui le gèrent | Les notifications, les autres appareils et tout ce qui suit le retrait de l’autorisation | La sortie de secours que l’app propose, puis le retrait de l’autorisation dans Réglages | Oui, car l’état est local et appliqué par iOS | Aux personnes qui veulent une condition de déverrouillage autre que « attendre » ou « saisir votre code » |
| **Filtre de contenu DNS ou VPN** ([NetworkExtension](https://developer.apple.com/documentation/networkextension){: hreflang="en"}) | Les domaines et les types de trafic, sur tout le système, y compris les apps que vous n’avez pas sélectionnées | Tout ce qui passe par le réseau mobile quand le profil est désactivé, le DNS chiffré à l’intérieur d’une app, ou un service qui partage un CDN avec quelque chose dont vous avez besoin | Désactiver le VPN dans Réglages, environ trois touchers | Non, c’est par définition un mécanisme réseau | Au blocage de classes entières de contenu (publicités, sites pour adultes), pas d’une app précise |
| **Appareil séparé ou boîtier verrouillé** (téléphone basique, coffre à minuterie, tag NFC de Brick) | Tout ce qui se trouve sur l’appareil que vous avez laissé | Tous les autres écrans autour de vous | Aller récupérer physiquement l’objet | Oui | Aux personnes dont le problème se limite à une heure, à un endroit précis : séances d’écriture, dîners, sommeil |
| **Nuances de gris et friction** (« Filtres de couleur », modes de concentration, apps retirées de l’écran d’accueil) | Rien : cela rend seulement le téléphone plus terne et plus long à atteindre | Tout, si vous le voulez vraiment | Trois touchers dans Réglages, ou Spotlight | Oui | À la dérive plus qu’à la compulsion : la personne qui ouvre une app sans raison et y reste 40 minutes |

Deux remarques sur ce tableau. Le filtre DNS est la seule ligne qui touche des apps que vous n’avez pas listées, ce qui en fait le bon outil pour bloquer les contenus pour adultes et le mauvais pour « m’éloigner de X entre 9 h et 17 h ». Et les règles de validation d’Apple encadrent la ligne VPN : la [règle 5.4 des App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/){: hreflang="en"} (en anglais) exige que les apps VPN utilisent `NEVPNManager` et viennent d’un développeur inscrit en tant qu’organisation, et l’autorisation de filtrage de contenu est accordée au cas par cas, ce qui explique le petit nombre de ces apps.

## Une app peut-elle bloquer Instagram sur iPhone ?

Oui, avec des réserves qui comptent plus que le oui.

**L’app, correctement.** Sélectionnez Instagram dans le sélecteur, placez le jeton dans `store.shield.applications`, et toucher l’icône affiche un écran de blocage au lieu de lancer l’app. L’app ne s’ouvre pas en arrière-plan, ne s’actualise pas et n’a pas droit à ses cinq secondes.

**Le site web, en grande partie.** `ShieldSettings.webDomains` couvre Safari. C’est la sélection du contenu web dans le sélecteur qui fait que instagram.com, dans Safari, se comporte comme l’app. La couverture dans les navigateurs tiers et les vues web intégrées aux apps est moins prévisible, et je ne bâtirais pas un plan là-dessus.

**Pas les notifications.** Un écran de blocage empêche un lancement, pas la réception d’une notification. Si ce sont un badge et une bannière qui vous attirent, l’écran de blocage règle la mauvaise moitié de la boucle : un mode de concentration est le meilleur outil, ou les deux ensemble.

**Pas vos autres écrans.** Le `ManagedSettingsStore` est propre à l’appareil. Votre iPad, votre Mac et l’ordinateur du travail ne sont pas touchés. Family Controls n’existe pas sur macOS sous une forme qui permette ce mécanisme, donc toute app de blocage qui couvre aussi le Mac y utilise un autre mécanisme.

## Existe-t-il une app de blocage impossible à contourner ?

Non, pas sur un appareil que vous possédez et contrôlez, et c’est voulu. Si une app tierce pouvait restreindre définitivement votre téléphone, la première app malveillante venue rendrait inutilisables un grand nombre de téléphones, alors Apple garde la sortie entre vos mains.

Il y a toujours une façon d’en sortir. La question utile est de savoir combien de temps cela prend, et si l’effort sert à quelque chose. Voici l’échelle, de la sortie la moins coûteuse à la plus coûteuse.

| Sortie | Durée approximative | Ce que cela vous coûte | L’app peut-elle le savoir ? |
|---|---|---|---|
| Bouton pour passer outre ou « J’en ai vraiment besoin », si l’app en propose un | 1 ou 2 touchers, moins de 5 secondes | Rien | Oui, elle a déclenché l’action |
| Attendre la fin d’une minuterie ou d’une pause de respiration | De 5 à 60 secondes | De l’attention, la monnaie que vous défendiez | Oui |
| Franchir une épreuve : un calcul, une longue phrase à saisir | De 20 à 60 secondes | De la concentration, et c’est le but | Oui |
| Supprimer le bloqueur | Environ 10 secondes, sauf si `denyAppRemoval` est activé | Vos réglages, votre historique, votre série | Non, il a disparu |
| Retirer l’autorisation Family Controls dans Réglages | Environ 15 secondes si vous connaissez le chemin | Tous les écrans de blocage tombent d’un coup ; les jetons deviennent inutilisables | Oui, [`authorizationStatus`](https://developer.apple.com/documentation/familycontrols/authorizationcenter/authorizationstatus){: hreflang="en"} est observable |
| Désactiver entièrement Temps d’écran | Environ 20 secondes | Vos limites et votre historique d’utilisation | Oui |
| Effacer puis restaurer l’appareil | 30 minutes ou plus | Tout | Non |
| Quelqu’un d’autre détient le code « Temps d’écran » | Hors de votre portée | L’autonomie, un coût réel qui vaut parfois d’être payé | Sans objet |

Deux lignes demandent un commentaire. `ApplicationSettings.denyAppRemoval` existe bel et bien : un bloqueur peut empêcher la suppression d’apps sur tout l’appareil, ce qui ferme la sortie la moins coûteuse. Et la révocation s’observe, si bien qu’une app peut surveiller l’état de sa propre autorisation et savoir à l’instant même que vous avez retiré l’autorisation. Savoir si elle doit en faire autre chose que l’enregistrer pour vous est une question de conception dont la mauvaise réponse est évidente.

Parcourez cette échelle et « impossible à contourner » ne veut plus rien dire. Ce qui varie, c’est le nombre de secondes qui séparent l’impulsion de l’app, et ce que ces secondes vous rapportent.

## Ce que la réalité de l’API change pour la conception

J’ai écrit il y a quelque temps que [le coût du déverrouillage doit se payer en dehors de l’app](/journal/unlock-cost-outside-the-app/){: hreflang="en"} (en anglais) : un coût que vous fixez vous-même, dans le logiciel, est un coût que votre envie peut renégocier en plein milieu de l’envie. Les faits techniques ci-dessus mènent au même argument à l’échelle de la plateforme. La révocation est toujours à une quinzaine de secondes, donc le mur n’est pas le produit. Le prix, si.

Et ce prix doit se payer là où vous en tirerez profit plus tard. Attendre échoue à ce test : vous payez en attention, justement ce que vous cherchiez à protéger, et vous n’obtenez rien en retour. Bouger le réussit, parce que le coût se retrouve dans le reste de votre vie.

Les autres conceptions n’ont pas tort pour autant. Plusieurs conviennent à des problèmes que la mienne ne résout pas :

[one sec](/fr/alternatives/one-sec/) vous interrompt avant l’ouverture de l’app, avec une respiration, une pause ou une question. Si votre pouce arrive avant votre intention, cela vous convient mieux qu’un verrou strict, parce que cela vise le réflexe. Un verrou que vous avez déjà franchi en le méritant ne fait rien contre un réflexe. one sec existe aussi sur Android, ce qu’aucune de nos apps ne propose.

[Brick](/alternatives/brick/){: hreflang="en"} (en anglais) place un tag NFC physique dans la boucle, pour environ 59 $ en une fois. Laisser le tag à la maison est un engagement que vous ne pouvez pas défaire depuis le canapé, et c’est la seule conception de la catégorie où la friction est faite d’atomes plutôt que d’un logiciel que vous avez autorisé. Le coût, c’est un objet à acheter, à transporter et à perdre. [Unpluq](/alternatives/unpluq/){: hreflang="en"} (en anglais) repose sur le même principe physique, associé à un abonnement.

[ScreenZen](/fr/alternatives/screenzen/) est gratuit, avec des pauses de plus en plus longues, et la gratuité est un avantage réel que l’offre à vie d’EarnLock à {P_LIFETIME@earnlock} n’efface pas. Les apps [Opal](/fr/alternatives/opal/) et [Jomo](/fr/alternatives/jomo/) sont plus abouties que la nôtre, et Jomo couvre l’iPhone, l’iPad et le Mac. Notre [guide pour limiter le temps d’écran sur iPhone](/fr/guides/limiter-temps-ecran-iphone/) compare ces apps une par une, avec Temps d’écran.

L’app [EarnLock](/fr/apps/earnlock/) utilise exactement les mêmes trois frameworks que toutes les autres et ne fait rien qu’Apple ne publie pas. Ce qu’elle change, c’est le prix : les apps que vous choisissez restent verrouillées jusqu’à ce que vous atteigniez un objectif d’activité quotidien lu dans Apple Santé (des pas dans la version gratuite, des minutes d’exercice ou des calories actives avec Premium). À la moitié de l’objectif, elles s’ouvrent pour une heure, et une fois l’objectif atteint, jusqu’à minuit. Son écran de blocage remplace l’écran de restriction générique d’Apple par le nombre de pas qui reste. « 2026 pas avant déverrouillage » vous dit où vous en êtes ; un écran qui annonce seulement que l’app est restreinte vous arrête, sans plus. Avec Premium, l’app Apple Watch lit ses propres données Santé et indique ce qui vous reste avant le déverrouillage, pendant que l’iPhone se charge du verrouillage. Quel objectif fixer est une autre question, traitée dans [ce que disent les études sur le nombre de pas](/fr/journal/how-many-steps-a-day-to-aim-for/). Verrouiller une app est gratuit ; Premium coûte {P_MONTHLY@earnlock}/mois, {P_YEARLY@earnlock}/an ou {P_LIFETIME@earnlock} en achat unique.

L’app a les mêmes contraintes que tout le reste de cette page. Elle ne peut pas non plus voir quelles apps vous avez bloquées. Elle n’arrête pas les notifications. C’est une app iPhone, avec une app Apple Watch dans Premium, sans version iPad ni Mac. Elle propose un déverrouillage d’urgence par jour, protégé par un calcul, et c’est voulu, parce que les gens suppriment un outil sans issue. Et si vous ouvrez Réglages et retirez son autorisation, tous les écrans de blocage tombent et elle n’y peut rien. Il en va de même pour chaque app Family Controls citée sur cette page, et mieux vaut le savoir avant de payer l’une de ces apps, la nôtre comprise. (Les règles sur les données qui sous-tendent cela, comme celles de toutes les autres apps Lagerland, sont décrites sur la [page de transparence](/fr/transparency/).)

## En bref

- **Aucune app iPhone tierce ne bloque quoi que ce soit elle-même.** Elle demande à iOS de le faire, via FamilyControls (la permission et le sélecteur), ManagedSettings (l’écran de blocage) et DeviceActivity (plannings et seuils).
- **Le sélecteur renvoie des jetons opaques, pas des noms d’apps.** Votre bloqueur ne peut ni consigner, ni vendre, ni laisser fuiter les apps que vous avez choisies, parce qu’iOS ne lui donne jamais les noms. La même règle l’empêche de vous proposer une liste préremplie d’apps à bloquer.
- **Un écran de blocage empêche le lancement, pas la notification.** Il couvre l’app et, via les domaines web, Safari. Il ne couvre ni votre iPad, ni votre Mac, ni la bannière qui a capté votre attention.
- **Rien n’est impossible à contourner, et Apple l’a voulu ainsi.** Retirer l’autorisation Family Controls dans Réglages prend environ quinze secondes et annule tous les écrans de blocage d’un coup. `denyAppRemoval` ferme la sortie la moins coûteuse ; rien ne ferme la dernière.
- **Comparez donc le prix, pas le mur.** Ce qui varie, c’est ce qui se dresse entre l’impulsion et l’app (un toucher, une attente, un tag physique ou un nombre de pas) et si ce prix, une fois payé, vous profite.
