---
layout: journal
slug: how-millrace-levels-are-made
title: "Sixty-four levels, none written by hand: how Millrace finds and proves its puzzles"
date: 2026-09-24
last_updated: 2026-10-29
seo:
  title: "How Puzzle Levels Are Generated and Verified: Millrace"
  description: "How Millrace's 64 puzzle levels are made: found by search, solved by a breadth-first solver, and checked by tests so that random play rarely wins."
  keywords:
    - puzzle level generation
    - how are puzzle levels made
    - procedural puzzle generator
    - breadth-first search puzzle solver
    - verified puzzle difficulty
    - tile delivery puzzle
    - millrace levels
    - millrace
lede: "I didn't write any of Millrace's 64 levels. A generator proposed them, a breadth-first solver measured each one, and a gate in the test suite decided which ones ship. This is how that works, and why the goal of every level is the one it is."
quick_answer: "Millrace's 64 levels are found by search, not written by hand. A generator proposes candidate levels: a starting board, a fixed queue of arriving tiles, an arrival cell, and a marked cell with an exact target. A breadth-first solver then finds each candidate's shortest solution, and a level without a proven solution does not ship. The checks live in the test suite: it asserts that each level's best possible move count is the solver's shortest solution, and it plays every level against random moves to make sure random play rarely wins. The result card shows that proven number as the best possible, and the Hint inside a level runs the same solver."
faq:
  - q: "How are Millrace's levels made?"
    a: "By search. A generator proposes candidate levels (a starting board, a fixed queue of arriving tiles, an arrival cell, and a marked cell with an exact target), and a breadth-first solver measures each one's shortest solution. A candidate ships only if it passes the checks in the test suite: its shortest solution must be proven, and random play must rarely win it."
  - q: "What does 'Best possible is X moves' mean on the result card?"
    a: "It is the level's proven shortest solution. Every level is solved by breadth-first search, and the first win that search reaches is provably the minimum; the test suite checks that the number stored with the level equals that result. When you solve a level, the result card shows your move count, your best, and the best possible. It is never an estimate or a target someone typed in."
  - q: "Can every Millrace level be won?"
    a: "Yes. Every level has a proven solution within its move limit, and a level without one does not ship. Nothing in a level is random, so no level depends on luck. You can still lose: block the arrival cell, or build past the target. A puzzle needs a way to go wrong."
  - q: "Can random play beat Millrace's levels?"
    a: "Rarely. The test suite plays every level against random moves, and a level that random play can win easily is held back, because it isn't a puzzle. The levels are built to reward looking ahead: where the next tile will land, and which merge to save for later."
  - q: "Why is the queue of arriving tiles fixed?"
    a: "A fixed queue keeps every position a pure function of the moves played. That makes it possible to prove a level's shortest solution. With random arrivals, the best possible solution would depend on tiles nobody has drawn yet. The status line shows how many tiles are still to arrive and which one is next."
  - q: "How hard do Millrace's levels get?"
    a: "The campaign runs through six chapters: Warm-up, which teaches the rules, then Tactics, Pressure, Precision, Deep Water, and Mastery. Every level has a move limit and a proven shortest solution, and the result card shows how close you came to it."
mentioned_apps:
  - millrace
read_time: "4 min read"
excerpt: "Millrace's launch-day design essay: how a search-based generator, a breadth-first solver, and a gate in the test suite produce 64 levels whose shortest solutions are proven and that random play rarely wins."
---

A puzzle level is real when thinking is the only way through it. Checked by machine, that idea turns into a list of testable properties. Every one of the 64 levels in [Millrace](/apps/millrace/), a tile logic puzzle, was found by search, and none ships unless these hold:

1. It is solvable within its move limit.
2. Its shortest solution is known exactly. A breadth-first search walks the level's states, and the first win it reaches is provably the minimum. The game calls that number the best possible; my own estimate plays no part.
3. Random play rarely wins it. A level that falls to random moves isn't a puzzle, so the gate holds it back.

The 64 levels that pass sit in six chapters: Warm-up, which teaches the rules, then Tactics, Pressure, Precision, Deep Water, and Mastery.

## Why greedy-friendly goals fail

A slide-and-merge board suggests obvious goals: clear the board down to a few tiles, or reach a tile of a certain size. Both make poor puzzles, and the reason is almost embarrassing once written down. A goal that a one-move greedy habit directly optimizes can't be a puzzle. A player who grabs the most empty cells *is* pursuing the clearing goal; one who grabs the biggest tile *is* pursuing the reach goal. Thoughtless play wins them.

Delivery survives because it can be lost twice over. The target must rest on one marked cell, so the number has to end up exactly there. It must also be an exact value, so building past it (a 128 when the level asked for a 64) loses the goal for good. No local score approximates either condition. That is why Millrace has one kind of goal: build exactly N on the marked cell.

## Why the arriving tiles are fixed in advance

The other half of the design is the arrival queue. Tiles enter one at a time at the arrival cell. If that cell is blocked when the next one is due, the run ends. That brings back the tension a slide-and-merge board depends on, because it fills while you merge.

Chance stays out. The queue is fixed, so every position is a pure function of the moves played. With random arrivals, "the shortest solution" isn't a number, since it depends on tiles nobody has drawn, and a solver can only average over futures. With a fixed queue there is nothing to average, and breadth-first search is the exact model. On screen, the status line tells you how many tiles are still to arrive and which one is next.

## How a candidate level is generated

The generator is simple, and the rigor sits in the gate. A candidate gets a starting board, a fixed queue, an arrival cell, a marked cell, and a target. The solver measures its shortest solution, and the candidate stays only if that solution exists within the move limit and the rest of the checks pass.

## Thoughtless play has to fail

The test suite plays every level against random moves, and a level random play wins easily is gone. The point is to certify that the content has depth. The skill a level asks for is looking ahead: where will the next arrival land, and which merge should wait? [How to plan moves ahead in Millrace](/journal/how-to-plan-moves-ahead-in-tile-puzzles/) shows that lookahead in play, with Level 1 worked move by move.

## Why the gate lives in the test suite

The checks live in the test target and run every time, not once. The suite asserts each property over the shipped levels, so a level that stops passing fails the tests. Tare's balance puzzles are made by hand, but a solver checks them in the same spirit; [here is how it proves each level has exactly one answer](/journal/how-to-solve-balance-puzzles/).

The Hint inside a level runs the same solver, so the move it suggests always leads to a solution. For [Chessful's forty opponents](/journal/forty-chess-opponents/), difficulty was a matter of character. Here it had to be a number the tests check.

## What you see of it

Almost none of this is on screen.

- The result card says "Solved in N moves", shows your best, and says "Best possible is X moves", where X is the proven minimum.
- Hint draws a move on the board with a one-line reason, and in a level that move lies on a winning line.
- In chess, search depth is an engine setting, and [more of it doesn't help a club player](/journal/engine-depth-at-club-level-tune-down/). Here the shortest solution is a measured property of the board.

Millrace is free on iPhone and iPad; the [app page](/apps/millrace/) has the rules and the privacy details. If a level ever feels impossible, somewhere in its states is a line exactly as long as the card says, and the tests have walked it.
