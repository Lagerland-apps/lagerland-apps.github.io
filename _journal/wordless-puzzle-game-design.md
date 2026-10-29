---
layout: journal
slug: wordless-puzzle-game-design
title: "Designing a puzzle with no words: how Tare teaches its rules, and what accessibility took"
date: 2026-10-09
seo:
  title: "Wordless Puzzle Game Design: How Tare Teaches With No Text"
  description: "How Tare teaches a balance puzzle with no words: onboarding levels with one way forward, a shudder for wrong, and a mobile VoiceOver can read."
  keywords:
    - wordless puzzle game
    - puzzle game without words
    - wordless game design
    - accessible puzzle game iphone
    - voiceover puzzle game
    - colorblind friendly puzzle game
    - puzzle game for any language
lede: "Tare has 200 levels and not one word on the playing field: no tutorial screen, no arrows, no “drag here”. The puzzle had to teach itself, and with no text to label, accessibility had to reach the board itself. This post covers what the first levels teach and how, then what it took to make the same puzzle work with VoiceOver, high contrast and large type."
quick_answer: "Tare teaches its rules without text by building each early level so that the only thing left to try is the lesson. Level 1 has one piece in the tray and one empty hook, so the only move balances the beam. Level 2 has two hooks and two equal weights, so every hook gets filled. Level 3 hangs a 2 and a 4 on notches 2 and 1: with the 4 far out the beam tips, and swapped it balances. Level 4 makes you choose hooks, and level 5 starts with a piece on the wrong hook. Every known weight shows its value as a numeral, while a hidden “?” is always drawn at one fixed size. A full but wrong board gives one small shudder, with no red and no buzzer. A test fails if the code that draws the level contains any text but numerals and the “?”. For accessibility, VoiceOver reads the mobile as named beams, hooks, and weights with place and return actions, a High contrast switch keeps flat colours at 4.5:1 or better, numerals follow Dynamic Type and give way to dots at the largest sizes, and Reduce Motion replaces a hidden weight's restless beam with a slow pulse."
faq:
  - q: "Does Tare have any text?"
    a: "Not on the playing field. A level shows beams, hooks, weights, picture cards and numerals, and the only character besides digits is the “?” on a hidden weight; a test fails if the code that draws a level contains anything else. Words appear only around the puzzle: Settings, the pause menu, the chapter and world names, and the unlock screen. Those screens are translated into 50 languages."
  - q: "How does Tare teach its rules without a tutorial?"
    a: "Each early level allows so little that the next thing to try is the lesson. Level 1 has one legal move, and it solves the level. Level 2 teaches that every hook is filled, level 3 that the heavy side drops and distance multiplies, level 4 that the hook matters, and level 5 that a hung piece can be moved. Level 7 brings the first nested beam, level 10 the first card and level 11 the first hidden weight. On levels 1 to 5, a faint line shows a possible move after 15 seconds of idling, and the first time each kind of card appears, the room briefly lights it and the pieces it quotes."
  - q: "Can you play Tare with VoiceOver?"
    a: "Yes. VoiceOver reads the mobile as a tree of named beams, hooks and weights, such as “Beam 2, hanging from Beam 1, left, notch 2”. Select a piece and every hook offers a place action; a hung piece offers Return to tray. Each beam says whether it is balanced, which side is heavier, or that it cannot settle because of a hidden weight, and the picture cards read as sentences. One test, written for the 80 launch levels, fills every hook using voice actions alone, and another solves levels 1 to 3 as a player who cannot see the screen."
  - q: "Is Tare colour-blind friendly?"
    a: "Colour never carries meaning on its own. The ten weight shapes can be told apart as bare silhouettes, so colour is never the only cue, and every known weight shows its value as a numeral. Beam tilt is shown as an angle, not a colour, and a wrong board shudders instead of flashing red."
  - q: "Can children or people who don't read English play Tare?"
    a: "Yes. The puzzle itself has no words, so it plays the same in any language and at any reading level. The few screens around it are translated into 50 languages. In Arabic, Hebrew and Urdu the menus mirror, but the mobile is always drawn left to right, so what you touch is where the piece is."
  - q: "Does Tare support Reduce Motion, Dynamic Type and high contrast?"
    a: "Yes. Reduce Motion stops the idle drift and the tilt parallax and turns the restless motion of a beam with a hidden weight into a slow pulse. Numerals grow with Dynamic Type and give way to dots at the accessibility sizes. The in-app High contrast switch, or the system's Increase Contrast, switches to flat fills held to 4.5:1 or better, and Reduce Transparency replaces the glassy “?” bubble with a matte one with a dashed rim."
mentioned_apps:
  - tare
read_time: "7 min read"
excerpt: "Tare's launch-day essay on designing without words: what each early level teaches and how, how the game keeps a hidden weight from showing through any channel, and the VoiceOver tree, contrast, Dynamic Type and motion settings that make the same puzzle playable without sight or with low vision."
last_updated: 2026-10-29
---

> **Note:** Tare has 200 levels in ten chapters of twenty. Chapter I, onboarding included, is free, and one purchase unlocks the other 180. This post is the launch-day essay, written when Tare had 80 levels.


Every level of [Tare](/apps/tare/) is a hanging mobile that you balance with weights, and none of the 200 has a word on the playing field. There is no tutorial screen, hand icon or arrow. The puzzle had to teach the rule, the hidden weights and the cards that reveal them on its own. And because there is no text to label, accessibility couldn't be a layer of button labels added at the end.
## What the first levels teach, and how

| You need to know | How Tare shows it | Level |
|---|---|---|
| Level and still means solved | One piece in the tray, one empty hook. The only move balances the beam, and its pivot flashes as it crosses level | 1 |
| Every hook takes a piece | Two hooks, two equal 3s | 2 |
| The heavy side drops, and distance multiplies | A 2 and a 4 for notches 2 and 1. With the 4 far out the beam tips; swapped, 2 × 2 = 4 × 1 | 3 |
| The hook matters as much as the piece | A 3 already hangs three notches out; a 2 and two 1s must fill notches 1, 2 and 3 on the other arm | 4 |
| Anything hung can be moved | A 4 starts on the wrong hook and has to come off | 5 |
| A hanging beam pulls with everything below it | The first nested beam: a 1 three notches out balances a small beam carrying 3 | 7 |
| A card is a true statement | Two different shapes, both 4s, level on a card above a lever the card doesn't picture | 10 |
| A beam with a secret won't tell you | A “?” starts hung, and its beam will not settle | 11 |
| The secret climbs | A “?” on a lower beam keeps the beam above it from settling too | 13 |

Two signals run through every level.

Every known weight states its value as a numeral. A hidden “?” is always drawn at one fixed size, whatever it weighs.

A full but wrong board shudders once, with a soft haptic on iPhone. There is no red, no buzzer and no failure screen. A drop that misses every hook doesn't even get a shudder; the piece glides back to its slot.

## Levels with one way forward

The rule for the first five levels was no text, no hand icons and no tutorial overlay. Each level offers so little that the next thing to try is the lesson. Level 1 has exactly one possible move, and it solves the level. By level 5 you have dragged, filled, swapped and re-hung, because level 5 can't be solved without moving the piece it starts with.

Two wordless helpers sit around those levels:

- A teaching line, on levels 1 to 5 only. After 15 seconds without a touch, a faint line arcs from a piece to a hook. It shows a move, not the solution.
- A short introduction for each kind of card. The first time a card appears, and again for the first secret, tilt, sum and ratio, the room dims on the card and the pieces it quotes, and a short wordless sequence shows what the card means. None is saved: the game works out what you've seen from the levels you've solved.

## No channel leaks a hidden weight

The deduction only works if the game keeps its own secrets. A beam carrying an unsolved “?” never settles, because, as the design notes put it, “the scale cannot weigh a secret”. [How to solve a balance puzzle](/journal/how-to-solve-balance-puzzles/) explains why that matters. The same rule holds elsewhere. The “?” bubble is always one size, and VoiceOver calls the piece hidden and never says a number.

## What accessibility took

With no words on the canvas, labelling the buttons covers almost nothing, so the board itself had to become something a screen reader can walk.

| Need | What Tare does |
|---|---|
| Playing without sight | VoiceOver reads the mobile as a tree: “Beam 2, hanging from Beam 1, left, notch 2.” A hook says what hangs on it or “empty hook”. Select a piece and every hook offers “Place the…”; a hung piece offers “Return to tray”. Each beam reports balanced, which side is heavier, or that it cannot settle. Cards read as sentences: “Reference scale, level. Left, notch 1: …” |
| Colour blindness | Colour never carries meaning alone. The ten weight shapes can be told apart as bare silhouettes, and every known weight shows its numeral |
| Low vision | The High contrast switch, or the system's Increase Contrast, swaps in flat fills held to 4.5:1 or better |
| Large text | The numeral grows with Dynamic Type; at the accessibility sizes it gives way to dots instead of overflowing a small piece |
| Motion sensitivity | Reduce Motion stops the idle drift and the tilt parallax, and turns a hidden weight's restless beam into a slow pulse, which keeps the meaning without the movement |
| Transparency | Reduce Transparency swaps the glassy bubble for a matte one with a dashed rim, at the same fixed size |
| Sound and haptics | Sound ships off, and no level needs it. The Haptics switch appears only on devices that have haptics, so not on iPads |

Tests check all of this. One fills every hook of every shipped level using voice actions alone. Another plays levels 1 to 3 as a player who cannot see the screen: it knows only what an empty hook and a level beam sound like, and how to put a piece back. Others check the contrast of the high-contrast colours and that every weight shape can be told apart without colour.

## Where the words went

Tare does use words in places. Settings, the chapter names (The Hang, The Secret, The Cascade, and the rest), the world names, and the unlock screen all have them, and so does everything VoiceOver says.

A test keeps the canvas to its rule: it reads the code that draws a level and fails if it finds any text other than a weight's numeral and the “?”.

The plan had been English-only VoiceOver at launch, on the reasoning that the gameplay is wordless. That holds for the canvas, but for a player who can't see it, the spoken clauses are the game, and shipping an English game inside a store listing written in 50 languages was where the wordless argument broke down. On 20 September I decided the whole app would ship in all 50 languages. Every spoken line was already a whole clause with placeholders, so a translator could reorder it.

Right-to-left languages turned up a different problem. In Arabic, Hebrew and Urdu, the system mirrored the drawing of the mobile but not the drag, so a player had to touch the mirror image of a piece to lift it. A mobile is a physical toy, so it is now drawn left to right in every language while the menus mirror, and VoiceOver's “left arm” matches what's on screen.

## Decisions that changed late

- Sound off by default, 20 September. I played the finished build and didn't want its sounds on unless a player asks. That cost a teaching channel, since sound had been part of how the first levels taught. Level 1's lesson now rests on the beam going level and still, which works because the level allows no other action.
- The idle line became a teacher only, 19 September. It used to appear by itself after 8 seconds on every level, and it made levels too easy. Now it appears unasked only on levels 1 to 5. Elsewhere, hints are a Settings switch, off by default: each press draws one line from the next piece to its hook, never for the last piece, and the first press on an attempt costs that attempt's third star.

Tare is a free download for iPhone and iPad on iOS and iPadOS 18 or later. Chapter I's 20 levels, onboarding included, are free to keep, and one {P_IAP:Tare Full Access@tare} purchase unlocks the other 180; [why it is priced that way](/journal/puzzle-game-no-ads-one-purchase/) is its own post. If you came for the rule-learning, compare [Baba Is You](/alternatives/baba-is-you/), whose rules are built out of word blocks, and [DragonBox Algebra](/alternatives/dragonbox-algebra/), which also teaches through balancing. For the wider field, see [the best logic puzzle games for iPhone](/guides/best-logic-puzzle-games-iphone/).
