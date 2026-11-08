---
layout: journal
slug: convertir-mkv-en-mp4
permalink: /fr/journal/convertir-mkv-en-mp4/
local_only: true
last_updated: 2026-11-08
date: 2026-11-08
title: "Convertir un MKV en MP4 : remux sans perte, VLC, en ligne ou MediaKit"
seo:
  title: "Convertir MKV en MP4 : VLC, en ligne ou MediaKit"
  description: "Convertir MKV en MP4 sur Mac ou iPhone : remux sans perte ou réencodage, VLC gratuit, convertisseur en ligne ou MediaKit sur l’appareil."
  keywords:
    - "convertir mkv en mp4"
    - "convertir mkv en mp4 mac"
    - "convertir mkv en mp4 iphone"
    - "convertir mkv en mp4 vlc"
    - "mkv vers mp4 sans perte"
    - "convertir mkv en mp4 gratuitement"
    - "convertir mkv en mp4 gros fichier"
lede: "Un fichier MKV est un conteneur, pas un codec : le convertir en MP4 peut se limiter à changer l’emballage sans toucher à l’image. Cet article explique la différence entre remux et réencodage, ce que l’on peut faire avec VLC, ce qu’implique un convertisseur en ligne pour un gros fichier, et comment MediaKit ouvre un MKV sur Mac et sur iPhone, avec les formats de son qui passent et ceux qui sont supprimés."
quick_answer: "Pour convertir un MKV en MP4 sans perte, il faut un remux : la vidéo et le son sont recopiés dans un conteneur MP4 sans être réencodés, ce qui suppose des codecs compatibles. VLC, gratuit, sait convertir (menu Media, Convert/Save), alors qu’un convertisseur en ligne oblige à envoyer tout le fichier. MediaKit remuxe un MKV sur l’appareil, sur Mac et sur iPhone : H.264, HEVC, AAC et AC-3 passent tels quels, mais le son DTS, E-AC-3 et MP3 est supprimé, avec un avertissement. L’outil « Convertir » est gratuit pendant les 3 premiers jours puis réservé à Pro, tandis que « Compresser une vidéo » reste gratuit et produit un MP4 en réencodant."
excerpt: "Convertir un MKV en MP4 : ce qu’est un conteneur, remux ou réencodage, VLC et les convertisseurs en ligne pour un gros fichier, et la façon dont MediaKit ouvre et convertit un MKV sur Mac et sur iPhone."
faq:
  - q: "Comment convertir un MKV en MP4 gratuitement ?"
    a: "VLC est gratuit et sait convertir : le wiki de VideoLAN décrit un assistant accessible par le menu Media, commande Convert/Save. Dans MediaKit, l’outil « Compresser une vidéo » reste gratuit après les 3 premiers jours, un fichier à la fois, et transforme un MKV en MP4 ; il réencode, donc il ne s’agit pas d’une conversion sans perte. L’outil « Convertir », qui sait remuxer, est gratuit pendant les 3 premiers jours, puis réservé à Pro."
  - q: "Peut-on convertir un MKV en MP4 sans perte de qualité ?"
    a: "Oui, quand les codecs le permettent : un remux recopie la vidéo et le son dans un nouveau conteneur sans les réencoder. MediaKit remuxe ainsi les MKV en H.264 ou HEVC avec du son AAC ou AC-3. Le son DTS, E-AC-3 ou MP3 d’un MKV est en revanche supprimé, avec un avertissement."
  - q: "Comment convertir un MKV en MP4 avec VLC ?"
    a: "Le wiki de VideoLAN, qui signale lui-même que sa page est dépassée, décrit un assistant ouvert par le menu Media, commande Convert/Save, où l’on choisit un codec vidéo, un codec audio et un conteneur. Il indique aussi qu’un transcodage peut être très lent, et qu’il est inutile de transcoder quand les flux ont déjà le codec voulu. La page étant dépassée, consultez la documentation de votre version de VLC."
  - q: "Quel convertisseur en ligne pour un gros fichier MKV ?"
    a: "Un convertisseur en ligne exige d’envoyer le fichier sur ses serveurs avant toute conversion, ce qui oblige à envoyer un gros MKV en entier. Pour un gros fichier, une conversion sur l’appareil évite cet envoi : VLC ou MediaKit conviennent."
  - q: "Comment convertir un MKV en MP4 sur iPhone ?"
    a: "MediaKit ouvre les fichiers MKV sur iPhone (iOS 17 ou version ultérieure) et propose l’outil « Convertir » vers MP4, MOV ou M4V. Pour un remux, choisissez l’option « Conserver l’original (remux) » : MediaKit recopie alors tels quels, sans réencodage, la vidéo H.264 ou HEVC et le son AAC ou AC-3. Le son DTS, E-AC-3 ou MP3 est supprimé, avec un avertissement."
  - q: "Comment convertir un MKV en MP4 sur Mac ?"
    a: "Dans le Finder, faites un clic droit sur le MKV, choisissez « Ouvrir avec », puis MediaKit, qui figure dans cette liste pour les MKV. Choisissez ensuite « Convertir », le format MP4 et « Conserver l’original (remux) ». MediaKit demande macOS 14.6 ou version ultérieure."
mentioned_apps:
  - mediakit
read_time: "6 min de lecture"
---

Un fichier MKV est un conteneur, qui emballe des flux de vidéo, de son et de sous-titres. Convertir un MKV en MP4 peut donc se limiter à changer l’emballage, sans réencoder l’image ni le son, et sans perte de qualité. C’est possible seulement quand les codecs à l’intérieur conviennent au conteneur MP4, et c’est ce qui distingue une conversion sans perte d’une conversion qui dégrade le fichier. Cet article suit ce fil, puis compare VLC, les convertisseurs en ligne et [MediaKit](/fr/apps/mediakit/).

## Qu’est-ce qu’un MKV, et en quoi diffère-t-il d’un MP4 ?

Le projet Matroska, qui maintient le format, précise sur son site que le conteneur [n’est pas un format de compression vidéo ou audio](https://www.matroska.org/what_is_matroska.html){: hreflang="en"} (en anglais). Il le décrit comme une enveloppe qui peut contenir plusieurs flux audio, vidéo et de sous-titres, de quoi stocker un film entier dans un seul fichier. Selon le projet, les fichiers vidéo Matroska portent l’extension .mkv. Il range MP4 parmi les conteneurs existants dont Matroska se veut l’alternative libre : MP4 est donc un conteneur lui aussi.

Deux fichiers peuvent ainsi avoir la même image et le même son et ne se distinguer que par leur enveloppe. Changer d’enveloppe se fait sans toucher au contenu ; changer de codec demande de décoder puis de réencoder.

## Pourquoi un MKV ne s’ouvre pas toujours sur un iPhone ou un Mac

Apple l’explique dans une page d’assistance sur les [fichiers multimédias qui ne s’ouvrent pas](https://support.apple.com/fr-fr/102644) : les apps d’Apple comme Photos, iMovie, Safari, Keynote et QuickTime Player sont compatibles avec de nombreux formats, mais les formats plus anciens ou spécialisés peuvent ne pas fonctionner s’ils ne sont pas pris en charge par l’appareil, son système ou l’app utilisée. Apple cite l’extension .mkv, avec .avi et .wmv, parmi celles à rechercher pour trouver une autre app qui prend en charge le format. Sur Mac, la même page indique que le Finder peut afficher « Type : fichier vidéo Matroska » : sélectionnez le fichier, puis appuyez sur Commande + I.

## Remux ou réencodage : quand on ne perd rien

Un remux déplace les flux de vidéo et de son d’un conteneur à l’autre sans les décoder. Dans MediaKit, c’est l’option « Conserver l’original (remux) » de l’outil « Convertir ». Le gain tient à ce que le fichier n’est pas recompressé : l’image qui sort est l’image qui entrait.

Un remux ne marche que si MP4 sait porter les codecs du fichier. Dans MediaKit, la vidéo H.264 et HEVC et le son AAC et AC-3 passent tels quels. Le son DTS, E-AC-3 et MP3 d’un MKV est supprimé, avec un avertissement : la vidéo est conservée, mais pas ces pistes de son. Si votre film a une piste DTS, lisez donc le message après la conversion.

Un réencodage, lui, produit une nouvelle compression : c’est ce que font la compression à une taille cible et le choix d’un autre codec. Il convient quand le remux est impossible ou quand on veut réduire le fichier, mais il coûte une partie de la qualité.

## Convertir un MKV en MP4 avec VLC

VLC est gratuit. Le [site de VideoLAN](https://www.videolan.org/vlc/){: hreflang="en"} (en anglais) présente VLC comme un lecteur multimédia libre et open source, et énumère MKV parmi les formats qu’il lit. Pour convertir, le wiki de VideoLAN décrit, dans une [page sur le transcodage](https://wiki.videolan.org/Transcode/){: hreflang="en"} (en anglais), un assistant ouvert par le menu Media, commande Convert/Save, qui demande un codec vidéo, un codec audio et un conteneur. La même page indique qu’il est inutile de transcoder quand les flux ont déjà le codec voulu ; son auteur pense, sans en être sûr, que l’interface appelle cette option « keep the original track ». Le wiki prévient aussi que la page est dépassée et qu’un transcodage peut être très lent. Pour les étapes exactes, reportez-vous à la documentation de votre version de VLC.

Si VLC fait déjà partie de vos outils, il fait le travail sans dépense, sur l’ordinateur. Cet article ne couvre pas son usage sur iPhone.

## Les convertisseurs en ligne et le gros fichier

Un convertisseur en ligne reçoit votre fichier sur ses serveurs avant de le convertir, puis vous le renvoie. Pour un gros MKV, le fichier doit donc d’abord être envoyé en entier, et son contenu quitte votre appareil. Deux pages de ce site détaillent ce compromis : l’article sur [la conversion d’une photo HEIC sans l’envoyer en ligne](/fr/journal/your-photos-shouldnt-ride-the-elevator/) et la [comparaison avec CloudConvert](/fr/alternatives/cloudconvert/).

## Convertir un MKV en MP4 avec MediaKit

MediaKit est une app pour iPhone et pour Mac qui travaille sur l’appareil : le fichier n’est envoyé nulle part. Elle ouvre les fichiers MKV directement, en les décompressant elle-même, et réunit d’autres outils vidéo, présentés dans l’article [Convertir une vidéo sur Mac](/fr/journal/every-media-tool-already-on-your-mac/).

Sur Mac (macOS 14.6 ou version ultérieure), dans le Finder, faites un clic droit sur le MKV, choisissez « Ouvrir avec », puis MediaKit, qui est listé pour les MKV. Vous pouvez aussi déposer le fichier sur l’icône du Dock.

Sur iPhone (iOS 17 ou version ultérieure), ouvrez MediaKit et importez le fichier depuis l’app Fichiers.

Dans les deux cas :

1. Choisissez l’outil « Convertir ».
2. Prenez MP4 comme format de sortie (MOV et M4V existent aussi).
3. Pour un remux, choisissez « Conserver l’original (remux) » comme codec. H.264, HEVC et ProRes sont les autres choix, avec réencodage.
4. Lancez l’exécution et lisez l’avertissement éventuel sur le son supprimé.

Si l’avertissement signale un son supprimé, cette piste manque dans le MP4. D’après la fiche de l’app, ces formats de son sont retirés quand MediaKit ouvre un MKV : si la piste compte pour vous, gardez l’original ou passez par un autre outil.

L’outil « Compresser une vidéo » accepte lui aussi un MKV : les sources MP4, MOV et M4V gardent leur conteneur, les autres deviennent des MP4. Il réencode selon une qualité, une taille cible ou un débit : utile pour alléger un fichier, mais ce n’est pas une conversion sans perte. Notre article sur [la compression d’une vidéo à envoyer par mail](/fr/journal/compress-a-video-for-email/) détaille la taille cible.

### Ce qui est gratuit

« Compresser une vidéo » fait partie des cinq outils qui restent gratuits sans limite de durée, un fichier à la fois. « Convertir » fonctionne gratuitement pendant les 3 premiers jours après l’installation, avec un export par exécution, puis demande Pro : {P_MONTHLY@mediakit}/mois, {P_YEARLY@mediakit}/an ou {P_LIFETIME@mediakit} en une fois, d’après les prix de l’App Store français. Un convertisseur gratuit comme VLC suffit si vous convertissez un fichier par an.

## Quelle méthode choisir ?

Choisissez d’abord entre remux et réencodage. Si vous voulez garder l’image telle quelle, cherchez une option qui recopie les flux et vérifiez qu’elle ne supprime aucune piste de son. Si vous voulez un fichier plus léger, un réencodage est normal, et il faut alors accepter une perte.

VLC et MediaKit ne s’excluent pas. VLC reste un lecteur gratuit qui lit déjà le MKV tel quel, ce qui peut suffire si le but est seulement de le regarder sur un ordinateur. MediaKit sert quand le fichier doit finir en MP4, MOV ou M4V sur un iPhone ou un Mac, par exemple pour l’ouvrir dans les apps d’Apple.

| Besoin | Piste |
|---|---|
| Un fichier, sans dépense, sur ordinateur | VLC |
| Un MKV sensible ou très gros, sans l’envoyer | VLC ou MediaKit |
| Un remux sans réencodage, sur Mac ou iPhone | MediaKit, « Convertir », « Conserver l’original (remux) » |
| Alléger un fichier trop lourd | MediaKit, « Compresser une vidéo » |
