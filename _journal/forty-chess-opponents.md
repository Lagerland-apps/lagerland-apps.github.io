---
layout: journal
slug: forty-chess-opponents
title: "Forty chess opponents, and none of them are me"
seo:
  title: "Forty Chess Opponents: Designing 40 Distinct AI Players"
  description: "How Chessful gives its 40 chess AI opponents a name, a play style, strengths, and weaknesses, on a ladder from 400 to 2400 Elo."
  keywords:
    - "forty chess"
    - "40 chess opponents"
    - "chess ai opponents"
    - "chess app opponents"
    - "play chess vs ai"
    - "chessful"
date: 2026-02-28
lede: "Of all the decisions in Chessful's design, including the engine, the analysis, and the spaced-repetition trainer, the hardest was making the app feel like forty different people. The usual approach is one engine and a strength slider."
quick_answer: "Chessful has 40 named AI chess opponents in eight tiers, from Pebble at 400 Elo to The Grandmaster at 2400. Each one has a play style (Balanced, Aggressive, Defensive, Tactical, Positional, or Endgame Specialist), strengths, and weaknesses, so the ladder reads as a series of different opponents rather than one strength slider. Beat an opponent twice to mark it defeated. The first 10 are free; Premium opens all 40. After each game, Stockfish analysis on your device explains every mistake in plain language."
faq:
  - q: "How is Chessful different from playing the engine on chess.com?"
    a: "Chessful is a training app with no online play. Many chess apps offer one engine with a strength slider; Chessful has 40 named opponents in eight tiers, from 400 to 2400 Elo, each with a play style, strengths, and weaknesses. After the game, on-device Stockfish analysis explains every mistake in plain language, and those mistakes become your daily training."
  - q: "Does Chessful explain my mistakes in plain language?"
    a: "Yes. After a game, Stockfish checks every move on your device. Each mistake shows what you played, what was best, why the better move works, and the line that punishes your move, worded for the coaching level you choose. Each one is tagged with one of 10 mistake types, such as Hanging Piece, Missed Fork, or Endgame Error."
  - q: "Does Chessful require an internet connection or account?"
    a: "No account, and no connection for the chess itself. All 40 opponents, the Stockfish analysis, lessons, and puzzles run on your device, so you can play on a flight. Buying or restoring Premium and the optional Game Center need a connection."
  - q: "Is Chessful a replacement for chess.com or lichess?"
    a: "No. Chessful has no online play, matchmaking, or clocks; every game is against its built-in opponents. Game Center leaderboards are optional. For rated games against people, chess.com and lichess remain the right tools, and you can import those games into Chessful as PGN to review them."
mentioned_apps:
  - chessful
read_time: "4 min read"
excerpt: "Why playing 'the engine at level 7' is unsatisfying, how Chessful gives each of its 40 opponents a name, a style, strengths, and weaknesses, and why the post-game explanations matter as much as the opponents."
last_updated: 2026-10-29
---

I learned chess from my grandfather and never got past competent. The reason I built [Chessful](/apps/chessful/) is that gap: I wanted an app that explained what I'd done wrong the way my grandfather would have, in plain language, instead of pointing at an evaluation graph and expecting me to read it.

Two parts of the app took the most design effort. One was the post-game analysis, which is the reason the app exists. The other was the forty opponents, which carry everything else. This post covers both.

## What's wrong with the slider-based chess opponent?

Many chess apps offer a slider from Level 1 (weak) to Level 20 (engine-strong). The slider feels reasonable until you play it for a week and notice something specific.

The engine plays the same way at every level. It just plays *worse on purpose* at lower levels. Level 5 is the same opponent as Level 15, making mistakes that have nothing to do with any style. After a dozen games you can feel it, and no real opponent plays that way.

People have *characters*. They favour certain openings. Some attack at every chance and some sit tight. They have blind spots: the bishop on the long diagonal they always miss, the rook on the seventh rank they always overestimate.

If you're building a chess app for improvement, a slider isn't enough. The opponents should feel like *people*.

## The forty opponents

Chessful has forty AI opponents on a ladder of eight tiers, five to a tier, from Novice to Master. The ladder starts with Pebble at 400 Elo and ends with The Grandmaster at 2400. Every opponent has a name, a play style, a set of strengths, and a set of weaknesses. They are fictional. None of them imitates a real grandmaster, which is a line I won't cross, but each one is recognisable as a *type*.

The styles are Balanced, Aggressive, Defensive, Tactical, Positional, and Endgame Specialist. An Aggressive opponent and a Positional one at a similar rating are meant to ask different questions of you. Knowing an opponent's strengths and weaknesses gives you something to play against instead of an abstract strength number.

You climb by beating each opponent twice, and Next Challenge points you at the first one you haven't beaten yet. The first ten opponents are free; Premium opens all forty, in any order. The Elo next to each name is a label for that opponent's strength on Chessful's own scale, not a FIDE or online rating.

## The post-game analysis

The other part that took real effort is the post-game analysis.

The standard chess-app flow is: play a game, hit "analyse," and watch the engine annotate every move with an evaluation. The output is technically correct and hard to read unless you're already strong. *"You played 18.Re1, computer prefers 18.Bxh6 with eval +1.4."* Yes, but *why?*

Chessful tries to answer the *why*. Stockfish runs on your device and rates every move from Brilliant to Blunder. For each mistake you get a card: what you played, what was best, how far the evaluation dropped, a plain-language explanation of why the better move works, and the line that punishes your move. The explanation is worded for the coaching level you pick, from "Just learning the rules" to rated 1400+. Each mistake is tagged with one of ten types, such as Hanging Piece, Missed Fork, Back-Rank Weakness, or Endgame Error, and Train This Pattern takes you straight to practice on it.

Those mistakes then become the puzzles in your daily training, and spaced repetition brings back the ones you miss.

## What Chessful does not do

Chessful is not a chess.com replacement. It has no online play, matchmaking, or clocks. Those products exist and are excellent at competitive play. Game Center leaderboards and achievements are there if you want them, and they are optional.

Chessful is for the player who wants to improve on their own against varied opponents, with explanations they can actually read, on a flight, in a kitchen, or between meetings. It needs no account, and the chess itself works offline. If you also play online, export your games as PGN and import them, so the same analysis covers those games too.

## A small, personal note

I've never told anyone this in print before, but the reason I made the post-game explanations read like a teacher is that my grandfather was a chess teacher before he was anything else. I lost him in 2019. The tone I aimed for in Chessful's explanations is, as best I could manage, his.

If you find the explanations patient, that's why.

[Chessful](/apps/chessful/) is on the App Store. It is free to try with daily limits, and Premium unlocks unlimited analysis and all forty opponents. If you've been looking for a chess app that explains what you did wrong without making you feel like an idiot, this one might be it.
