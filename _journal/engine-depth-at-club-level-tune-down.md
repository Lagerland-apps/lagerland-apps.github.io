---
layout: journal
slug: engine-depth-at-club-level-tune-down
title: "Why engine depth at club level should be tuned down, not up"
seo:
  title: "Chess Engine Depth: Why Club Players Should Tune It Down"
  description: "Chess engine depth: Chess.com runs 22 and Stockfish hits 35, yet none of it helps an 800 to 1800 player. Why deeper analysis makes club feedback worse."
  keywords:
    - "chess engine depth"
    - "stockfish depth"
    - "how good is stockfish"
    - "chess analysis depth"
    - "club level chess analysis"
    - "stockfish for beginners"
date: 2026-05-13
lede: "Every chess app advertises its engine depth. Chess.com's analysis runs to depth 22. Lichess Cloud reaches 28. Stockfish on a modern desktop will happily run depth 35 if you let it. This post explains why none of that helps an 800 to 1800 rated player improve, and why Chessful deliberately caps engine depth at the level where the mistakes that decide club games become visible, and goes no deeper."
quick_answer: "Engine depth above roughly 13-15 ply produces lines that even strong club players cannot read or apply. The lines are correct, but they can't be taught. For a player rated 800-1800, the mistakes that decide games are visible at depth 10-15: hung pieces, missed forks, defender-removal blindness, opposition errors. Deeper analysis surfaces grandmaster-level subtleties the user cannot act on, and they crowd out the useful signal. Chessful tunes engine depth down to the band where the fixable mistakes live, which also makes on-device analysis fast. The reason is teaching; the hardware is not the constraint."
faq:
  - q: "Why does Chessful run Stockfish at lower depth than Chess.com or Lichess?"
    a: "Because deeper engine analysis produces lines club players cannot read or apply. At depth 25+, Stockfish surfaces seven-move forcing sequences that even 2000-rated players miss. Showing them to a 1400-rated player is noise: the player cannot act on the information, and it crowds out the mistakes visible at depth 12-15 (hung pieces, missed forks, opposition errors) that the player can fix. Chessful caps depth at the band where the mistakes that decide club games become visible, and goes no deeper. The reason is teaching; the hardware is not the constraint."
  - q: "Is Chessful's analysis less accurate than Chess.com's?"
    a: "Accuracy and depth aren't the same thing. Chessful's analysis is correct. Stockfish is correct at depth 13 in the same sense it is correct at depth 33: the evaluations may differ, but neither is wrong. What matters is which evaluation is useful. For a club player, depth 13-15 is the horizon where their decisions actually happen. Chess.com's depth 22 analysis is more accurate in the absolute sense, but the extra accuracy describes positions the player can't reach from where they are."
  - q: "Doesn't deeper analysis help me find the strongest move?"
    a: "Not at club level. At depth 25, the engine's preferred move is often a quiet positional move whose advantage doesn't show for 12 plies. A player who can't see that material gain gets nothing from being shown the move: they can't justify it to themselves, can't generalise it to similar positions, and won't repeat it. The move worth teaching is the one that wins material or stops a threat within the player's calculation horizon, and that move is usually visible at depth 13."
  - q: "When does deeper engine analysis become useful?"
    a: "Roughly around 2000+ rated play, where forcing sequences of 5-7 plies become routinely calculable and the relevant decisions move into the 6-12 ply horizon. At that level, the user can read longer engine lines and apply them. For Chessful's target audience (800-1800), capping at lower depth gives a faster, cleaner training signal."
  - q: "Does running Stockfish at lower depth save battery on iPhone?"
    a: "Yes, substantially. Stockfish's CPU cost grows roughly geometrically with depth (each additional ply explores 4-5× more nodes). Running at depth 13 versus depth 25 is the difference between analysing a game in two seconds and analysing it in two minutes, and battery cost scales with that. The battery saving is a side effect, though. If deeper analysis produced better training for club players, Chessful would run deeper and accept the battery cost. It doesn't, so we don't."
mentioned_apps:
  - chessful
read_time: "8 min read"
excerpt: "Every chess app advertises its engine depth. Chessful deliberately caps it. The argument: above depth 15, you get lines that even strong club players cannot read or apply. They are correct and impossible to learn from. The mistakes that decide club games are visible at depth 13."
last_updated: 2026-10-26
---

Every chess app advertises its engine depth. Chess.com's *Game Review* runs Stockfish to depth 22. Lichess's cloud analysis offers depth 28. Stockfish on a modern desktop will happily run depth 35 if you give it the time.

Chessful runs Stockfish considerably shallower than any of them. It doesn't have to; it does it because, for the players Chessful is made for, deeper analysis makes the training worse.

Here is the argument. It's a contrarian position in chess software, where "depth" is treated as a quality metric the way horsepower is in cars. Below roughly 2000 rating, **engine depth above 15 ply produces lines that the user cannot read or apply.** The lines are correct, and nobody at that level can learn from them. The mistakes that decide games at 800-1800 are visible at depth 10-15, and deeper analysis surfaces subtleties that crowd them out.

The choice has a measurable side effect: analysis runs fast on-device, which is what makes the iPhone, iPad, and Mac on-device promise possible. But the teaching reason came first.

## What "engine depth" actually means

In chess engine terminology, *depth* is the number of half-moves (plies) the engine looks ahead. Depth 13 means the engine evaluates positions assuming both players will play their best moves for the next 13 ply (roughly 6 full moves for each side, give or take). Depth 25 means roughly 12 full moves of look-ahead.

Each additional ply expands the search tree by a factor of roughly 4-5 (the *branching factor* of chess after pruning). Going from depth 13 to depth 25 costs something like 10,000-50,000× more work, far more than double. Modern engines soften this with alpha-beta pruning, transposition tables and aggressive heuristics, but that cost growth is why cloud analysis exists at all: most depth-25 analyses are too expensive to run on a phone.

Chess.com and Lichess can offer depth 22-28 because they run the analysis in the cloud, on rented compute, and send back the result. The cost is the cloud round-trip, plus, in Chess.com's case, a daily quota on the deep analyses.

Chessful runs Stockfish on-device, and its cost is the hardware: an iPhone has roughly 1/50th of the compute of a desktop, and deep analysis on a phone is slow enough to be unusable.

Most people stop reasoning here. The usual version goes: "Chessful runs shallower because it has to; Chess.com / Lichess run deeper because they can." Put like that, deeper is better and Chessful is making the best of a hardware limitation.

That version is wrong, and the error matters, because it decides whether the training the app produces actually helps you improve. The real argument runs the other way.

## What club players can read

Take a specific example. Imagine a position from a 1400 vs 1400 club game, move 18. The user has just played `Bd3`, intending to bolster the kingside. Stockfish evaluates this position.

At **depth 12**, Stockfish reports: `eval -1.4. Best move: Qe2. Line: Qe2 Nf4 Bxf4 Qxf4 Rxe6.` The line is five plies long, and the user can read it: queen to e2 defends, knight comes in, bishop trades, queen recaptures, rook lifts to take on e6. A five-move sequence is within calculation reach for a 1400 player. They can see why Qe2 was right (it stops Nf4 from being effective), play through the line on a board, and generalise it to "when the e-file is open and the queen is exposed, develop the queen toward the defence."

At **depth 22**, Stockfish reports: `eval -1.9. Best move: Re1. Line: Re1 Nf4 Bxf4 Qxf4 Re5 Qg4 h3 Qxd1+ Kh2 Qxa1 Re8+ Rxe8 Qxa1`. The line is 13 plies long. It begins with a quiet rook move that pays off ten moves later as a queen trade. The 1400 player cannot read this line. They cannot calculate to move 13 in their head, and playing through it on a board won't show them why Re1 beats the Qe2 line the depth-12 engine recommended.

Both engine recommendations are correct. The evaluations differ (-1.4 vs -1.9), but neither is wrong; each is Stockfish reading the position to its own horizon. What matters is which one teaches anything.

For the 1400 player, the depth-12 line **teaches them something** about defensive piece placement. The depth-22 line teaches them that the engine knows better than they do, which they already knew, and which gives them nothing to carry into the next game.

That is the central claim: **at club level, engine depth beyond what the user can calculate is noise.**

## Why the noise actively harms training

Deeper analysis does more than fail to help. It crowds out the help that's available.

Suppose the depth-22 analysis flags `Re1` as the best move and rates the user's `Bd3` as a "blunder" (the eval difference is greater than the platform's blunder threshold). Suppose the depth-12 analysis flags `Qe2` as the best move and rates `Bd3` as a "mistake" (a smaller eval drop, since the comparison is to a shorter calculation horizon).

The depth-12 verdict is the more useful one. `Bd3` was a defensive misjudgement the user can recognise and drill: they missed the importance of getting the queen to e2 before letting `Nf4` in. That's a defender-placement motif, and it can be drilled and carried into the next game.

The depth-22 verdict is technically correct and produces no training. "You should have played `Re1` for a 13-move forcing sequence" is not a lesson the player can absorb. It's a fact about the position that changes nothing about how they play.

Train a player on depth-22 analyses and they learn to nod at engine output and accept that the engine sees further than they do. They don't learn to find better moves themselves. The engine's accuracy ends up replacing the development of their own calculation.

## What the right depth is

For Chessful's audience (800-1800 rating range), depth 12-15 is the band where:

1. The engine's recommendations are short enough for a careful club player to calculate.
2. The mistakes the engine flags (hung pieces, missed tactics, defender-removal blindness, prophylactic skips, opposition errors) are the ones that decide games at this level.
3. The drills built from the analysis target patterns the player has a realistic chance of recognising in their next game.

At depth 13 specifically, Stockfish reliably finds:
- **All hung pieces** (depth 2-3 is enough).
- **All one-move tactics** (forks, pins, skewers): depth 3-5.
- **All two-move forcing sequences** (most tactical combinations club players miss): depth 7-9.
- **Most three-move forcing sequences** (the long end of a club player's tactical horizon): depth 11-13.
- **Defensive misjudgements whose consequences show up within 3-5 plies**: depth 10-13.

Depth 13 covers the whole calculation horizon of a typical club player's actual games. Going deeper finds *additional* mistakes, and those are also mistakes the player cannot fix.

The balance shifts at the top of the club range. Around 1800-2000, players start to read longer engine lines reliably, and the right depth creeps up. By 2200, deeper analysis is genuinely useful. By 2400, players want depth 30+ because they can use it.

Chessful's audience is below that band, and for them the mistakes live at depth 13-15.

Puzzle design uses the same idea in the other direction, with depth as the measure of what a player can use: in Millrace, every chapter is pinned to an exact shortest-solution depth, from five moves to ten or more, and [the levels are generated and verified by search](/journal/how-millrace-levels-are-made/) to guarantee it.

## The hardware side effect

Running Stockfish at depth 13 on an iPhone is fast. A modern A-series chip produces the analysis in roughly 0.5-2 seconds per move on a typical middlegame position. A full 50-move game analyses in 30-90 seconds, comfortably inside the "I closed the app and reopened it and it's done" budget.

Running Stockfish at depth 22 on the same phone is slow. The same game would take 5-20 minutes, the phone would be hot by the end, and the battery cost is real.

So the speed follows from the teaching choice. Chessful's analysis is fast on-device because depth 13 is fast on-device. The on-device-only promise (no cloud, no daily quota, no account) is *enabled* by the depth choice, but the depth choice came first.

If depth 22 produced better training for club players, Chessful would run depth 22 and accept the slower analysis and the battery cost. It would probably also have to fall back to cloud analysis on older phones, which would weaken the privacy story. That didn't happen because depth 22 doesn't produce better training; the privacy story was never ranked above the training. The teaching choice and the privacy story happen to point the same way.

## What deeper analysis is useful for

Deep engine analysis has real uses:

- **Players above 2000 rating**, whose calculation horizons extend into the 6-12 ply range.
- **Opening preparation**, where you want the objectively best moves in book positions you'll see again.
- **Correspondence chess**, where the time control lets the player actually work through engine lines.
- **Engine vs engine games**, where the goal is engine accuracy, and human improvement doesn't come into it.
- **Theoretical exploration**, where the question is "what is the truth of this position" and not "what should this player do next."

None of these apply to club-level improvement. That training aims to fix the patterns the player gets wrong in actual games, and those patterns are visible at depth 13. Deeper analysis adds patterns the player cannot act on.

The chess software industry settled on "more depth = better app" for two reasons. Depth is an easy metric to compete on (rent more cloud compute). And the most visible chess players, titled players, streamers and content creators, can use deeper analysis and praise it accordingly. The metric became a marketing claim before anyone asked whether it served the median user.

Chessful is betting that the median user is better served by training they can read.

---

[Chessful is available on the App Store.](https://apps.apple.com/app/id6761336870) The full training method, including how Stockfish output becomes motif classifications and spaced-repetition drills, is in [How Chessful turns a Stockfish evaluation into adaptive training](/journal/how-chessful-builds-adaptive-training/). The complete catalogue of the 30 mistake motifs the analyser flags is in [The 30 chess mistake motifs Chessful detects](/journal/30-chess-mistake-motifs/).
