---
layout: journal
slug: how-chessful-builds-adaptive-training
title: "How Chessful turns a Stockfish evaluation into adaptive training"
seo:
  title: "Adaptive Chess Training Built From Your Own Games"
  description: "Adaptive chess training in most apps follows a set curve. Chessful builds drills from the real mistakes in your own games. Here is how the pipeline works."
  keywords:
    - "adaptive chess training"
    - "chess training app"
    - "chess training from your games"
    - "personalized chess training"
    - "chess improvement app"
    - "chessful"
date: 2026-05-13
lede: "Most chess apps that claim 'adaptive training' adapt to a generic difficulty curve over a fixed puzzle pool, not to your games. Chessful adapts to the specific mistake patterns in your real losses. This post is the design note for that engine: how raw centipawn output becomes a motif classification, how motifs become skill-bucket flags, and how those flags become a spaced-repetition training queue. Every step is described, with nothing held back as a secret."
quick_answer: "Chessful's adaptive training works in five stages. Stockfish runs on-device over your finished game and produces a centipawn evaluation per move. A layered classifier (engine output combined with hand-curated motif detectors) assigns each significant mistake to one of roughly thirty motif categories (hung piece, missed fork, weak back rank, prophylactic skip, repertoire lapse, endgame technique error, and so on). Each motif maps to one of five skill dimensions: tactics, defense, positional play, openings, and endgames. After each game, the relevant skill buckets get a flag. A spaced-repetition queue pulls from the flagged buckets: patterns seen most recently come back sooner, and patterns solved correctly twice in a row drop out. Free tier: 3 sessions/week. Premium: unlimited."
faq:
  - q: "What does 'adaptive training' actually mean in Chessful?"
    a: "The training session you get tomorrow is generated from the mistakes in the games you played yesterday, not from a fixed puzzle library. After each game, Chessful sorts your significant mistakes into about thirty motif categories (hung piece, missed fork, weak back rank, prophylactic skip, repertoire lapse, endgame technique error, etc.). Each motif flags one of five skill buckets, and the next training session pulls from the flagged buckets on a spaced-repetition schedule. If you keep hanging pieces, you'll keep seeing hanging-piece positions until you stop."
  - q: "How is this different from chess puzzles?"
    a: "A puzzle is a position with a forcing tactical solution that you have to find. Generic chess puzzles come from a shared pool, ordered by rating or theme. Chessful's training positions come from your own games: the move where you went wrong, plus a few engineered variants on the same motif. The upside is that you drill the exact pattern that beat you, in a form you have already seen once. The downside is that the queue stays thin until you've played a handful of games inside Chessful."
  - q: "Does Chessful use machine learning to classify mistakes?"
    a: "A small on-device language model helps write the plain-language explanations, but the motif classification itself is mostly hand-curated rule-based detection on top of Stockfish output. We chose that on purpose: rules are auditable and stable, while a learned classifier for chess motifs would be opaque and would drift between app updates. The thirty or so motif categories are explicit and listed in the app's documentation."
  - q: "Why does Chessful use spaced repetition?"
    a: "Chess pattern recognition is more a memory task than a calculation task. A 1600 player beats a 1400 player on the same tactical position mostly because the 1600 has seen the pattern often enough to recognise it within two seconds. Spaced repetition is the standard tool for memorising this kind of pattern (Anki popularised it for languages; SuperMemo formalised the underlying schedule decades ago). Chessful uses a Leitner-style schedule: positions seen most recently come back sooner, and positions you've solved correctly twice in a row drop out of rotation."
  - q: "How long does Chessful take to start producing useful training?"
    a: "About three games. The first game gives the engine enough material to flag a couple of motifs. The second either confirms a pattern (you hung another piece, so the back-rank-defender motif gets stronger) or shows a new one. By the third game the spaced-repetition queue has enough flagged positions for a session that doesn't repeat itself. Most users say the training feels 'aimed at me' from game four or five onward."
mentioned_apps:
  - chessful
read_time: "9 min read"
excerpt: "The design note for Chessful's adaptive training engine: how raw Stockfish output becomes a motif classification, how motifs become skill-bucket flags, and how flags become a spaced-repetition queue built from your own losses instead of a generic puzzle pool."
last_updated: 2026-10-26
---

When a chess app says "adaptive training," it usually means one of two things: "we have a difficulty slider," or "we have a recommendation algorithm over a fixed puzzle library." Chessful does neither.

Chessful's adaptive training adapts to **your specific games**. The session you get tomorrow is generated from the mistakes in the games you played yesterday. If you spent last weekend hanging back-rank defenders, this week's queue drills back-rank defenders. If you finally stop doing that and start misjudging king-and-pawn endgames, the queue moves on to opposition technique.

This is the design note for how that works, organised around the five stages between "you played a game" and "tomorrow's training session is ready," in order. None of it is new computer science. It combines well-understood techniques (engine analysis, rule-based classification, spaced repetition), and most of the work went into the judgement calls that decide whether the feature works.

## Stage 1: Stockfish on-device

At the end of every Chessful game, the position goes to a local Stockfish process on the same device. There is no cloud call. The engine's depth is tuned to the device (deeper on Macs and recent iPads, shallower on older iPhones), and it produces a centipawn evaluation per move.

This part of the pipeline looks most like Chess.com, Lichess, and every other chess analyser. It's a commodity. In Chessful, though, the centipawn output is the **input** to the next stage and not the thing the user gets. Other apps show a centipawn graph and call it "analysis," and Chessful is structured specifically to avoid that.

On engine depth: it's tempting to run the engine deeper to find more mistakes, and we decided against it. A 13-ply analysis finds the mistakes that matter for a club player rated 800 to 1800; a 25-ply analysis turns up lines that even good players can't read. We want patterns the user can act on, and a show of engine strength doesn't help with that.

## Stage 2: Motif classification

This is where Chessful departs from other chess analysers. The centipawn evaluation goes through a **layered motif classifier**: hand-curated rule-based detectors plus a small on-device language model. The classifier takes a position where the user lost a significant amount of centipawn value and labels it with one of about thirty motif categories.

Some of the categories (the list isn't complete):

- **Tactical motifs:** hung piece, missed fork, missed pin, missed skewer, missed discovered attack, missed double attack, missed deflection, missed overload, back-rank threat, smothered mate possibility.
- **Defensive motifs:** defender-removal blindness (the piece you captured with was the only defender of another of your pieces), king-safety underestimate, prophylactic skip, weakening pawn push without compensation.
- **Positional motifs:** wrong piece traded (good bishop for a bad knight), wrong side castled, weak square allowed, wrong pawn break, time-on-the-clock-on-the-wrong-move.
- **Opening motifs:** repertoire drift (you deviated from your usual opening setup), book-move missed, transposition into a known-bad line.
- **Endgame motifs:** opposition direction error, king-too-late, wrong rook activation, drawn-but-played-on, wrong-color bishop endgame mistake.

Each significant mistake gets exactly one label, chosen by the strictest matching detector. The rules are ordered and the first match wins, so one position can't be classified as five different things and dilute the training signal.

We use hand-curated rules instead of a learned classifier for two reasons. First, **rules are auditable**: if the trainer drills the wrong pattern, we can read the rule and fix it. A learned classifier for chess motifs would be opaque, and it would drift between app updates as the model gets retrained, so the user's "improvement" might just be the algorithm changing what it counts as a mistake. Second, the **chess motif catalogue is small enough to handle by hand**. Roughly thirty mistake categories matter for club players. Encoding them as rules over the engine's output is real engineering work, but the amount is bounded, and a trained classifier wouldn't beat rules on a problem this constrained.

The small on-device language model works on the explanation layer. It turns the motif label and the engine evaluation into the one or two sentences the user reads, and it doesn't do any classification.

## Stage 3: Skill-bucket flagging

Each of the thirty or so motif categories maps to one of five **skill dimensions**: tactics, defense, positional play, openings, and endgames. When a mistake is classified, its skill bucket gets a flag. The flag holds the motif label, the position, the move you played, the move you should have played, and a plain-language explanation.

You can see the buckets in the app: how many tactical motifs were flagged this week, which ones they were (mostly missed forks? mostly back-rank threats?), and how the count compares with two weeks ago. Premium adds long-term trend graphs (90 / 180 / 365 days), so you can see whether, say, your defense flag count is really going down over a quarter or has levelled off.

Showing this matters because **adaptive training only works if the user trusts the algorithm**. If the next session drills "back-rank threats" and the user has no idea why, they lose interest. If they can see that the algorithm is drilling back-rank threats because they made the same mistake in three of their last five losses, they do the session, and the session works.

## Stage 4: Spaced-repetition queue generation

Each training session pulls a set of positions from the flagged buckets, scheduled with **spaced repetition**.

Spaced repetition is the standard memory technique for pattern recognition. Anki popularised it for languages; SuperMemo formalised the underlying schedule decades ago. The mechanics are simple: positions you've seen recently come back sooner, positions you've solved correctly several times in a row drop out of rotation, and positions you got wrong recently come back fast.

It suits chess because chess pattern recognition is more a **memory task than a calculation task**. A 1600 player beats a 1400 player on the same tactical position mostly because the 1600 has seen the pattern often enough to recognise it within two seconds. Making the 1400 player see the pattern again and again at growing intervals is the right way to teach it. It's dull, and it works.

Chessful uses a Leitner-style schedule (boxes 1 through 5, with intervals of roughly 1 day, 3 days, 7 days, 14 days, and 30 days). A newly flagged motif starts in box 1. A correct solve moves it up a box; a wrong one sends it back to box 1. After two correct solves in box 5 the motif leaves rotation, though it can come back if a new game flags the same motif again.

**Free tier: three sessions per week.** Three sessions cover the highest-priority bucket flags, but you have to choose. Premium gives unlimited sessions. Premium makes sense for players who are serious about improving; the free tier is real training for casual players.

## Stage 5: Skill graphs and the feedback loop

After each session the graphs for each skill dimension update. The Free tier shows the current week and the previous week. Premium adds 90 / 180 / 365-day views.

The graphs exist for the **feedback loop**. If you're three weeks into drilling defense motifs and the defense bucket count is still going up, the drills aren't working and you need to try something else. Maybe the motif you keep missing isn't a defense problem at all but a calculation problem that's been misclassified. Maybe you're tired and rushing the drills. Maybe you're playing in time trouble, the motif is fine, and time management is what's holding you back. The graphs let you answer those questions.

This part of the engine takes longest to pay off. Most users ignore the trend graphs until they've used the app for a month or two. After that, the graphs are what keep them training, because they can see the curve move, or see that it doesn't, and react.

## What adaptive training in Chessful doesn't do

- **It doesn't replace studying.** Drilling motifs from your own games closes specific gaps, but you still need to work through an endgame book or a structured course on the Sicilian Dragon. Many improving players use Chessful alongside Magnus Trainer, Chessable, or printed books. Structured study and adaptive drilling on your real losses add up.
- **It doesn't replace playing.** The engine needs your games to work with. Chessful has 40 AI opponents to play against, but the training queue depends on having games to draw from. Three games is the minimum for useful training; at ten games the queue gets really specific.
- **It doesn't replace live human play.** Chessful has no live matchmaking and we aren't planning to add it. Our view is that the improvement that happens between games has too few tools, while Chess.com and Lichess cover live play well. The two complement each other.
- **It isn't personalised by an opaque AI.** The motif categories and skill buckets are explicit, and the spaced-repetition schedule is well known. You can read what the trainer is doing and argue with it.

## Why publish this

Most chess apps with adaptive training don't say what the algorithm does. Usually it isn't a trade secret. "Adaptive training" often just means "we picked a difficulty curve," and saying so would deflate the marketing. By publishing ours we're saying there is a real mechanism here, built on established techniques (Stockfish + rules + Leitner-style spaced repetition), and you can check over a month of your own games whether it works.

It's also because **we publish our algorithms by default at Lagerland**. Plateau detection in [GymLogger X](/apps/gymlogger-x/) is documented the same way. The pattern recognition rules in [Observa](/apps/observa/) are published. The Plan Mode template engine in [Soon.](/apps/soon/) is [documented in a separate post](/journal/how-plan-mode-builds-a-checklist/). Across the catalogue, if the algorithm is the product, people should be able to read it.

---

[Chessful is available on the App Store.](https://apps.apple.com/app/id6761336870) The free tier includes 40 AI opponents, Stockfish analysis on every game, plain-language mistake summaries, and three training sessions per week. Premium unlocks unlimited deep analysis, unlimited adaptive training, full progress tracking with 90/180/365-day skill-trend graphs, and alternative-move exploration: {P_MONTHLY@chessful}/month, {P_YEARLY@chessful}/year, or {P_LIFETIME@chessful} once for lifetime access with a 7-day free trial. The companion design note on the forty AI opponents is [Forty chess opponents, and none of them are me](/journal/forty-chess-opponents/).
