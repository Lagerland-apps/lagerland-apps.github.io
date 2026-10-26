---
layout: journal
slug: 30-chess-mistake-motifs
title: "The 30 chess mistake motifs Chessful detects (and why each one matters)"
seo:
  title: "Chess Mistakes Explained: 30 Types That Lose Games"
  description: "The 30 chess mistakes that lose club-level games, from hung pieces and missed forks to wrong pawn breaks and endgame slips, each with its cause and fix."
  keywords:
    - "chess mistakes"
    - "types of chess mistakes"
    - "chess mistake categories"
    - "common chess mistakes"
    - "chess blunders"
    - "chess improvement"
date: 2026-05-13
lede: "Most chess apps reduce 'why did I lose' to a centipawn graph. Chessful sorts the mistake into one of about thirty specific categories, each with a name, a structural cause, and a drill that fixes it. This post is the full catalogue. Chessful users can use it as a reference, and anyone else gets a short tour of the mistakes that decide club-level games."
quick_answer: "Chessful classifies significant chess mistakes into roughly 30 categories grouped under five skill dimensions. Tactical motifs (hung piece, missed fork, missed pin, missed skewer, missed discovered attack, missed double attack, missed deflection, missed overload, back-rank threat, smothered mate possibility). Defensive motifs (defender-removal blindness, king-safety underestimate, prophylactic skip, weakening pawn push). Positional motifs (wrong piece traded, wrong side castled, weak square allowed, wrong pawn break, time-on-wrong-move). Opening motifs (repertoire drift, book-move missed, transposition into bad line). Endgame motifs (opposition direction error, king-too-late, wrong rook activation, drawn-but-played-on, wrong-color bishop endgame, technique error in K+P). Each motif maps to one of five skill buckets and triggers spaced-repetition drilling on the underlying pattern."
faq:
  - q: "How many chess mistake categories does Chessful detect?"
    a: "About 30, organised under five skill dimensions: tactics, defense, positional play, openings, and endgames. The exact count shifts a little between app versions as the motif detectors get refined. This post lists the current catalogue and the dimension each motif belongs to."
  - q: "Why classify mistakes into motifs instead of just showing the engine evaluation?"
    a: "Most club-level players can't read a centipawn evaluation, and feedback they can't read doesn't change how they play. A motif label is something you can remember, drill, and recognise. You can carry \"defender-removal blindness\" into your next game; you can't do much with \"-3.4 → -8.1 over the line Nxd5 Qxe1+ Kh2 Qe5+\"."
  - q: "How are the motifs detected?"
    a: "Hand-curated rule-based detectors run on top of Stockfish output. The rules are ordered by specificity and the strictest matching rule wins, so one position doesn't get classified as five different things and dilute the training signal. The rules are explicit and inspectable, not learned, which keeps the classification stable between app updates."
  - q: "Are these the same mistake categories chess coaches teach?"
    a: "Mostly. The taxonomy draws on mainstream improvement literature (Aagaard's Excelling at Chess, Yusupov's Build Up Your Chess series, Silman's How to Reassess Your Chess) and on what coaches flag in club-level games. A few categories, such as \"repertoire drift\" and \"book-move missed\", exist because the algorithm can compare your current game with your historical opening choices. Most of the rest are standard."
  - q: "Will the motif list change?"
    a: "Yes. We add motifs when we see recurring mistake patterns that the current rules don't catch cleanly. Now and then a motif gets split (when one category is doing too much work) or two get merged (when they rarely produce different training value). Every change goes in the app's changelog. Between releases the taxonomy is stable enough that the spaced-repetition queue doesn't reset."
mentioned_apps:
  - chessful
read_time: "11 min read"
excerpt: "The complete catalogue of the ~30 chess mistake motifs Chessful detects, grouped under five skill dimensions, each with its structural cause and the drill that fixes it. A reference for Chessful users and a short tour of the mistakes that decide club-level games."
last_updated: 2026-10-26
---

After the earlier post, [How Chessful turns a Stockfish evaluation into adaptive training](/journal/how-chessful-builds-adaptive-training/), went up, the most common follow-up question was simple: *what are the motif categories?*

That post described the pipeline and left the catalogue as a black box of "about thirty categories." Here is the full current taxonomy, organised under the five skill dimensions Chessful tracks, with the structural cause of each motif and the drill that fixes it.

The taxonomy isn't proprietary. Most of these categories are standard chess teaching, covered in Aagaard's *Excelling at Chess* series, Yusupov's nine-volume *Build Up Your Chess* curriculum, Silman's *How to Reassess Your Chess*, and de la Maza's *Rapid Chess Improvement*. A few (repertoire drift, book-move missed, time-on-wrong-move) are things an analyser with your full game history can see and a coach reviewing one game can't. The rest is standard improvement material under a name a club player can remember during the next game.

We publish the catalogue because **you can only argue with an algorithm if you know what it is looking for**. Without the list, you can't tell whether Chessful's classifier flagged the right thing in your game. With it, you can check.

## Skill dimension 1: Tactics (10 motifs)

In a tactical motif the mistake was a failure of calculation or pattern recognition in a forcing sequence. These are usually the easiest to act on: they drill well, you learn to spot them quickly, and they come up again in every opening.

### 1. Hung piece

The classic. You moved a piece (or left one) on a square where it can be taken for nothing, or for less than it's worth. Drilling pattern: a piece-safety scan of the position before you commit to a move.

### 2. Missed fork

An enemy piece (often a knight) could reach a square that attacks two of your pieces at once and wins material. Drilling pattern: knight-radius blindness, meaning learning to see where an opposing knight could land next, especially around the king.

### 3. Missed pin

You moved a piece so that another piece behind it could no longer move (or would be unprotected if it did). Drilling pattern: awareness of files and diagonals around long-range pieces (bishops, rooks, queens).

### 4. Missed skewer

A piece attacked a more valuable piece in front, forced it to move, and took the less valuable piece behind. Drilling pattern: noticing when pieces line up, particularly rooks on the back rank and queens on a shared diagonal.

### 5. Missed discovered attack

A piece moved out of the way and uncovered an attack by the piece behind it, often with check. Drilling pattern: x-ray vision through your own pieces.

### 6. Missed double attack

One move that attacks two separate enemy pieces or squares, not necessarily a fork. Drilling pattern: spotting two threats at once.

### 7. Missed deflection

A piece needed to be lured off a critical defensive square, and the deflecting move was there but wasn't played. Drilling pattern: finding which enemy piece is over-loaded (defending several squares) and the move that exploits it.

### 8. Missed overload

A defending piece had too many jobs, and a single attack forced it to choose and won material. Drilling pattern: counting attackers and defenders on every critical square before you commit.

### 9. Back-rank threat

Your own pieces blocked your king's escape squares, and a back-rank mate was available but not seen (in either direction). Drilling pattern: prophylactic h-pawn pushes and recognising rook-plus-back-rank shapes.

### 10. Smothered mate possibility

A knight on f7 / f2 (or similar) gives mate when the king's own pieces block its escape squares. It's less common, but when it appears it usually decides the game.

## Skill dimension 2: Defense (5 motifs)

Club players train defense less than anything else. Generic puzzle apps drill attacking tactics, while failing to recognise defensive problems is what costs games in the 1200 to 1800 range.

### 11. Defender-removal blindness

The piece you just moved was the only defender of a critical square (often on the back rank, often next to the king). Drilling pattern: before any capture or trade, check whether your piece is currently defending something. This is the most common motif at club level; Chessful logs flag it more than any other category.

### 12. King-safety underestimate

You played a move that opens lines toward your king (a pawn move, a piece trade) and did nothing about the structural weakness it created. Drilling pattern: counting attackers near the king before each move.

### 13. Prophylactic skip

A defensive move (often h3 / h6, or a piece retreat to a defensive square) was available and would have stopped a threat that arrived three moves later. Drilling pattern: looking for the opponent's plan before you make your own.

### 14. Weakening pawn push without compensation

A pawn push (often f3 / f6 or g3 / g6) created a hole or weakened a diagonal without giving you enough activity back. Drilling pattern: pawn-structure awareness, meaning knowing which pawn moves leave permanent weaknesses.

### 15. Wrong piece exchanged for defender

A trade you started removed one of your own defenders and left a critical square uncovered. It differs from defender-removal blindness because you chose the trade. Drilling pattern: counting defenders after the trade.

## Skill dimension 3: Positional play (5 motifs)

Positional motifs take longest to drill, but the improvement lasts longest too, and it carries over from one opening to another.

### 16. Wrong piece traded

You traded a structurally important piece (a good bishop, an active knight) for a less important enemy piece. Drilling pattern: judging piece quality before any trade.

### 17. Wrong side castled

You castled on one side when the pawn structure or piece placement made the other side safer. Drilling pattern: a structural check before castling.

### 18. Weak square allowed

You let an enemy piece reach an outpost (often c4 / c5 / d4 / d5 / e4 / e5 / f4 / f5) where nothing could challenge it. Drilling pattern: spotting outposts before your opponent gets there.

### 19. Wrong pawn break

A pawn break (the move that resolves central tension or opens an attacking path) came too late, at the wrong moment, or in the wrong direction. Drilling pattern: learning the standard pawn break for each pawn structure.

### 20. Time-on-the-clock-on-the-wrong-move

This one is specific to Chessful. You spent far too much clock time on a move that didn't need it (often a forced recapture or a routine developing move) and were short of time for a critical decision later. Drilling pattern: budgeting time per move. It's only flagged in games played with a clock.

## Skill dimension 4: Openings (3 motifs)

Opening motifs depend most on the individual user, because they depend on the repertoire you actually play. Over time Chessful builds a profile of your most-played lines and flags deviations from them.

### 21. Repertoire drift

You left your usual opening setup in a way that lost a tempo, allowed an early exchange you normally avoid, or transposed into a structure outside your repertoire. Drilling pattern: reviewing the opening line around the point where you deviated.

### 22. Book-move missed

A widely known book continuation was available and was the principled move. You played a reasonable-looking non-book move that gave up an advantage the book line keeps. Drilling pattern: studying the book line in that specific opening.

### 23. Transposition into a bad line

Your sequence of moves transposed into a position known to be inferior, often because the move order gave up a critical defensive resource. Drilling pattern: transposition awareness within your own repertoire.

## Skill dimension 5: Endgames (6 motifs)

Endgame motifs are the most technical. Pattern recognition has to come with concrete calculation, and small mistakes here are the likeliest to turn a winning position into a draw.

### 24. Opposition direction error

In a king-and-pawn endgame you took (or gave up) the opposition in the wrong direction, so the opposing king could either advance with its pawn or block yours. Drilling pattern: technique for direct, distant, and diagonal opposition.

### 25. King-too-late

Your king didn't become active in time. It stayed on the back rank while the opposing king walked to the centre and the position simplified into a lost king-and-pawn race. Drilling pattern: recognising the moment in a middlegame when activating the king becomes the most important move.

### 26. Wrong rook activation

In a rook endgame you put your rook in a passive spot (behind your own pawn, or in front of an opposing passed pawn from the wrong side). Drilling pattern: Tarrasch's rule, rooks behind passed pawns, both yours and the opponent's.

### 27. Drawn-but-played-on

You turned a winning endgame into a draw with a move that simplified into a known drawn structure (often a wrong-color bishop ending, or a fortress). Drilling pattern: recognising drawn endgame structures before you simplify into them.

### 28. Wrong-color bishop endgame

You traded into an endgame where your remaining bishop is the wrong colour to control your passed pawn's promotion square. It often comes together with drawn-but-played-on. Drilling pattern: projecting the endgame before the trade.

### 29. Technique error in K+P endgame

A known winning technique (Lucena, Philidor, square-of-the-pawn, key-square calculation) was available, and you didn't execute it correctly. Drilling pattern: repeating the specific technique that failed.

### 30. Technique error in R+P endgame

The rook-endgame version of the K+P motif: you picked the right technique (Lucena bridge, Philidor third-rank defence, short-side defence) and executed it incorrectly. Drilling pattern: repetition of that specific rook-endgame technique.

## How the catalogue maps to training

Each motif belongs to exactly one of the five skill buckets (the dimension it's listed under above). When Chessful flags a motif in one of your games, it flags that skill bucket. The spaced-repetition queue draws from the flagged buckets, most recently flagged first, with Leitner-schedule intervals between repeats.

The bucket layer sits between motif detection and the training queue because **patterns generalise better within a skill dimension than across dimensions**. If you keep missing forks, more fork puzzles are the right fix. If you alternate between missing forks and misjudging the opposition in endgames, those are two separate failures and need separate drilling, which a generic "tactics-and-endgame practice" queue wouldn't give you.

So the skill dimensions are where spaced repetition gets scheduled, and grouping the list for display is a side effect.

## What's not in the catalogue (and why)

A few things Chessful deliberately doesn't detect:

- **Time-pressure tactics.** A blunder with under thirty seconds on the clock is often a time-management problem and not a pattern problem. Chessful flags it as `time-on-the-clock-on-the-wrong-move` (motif 20) and not as a tactical failure, because drilling tactics doesn't fix time pressure. Drilling time budgeting does.
- **Move-order subtleties in deeply theoretical lines.** If you play the Najdorf Poisoned Pawn and miss a nuance on move 20, Chessful flags it as `repertoire drift`, not as a positional or tactical motif. What helps there is opening study, and pattern drilling wouldn't.
- **Psychological mistakes.** Resigning too early, accepting a draw in a winning position, playing too aggressively when ahead: Chessful doesn't try to detect these, because engine output alone can't reliably tell them apart from objective mistakes.

We left these out on purpose. In each case motif drilling is the wrong fix, and Chessful would mislead you by pretending it wasn't.

## How the catalogue evolves

The catalogue changes between app versions in two ways:

- **New motifs get added** when a recurring mistake shows up in user games and the existing rules don't catch it cleanly. The latest addition (v1.4) was `weakening pawn push without compensation`. It used to be part of king-safety underestimate and was split out because the two need different drills.
- **Existing motifs occasionally get split or merged** when one category is doing too much work, or when two categories rarely produce different training value. We're conservative about it and only do it when the resulting training queue would clearly differ.

Every change goes in the app's changelog with the motif name and the version. The spaced-repetition queue doesn't reset when the taxonomy changes; flagged positions move to the closest matching motif in the new taxonomy.

---

This catalogue is what Chessful is checking when it tells you "you played Nxd5; the knight was your only back-rank defender." That sentence is what you see. Underneath, the motif label is `defender-removal blindness`, the bucket it flags is `Defense`, and your next training session draws from that bucket using spaced repetition.

All of it is open to inspection, which is why we published it.

[Chessful is available on the App Store.](https://apps.apple.com/app/id6761336870) The method behind the catalogue is in [How Chessful turns a Stockfish evaluation into adaptive training](/journal/how-chessful-builds-adaptive-training/). The companion design note on the forty AI opponents is [Forty chess opponents, and none of them are me](/journal/forty-chess-opponents/).
