---
layout: journal
slug: every-media-tool-already-on-your-mac
ref: /journal/every-media-tool-already-on-your-mac/
permalink: /fr/journal/every-media-tool-already-on-your-mac/
translated_from: 2026-11-08
last_updated: 2026-11-08
date: 2026-11-08
title: "Convertir une vidéo sur Mac : les outils sont déjà dans macOS, il fallait les relier"
seo:
  title: "Convertir une vidéo sur Mac sans l’envoyer en ligne"
  description: "Convertir une vidéo sur Mac sans l’envoyer en ligne : MediaKit réunit plus de 150 outils vidéo, audio, image, PDF et archives, exécutés sur l’appareil."
  keywords:
    - "convertir une vidéo sur mac"
    - "convertir vidéo mac"
    - "compresser une vidéo sur mac"
    - "outils intégrés au mac"
    - "convertisseur de fichiers hors ligne"
    - "convertir des fichiers sans les envoyer en ligne"
    - "compresser pdf mac"
    - "mediakit"
lede: "MediaKit réunit plus de 150 outils locaux pour la vidéo, l’audio, l’image, le PDF, les archives et les livres numériques derrière une seule interface de glisser-déposer, sur Mac et sur iPhone. Chaque opération s’exécute sur votre appareil. Cet article défend cette idée, et explique pourquoi « envoyer son fichier sur un site au hasard pour le convertir » reste l’une des pires options par défaut du web ouvert en 2026."
quick_answer: "Pour convertir une vidéo sur Mac sans l’envoyer sur un site, MediaKit s’en charge sur l’appareil : cette app pour Mac et iPhone réunit plus de 150 outils pour la vidéo, l’audio, l’image, le PDF, les archives et les livres numériques derrière une seule surface de glisser-déposer. Le travail sur la vidéo, l’image, le PDF et la voix s’appuie sur des frameworks d’Apple comme AVFoundation, Core Image, PDFKit, Vision et Speech. Les fichiers ne quittent jamais l’appareil, à la différence de CloudConvert, Zamzar ou Smallpdf. Cinq outils, dont la compression vidéo, restent gratuits sans limite de durée ; la conversion vidéo n’en fait pas partie."
excerpt: "MediaKit est une app pour Mac et iPhone qui réunit plus de 150 outils sur l’appareil pour compresser, convertir et retoucher la vidéo, l’audio, l’image, le PDF, les archives et les livres numériques, en grande partie avec les frameworks d’Apple. Cet article soutient que le Mac fournit depuis des années les briques du travail multimédia en local, que des convertisseurs en ligne comme CloudConvert, Zamzar et Smallpdf survivent surtout parce que personne n’avait réuni les outils locaux derrière une seule interface, et explique pourquoi cinq outils sont gratuits sans limite de durée."
faq:
  - q: "Existe-t-il une alternative à CloudConvert ou à Smallpdf sur Mac ?"
    a: "MediaKit est une app pour Mac et iPhone qui compte plus de 150 outils et exécute chaque opération en local, en grande partie avec des frameworks d’Apple comme AVFoundation, Core Image, PDFKit, Vision et AppleArchive. Les fichiers ne quittent jamais la machine, à la différence de CloudConvert, Zamzar, Smallpdf ou iLovePDF, qui les envoient à l’infrastructure de leur exploitant pour les traiter."
  - q: "Quels outils de MediaKit restent gratuits ?"
    a: "Cinq outils sont gratuits sans limite de durée, un fichier à la fois : compresser une vidéo, compresser une image, redimensionner une image, convertir un audio et compresser un PDF. Pendant vos 3 premiers jours, tous les autres outils fonctionnent aussi, avec un export par exécution. Ensuite, ils demandent Pro, vendu au mois, à l’année ou en achat unique à vie : l’abonnement est donc facultatif."
  - q: "MediaKit peut-il remplacer Final Cut Pro ou DaVinci Resolve ?"
    a: "Non. MediaKit effectue des opérations linéaires du quotidien comme compresser, convertir, couper, recadrer, fusionner et normaliser. Il n’a pas de timeline et n’est pas un logiciel de montage non linéaire : pour monter un film, utilisez Final Cut Pro ou DaVinci Resolve."
  - q: "MediaKit fonctionne-t-il avec l’app Raccourcis ?"
    a: "Oui, sur iPhone et sur Mac. MediaKit propose six actions pour l’app Raccourcis (Compresser une vidéo, Convertir une image, Compresser une image, Fusionner des PDF, Créer un ZIP et Extraire le texte d’une image) et, sur Mac, un élément dans la barre des menus : ses outils s’intègrent donc à vos propres automatisations. Les actions s’exécutent en local, comme le reste de l’app."
mentioned_apps:
  - mediakit
read_time: "7 min de lecture"
---

Quelque part sur le web, quelqu’un envoie une vidéo de quatre gigaoctets, le récital de piano d’un enfant, vers un site de conversion gratuit, parce que le format que produit son appareil photo est un format que sa mère ou son père ne peut pas ouvrir. Le site prendra la vidéo, la fera passer par un serveur que cette personne ne voit pas, enregistrera la requête, gardera peut-être le fichier en cache, lira à coup sûr les métadonnées, puis renverra un fichier qui se lit sur un portable Windows. L’utilisateur fermera l’onglet et supposera que tout va bien.

Tout ne va pas bien, et en 2026 c’est aussi inutile.

[MediaKit](/fr/apps/mediakit/) est la petite app pour Mac (elle fonctionne aussi sur iPhone) que le studio a lancée précisément sur cette idée : toutes les opérations de conversion multimédia dont un utilisateur ordinaire a besoin sont faisables en local sur un Mac depuis une dizaine d’années, et des services comme [CloudConvert](/fr/alternatives/cloudconvert/), Zamzar, Smallpdf et les autres dominent encore parce que personne ne s’était donné la peine de réunir ces briques locales derrière une seule interface de glisser-déposer.

Cet article dit ce qu’est MediaKit, ce qu’il n’est pas, et pourquoi « le site de conversion gratuit » reste l’une des pires options par défaut du web ouvert.

## Quels outils multimédias Apple fournit-il déjà avec le Mac ?

Je veux être précis, parce que l’apport de MediaKit est réel mais limité.

La plupart des algorithmes (encodage H.264 et HEVC, encodage AAC, quantification PNG, compression PDF, OCR, transcription vocale sur l’appareil, suppression de l’arrière-plan) viennent de frameworks d’Apple fournis avec macOS :

- **AVFoundation** s’occupe de la vidéo et de l’audio : compression, conversion, coupe et fusion.
- **Core Image** s’occupe des transformations d’image, des réglages de couleur et des filtres au niveau du pixel.
- **PDFKit** s’occupe de la fusion, de la division, du caviardage, de la signature, des filigranes, des en-têtes et pieds de page, et des modifications qui gardent les vecteurs nets et le texte interrogeable.
- **Vision** s’occupe de l’OCR et de la suppression de l’arrière-plan.
- **Speech** s’occupe de la transcription de l’audio et de la vidéo sur l’appareil.
- **Compression** et **AppleArchive** s’occupent du ZIP, du TAR, du GZIP, du XZ et du BZIP2. MediaKit y ajoute ses propres garde-fous contre le path traversal et les zip bombs.

Le RAR fait exception : Apple ne le lit pas, si bien que MediaKit s’appuie sur une petite bibliothèque unrar open source, en extraction seule. Rien du reste n’est nouveau ni propriétaire du studio. Ces frameworks sont présents sur tous les Mac depuis des années.

MediaKit les relie : une seule app avec une seule surface de glisser-déposer, un élément dans la barre des menus, six actions pour l’app Raccourcis et plus de 150 outils qui correspondent aux formats et aux opérations qu’un utilisateur ordinaire de Mac veut réellement. L’autre option, ce sont cinq utilitaires distincts, chacun avec ses réglages, son modèle de licence et son rythme de mises à jour.

Le pari, c’est donc la réunion de ces outils en un seul endroit. Rien dans MediaKit n’est nouveau, et je continuerai à le dire, parce que la tentation marketing d’exagérer est réelle.

## Pourquoi les convertisseurs en ligne restent pourtant utilisés

Si les briques locales sont là depuis des années, pourquoi l’utilisateur médian envoie-t-il encore sa vidéo à un inconnu ?

Je vois quatre raisons, et elles expliquent aussi la forme que MediaKit devait prendre :

1. **La découverte.** Dans une recherche en anglais comme « convert HEIC to JPG », les premiers résultats sont des sites de conversion. Avec « convert HEIC to JPG on Mac », ce sont *aussi* des sites de conversion. Apple ne fait pas connaître aux utilisateurs l’existence de Core Image. Elle n’a pas à le faire.
2. **La couverture des formats.** Les outils intégrés au Mac gèrent les formats courants ; les convertisseurs en ligne gèrent la longue traîne : un RAR chiffré, du WebM, de l’ALAC dans un MKV inhabituel. L’utilisateur ouvre le site parce que le site *traitera* tout ce qu’on lui envoie. MediaKit couvre une partie de cette longue traîne en local (RAR4 et RAR5, fichiers MKV, RAW d’appareil photo et AVIF en entrée) et en laisse une autre de côté : il refuse les RAR chiffrés et ne lit pas le WebM.
3. **L’usage en une étape.** Le site, c’est un clic : coller, déposer, télécharger. Les outils natifs obligeaient jusqu’ici à savoir quelle app ouvrir. La réponse de MediaKit est la surface de dépôt unique : déposez n’importe quel fichier et l’app propose les outils qui lui conviennent.
4. **La confiance par lassitude.** Les utilisateurs sont las, le site est rapide et a l’air professionnel, et le coût pour la vie privée est invisible. Il ne le devient que si l’on imagine ce fichier indexé quelque part, ou cité plus tard dans l’annonce d’une fuite de données.

Je ne crois pas que la plupart des utilisateurs *veuillent* envoyer des fichiers sensibles à des inconnus. Je crois qu’on ne leur a pas proposé d’option par défaut tout aussi simple et qui n’envoie rien.

Le cas des fichiers MKV, et la différence entre changer de conteneur et réencoder, est traité dans notre article [convertir MKV en MP4](/fr/journal/convertir-mkv-en-mp4/).

## Ce qui est gratuit, ce qui est payant

L’offre gratuite compte cinq outils : compresser une vidéo, compresser une image, redimensionner une image, convertir un audio et compresser un PDF. Ce sont les opérations qu’un utilisateur ordinaire de Mac effectue réellement : compresser une pièce jointe pour un mail, alléger une photo, convertir un fichier audio. Elles restent gratuites sans limite de durée, un fichier à la fois, sans compte à rebours.

Pendant les 3 premiers jours, tous les autres outils sont aussi débloqués, avec un export par exécution, pour que vous puissiez voir si la longue traîne compte pour vous avant de décider. Passés ces 3 jours, les cinq outils gratuits le restent ; tout le reste, ainsi que les lots de plus d’un fichier, demande Pro. Pro se vend au mois, à l’année ou en achat unique à vie : vous pouvez donc vous passer complètement d’abonnement.

Fixer l’offre gratuite ainsi est, parmi les apps Mac indépendantes, un peu inhabituel. HandBrake, ImageOptim et Keka sont tous gratuits. L’argument du studio : les opérations qu’un utilisateur type exécute *le plus souvent* doivent aussi être gratuites dans MediaKit, de façon permanente et non comme prolongation d’un essai. Si vous ne faites que compresser des vidéos et redimensionner des photos, MediaKit ne vous coûte rien, et vous avez une app de l’App Store en bac à sable plutôt qu’une installation de FFmpeg avec Homebrew.

Pro existe pour ceux qui utilisent la longue traîne.

Les archives RAR et les PDF trop lourds ont chacun leur article : [ouvrir un fichier RAR sur Mac ou iPhone](/fr/journal/ouvrir-fichier-rar-mac-iphone/) et [compresser un PDF sur Mac](/fr/journal/compresser-pdf-mac/).

## Ce que MediaKit ne fait pas

Quelques précisions que j’ai appris à mettre par écrit :

- **MediaKit n’est pas un logiciel de montage non linéaire.** Il ne remplace ni Final Cut Pro ni DaVinci Resolve. Si vous montez un film, n’utilisez pas MediaKit : les opérations disponibles sont linéaires (compresser, convertir, couper, recadrer, fusionner, normaliser).
- **MediaKit n’est pas un outil d’IA générative.** Vision et Speech sont des frameworks de reconnaissance : OCR, segmentation de l’arrière-plan, transcription. Le studio n’exécute aucun modèle de diffusion, et rien ne part vers un service d’IA dans le cloud. Si vous avez besoin de générer des images, MediaKit n’est pas le bon outil.
- **MediaKit n’est pas un outil de synchronisation dans le cloud.** Il n’y a pas de cloud. Pour retrouver vos modifications sur un autre appareil, enregistrez-les vous-même dans iCloud Drive, ou là où vous gardez vos fichiers.
- **MediaKit ne règle pas le problème des convertisseurs en ligne à l’échelle des institutions.** Des universités disent encore aux étudiants d’envoyer leurs PDF à un outil tiers parce que le service informatique n’a pas pris la peine d’installer quoi que ce soit. Le studio ne peut pas y remédier de l’extérieur. Mais sur un Mac personnel, la réponse est désormais dans l’App Store.

## Avant d’envoyer une vidéo de famille

Il se peut que vous soyez sur le point d’envoyer une vidéo de famille à vos parents, dans un format qu’ils ne peuvent pas ouvrir. Si vous cherchez un site de conversion pour y remédier : n’y allez pas.

Le fichier ferait l’aller-retour par le centre de données de quelqu’un d’autre, et vous n’avez aucun moyen de vérifier qu’il est supprimé dès la fermeture de l’onglet, quoi que dise la politique de confidentialité.

[MediaKit](/fr/apps/mediakit/) est gratuit pour les opérations dont vous avez le plus probablement besoin (compresser une vidéo, compresser une image, redimensionner une image, convertir un audio et compresser un PDF), débloqué pendant 3 jours pour tout le reste, et votre fichier ne quitte jamais l’appareil.

L’argument plus large du studio sur le traitement des fichiers, dans le cloud ou en local, se trouve dans l’article [Convertir une photo HEIC en JPG sans l’envoyer au centre de données d’un inconnu](/fr/journal/your-photos-shouldnt-ride-the-elevator/), si vous voulez la version longue. La version courte : Apple nous donne ces briques depuis des années, et nous devrions les utiliser.
