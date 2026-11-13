---
layout: journal
slug: app-store-connect-mcp-server
ref: /journal/app-store-connect-mcp-server/
permalink: /fr/journal/app-store-connect-mcp-server/
translated_from: 2026-11-13
last_updated: 2026-11-13
date: 2026-11-13
title: "Un serveur MCP pour App Store Connect qui ne voit jamais votre clé d’API"
seo:
  title: "Serveur MCP App Store Connect : vos ventes dans Claude"
  description: "Interrogez Claude, Cursor ou une autre app d’IA sur vos ventes App Store. AppMeta Pulse pour Mac sert vos rapports via MCP sans voir votre clé d’API."
  keywords:
    - "app store connect mcp"
    - "serveur mcp app store connect"
    - "claude app store connect"
    - "assistant ia ventes app store"
    - "analyser ses ventes app store avec l’ia"
    - "mcp rapports app store connect"
    - "cursor mcp app store connect"
    - "appmeta pulse"
lede: "AppMeta Pulse fonctionne désormais sur Mac, et l’app Mac intègre un serveur MCP. Une fois la fonction activée, Claude, Cursor ou une autre app d’IA compatible MCP peut répondre à vos questions à partir de vos propres rapports App Store Connect. Le programme auxiliaire qui sert ces rapports n’a aucun accès au réseau et ne voit jamais votre clé d’API. Cet article explique son fonctionnement, ce que l’assistant peut lire ou non, et comment il se compare aux autres façons de relier App Store Connect à une app d’IA."
quick_answer: "Un serveur MCP pour App Store Connect permet à une app d’IA comme Claude ou Cursor de lire vos données App Store et de répondre à vos questions à leur sujet. AppMeta Pulse pour Mac (macOS 14 ou version ultérieure) en intègre un. Activez Réglages › Assistants IA : l’app conserve alors une copie SQLite en lecture seule des rapports qu’elle a téléchargés depuis App Store Connect, et un programme auxiliaire intégré la sert aux apps d’IA que vous connectez. Ce programme n’a aucun accès au réseau, ne peut rien modifier et ne voit jamais votre clé d’API. La fonction reste désactivée tant que vous ne l’activez pas et fait partie de l’accès complet d’AppMeta Pulse (un abonnement ou l’achat À vie)."
faq:
  - q: "Existe-t-il un serveur MCP pour App Store Connect ?"
    a: "Oui, plusieurs. Des serveurs open source comme l’App Store Connect MCP server de JoshuaRileyDev et asc-mcp tournent sur votre ordinateur et appellent l’API d’Apple avec votre clé. Appfigures propose un serveur MCP pour les données de votre compte Appfigures. AppMeta Pulse pour Mac en intègre un qui sert une copie en lecture seule des rapports que Pulse a téléchargés, par l’intermédiaire d’un programme auxiliaire en bac à sable, sans accès au réseau, qui ne voit jamais votre clé d’API."
  - q: "Claude peut-il lire mes ventes App Store Connect ?"
    a: "Oui, grâce à un serveur MCP. Avec AppMeta Pulse pour Mac, activez Réglages › Assistants IA, puis ajoutez le programme auxiliaire à Claude Desktop ou à Claude Code avec la configuration que la page de réglages copie pour vous. Claude peut alors interroger vos données de ventes, d’abonnements et d’avis, et vous répondre en langage courant."
  - q: "L’app d’IA obtient-elle ma clé d’API App Store Connect ?"
    a: "Non. La clé .p8 reste dans le trousseau d’AppMeta Pulse, et le programme auxiliaire qui sert vos rapports n’a pas accès au trousseau. La configuration de l’app d’IA contient uniquement le chemin du programme auxiliaire sur votre Mac, sans clé, sans jeton et sans numéro de fournisseur."
  - q: "L’assistant peut-il modifier mes apps, mes prix ou ma fiche ?"
    a: "Non. Le programme auxiliaire accepte une seule instruction SQLite en lecture seule par requête, travaille sur une copie de vos rapports et n’a aucun accès au réseau : il ne peut donc pas joindre App Store Connect."
  - q: "Mes données quittent-elles mon Mac ?"
    a: "AppMeta Pulse n’envoie rien à l’app d’IA ni à l’entreprise qui l’exploite. Ce que l’app d’IA lit par le programme auxiliaire pour vous répondre lui parvient, ainsi qu’à cette entreprise dans le cas d’un modèle dans le cloud, selon leurs conditions, comme tout ce que vous collez dans une conversation."
  - q: "Le serveur MCP fonctionne-t-il sur iPhone ?"
    a: "Non. Il fait partie d’AppMeta Pulse pour Mac. Le même achat couvre les apps iPhone et Mac, et l’app iPhone renvoie vers la fonction Mac dans sa rubrique Aide et FAQ."
mentioned_apps:
  - appmeta-pulse
read_time: "8 min de lecture"
excerpt: "AppMeta Pulse pour Mac intègre un serveur MCP pour Claude, Cursor et d’autres apps d’IA. Comment il sert une copie en lecture seule des rapports d’Apple par un programme auxiliaire en bac à sable, sans accès au réseau ni clé d’API, ce que l’assistant peut lire, et comment il se compare aux autres serveurs MCP pour App Store Connect."
---

Si vous vendez des apps sur l’App Store, vous avez sans doute déjà voulu poser une question simple sur vos chiffres et obtenir une réponse simple. Quels pays ont progressé ce trimestre ? Combien de remboursements le mois dernier ? Le changement de prix a-t-il fait baisser les essais ? App Store Connect a les données, mais elles sont réparties dans des fichiers de rapports qu’il faut télécharger, décompresser et croiser avant d’en tirer quoi que ce soit.

[AppMeta Pulse](/fr/apps/appmeta-pulse/) fonctionne désormais sur Mac, et l’app Mac intègre un serveur MCP : une app d’IA peut donc faire ce travail à votre place. L’assistant lit les mêmes fichiers de rapports que ceux que vous pourriez télécharger vous-même, et la partie de Pulse qui les sert ne peut atteindre ni Internet ni votre clé d’API.

## Qu’est-ce qu’un serveur MCP ?

MCP, le [Model Context Protocol](https://modelcontextprotocol.io/), est un standard ouvert publié par Anthropic en novembre 2024 pour relier des apps d’IA à des outils et à des données. Un serveur MCP propose quelques outils nommés. L’app d’IA décide quand les appeler et lit ce qu’ils renvoient. Claude Desktop, Claude Code, Cursor et VS Code prennent tous en charge les serveurs MCP.

Pour App Store Connect, cela veut dire que vous posez votre question en langage courant et que l’assistant va chercher lui-même les lignes dont il a besoin. Vous n’avez plus à exporter des rapports pour les coller dans une conversation.

## Comment fonctionne le serveur MCP d’AppMeta Pulse ?

1. Dans AppMeta Pulse pour Mac, ouvrez Réglages › Assistants IA et activez « Autoriser les assistants IA à lire vos rapports ». Avant que quoi que ce soit ne se passe, une alerte explique ce que cela autorise.
2. Le Mac crée une copie SQLite des rapports que Pulse a téléchargés : les lignes et les colonnes d’Apple telles qu’elles sont arrivées, sans conversion ni total. Pulse actualise la copie à l’arrivée de nouveaux rapports.
3. La copie se trouve dans un dossier que seuls l’app et son programme auxiliaire partagent. Ce programme est une petite app en bac à sable intégrée à AppMeta Pulse. Il peut lire ce dossier et rien d’autre : il n’a accès ni au réseau, ni au trousseau, ni aux données propres de l’app.
4. Vous ajoutez le programme auxiliaire à votre app d’IA. La page de réglages comporte des lignes qui copient la configuration pour vous : une commande pour Claude Code, une configuration JSON pour Claude Desktop, Cursor et VS Code, ou le chemin du programme auxiliaire.
5. L’app d’IA lance le programme auxiliaire sur votre Mac et communique avec lui par l’entrée et la sortie standard.

La configuration que votre app d’IA enregistre contient le chemin du programme auxiliaire, et rien d’autre. On n’y trouve ni clé d’API, ni jeton, ni numéro de fournisseur, car le programme auxiliaire n’en a jamais besoin.

Le programme auxiliaire propose quatre outils :

| Outil | Rôle |
|---|---|
| `describe_data` | Un guide de la copie : l’organisation des tables, les erreurs à éviter et les colonnes de chaque table sous les noms d’en-têtes d’Apple |
| `data_coverage` | Les rapports présents dans la copie et les dates qu’ils couvrent, pour que l’assistant distingue un jour manquant d’un jour sans ventes |
| `query` | Exécute une instruction SQLite en lecture seule, jusqu’à 5 000 lignes, 60 Ko et environ 10 secondes par appel |
| `list_accounts` | Les équipes App Store Connect dont les rapports sont partagés sur ce Mac |

## Que peut lire l’assistant ?

Par défaut, la copie contient :

- les rapports de ventes (quotidiens, hebdomadaires, mensuels et annuels) ;
- les rapports d’abonnements et les événements d’abonnement ;
- les avis des clients ;
- la liste de vos apps et de vos achats intégrés.

Activez « Collecter plus de rapports » (Réglages › Données) et Pulse conserve aussi les rapports financiers, les rapports Subscriber, de codes d’offre et de reconquête (win-back), les rapports d’analyse de l’App Store (téléchargements, engagement, sessions, installations et suppressions, notamment) et la configuration de vos apps sur l’App Store : prix, disponibilité, versions et textes de fiche. App Store Connect ne garde aucun historique de cette configuration, alors Pulse enregistre une nouvelle copie d’une page chaque fois qu’elle change.

L’assistant reçoit les rapports d’Apple tels qu’ils ont été livrés. Il ne reçoit rien de ce que Pulse calcule, comme le MRR, ni votre clé d’API ou vos réglages. Le guide de `describe_data` lui explique comment lire correctement les fichiers d’Apple : filtrer par fréquence de rapport pour ne pas compter une vente quatre fois, ne jamais additionner des devises différentes, traiter les remboursements comme des lignes aux unités négatives et indiquer de quelle table et de quelles dates vient chaque chiffre.

Tant que la fonction est activée, Pulse comble aussi les manques de la copie. Elle télécharge de nouveau chaque rapport quotidien de ventes, d’abonnements et d’événements d’abonnement qu’Apple fournit encore (environ la dernière année), ainsi que chaque rapport annuel des dix dernières années dont elle ne détient pas encore le fichier original d’Apple. Les réglages indiquent ce qui manque encore. Pulse garde chaque fichier une fois récupéré : à partir du jour où vous commencez, la copie continue de s’enrichir après qu’Apple a cessé de fournir les jours plus anciens.

## Que ne peut-il pas faire ?

- **Modifier quoi que ce soit.** L’outil de requête n’accepte qu’une instruction en lecture seule sur une copie. Le programme auxiliaire ne peut ni écrire dans cette copie ni joindre App Store Connect.
- **Voir votre clé d’API.** La clé .p8 reste dans le trousseau d’AppMeta Pulse, et le programme auxiliaire n’a pas accès au trousseau.
- **Fonctionner sans vous.** La fonction reste désactivée tant que vous ne l’activez pas. La désactiver, ou la fin de votre accès complet, supprime la copie. Cette copie n’est pas synchronisée avec iCloud et n’est pas incluse dans les sauvegardes.

AppMeta Pulse n’envoie rien à votre app d’IA ni à l’entreprise qui l’exploite. Les lignes que l’assistant lit pour vous répondre parviennent bien à cette app d’IA et, pour un modèle dans le cloud, à cette entreprise, selon leurs conditions. Un rapport que vous collez vous-même dans une conversation suit le même chemin.

## Comment se compare-t-il aux autres serveurs MCP pour App Store Connect ?

Pulse n’est pas la seule façon de relier App Store Connect à une app d’IA, et les autres solutions répondent à d’autres besoins :

- **Les serveurs open source**, comme [l’App Store Connect MCP server de JoshuaRileyDev](https://mcpservers.org/servers/JoshuaRileyDev/app-store-connect-mcp-server){: hreflang="en"} (en anglais) et [asc-mcp](https://pypi.org/project/asc-mcp/){: hreflang="en"} (en anglais), tournent sur votre ordinateur et appellent l’API d’Apple en direct avec votre clé. Certains vont bien au-delà des rapports et gèrent TestFlight ou les métadonnées de vos apps, et la clé qu’ils détiennent peut en faire autant.
- **[Appfigures](https://appfigures.com/products/cli-ai){: hreflang="en"}** (en anglais) propose un serveur MCP pour les données de votre compte Appfigures, avec en plus des données de marché comme les classements et la concurrence.
- **Les connecteurs hébergés**, comme [celui de Truto](https://truto.one/blog/connect-app-store-connect-to-claude-analyze-sales-user-reviews/){: hreflang="en"} (en anglais), vous fournissent un point d’accès MCP qui appelle App Store Connect depuis leurs serveurs.

Le serveur d’AppMeta Pulse en fait moins, à dessein. Il fonctionne en lecture seule, s’appuie sur les fichiers de rapports d’Apple et tourne sur votre Mac avec un programme auxiliaire qui ne peut pas joindre le réseau. Si vous voulez un assistant qui modifie aussi votre fiche ou publie vos builds, un serveur open source vous conviendra mieux.

## Des questions à poser

La copie contient les lignes brutes des rapports, et des questions comme celles-ci fonctionnent :

- Quels pays ont le plus progressé en revenus ce trimestre par rapport au même trimestre l’an dernier ?
- Quelle part des nouveaux abonnements du mois dernier a commencé par un essai gratuit, app par app ?
- Combien de remboursements chaque app a-t-elle eus ces 90 derniers jours ?
- De quoi se plaignent le plus les avis à 1 et 2 étoiles de ce mois-ci ?
- Que disait ma fiche en mars ? (Seulement si « Collecter plus de rapports » était déjà activé à ce moment-là.)

L’assistant fait les calculs. Demandez-lui de montrer la requête SQL qu’il a exécutée, ainsi que le rapport et les dates d’où vient chaque chiffre. Une comparaison d’une année sur l’autre ne fonctionne qu’une fois que la copie contient les deux années.

## De quoi avez-vous besoin ?

- Un Mac sous macOS 14 ou version ultérieure et AppMeta Pulse pour Mac. Un seul achat couvre les apps iPhone et Mac.
- L’accès complet : un abonnement ou l’achat À vie ({P_MONTHLY@appmeta-pulse}/mois, {P_YEARLY@appmeta-pulse}/an ou {P_LIFETIME@appmeta-pulse} en une fois).
- Des rapports sur le Mac, soit par sa propre clé d’API App Store Connect avec le rôle Admin, soit par la synchronisation iCloud depuis un appareil qui en a une.
- Une app d’IA compatible avec les serveurs MCP, comme Claude Desktop, Claude Code, Cursor ou VS Code.

Si vous utilisez déjà AppMeta Pulse sur iPhone, installez-la sur votre Mac, activez Assistants IA et collez la configuration dans votre app d’IA. La [page d’AppMeta Pulse](/fr/apps/appmeta-pulse/) présente tout ce que fait l’app, et [le guide du calcul du MRR des abonnements App Store](/journal/how-to-calculate-mrr-for-app-store-subscriptions/){: hreflang="en"} (en anglais) permet de vérifier n’importe quel chiffre de MRR qu’un assistant vous donne.
