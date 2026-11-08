---
layout: journal
slug: i-will-not-ask-for-your-bank-login
ref: /journal/i-will-not-ask-for-your-bank-login/
permalink: /fr/journal/i-will-not-ask-for-your-bank-login/
translated_from: 2026-11-07
last_updated: 2026-11-08
date: 2026-11-08
title: "Suivre ses factures sans connexion bancaire : je ne vous demanderai pas vos identifiants de banque"
seo:
  title: "Suivre ses factures sans connexion bancaire ni agrégateur"
  description: "Suivre ses factures sans connexion bancaire : AllPaid ne lit pas vos comptes. Ce que voit un agrégateur, son cadre en France et ce que vous y perdez."
  keywords:
    - "suivre ses factures sans connexion bancaire"
    - "application budget sans banque"
    - "application budget sans connexion bancaire"
    - "agrégateur bancaire c’est quoi"
    - "application gestion budget sans synchronisation"
    - "suivi des abonnements sans banque"
    - "rappel factures sans banque"
    - "allpaid"
lede: "Les applications reliées à la banque promettent la commodité. Le prix, c’est un accès en lecture à votre propre compte courant. AllPaid renonce volontairement à la connexion bancaire."
quick_answer: "Les applications de suivi de factures qui demandent vos identifiants bancaires les font passer par des agrégateurs comme Plaid, qui peuvent en général lire chaque opération du compte jusqu’à ce que vous révoquiez l’accès, bien plus que les prélèvements récurrents que l’on veut voir. En France, les agrégateurs de comptes ont un cadre juridique depuis la DSP2 et reçoivent un agrément de l’ACPR. AllPaid ne se connecte à aucune banque : vous ajoutez vos factures à la main, elles restent sur votre iPhone, et il n’y a aucun compte à créer."
excerpt: "La plupart des applications modernes de suivi de factures se connectent à votre banque par Plaid ou un agrégateur similaire. AllPaid est volontairement manuelle. Cet article donne les raisons structurelles contre la connexion bancaire, explique comment l’agrégation est encadrée en France, dit ce que l’on y perd et pourquoi la saisie à la main peut rester commode."
faq:
  - q: "Existe-t-il une application pour suivre ses factures sans connexion à la banque ?"
    a: "AllPaid est un suivi manuel de factures et d’abonnements pour iPhone, iPad et Mac, qui ne se connecte ni à une banque ni à un agrégateur comme Plaid. Vous saisissez chaque facture une fois et l’app la garde sur votre appareil. Il n’y a pas de compte : AllPaid ne vous demande donc jamais votre adresse e-mail. Rien ne quitte l’appareil, sauf si vous partagez une facture ou activez la synchronisation iCloud (Pro), qui passe par votre propre iCloud privé."
  - q: "Que voit Plaid quand une app de factures me demande de me connecter à ma banque ?"
    a: "Plaid conserve vos identifiants ou un jeton OAuth qui en découle, et obtient un accès en lecture persistant à chaque opération du compte, pas seulement aux prélèvements récurrents. Cet accès dure jusqu’à ce que vous le révoquiez. Les agrégateurs sont des entreprises réglementées, et les données alimentent aussi leurs produits plus larges, ce que les écrans d’accueil mentionnent rarement."
  - q: "Comment les agrégateurs de comptes sont-ils encadrés en France ?"
    a: "D’après l’ACPR, l’agrégation de comptes est un service en ligne qui fournit des informations consolidées sur un ou plusieurs comptes de paiement détenus auprès d’un ou plusieurs prestataires. Selon la Banque de France, les agrégateurs reçoivent un agrément de l’ACPR pour exercer, l’utilisateur doit renouveler régulièrement son authentification forte pour que l’agrégateur continue d’accéder à ses données, et il peut résilier le service à tout moment, après quoi le prestataire est tenu de ne plus y accéder."
  - q: "AllPaid retrouvera-t-elle les abonnements que j’ai oubliés ?"
    a: "Non. Dans ce seul cas, une app reliée à la banque a un avantage réel. Si votre besoin principal est de retrouver des prélèvements oubliés depuis des années, un outil fondé sur l’agrégation convient mieux. AllPaid s’adresse à ceux qui savent à peu près ce qu’ils paient et veulent des rappels sans confier l’historique de leurs opérations."
  - q: "Combien coûte AllPaid ?"
    a: "AllPaid est gratuite jusqu’à 3 factures, avec les rappels, les dates de fin de contrat, les dix widgets, Siri et le verrouillage de l’app. Pro ajoute les factures illimitées, plusieurs rappels par facture, l’analyse des dépenses, l’historique des paiements et la synchronisation iCloud, pour {P_MONTHLY@allpaid}/mois, {P_YEARLY@allpaid}/an ou {P_LIFETIME@allpaid} en achat unique. Il n’y a aucun compte à créer, et l’app n’embarque ni publicité, ni outil d’analyse, ni SDK tiers."
mentioned_apps:
  - allpaid
read_time: "8 min de lecture"
---

La plupart des applications modernes de suivi de factures se connectent à votre banque par l’intermédiaire de Plaid ou d’un agrégateur similaire, et s’ouvrent souvent sur la même consigne :

> *Pour commencer, connectez-vous à votre banque.*

[AllPaid](/fr/apps/allpaid/), l’app de suivi de factures et d’abonnements que Lagerland Apps publie, n’a pas ce parcours et n’en aura pas. Cet article explique pourquoi.

## Que se passe-t-il quand une app demande de vous connecter à votre banque ?

Quand une app qui n’est pas une banque vous demande de vous connecter à votre banque, ce qui se passe en dessous n’est pas tout à fait ce que la plupart des utilisateurs imaginent. Vous saisissez le mot de passe de votre banque sur un écran tiers. Dans le modèle américain, ce tiers est presque toujours **Plaid**, parfois MX ou Finicity. Il conserve vos identifiants ou, dans les montages plus récents, détient un jeton OAuth émis par votre banque. Dans les deux cas, il obtient un **accès en lecture** persistant à votre compte : opérations, soldes et souvent relevés historiques.

L’app que vous vouliez utiliser se connecte alors au *tiers*, pas à votre banque, et récupère un flux d’opérations filtré par les modèles de cet agrégateur.

C’est l’architecture habituelle de la fintech. Elle est réglementée et, la plupart du temps, elle fonctionne. Elle a aussi trois propriétés que les utilisateurs devraient connaître :

1. **Vos identifiants bancaires, ou un jeton qui en découle, se trouvent désormais à un endroit où ils n’étaient pas.** Cet endroit est une cible.
2. **L’agrégateur peut voir chaque opération de votre compte, à perpétuité, jusqu’à ce que vous révoquiez l’accès**, y compris quand l’app que vous avez choisie n’a pas besoin de ces données.
3. **Les agrégateurs sont des entreprises commerciales.** Leur croissance dépend de la vente croisée des données qu’ils agrègent à d’autres applications, anonymisées ou non. L’anonymisation a parfois une portée réelle, parfois non.

Je ne pense pas que les agrégateurs soient malveillants. Je pense en revanche que ce compromis de commodité n’entre pas dans l’idée que l’utilisateur s’en fait quand il touche *Continuer* sur l’écran d’accueil.

## Agrégateur de comptes : le cadre français

En France, le même principe porte un autre nom et dépend d’un autre cadre, que décrivent deux sources officielles.

Selon l’ACPR, le service d’information sur les comptes, ou agrégation de comptes, est « un service en ligne consistant à fournir des informations consolidées concernant un ou plusieurs comptes de paiement détenus par l’utilisateur auprès d’un ou plusieurs prestataires ». Les prestataires qui fournissent habituellement ce seul service sont les « prestataires de service d’information sur les comptes » (« PSIC » ou « agrégateur de comptes ») : avant de fournir le service, ils « doivent adresser à l’ACPR une demande d’enregistrement ». L’ACPR détaille ces statuts [sur une page destinée aux professionnels](https://acpr.banque-france.fr/fr/professionnels/lacpr-vous-accompagne/parcours-fintech/contenus-pedagogiques/de-quel-statut-releve-mon-activite/jaccede-aux-api-des-banques-jinitie-des-ordres-pour-le-compte-de-mes-clients).

La [FAQ de la Banque de France](https://www.banque-france.fr/fr/faq/recherche?mot-cle=agr%C3%A9gateur) précise que les agrégateurs « bénéficient d’un cadre juridique depuis la deuxième directive sur les services de paiement » (la DSP2) et qu’ils « reçoivent notamment un agrément de l’Autorité de contrôle prudentiel et de résolution (ACPR) pour pouvoir exercer leurs activités ». Elle ajoute que l’ACPR « ne délivre des agréments que lorsque les agrégateurs apportent toutes les garanties de sécurité ».

Sur ce que vous pouvez faire vous-même, la même FAQ dit trois choses :

- La DSP2 et le règlement délégué relatif à l’authentification forte prévoient que l’utilisateur doit procéder régulièrement à une authentification forte pour que l’agrégateur puisse accéder à ses données de comptes de paiement. Sans ce renouvellement, le prestataire ne peut plus accéder à ces données.
- À tout moment, vous pouvez résilier le service auprès du prestataire, qui est alors « tenu par la réglementation de ne plus accéder » à vos données de comptes.
- En cas de suspicion d’accès non autorisé, vous pouvez demander à votre banque de révoquer les droits du prestataire.

Ces règles encadrent l’accès : il se renouvelle et se retire. Elles ne changent pas le choix de départ : une app reliée à votre banque place quand même un tiers entre votre banque et vous, alors qu’une app à saisie manuelle n’en a pas besoin. Les deux applications de budget françaises que nous comparons à AllPaid passent par ce circuit : d’après sa fiche dans l’App Store, Bankin’ accède aux comptes par Bridge (Perspecteev), agréée par l’ACPR, et Linxo présente sa technologie comme agréée par la Banque de France. Le détail se trouve dans notre [comparaison entre AllPaid et Bankin’](/fr/alternatives/alternative-bankin/) et dans le [guide pour suivre ses factures sans connexion bancaire](/fr/guides/bill-tracker-without-bank-connection/).

## Ce que vous achetez vraiment

La promesse des apps de factures reliées à la banque, c’est qu’elles vont *trouver* vos abonnements et vos factures automatiquement. Vous vous inscrivez, vous donnez l’accès en lecture, et une liste de prélèvements récurrents apparaît.

Cela fonctionne, et c’est réellement utile. Mais l’app fait deux choses à la fois, et une seule est celle que l’utilisateur a demandée.

La première est d’identifier les prélèvements récurrents, ce qui est la partie utile.

La seconde est de dresser le portrait de *tout le reste* de ce que vous dépensez, ce que vous n’avez jamais demandé et qui est l’actif que l’entreprise construit en réalité. Le suivi des factures sert de prétexte au flux de données. Certaines de ces entreprises l’assument (pour celles dont le modèle économique est de « retrouver les abonnements oubliés et de proposer de les résilier », c’est l’échange de valeur). D’autres sont plus discrètes.

Dans tous les cas, l’utilisateur paie avec un accès en lecture à toute sa vie financière une fonction qui se résume à une liste qu’il aurait pu écrire lui-même en vingt minutes.

## La réponse de la saisie manuelle

[AllPaid](/fr/apps/allpaid/) part d’un autre principe : la plupart des gens ont entre cinq et quarante factures récurrentes, et les saisir une fois n’est pas un problème difficile.

L’app est d’abord manuelle. Vous saisissez vos factures, vos abonnements, le loyer, les charges et les contrats qui se reconduisent tous les ans ou tous les deux ans. L’app les garde sur votre iPhone, vous rappelle chaque échéance à 9 h, montre les factures du mois dans un résumé mensuel et dans le widget « Calendrier mensuel », et vous laisse marquer une facture comme payée directement depuis la notification. Elle vous prévient aussi avant la fin d’un contrat, et « Partager la facture » envoie à un conjoint ou à un colocataire un court message sur une facture à venir. Les widgets et Siri allègent le quotidien : demandez à Siri « What bills are due in AllPaid » et il lit les factures des sept prochains jours (les phrases pour Siri n’existent qu’en anglais). Le niveau Pro ajoute l’analyse des dépenses et l’historique complet des paiements, qui restent eux aussi sur l’appareil.

Ce que l’app ne fait pas, et ne fera pas :

- Elle ne se connecte pas à votre banque.
- Elle ne se connecte à aucun agrégateur tiers.
- Elle n’a pas de système de compte : elle ne demande donc ni identifiant ni adresse e-mail.
- Elle ne voit rien de ce que vous n’y saisissez pas.

Sur le papier, c’est moins pratique qu’une app reliée à Plaid. En pratique, l’écart est plus petit qu’on ne le croit. La première saisie prend environ quinze minutes si la liste est longue. Ensuite, le travail consiste à toucher une notification pour marquer une facture comme payée, ce qui demande le même effort qu’une app reliée à la banque, pour un coût moindre.

## Ce que cela fait perdre

Les apps de factures reliées à la banque repèrent une catégorie de facture qu’AllPaid manquera : **l’abonnement souscrit, oublié, et que l’on ne penserait pas à saisir dans une app manuelle**. Le classique service de streaming à 8,99 € par mois, utilisé deux fois. C’est un avantage réel, qu’AllPaid n’offre pas.

AllPaid n’est pas non plus une app de budget : d’après notre page de comparaison, elle n’a ni budgets par catégorie, ni suivi des revenus, ni soldes de comptes, et elle ne classe pas vos opérations. Si ce que vous cherchez est une application de budget qui se remplit toute seule, une app reliée à la banque convient mieux.

Si [retrouver ses prélèvements oubliés](/fr/journal/find-every-recurring-charge/) est votre besoin principal, une app reliée à la banque convient mieux, et je vous en recommanderais une. Sachez simplement ce que vous abandonnez en la connectant.

La saisie manuelle convient à tous les autres : ceux qui savent à peu près ce qu’ils paient, veulent un rappel pour le payer, veulent relancer un colocataire quand le loyer arrive à échéance, veulent voir d’un coup d’œil les factures du mois, et ne veulent pas qu’un tiers lise leur compte courant à perpétuité.

## Essayer sans rien connecter

[AllPaid](/fr/apps/allpaid/) se veut une réponse plus calme. Elle saute la connexion bancaire et l’inscription anxiogène, garde vos factures sur votre iPhone et fait le travail ingrat : vous éviter de manquer une facture ou de payer des frais de retard. Elle est gratuite jusqu’à 3 factures, avec Pro à {P_MONTHLY@allpaid}/mois, {P_YEARLY@allpaid}/an ou {P_LIFETIME@allpaid} en achat unique.

Si vous voulez cesser d’échanger un accès en lecture à votre banque contre des fonctions que vous pourriez noter vous-même, nous pensons que vous avez raison.
