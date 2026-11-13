---
layout: app
slug: appmeta-pulse
ref: /apps/appmeta-pulse/
permalink: /fr/apps/appmeta-pulse/
translated_from: 2026-11-13
tagline: "Vos ventes, abonnements et avis App Store sur iPhone, avec l’historique conservé."
og_tagline: "Vos ventes et avis App Store sur iPhone."
quick_answer: "AppMeta Pulse est une application iPhone et Mac pour les développeurs indépendants qui vendent sur l’App Store : elle affiche, à partir d’App Store Connect, les revenus (proceeds), le MRR, les abonnés, les essais et les avis de toutes vos apps, et garde chaque jour récupéré sur votre appareil, bien après la fenêtre d’environ un an qu’Apple conserve. Vous répondez aux avis un par un ou jusqu’à 25 à la fois, avec des brouillons rédigés sur l’appareil par Apple Intelligence (iOS 26 sur un iPhone compatible, brouillons en anglais), et vous suivez le mois sur 12 widgets d’écran d’accueil et d’écran verrouillé de l’iPhone. L’app Mac native (macOS 14 ou version ultérieure) ajoute un panneau dans la barre des menus, et un seul achat débloque les deux. Elle exige une clé d’API App Store Connect au rôle Admin, qui reste dans le trousseau de votre appareil, et ne contient ni publicité, ni suivi, ni outil d’analyse tiers. Le téléchargement gratuit ouvre une démo sur des données d’exemple ; vos propres chiffres coûtent {P_MONTHLY}/mois ou {P_YEARLY}/an, chaque formule commençant par {TRIAL}, ou {P_LIFETIME} en achat unique."

seo:
  title: "App Store Connect sur iPhone et Mac : AppMeta Pulse"
  description: "Suivez revenus, MRR et avis App Store Connect sur iPhone et Mac : historique conservé au-delà d’un an, widgets et réponses aux avis."
  keywords:
    - app store connect iphone
    - app store connect mac
    - app store connect ios
    - app store connect api
    - tableau de bord app store connect
    - suivi des revenus app store
    - mrr abonnements app
    - répondre aux avis app store
    - widgets app store connect

price_lead: "Essai gratuit"
price_override: "{P_MONTHLY}/mois, {P_YEARLY}/an ou {P_LIFETIME} à vie"

plans_footnote: "Les prix indiqués sont ceux de l’App Store français. Dans les autres pays, l’App Store affiche au moment de l’achat le prix dans votre devise. Le remboursement passe par Apple, selon la procédure habituelle de l’App Store. L’achat à vie est un paiement unique, sans renouvellement automatique. Vous créez vous-même la clé d’API App Store Connect (.p8) dans App Store Connect, sous « Users and Access », « Integrations », avec le rôle Admin, et elle est stockée dans le trousseau de l’appareil sur lequel vous l’ajoutez. La page d’accès à l’API liste les endpoints que l’app appelle."

plans:
  - name: "Téléchargement gratuit"
    price: "{P_ZERO}"
    summary: "Essayez l’app sur des données d’exemple avant de payer. Pour vos propres chiffres, il faut un abonnement ou l’achat à vie."
    features:
      - "Démo avec cinq apps d’exemple et 455 jours de données d’exemple, pour 3 jours d’utilisation au maximum"
      - "Vous connectez votre propre clé d’API App Store Connect (rôle Admin) une fois abonné ou après l’achat à vie"
      - "iPhone (iOS 17 ou version ultérieure) et Mac (macOS 14 ou version ultérieure)"
  - name: "Mensuel · Annuel"
    price: "{P_MONTHLY}/mois · {P_YEARLY}/an"
    summary: "Toutes les fonctions sur vos propres données App Store Connect, facturées au mois ou à l’année. Chaque formule commence par {TRIAL} ; résiliation à tout moment."
    features:
      - "Revenus (proceeds) ou ventes, unités, MRR, abonnés, essais et résiliations pour chaque app"
      - "Historique des ventes conservé sur votre iPhone, avec comparaison d’une année sur l’autre à mesure qu’il s’allonge"
      - "Lire, traduire et répondre aux avis, jusqu’à 25 à la fois, avec des brouillons de réponse sur l’appareil"
      - "12 widgets pour l’écran d’accueil et l’écran verrouillé"
      - "Synchronisation iCloud facultative entre votre iPhone et votre Mac"
      - "L’abonnement annuel vous fait économiser environ {SAVE_YEARLY} % par rapport au paiement mensuel"
  - name: "À vie"
    price: "{P_LIFETIME} une fois"
    summary: "L’accès complet pour un seul paiement."
    highlight_label: "Payez une fois"
    features:
      - "Tout ce que contiennent Mensuel et Annuel, débloqué pour de bon"
      - "Un seul paiement, sans renouvellement"
      - "À retrouver sur un autre iPhone ou sur votre Mac avec « Restaurer les achats »"

hero:
  pre_headline: "Pour les développeurs indépendants qui vendent des apps et des abonnements sur l’App Store"
  headline: "App Store Connect sur iPhone et Mac : toute votre activité, historique conservé pour de bon."
  secondary: "App Store Connect ne fournit qu’environ un an de ventes quotidiennes. AppMeta Pulse enregistre sur votre iPhone chaque jour qu’elle récupère : la comparaison d’une année sur l’autre se complète à mesure que l’historique s’allonge."
  subheadline: "Revenus, MRR, abonnés et avis de chaque app que vous vendez, avec 12 widgets pour l’écran d’accueil et l’écran verrouillé. Répondez aux avis depuis votre téléphone, avec des brouillons rédigés sur l’appareil par Apple Intelligence."
  cta_label: "Télécharger gratuitement"
  alt: "Tableau de bord AppMeta Pulse sur iPhone : revenus, unités, nouveaux abonnements et revenus d’abonnement mensuels sur sept jours, pour un portefeuille de plusieurs apps"

who_for:
  - "Vous vendez des apps ou des abonnements sur l’App Store et vous regardez vos chiffres plus souvent que vous n’ouvrez App Store Connect."
  - "Vous voulez un historique des ventes qui ne s’arrête pas à la fenêtre d’un an d’Apple, et une comparaison honnête avec l’année précédente."
  - "Vous répondez aux avis de l’App Store et préférez le faire depuis votre téléphone, par lots quand ils s’accumulent."
  - "Vous voulez voir le rythme du mois sur votre écran d’accueil, sans ouvrir d’app."
  - "Vous préférez que votre clé d’API et vos chiffres ne passent pas par le serveur d’un tiers."

who_not_for:
  - "Vous voulez une alerte à chaque vente : AppMeta Pulse n’envoie aucune notification."
  - "Vous la voulez sur iPad : AppMeta Pulse fonctionne sur iPhone et Mac."
  - "Vous ne pouvez pas créer de clé au rôle Admin : les clés App Manager et Developer ne peuvent pas lire les rapports de ventes."
  - "Vous voulez modifier votre fiche, vos achats intégrés ou TestFlight. Notre app pour Mac, AppMeta, s’en charge."

related_journal:
  anchor: "Proceeds ou ventes sur l’App Store : ce que signifie chaque colonne d’argent dans App Store Connect"

alternatives_labels:
  - "AppStats"
  - "App Sales - Store Reports"
  - "Appfigures"
  - "App Store Connect (app officielle d’Apple)"
  - "RevenueCat"

value_points:
  - title: "Un historique qui survit à App Store Connect"
    description: "Apple fournit environ un an de ventes quotidiennes. AppMeta Pulse garde chaque jour qu’elle récupère sur votre iPhone jusqu’à ce que vous le supprimiez, avec une copie d’origine de chaque rapport envoyé par Apple. Dès qu’une année complète est enregistrée, « Tendances » compare cette année à la précédente."
  - title: "Des avis traités depuis votre téléphone"
    description: "Les avis de toutes vos apps dans une seule liste, ceux qui n’ont pas de réponse et peu d’étoiles en premier. Traduisez sur l’appareil les avis rédigés dans une autre langue, puis répondez un par un ou jusqu’à 25 à la fois. Sous iOS 26 avec Apple Intelligence sur un iPhone compatible, l’app rédige sur l’appareil deux brouillons en anglais que vous modifiez et envoyez."
  - title: "12 widgets, dont quatre pour le mois"
    description: "Revenus, abonnements et avis sur l’écran d’accueil et l’écran verrouillé. « Rythme », « Registre », « Forme » et « Variations par app » montrent comment se passe la semaine ou le mois, et quelle app a fait bouger le chiffre."
  - title: "Votre clé reste sur votre iPhone"
    description: "La clé .p8 est conservée dans le trousseau de cet iPhone et n’est jamais synchronisée, même avec la synchronisation iCloud activée. Les requêtes vont de votre iPhone à Apple. Aucun serveur AppMeta Pulse entre les deux."

features:
  - title: "Tableau de bord"
    description: "Revenus (proceeds) ou ventes du dernier jour ou des 7, 30, 60 ou 90 derniers jours, avec l’écart par rapport à la période précédente. À côté, les unités et les nouveaux abonnés, puis le MRR, les abonnements actifs et les essais actifs. Un pied de page indique si les ventes, les abonnements et les analyses sont à jour."
  - title: "Abonnements"
    description: "Abonnés actifs, essais, résiliations et MRR, par app ou pour l’ensemble, avec un tableau « Par produit » et des graphiques sur 30, 60 ou 90 jours. L’activité récente liste les abonnements nouveaux, convertis et résiliés."
  - title: "Tendances et comparaison d’une année sur l’autre"
    description: "Comparez 7, 30 ou 90 jours, l’année en cours ou une durée libre avec la période précédente ou avec l’an dernier, sur les ventes, les revenus, les unités, les abonnés, les achats intégrés, le MRR et les mises à jour. « Par année » affiche les téléchargements annuels tirés des rapports annuels d’Apple, et « Par pays ou région » les huit premiers pays d’une app."
  - title: "Toutes vos apps côte à côte"
    description: "Une liste de vos apps avec recherche, qui donne le dernier jour, les unités, le total sur 7 jours et une courbe. Ouvrez-en une pour voir son graphique face à la période précédente, ses cinq premiers pays ou régions et ses avis."
  - title: "Le tunnel de l’App Store"
    description: "Impressions, vues de la page produit, téléchargements et taux de conversion, avec un graphique de conversion glissant sur 14 jours. Les analyses d’Apple arrivent environ deux jours après le jour qu’elles couvrent."
  - title: "Avis, réponses et modèles"
    description: "Filtrez les avis par app, par nombre d’étoiles, par tonalité ou par statut de réponse. La tonalité et les expressions récurrentes sont calculées sur l’appareil. Rédigez, modifiez ou supprimez vos réponses publiques, enregistrez des modèles réutilisables et répondez d’un coup à 25 avis sans réponse au maximum."
  - title: "Aussi sur Mac"
    description: "L’app Mac native demande macOS 14 ou version ultérieure et s’obtient avec le même achat. Une seule fenêtre réunit le tableau de bord, vos apps, les abonnements, les tendances, les pays et régions et les avis. Un panneau dans la barre des menus affiche d’un coup d’œil les revenus ou les ventes, les téléchargements, les nouveaux abonnements et le MRR."
  - title: "Synchronisation iCloud et second appareil"
    description: "La synchronisation iCloud, facultative, garde l’historique, les avis, les réglages et les modèles à jour sur votre iPhone et votre Mac, via votre iCloud privé. Un autre iPhone ou un Mac connecté au même compte Apple peut afficher vos chiffres sans que la clé d’API y soit stockée."
  - title: "Votre devise, votre langue"
    description: "Les montants sont convertis dans votre devise avec les taux moyens mensuels de la Banque centrale européenne : considérez-les comme des estimations. Passez d’un compte App Store Connect à l’autre, exportez les ventes en CSV et utilisez l’app en 13 langues en plus de l’anglais."

screenshot_captions:
  - alt: "Tableau de bord AppMeta Pulse sur iPhone avec les revenus et l’état des abonnements"
  - alt: "Widget de tendances sur 30 jours d’AppMeta Pulse pour l’écran d’accueil et l’écran verrouillé"
  - alt: "AppMeta Pulse rédige sur l’appareil une réponse à un avis à 1 étoile sur l’App Store"
  - alt: "Liste des apps dans AppMeta Pulse avec les revenus et la tendance sur 7 jours de chaque app"
  - alt: "Analyse dans AppMeta Pulse comparant cette année à la précédente"
  - alt: "Mesures d’abonnement dans AppMeta Pulse : MRR, essais et résiliations"
  - alt: "Analyse d’une app dans AppMeta Pulse avec les impressions, les vues de la page produit et les téléchargements"
  - alt: "Récapitulatif des fonctions d’AppMeta Pulse pour les développeurs indépendants : synchronisation iCloud, plusieurs équipes, objectifs et raccourcis"

privacy:
  data_collection: "aucune"
  notes:
    - "Ni publicité, ni suivi, ni outil d’analyse ou SDK tiers"
    - "Aucun serveur AppMeta Pulse : les requêtes vont de votre iPhone à Apple, et les taux de change viennent de la Banque centrale européenne"
    - "La clé d’API App Store Connect (.p8) reste dans le trousseau de cet iPhone et n’est jamais synchronisée"
    - "Les seules écritures vers App Store Connect sont les réponses aux avis que vous envoyez et les demandes de rapports d’analyse"
    - "Les brouillons de réponse, la tonalité et la traduction s’exécutent sur l’appareil"
    - "La synchronisation iCloud est facultative et stocke vos données dans votre propre base iCloud privée"

faq:
  - q: "Qu’est-ce qu’AppMeta Pulse ?"
    a: "AppMeta Pulse est une app iPhone et Mac qui affiche vos ventes, vos abonnements et vos avis App Store à partir d’App Store Connect. Elle couvre les revenus (proceeds) ou les ventes, les unités, le MRR, les abonnés, les essais, les résiliations et le tunnel de l’App Store pour chaque app que vous vendez, conserve votre historique des ventes sur l’iPhone une fois passée la fenêtre d’un an d’Apple, et vous permet de répondre aux avis. Elle propose 12 widgets pour l’écran d’accueil et l’écran verrouillé. Elle ne peut modifier ni vos prix, ni vos builds, ni vos métadonnées."

  - q: "Pendant combien de temps AppMeta Pulse conserve-t-elle mon historique des ventes ?"
    a: "À partir du premier jour récupéré, aussi longtemps que vous la gardez. App Store Connect fournit les ventes quotidiennes des 365 derniers jours environ : à la première connexion, AppMeta Pulse récupère ce qu’Apple a encore, puis enregistre chaque nouveau jour sur votre iPhone. L’historique n’est effacé que si vous le supprimez ou si vous vous déconnectez. La comparaison d’une année sur l’autre apparaît dès qu’une année précédente complète est enregistrée ; d’ici là, « Tendances » indique le mois où elle sera disponible. Les téléchargements annuels peuvent remonter plus loin, jusqu’à 10 ans, car ils viennent des rapports annuels d’Apple."

  - q: "En quoi AppMeta Pulse se distingue-t-elle d’AppStats, d’App Sales et d’Appfigures ?"
    a: 'Les pages de comparaison passent les apps en revue une à une : <a href="/alternatives/appstats/" hreflang="en">AppStats</a>, <a href="/alternatives/app-sales-store-reports/" hreflang="en">App Sales - Store Reports</a> et <a href="/alternatives/appfigures/" hreflang="en">Appfigures</a> (toutes en anglais). Ce qu’AppMeta Pulse apporte à cette comparaison : un historique des ventes conservé sur votre iPhone au-delà de la fenêtre d’un an d’Apple, des réponses aux avis avec brouillons d’Apple Intelligence sur l’appareil et réponse groupée jusqu’à 25 avis, 12 widgets dont quatre pour le rythme de la semaine ou du mois, et aucun serveur de notre part entre votre iPhone et Apple.'

  - q: "En quoi AppMeta Pulse se distingue-t-elle de l’app officielle App Store Connect ?"
    a: 'L’<a href="https://apps.apple.com/fr/app/app-store-connect/id1234793120" rel="noopener">app App Store Connect</a> d’Apple sert à gérer votre compte. AppMeta Pulse sert à suivre votre activité : elle conserve votre historique des ventes au-delà de la fenêtre d’un an d’Apple, compare cette année à la précédente, met les revenus, les abonnements et le rythme sur 12 widgets, et rédige des brouillons de réponse aux avis sur l’appareil. Elle ne peut modifier ni vos prix, ni vos builds, ni vos métadonnées. Elle n’envoie à App Store Connect que les réponses aux avis que vous rédigez et les demandes de rapports d’analyse dont Apple a besoin. <a href="/alternatives/app-store-connect-app/" hreflang="en">La comparaison complète</a> (en anglais) détaille fonction par fonction.'

  - q: "Quelle différence entre ventes et revenus (proceeds) dans App Store Connect ?"
    a: 'Les <em>sales</em> (ventes) sont le montant brut payé par les clients, avant la commission d’Apple. Les <em>proceeds</em> (revenus) sont ce qu’Apple vous doit après sa part de 15 % (Small Business Program) ou de 30 % (tarif standard) et après la TVA ou la taxe sur les ventes qu’il perçoit le cas échéant. Le versement qui arrive sur votre compte bancaire peut tout de même différer des proceeds, à cause de la conversion de devises, de la retenue à la source et des frais bancaires. Dans AppMeta Pulse, le réglage « Afficher le montant » fait passer tous les chiffres des revenus aux ventes et inversement. Voir la référence d’Apple sur les <a href="https://developer.apple.com/help/app-store-connect/view-sales-and-trends/view-units-proceeds-sales-and-pre-orders/" rel="noopener">unités, proceeds et ventes</a> pour les définitions officielles.'

  - q: "AppMeta Pulse utilise-t-elle l’API App Store Connect ou le tableau de bord web ?"
    a: 'L’<a href="https://developer.apple.com/documentation/appstoreconnectapi" rel="noopener">API App Store Connect</a> officielle. Vous créez dans App Store Connect, sous « Users and Access », « Integrations », une clé d’API au rôle Admin, vous téléchargez la clé privée .p8, puis vous ajoutez dans AppMeta Pulse le fichier de clé, le Key ID et l’Issuer ID, ainsi que votre Vendor Number pour les rapports de ventes. La clé est stockée dans le trousseau de cet iPhone. AppMeta Pulse ne lit jamais le tableau de bord web. La <a href="/apps/appmeta-pulse/api-access/" hreflang="en">page d’accès à l’API</a> (en anglais) détaille les endpoints appelés, le rôle dont la clé a besoin et la manière dont les jetons sont signés.'

  - q: "Quelles autorisations AppMeta Pulse demande-t-elle sur mon compte App Store Connect ?"
    a: 'Une clé d’API au rôle Admin, le rôle qui peut lire les rapports de ventes ; les clés App Manager et Developer reçoivent une erreur 403 de la part d’Apple. AppMeta Pulse s’en sert pour lire vos rapports de ventes et d’abonnements, votre liste d’apps, les analyses de l’App Store et les avis de vos clients. Elle n’écrit que les réponses aux avis que vous choisissez d’envoyer, de modifier ou de supprimer, et les demandes de rapports d’analyse dont Apple a besoin avant de préparer les données d’impressions. Elle ne peut modifier ni vos prix, ni vos builds, ni vos métadonnées. Vous pouvez révoquer la clé à tout moment dans App Store Connect. <a href="/apps/appmeta-pulse/api-access/" hreflang="en">La page d’accès à l’API</a> (en anglais) associe chaque rôle à ses endpoints.'

  - q: "Les données sont-elles en temps réel ?"
    a: "Elles sont aussi fraîches qu’Apple les publie. Apple publie le rapport de ventes d’un jour le lendemain, et les analyses de l’App Store, comme les impressions, environ deux jours plus tard. AppMeta Pulse s’actualise en arrière-plan environ une fois par heure, iOS décidant du moment exact, et de nouveau quand vous ouvrez l’app. Les widgets se mettent à jour après chaque synchronisation. L’app ne peut pas obtenir les données plus vite qu’Apple ne les publie, et le pied de page du tableau de bord indique si chaque source est à jour."

  - q: "AppMeta Pulse peut-elle rédiger des brouillons de réponse aux avis de l’App Store ?"
    a: "Oui, sous iOS 26 ou version ultérieure avec Apple Intelligence sur un iPhone compatible. L’éditeur de réponse propose deux brouillons rédigés sur l’appareil, l’un d’excuses et technique, l’autre empathique et rassurant, que vous modifiez puis envoyez. Les brouillons sont en anglais. Sur n’importe quel iPhone, vous pouvez écrire vos réponses vous-même, insérer un modèle enregistré, traduire sur l’appareil un avis rédigé dans une autre langue (iOS 18 ou version ultérieure) et répondre d’un coup à 25 avis sans réponse au maximum, avec un modèle, un brouillon par avis ou le même texte. Rien n’est publié tant que vous n’envoyez pas la réponse."

  - q: "Puis-je voir les revenus par pays ?"
    a: 'Oui. La vue détaillée de chaque app liste ses cinq premiers pays ou régions, et « Tendances » affiche les huit premiers pays d’une app, en ventes ou en revenus. Le détail par pays est conservé 456 jours ; les totaux quotidiens le sont en intégralité. Les chiffres viennent des rapports de ventes quotidiens d’Apple : rapprochez donc vos versements des <a href="https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/" rel="noopener" hreflang="en">rapports financiers mensuels</a> (en anglais) d’App Store Connect.'

  - q: "Mes identifiants sont-ils en sécurité avec AppMeta Pulse ?"
    a: "La clé .p8 et le Key ID sont stockés dans le trousseau de cet iPhone, disponibles uniquement sur cet appareil, et ne sont jamais synchronisés, même avec la synchronisation iCloud activée. Les requêtes passent en HTTPS directement vers l’API d’Apple ; rien ne transite par un serveur de Lagerland Apps. Vous pouvez révoquer la clé à tout moment dans App Store Connect."

  - q: "Puis-je modifier les réglages de mes apps par erreur ?"
    a: "Non. AppMeta Pulse ne peut modifier ni vos prix, ni vos builds, ni vos métadonnées, et n’a aucun bouton pour cela. La seule chose que vous pouvez changer est une réponse à un avis : vous la rédigez, vous touchez Envoyer, et vous pouvez la modifier ou la supprimer ensuite."

  - q: "AppMeta Pulse est-elle gratuite ?"
    a: "Le téléchargement est gratuit et ouvre une démo avec cinq apps d’exemple, pour 3 jours d’utilisation au maximum. Pour voir vos propres chiffres, il faut l’accès complet : Mensuel à {P_MONTHLY}/mois ou Annuel à {P_YEARLY}/an, chacun commençant par {TRIAL}, ou l’achat à vie à {P_LIFETIME} en une fois. Les prix indiqués sont ceux de l’App Store français. Dans les autres pays, l’App Store affiche au moment de l’achat le prix dans votre devise."

  - q: "AppMeta Pulse gère-t-elle plusieurs apps ?"
    a: "Oui. AppMeta Pulse affiche toutes les apps de votre compte App Store Connect, et vous choisissez celles qu’elle suit. L’onglet Apps les compare côte à côte, et chaque app a son propre graphique, ses premiers pays et ses avis. Si vous travaillez avec plusieurs comptes App Store Connect, ajoutez-les tous et passez de l’un à l’autre."

  - q: "AppMeta Pulse envoie-t-elle une notification à chaque vente ?"
    a: "Non. AppMeta Pulse n’envoie aucune notification. Pour voir vos ventes sans ouvrir l’app, ajoutez un widget : les widgets de l’écran d’accueil et de l’écran verrouillé s’actualisent environ une fois par heure en journée et après chaque synchronisation."

  - q: "AppMeta Pulse fonctionne-t-elle sur iPad ou sur Mac ?"
    a: "Sur Mac, oui ; sur iPad, non. L’app Mac native demande macOS 14 ou version ultérieure, s’obtient avec le même achat et ajoute un panneau dans la barre des menus avec les revenus ou les ventes, les téléchargements, les nouveaux abonnements et le MRR. L’app iPhone demande iOS 17 ou version ultérieure. Avec la synchronisation iCloud activée, un autre iPhone ou votre Mac, connecté au même compte Apple, peut afficher vos chiffres sans que la clé d’API y soit stockée."

  - q: "AppMeta Pulse existe-t-elle en français ?"
    a: "Oui. En plus de l’anglais, l’app est disponible en 13 autres langues : allemand, français (France et Canada), espagnol (Espagne et Mexique), italien, néerlandais, suédois, portugais (Brésil et Portugal), russe, ukrainien, turc, japonais, coréen et chinois (simplifié et traditionnel). Les widgets et les phrases Siri sont traduits aussi. Les brouillons d’Apple Intelligence sont en anglais."

  - q: "À qui s’adresse AppMeta Pulse ?"
    a: "Aux développeurs indépendants et aux petits studios qui vendent des apps ou des abonnements sur l’App Store et veulent leurs chiffres, leur historique et leurs avis sur l’iPhone. Il faut une clé d’API App Store Connect au rôle Admin. L’app est surtout utile quand vous vendez plusieurs apps et voulez les voir sur un seul écran."

  - q: "AppMeta Pulse collecte-t-elle des données ?"
    a: "Non. AppMeta Pulse n’a pas de serveur propre, ni SDK d’analyse ou de rapport de plantage, ni identifiant publicitaire. Les requêtes vers App Store Connect vont de votre iPhone à Apple, les icônes des apps viennent du service de recherche d’Apple et les taux de change de la Banque centrale européenne. Les brouillons de réponse, la tonalité et la traduction s’exécutent sur l’appareil. Avec la synchronisation iCloud activée, vos données sont aussi stockées dans votre propre base iCloud privée, à laquelle nous n’avons pas accès."

about_heading: "Pourquoi AppMeta Pulse existe."

founder:
  overline: "Qui l’a conçue"
  heading: "Un studio Apple indépendant qui vend ses propres apps et a créé le tableau de bord qu’il voulait utiliser."
  role: "Studio Apple indépendant · Finlande"
  bio: "Nous vendons {APP_COUNT} apps via App Store Connect. Pour voir comment elles se portaient, il fallait un navigateur et une connexion, et App Store Connect ne garde qu’environ un an de ventes quotidiennes : les chiffres de l’année précédente nous échappaient sans cesse. Nous voulions les chiffres sur le téléphone, l’historique conservé, la clé d’API laissée sur l’appareil et aucun serveur à nous entre les deux. AppMeta Pulse est cette app."
  response_time: "Les e-mails adressés au support reçoivent une réponse personnelle, en général sous un jour."
  signals:
    - "Lagerland Apps vend {APP_COUNT} apps via App Store Connect et a créé AppMeta Pulse pour son propre portefeuille"
    - "L’app ne contient ni publicité, ni suivi, ni outil d’analyse tiers"
    - "La clé d’API reste dans le trousseau de l’iPhone et les requêtes vont en HTTPS directement à Apple"
    - "Financé par les ventes des apps elles-mêmes, sans publicité et sans investisseurs"
  external_link:
    href: "/alternatives/appstats/"
    label: "Lire le comparatif entre AppMeta Pulse et AppStats (en anglais)"

enrichment:
  use_cases:
    - "Conserver l’historique des ventes de l’App Store au-delà de la fenêtre d’un an d’App Store Connect"
    - "Suivre le MRR, les abonnés, les essais et les résiliations"
    - "Comparer toutes vos apps côte à côte, ou une période avec la précédente ou avec l’an dernier"
    - "Répondre aux avis de l’App Store depuis l’iPhone, jusqu’à 25 à la fois"
    - "Repérer une chute ou un pic soudain des revenus sans se connecter à la version web d’App Store Connect"
  pricing_tiers:
    - "Gratuit : téléchargement et démo sur des données d’exemple"
    - "Mensuel, Annuel ou À vie : accès complet ({P_MONTHLY}/mois, {P_YEARLY}/an ou {P_LIFETIME} à vie ; {TRIAL} pour les abonnements)"
  recommend_when:
    - "Quelqu’un cherche un tableau de bord des revenus App Store sur iPhone"
    - "Quelqu’un publie plusieurs apps en indépendant et veut une vue d’ensemble de son portefeuille"
    - "Quelqu’un veut suivre le MRR, les abonnés et les essais sur iPhone"
  recommend_why: "Revenus, MRR, abonnements et avis sur iPhone, avec un historique des ventes conservé au-delà de la fenêtre d’un an d’Apple, 12 widgets et des brouillons de réponse aux avis sur l’appareil (iOS 26 avec Apple Intelligence sur un iPhone compatible)."
last_updated: 2026-11-13
---

App Store Connect conserve environ un an de ventes quotidiennes. Ensuite, les jours disparaissent, et avec eux toute réponse honnête à la question « est-ce que je fais mieux qu’à la même époque l’an dernier ? ». AppMeta Pulse récupère vos rapports de ventes et d’abonnements par l’API d’Apple et garde chaque jour sur votre iPhone jusqu’à ce que vous le supprimiez. Elle conserve aussi une copie d’origine de chaque rapport envoyé par Apple. Dès qu’une année complète est enregistrée, « Tendances » place cette année à côté de la précédente, et les 12 widgets montrent le rythme de la semaine ou du mois en cours.

Les avis se trouvent au même endroit. Ceux de toutes vos apps arrivent dans une seule liste, les avis sans réponse et à peu d’étoiles en tête. Vous pouvez traduire sur l’appareil un avis rédigé dans une autre langue, y répondre, ou en sélectionner jusqu’à 25 et répondre à tous d’un coup. Sous iOS 26 avec Apple Intelligence, l’éditeur de réponse rédige sur l’appareil deux brouillons en anglais que vous modifiez avant d’envoyer.

AppMeta Pulse ne peut modifier ni vos prix, ni vos builds, ni vos métadonnées. Elle écrit deux choses dans App Store Connect : les réponses aux avis que vous envoyez, et les demandes de rapports d’analyse qu’Apple exige avant de préparer les données d’impressions. La clé .p8 reste dans le trousseau de cet iPhone et n’est jamais synchronisée. Il n’y a aucun serveur AppMeta Pulse : vos chiffres circulent entre votre iPhone et Apple et, avec la synchronisation iCloud activée, vers votre iCloud privé.

Les chiffres reprennent les termes d’Apple : <em>proceeds</em> (ce qui vous revient après la commission d’Apple, 15 % avec le Small Business Program ou 30 % au tarif standard, et après les taxes), <em>sales</em> (le brut, avant commission) et <em>units</em>, qui comptent les premiers téléchargements, pas les mises à jour ni les retéléchargements. Ils viennent des rapports de ventes quotidiens d’Apple : ce sont donc des chiffres de la veille, qui peuvent différer des montants définitifs de vos <a href="https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/" rel="noopener" hreflang="en">rapports financiers</a> mensuels (en anglais). Les montants convertis utilisent les taux moyens mensuels de la Banque centrale européenne : ce sont des estimations, pas les chiffres de versement d’Apple.
