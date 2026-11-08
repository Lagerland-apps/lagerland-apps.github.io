---
layout: journal
slug: supprimer-metadonnees-photo-iphone
permalink: /fr/journal/supprimer-metadonnees-photo-iphone/
local_only: true
last_updated: 2026-11-08
date: 2026-11-08
title: "Supprimer les métadonnées d’une photo sur iPhone : lieu, date, appareil et EXIF"
seo:
  title: "Supprimer métadonnées photo iPhone : lieu, EXIF, date"
  description: "Supprimer métadonnées photo iPhone : retirer le lieu avant un partage, effacer le lieu d’une photo, voir les infos et ce que MediaKit supprime en plus."
  keywords:
    - "supprimer métadonnées photo iphone"
    - "supprimer métadonnées photo"
    - "supprimer exif photo iphone"
    - "supprimer la localisation d’une photo iphone"
    - "voir les métadonnées d’une photo iphone"
    - "supprimer info photo iphone"
    - "supprimer exif photo"
    - "mediakit"
lede: "Une photo prise avec un iPhone peut emporter avec elle l’endroit où elle a été prise, la date, l’heure et l’appareil. Cette page indique comment voir ces informations dans l’app Photos, comment retirer le lieu d’une photo ou au moment du partage, comment empêcher l’iPhone de l’enregistrer, et ce que MediaKit ajoute pour les autres métadonnées."
quick_answer: "Sur iPhone, ouvrez la photo dans l’app Photos, touchez « Ajuster les infos », puis « Ajuster le lieu » et « Aucun lieu » : Apple décrit ces étapes pour supprimer les métadonnées de localisation d’une photo. Pour partager sans le lieu, touchez Options dans la feuille de partage et désactivez Localisation. Pour que l’iPhone n’enregistre plus le lieu, réglez l’app Appareil photo sur Jamais dans Réglages > Confidentialité et sécurité > Service de localisation. Ces gestes d’Apple concernent le lieu, pas toutes les métadonnées. Pour retirer en plus les informations d’appareil et d’auteur, l’outil « Supprimer les métadonnées » de MediaKit travaille sur l’appareil, sans envoi en ligne ; il demande Pro après les 3 premiers jours."
excerpt: "Supprimer les métadonnées d’une photo sur iPhone : voir les infos dans Photos, retirer le lieu d’une photo ou au partage, couper l’enregistrement du lieu dans Appareil photo, et utiliser MediaKit sur l’appareil plutôt qu’un site en ligne."
faq:
  - q: "Comment supprimer les métadonnées d’une photo sur iPhone ?"
    a: "Dans l’app Photos, les pages d’Apple décrivent le retrait du lieu : touchez Albums, ouvrez la photo, touchez « Ajuster les infos », « Ajuster le lieu », puis « Aucun lieu ». La date et l’heure s’ajustent au même endroit avec « Ajuster la date et l’heure ». Ces pages ne décrivent pas de retrait de l’ensemble des métadonnées. Pour les informations d’appareil et d’auteur, MediaKit propose l’outil « Supprimer les métadonnées »."
  - q: "Comment voir les métadonnées d’une photo sur iPhone ?"
    a: "Ouvrez la photo dans l’app Photos, puis balayez vers le haut ou touchez le bouton Infos. Selon la photo, Apple indique que vous voyez notamment l’appareil, la date et l’heure, les métadonnées de la caméra (objectif, vitesse de l’obturateur, taille du fichier) et le lieu de prise de vue."
  - q: "Comment supprimer la localisation d’une photo sur iPhone ?"
    a: "Pour une photo déjà prise : Photos > Albums > la photo > « Ajuster les infos » > « Ajuster le lieu » > « Aucun lieu ». Pour partager sans le lieu : touchez Options dans la feuille de partage et désactivez Localisation. Pour les prochaines photos : Réglages > Confidentialité et sécurité > Service de localisation > Appareil photo > Jamais."
  - q: "Peut-on supprimer les données EXIF d’une photo sans passer par un site en ligne ?"
    a: "Oui. Un site en ligne reçoit le fichier sur ses serveurs, alors que les gestes d’Apple et l’outil « Supprimer les métadonnées » de MediaKit se font sur l’appareil. Selon la fiche de MediaKit, l’outil retire les informations de lieu, d’appareil et d’auteur des photos, et rien n’est envoyé en ligne."
  - q: "L’outil « Supprimer les métadonnées » de MediaKit est-il gratuit ?"
    a: "Pendant les 3 premiers jours, tous les outils fonctionnent, avec un export par exécution. Ensuite, cinq outils restent gratuits, dont « Compresser » et « Redimensionner » pour les images, mais « Supprimer les métadonnées » demande Pro."
mentioned_apps:
  - mediakit
read_time: "5 min de lecture"
---

Pour retirer le lieu d’une photo sur iPhone, ouvrez-la dans l’app Photos, touchez « Ajuster les infos », puis « Ajuster le lieu » et « Aucun lieu ». C’est le chemin que décrit Apple, et il concerne le lieu. L’appareil, la date et l’heure sont d’autres métadonnées, et les pages d’Apple consultées pour cet article ne décrivent pas de geste pour tout retirer d’un coup. Cet article passe en revue ce que contient une photo, les gestes d’Apple pour le lieu, puis l’outil de MediaKit pour le reste.

## Que contiennent les métadonnées d’une photo ?

Une photo porte avec elle des informations en plus de l’image. La CNIL, dans ses [conseils sur les applications de retouche photo](https://www.cnil.fr/fr/applications-de-retouche-photo-les-conseils-de-la-cnil), rappelle que les photos partagées peuvent inclure des métadonnées : la géolocalisation, l’heure de la prise de vue ou des informations sur l’appareil, par exemple.

Apple détaille ce que montre l’app Photos dans son [guide de l’iPhone sur les informations des photos](https://support.apple.com/fr-fr/guide/iphone/iph0edb9c18f/ios) : l’appareil qui a pris la photo, la date et l’heure, les métadonnées de la caméra telles que l’objectif, la vitesse de l’obturateur et la taille du fichier, et le lieu où la photo a été prise.

Apple consacre au lieu une page de son guide de sécurité personnelle : quand « Service de localisation » est activé pour l’app Appareil photo, l’iPhone intègre à chaque photo et vidéo les coordonnées de l’endroit de la prise de vue, et les personnes avec qui vous partagez ces fichiers sont susceptibles d’accéder à ces métadonnées de localisation. La CNIL cite d’ailleurs, à propos des photos d’enfants publiées en ligne, une équipe qui a géolocalisé des dealers grâce aux coordonnées GPS et EXIF contenues dans leurs photos ([page de la CNIL](https://www.cnil.fr/fr/5-arguments-pour-rappeler-que-la-mise-en-ligne-dune-photo-de-votre-enfant-nest-pas-un-acte-anodin)).

## Comment voir les métadonnées d’une photo sur iPhone ?

D’après le guide d’Apple :

1. Ouvrez l’app Photos.
2. Touchez la photo ou la vidéo, puis balayez vers le haut ou touchez le bouton Infos.
3. Lisez les détails : appareil, date et heure, métadonnées de la caméra, lieu (un lien l’ouvre dans Plans).

Cet écran sert aussi de contrôle avant d’envoyer un fichier : c’est là que s’affiche le lieu.

## Comment supprimer la localisation d’une photo sur iPhone ?

Apple décrit trois gestes, sur la page [Gérer les métadonnées de positions dans Photos](https://support.apple.com/fr-fr/guide/personal-safety/ips0d7a5df82/web) :

| Situation | Chemin indiqué par Apple |
|---|---|
| Retirer le lieu d’une photo déjà prise | Photos > Albums > ouvrir la photo > bouton Infos > « Ajuster les infos » > « Ajuster le lieu » > « Aucun lieu » |
| Partager une photo sans son lieu | Dans Photos, sélectionner la photo, toucher le bouton Partager, puis Options, et désactiver Localisation. « Lieu non inclus » s’affiche au-dessus du bouton Options |
| Empêcher l’iPhone d’enregistrer le lieu | Réglages > Confidentialité et sécurité > Service de localisation > Appareil photo, puis Jamais |

Le premier geste concerne une photo déjà prise, le deuxième ce qui part au moment du partage, le troisième les photos à venir. Apple précise que les métadonnées de localisation ne peuvent être recueillies que si l’app Appareil photo a accès au service de localisation.

Sur Mac, Apple indique : dans l’app Photos, sélectionnez les photos, choisissez Image > Lieu, puis « Masquer l’emplacement » ou « Rétablir l’emplacement d’origine ».

Le guide de l’iPhone cité plus haut explique aussi comment corriger la date et l’heure : touchez « Ajuster les infos » puis « Ajuster la date et l’heure ». Pour revenir en arrière sur une date, une heure ou un lieu, Apple prévoit de toucher Rétablir à la dernière étape.

## Et les autres métadonnées : appareil, objectif, auteur ?

Les gestes d’Apple ci-dessus portent sur le lieu, la date et l’heure. Dans les pages consultées, aucun ne retire l’appareil ou les métadonnées de la caméra. Pour ces informations, MediaKit propose un outil dédié, décrit plus bas.

## En pratique, dans quel ordre faire ?

1. Ouvrez la photo dans Photos et regardez ses informations : lieu, date, appareil.
2. Si seul le lieu pose problème pour un envoi ponctuel, partagez la photo en désactivant Localisation dans Options.
3. Si vous voulez retirer le lieu de la photo elle-même, passez par « Ajuster le lieu » puis « Aucun lieu ».
4. Si les informations d’appareil ou d’auteur comptent aussi, passez la photo dans « Supprimer les métadonnées » de MediaKit avant de l’envoyer.
5. Pour les prochaines photos, réglez Appareil photo sur Jamais dans le service de localisation. Sachez qu’Apple se sert de ces coordonnées pour rechercher les photos par lieu dans Photos, et que la collection Plan n’inclut que les photos qui contiennent des informations géographiques.

## Faut-il utiliser un site en ligne pour supprimer l’EXIF ?

Un site de suppression de métadonnées reçoit la photo, donc le fichier même dont vous voulez protéger les informations. L’article [Convertir une photo HEIC en JPG sans l’envoyer au centre de données d’un inconnu](/fr/journal/your-photos-shouldnt-ride-the-elevator/) décrit ce que fait un convertisseur en ligne : le fichier quitte l’appareil, arrive sur le stockage de l’opérateur, y reste des heures ou des jours, et vous ne pouvez pas vérifier qu’il est supprimé. Le raisonnement vaut ici aussi : une photo dont on veut effacer le lieu est justement celle qu’on préfère ne pas laisser sur un serveur.

## Ce que MediaKit ajoute

[MediaKit](/fr/apps/mediakit/) est une app pour iPhone et Mac. Parmi ses outils pour l’image figure « Supprimer les métadonnées ». D’après la fiche de l’app, il retire les informations de lieu, d’appareil et d’auteur des photos (et des vidéos, des fichiers audio et des PDF) avant un partage. Tout fonctionne sur l’appareil : rien n’est envoyé en ligne, et il n’y a ni compte ni outil de suivi.

Sur iPhone, envoyez la photo depuis le menu Partager, lancez l’outil, puis enregistrez le résultat dans l’app Photos ou gardez-le dans l’onglet « Bibliothèque ». Vous pouvez ensuite ouvrir le résultat dans Photos et regarder ses informations, comme plus haut.

À savoir :

- Les 3 premiers jours, tous les outils fonctionnent, avec un export par exécution et sans paiement. Ensuite, cinq outils restent gratuits sans limite de durée, dont « Compresser » et « Redimensionner » pour les images. « Supprimer les métadonnées » n’en fait pas partie : il demande Pro.
- La fiche de l’app ne dit pas que « Compresser » ou « Redimensionner » retirent ces informations : pour cela, passez par « Supprimer les métadonnées ».
- Les réglages de MediaKit contiennent aussi un interrupteur « Conserver les métadonnées des fichiers » (« Conserver les métadonnées » sur iPhone). Pour une photo sensible, ne comptez pas sur lui : utilisez l’outil dédié et contrôlez le résultat dans Photos.
- Les formules Pro et leurs prix figurent sur la [page de MediaKit](/fr/apps/mediakit/).

Cet article décrit l’iPhone et le Mac, pas Android. Pour la publication de photos d’enfants, la CNIL détaille les risques sur [sa page](https://www.cnil.fr/fr/5-arguments-pour-rappeler-que-la-mise-en-ligne-dune-photo-de-votre-enfant-nest-pas-un-acte-anodin).
