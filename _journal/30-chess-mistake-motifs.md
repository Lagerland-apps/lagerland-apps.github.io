---
layout: journal
slug: 30-chess-mistake-motifs
title: "The 30 chess mistake motifs Chessful detects (and why each one matters)"
seo:
  title: "Chess Mistakes Explained: 30 Types That Lose Games"
  description: "The 30 chess mistakes that lose club-level games — hung pieces, missed forks, wrong pawn breaks, endgame slips — each with its cause and the fix."
  keywords:
    - "chess mistakes"
    - "types of chess mistakes"
    - "chess mistake categories"
    - "common chess mistakes"
    - "chess blunders"
    - "chess improvement"
date: 2026-05-13
lede: "Most chess apps reduce 'why did I lose' to a centipawn graph. Chessful turns it into one of about thirty specific mistake categories — each with a name, a structural cause, and an explicit drill that fixes it. This post is the full catalogue. It doubles as a reference page for Chessful users and a short tour of the mistakes that actually decide club-level games."
quick_answer: "Chessful classifies significant chess mistakes into roughly 30 categories grouped under five skill dimensions. Tactical motifs (hung piece, missed fork, missed pin, missed skewer, missed discovered attack, missed double attack, missed deflection, missed overload, back-rank threat, smothered mate possibility). Defensive motifs (defender-removal blindness, king-safety underestimate, prophylactic skip, weakening pawn push). Positional motifs (wrong piece traded, wrong side castled, weak square allowed, wrong pawn break, time-on-wrong-move). Opening motifs (repertoire drift, book-move missed, transposition into bad line). Endgame motifs (opposition direction error, king-too-late, wrong rook activation, drawn-but-played-on, wrong-color bishop endgame, technique error in K+P). Each motif maps to one of five skill buckets and triggers spaced-repetition drilling on the underlying pattern."
faq:
  - q: "How many chess mistake categories does Chessful detect?"
    a: "Approximately 30, organised under five skill dimensions: tactics, defense, positional play, openings, endgames. The exact count varies slightly with app version as motif detectors get refined. The current catalogue and the dimension each motif maps to are documented in this post."
  - q: "Why classify mistakes into motifs instead of just showing the engine evaluation?"
    a: "Because centipawn evaluation is unreadable to most club-level players, and unreadable feedback doesn't change behaviour. A motif label gives the user something memorable, drillable, and recognisable — \"defender-removal blindness\" is a concept you can carry into the next game; \"-3.4 → -8.1 over the line Nxd5 Qxe1+ Kh2 Qe5+\" is not."
  - q: "How are the motifs detected?"
    a: "Hand-curated rule-based detectors run on top of Stockfish output. Rules are ordered by specificity — the strictest matching rule wins, to avoid the failure mode where one position gets classified as five different things and dilutes the training signal. The rules are explicit and inspectable rather than learned, which keeps the classification stable between app updates."
  - q: "Are these the same mistake categories chess coaches teach?"
    a: "Mostly yes. The taxonomy is informed by mainstream improvement literature (Aagaard's Excelling at Chess, Yusupov's Build Up Your Chess series, Silman's How to Reassess Your Chess) and by what coaches actually flag in club-level games. A few categories — like \"repertoire drift\" and \"book-move missed\" — are specific to the algorithm's ability to compare your current game against your historical opening choices. Most of the rest are standard."
  - q: "Will the motif list change?"
    a: "Yes. New motifs get added as we encounter recurring mistake patterns the current rules don't catch cleanly. Existing motifs occasionally get split (when a single category is doing too much work) or merged (when two categories rarely produce distinct training value). All changes are logged in the app's changelog. The taxonomy is stable enough between releases that the spaced-repetition queue doesn't reset."
mentioned_apps:
  - chessful
read_time: "11 min read"
excerpt: "The complete catalogue of the ~30 chess mistake motifs Chessful detects, grouped under five skill dimensions, each with the structural cause and the drill that fixes it. Doubles as a reference for Chessful users and a short tour of the mistakes that actually decide club-level games."
---

When the prior post — [How Chessful turns a Stockfish evaluation into adaptive training](/journal/how-chessful-builds-adaptive-training/) — went up, the most common follow-up question was straightforward: *what are the motif categories?*

Fair question. The post described the pipeline but treated the motif catalogue as a black box of "about thirty categories." This post opens that box. Below is the full current taxonomy, organised under the five skill dimensions Chessful tracks, with the structural cause of each motif and the drill that fixes it.

The taxonomy isn't proprietary. Most of these categories are standard chess pedagogy — what's documented in Aagaard's *Excelling at Chess* series, Yusupov's *Build Up Your Chess* nine-volume curriculum, Silman's *How to Reassess Your Chess*, and de la Maza's *Rapid Chess Improvement*. A few — repertoire drift, book-move missed, time-on-wrong-move — are specific to what an analyser running on top of your full game history can detect that a human coach reviewing one game cannot. Most of the rest is standard improvement material wrapped in a name a club player can carry into the next game.

The reason it's worth publishing the catalogue is that **algorithm transparency is the only way to argue with an algorithm**. If you don't know what Chessful's classifier is looking for, you can't tell whether it's flagging the right thing about your game. If you can read the catalogue, you can.

## Skill dimension 1: Tactics (10 motifs)

Tactical motifs are the ones where the mistake was a calculation or pattern-recognition failure on a forcing sequence. They tend to be the most actionable category — drillable, fast to recognise, and reliably re-encountered across openings.

### 1. Hung piece

The classic. You moved a piece (or left a piece) onto a square where it can be captured for nothing, or for less than it's worth. Drilling pattern: piece-safety scans on the position before committing a move.

### 2. Missed fork

An enemy piece (often a knight) could have moved to a square attacking two of your pieces simultaneously, winning material. Drilling pattern: knight-radius blindness — recognising where an opposing knight could land next, especially around the king.

### 3. Missed pin

You moved a piece in a way that left another piece behind it unable to move (or unprotected if it did move). Drilling pattern: file/diagonal awareness around long-range pieces (bishops, rooks, queens).

### 4. Missed skewer

A piece attacked a more valuable piece in front, forcing it to move and capturing the less valuable piece behind. Drilling pattern: piece-alignment awareness — particularly for back-rank rooks and same-diagonal queens.

### 5. Missed discovered attack

A piece moved out of the way to reveal an attack from another piece behind it — often combined with check. Drilling pattern: x-ray vision through your own pieces.

### 6. Missed double attack

A single move attacking two distinct enemy pieces or squares, not necessarily a fork. Drilling pattern: simultaneous-threat detection.

### 7. Missed deflection

A piece had to be lured off a critical defensive square, and the deflecting move was available but not played. Drilling pattern: identifying which enemy piece is over-loaded (defending multiple squares) and finding the move that exploits it.

### 8. Missed overload

A defending piece had too many jobs; a single attack forced the choice and won material. Drilling pattern: counting attackers and defenders on every critical square before committing.

### 9. Back-rank threat

Your king's escape squares were blocked by your own pieces, and a back-rank mate was available but not seen (in either direction). Drilling pattern: prophylactic h-pawn pushes; recognising rook + back-rank shapes.

### 10. Smothered mate possibility

A knight on f7 / f2 (or similar) creates a mate when the king's escape squares are blocked by its own pieces. Less common but reliably decisive when it appears.

## Skill dimension 2: Defense (5 motifs)

Defensive motifs are the most under-trained category among club players. Generic puzzle apps drill tactical attacks; defensive recognition is what costs games at the 1200–1800 range.

### 11. Defender-removal blindness

The piece you just moved was the only defender of a critical square (often the back rank, often a king-adjacent square). Drilling pattern: before any capture or trade, identify whether your piece is currently defending something. This is the single most common motif at club level — Chessful logs flag it more than any other category.

### 12. King-safety underestimate

You played a move that opens lines toward your king (a pawn move, a piece trade) without compensating for the structural weakness. Drilling pattern: counting attackers near the king before each move.

### 13. Prophylactic skip

A defensive move (often h3 / h6, or a piece retreat to a defensive square) was available and would have stopped a threat that materialised three moves later. Drilling pattern: looking for the opponent's plan before formulating your own.

### 14. Weakening pawn push without compensation

A pawn push (often f3 / f6 or g3 / g6) created a hole or weakened a diagonal without enough activity in return. Drilling pattern: pawn structural awareness — identifying which pawn moves create permanent weaknesses.

### 15. Wrong piece exchanged for defender

A trade you initiated removed your own defensive piece and left a critical square undefended. Distinct from defender-removal blindness because the trade was voluntary. Drilling pattern: post-trade defender count.

## Skill dimension 3: Positional play (5 motifs)

Positional motifs are the slowest to drill but produce the most durable improvement. They generalise across openings.

### 16. Wrong piece traded

You exchanged a piece that was structurally important (a good bishop, an active knight) for a less important enemy piece. Drilling pattern: piece-quality assessment before any trade.

### 17. Wrong side castled

You castled queenside or kingside when the opposite would have been safer based on pawn structure or piece placement. Drilling pattern: pre-castling structural review.

### 18. Weak square allowed

You allowed an enemy piece to reach an outpost square (often c4 / c5 / d4 / d5 / e4 / e5 / f4 / f5) where it couldn't be challenged. Drilling pattern: identifying outpost squares before your opponent gets there.

### 19. Wrong pawn break

A pawn break (the move that resolves the central tension or creates an attacking path) was either delayed too long, mistimed, or played in the wrong direction. Drilling pattern: recognising the canonical pawn break for each pawn structure.

### 20. Time-on-the-clock-on-the-wrong-move

The Chessful-specific motif — you spent disproportionate clock time on a move that didn't deserve it (often a recapture that was forced, or a routine developing move), leaving you with too little time for a critical decision later. Drilling pattern: time-budgeting per move. Only flagged in games where a clock is on.

## Skill dimension 4: Openings (3 motifs)

Opening motifs are the most user-specific category — they depend on what repertoire the user actually plays. Chessful builds a profile of your most-played opening lines over time and flags deviations.

### 21. Repertoire drift

You deviated from your usual opening setup in a way that lost a tempo, allowed an early piece exchange you don't normally allow, or transposed into a structure outside your repertoire. Drilling pattern: opening-line review focused on the deviation point.

### 22. Book-move missed

A widely-known book continuation was available and would have been the principled move; you played a reasonable-looking but non-book alternative that gave up an advantage the book line preserves. Drilling pattern: book-line study on the specific opening.

### 23. Transposition into a bad line

You played a sequence of moves that, by transposition, reached a position known to be inferior — often because the move order swapped a critical defensive resource. Drilling pattern: transposition-awareness for your own repertoire.

## Skill dimension 5: Endgames (6 motifs)

Endgame motifs are the most technically distinct — they're the ones where pattern recognition has to be paired with concrete calculation, and where small mistakes are most likely to convert a winning position into a draw.

### 24. Opposition direction error

In a king-and-pawn endgame, you took (or yielded) the opposition in the wrong direction, allowing the opposing king to either advance with its pawn or block your advance. Drilling pattern: opposition technique on direct, distant, and diagonal opposition.

### 25. King-too-late

Your king didn't activate in time for the endgame — it sat passively on the back rank while the opposing king moved to the centre and the position simplified into a lost king-and-pawn race. Drilling pattern: identifying the point in a middlegame where king activation becomes the most important move.

### 26. Wrong rook activation

In a rook endgame, you placed your rook passively (behind your own pawn, or in front of an opposing passed pawn from the wrong side). Drilling pattern: Tarrasch's rule — rooks behind passed pawns, both yours and the opponent's.

### 27. Drawn-but-played-on

You converted a winning endgame into a draw by playing a move that simplified to a known-drawn structure (often wrong-color bishop, or a fortress). Drilling pattern: recognising drawn endgame structures before simplifying into them.

### 28. Wrong-color bishop endgame

You traded into an endgame where your remaining bishop is the wrong colour to control the promotion square of your passed pawn. Often combined with drawn-but-played-on. Drilling pattern: pre-trade endgame projection.

### 29. Technique error in K+P endgame

A specific technique (Lucena, Philidor, square-of-the-pawn, key-square calculation) was available and known to be winning, but the technique wasn't executed correctly. Drilling pattern: drilling the specific technique that failed.

### 30. Technique error in R+P endgame

Same as the K+P version but for rook endgames — the technique (Lucena bridge, Philidor third-rank defence, short-side defence) was the right one but executed incorrectly. Drilling pattern: rook-endgame technique-specific repetition.

## How the catalogue maps to training

Each motif maps to exactly one of the five skill buckets (the dimension it appears under above). When Chessful flags a motif in one of your games, the corresponding skill bucket gets a flag. The spaced-repetition queue pulls from the flagged buckets — most-recently-flagged first, with Leitner-schedule intervals between repeats.

The reason the bucket layer exists between motif detection and the training queue is that **patterns generalise within a skill dimension better than they generalise across dimensions**. If you keep missing forks, drilling more fork puzzles is the right intervention. If you alternate between missing forks and misjudging endgame opposition, those are different cognitive failures and need to be drilled separately — not bundled into a generic "tactics-and-endgame practice" queue.

That's the whole reason for skill dimensions. They aren't display categories; they're the level at which spaced repetition is scheduled.

## What's not in the catalogue (and why)

A few things Chessful explicitly does not detect:

- **Time-pressure tactics.** A blunder under thirty seconds on the clock often isn't a pattern problem — it's a time-management problem. Chessful flags it as `time-on-the-clock-on-the-wrong-move` (motif 20) rather than as a tactical failure, because drilling tactics doesn't fix time pressure. Drilling time budgeting does.
- **Move-order subtleties in deeply theoretical lines.** If you're playing the Najdorf Poisoned Pawn variation and miss a move-20 nuance, Chessful flags it as `repertoire drift` rather than as a positional or tactical motif. The correct intervention is opening study, not pattern drilling.
- **Psychological mistakes.** Resigning prematurely, accepting a draw in a winning position, playing too aggressively when ahead — Chessful doesn't try to detect these because they're hard to disambiguate from objective mistakes from engine output alone.

These exclusions aren't oversights; they're the cases where motif-based drilling isn't the right intervention, and where Chessful would mislead the user by pretending otherwise.

## How the catalogue evolves

The catalogue isn't frozen. Two things change between app versions:

- **New motifs get added** when a recurring mistake pattern appears in user games that the existing rules don't catch cleanly. The most recent addition (v1.4) was `weakening pawn push without compensation` — previously folded into king-safety underestimate, split out because the drilling patterns are genuinely different.
- **Existing motifs occasionally get split or merged** when one category is doing too much work, or when two categories rarely produce distinct training value. Splits and merges are conservative — they only happen when the resulting training queue would meaningfully differ.

All changes are logged in the app's changelog with the motif name and the version. The spaced-repetition queue doesn't reset on a taxonomy change — flagged positions migrate to the closest equivalent motif under the new taxonomy.

---

The catalogue above is what Chessful is currently looking at when it tells you "you played Nxd5; the knight was your only back-rank defender." That sentence is the surface; the motif label underneath it is `defender-removal blindness`; the bucket it flags is `Defense`; the next training session draws from that bucket using spaced repetition.

The whole machine is open to inspection. That's the point of publishing it.

[Chessful is available on the App Store.](https://apps.apple.com/app/id6761336870) The methodology behind the catalogue is documented in [How Chessful turns a Stockfish evaluation into adaptive training](/journal/how-chessful-builds-adaptive-training/). The companion design note on the forty AI opponents is at [Forty chess opponents, and none of them are me](/journal/forty-chess-opponents/).
