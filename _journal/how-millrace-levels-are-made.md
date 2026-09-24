---
layout: journal
slug: how-millrace-levels-are-made
title: "Sixty-four levels, none written by hand: how Millrace finds and proves its puzzles"
date: 2026-09-24
seo:
  title: "How Puzzle Levels Are Generated and Verified — Millrace"
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
lede: "I didn't write any of Millrace's 64 levels. A generator proposed them, an exhaustive solver measured each one, and a gate in the test suite threw away all but a few candidates in every thousand. This is how that works — and what an earlier version of this game's puzzle mode taught me about why it has to."
quick_answer: "Millrace's 64 levels are found by search, not written by hand. A generator proposes candidate boards — a starting grid, a queue of arriving 2s and 4s, one inlet and one vault with an exact target — and an exhaustive breadth-first solver measures each candidate's true shortest solution. A level ships only if it passes sixteen automated checks, including: it is solvable and its stated shortest solution is the proven one; its depth matches its chapter (exactly 5, 6, 7, 8 or 9 moves, then 10 or more); none of 280 no-lookahead strategies can win it; random play wins at most 2% of the time, computed exactly; and it is not the same board as any other level under rotation, reflection or relabelled tile values. Roughly one to eight candidates in a thousand survive. The checks run in the test suite, so a level that stops passing fails the tests by name."
faq:
  - q: "How are Millrace's levels made?"
    a: "By search, not by hand. A generator proposes random candidates — a board, a vault cell with an exact target, a single inlet chosen from edge cells the opening slides cannot fill, and a queue of 2s and 4s — and an exhaustive breadth-first solver measures each one's shortest solution. Any candidate whose depth doesn't match the chapter being filled, or that fails any of the gate's sixteen checks, is thrown away. Depending on the chapter, roughly one to eight candidates in a thousand survive."
  - q: "What does 'Best possible is X moves' mean on the result card?"
    a: "It is the level's proven shortest solution. Every level is solved exhaustively by breadth-first search over its whole state graph, and the first win that search reaches is provably the minimum; the test suite checks that the number stored with the level equals that result. The line appears only when you used more moves than necessary, and it is never an estimate or a target someone typed in."
  - q: "Can every Millrace level be won, and can I lose on the first move?"
    a: "Every level has a proven solution within its move budget, and nothing in a level is random, so no level depends on luck. The gate also requires that every legal first move leaves the level still winnable — move one is always free — while some later line must be able to lose it, because a puzzle needs a way to go wrong."
  - q: "Why can't a simple strategy beat Millrace's levels?"
    a: "Because any level a simple strategy can win is thrown away before it ships. Each candidate is played by 280 deterministic policies that never look beyond the move in front of them: one direction forever, fixed cycles, fixed priority orders, greedy play on score, empty cells or biggest tile under all 24 tiebreak orders, and rule-aware players that keep the inlet clear, avoid losing on this move, herd the biggest tile to a corner or chase the target onto the vault. All 280 must fail. Looking two moves ahead is deliberately left out of the battery — that is the skill the levels teach."
  - q: "Why does Millrace show the arriving tiles in advance?"
    a: "Because a visible, authored queue keeps every position a pure function of the moves played. That is what makes it possible to prove a level's shortest solution and to compute random play's exact odds of winning. With random arrivals, the best possible solution would depend on tiles nobody has drawn yet. The solver knows exactly what the player knows, and nothing more."
  - q: "How hard do Millrace's levels get?"
    a: "Each of the six chapters is one move deeper than the last: every Warm-up level has a shortest solution of exactly 5 moves, Tactics 6, Pressure 7, Precision 8, Deep Water 9, and Mastery 10 to 16. The deepest level needs 16 moves and allows exactly 16. On the deepest boards, a player choosing moves at random wins about once in a million attempts."
mentioned_apps:
  - millrace
read_time: "8 min read"
excerpt: "Millrace's launch-day design essay: how a search-based generator, an exhaustive breadth-first solver and a sixteen-check gate in the test suite produce 64 levels whose shortest solutions are proven, whose difficulty is measured rather than labelled, and which no thoughtless strategy can win."
---

A puzzle level is real when thinking is the only way through it. That sounds like a slogan until you check it by machine; then it becomes a list of testable properties. Every one of the 64 levels in [Millrace](/apps/millrace/), a tile-delivery puzzle, was found by search, not written by hand, and none ships unless all five hold:

1. **It is solvable** within its move budget.
2. **Its shortest solution is known exactly.** A breadth-first search walks the level's entire state graph; the first win it reaches is provably the minimum. That number, not my estimate, is what the game calls the best possible.
3. **No thoughtless strategy wins it.** 280 strategies that never look beyond the move in front of them play it through. If one wins, the level is gone.
4. **Random play almost never wins.** Its exact odds are computed, not sampled. Above 2%, the level is gone.
5. **It is not another level in disguise** — rotated, reflected or with its tile values relabelled.

Those five head a list of sixteen numbered checks. The others keep levels fair: move one can never lose, some later line always can, a blocked inlet must be a reachable loss, the budget allows at most two spare moves, and there must be at least ten winning lines — many roads, no dumb ones. The chapters make one check visible:

| Chapter | Levels | Shortest solution (moves) | Move budget |
|---|---|---|---|
| Warm-up | 4 | exactly 5 | 7 |
| Tactics | 12 | exactly 6 | 8 |
| Pressure | 12 | exactly 7 | 8–9 |
| Precision | 12 | exactly 8 | 9–10 |
| Deep Water | 12 | exactly 9 | 9–11 |
| Mastery | 12 | 10 to 16 | 12–16 |

## An earlier version looked like puzzles

An earlier version of this game's puzzle mode shipped 22 puzzles, and a test confirmed each had a solution. When I finally solved all 22 exhaustively, the mean shortest solution was 1.91 moves. "Up, then left" solved 19 of them. Random play won at least 98% of the time on 20, and even the hardest fell to it two times in three. One could not be lost by any legal sequence. Nine were the same board with different numbers printed on the tiles.

That was structural, not bad luck. Nothing arrived on those boards, so every move made the position easier, and every goal was monotone — once reached, nothing could undo it. No position could be ruined, and a puzzle needs a way to go wrong. The test asked only whether a solution existed: a floor with no ceiling.

## A goal a greedy player can chase is not a puzzle

I assumed the old goals only needed a failure rule. Of 400 forged candidates for "clear the board down to N tiles", 215 reached the target depth and none passed. Of 400 for "reach a tile of at least T", 100 reached it and none passed. "Deliver an exact value to a marked cell" passed readily.

The reason is almost embarrassing once written down: a goal that a one-move greedy metric directly optimises can never be a puzzle. A player who grabs the most empty cells *is* pursuing the clearing goal; one who grabs the biggest tile *is* pursuing the reach goal. What beat the clearing goal were the dumbest strategies in the battery — one direction over and over, or a fixed cycle.

Delivery survives because it can be lost twice over. The target must rest on one cell, so sliding it off loses it; and it must be an exact value, so merging past it — building a 128 when the level asked for a 64 — loses it for good. No local score approximates either condition. That is why Millrace has exactly one kind of goal: a measurement, not a lack of imagination.

## Why you can see every tile before it arrives

The other half of the fix is the arrival queue. Tiles — only 2s and 4s — enter one at a time through a single inlet on the board's edge; if the inlet is occupied when the next one is due, the run ends. That restores the tension a slide-and-merge board lives on: it fills while you merge.

It does not restore chance. The queue is authored and always on screen, so every position is a pure function of the moves played, with at most four moves from each. With random arrivals, "the shortest solution" isn't a number — it depends on tiles nobody has drawn — and a solver can only average over futures. With a visible queue there is nothing to average; breadth-first search is the correct model, not an approximation. The gate knows exactly what you know, and nothing more.

## How a candidate level is generated

The generator is simple; the rigour lives in the gate. A candidate gets a vault on an edge cell (never a corner, which would be marked twice) and a scatter of tiles from 2 to 32. The inlet is chosen last, from edge cells no opening slide can fill — picking it first meant most candidates buried their own inlet on move one. The target is one or two doublings above the biggest starting tile, then comes a queue of 2s and 4s; a candidate whose tiles cannot sum to the target is dropped before any search runs.

The solver measures the true shortest solution under the gate's most generous budget, 16 moves, and the candidate stays only if that depth is what the chapter demands. It tries two spare moves, then one, then none, keeping the kindest budget that passes. Depending on the chapter, roughly one to eight candidates in a thousand make it.

## 280 thoughtless players, and one random one

The battery at the gate's heart: 4 policies that push one direction until they can't; 60 that cycle through two, three or four directions; 24 fixed priority orders; 72 greedy players chasing points, empty cells or the biggest tile under all 24 tiebreak orders; and 120 that know the rules — keep the inlet clear, keep it clear then score, don't lose on this move, herd the biggest tile to a corner, chase the target onto the vault — again under all 24 orders. Each is deterministic, so one playthrough is a proof, not a sample. A level ships only if all 280 fail.

The battery's first version was circular, and it's worth saying so: its 70 policies never looked at the inlet, so "none of them solves it" only meant "players who ignore the inlet die to the inlet". Adding rule-aware players broke six of the eight puzzles that had passed it.

The line sits at one move on purpose. Looking two moves ahead — where will the next arrival land? — isn't thoughtless; it is the skill the levels teach. The gate certifies that the content has depth, not that you can't think.

Chance gets the same treatment. The move budget makes each level's state graph finite and loop-free, so a random player's odds are computed exactly by a memoised walk, not simulated. The ceiling is 2%, Warm-up included. Across the 64 levels the odds run from about one in a million on the deepest boards to 1.31% on Level 1; the median sits near one in a thousand.

Finally, no two levels may share a canonical form: tile values replaced by rank, then the smallest of the eight rotations and reflections of board, inlet, vault and queue together. Those nine identical boards are why.

## Why the gate lives in the test suite

None of this is a script I ran once. The sixteen checks live in the test target; the generator filters with the same functions, and the suite asserts each property over the shipped library, so a level that stops passing fails the tests, naming the property that broke. A search that runs out of budget fails too — unproven is unshippable. And the gate must prove itself: a board from the earlier library is kept as a fixture, and the suite fails if it ever gets through. Re-proving all 64 levels takes just under a hundred seconds.

The Hint inside a level runs the same solver, so the two cannot drift apart, and one check plays every level on the hint alone: it must win in exactly the shortest number of moves. For [Chessful's forty opponents](/journal/forty-chess-opponents/), difficulty was a matter of character; here it had to stop being a feeling and become a number the tests check.

## What you see of it

Almost none of this is on screen, which is the point.

- **The chapter is the depth.** Every Tactics level can be solved in six moves and no fewer; every Deep Water level, in nine. In chess, depth is an engine setting, and [more of it doesn't help a club player](/journal/engine-depth-at-club-level-tune-down/). Here it is a measured property of the board.
- **The budget is tight.** The deepest level needs all 16 of its 16 moves.
- **The result card tells the truth.** "Solved in N moves" — and if you used more, "Best possible is X moves", where X is the proven minimum.
- **A loss can say when it happened.** After a failed run, the card can name the move where the position became unwinnable — only afterwards, because a live warning turns a level into trial and error, and you reach the answer having understood nothing.

Millrace is free on iPhone and iPad; the [app page](/apps/millrace/) has the rules and the privacy details. If a level ever feels impossible, it isn't. Somewhere in its graph is a line exactly as long as the card says, and the tests have walked it.
