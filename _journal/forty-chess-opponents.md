---
layout: journal
slug: forty-chess-opponents
title: "Forty chess opponents, and none of them are me"
date: 2026-02-28
lede: "The single hardest decision in Chessful's design wasn't the engine, the analysis, or the spaced-repetition trainer. It was that the app needed to feel like you were playing forty different people, not the same engine forty times wearing different hats."
read_time: "5 min read"
excerpt: "The story of Chessful's 40 AI opponent personalities — why playing 'the engine at level 7' is unsatisfying, what it took to give each opponent a recognizable style, and how plain-language post-game analysis ended up being the feature users mention most."
---

I learned chess from my grandfather and never got past competent. The reason I built [Chessful](/apps/chessful/) is precisely that gap: I wanted an app that explained what I'd done wrong in a way my grandfather would have, in plain language, instead of pointing at a centipawn evaluation graph and expecting me to read it.

The app shipped with two features that took disproportionate engineering effort. One was the post-game analysis, which is the feature users actually mention. The other was forty distinct AI opponents, which is the feature that quietly carries everything else. This is the post about both.

## The opponent problem

Most chess apps offer a slider. Level 1 (weak) to Level 20 (engine-strong). The slider feels reasonable until you play it for a week and realise something specific:

The engine plays the same way at every level. It just plays *worse on purpose* at lower levels, by adding noise to its evaluation function. Level 5 isn't a different opponent than Level 15. It's the same opponent making mathematically random mistakes. After a dozen games you can feel the noise. The mistakes aren't *wrong* — they're *uncorrelated with style*. No real opponent plays that way.

The result is that improvement against the engine slider doesn't transfer well to playing humans, because humans are not noisy engines. Humans have *characters*. They favour certain openings. They get into trouble in specific structural positions. They have blind spots — the bishop on the long diagonal they always miss, the rook on the seventh rank they always overestimate.

If you're trying to build a chess app for improvement, the slider isn't enough. The app needs opponents that feel like *people*.

## The forty

Chessful ships with forty AI opponents, each with a distinct rating, opening repertoire, structural preferences, and a small set of characteristic blind spots. Every opponent has a name, a portrait, and a one-paragraph backstory. They are explicitly fictional. None of them are designed to imitate any specific real grandmaster — that line is one I won't cross — but each one is recognisable as a *type*.

There's the aggressive Sicilian player who attacks the kingside relentlessly and sometimes overcommits. The positional grinder who exchanges pieces to reach better endgames. The fianchetto specialist who handles the long diagonals beautifully but flails in tactics. The student who plays well in opening theory but forgets it after move twelve. The 1700-rated club player who is slightly drunk on a Tuesday night and slightly sober on a Thursday morning.

Each opponent is built from a base engine with a *style overlay* — modifiers to the evaluation function that nudge it toward characteristic moves, openings, and structural decisions. The implementation is not glamorous. It is mostly piecewise weighting of evaluation features (mobility vs. king safety vs. pawn structure vs. material) tuned by playing thousands of games against a fixed test set and watching for behavioural drift.

What it produces is *recognisability*. After ten games against the aggressive Sicilian player, you start to anticipate her openings. You start to know where her blind spots are. You start to play *against her*, not against an abstract evaluation function. That recognisability is what makes the games feel like games, and it's what makes improvement against Chessful's opponents transfer to playing humans.

## The post-game thing

The other feature that took disproportionate effort is the post-game analysis, and it is genuinely the feature users write to me about.

The standard chess-app analysis flow is: play a game, hit "analyse," watch the engine annotate every move with a depth-15 evaluation. The output is technically correct and almost completely unreadable for anyone below 1800 rating. *"You played 18.Re1, computer prefers 18.Bxh6 with eval +1.4."* Yes, but *why?*

Chessful's analysis tries to answer the *why* in plain language. It identifies the move that lost the game. It identifies the threat the user missed. It explains, in one or two sentences, what was happening structurally. Sometimes it suggests the principle the user should remember — *"Trades that benefit your opponent's pawn structure are usually bad even if material is even"*, or *"This is a known weak square for the bishop in the Caro-Kann"*.

The implementation is a layered model: the engine identifies critical moments, a smaller language model produces the explanation in natural English, and a hand-curated set of pattern detectors flag known motifs (back-rank weakness, isolated queen pawn, knight on rim). The combination produces something that reads like a chess teacher rather than a chess engine.

This was disproportionately hard. It is also the thing users mention most.

## What this is *not*

Chessful is not a chess.com replacement. It does not have ranked play, leaderboards, or live human matchmaking. The studio's deliberate position is that those products exist and are excellent at what they do — competitive play with the world's best chess infrastructure.

What Chessful is for: the player who wants to improve quietly, against varied opponents, with explanations they can actually read, on a flight, in a kitchen, between meetings. No account required. No internet required. No ranking attached to your name that you'll be embarrassed by.

## A small accidentally-personal note

I've never told anyone this in print before, but the reason I made the post-game analysis read like a teacher is that my grandfather was a chess teacher in the Soviet Union before he was anything else. I lost him in 2019. The voice in Chessful's annotations is, I am told by family who would know, more or less his.

That isn't a marketing claim. It's just how the prompts ended up calibrated. If you find the explanations unusually patient, that's why.

[Chessful](/apps/chessful/) is on the App Store. Free to try, premium for unlimited analysis and the full forty-opponent roster. If you've been looking for a chess app that explains what you did wrong without making you feel like an idiot, this one might be it.
