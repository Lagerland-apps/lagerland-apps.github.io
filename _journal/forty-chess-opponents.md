---
layout: journal
slug: forty-chess-opponents
title: "Forty chess opponents, and none of them are me"
seo:
  title: "Forty Chess Opponents: Designing 40 Distinct AI Players"
  description: "How Chessful makes 40 chess AI opponents feel like forty different people, each with its own style and strength instead of one engine in forty masks."
  keywords:
    - "forty chess"
    - "40 chess opponents"
    - "chess ai opponents"
    - "chess app opponents"
    - "play chess vs ai"
    - "chessful"
date: 2026-02-28
lede: "Of all the decisions in Chessful's design, including the engine, the analysis, and the spaced-repetition trainer, the hardest was making the app feel like forty different people. The usual approach is one engine wearing forty hats."
quick_answer: "Chessful ships forty distinct AI chess opponents instead of a single engine made worse on purpose at lower levels. Each opponent has a rating, opening repertoire, structural preference, and characteristic blind spots, so games feel like playing different people, where a slider just adds noise. Post-game analysis explains mistakes in plain language a club player can actually read."
faq:
  - q: "How is Chessful different from playing the engine on chess.com?"
    a: "Chess.com and most chess apps use a single engine with added evaluation noise at lower levels, so every opponent is structurally the same player making random mistakes. Chessful ships forty distinct opponents, each with its own opening repertoire, structural preferences, and blind spots, so games feel like playing different people, where a slider gives you one player with noise added."
  - q: "Does Chessful explain my mistakes in plain language?"
    a: "Yes. Chessful's post-game analysis identifies the move that lost the game, the threat you missed, and the structural reason in one or two sentences. A layered model combines an engine, a small language model, and hand-curated motif detectors so explanations read like a chess teacher talking, with no centipawn graph."
  - q: "Does Chessful require an internet connection or account?"
    a: "No. Chessful does not require internet, an account, or matchmaking infrastructure. All forty opponents and the analysis layer run on-device, so you can play on a flight, in a kitchen, or between meetings without exposing a ranking attached to your name."
  - q: "Is Chessful a replacement for chess.com or lichess?"
    a: "No. Chessful does not offer ranked play, live human matchmaking, or leaderboards. It is for the player who wants to improve at their own pace against varied AI opponents with readable explanations. For ranked human play, chess.com and lichess remain the right tools."
mentioned_apps:
  - chessful
read_time: "5 min read"
excerpt: "The story of Chessful's 40 AI opponent personalities: why playing 'the engine at level 7' is unsatisfying, what it took to give each opponent a recognizable style, and how plain-language post-game analysis ended up being the feature users mention most."
last_updated: 2026-10-26
---

I learned chess from my grandfather and never got past competent. The reason I built [Chessful](/apps/chessful/) is precisely that gap: I wanted an app that explained what I'd done wrong in a way my grandfather would have, in plain language, instead of pointing at a centipawn evaluation graph and expecting me to read it.

The app shipped with two features that took disproportionate engineering effort. One was the post-game analysis, which is the feature users actually mention. The other was forty distinct AI opponents, which carry everything else without anyone noticing. This post covers both.

## What's wrong with the slider-based chess opponent?

Most chess apps offer a slider from Level 1 (weak) to Level 20 (engine-strong). The slider feels reasonable until you play it for a week and realise something specific:

The engine plays the same way at every level. It just plays *worse on purpose* at lower levels, by adding noise to its evaluation function. Level 5 is the same opponent as Level 15, making mathematically random mistakes. After a dozen games you can feel the noise. The mistakes have nothing to do with any style, and no real opponent plays that way.

The result is that improvement against the engine slider doesn't transfer well to playing humans, because humans have *characters*. They favour certain openings. They get into trouble in specific structural positions. They have blind spots: the bishop on the long diagonal they always miss, the rook on the seventh rank they always overestimate.

If you're trying to build a chess app for improvement, the slider isn't enough. You need opponents that feel like *people*.

## The forty opponents

Chessful ships with forty AI opponents, each with a distinct rating, opening repertoire, structural preferences, and a small set of characteristic blind spots. Every opponent has a name, a portrait, and a one-paragraph backstory. They are explicitly fictional. None of them imitates a specific real grandmaster, which is a line I won't cross, but each one is recognisable as a *type*.

There's the aggressive Sicilian player who attacks the kingside relentlessly and sometimes overcommits. The positional grinder who exchanges pieces to reach better endgames. The fianchetto specialist who handles the long diagonals beautifully but flails in tactics. The student who plays well in opening theory but forgets it after move twelve. The 1700-rated club player who is slightly drunk on a Tuesday night and slightly sober on a Thursday morning.

Each opponent is built from a base engine with a *style overlay*: modifiers to the evaluation function that nudge it toward characteristic moves, openings, and structural decisions. The implementation is unglamorous, mostly piecewise weighting of evaluation features (mobility vs. king safety vs. pawn structure vs. material) tuned by playing thousands of games against a fixed test set and watching for behavioural drift.

The result is *recognisability*. After ten games against the aggressive Sicilian player, you start to anticipate her openings and learn where her blind spots are, and you are playing against her instead of an abstract evaluation function. That is what makes the games feel like games, and it is why improvement against Chessful's opponents transfers to playing humans.

## The post-game analysis

The other feature that took disproportionate effort is the post-game analysis, and it is the feature users write to me about.

The standard chess-app analysis flow is: play a game, hit "analyse," watch the engine annotate every move with a depth-15 evaluation. The output is technically correct and almost completely unreadable for anyone below 1800 rating. *"You played 18.Re1, computer prefers 18.Bxh6 with eval +1.4."* Yes, but *why?*

Chessful's analysis tries to answer the *why* in plain language. It finds the move that lost the game and the threat the user missed, then explains in one or two sentences what was happening structurally. Sometimes it suggests the principle the user should remember, such as *"Trades that benefit your opponent's pawn structure are usually bad even if material is even"*, or *"This is a known weak square for the bishop in the Caro-Kann"*.

The implementation is a layered model: the engine identifies critical moments, a smaller language model produces the explanation in natural English, and a hand-curated set of pattern detectors flag known motifs (back-rank weakness, isolated queen pawn, knight on rim). Together they produce something that reads like a chess teacher talking.

## What Chessful does not do

Chessful is not a chess.com replacement. It does not have ranked play, leaderboards, or live human matchmaking. The studio's deliberate position is that those products exist and are excellent at competitive play, with the world's best chess infrastructure.

Chessful is for the player who wants to improve on their own against varied opponents, with explanations they can actually read, on a flight, in a kitchen, or between meetings. It needs no account and no internet, and there is no ranking attached to your name to be embarrassed by.

## A small accidentally-personal note

I've never told anyone this in print before, but the reason I made the post-game analysis read like a teacher is that my grandfather was a chess teacher in the Soviet Union before he was anything else. I lost him in 2019. The voice in Chessful's annotations is, I am told by family who would know, more or less his.

It's how the prompts ended up calibrated. If you find the explanations unusually patient, that's why.

[Chessful](/apps/chessful/) is on the App Store. It is free to try, and premium unlocks unlimited analysis and the full forty-opponent roster. If you've been looking for a chess app that explains what you did wrong without making you feel like an idiot, this one might be it.
