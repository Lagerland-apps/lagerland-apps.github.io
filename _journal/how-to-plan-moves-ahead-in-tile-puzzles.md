---
layout: journal
slug: how-to-plan-moves-ahead-in-tile-puzzles
title: "How to plan moves ahead in a tile puzzle: six checks, and Millrace's Level 1 move by move"
date: 2026-09-27
seo:
  title: "How to Plan Moves Ahead in a Tile Puzzle: Millrace Guide"
  description: "How to plan moves ahead in a tile puzzle: six checks for Millrace's arrival cell, tile queue, exact target, and move limit, and Level 1 in five moves."
  keywords:
    - how to plan moves ahead in puzzle games
    - tile puzzle strategy
    - merge puzzle strategy
    - thinking ahead in puzzle games
    - millrace tips
    - millrace level 1 solution
    - millrace strategy
    - millrace
lede: "Nothing in a Millrace level is random, so every level can be planned to the end before your first swipe. In practice, planning is a short list of checks you run before each move. This post gives the six that matter, why each follows from the rules, and Level 1 played move by move, including the two swipes that lose it on the spot."
quick_answer: "To plan ahead in Millrace, read the whole level before your first swipe, then run the same checks before every move. 1) Read the move limit and sketch a line that fits inside it. 2) Work out which tiles add up to the exact target. 3) While any tile is still due, never slide toward the edge the arrival cell sits on unless that slide completes the delivery: the tile that just arrived can't leave the edge, so the next one has nowhere to land. 4) On the two slides along that edge, count the tiles in the arrival cell's line; if they pack onto the arrival cell, that slide loses too. 5) Count the queue: once the last tile has arrived, the arrival cell stops mattering and the remaining moves are free for carrying the target. 6) Decide early whether you will build the value elsewhere and slide it onto the marked cell, or make the final merge on the marked cell itself. Keeping the arrival cell clear is necessary but never enough; solving takes looking further ahead."
faq:
  - q: "What is the best strategy for Millrace?"
    a: "Plan from the numbers the level gives you: the move limit, the target, and the tiles still to arrive. Work out which tiles make the exact target, never slide toward the arrival cell's edge while a tile is still due unless that slide wins, check that the other slides don't push a tile onto the arrival cell, and watch for the moment the queue runs out, after which the arrival cell no longer matters."
  - q: "Why do I keep getting Blocked in Millrace?"
    a: "Blocked means the next tile was due and the arrival cell was occupied. It has two causes. Sliding toward the arrival cell's edge after an arrival leaves the newest tile where it is, against the edge. A slide along that edge packs the arrival cell's row or column toward one end and can push another tile onto it. Inside a level, Undo is free and unlimited, and after a loss the card offers Undo that move."
  - q: "How do you solve Millrace Level 1?"
    a: "Down, Right, Right, Up, Left. That is the only five-move solution, and five is the minimum. The two 4s merge into an 8 on the bottom row, the two 8s merge into the 16 in the bottom-right corner, and once all three queued 2s have arrived, Up lifts the 16 into the marked cell's row and Left slides it onto the marked cell. The move limit is 7, so a solution of six or seven moves also counts."
  - q: "How many moves do Millrace levels need?"
    a: "It depends on the level, and each one has a move limit you can see before your first swipe. Level 1 has a limit of 7 and a shortest solution of 5. When you solve a level, the result card shows your move count, your best, and the best possible, which is the shortest solution a solver proved before the level shipped."
  - q: "Does using Hint or Undo cost anything in a Millrace level?"
    a: "No. Hint asks the same solver that proved the level for a move on a winning line from your current position, and it is free. Undo inside a level is free and unlimited. Undo tokens, the consumable that is sold, are only spent in Freeplay, the endless board."
  - q: "What does Position lost at move N mean?"
    a: "After a failed run, the result card can name the move after which the level could no longer be won. It is shown only after the run, never during it. A run can end on its last move after being lost several moves earlier, and this line tells you which move did it."
mentioned_apps:
  - millrace
read_time: "8 min read"
excerpt: "A strategy guide to Millrace's tile levels: the rules that matter for planning, six checks to run before each swipe, and Levels 1 and 8 worked through with their real boards, queues, and move counts."
last_updated: 2026-10-29
---

[Millrace](/apps/millrace/) is a tile logic puzzle: build one exact number on the marked cell within a move limit, while tiles keep arriving one at a time at the arrival cell. The board is set and the queue of arriving tiles is fixed, so a level can be planned to the end.

## The rules that matter for planning

| Rule | What it means when you plan |
|---|---|
| The board is 4×4. A swipe slides every tile; two equal tiles merge into their sum, once per move. | One swipe changes all four rows or columns at once. |
| After each move, the next tile in the queue lands on the arrival cell. | Every arrival lands on the same cell, and the queue never changes. |
| The level card shows how many tiles arrive; during play, the status line shows how many are still to come and which one is next. | You know what is coming before it lands. |
| If the arrival cell is occupied when a tile is due, the run ends: Blocked. | While tiles remain, the arrival cell must be empty after every move. |
| The goal is one exact number on the marked cell. | Too small isn't finished, and building past it (a 32 when the level asks for 16) loses the goal. |
| The goal is checked before the next tile arrives. | The winning move can't be spoiled by the arrival cell. |
| Every level has a move limit. | Spare moves are few, so a wasted swipe costs. |

## Six checks before every swipe

**1. Read the move limit.** The "moves left" counter is your whole budget. Before your first swipe, sketch a line that fits inside it. After a solve, the result card shows the best possible, so a second attempt has a number to aim at.

**2. Do the target arithmetic.** Every tile is a power of two, so the target is built from pairs: a 32 is two 16s, a 16 is two 8s. Before moving, find the tiles that will become the target, including any still in the queue. Note anything that could merge with the finished value, too.

**3. Never slide toward the arrival cell's edge while a tile is due.** When the arrival cell sits against an edge, as it does in Level 1, the newest tile lands there after every move. A slide toward that edge can't move it off. It either stays put or absorbs an equal tile behind it, and either way the cell is still occupied when the next tile comes. So from move 2 on, while the queue isn't empty, that swipe does nothing, loses, or wins. It can win because the goal is checked before the next arrival, so a slide that completes the delivery still counts.

**4. Check the arrival cell's own line on the other slides.** Say the arrival cell is on the left edge. Left is check 3. Right moves the newest tile away, unless its row is still full after merging. Up and Down pack the arrival cell's column toward one end, and if it holds enough tiles after merging to reach the arrival cell, one of them lands on it. Count before you swipe.

**5. Count the queue.** One tile arrives after each move until the queue is empty. Level 1 has three arrivals and a 7-move limit, so the arrival cell matters for the first three moves only. After that, the board is a pure delivery problem. When the queue holds at least as many tiles as the level has moves, the arrival cell never stops mattering.

**6. Choose your finish early.** A delivery ends in one of two ways. Either you build the value elsewhere and slide it onto the marked cell, or the final merge happens on the marked cell itself. Carrying needs an open lane to the marked cell; merging there needs the second tile to line up with it. The early moves build one or the other.

## Level 1, move by move

Here is the first Warm-up level's starting board:

| | Column 1 | Column 2 | Column 3 | Column 4 |
|---|---|---|---|---|
| **Row 1** | 4 | · | 2 | · |
| **Row 2** | arrival cell | · | · | · |
| **Row 3** | marked cell | · | · | · |
| **Row 4** | · | · | 4 | 8 |

The arrival cell is on the left edge, second row; the marked cell is directly below it. The target is exactly 16. The queue is 2, 2, 2, and the move limit is 7. The shortest solution is 5 moves, and only one five-move line exists.

Start with the arithmetic. 16 is 8 + 8, and the second 8 can come from the two 4s. The three queued 2s play no part in the target. They are the cost of the level: three tiles to keep off the arrival cell.

| Move | Swipe | What happens | Tiles still due |
|---|---|---|---|
| 1 | Down | The top-left 4 drops to the bottom-left corner; the 2 in the third column stops on the 4 below it. Bottom row: 4 · 4 8. A 2 arrives on the arrival cell. | 2 |
| 2 | Right | The bottom 4s merge: · · 8 8. The new 2 slides off the arrival cell to the right edge. Another 2 arrives. | 1 |
| 3 | Right | The 8s merge into the 16 in the bottom-right corner; the two 2s in the arrival cell's row merge into a 4. The last 2 arrives. | 0 |
| 4 | Up | Nothing else is coming, so the arrival cell no longer matters. The right column rises, lifting the 16 into the marked cell's row. | 0 |
| 5 | Left | The 16 slides along the third row onto the marked cell. Solved. | none |

The 16 is built in the far corner, away from the arrivals, and carried to the marked cell only after the queue is empty. That is check 5 and check 6 working together.

Where it goes wrong:

- **Move 2, Left or Up: Blocked.** Two of the four swipes lose on the spot. Left pushes the 2 that just arrived against the edge (check 3). Up packs the left column, the 2 on the arrival cell and the 4 in the corner, into the top two cells, which puts the 4 on the arrival cell (check 4).
- **Move 3, Up: lost, quietly.** Up is legal and blocks nothing. It splits the two 8s: one goes to the top of the third column, the other to the second row of the fourth. With four moves left, no line brings a 16 to the marked cell. Nothing on screen says so, but if the run ends in a loss, the card reads "Position lost at move 3".
- **Move 3, Down: safe, but slower.** It still wins, in six moves instead of five, so it costs one of the two spare moves.

## Level 8: when the queue never runs out

Level 8, in Tactics, turns check 5 around. Nine tiles are queued against an 8-move limit, so a tile is due after every move the level allows. The arrival cell is in the top row, second column, and the marked cell sits right next to it in the third column. The target is exactly 32.

The only shortest line takes six moves: Right, Down, Left, Down, Right, Up. Its last swipe goes toward the arrival cell's own edge with tiles still waiting. That's the exception in check 3. Up carries a 32 from the third row onto the marked cell, and the goal is checked before the next tile is due. The same swipe one move earlier would have lost on the spot.

## Why the checks are not enough on their own

Every check above looks one move ahead, and the levels are built so that one-move play rarely gets through; [how Millrace's levels are made](/journal/how-millrace-levels-are-made/) explains the checks every level passes before it ships. The six checks keep you alive. Solving takes the next step: where the tile after next will land, and what the board must look like when it does.

## When you get stuck

- **Hint** draws a move on a winning line from where you stand, with a one-line reason. It runs the same solver that proved the level, and it's free.
- **Undo** inside a level is free and unlimited. After a loss, the card offers "Undo that move" and Retry. Undo tokens apply only to Freeplay, the endless board.
- **The result card** shows your move count, your best, and "Best possible is N moves".

Millrace is free on iPhone and iPad, with no ads; the [app page](/apps/millrace/) has the full rules. The comparisons with [Threes](/alternatives/threes/), [KAMI 2](/alternatives/kami-2/), and [Flow Free](/alternatives/flow-free/) set out what each of those games asks of you.
