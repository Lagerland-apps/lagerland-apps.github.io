---
layout: journal
slug: engine-depth-at-club-level-tune-down
ref: /journal/engine-depth-at-club-level-tune-down/
permalink: /fr/journal/engine-depth-at-club-level-tune-down/
translated_from: 2026-11-08
last_updated: 2026-11-08
date: 2026-11-08
title: "Analyse de partie d’échecs : au niveau club, mieux vaut baisser la profondeur du moteur que la monter"
seo:
  title: "Analyse de partie d’échecs : quelle profondeur de moteur ?"
  description: "Analyse de partie d’échecs : Chess.com va à la profondeur 22, Stockfish à 35, mais un joueur de 800 à 1800 n’en tire rien. Pourquoi viser plus bas."
  keywords:
    - "analyse de partie d’échecs"
    - "analyse partie échecs"
    - "profondeur stockfish"
    - "niveau stockfish"
    - "profondeur d’analyse échecs"
    - "stockfish pour débutants"
    - "analyse d’échecs niveau club"
lede: "Toutes les applications d’échecs mettent en avant la profondeur de leur moteur. L’analyse de Chess.com va jusqu’à la profondeur 22 et le cloud de Lichess jusqu’à 28. Stockfish sur un ordinateur récent ira sans broncher à la profondeur 35 si on lui en laisse le temps. Cet article explique pourquoi rien de tout cela n’aide un joueur classé entre 800 et 1800 à progresser, et pourquoi la revue de partie de Chessful fait tourner Stockfish à la profondeur 16 : juste au-delà du niveau où les erreurs qui décident les parties de club deviennent visibles, et pas plus profond."
quick_answer: "Pour l’analyse de partie d’échecs d’un joueur de club, une profondeur de moteur supérieure à environ 13 à 15 demi-coups produit des lignes que même de bons joueurs de club ne peuvent ni lire ni appliquer : elles sont justes, mais on ne peut pas les enseigner. Pour un joueur classé entre 800 et 1800, les erreurs qui décident les parties sont visibles aux profondeurs 10 à 15 : pièces en prise, fourchettes manquées, angle mort face à l’élimination du défenseur, erreurs d’opposition. Une analyse plus profonde fait ressortir des subtilités de niveau grand maître sur lesquelles l’utilisateur ne peut pas agir, et elles noient le signal utile. La revue de partie de Chessful fait tourner Stockfish à la profondeur 16, juste au-delà de la bande où se trouvent les erreurs corrigibles, ce qui garde aussi l’analyse rapide sur l’appareil ; la raison est pédagogique, le matériel n’est pas la contrainte."
excerpt: "Toutes les applications d’échecs mettent en avant la profondeur de leur moteur. Chessful choisit délibérément une profondeur plus basse, 16. L’argument : au-delà de la profondeur 15, on obtient des lignes que même de bons joueurs de club ne peuvent ni lire ni appliquer. Elles sont justes, mais on ne peut rien en apprendre. Les erreurs qui décident les parties de club sont visibles à la profondeur 13."
faq:
  - q: "Pourquoi Chessful fait-elle tourner Stockfish moins profond que Chess.com ou Lichess ?"
    a: "Parce qu’une analyse plus profonde produit des lignes que les joueurs de club ne peuvent ni lire ni appliquer. À partir de la profondeur 25, Stockfish fait ressortir des séquences forcées de sept coups que même des joueurs classés 2000 ratent. Les montrer à un joueur classé 1400, c’est du bruit : il ne peut pas agir sur l’information, et elle prend la place des erreurs visibles aux profondeurs 12 à 15 (pièces en prise, fourchettes manquées, erreurs d’opposition) qu’il peut corriger. La revue de partie de Chessful va à la profondeur 16, juste au-delà de la bande où les erreurs qui décident les parties de club deviennent visibles, et pas plus loin. La raison est pédagogique ; le matériel n’est pas la contrainte."
  - q: "L’analyse de Chessful est-elle moins précise que celle de Chess.com ?"
    a: "Précision et profondeur ne sont pas la même chose. L’analyse de Chessful est juste. Stockfish est juste à la profondeur 13 comme il l’est à la profondeur 33 : les évaluations peuvent différer, mais aucune n’est fausse. Ce qui compte, c’est de savoir quelle évaluation est utile. Pour un joueur de club, les profondeurs 13 à 15 sont l’horizon où ses décisions se jouent réellement. L’analyse à la profondeur 22 de Chess.com est plus précise au sens absolu, mais cette précision supplémentaire décrit des positions que le joueur ne peut pas atteindre depuis son niveau."
  - q: "Une analyse plus profonde aide-t-elle à trouver le meilleur coup ?"
    a: "Pas au niveau club. À la profondeur 25, le coup préféré du moteur est souvent un coup positionnel tranquille dont l’avantage n’apparaît qu’au bout de 12 demi-coups. Un joueur qui ne voit pas ce gain de matériel ne tire rien du coup qu’on lui montre : il ne peut pas se le justifier, ne peut pas le généraliser à des positions voisines et ne le rejouera pas. Le coup qui mérite d’être enseigné est celui qui gagne du matériel ou arrête une menace dans l’horizon de calcul du joueur, et ce coup est généralement visible à la profondeur 13."
  - q: "À partir de quel niveau une analyse plus profonde devient-elle utile ?"
    a: "Autour de 2000 de classement et au-delà, où les séquences forcées de 5 à 7 demi-coups deviennent couramment calculables et où les décisions pertinentes passent dans l’horizon de 6 à 12 demi-coups. À ce niveau, l’utilisateur peut lire des lignes de moteur plus longues et les appliquer. Pour la plupart des joueurs de club (800 à 1800), une profondeur plus faible donne un signal d’entraînement plus rapide et plus net."
  - q: "Une profondeur plus faible économise-t-elle la batterie de l’iPhone ?"
    a: "Oui. La charge de travail de Stockfish croît à peu près géométriquement avec la profondeur (chaque demi-coup supplémentaire explore plusieurs fois plus de nœuds), donc une recherche moins profonde se termine plus tôt et consomme moins d’énergie. L’économie de batterie n’est toutefois qu’un effet secondaire. Si une analyse plus profonde donnait un meilleur entraînement aux joueurs de club, Chessful irait plus profond et en accepterait le coût en batterie. Ce n’est pas le cas, donc elle ne le fait pas."
mentioned_apps:
  - chessful
read_time: "10 min de lecture"
---

Toutes les applications d’échecs mettent en avant la profondeur de leur moteur. Le Game Review de [Chess.com](/fr/alternatives/chess-com/) fait tourner Stockfish jusqu’à la profondeur 22. L’analyse dans le cloud de [Lichess](/fr/alternatives/lichess/) propose la profondeur 28. Stockfish sur un ordinateur récent ira sans broncher à la profondeur 35 si on lui en laisse le temps.

La revue de partie de [Chessful](/fr/apps/chessful/) fait tourner Stockfish à la profondeur 16, moins profond que toutes les autres. Rien ne l’y oblige : elle le fait parce que, pour les joueurs auxquels s’adresse Chessful, une analyse plus profonde rend l’entraînement moins bon.

Voici l’argument. Il va à contre-courant dans les logiciels d’échecs, où la « profondeur » passe pour un critère de qualité, comme la puissance pour une voiture. En dessous d’environ 2000 de classement, **une profondeur de moteur supérieure à 15 demi-coups produit des lignes que l’utilisateur ne peut ni lire ni appliquer.** Les lignes sont justes, et personne à ce niveau ne peut en tirer de leçon. Les erreurs qui décident les parties entre 800 et 1800 sont visibles aux profondeurs 10 à 15, et une analyse plus profonde fait ressortir des subtilités qui les noient.

Ce choix a un effet secondaire : l’analyse s’exécute vite sur l’appareil, ce qui rend l’analyse sur iPhone, iPad et Mac praticable. Mais la raison pédagogique est venue en premier.

## Ce que signifie vraiment la profondeur du moteur

Dans le vocabulaire des moteurs d’échecs, la *profondeur* est le nombre de demi-coups (ply en anglais) que le moteur calcule à l’avance. À la profondeur 13, le moteur évalue les positions en supposant que les deux camps jouent leurs meilleurs coups pendant 13 demi-coups (environ 6 coups complets de chaque camp). La profondeur 25 représente environ 12 coups complets d’avance.

Chaque demi-coup supplémentaire multiplie la taille de l’arbre de recherche (par le *facteur de branchement effectif* qui subsiste après l’élagage), si bien que le coût s’accumule : passer de la profondeur 13 à la profondeur 25 demande de nombreuses fois plus de calcul, bien plus que le double. Les moteurs modernes l’atténuent avec l’élagage alpha-bêta, les tables de transposition et des heuristiques agressives, mais c’est cette croissance du coût qui justifie l’existence même de l’analyse dans le cloud : la plupart des analyses à la profondeur 25 sont trop coûteuses pour un téléphone.

Chess.com et Lichess peuvent proposer les profondeurs 22 à 28 parce qu’elles font tourner l’analyse dans le cloud, sur de la puissance de calcul louée, et renvoient le résultat. Le prix à payer est l’aller-retour avec le cloud et, chez Chess.com, un quota quotidien d’analyses profondes.

Chessful fait tourner Stockfish sur l’appareil, et son coût est le matériel : un iPhone dispose d’une fraction de la puissance d’un ordinateur de bureau, et une analyse profonde sur un téléphone est trop lente pour être utilisable.

La plupart des gens s’arrêtent là. La version habituelle : « Chessful va moins profond parce qu’elle y est obligée ; Chess.com et Lichess vont plus profond parce qu’elles le peuvent. » Présenté ainsi, plus profond vaut mieux, et Chessful fait au mieux avec une limite matérielle.

Cette version est fausse, et l’erreur compte, parce qu’elle décide si l’entraînement que produit l’app aide effectivement à progresser. L’argument va en réalité dans l’autre sens.

## Ce que les joueurs de club peuvent lire

Prenons un exemple précis. Imaginez une position d’une partie de club entre deux joueurs classés 1400, au 18e coup. Le joueur vient de jouer `Fd3`, dans l’intention de renforcer l’aile roi. Stockfish évalue la position.

À la **profondeur 12**, Stockfish indique : évaluation -1,4, meilleur coup `De2`, ligne `De2 Cf4 Fxf4 Dxf4 Txe6`. La ligne compte cinq demi-coups, et le joueur peut la lire : la dame en e2 défend, le cavalier entre en jeu, le fou s’échange, la dame reprend, la tour monte prendre en e6. Une séquence de cinq demi-coups est à la portée du calcul d’un joueur classé 1400. Il peut voir pourquoi `De2` était juste (elle empêche `Cf4` d’être efficace), dérouler la ligne sur un échiquier et en tirer une règle générale : quand la colonne e est ouverte et que la dame est exposée, développer la dame vers la défense.

À la **profondeur 22**, Stockfish indique : évaluation -1,9, meilleur coup `Te1`, ligne `Te1 Cf4 Fxf4 Dxf4 Te5 Dg4 h3 Dxd1+ Rh2 Dxa1 Te8+ Txe8 Dxa1`. La ligne compte 13 demi-coups. Elle commence par un coup de tour tranquille qui ne rapporte que dix coups plus tard, sous la forme d’un échange de dames. Le joueur classé 1400 ne peut pas lire cette ligne. Il ne peut pas calculer 13 demi-coups de tête, et la jouer sur un échiquier ne lui montrera pas pourquoi `Te1` vaut mieux que la ligne `De2` que le moteur recommandait à la profondeur 12.

Les deux recommandations du moteur sont justes. Les évaluations diffèrent (-1,4 contre -1,9), mais aucune n’est fausse : chaque fois, Stockfish lit la position jusqu’à son propre horizon. Ce qui compte, c’est laquelle enseigne quelque chose.

Pour le joueur classé 1400, la ligne de la profondeur 12 **lui apprend quelque chose** sur le placement défensif des pièces. La ligne de la profondeur 22 lui apprend que le moteur en sait plus que lui, ce qu’il savait déjà, et qui ne lui donne rien à emporter dans la partie suivante.

Voilà l’affirmation centrale : **au niveau club, une profondeur de moteur au-delà de ce que le joueur peut calculer est du bruit.**

## Pourquoi le bruit nuit activement à l’entraînement

Une analyse plus profonde ne se contente pas d’être inutile. Elle prend la place de l’aide qui existe.

Supposons que l’analyse à la profondeur 22 désigne `Te1` comme meilleur coup et classe le `Fd3` du joueur parmi les « gaffes » (l’écart d’évaluation dépasse le seuil de gaffe de la plateforme). Supposons que l’analyse à la profondeur 12 désigne `De2` comme meilleur coup et classe `Fd3` parmi les « erreurs » (une chute d’évaluation plus faible, puisque la comparaison porte sur un horizon de calcul plus court).

Le verdict de la profondeur 12 est le plus utile. `Fd3` était une mauvaise appréciation défensive que le joueur peut reconnaître et travailler : il n’a pas vu qu’il fallait placer la dame en e2 avant de laisser entrer `Cf4`. C’est un motif de placement des défenseurs, qui se travaille et se reporte dans la partie suivante.

Le verdict de la profondeur 22 est exact sur le plan technique et ne produit aucun entraînement. « Vous auriez dû jouer `Te1` pour une séquence forcée de 13 demi-coups » n’est pas une leçon qu’un joueur peut absorber. C’est un fait sur la position, qui ne change rien à sa façon de jouer.

Entraînez un joueur sur des analyses à la profondeur 22 : il apprend à hocher la tête devant ce que dit le moteur et à admettre que le moteur voit plus loin. Il n’apprend pas à trouver lui-même de meilleurs coups. La justesse du moteur finit par remplacer le développement de son propre calcul.

## La bonne profondeur

Pour les joueurs de club classés entre 800 et 1800, les profondeurs 12 à 15 forment la bande où :

1. Les recommandations du moteur sont assez courtes pour qu’un joueur de club attentif les calcule.
2. Les erreurs que le moteur signale (pièces en prise, fourchettes et clouages manqués, faiblesses de la dernière rangée, mauvaise sécurité du roi, erreurs de finale) sont celles qui décident les parties à ce niveau.
3. Les exercices construits à partir de l’analyse visent des motifs que le joueur a une chance réaliste de reconnaître dans sa prochaine partie.

À la profondeur 13 en particulier, Stockfish trouve de façon fiable :

- toutes les pièces en prise (la profondeur 2 à 3 suffit) ;
- toutes les tactiques en un coup (fourchettes, clouages, enfilades) : profondeur 3 à 5 ;
- toutes les séquences forcées en deux coups (la plupart des combinaisons tactiques que les joueurs de club ratent) : profondeur 7 à 9 ;
- la plupart des séquences forcées en trois coups (l’extrémité de l’horizon tactique d’un joueur de club) : profondeur 11 à 13 ;
- les mauvaises appréciations défensives dont les conséquences apparaissent en 3 à 5 demi-coups : profondeur 10 à 13.

La profondeur 13 couvre tout l’horizon de calcul d’un joueur de club type dans ses parties réelles. Aller plus loin trouve des erreurs *supplémentaires*, et ce sont aussi des erreurs que le joueur ne peut pas corriger.

L’équilibre bascule en haut de la fourchette des joueurs de club. Entre 1800 et 2000 environ, les joueurs commencent à lire de façon fiable des lignes de moteur plus longues, et la bonne profondeur monte. À 2200, une analyse plus profonde est vraiment utile. À 2400, les joueurs veulent la profondeur 30 et plus, parce qu’ils peuvent s’en servir.

La plupart des joueurs de club sont en dessous de cette bande, et pour eux les erreurs se situent aux profondeurs 13 à 15. La profondeur 16 de Chessful se place juste au-delà.

La conception de puzzles reprend la même idée par l’autre bout, avec la profondeur comme mesure de ce qu’un joueur peut utiliser : dans Millrace, un solveur en largeur d’abord prouve la plus courte solution de chaque niveau, et [les niveaux sont générés et vérifiés par recherche](/journal/how-millrace-levels-are-made/){: hreflang="en"} (en anglais) pour que des coups joués au hasard en viennent rarement à bout.

## L’effet secondaire matériel

Faire tourner Stockfish à une profondeur de niveau club sur un iPhone est rapide, et Chessful estime la durée de l’analyse avant le début d’un import. À la profondeur 22, sur le même téléphone, l’analyse prendrait plusieurs fois plus longtemps, le téléphone chaufferait et le coût en batterie serait réel.

La rapidité découle donc du choix pédagogique. L’analyse de Chessful est praticable sur l’appareil parce qu’une profondeur modérée y est rapide. Analyser sur l’appareil, sans cloud ni compte, est *rendu possible* par le choix de la profondeur, mais le choix de la profondeur est venu en premier.

Si la profondeur 22 produisait un meilleur entraînement pour les joueurs de club, Chessful ferait tourner la profondeur 22 et accepterait l’analyse plus lente et le coût en batterie. Elle devrait probablement aussi se rabattre sur l’analyse dans le cloud sur les téléphones plus anciens, ce qui affaiblirait le volet vie privée. Cela ne s’est pas produit, parce que la profondeur 22 ne produit pas un meilleur entraînement ; le volet vie privée n’a jamais été placé avant l’entraînement. Le choix pédagogique et le volet vie privée vont simplement dans le même sens.

## À quoi sert une analyse plus profonde

L’analyse profonde du moteur a des usages concrets :

- les joueurs classés au-dessus de 2000, dont l’horizon de calcul s’étend sur 6 à 12 demi-coups ;
- la préparation d’ouvertures, où l’on veut les meilleurs coups objectifs dans des positions de théorie que l’on reverra ;
- les échecs par correspondance, où la cadence permet de travailler réellement les lignes du moteur ;
- les parties entre moteurs, où l’objectif est la justesse du moteur et où la progression humaine n’entre pas en jeu ;
- l’exploration théorique, où la question est « quelle est la vérité de cette position ? » et non « que devrait jouer ce joueur ensuite ? ».

Aucun de ces cas ne relève de la progression au niveau club. Cet entraînement vise à corriger les motifs que le joueur rate dans ses parties réelles, et ces motifs sont visibles à la profondeur 13. Une analyse plus profonde ajoute des motifs sur lesquels le joueur ne peut pas agir.

Le secteur des logiciels d’échecs a adopté « plus de profondeur = meilleure app » pour deux raisons. La profondeur est un critère facile pour se faire concurrence (il suffit de louer plus de puissance dans le cloud). Et les joueurs les plus visibles, joueurs titrés, streamers et créateurs de contenu, peuvent utiliser une analyse plus profonde et en font l’éloge en conséquence. Le critère est devenu un argument marketing avant que quiconque se demande s’il servait l’utilisateur médian.

Chessful parie que l’utilisateur médian est mieux servi par un entraînement qu’il peut lire.

---

[Chessful est disponible sur l’App Store.](https://apps.apple.com/app/id6761336870) Chaque erreur qu’elle trouve est expliquée en langage clair et classée dans l’un des 10 types d’erreur, et votre entraînement quotidien est construit à partir de ces erreurs ; la [page de l’app](/fr/apps/chessful/) donne les détails. Un référentiel plus large de 30 motifs d’erreur courants au niveau club, et la façon dont ils correspondent aux 10 types de Chessful, se trouve dans l’article sur [les 30 motifs d’erreur aux échecs](/fr/journal/30-chess-mistake-motifs/). Le [guide des meilleures applications d’échecs pour iPhone](/fr/guides/best-chess-apps-iphone/) situe Chessful parmi les autres applications.
