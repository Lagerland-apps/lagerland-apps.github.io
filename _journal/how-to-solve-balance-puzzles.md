---
layout: journal
slug: how-to-solve-balance-puzzles
title: "How to solve a balance puzzle, and how Tare proves all 80 of its levels"
date: 2026-10-09
seo:
  title: "How to Solve Balance Puzzles and Hanging Mobiles — Tare"
  description: "How to solve a balance puzzle: weight × distance, nested beams and clue cards on a real level, then how Tare proves each of its 80 levels has one answer."
  keywords:
    - how to solve balance puzzles
    - balance puzzle
    - hanging mobile puzzle
    - mobile puzzles algebra
    - balance logic puzzle
    - torque puzzle
    - puzzle with one solution
    - tare balance puzzle
lede: "Tare's 80 levels are hanging mobiles you balance with numbered weights, and some of the weights are hidden. Every one was built by hand, and none ships until the test suite proves three things about it: it has exactly one answer, its cards alone name every hidden weight, and its decoys fit nowhere. Here is how to solve one, and how that proof works."
quick_answer: "To solve a balance puzzle, use the lever rule: a beam is level when weight × distance from the pivot is equal on both sides, so a 2 two notches out balances a 4 one notch out. A beam hanging from another beam acts as one weight equal to everything below it, so solve the deepest beams first and carry their totals up. Two beams hung the same distance either side of a pivot must carry equal loads. In Tare, read the clue cards before you place anything: a beam carrying a hidden “?” sways instead of tilting, so the cards are the only way to learn its value. A card can show two sides equal, one side heavier, or a balance on unequal arms, and pieces with the same silhouette always weigh the same. Each of Tare's 80 handcrafted levels is checked by its test suite before it ships: an exhaustive solver must find exactly one balanced arrangement, the cards alone must pin every hidden weight to one value from 1 to 9, and every decoy must fit no balanced arrangement."
faq:
  - q: "How do you solve a balance puzzle?"
    a: "Use the lever rule: a beam is level when the sum of weight × distance from the pivot is the same on both sides. Treat any beam hanging from another as a single weight equal to everything below it, and work from the deepest beam upward. Two beams hung at the same distance either side of a pivot must carry the same load, which often splits the available weights in half. If some weights are unknown, work out their values from the clues before you place anything, then arrange."
  - q: "What is a hanging mobile puzzle?"
    a: "A puzzle built like a mobile: beams on strings, each balancing on its own pivot, with weights hanging from hooks and sometimes other beams hanging from those. Some mobile puzzles show the pieces in place and ask what each shape weighs, which is a set of equations to solve. In Tare you do the placing: you hang weights numbered 1 to 9 on hooks until every beam is level, and work out the hidden weights from picture-card clues along the way."
  - q: "Why does a beam with a “?” sway in Tare instead of tilting?"
    a: "So the scale can't be used to measure a secret. If a beam carrying a hidden weight tilted truthfully, you could hang the “?” on different hooks and read its value off the angle. Instead, any beam whose load includes an unsolved “?” sways slowly, about 3 degrees either side of level, and never settles, and every beam above it sways too. Beams with nothing hidden below them tilt honestly. The only way to learn a hidden value is to reason it out from the cards."
  - q: "What do the clue cards in Tare mean?"
    a: "Each card is a small beam. A level card with equal arms says both sides weigh the same, and two pieces on one side add up. A tilted card says the low side is strictly heavier, and two tilted cards can bracket a value, so heavier than 3 and lighter than 5 means 4. A level card with unequal arms is a ratio: a “?” one notch out balancing a 4 two notches out is an 8. A card may also show a weight you don't have in the tray, for comparison only. One rule needs no card: pieces with the same silhouette always weigh the same."
  - q: "How does Tare make sure every level has exactly one answer?"
    a: "A gate in the test suite runs over every bundled level. An exhaustive solver tries every way to fill the hooks and must find exactly one balanced arrangement, counting two pieces of equal weight as interchangeable. A separate check tries every value from 1 to 9 for each hidden weight against the cards alone and must be left with exactly one, the level's real weight. A third confirms that the pieces flagged as decoys are exactly the pieces no balanced arrangement uses. A level that fails any check fails the tests, with the rule it broke named."
  - q: "What is a decoy in Tare?"
    a: "A piece in the tray that belongs on no hook. The first one appears in the last level of Chapter III, and every Chapter IV level has one or two. Because every hook takes exactly one weight, pieces minus hooks always tells you how many decoys there are; which pieces they are is what you have to prove. The test suite checks that each decoy fits no balanced arrangement at all, and a decoy never shares a weight with a piece that hangs."
  - q: "Is Tare free?"
    a: "Tare is a free download for iPhone and iPad. Chapter I's 20 levels are free to keep, and one $2.99 purchase unlocks the other 60. There are no ads, it works offline, and its App Store privacy label is Data Not Collected."
mentioned_apps:
  - tare
read_time: "9 min read"
excerpt: "Tare's launch-day design essay: how to solve a hanging-mobile balance puzzle, worked through on a real level, and how a gate in the test suite proves each of the 80 handcrafted levels has one balanced arrangement, hidden weights the cards alone determine, and decoys that fit nowhere."
---

Every level of [Tare](/apps/tare/) is a hanging mobile: beams on strings, hooks on the beams, and a shelf of weights numbered 1 to 9. You hang every weight so that every beam balances at once. Some hide inside a “?” bubble drawn at one fixed size, and the scale won't tell you what they weigh; small picture cards above the board will. All 80 were built by hand, and none ships until a gate in the test suite has proved three things about it:

1. **Exactly one arrangement balances.**
2. **The cards alone pin every hidden weight** to a single value.
3. **Every decoy fits no balanced arrangement at all.**

First the method, on a real level, then the gate.

## The one rule: weight × distance

A beam is level when the turning force on each side of its pivot is equal. Each weight contributes its number times its distance from the pivot, counted in notches from 1 to 4. A 2 two notches out balances a 4 one notch out, because 2 × 2 = 4 × 1. Several weights on one side add up.

Beams can hang from other beams. A hanging beam pulls on its hook with the total of everything below it, and the beams themselves weigh nothing. So a child beam has to balance on its own, and its parent sees only one number: its load.

A level is solved when every hook holds a weight and every beam is level. Two pieces of the same weight are interchangeable, so swapping them is not a second answer.

## Read the cards before you hang anything

On a real scale you could weigh a secret by hanging it and watching the beam tip. Tare doesn't allow that. A beam carrying an unsolved “?” doesn't tilt: it sways slowly, about 3° either side of level, and never settles, and the sway climbs to every beam above it. If it tilted truthfully, you could binary-search every hidden value by reading angles, and the puzzle would become measurement.

So the cards are the only scale for a secret. Each card is itself a small beam:

| Card | What it shows | What it tells you | From the game |
|---|---|---|---|
| Equal | Level, equal arms | Both sides weigh the same; two pieces on one side add up | Chapter II, level 5: “?” = 1 + 3, so 4 |
| Tilted | Heavy side down | That side is strictly heavier; two tilts can bracket a value | Chapter II, level 3: heavier than the 3, lighter than the 5, so 4 |
| Ratio | Level, unequal arms | Multiply each side by its notches | Chapter II, level 10: “?” at notch 1 balances a 4 at notch 2, so 8 |
| Twin rule | No card; it holds everywhere | Pieces with the same silhouette weigh the same | Solve one twin and you know both |

A card can also show a weight that isn't in your tray, drawn only for comparison. Chapter II's first level sets its “?” against a 3 you don't own.

## A worked example: Chapter II, level 14

A top beam with no hooks of its own carries two beams, two notches either side of its pivot. The left beam has a hook one notch either side. The right beam has hooks two notches and one notch left, and one notch right. The tray holds a “?”, a 3, two 6s and a 7: five pieces for five hooks.

1. **The cards.** One card shows the “?” heavier than a 1. The other shows it lighter than the 3. Weights are whole numbers, so the “?” is 2.
2. **The top beam.** Both children hang two notches out, so they balance only if they carry the same load. The tray totals 2 + 3 + 6 + 6 + 7 = 24, so each child carries 12.
3. **The left beam.** Equal arms with one hook each means two equal weights. The only pair is the two 6s, and 6 + 6 = 12.
4. **The right beam.** It gets the 2, 3 and 7, also 12. Its one right-hand hook must match both left hooks. Put the 7 there, the 2 two notches out and the 3 one notch out: 4 + 3 = 7. With the 2 or the 3 on the right, the left side comes to at least 11.
5. **Check the top.** 12 × 2 on each side: 24 against 24.

While you play it, the left beam settles level as soon as both 6s are on, because nothing on it is hidden. Once the “?” hangs on the right beam, that beam and the top beam sway until the level is solved.

## Habits that solve most levels

- **Cards first, then arrange.** They are always enough to name every “?”.
- **Work from the bottom up.** A parent sees only a child's total.
- **Equal distances mean equal loads.** Two beams hung equally far either side of a pivot carry the same total.
- **Count the tray.** Every hook takes one weight, so pieces minus hooks is the number of decoys.

## How a level is built

These 80 are the second attempt. On 1 September I played the first two finished chapters: every level was a single flat beam, the cards were hard to read, and there was no reason to keep going. The next day the arc was redesigned so that chapters mix mechanics and the mobile changes shape from level to level.

The design notes call the method "sketched by hand, proven by machine". A level starts as a silhouette, one of ten families: bar, lever, pendant, yoke, fork, outrigger, cradle, ladder, staircase and tree. No structure appears twice in the game, and from level 6 on, no two neighbours on a chapter's four-column grid share a family.

A search in the test target then fills in the numbers. It runs combinations of weights from 1 to 9, one per hook, through the game's own solver and keeps those with exactly one answer, every piece hung and no beam side above 36, ranked by how badly a player who never counts does or by how much work the cards have to do. A card assistant proposes cards and keeps only sets the deduction engine accepts. Then I choose by hand: nice numbers, a symmetry that misleads, a satisfying last piece.

Every level stays inside the same limits: weights 1 to 9, hooks at notches 1 to 4, at most eight pieces, eight hooks, three beams deep, three hidden weights, three decoys and three cards, and 36 on any side of any beam, so the arithmetic fits in your head.

## What the gate proves

As with [Millrace's levels](/journal/how-millrace-levels-are-made/), the gate is a test that runs over every bundled level, not a script run once.

**Exactly one arrangement.** The solver tries every way to fill the hooks, up to 40,320 for eight pieces on eight hooks, branching on weights rather than pieces and filling the deepest beams first so a beam that can't balance is abandoned early. It may call a level unique only if it searched to the end. Its shortcuts are tested against a deliberately naive solver: on an eight-hook test level with 882 solutions, both find the same 882.

**Every “?” from the cards alone.** A separate check ignores the mobile. It tries every value from 1 to 9 for each hidden weight, at most 729 combinations for three, against every card and the twin rule. Exactly one may survive, and it must be the level's real weight. Another check confirms each card is true as drawn, with its own arithmetic rather than the deduction engine's, so a bug in one can't hide a card that lies.

**Every decoy fits nowhere.** The pieces flagged as decoys must be exactly the pieces no balanced arrangement uses. Because the solver counts by weight, a decoy can never share a weight with a piece that hangs: there would be no fact about which of the two is spare.

**No decorative cards.** On a level with a “?”, every card must belong to the smallest set of cards that pins down some hidden weight.

Each check has a deliberately broken level in the suite that it must catch: one with two answers, one with a lying card, one whose “?” the cards leave open. A failure names the level and the rule it broke. For this post, all 80 were also re-checked by a brute-force script that shares no code with the app: 80 single answers, every “?” pinned to its real weight, every decoy unused.

## The 80-level ramp

| Chapter | Levels | Hooks | Beams deep (1 / 2 / 3) | Levels with a “?” | Hidden weights (most in one level) | Decoys | Cards |
|---|---|---|---|---|---|---|---|
| I · The Hang (free) | 1–20 | 2–6 | 10 / 7 / 3 | 4 | 4 (1) | 0 | 5 |
| II · The Secret | 21–40 | 3–6 | 6 / 9 / 5 | 20 | 33 (2) | 0 | 35 |
| III · The Cascade | 41–60 | 4–7 | 1 / 9 / 10 | 13 | 29 (3) | 1 | 30 |
| IV · The Exhibition | 61–80 | 4–6 | 2 / 11 / 7 | 14 | 28 (3) | 30 | 24 |
| **All** | **80** | **2–7** | **19 / 36 / 25** | **51** | **94** | **31** | **94** |

Counting all 80 in order, each idea arrives on a fixed level: the first nested beam at 7, the first card at 10, the first “?” at 11, three beams deep at 15, the first sum card at 17, a weight you don't own at 21, the first bracket at 23, the first ratio at 30, three hidden weights at 51, and one decoy at 60 as a preview of Chapter IV, where every level has one or two.

The solver's own counts show the climb. Chapter I's first level took it 2 weight-into-hook trials; Chapter IV's level 19 took 600. On levels with nothing hidden, a simulated player who never counts hangs everything at random, then keeps making the swap that most reduces the tilt, from 300 fixed starts. It solves the first three levels every time, Chapter I's level 18 one time in ten, and the finale 13% of the time. Ignore the cards on Chapter IV's level 17 and 294 combinations of hidden values and arrangements balance; with them, one does. Chapter IV's level 11 puts exactly 36 on one side of a beam, the cap.

Tare is a free download for iPhone and iPad. Chapter I's 20 levels are free to keep, and one $2.99 purchase unlocks the other 60. There are no ads, it works offline, and its App Store privacy label reads Data Not Collected; the [privacy policy](/apps/tare/privacy/) has the details. If a level seems to need a guess, it doesn't: the cards are enough, and the tests have checked that they are.
