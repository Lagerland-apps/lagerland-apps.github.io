---
layout: journal
slug: compress-a-video-for-email
ref: /journal/compress-a-video-for-email/
permalink: /fr/journal/compress-a-video-for-email/
translated_from: 2026-10-29
last_updated: 2026-11-08
date: 2026-11-08
title: "Comment compresser une vidéo pour l’envoyer par mail : limites de taille et calcul du débit"
seo:
  title: "Compresser une vidéo pour l’envoyer par mail : taille, débit"
  description: "Compresser une vidéo pour l’envoyer par mail : Gmail accepte 25 Mo, Outlook et iCloud Mail 20 Mo. La marge à garder, le débit à viser, sur iPhone ou Mac."
  keywords:
    - "compresser une vidéo pour l’envoyer par mail"
    - "vidéo trop lourde pour envoyer par mail"
    - "envoyer une grosse vidéo par mail"
    - "taille max pièce jointe gmail"
    - "compresser vidéo iphone pour mail"
    - "limite pièce jointe outlook"
    - "débit vidéo pour une taille de fichier"
    - "mail drop taille maximale"
lede: "Chaque messagerie plafonne la taille des pièces jointes, et une vidéo atteint vite ce plafond. Cet article donne les limites que publient Gmail, Outlook et iCloud Mail, explique pourquoi une limite de 25 Mo n’accepte pas un fichier de 25 Mo, détaille le calcul qui transforme une taille cible en débit, puis montre comment MediaKit fait ce calcul sur iPhone ou sur Mac sans envoyer la vidéo en ligne."
quick_answer: "Pour envoyer une vidéo par mail, compressez-la sous la limite de votre messagerie, avec de la marge. Un compte Gmail personnel accepte 25 Mo de pièces jointes, l’app Outlook 20 Mo par message pour les comptes internet comme Outlook.com, iCloud Mail 20 Mo, et les comptes professionnels Exchange 10 Mo par défaut. Les pièces jointes voyagent encodées en Base64, ce qui ajoute environ 33 % d’après Microsoft : visez donc les trois quarts de la limite, soit environ 18 Mo pour Gmail et 15 Mo pour Outlook ou iCloud Mail. Pour trouver le débit, multipliez la cible en mégaoctets par 8000, puis divisez par la durée de la vidéo en secondes : vous obtenez le débit total en kbit/s. Retranchez le débit audio (128 kbit/s est une valeur courante) : ce qui reste est le budget vidéo. Baissez la résolution jusqu’à ce que ce budget lui convienne, gardez le H.264 pour que la vidéo se lise partout, et envoyez un lien plutôt qu’un fichier quand le budget devient trop mince : Mail Drop transmet jusqu’à 5 Go."
excerpt: "Un guide pour envoyer une vidéo par mail : les limites de pièces jointes de Gmail, Outlook, Exchange, iCloud Mail et Mail Drop, pourquoi l’encodage Base64 impose de viser les trois quarts de la limite, un tableau de débits pour des vidéos de 30 secondes à 5 minutes, et la façon dont le mode « Taille cible » de MediaKit refait le même calcul sur iPhone et Mac."
faq:
  - q: "Quelle est la taille maximale d’une pièce jointe Gmail pour une vidéo ?"
    a: "Un compte Gmail personnel peut envoyer jusqu’à 25 Mo de pièces jointes dans un même message, toutes additionnées ; les comptes professionnels et scolaires suivent les limites que fixe leur administrateur Google Workspace. Au-delà, Gmail retire la pièce jointe et la remplace par un lien Google Drive. Comme les pièces jointes sont encodées en Base64 pendant le trajet, visez une vidéo d’environ 18 Mo si elle doit arriver en pièce jointe et non sous forme de lien."
  - q: "Pourquoi ma vidéo est-elle refusée alors qu’elle est sous la limite ?"
    a: "Il y a trois causes courantes. Les pièces jointes sont encodées en Base64 avant de voyager, ce qui ajoute environ 33 % au message d’après la documentation Exchange de Microsoft : un fichier proche de la limite peut donc la dépasser une fois encodé. Certaines limites comptent le message entier, pas seulement la pièce jointe ; Microsoft précise que la limite de 20 Mo d’Outlook inclut le texte du mail. Enfin, le serveur du destinataire a sa propre limite, parfois plus basse que la vôtre, comme les 10 Mo par défaut d’Exchange."
  - q: "Comment calculer le débit pour une taille de fichier donnée ?"
    a: "Multipliez la taille cible en mégaoctets par 8000 pour obtenir des kilobits, divisez par la durée de la vidéo en secondes pour obtenir le débit total en kbit/s, puis retranchez le débit audio. Ce qui reste est le débit vidéo. Pour une cible de 18 Mo et une vidéo de 90 secondes : 18 × 8000 = 144 000 kilobits ; divisés par 90, cela donne 1600 kbit/s ; une fois retranchés 128 kbit/s d’audio, il reste environ 1470 kbit/s pour l’image."
  - q: "H.264 ou HEVC pour une vidéo envoyée par mail ?"
    a: "H.264 dans un fichier MP4, sauf si vous savez que le destinataire utilise un appareil Apple récent. Selon Apple, le HEVC compresse mieux que le H.264 : à taille égale, un fichier HEVC est donc de meilleure qualité. Mais vous ne maîtrisez pas l’appareil sur lequel la pièce jointe sera ouverte, et le H.264 est le format que presque tous les appareils lisent. Si le destinataire a un iPhone, un iPad ou un Mac récent, le HEVC offre une meilleure qualité pour la même taille."
  - q: "Comment envoyer une grosse vidéo par mail quand la compression ne suffit pas ?"
    a: "Envoyez un lien. Mail Drop, dans l’app Mail et iCloud Mail, envoie des fichiers jusqu’à 5 Go sous forme de lien de téléchargement qui expire au bout de 30 jours, et Mail le propose quand un message est trop volumineux pour votre fournisseur. Gmail remplace de lui-même une pièce jointe trop lourde par un lien Google Drive. Une vidéo de 5 minutes compressée à 15 Mo laisse environ 270 kbit/s pour l’image, soit le quart de ce que YouTube conseille pour la mise en ligne, même en 360p."
  - q: "MediaKit peut-il compresser une vidéo à une taille précise ?"
    a: "Oui. L’outil « Compresser une vidéo » a un mode « Taille cible » qui accepte un nombre en Ko, en Mo ou en Go. MediaKit divise la cible par la durée de la vidéo, retranche le débit audio que vous avez choisi, garde 3 % de marge, encode, puis mesure le fichier écrit et réencode avec un débit corrigé s’il a manqué la cible. S’il n’arrive toujours pas à passer sous la cible, il s’arrête avec une erreur plutôt que de vous remettre un fichier trop gros. Il s’exécute sur l’appareil, sur iPhone et sur Mac, et « Compresser une vidéo » fait partie des cinq outils qui restent gratuits sans limite de durée après les 3 premiers jours."
mentioned_apps:
  - mediakit
read_time: "8 min de lecture"
---

À 8 Mbit/s, le débit que YouTube recommande pour mettre en ligne une vidéo en 1080p, une minute de vidéo pèse 60 Mo. C’est plus du double de ce que Gmail accepte en pièce jointe. Pour envoyer une vidéo par mail, il suffit de faire un petit calcul : choisir une cible sous la limite de votre messagerie, trouver le débit qui y correspond, puis réencoder la vidéo à ce débit. Cet article donne les chiffres de chaque étape, puis montre comment [MediaKit](/fr/apps/mediakit/) s’en charge sur iPhone et sur Mac sans envoyer la vidéo ailleurs au préalable.

## Quelle taille de vidéo peut-on envoyer par mail ?

| Service | Limite | Ce qui est compté | Au-delà de la limite |
|---|---|---|---|
| Gmail, compte personnel | 25 Mo | Toutes les pièces jointes du message, additionnées | Gmail remplace la pièce jointe par un lien Google Drive |
| App Outlook, comptes internet comme Outlook.com | 20 Mo | Les pièces jointes et le mail lui-même | Microsoft conseille de compresser le fichier ou de partager un lien vers un espace de stockage en ligne |
| Exchange, comptes professionnels | 10 Mo par défaut | Le message entier ; les administrateurs peuvent modifier la limite | Comme ci-dessus |
| iCloud Mail | 20 Mo | Les messages reçus et envoyés | Jusqu’à 5 Go avec Mail Drop activé |
| Mail Drop (app Mail, iCloud Mail) | 5 Go | Le message, pièces jointes comprises ; chaque lien expire au bout de 30 jours | Mail Drop ne peut pas l’envoyer |

Limites telles que la page d’aide de chaque fournisseur les indiquait en juillet 2026 : [aide Gmail](https://support.google.com/mail/answer/6584){: hreflang="en"} (en anglais), [assistance Microsoft](https://support.microsoft.com/en-us/office/send-large-files-with-outlook-8c698842-b462-4a4c-8d53-5c5dd04f77ef){: hreflang="en"} (en anglais), et les pages Apple sur les [limites d’iCloud Mail](https://support.apple.com/fr-fr/102198) et sur [Mail Drop](https://support.apple.com/fr-fr/108329). Les administrateurs peuvent fixer des limites plus basses pour les comptes professionnels et scolaires, et le serveur qui reçoit le message applique la sienne. La [documentation Exchange](https://learn.microsoft.com/en-us/exchange/mail-flow/message-size-limits){: hreflang="en"} (en anglais) de Microsoft indique qu’un message doit respecter les limites de l’expéditeur et du destinataire : la plus petite limite du trajet l’emporte.

## Pourquoi une limite de 25 Mo n’accepte pas un fichier de 25 Mo

Le mail est un format texte. Avant de voyager en pièce jointe, une vidéo est encodée en Base64 : chaque groupe de trois octets du fichier devient quatre caractères de texte, répartis en lignes de 76 caractères au plus ([RFC 2045, section 6.8](https://www.rfc-editor.org/rfc/rfc2045#section-6.8){: hreflang="en"} (en anglais)). Le message qui traverse le réseau est donc environ un tiers plus gros que le fichier sur votre disque.

Que la limite se mesure avant ou après cet encodage varie d’un service à l’autre, et les pages d’aide grand public le disent rarement. La documentation Exchange de Microsoft le précise : le Base64 ajoute environ 33 %, si bien qu’une limite de message de 64 Mo donne un maximum réaliste d’environ 48 Mo. Sa page sur Outlook ajoute que la limite de 20 Mo inclut le mail, pas seulement la pièce jointe.

En pratique, visez donc les trois quarts de la limite affichée :

| Limite affichée | Taille de fichier à viser |
|---|---|
| 25 Mo (Gmail) | 18 Mo |
| 20 Mo (Outlook, iCloud Mail) | 15 Mo |
| 10 Mo (Exchange par défaut) | 7,5 Mo |

Viser trop bas coûte un peu de qualité d’image. Viser trop haut, c’est un message refusé, ou un lien là où vous vouliez une pièce jointe.

## Comment calculer le débit qui correspond à la taille visée

La taille d’un fichier est son débit multiplié par sa durée. Il suffit de faire le calcul à l’envers :

1. **Convertissez la cible en kilobits.** Mégaoctets × 8000, en comptant un mégaoctet pour 1 000 000 d’octets.
2. **Divisez par la durée de la vidéo en secondes.** Vous obtenez le débit total en kbit/s.
3. **Retranchez l’audio.** 128 kbit/s est un réglage stéréo courant ; 64 kbit/s suffit largement pour la voix.
4. **Le reste est le débit vidéo.** Gardez quelques pour cent de marge pour le conteneur lui-même.

Pour une vidéo de 90 secondes destinée à Gmail : 18 Mo × 8000 = 144 000 kilobits. Divisés par 90 secondes, cela donne 1600 kbit/s. Une fois retranchés 128 kbit/s d’audio, il reste environ 1470 kbit/s pour l’image.

Le même calcul pour des durées courantes, après déduction de 128 kbit/s d’audio :

| Durée de la vidéo | Fichier de 7,5 Mo | Fichier de 15 Mo | Fichier de 18 Mo |
|---|---|---|---|
| 30 secondes | 1870 kbit/s | 3870 kbit/s | 4670 kbit/s |
| 1 minute | 870 kbit/s | 1870 kbit/s | 2270 kbit/s |
| 2 minutes | 370 kbit/s | 870 kbit/s | 1070 kbit/s |
| 5 minutes | 70 kbit/s | 270 kbit/s | 350 kbit/s |

Les valeurs sont arrondies à l’inférieur.

## Quelle résolution et quel codec choisir

Un débit n’est généreux ou serré que par rapport à l’image qu’il doit remplir. Pour situer l’échelle, les [réglages de mise en ligne recommandés](https://support.google.com/youtube/answer/1722171){: hreflang="en"} (en anglais) par YouTube pour les fréquences d’images standard demandent 8 Mbit/s en 1080p, 5 Mbit/s en 720p, 2,5 Mbit/s en 480p et 1 Mbit/s en 360p. Ces valeurs sont élevées, car YouTube réencode tout ce qu’il reçoit, mais elles montrent à quelle vitesse le besoin diminue avec la taille de l’image : le 1080p compte 2,25 fois plus de pixels que le 720p.

Une règle approximative : si votre budget vidéo est nettement sous la moitié de la valeur de YouTube pour la résolution de la vidéo, descendez d’un cran de résolution. Selon cette règle, une vidéo d’une minute à 18 Mo (2270 kbit/s) convient mieux au 720p qu’au 1080p, et à 7,5 Mo (870 kbit/s) elle relève du 480p ou moins. Trois autres réglages jouent sur le résultat :

- **Le débit audio.** Pour une vidéo où quelqu’un parle face caméra, 64 kbit/s au lieu de 128 kbit/s laisse la différence à l’image. Sur une vidéo de 5 minutes à 15 Mo, cela représente près d’un quart de débit vidéo en plus.
- **La fréquence d’images.** Une vidéo à 60 i/s répartit ses bits sur deux fois plus d’images qu’une vidéo à 30 i/s. Les valeurs de YouTube pour 48 à 60 i/s sont supérieures de moitié environ à celles pour 24 à 30 i/s.
- **Le codec.** Apple indique que le [HEVC compresse mieux que le H.264](https://support.apple.com/fr-fr/116944) et que les appareils Apple récents le lisent. Mais vous ne maîtrisez pas l’appareil sur lequel la pièce jointe sera ouverte, et le H.264 dans un fichier MP4 se lit presque partout. La page d’Apple précise aussi que ses appareils *peuvent* convertir le HEVC en H.264 lors d’un partage vers un appareil qui ne sait pas le lire ; pour un fichier déjà compressé, il est plus simple de choisir le H.264 vous-même.

## Quand envoyer un lien plutôt qu’un fichier

La ligne des 5 minutes du tableau marque le point où la compression cesse d’être utile : 270 kbit/s, c’est environ le quart de ce que YouTube conseille pour le 360p. Quand le budget tombe aussi bas, un lien sert mieux le destinataire qu’une pièce jointe.

- **Mail Drop**, dans l’app Mail et iCloud Mail, envoie des fichiers jusqu’à 5 Go sous forme de lien de téléchargement qui expire au bout de 30 jours. Mail le propose quand un message dépasse ce que votre fournisseur autorise.
- **Gmail** remplace de lui-même une pièce jointe de plus de 25 Mo par un lien Google Drive.
- **Outlook** vous invite à compresser le fichier ou à le partager depuis un espace de stockage en ligne.

Avec un lien, le destinataire reçoit l’original en pleine qualité, et une copie reste sur un serveur aussi longtemps que le lien existe.

## Compresser la vidéo pour un mail avec MediaKit

[MediaKit](/fr/apps/mediakit/) fait le calcul ci-dessus sur l’appareil, sur iPhone comme sur Mac, et n’envoie jamais la vidéo en ligne. « Compresser une vidéo » fait partie des cinq outils qui restent gratuits sans limite de durée après les 3 premiers jours, un fichier à la fois.

1. **Ouvrez la vidéo.** Sur Mac, déposez-la sur la fenêtre. Sur iPhone, ajoutez-la depuis l’app Photos ou l’app Fichiers, ou envoyez-la depuis le menu Partager d’une autre app.
2. **Choisissez l’outil « Compresser une vidéo »** et réglez **Mode** sur **Taille cible**.
3. **Saisissez la cible** du tableau des trois quarts, par exemple 18, avec l’unité sur Mo. MediaKit compte un mégaoctet pour 1 000 000 d’octets.
4. **Ouvrez « Avancé ».** Réglez **Résolution max.** d’après le tableau des débits, laissez **Codec** sur H.264 pour un mail, et choisissez **64 kbps (voix)** sous **Débit audio** si la vidéo contient surtout de la parole.
5. **Lancez la compression, puis vérifiez la taille** du résultat avant de le joindre.

En mode « Taille cible », MediaKit fait lui-même les étapes 1 à 4 du calcul : il divise la cible par la durée de la vidéo, retranche le débit audio que vous avez choisi et garde 3 % de marge, encode, puis mesure le fichier écrit et réencode avec un débit corrigé s’il a manqué la cible. Il ne vous remet jamais un fichier plus gros que la cible : s’il n’y parvient pas, il s’arrête avec une erreur. Une source en 4K ou en 1440p démarre avec **Résolution max.** réglée sur 1080p ; pour une petite cible, choisissez une valeur plus basse.

Si vous utilisez déjà HandBrake pour cette tâche, le [comparatif avec HandBrake](/alternatives/handbrake/){: hreflang="en"} (en anglais) détaille les différences entre les deux, et le [comparatif avec Compress Videos & Resize Video](/alternatives/compress-videos-resize-video/){: hreflang="en"} (en anglais) fait de même sur iPhone. Un [article précédent](/fr/journal/your-photos-shouldnt-ride-the-elevator/) explique pourquoi le studio garde ce travail à l’écart des serveurs d’autrui, et [un autre](/fr/journal/every-media-tool-already-on-your-mac/) présente toute la boîte à outils.
