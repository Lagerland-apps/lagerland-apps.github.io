---
layout: journal
slug: engine-depth-at-club-level-tune-down
title: "Why engine depth at club level should be tuned down, not up"
seo:
  title: "Chess Engine Depth: Why Club Players Should Tune It Down"
  description: "Chess.com runs depth 22, Stockfish hits 35 — none of it helps an 800–1800 player. Why deeper engine analysis makes club-level feedback worse, not better."
  keywords:
    - "chess engine depth"
    - "stockfish depth"
    - "how good is stockfish"
    - "chess analysis depth"
    - "club level chess analysis"
    - "stockfish for beginners"
date: 2026-05-13
lede: "Every chess app boasts about engine depth. Chess.com's analysis runs to depth 22. Lichess Cloud reaches 28. Stockfish on a modern desktop will happily run depth 35 if you let it. This post is about why none of that helps an 800–1800 rated player improve, and why Chessful intentionally caps engine depth at the level where the mistakes that actually decide club games become visible — and not deeper."
quick_answer: "Engine depth above roughly 13-15 ply produces lines that even strong club players cannot read or apply. The lines are correct but unteachable. For a player rated 800-1800, the mistakes that actually decide games are visible at depth 10-15 — hung pieces, missed forks, defender-removal blindness, opposition errors. Deeper analysis surfaces grandmaster-level subtleties that the user cannot act on and that crowd out the actionable signal. Chessful tunes engine depth down to the band where the actionable mistakes live, which has the side-effect of running analysis fast on-device. The choice is pedagogic, not a hardware constraint."
faq:
  - q: "Why does Chessful run Stockfish at lower depth than Chess.com or Lichess?"
    a: "Because deeper engine analysis produces lines club players cannot read or apply. At depth 25+, Stockfish surfaces seven-move forcing sequences that even 2000-rated players miss. Showing them to an 1400-rated player is noise — the player cannot act on the information, and it crowds out the actionable mistakes at depth 12-15 (hung pieces, missed forks, opposition errors) that the player can fix. Chessful caps depth at the band where the mistakes that actually decide club games become visible — and not deeper. The choice is pedagogic, not a hardware constraint."
  - q: "Is Chessful's analysis less accurate than Chess.com's?"
    a: "Accuracy and depth aren't the same thing. Chessful's analysis is correct (Stockfish is correct at depth 13 in the same sense it is correct at depth 33 — the evaluation may differ, but neither is wrong). The question is which evaluation is useful. For a club player, depth 13-15 is the evaluation horizon where their decisions actually live. Chess.com's depth 22 analysis is more accurate in the absolute sense, but the additional accuracy describes positions the player can't reach from where they are."
  - q: "Doesn't deeper analysis help me find the strongest move?"
    a: "Not at club level. At depth 25, the engine's preferred move is often a quiet positional move whose advantage doesn't materialise for 12 plies. A player who can't see that material gain doesn't gain anything from being shown the move — they can't justify it to themselves, can't generalise it to similar positions, and won't repeat it. The pedagogically right move is the one that wins material or stops a threat within the player's calculation horizon. That move is usually visible at depth 13."
  - q: "When does deeper engine analysis become useful?"
    a: "Roughly around 2000+ rated play, where forcing sequences of 5-7 plies become routinely calculable and the relevant decisions move into the 6-12 ply horizon. At that level, the user can read longer engine lines and apply them. For Chessful's target audience (800-1800), capping at lower depth gives a faster, cleaner training signal."
  - q: "Does running Stockfish at lower depth save battery on iPhone?"
    a: "Yes — substantially. Stockfish CPU cost grows roughly geometrically with depth (each additional ply explores 4-5× more nodes). Running at depth 13 versus depth 25 is the difference between analysing a game in two seconds and analysing it in two minutes. Battery cost scales with that. But that's a side-effect of the pedagogic choice, not the reason for it. If deeper analysis produced better training for club players, Chessful would run deeper and accept the battery cost. It doesn't, so we don't."
mentioned_apps:
  - chessful
read_time: "8 min read"
excerpt: "Every chess app boasts about engine depth. Chessful intentionally caps it. The argument: above depth 15, you get lines that even strong club players cannot read or apply — correct but unteachable. The mistakes that actually decide club games are visible at depth 13."
---

Every chess app boasts about engine depth. Chess.com's *Game Review* runs Stockfish to depth 22. Lichess's cloud analysis offers depth 28. Stockfish on a modern desktop will happily run depth 35 if you give it the time.

Chessful runs Stockfish considerably shallower than any of them — and not because it has to, but because, for the players Chessful is built for, deeper analysis makes the training worse.

This post is the argument. It's a contrarian position to take in chess software, where "depth" is treated as a quality metric the way "horsepower" is in cars. The position is that, below roughly 2000 rating, **engine depth above 15 ply produces lines that the user cannot read or apply** — correct lines, but unteachable ones. The mistakes that actually decide games at 800-1800 are visible at depth 10-15. Deeper analysis surfaces subtleties that crowd out the actionable signal.

It's a pedagogic choice with a measurable side-effect (analysis runs fast on-device, which makes the iPhone-iPad-Mac on-device promise possible). But the pedagogy comes first.

## What "engine depth" actually means

In chess engine terminology, *depth* is the number of half-moves (plies) the engine looks ahead. Depth 13 means the engine evaluates positions assuming both players will play their best moves for the next 13 ply (roughly 6 full moves for each side, give or take). Depth 25 means roughly 12 full moves of look-ahead.

Each additional ply expands the search tree by a factor of roughly 4-5 (the *branching factor* of chess after pruning). Going from depth 13 to depth 25 is not a doubling of work — it's something like 10,000-50,000× more work. Modern engines mitigate this with alpha-beta pruning, transposition tables, and aggressive heuristics, but the underlying cost growth is the reason cloud analysis exists at all: most depth-25 analyses are too expensive to run on a phone.

The reason Chess.com and Lichess can offer depth 22-28 is that they run the analysis in the cloud, on rented compute, and return the result. The trade-off is the cloud round-trip (and, in Chess.com's case, a daily quota gating the deep analyses).

Chessful runs Stockfish on-device. The trade-off is the hardware constraint — an iPhone has roughly 1/50th of the compute of a desktop, and aggressive deep analysis on a phone is slow enough to be unusable.

This is where most people stop the reasoning. The argument tends to be: "Chessful runs shallower because it has to; Chess.com / Lichess run deeper because they can." Phrased like that, deeper is better and Chessful is making the best of a hardware limitation.

But that argument is wrong, and not just slightly — it's wrong in a load-bearing way that determines whether the training the app produces actually helps you improve. The real argument runs the other direction.

## What club players can read

Take a specific example. Imagine a position from a 1400 vs 1400 club game, move 18. The user has just played `Bd3`, intending to bolster the kingside. Stockfish evaluates this position.

At **depth 12**, Stockfish reports: `eval -1.4. Best move: Qe2. Line: Qe2 Nf4 Bxf4 Qxf4 Rxe6.` The line is five plies long. The user can read it: queen to e2 defends, knight comes in, bishop trades, queen recaptures, rook lifts to take on e6. The five-move sequence is within calculation reach for a 1400 player. They can see why Qe2 was right (it stops Nf4 from being effective), they can play through the line on a board, they can generalise it to "when the e-file is open and the queen is exposed, develop the queen toward the defence."

At **depth 22**, Stockfish reports: `eval -1.9. Best move: Re1. Line: Re1 Nf4 Bxf4 Qxf4 Re5 Qg4 h3 Qxd1+ Kh2 Qxa1 Re8+ Rxe8 Qxa1`. The line is 13 plies long. It begins with a quiet rook move whose payoff materialises ten moves later as a queen trade. The 1400 player cannot read this line. They cannot calculate to move 13 in their head; they cannot, by playing through it on a board, see why Re1 is the *right* move rather than the longer Qe2 line that the depth-12 engine recommended.

Both engine recommendations are correct. The position evaluation differs (-1.4 vs -1.9), but neither evaluation is wrong — they're both Stockfish reading the position to their respective horizons. The question is which one is useful pedagogically.

For the 1400 player, the depth-12 line **teaches them something** about defensive piece placement. The depth-22 line teaches them that the engine knows better than they do, which they already knew, and which doesn't generalise to anything they can carry into the next game.

This is the central pedagogic claim: **at club level, engine depth beyond what the user can calculate is noise, not signal.**

## Why the noise actively harms training

It's not just that deeper analysis doesn't help. It's that deeper analysis actively crowds out the help that's available.

Suppose the depth-22 analysis flags `Re1` as the best move and rates the user's `Bd3` as a "blunder" (since the eval difference is greater than the platform's blunder threshold). Suppose the depth-12 analysis flags `Qe2` as the best move and rates the user's `Bd3` as a "mistake" (smaller eval drop, since the comparison is to a shorter calculation horizon).

The depth-12 verdict is actually more useful. `Bd3` was a defensive misjudgement that the user can recognise and drill — they failed to see the importance of getting the queen to e2 before letting `Nf4` get in. That's a defender-placement motif. Drillable. Carry-able.

The depth-22 verdict is technically correct but produces no training. "You should have played `Re1` for a 13-move forcing sequence" is not a lesson the player can internalise. It's a fact about the position that has no behavioural consequence.

If you train a player on depth-22 analyses, they learn to nod at engine output and accept that the engine sees further than they do. They don't learn to play better moves themselves. The accuracy of the engine becomes a substitute for the development of their own calculation.

## What the right depth is

For Chessful's audience (800-1800 rating range), depth 12-15 is the band where:

1. The engine's recommendations are short enough to be calculable by a careful club player.
2. The mistakes the engine flags (hung pieces, missed tactics, defender-removal blindness, prophylactic skips, opposition errors) are the mistakes that actually decide games at this level.
3. The training drills derived from the analysis target patterns the player has any realistic chance of recognising in their next game.

At depth 13 specifically, Stockfish reliably finds:
- **All hung pieces** (depth 2-3 is enough).
- **All one-move tactics** (forks, pins, skewers): depth 3-5.
- **All two-move forcing sequences** (most tactical combinations club players miss): depth 7-9.
- **Most three-move forcing sequences** (the long end of club-level tactical horizon): depth 11-13.
- **Defensive misjudgements with consequences materialising in 3-5 plies**: depth 10-13.

Depth 13 covers the entire calculation horizon of a typical club player's actual play. Going deeper finds *additional* mistakes — but those mistakes are also additional things the player cannot fix.

The trade-off lives at the top of the club-player range. Around 1800-2000, players begin to read longer engine lines reliably, and the right depth starts creeping up. By 2200, deeper analysis is genuinely useful. By 2400, players want depth 30+ because they actually can use it.

Chessful's audience is below that band. Depth 13-15 is where the mistakes live.

## The hardware side-effect

Running Stockfish at depth 13 on an iPhone is fast. A modern A-series chip will produce the analysis in roughly 0.5-2 seconds per move on a typical mid-game position. A full 50-move game analyses in 30-90 seconds. That's well within "I closed the app and reopened it; it's done" budget.

Running Stockfish at depth 22 on the same phone is slow. The same game would take 5-20 minutes — and the phone would be hot at the end of it. Battery cost is non-trivial.

This is the side-effect of the pedagogic choice. Chessful runs analysis fast on-device because depth 13 is fast on-device. The on-device-only promise (no cloud, no daily quota, no account) is *enabled* by the depth choice, but the depth choice came first.

If depth 22 produced better training for club players, Chessful would run depth 22 and accept the slower analysis and the battery cost — and would probably have to fall back to cloud analysis for older phones, which would compromise the privacy story. The reason that didn't happen isn't that the privacy story is more important than the training; it's that depth 22 doesn't produce better training. The pedagogic choice and the privacy story both happen to point the same direction.

## What deeper analysis is useful for

This isn't an argument against deep engine analysis in general. Deep analysis is useful for:

- **Players above 2000 rating**, where calculation horizons extend into the 6-12 ply range.
- **Opening preparation**, where you're trying to identify objectively best moves in book positions you'll see again.
- **Correspondence chess**, where the time control allows the player to actually work through engine lines.
- **Engine vs engine games**, where the goal is engine accuracy rather than human improvement.
- **Theoretical exploration**, where the question is "what is the truth of this position" rather than "what should this player do next."

For club-level improvement training, none of these apply. The training goal is to fix the patterns the player gets wrong in actual games. Those patterns are visible at depth 13. Deeper analysis surfaces additional patterns the player cannot act on.

The mainstream chess software industry has settled on "more depth = better app" partly because depth is a metric that's easy to compete on (just rent more cloud compute), and partly because the most visible chess players (titled players, streamers, content creators) actually can use deeper analysis and praise it accordingly. The metric became a marketing claim before anyone asked whether it served the median user.

Chessful's bet is that the median user is served better by training they can read.

---

[Chessful is available on the App Store.](https://apps.apple.com/app/id6761336870) The full training methodology — including how Stockfish output gets translated into motif classifications and spaced-repetition drilling — is documented in [How Chessful turns a Stockfish evaluation into adaptive training](/journal/how-chessful-builds-adaptive-training/). The complete catalogue of the 30 mistake motifs the analyser flags is documented in [The 30 chess mistake motifs Chessful detects](/journal/30-chess-mistake-motifs/).
