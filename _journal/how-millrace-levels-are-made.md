---
layout: journal
slug: how-millrace-levels-are-made
title: "Sixty-four levels, none written by hand: how Millrace finds and proves its puzzles"
date: 2026-09-24
last_updated: 2026-10-26
seo:
  title: "How Puzzle Levels Are Generated and Verified: Millrace"
  description: "How Millrace's 64 puzzle levels are generated and verified: found by search, solved exhaustively, and discarded if any of 280 thoughtless strategies wins."
  keywords:
    - puzzle level generation
    - how are puzzle levels made
    - procedural puzzle generator
    - breadth-first search puzzle solver
    - verified puzzle difficulty
    - tile delivery puzzle
    - millrace levels
    - millrace
lede: "I didn't write any of Millrace's 64 levels. A generator proposed them, an exhaustive solver measured each one, and a gate in the test suite threw away all but a few candidates in every thousand. This is how that works, and what an earlier version of this game's puzzle mode taught me about why it has to."
quick_answer: "Millrace's 64 levels are found by search, not written by hand. A generator proposes candidate boards (a starting grid, a queue of arriving 2s and 4s, one inlet, and one vault with an exact target), and an exhaustive breadth-first solver measures each candidate's true shortest solution. A level ships only if it passes sixteen automated checks, including: it is solvable and its stated shortest solution is the proven one; its depth matches its chapter (exactly 5, 6, 7, 8 or 9 moves, then 10 or more); none of 280 no-lookahead strategies can win it; random play wins at most 2% of the time, computed exactly; and it is not the same board as any other level under rotation, reflection or relabelled tile values. Roughly one to eight candidates in a thousand survive. The checks run in the test suite, so a level that stops passing fails the tests by name."
faq:
  - q: "How are Millrace's levels made?"
    a: "By search. A generator proposes random candidates (a board, a vault cell with an exact target, a single inlet chosen from edge cells the opening slides cannot fill, and a queue of 2s and 4s), and an exhaustive breadth-first solver measures each one's shortest solution. Any candidate whose depth doesn't match the chapter being filled, or that fails any of the gate's sixteen checks, is thrown away. Depending on the chapter, roughly one to eight candidates in a thousand survive."
  - q: "What does 'Best possible is X moves' mean on the result card?"
    a: "It is the level's proven shortest solution. Every level is solved exhaustively by breadth-first search over its whole state graph, and the first win that search reaches is provably the minimum; the test suite checks that the number stored with the level equals that result. The line appears only when you used more moves than necessary. It is never an estimate or a target someone typed in."
  - q: "Can every Millrace level be won, and can I lose on the first move?"
    a: "Every level has a proven solution within its move budget, and nothing in a level is random, so no level depends on luck. The gate also requires that every legal first move leaves the level still winnable, so move one is always free, while some later line must be able to lose it. A puzzle needs a way to go wrong."
  - q: "Why can't a simple strategy beat Millrace's levels?"
    a: "Any level a simple strategy can win is thrown away before it ships. Each candidate is played by 280 deterministic policies that never look beyond the move in front of them: one direction forever, fixed cycles, fixed priority orders, greedy play on score, empty cells or biggest tile under all 24 tiebreak orders, and rule-aware players that keep the inlet clear, avoid losing on this move, herd the biggest tile to a corner or chase the target onto the vault. All 280 must fail. Looking two moves ahead is deliberately left out of the battery, because that is the skill the levels teach."
  - q: "Why does Millrace show the arriving tiles in advance?"
    a: "A visible, authored queue keeps every position a pure function of the moves played. That makes it possible to prove a level's shortest solution and to compute random play's exact odds of winning. With random arrivals, the best possible solution would depend on tiles nobody has drawn yet. The solver knows exactly what the player knows."
  - q: "How hard do Millrace's levels get?"
    a: "Each of the six chapters is one move deeper than the last: every Warm-up level has a shortest solution of exactly 5 moves, Tactics 6, Pressure 7, Precision 8, Deep Water 9, and Mastery 10 to 16. The deepest level needs 16 moves and allows exactly 16. On the deepest boards, a player choosing moves at random wins about once in a million attempts."
mentioned_apps:
  - millrace
read_time: "8 min read"
excerpt: "Millrace's launch-day design essay: how a search-based generator, an exhaustive breadth-first solver and a sixteen-check gate in the test suite produce 64 levels whose shortest solutions are proven, whose difficulty is measured, and which no thoughtless strategy can win."
---

A puzzle level is real when thinking is the only way through it. Checked by machine, that idea turns into a list of testable properties. Every one of the 64 levels in [Millrace](/apps/millrace/), a tile-delivery puzzle, was found by search, and none ships unless all five of these hold:

1. It is solvable within its move budget.
2. Its shortest solution is known exactly. A breadth-first search walks the level's entire state graph, and the first win it reaches is provably the minimum. The game calls that number the best possible; my own estimate plays no part.
3. No thoughtless strategy wins it. 280 strategies that never look beyond the move in front of them play it through. If one wins, the level is gone.
4. Random play almost never wins. The exact odds are computed (no sampling), and above 2% the level is gone.
5. It is not another level in disguise, whether rotated, reflected or with its tile values relabelled.

Those five head a list of sixteen numbered checks. The others keep levels fair: move one can never lose, some later line always can, a blocked inlet must be a reachable loss, the budget allows at most two spare moves, and there must be at least ten winning lines. So there are many routes through each level, and none of them is a dumb one. The chapters make one check visible:

| Chapter | Levels | Shortest solution (moves) | Move budget |
|---|---|---|---|
| Warm-up | 4 | exactly 5 | 7 |
| Tactics | 12 | exactly 6 | 8 |
| Pressure | 12 | exactly 7 | 8-9 |
| Precision | 12 | exactly 8 | 9-10 |
| Deep Water | 12 | exactly 9 | 9-11 |
| Mastery | 12 | 10 to 16 | 12-16 |

## What the earlier puzzle mode got wrong

An earlier version of this game's puzzle mode shipped 22 puzzles, and a test confirmed each had a solution. When I finally solved all 22 exhaustively, the mean shortest solution was 1.91 moves. "Up, then left" solved 19 of them. Random play won at least 98% of the time on 20, and even the hardest fell to it two times in three. One could not be lost by any legal sequence. Nine were the same board with different numbers printed on the tiles.

The cause was structural. Nothing arrived on those boards, so every move made the position easier, and every goal was monotone: once reached, nothing could undo it. No position could be ruined, and a puzzle needs a way to go wrong. The test only asked whether a solution existed, which sets a floor and no ceiling.

## Why greedy-friendly goals fail

I assumed the old goals only needed a failure rule. Of 400 forged candidates for "clear the board down to N tiles", 215 reached the target depth and none passed. Of 400 for "reach a tile of at least T", 100 reached it and none passed. "Deliver an exact value to a marked cell" passed readily.

The reason is almost embarrassing once written down. A goal that a one-move greedy metric directly optimises can never be a puzzle. A player who grabs the most empty cells *is* pursuing the clearing goal; one who grabs the biggest tile *is* pursuing the reach goal. The clearing goal fell to the dumbest strategies in the battery: one direction over and over, or a fixed cycle.

Delivery survives because it can be lost twice over. The target must rest on one cell, so sliding it off loses it. It must also be an exact value, so merging past it (building a 128 when the level asked for a 64) loses it for good. No local score approximates either condition. Millrace has exactly one kind of goal because the measurements left only one.

## Why you can see every tile before it arrives

The other half of the fix is the arrival queue. Tiles, only 2s and 4s, enter one at a time through a single inlet on the board's edge. If the inlet is occupied when the next one is due, the run ends. That brings back the tension a slide-and-merge board depends on, because it fills while you merge.

Chance stays out. The queue is authored and always on screen, so every position is a pure function of the moves played, with at most four moves from each. With random arrivals, "the shortest solution" isn't a number, since it depends on tiles nobody has drawn, and a solver can only average over futures. With a visible queue there is nothing to average, and breadth-first search is the exact model. The gate knows exactly what you know.

## How a candidate level is generated

The generator is simple, and the rigour sits in the gate. A candidate gets a vault on an edge cell (never a corner, which would be marked twice) and a scatter of tiles from 2 to 32. The inlet is chosen last, from edge cells no opening slide can fill; when it was picked first, most candidates buried their own inlet on move one. The target is one or two doublings above the biggest starting tile, followed by a queue of 2s and 4s. A candidate whose tiles cannot sum to the target is dropped before any search runs.

The solver measures the true shortest solution under the gate's most generous budget, 16 moves, and the candidate stays only if that depth is what the chapter demands. It tries two spare moves, then one, then none, keeping the kindest budget that passes. Depending on the chapter, roughly one to eight candidates in a thousand make it.

## 280 thoughtless players, and one random one

The battery in the middle of the gate has 4 policies that push one direction until they can't, 60 that cycle through two, three or four directions, 24 fixed priority orders, 72 greedy players chasing points, empty cells or the biggest tile under all 24 tiebreak orders, and 120 that know the rules. Those last ones keep the inlet clear, keep it clear then score, avoid losing on this move, herd the biggest tile to a corner, or chase the target onto the vault, again under all 24 orders. Each is deterministic, so one playthrough counts as a proof. A level ships only if all 280 fail.

The battery's first version was circular. Its 70 policies never looked at the inlet, so "none of them solves it" only meant "players who ignore the inlet die to the inlet". Adding rule-aware players broke six of the eight puzzles that had passed it.

The line sits at one move on purpose. Looking two moves ahead (where will the next arrival land?) isn't thoughtless, and it is the skill the levels teach. The gate certifies that the content has depth; it doesn't assume you can't think. [How to plan moves ahead in Millrace](/journal/how-to-plan-moves-ahead-in-tile-puzzles/) shows that lookahead in play, with Level 1 worked move by move.

Chance gets the same treatment. The move budget makes each level's state graph finite and loop-free, so a random player's odds are computed exactly by a memoised walk instead of a simulation. The ceiling is 2%, Warm-up included. Across the 64 levels the odds run from about one in a million on the deepest boards to 1.31% on Level 1, with the median near one in a thousand.

Finally, no two levels may share a canonical form: tile values replaced by rank, then the smallest of the eight rotations and reflections of board, inlet, vault and queue together. That check exists because of those nine identical boards.

## Why the gate lives in the test suite

The sixteen checks live in the test target and run every time, not once. The generator filters with the same functions, and the suite asserts each property over the shipped library, so a level that stops passing fails the tests and names the property that broke. A search that runs out of budget fails too, since an unproven level can't ship. The gate also has to prove itself: a board from the earlier library is kept as a fixture, and the suite fails if it ever gets through. Re-proving all 64 levels takes just under a hundred seconds. Tare's balance puzzles are built by hand, but they pass the same kind of gate; [here is how it proves all 80](/journal/how-to-solve-balance-puzzles/).

The Hint inside a level runs the same solver, so the two cannot drift apart, and one check plays every level on the hint alone: it must win in exactly the shortest number of moves. For [Chessful's forty opponents](/journal/forty-chess-opponents/), difficulty was a matter of character. Here it had to be a number the tests check.

## What you see of it

Almost none of this is on screen.

- The chapter is the depth. Every Tactics level can be solved in six moves and no fewer; every Deep Water level, in nine. In chess, depth is an engine setting, and [more of it doesn't help a club player](/journal/engine-depth-at-club-level-tune-down/). Here it is a measured property of the board.
- The budget is tight. The deepest level needs all 16 of its 16 moves.
- The result card says "Solved in N moves", and if you used more, "Best possible is X moves", where X is the proven minimum.
- A loss can say when it happened. After a failed run, the card can name the move where the position became unwinnable. It only does so afterwards, because a live warning turns a level into trial and error, and you reach the answer having understood nothing.

Millrace is free on iPhone and iPad; the [app page](/apps/millrace/) has the rules and the privacy details. If a level ever feels impossible, somewhere in its graph is a line exactly as long as the card says, and the tests have walked it.
