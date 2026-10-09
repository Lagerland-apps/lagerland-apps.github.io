---
layout: journal
slug: how-to-plan-moves-ahead-in-tile-puzzles
title: "How to plan moves ahead in a tile puzzle: six checks, and Millrace's Level 1 move by move"
date: 2026-09-27
seo:
  title: "How to Plan Moves Ahead in a Tile Puzzle — Millrace Guide"
  description: "How to plan moves ahead in a tile puzzle: six checks for Millrace's inlet, visible queue, exact target and move budget, with Level 1 solved in five moves."
  keywords:
    - how to plan moves ahead in puzzle games
    - tile puzzle strategy
    - merge puzzle strategy
    - thinking ahead in puzzle games
    - millrace tips
    - millrace level 1 solution
    - millrace strategy
    - millrace
lede: "Nothing in a Millrace level is random, so every level can be planned to the end before your first swipe. In practice, planning is a short list of checks you run before each move. Here are the six that matter, why each follows from the rules, and Level 1 played move by move, including the two swipes that lose it on the spot."
quick_answer: "To plan ahead in Millrace, read the whole level before your first swipe, then run the same checks before every move. 1) Read the chapter as a number: every Warm-up level's shortest solution is 5 moves, Tactics 6, Pressure 7, Precision 8, Deep Water 9 and Mastery 10 to 16, so the move budget minus that number is your slack — two spare moves on 56 levels, one on six, none on two. 2) Work out which tiles add up to the exact target. 3) While any tile is still due, never slide toward the inlet's edge unless that slide completes the delivery: the tile that just arrived cannot leave the edge, so the next one has nowhere to land. 4) On the two slides along that edge, count the tiles in the inlet's line; if they pack onto the inlet, that slide loses too. 5) Count the queue: once the last tile has arrived, the inlet stops mattering and the remaining moves are free for carrying the target. 6) Decide early whether you will build the value elsewhere and slide it onto the marked cell, or make the final merge on the cell itself. Keeping the inlet clear is necessary but never enough: every level is tested against 24 strategies that keep the inlet clear and look no further, and all 24 lose."
faq:
  - q: "What is the best strategy for Millrace?"
    a: "Plan from the numbers the level gives you. The chapter tells you the shortest solution (5 moves in Warm-up, then 6, 7, 8 and 9, and 10 to 16 in Mastery), so you know your spare moves before you start. Work out which tiles make the exact target, never slide toward the inlet's edge while a tile is still due unless that slide wins, check that the other slides don't push a tile onto the inlet, and watch for the moment the queue runs out, after which the inlet no longer matters."
  - q: "Why do I keep getting Blocked in Millrace?"
    a: "Blocked means the next tile was due and the inlet was occupied. It has two causes. Sliding toward the inlet's edge after an arrival leaves the newest tile where it is, against the edge. A slide along that edge packs the inlet's row or column toward one end and can push another tile onto the inlet. Inside a level, Undo is free and unlimited, and after a loss the card's main button is Undo that move."
  - q: "How do you solve Millrace Level 1?"
    a: "Down, Right, Right, Up, Left. That is the only five-move solution, and five is the minimum. The two 4s merge into an 8 on the bottom row, the two 8s merge into the 16 in the bottom-right corner, and once all three queued 2s have arrived, Up lifts the 16 into the vault's row and Left slides it onto the vault. The budget is 7 moves, so a solution of six or seven moves also counts."
  - q: "How many moves do Millrace levels need?"
    a: "Each chapter is pinned to one shortest-solution length: every Warm-up level needs exactly 5 moves, Tactics 6, Pressure 7, Precision 8 and Deep Water 9, and Mastery levels need 10 to 16. The move budget is two moves above the shortest solution on 56 of the 64 levels, one above on 6, and equal to it on 2, Levels 51 and 64."
  - q: "Does using Hint or Undo cost anything in a Millrace level?"
    a: "No. Hint asks the same solver that verified the level for the first move of a shortest line from your current position, and it is free and unlimited. Undo inside a level is also free and unlimited. Undo tokens, the consumable that is sold, are only spent in Freeplay, the endless board."
  - q: "What does Position lost at move N mean?"
    a: "After a failed run, the result card can name the move after which no line within the budget could still win. It is shown only after the run, never during it. A run can end on its last move after being lost several moves earlier, and this line tells you which move did it."
mentioned_apps:
  - millrace
read_time: "8 min read"
excerpt: "A strategy guide to Millrace's tile-delivery levels: the rules that matter for planning, six checks to run before each swipe, and Levels 1 and 8 worked through with their real boards, queues and move counts."
---

[Millrace](/apps/millrace/) is a tile-delivery puzzle: build one exact value on one marked cell inside a move budget, while tiles keep arriving through a single inlet on the board's edge. The board is fixed and every arriving tile is shown before your first move, so a level can be planned to the end. The campaign screen states the core rule in one line: "Tiles keep arriving at the marked cell. Block it and you lose."

## The rules that matter for planning

| Rule | What it means when you plan |
|---|---|
| The board is 4×4. A swipe slides every tile; two equal tiles merge into their sum, once per move. | One swipe changes all four rows or columns at once. |
| Tiles arrive through one inlet, on an edge, never in a corner. | Every arrival lands on the same cell. |
| After each move, the next tile in the queue lands on the inlet. Only 2s and 4s arrive, and the whole queue is shown. | You know every future arrival before you start. |
| If the inlet is occupied when a tile is due, the run ends: Blocked. | While tiles remain, the inlet must be empty after every move. |
| The goal is one exact value on one marked cell, the vault. | Too small isn't finished, and merging past it — a 32 when the level asks for 16 — destroys it. |
| The goal is checked before the next tile arrives. | The winning move can't be spoiled by the inlet. |
| The move budget is two above the shortest solution on 56 levels, one above on 6, and equal to it on 2. | At most two spare moves; on Levels 51 and 64, none. |
| Every legal first move leaves the level winnable. | Your first swipe can never lose. |

## Six checks before every swipe

**1. Read the chapter as a number.** Each chapter is pinned to one solution length. Every Warm-up level's shortest solution is exactly 5 moves, Tactics 6, Pressure 7, Precision 8 and Deep Water 9; Mastery runs from 10 to 16. Compare it with the "moves left" counter before your first swipe: a Tactics level that opens with 8 moves left gives you two spare moves.

**2. Do the target arithmetic.** Every tile is a power of two, so the target is built from pairs: a 32 is two 16s, a 16 is two 8s. Before moving, find the tiles that will become the target, including any still in the queue. Note anything that could merge with the finished value, too.

**3. Never slide toward the inlet's edge while a tile is due.** After every arrival, the newest tile sits on the inlet, against the edge. A slide toward that edge can't move it off. It either stays put or absorbs an equal tile behind it, and either way the cell is still occupied when the next tile comes. So from move 2 on, while the queue isn't empty, that swipe does nothing, loses, or wins. It can win because the goal is checked before the next arrival, so a slide that completes the delivery still counts. No level is an exception.

**4. Check the inlet's own line on the other slides.** Say the inlet is on the left edge. Left is check 3. Right moves the newest tile away, unless its row is still full after merging. Up and Down pack the inlet's column toward one end, and if it holds enough tiles after merging to reach the inlet, one of them lands on it. Count before you swipe.

**5. Count the queue.** Each level card shows how many tiles are arriving, and the status bar under the board shows the remaining queue with the next tile highlighted. One tile arrives after each move until the queue is empty. Level 1 has three arrivals and a 7-move budget, so the inlet matters for the first three moves only. After that, the board is a pure delivery problem. In 9 of the 64 levels the queue holds at least as many tiles as the budget has moves, so the inlet never stops mattering.

**6. Choose your finish early.** A delivery ends in one of two ways. Either you build the value elsewhere and slide it onto the vault, or the final merge happens on the vault itself. In 22 levels every shortest solution ends with a slide, in 29 with a merge on the vault, and 13 can be finished either way. Carrying needs an open lane to the vault; merging there needs the second tile to line up with it. The early moves build one or the other.

## Level 1, move by move

Here is the first Warm-up level's starting board:

| | Column 1 | Column 2 | Column 3 | Column 4 |
|---|---|---|---|---|
| **Row 1** | 4 | · | 2 | · |
| **Row 2** | inlet | · | · | · |
| **Row 3** | vault | · | · | · |
| **Row 4** | · | · | 4 | 8 |

The inlet is on the left edge, second row; the vault is directly below it. The target is exactly 16. The queue is 2, 2, 2, and the budget is 7 moves. The shortest solution is 5 moves, and only one five-move line exists.

Start with the arithmetic. 16 is 8 + 8, and the second 8 can come from the two 4s. The three queued 2s play no part in the target. They are the cost of the level: three tiles to keep off the inlet.

| Move | Swipe | What happens | Tiles still due |
|---|---|---|---|
| 1 | Down | The top-left 4 drops to the bottom-left corner; the 2 in the third column stops on the 4 below it. Bottom row: 4 · 4 8. A 2 arrives on the inlet. | 2 |
| 2 | Right | The bottom 4s merge: · · 8 8. The new 2 slides off the inlet to the right edge. Another 2 arrives. | 1 |
| 3 | Right | The 8s merge into the 16 in the bottom-right corner; the two 2s in the inlet's row merge into a 4. The last 2 arrives. | 0 |
| 4 | Up | Nothing else is coming, so the inlet no longer matters. The right column rises, lifting the 16 into the vault's row. | 0 |
| 5 | Left | The 16 slides along the third row onto the vault. Solved. | — |

The 16 is built in the far corner, away from the arrivals, and carried to the vault only after the queue is empty. That is check 5 and check 6 working together.

Where it goes wrong:

- **Move 2, Left or Up: Blocked.** Two of the four swipes lose on the spot. Left pushes the 2 that just arrived against the edge (check 3). Up packs the left column, the 2 on the inlet and the 4 in the corner, into the top two cells, which puts the 4 on the inlet (check 4).
- **Move 3, Up: lost, quietly.** Up is legal and blocks nothing. It splits the two 8s: one goes to the top of the third column, the other to the second row of the fourth. With four moves left, no line brings a 16 to the vault. Nothing on screen says so, but if the run ends in a loss, the card reads "Position lost at move 3".
- **Move 3, Down: safe, but slower.** It still wins, in six moves instead of five, so it costs one of the two spare moves.

## Level 8: when the queue never runs out

Level 8, in Tactics, turns check 5 around. Nine tiles are queued against an 8-move budget, so a tile is due after every move the level allows. The inlet is in the top row, second column, and the vault sits right next to it in the third column. The target is exactly 32.

The only shortest line takes six moves: Right, Down, Left, Down, Right, Up. Its last swipe goes toward the inlet's own edge with four tiles still waiting. That's the exception in check 3. Up carries a 32 from the third row onto the vault, and the goal is checked before the next tile is due. The same swipe one move earlier would have lost on the spot.

## Why the checks are not enough on their own

Every check above looks one move ahead, and one-move play is what the levels are built to beat. Before a level ships, 280 strategies that never look past the current move play it, among them 24 versions of "keep the inlet clear", 24 that refuse any move that loses at once, and 24 that steer the target toward the vault. If any of them wins, the level is thrown away; [how Millrace's levels are made](/journal/how-millrace-levels-are-made/) covers the full battery. The checks keep you alive. Solving takes the next step: where the tile after next will land, and what the board must look like when it does.

## When you get stuck

- **Hint** draws the first move of a shortest line from where you stand, with a one-line reason. It runs the same solver that verified the level, and it's free and unlimited.
- **Undo** inside a level is free and unlimited. After a loss, the card's main button is "Undo that move", not Restart. Undo tokens apply only to Freeplay, the endless board.
- **The result card** says "Best possible is N moves" when you solved a level in more moves than it needed.

Millrace is free on iPhone and iPad, with no ads and no lives; the [app page](/apps/millrace/) has the full rules. The comparisons with [Threes](/alternatives/threes/), [KAMI 2](/alternatives/kami-2/) and [Flow Free](/alternatives/flow-free/) set out what each of those games asks of you.
