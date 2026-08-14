---
layout: journal
slug: reading-a-shogi-engine-evaluation
title: "How to read a shogi engine evaluation (and why it is not a chess centipawn)"
seo:
  title: "Shogi Engine Evaluation: What the Number Actually Means"
  description: "Shogi engine evaluation explained: what a YaneuraOu number means, the bands club players need, why shogi evals swing harder than chess, and mate scores."
  keywords:
    - "shogi engine evaluation"
    - "yaneuraou explained"
    - "what does the shogi eval number mean"
    - "shogi analysis app"
    - "shogi evaluation value"
    - "shogi vs chess engine"
    - "shogi mate score"
    - "shogi pieces in hand value"
date: 2026-06-23
lede: "A chess player opens a shogi analysis for the first time, sees +1800, and divides by a hundred out of habit. The arithmetic almost works — a YaneuraOu pawn is 90 points, not 100 — and the conclusion is still wrong, because the same nominal material edge buys far less in a game where captured pieces come back as drops. Here is the whole conversion, band by band."
quick_answer: "A shogi engine evaluation is one number in the engine's own units saying who stands better and by how much, reported from the side to move and usually normalised to Black in a display. In YaneuraOu's default scale a pawn is worth about 90 points, so the useful bands are wide: under 150 is level, 400 to 900 is a clear advantage, past 2000 the game is decided. Shogi numbers swing harder than chess centipawns because a captured piece goes to your hand instead of off the board, so a clean capture counts roughly twice. A mate score is not a magnitude at all — it is a verdict."
faq:
  - q: "What does the evaluation number in a shogi engine mean?"
    a: "It is the engine's estimate of who is better, in its own internal units, at the end of the search it just ran. YaneuraOu's default material table sets a pawn at roughly 90 points, so a reading of +900 is about ten pawns of advantage, not nine. The sign is reported from the side to move under the USI protocol, though most graphical front-ends flip it so that positive always means Black (sente) is better."
  - q: "Is a shogi evaluation the same as a chess centipawn?"
    a: "No, though the per-pawn units are close enough to be a trap. A chess centipawn is nominally one hundredth of a pawn, and modern Stockfish normalises it further so that plus one point means roughly a fifty percent win probability rather than literal material. A shogi eval is an engine-specific integer anchored to a piece table where a pawn is about 90. So the raw integers look interchangeable and are not: a chess front-end divides by a hundred before showing you anything, a shogi front-end prints the integer, and ten pawns of material is a decided chess game but only about an 82 percent shogi position on the standard win-rate curve."
  - q: "What is a good evaluation score in shogi?"
    a: "For a club player: anything under about 150 is level and not worth thinking about, 150 to 400 is a small edge, 400 to 900 is a clear advantage, 900 to 2000 is winning if you can convert, and beyond 2000 the game is decided. Those boundaries are conventions borrowed from Japanese broadcast displays, not physics, and they shift with the engine and its tuning."
  - q: "Why do shogi engine evaluations swing so much?"
    a: "Because of drops. When you capture a piece in shogi it goes to your hand and can be dropped back onto almost any empty square as a whole move. So a clean capture subtracts the piece from your opponent and adds it to you — roughly double the swing of the same capture in chess. Winning a silver moves the number by about 990 points, which in that engine's own scale is eleven pawns."
  - q: "What does score mate mean in a shogi engine?"
    a: "It means the engine has a forced mate and is no longer estimating anything. The USI protocol carries it as score mate N, where N counts the moves to mate and a negative N means you are the one being mated. It is categorical, not a magnitude: mate in eleven is not a worse result than mate in three, only a longer proof. Engines store it internally as a sentinel near the top of their integer range."
  - q: "How deep should shogi engine analysis run for a club player?"
    a: "Deep enough to see the mistake you actually made, and no deeper. Shogi positions offer roughly 80 to 90 legal moves against chess's 35, so extra plies are expensive, and most of what they buy are long drop sequences a club player could never have calculated at the board. The band where hanging pieces, drop forks, wrong promotions and short mating nets appear is the band that produces training you can use."
mentioned_apps:
  - shogiful
  - chessful
read_time: "14 min read"
excerpt: "Shogi evaluation numbers look like chess centipawns and are not. This post gives the band-to-meaning table, the material scale a YaneuraOu number is anchored to, why every capture counts twice because of pieces in hand, and how mate scores read differently."
---

A chess player opens a shogi game record, runs the analysis, and sees the graph spike to **+1800**. They divide by a hundred out of chess habit and read eighteen pawns. Two moves later it is back to +200, and they conclude the engine is broken or the position is insane.

The engine is fine. The position is probably fine too. And the division was almost right, which is the trap: a YaneuraOu pawn is 90 points, so +1800 is nearer twenty pawns than eighteen. What does not carry over is everything the number *implies* — how likely that edge is to hold, and how far a single capture can move it in a game where captured material comes straight back.

This is the conversion table nobody hands you. Reference first; the argument about what an evaluation is *for* sits at the bottom.

## What is a shogi engine evaluation, exactly?

It is a single signed integer that the engine emits at the end of a search, in units it defined for itself. Under USI — the [Universal Shogi Interface](http://hgm.nubati.net/usi.html), adapted from chess's UCI — the engine prints a line containing `score cp <n>` for a positional evaluation or `score mate <n>` when it has found a forced mate.

Two conventions matter before you read a single digit:

**The sign is from the side to move.** USI reports the score from the perspective of whoever is on move in the position being searched. Almost every graphical front-end flips it so that a positive number always means Black (先手, *sente*, the first player) is better. If your numbers seem to alternate sign every ply, you are reading raw engine output, not a normalised display.

**The scale is the engine's, not the game's.** [YaneuraOu](https://github.com/yaneurao/YaneuraOu) — the strongest open-source shogi engine — inherits the material table computer shogi has used since the Bonanza and Apery lineage: a pawn is worth about 90, a rook about 990. The NNUE network that produces the evaluation departs from pure material immediately, but the *scale* stays anchored there. Note how close that is to a chess centipawn: 90 units per pawn against 100. The reason shogi evals *look* like four-digit numbers and chess evals like small decimals is display convention — chess front-ends divide by a hundred before drawing anything, shogi front-ends print the integer. Tunings shift these constants, so if you need them exact, read them in the source rather than trusting a blog.

## What do the evaluation bands mean for a club player?

Japanese broadcast coverage has settled on a rough set of bands, and they translate well to a club player's decisions. The win-probability column comes from the logistic curve computer shogi uses to convert an evaluation to a win rate, `1 / (1 + e^(-eval/600))`. The 600 comes out of win-rate fitting in the elmo and YaneuraOu learning code — a tuning constant, not a law.

| Evaluation (your side) | Rough win probability | What it usually means | What to do with it |
|---|---|---|---|
| 0 to ±150 | 50-56% | Level. Inside the noise of any club game. | Nothing. Do not chase it. |
| ±150 to ±400 | 56-66% | A small edge: a tempo, a better-placed silver, a marginally safer king. | Read the plan, not the number. |
| ±400 to ±900 | 66-82% | A clear advantage. Usually a piece won cleanly, or a castle with a hole in it. | Find the move where it moved. That move is the lesson. |
| ±900 to ±2000 | 82-97% | Winning, if you convert. A major piece up, or an attack already landing. | Study the conversion, not the win. |
| Beyond ±2000 | 97%+ | Decided. The rest is bookkeeping. | Scroll back to where it crossed. |
| `mate N` | 100% | Not a magnitude. A proof. | Solve it yourself before you look. |

Two caveats matter more than the table does. The boundaries are conventions — a different engine, network, or search budget draws them elsewhere, and nobody has a principled reason to prefer 400 over 450. And the win probability is a *machine's*: between two 1200-rated club players, a +1500 position gets thrown away often enough that the number is advice, not a forecast.

## Why do shogi evaluations swing harder than chess centipawns?

Because a captured shogi piece is not removed from the game. It goes to your hand — the *mochigoma* (持ち駒), which sit on the wooden stand beside the board called the *komadai* (駒台) — and from there it can be dropped onto almost any empty square as an entire move.

So a capture is not a subtraction. It is a subtraction *and* an addition, in the same move, and the evaluation moves by roughly the sum of both. Using the default material constants:

| Piece captured | Kanji | Its value to them | Arrives in your hand as | Approx. total swing |
|---|---|---|---|---|
| Pawn | 歩 | 90 | pawn (90) | ~180 |
| Lance | 香 | 315 | lance (315) | ~630 |
| Knight | 桂 | 405 | knight (405) | ~810 |
| Silver | 銀 | 495 | silver (495) | ~990 |
| Gold | 金 | 540 | gold (540) | ~1080 |
| Bishop | 角 | 855 | bishop (855) | ~1710 |
| Rook | 飛 | 990 | rook (990) | ~1980 |
| Tokin (promoted pawn) | と | 540 | **pawn (90)** | ~630 |
| Promoted silver | 成銀 | 540 | **silver (495)** | ~1035 |
| Horse (promoted bishop) | 馬 | 945 | **bishop (855)** | ~1800 |
| Dragon (promoted rook) | 龍 | 1395 | **rook (990)** | ~2385 |

The bolded rows carry the most useful piece of shogi arithmetic: **promoted pieces revert when captured.** A tokin is worth a gold to the player who owns it and only a pawn to the player who takes it. That asymmetry is why building tokin is such a cheap, strong plan, and why losing one hurts you six times more than it helps your opponent.

Now put the numbers together. Winning a silver cleanly moves the evaluation about 990 points, which on the same scale is eleven pawns. In chess, winning a bishop moves you three pawns and you are pleased. In shogi, winning a silver drops you from "level" into the "winning" band in one move. That is not the engine being dramatic. That is the game.

The other half of the answer is what *does not* happen. Chess evaluations calm down because material leaves and positions simplify toward technically drawn endings. Shogi has no such drain. Trades load both komadai and sharpen the position rather than quieting it. Shogi also has no stalemate draw and no draw by insufficient material — the only two draw mechanisms are *sennichite*, the fourfold repetition that gets replayed with colours swapped, and the rare double-entering-king impasse called *jishogi* ([both are laid out on Wikipedia's shogi page](https://en.wikipedia.org/wiki/Shogi)). An eval near zero in shogi means "unclear", not "heading for a draw".

Side by side:

| | Chess (Stockfish) | Shogi (YaneuraOu) |
|---|---|---|
| Unit shown | Centipawns, normalised in [modern Stockfish](https://github.com/official-stockfish/Stockfish) so +1.00 is roughly a 50% win probability | Engine points on a table where a pawn is about 90 |
| Captured material | Leaves the game | Goes to the capturer's hand |
| Swing of a clean capture | About the piece's value | About twice the piece's value |
| Legal moves in a typical middlegame | Roughly 35 | Roughly 80-90 ([game-complexity figures](https://en.wikipedia.org/wiki/Game_complexity)) |
| What ten pawns of material is worth | A decided game | About 82% win probability on the standard curve |
| Effect of trades | Simplification toward drawn endings | Sharpening, with fuller hands |
| Forced mate | `score mate N` | `score mate N`, same protocol shape |

### Why is a piece in hand worth more than the same piece on the board?

The material table gives one value per piece, but the two states are not equal — and the NNUE network, which is not a material table, prices the difference even where the table cannot.

**A piece in hand has no travel time.** A knight on your second rank needs several moves to matter. A knight in hand is already everywhere: it arrives on any legal square in one move.

**It has not committed to anything.** A silver on the board is an argument about one part of the board. A silver in hand is a live threat against every weak square at once, and your opponent has to answer all of them.

**It is not blocking your own pieces**, which is no small thing on a 9x9 board where all nine of your pawns start on one unbroken rank.

The effect is strongest for the two pieces that can only move forward. A lance or a knight stuck behind your own lines is close to dead weight — as [the piece guide explains](/journal/making-shogi-readable-without-kanji/), neither can ever turn around. The same lance in hand drops deep in enemy territory, aimed at a castle. The evaluation reflects that transformation even though the material table does not.

The restrictions are worth memorising, because the engine has already accounted for them and you have not: no two of your unpromoted pawns on one file (*nifu*), no pawn drop that delivers immediate checkmate (*uchifuzume*), and no drop onto a square where the piece would have no legal move.

## What does a mate score mean in shogi?

It means the engine has stopped estimating. `score mate 7` is not "very good", it is "there is a forced mate, and here is the proof, seven moves long". Three consequences follow.

**It is not on the eval scale.** Mate in 11 is not worse than mate in 3. Both are 100%. Engines store mate as a sentinel near the top of their integer range, so a bare five-digit figure in a front-end is a mate flag leaking through as a number, not an evaluation.

**A negative mate score is the one to read.** `score mate -5` means *you* are being mated in five, and it is the most instructive line any shogi engine hands you, because it usually starts with a drop you never considered.

**An engine mate is not a tsume.** [Tsume-shogi](https://en.wikipedia.org/wiki/Tsume_shogi) is a strict problem form: every attacking move must be a check, the defender resists as long as possible, and every piece in hand must be used. An engine's forced mate has none of those constraints. There is also no score at all for *hisshi* (必至), the brinkmate where mate is unavoidable next move but not yet forced by checks — and club games are decided in that gap constantly. The engine shows you a slightly worse number and never mentions that the game was over.

## How much depth does a club player actually need?

I have argued the general case elsewhere: [engine depth at club level should be tuned down, not up](/journal/engine-depth-at-club-level-tune-down/), because analysis deeper than a player can calculate produces lines that are correct and unteachable. Shogi makes that argument stronger in two specific ways.

The first is cost. With roughly 80 to 90 legal moves in a typical position against chess's 35, each extra ply in shogi buys less and costs more. Comparing a shogi "depth 20" with a chess "depth 20" is meaningless: no honest conversion exists.

The second is what the extra plies contain. In chess, deeper search mostly surfaces quiet positional moves whose payoff arrives ten moves later. In shogi it mostly surfaces **longer drop sequences**: five-move nets starting with a pawn dropped on an empty file to be promoted three moves later. Those are exactly the moves a club player had no chance of finding at the board and no chance of generalising afterwards. The mistakes that actually decided your game — the hanging silver, the knight drop that would have forked king and rook, the reflexive promotion, the edge pawn that opened your mino castle — are visible far shallower.

So no ply number here, the way the chess post gives one for Stockfish: the right depth moves with the position, the hardware, and how full the komadai are. Search deep enough to prove the mistake, then stop.

## Where can I get a free shogi engine evaluation?

Say the true thing first. [Lishogi](/alternatives/lishogi/) is free, open source, and genuinely excellent. It runs online play, gives you a server-side analysis that searches harder than any phone will, produces a shareable URL for the game, and — being open source — lets you read exactly what the analysis did rather than trust a description of it. If what you want is *the number*, on a board you can send to someone, that is the answer and it is free. [PiyoShogi](/alternatives/piyoshogi/) is likewise a fine free app with an analysis function and finely graded opponents. The [honest guide to shogi apps for iPhone](/guides/best-shogi-apps-iphone/) covers the rest of the category, [81Dojo](/alternatives/81dojo/) included.

## An evaluation is a verdict without a reason

Everything above teaches you to read a number that, once read, still does not tell you what to do. `-980` is a verdict. It says you are losing and roughly by how much. It does not say *why*, which of your last thirty moves caused it, or what to practise tomorrow. An evaluation graph with a cliff in it is a crime-scene photo with no detective.

Translating verdict into sentence is the whole job of a training app, and it is harder in shogi than in chess, because the chess vocabulary does not carry over. A chess trainer has fork, pin, skewer, back-rank, discovered attack. Shogi needs categories that do not exist in that taxonomy: the drop that would have forked, the promotion that cost you a retreat, the castle brick you removed yourself, the mating race you lost by one tempo. [Shogiful](/apps/shogiful/) builds those from scratch rather than adapting a chess list — missed drop tactic, wrong promotion decision, castle weakness, missed tsume, hanging piece, endgame error — turns each detected mistake into one or two sentences, and generates tomorrow's training from whichever category keeps recurring. YaneuraOu's NNUE network runs on the device, so there is no server, no account, and no server-side rate limit. Free covers two full game analyses and three training puzzles a day; Premium is $1.99/month, $9.99/year, or $19.99 once, and Premium is the tier that raises engine depth and shows multiple candidate lines.

The limitation is the exact flip side of that design. Shogiful leads with the sentence rather than the number, and it has no online human play at all — so if what you wanted was the eval graph itself, deep and shareable, lishogi does it better and free. [Chessful](/apps/chessful/) makes the same trade on the chess side with Stockfish, which is how I know it is a real trade and not a rationalisation: both give up the raw number as the headline in exchange for a sentence you can act on.

## TL;DR

- **A shogi eval is not a centipawn — but the units are close enough to fool you.** YaneuraOu anchors to a table where a pawn is about 90 against a centipawn's 100; shogi front-ends just print the integer instead of dividing. Divide by roughly 90 to get pawns, then stop trusting the comparison: ten pawns is a decided chess game and an 82% shogi position.
- **The bands, for a club player:** under ±150 level, ±150-400 a small edge, ±400-900 a clear advantage, ±900-2000 winning if converted, beyond ±2000 decided. These are display conventions, not physics, and they move with the engine.
- **Every capture counts twice**, because the piece goes to your hand rather than off the board. Winning a silver swings the number by about 990 — eleven pawns' worth. Promoted pieces revert when captured, so a tokin is a gold to its owner and a pawn to its taker.
- **A piece in hand beats the same piece on the board** in most positions: no travel time, no positional commitment, and a live threat against every weak square at once. This is most extreme for the lance and knight, which cannot turn around.
- **A mate score is categorical, not numeric.** Mate in 11 is worth exactly as much as mate in 3, and a negative mate score is the most instructive output a shogi engine produces. An engine mate is not the same as a tsume, and no engine reports hisshi at all.
- **More depth is not more instructive.** Shogi's branching factor makes plies expensive, and what they buy are long drop sequences a club player could never have found. Search deep enough to prove the mistake, then stop.
