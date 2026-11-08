---
layout: journal
slug: how-plan-mode-builds-a-checklist
ref: /journal/how-plan-mode-builds-a-checklist/
permalink: /fr/journal/how-plan-mode-builds-a-checklist/
translated_from: 2026-10-29
last_updated: 2026-11-08
date: 2026-11-08
title: "Application pour organiser un mariage ou un voyage : la checklist à rebours du mode planification de Soon."
seo:
  title: "Application organisation mariage : checklist à rebours"
  description: "Application organisation mariage ou voyage : le mode planification gratuit de Soon. suggère une checklist et des jalons comptés à rebours depuis la date."
  keywords:
    - "application organisation mariage"
    - "checklist mariage"
    - "rétroplanning mariage"
    - "checklist voyage"
    - "application checklist"
    - "compte à rebours avec checklist"
    - "application préparation mariage"
lede: "La plupart des applications de compte à rebours s’arrêtent au nombre de jours. Le mode planification de Soon. propose aussi une checklist et une chronologie de jalons pour le type d’événement choisi. Voici comment fonctionnent ces suggestions, pourquoi elles sont rédigées à l’avance plutôt que générées et ce que nous avons écarté volontairement."
quick_answer: "Pour organiser un mariage, un voyage ou un autre événement dans une application de compte à rebours, Soon. propose le mode planification, gratuit, qui donne à chaque compte à rebours une checklist et une chronologie de jalons. Quand vous ouvrez l’onglet Planifier d’un événement, Soon. suggère un plan de départ pour son type : voyage, mariage, anniversaire, examen, travail, fête, santé, bébé, concert ou sport. Vous cochez les tâches, ajoutez vos propres tâches et jalons, et « Revenir aux suggestions » rétablit le plan de départ. Avec Premium, un événement de type Bébé reçoit un plan guidé semaine par semaine et les éléments du plan peuvent envoyer des rappels. Les suggestions sont rédigées à l’avance et livrées avec l’app ; rien n’est généré par IA."
excerpt: "La plupart des applications de compte à rebours vous montrent des jours. Le mode planification de Soon. suggère ce qu’il faut en faire : une checklist et une chronologie de jalons pour le type d’événement, rédigées à l’avance et livrées avec l’app, sans IA. Une note sur la conception."
faq:
  - q: "Qu’est-ce que le mode planification dans Soon. ?"
    a: "Le mode planification donne à chaque événement de Soon. une checklist et une chronologie de jalons. Quand vous ouvrez l’onglet Planifier d’un événement, Soon. propose un plan de départ pour son type : voyage, mariage, anniversaire, examen, travail, fête, santé, bébé, concert ou sport. Vous cochez les tâches, ajoutez vos propres tâches et jalons, et « Revenir aux suggestions » rétablit le plan de départ. Le mode planification est gratuit."
  - q: "Pourquoi les jalons sont-ils comptés à rebours depuis la date ?"
    a: "Parce qu’un plan pour une date dépend du temps qu’il reste. Compter à rebours depuis le jour permet aux mêmes suggestions de convenir à un voyage dans sept mois comme à un voyage dans trois semaines, et cela correspond au reste de l’app, où les widgets et l’écran verrouillé affichent les jours restants. C’est aussi comme cela qu’on parle de la préparation : deux semaines avant le mariage, pas une date du calendrier."
  - q: "Le mode planification utilise-t-il l’IA pour générer la checklist ?"
    a: "Non. Les checklists et chronologies suggérées sont rédigées à l’avance et livrées avec l’app : chaque mariage part donc de la même liste, et aucun détail de l’événement ne quitte votre iPhone pour la construire. Il en va de même pour les notes quotidiennes de Soon., qui viennent de modèles, pas d’une IA."
  - q: "Puis-je modifier la checklist du mode planification ?"
    a: "Oui. Le plan suggéré est un point de départ. Cochez les tâches au fur et à mesure et ajoutez vos propres tâches et jalons. Si vous voulez retrouver le plan de départ, « Revenir aux suggestions » le rétablit."
  - q: "Le mode planification envoie-t-il des rappels ?"
    a: "Seulement avec Premium. Premium ajoute des rappels pour les éléments du plan, et des rappels pour l’événement lui-même 7 jours, 3 jours et 1 jour avant, ainsi que le jour même. La version gratuite affiche le plan et n’envoie aucune notification."
mentioned_apps:
  - soon
read_time: "6 min de lecture"
---

La plupart des applications de compte à rebours s’arrêtent aux jours, parce que les jours sont faciles à obtenir. On soustrait une date d’une autre et on obtient un nombre. On l’affiche en grand, on met une photo derrière, et on publie l’app.

Soon. fait cela aussi. Le mode planification est la couche qui vient après le nombre : une checklist de ce qu’il y a à faire d’ici la date, et une chronologie de jalons pour y arriver, adaptées au type d’événement. Il est gratuit.

Cet article est la note de conception de cette couche : ce qu’elle fait, ce qu’elle laisse de côté volontairement et pourquoi.

## Des suggestions rédigées à l’avance, pas générées

Quand vous ouvrez l’onglet Planifier d’un événement, Soon. propose un plan de départ pour son type. Il existe des suggestions pour les voyages, les mariages, les anniversaires, les examens, le travail, les fêtes, la santé, un bébé, les concerts et le sport. Les anniversaires de couple et les événements génériques peuvent aussi avoir un plan.

Les suggestions sont rédigées une seule fois, livrées dans l’app et identiques pour tout le monde. Ce choix est délibéré, et il mérite d’être défendu.

L’autre option, c’est la génération : à la création d’un événement, envoyer son type et sa date à un serveur (ou à un modèle sur l’appareil) et recevoir en retour une checklist personnalisée. Nous y avons réfléchi et nous l’avons écartée pour quatre raisons.

1. **La génération fait sortir des données de l’appareil.** Même avec un modèle local, la conception pousse à donner plus de contexte au modèle pour améliorer le résultat, et plus on collecte de contexte, plus la garantie de confidentialité s’affaiblit. Une liste livrée dans l’app n’a besoin de rien venant de vous pour s’afficher.

2. **Les checklists générées manquent de constance.** Une liste de mariage rédigée une fois est la même pour tout le monde, si bien que deux amis qui comparent leurs notes partent de la même base. Une liste générée peut inclure le dîner de répétition une fois et l’oublier la suivante, ou ajouter une tâche qui n’existe pas. Nous privilégions la stabilité.

3. **Rédiger les listes à la main prend du temps, et c’est utile.** Écrire une bonne liste de mariage oblige à décider si une tâche passe en septième position ou en première. Un modèle ne se pose pas la question, et c’est dans cette lenteur de l’écriture que l’ordre se fixe.

4. **Une liste écrite peut être vérifiée.** Ce que l’app suggère aujourd’hui pour un mariage est ce qu’elle suggérera demain : on peut donc la lire, la discuter et la corriger.

Chaque plan de départ est donc une liste écrite par une personne, la même pour tout le monde. Vos propres ajouts se placent par-dessus.

## Compté à rebours depuis la date

La deuxième décision de conception est que la chronologie se compte à rebours depuis le jour que vous attendez, et non en avançant depuis aujourd’hui.

Les mêmes suggestions conviennent ainsi à n’importe quelle date, une année comme une autre. Un voyage dans sept mois et un voyage dans trois semaines partent du même plan ; seule change la distance qui vous sépare du jour. C’est aussi comme cela qu’on pense la préparation. On dit à son photographe « deux semaines avant le mariage », pas une date du calendrier.

Le reste de l’app fonctionne déjà ainsi. Les widgets de l’écran d’accueil, de l’écran verrouillé et du mode « En veille » affichent les jours restants : le temps avant le jour est l’unité naturelle de l’app, et le plan utilise la même.

L’exemple le plus parlant est celui d’un bébé. Avec Premium, un événement de type Bébé reçoit une chronologie guidée semaine par semaine : semaine 12, fin du premier trimestre ; semaine 20, l’échographie morphologique ; semaine 36, préparer la valise de maternité. Sa checklist comprend « Préparer la valise de maternité » et « Installer le siège auto ». La grossesse se compte en semaines parce que c’est ainsi qu’on en parle. C’est une aide à la planification, pas un avis médical, et les semaines sont génériques.

## Des rappels, si vous en voulez

La version gratuite de Soon. n’envoie aucune notification. Le plan reste attaché à l’événement, et le compte à rebours reste sur vos widgets.

Premium ajoute des rappels pour les éléments du plan, et des rappels pour l’événement lui-même 7 jours, 3 jours et 1 jour avant, ainsi que le jour même. Rien n’arrive chaque matin pour vous dire que le nombre a baissé d’une unité.

## Ce que le mode planification laisse de côté

Il ne réorganise pas votre plan. Ce que vous ajoutez reste là où vous l’avez mis, et Soon. ne remanie pas la liste dans votre dos. Si vous voulez retrouver le plan de départ, « Revenir aux suggestions » est là.

Il ne partage pas. Soon. synchronise vos événements via votre propre iCloud privé, vers vos propres appareils. Il n’existe pas de comptes à rebours partagés entre personnes : deux personnes qui préparent le même mariage l’ajoutent chacune dans sa propre copie de Soon.

Il n’optimise pas. Aucun algorithme ne regarde quelles tâches vous terminez pour repondérer les suggestions. Le plan de départ est celui que vous gardez, et toute personnalisation vient de vos propres ajouts.

Il ne vous suit pas. Soon. ne contient ni publicité, ni suivi, ni SDK tiers, et rien sur les tâches que vous cochez n’est envoyé nulle part. Nous ne savons pas ce que les utilisateurs cochent, ignorent ou ajoutent, et nous ne voulons pas le savoir.

Chacun de ces choix est volontaire.

## À quoi ressemblent les plans

[La page de l’app Soon.](/fr/apps/soon/#templates) montre à quoi ressemble un événement dans l’app, avec un voyage à une semaine et un plan de bébé semaine par semaine.

Les suggestions reflètent le jugement de leur auteur, sans données d’usage derrière. Un plan de mariage commence plus tôt qu’un plan d’anniversaire, parce que les préparatifs longs (le lieu, les save-the-date, les essayages) démarrent plus tôt. Si une suggestion ne convient pas à votre événement, ajoutez ce qui manque et cochez ce qui ne s’applique pas.

## Au-delà de Soon.

La plupart des apps qui tentent de planifier finissent soit (a) trop génériques pour servir, soit (b) si configurables qu’elles demandent un travail de réglage dont personne ne veut. Un plan de départ par type d’événement se place entre les deux : il arrive avec des réglages par défaut raisonnables, accepte vos propres ajouts et ne cherche rien à apprendre sur vous.

Pour une application de compte à rebours, l’ingénierie est légère. Une suggestion est une liste, et un jalon est un nombre de jours avant la date. Le plus difficile est de bien rédiger les listes, ce qui relève plus de l’écriture que de la technique.

Si vous intégrez des fonctions de planification dans une app spécialisée (sport, cuisine, études, projet), la même forme fonctionne : livrer des listes rédigées, les ancrer à un zéro qui compte (la date, l’échéance, le jalon), compter à rebours à partir de ce zéro et s’arrêter là. Laissez de côté la génération, le suivi et le réglage automatique, et livrez la liste.

---

[Soon. est disponible sur l’App Store](https://apps.apple.com/app/id6757280643) pour iPhone. L’app est gratuite jusqu’à 5 événements, mode planification compris, sans limite de durée. Premium ajoute les événements illimités, les rappels pour les événements et les éléments du plan, les prévisions météo, les notes quotidiennes, les événements récurrents et le mode Bébé. Plus de détails sur la [page de l’app Soon.](/fr/apps/soon/).
