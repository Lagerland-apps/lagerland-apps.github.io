---
layout: journal
slug: how-chessful-builds-adaptive-training
title: "How Chessful turns a Stockfish evaluation into adaptive training"
date: 2026-05-13
lede: "Most chess apps that claim 'adaptive training' don't actually adapt to your games — they adapt to a generic difficulty curve over a fixed puzzle pool. Chessful adapts to the specific mistake patterns in your real losses. This post is the design note for that engine: how raw centipawn output becomes a motif classification, how motifs become skill-bucket flags, and how skill-bucket flags become a spaced-repetition training queue. No marketing. No black box."
quick_answer: "Chessful's adaptive training works in five stages. Stockfish runs on-device over your finished game and produces a centipawn evaluation per move. A layered classifier — engine output combined with hand-curated motif detectors — assigns each significant mistake to one of roughly thirty motif categories (hung piece, missed fork, weak back rank, prophylactic skip, repertoire lapse, endgame technique error, and so on). Each motif maps to one of five skill dimensions: tactics, defense, positional play, openings, endgames. After each game, the relevant skill buckets get a flag. A spaced-repetition queue pulls from the flagged buckets — patterns seen most recently are seen again sooner; patterns solved correctly twice in a row drop out. Free tier: 3 sessions/week. Premium: unlimited."
faq:
  - q: "What does 'adaptive training' actually mean in Chessful?"
    a: "It means the training session you get tomorrow is generated from the mistakes in the games you played yesterday — not from a fixed puzzle library. After each game, Chessful classifies your significant mistakes into one of about thirty motif categories (hung piece, missed fork, weak back rank, prophylactic skip, repertoire lapse, endgame technique error, etc.). Each motif flags one of five skill buckets. The next training session pulls from the flagged buckets using a spaced-repetition schedule. If you keep hanging pieces, you'll keep seeing hanging-piece positions until you stop hanging pieces."
  - q: "How is this different from chess puzzles?"
    a: "Puzzles are positions where there's a forcing tactical solution and you have to find it. Generic chess puzzles are pulled from a shared pool and ordered by rating or theme. Chessful's training positions are pulled from your own games — the actual move where you went wrong, plus a few engineered variants on the same motif. The advantage is that you're drilling the exact pattern that broke you, in a form your brain has already seen once. The disadvantage is that until you've played a handful of games inside Chessful, the queue is thin."
  - q: "Does Chessful use machine learning to classify mistakes?"
    a: "A small on-device language model contributes to the plain-language explanation layer, but the motif classification itself is mostly hand-curated rule-based detection on top of Stockfish output. We did this deliberately: rules are auditable and stable; a learned classifier on chess motifs would be opaque and would drift between app updates. The thirty-ish motif categories are explicit and inspectable in the app's documentation."
  - q: "Why does Chessful use spaced repetition?"
    a: "Because chess pattern recognition is a memory task more than a calculation task. The reason a 1600 player beats a 1400 player on the same tactical position is mostly that the 1600 has seen the pattern enough times to recognise it within two seconds. Spaced repetition is the established memory-encoding tool for this kind of pattern recognition (Anki popularised it for languages; SuperMemo formalised the underlying schedule decades ago). Chessful uses a Leitner-style schedule: positions seen most recently are seen again sooner; positions you've solved correctly twice in a row drop out of rotation."
  - q: "How long does Chessful take to start producing useful training?"
    a: "About three games. The first game gives the engine enough material to flag a couple of motifs. The second game either confirms a pattern (you hung another piece — the back-rank-defender motif gets stronger) or reveals a new one. By the third game, the spaced-repetition queue has enough flagged positions to produce a session that isn't redundant. Most users report the training feels noticeably 'aimed at me' from game four or five onward."
mentioned_apps:
  - chessful
read_time: "9 min read"
excerpt: "The design note for Chessful's adaptive training engine — how raw Stockfish output becomes motif classification, how motifs become skill-bucket flags, and how flags become a spaced-repetition queue derived from your own losses, not a generic puzzle pool."
---

Most chess apps that say "adaptive training" mean one of two things. They either mean "we have a difficulty slider," or they mean "we have a recommendation algorithm over a fixed puzzle library." Neither of those is what Chessful does.

Chessful's adaptive training adapts to **your specific games**. The training session you get tomorrow is generated from the mistakes in the games you played yesterday. If you spent last weekend hanging back-rank defenders, this week's training queue is going to drill back-rank defenders. If you finally stopped doing that and started misjudging king-and-pawn endgames, the queue is going to start drilling opposition technique.

This is the design note for how that works. The post is structured around the five stages between "you played a game" and "tomorrow's training session is ready," in order. Nothing here is novel computer science — it's the application of well-understood techniques (engine analysis, rule-based classification, spaced repetition) glued together with the specific judgement calls that make the difference between a feature that works and one that doesn't.

## Stage 1: Stockfish on-device

Every Chessful game ends with the position passed into a local Stockfish process running on the same device. There is no cloud call. The engine runs at a depth tuned to the device — deeper on Macs and recent iPads, shallower on older iPhones — and produces a centipawn evaluation per move.

This is the part of the pipeline that most directly resembles what Chess.com, Lichess, and every other chess analyser does. It's a commodity. The difference is that for Chessful, the centipawn output is not the product — it's the **input** to the next stage. Showing a user a centipawn graph and calling that "analysis" is what every other app does, and it's exactly the move Chessful is structured to avoid.

A note on engine depth: there's a tempting design pressure to crank the engine deeper to find more mistakes. We chose not to. A 13-ply analysis at club level finds the mistakes that actually matter for an 800–1800 rated player; a 25-ply analysis surfaces lines that even good players can't read. The point is to identify the patterns the user can act on, not to demonstrate engine strength.

## Stage 2: Motif classification

This is where Chessful diverges from every other chess analyser. The centipawn evaluation is run through a **layered motif classifier**: hand-curated rule-based detectors plus a small on-device language model. The job of the classifier is to take a position where the user lost a significant amount of centipawn value and label it with one of about thirty motif categories.

A non-exhaustive list of the categories:

- **Tactical motifs:** hung piece, missed fork, missed pin, missed skewer, missed discovered attack, missed double attack, missed deflection, missed overload, back-rank threat, smothered mate possibility.
- **Defensive motifs:** defender-removal blindness (the piece you captured with was your own piece's only defender), king-safety underestimate, prophylactic skip, weakening pawn push without compensation.
- **Positional motifs:** wrong piece traded (good bishop for a bad knight), wrong side castled, weak square allowed, wrong pawn break, time-on-the-clock-on-the-wrong-move.
- **Opening motifs:** repertoire drift (you deviated from your usual opening setup), book-move missed, transposition into a known-bad line.
- **Endgame motifs:** opposition direction error, king-too-late, wrong rook activation, drawn-but-played-on, wrong-color bishop endgame mistake.

Each significant mistake gets exactly one label. The label is chosen by the strictest matching detector — the rules are ordered and the first match wins, to avoid the failure mode where one position gets classified as five different things and dilutes the training signal.

Why hand-curated rules and not a learned classifier? Two reasons. First, **rules are auditable**: if the trainer is drilling the wrong pattern, we can read the rule and fix it. A learned classifier on chess motifs would be opaque — and worse, would drift between app updates as the model gets retrained, which means the user's "improvement" might be the algorithm changing what it considers a mistake rather than the user actually improving. Second, the **chess motif catalogue is small enough to be tractable**. There are roughly thirty mistake categories that matter for club players. Encoding them as rules over the engine's output is engineering work, but it's bounded engineering work. Training a classifier wouldn't beat rules at a problem this constrained.

The small on-device language model contributes to the explanation layer — turning the motif label and the engine evaluation into the one or two sentences the user actually reads. It doesn't do the classification.

## Stage 3: Skill-bucket flagging

Each of the thirty-ish motif categories maps to one of five **skill dimensions**: tactics, defense, positional play, openings, endgames. When a mistake is classified, the corresponding skill bucket gets a flag. The flag includes the motif label, the position, the move you played, the move you should have played, and a plain-language explanation.

The buckets are visible inside the app. You can see exactly how many tactical motifs were flagged this week, which specific tactical motifs they were (mostly missed forks? mostly back-rank threats?), and how the count compares to two weeks ago. Premium adds long-term trend graphs (90 / 180 / 365 days) so you can see whether (say) your defense flag count is actually trending down over a quarter, or whether you're plateauing.

This visibility matters because **adaptive training depends on the user trusting the algorithm**. If the next training session is drilling "back-rank threats" and the user has no idea why, the user disengages. If the user can see — "right, the algorithm is drilling back-rank threats because I made the same mistake in three of my last five losses" — the user does the session and the session works.

## Stage 4: Spaced-repetition queue generation

Each training session pulls a set of positions from the flagged buckets, scheduled with **spaced repetition**.

Spaced repetition is the established memory-encoding tool for pattern recognition. Anki popularised it for languages; SuperMemo formalised the underlying schedule decades ago. The mechanic is simple: positions you've seen recently are seen again sooner; positions you've solved correctly multiple times in a row drop out of rotation; positions you got wrong recently come back fast.

The reason it works for chess specifically is that chess pattern recognition is a **memory task more than a calculation task**. The reason a 1600 player beats a 1400 player on the same tactical position is mostly that the 1600 has seen the pattern enough times to recognise it within two seconds. Forcing the 1400 player to see the pattern repeatedly at increasing intervals is the right pedagogic move. It's not glamorous, but it's correct.

Chessful uses a Leitner-style schedule (boxes 1 through 5, intervals roughly 1 day, 3 days, 7 days, 14 days, 30 days). A new flagged motif starts in box 1. A correct solve moves it up a box; an incorrect solve drops it back to box 1. After two correct solves at box 5, the motif graduates out of rotation — though it can come back if the same motif gets re-flagged from a new game.

**Free tier: three sessions per week.** Three sessions is enough to cover the highest-priority bucket flags but forces the user to choose. Premium: unlimited sessions. The Premium upgrade is the right move for serious improvers; the free tier is honest training for casual players.

## Stage 5: Skill graphs and the feedback loop

After each session, the per-skill-dimension graphs update. The Free tier shows the current week and the previous week. Premium adds 90 / 180 / 365-day views.

The reason these graphs matter is the **feedback loop**. If you're three weeks into drilling defense motifs and the defense bucket count is still rising rather than falling, that's a signal that the drills aren't working — you need a different intervention. Maybe the motif you're missing isn't actually a defense problem; maybe it's a calculation problem you've been mis-classifying. Maybe you're tired and rushing on the drills. Maybe you're playing in time-trouble and the motif is fine but the time management is the real bottleneck. The graphs make those questions answerable.

This is the part of the engine that takes the longest to surface. Most users don't engage with the trend graphs until they've been using the app for a month or two. But once they do, the trend graphs become the thing that keeps them training — because they can see the curve moving, or notice when it's not, and respond.

## What this isn't

A few things adaptive training in Chessful deliberately is not:

- **It's not a replacement for studying.** Drilling motifs from your own games closes specific gaps, but it doesn't replace working through an endgame book or a structured course on the Sicilian Dragon. Many improving players run Chessful alongside Magnus Trainer, Chessable, or printed books. The two layers — structured study and adaptive drilling on your real losses — compound.
- **It's not a replacement for playing.** You need to play games for the engine to have material to work with. Chessful provides 40 AI opponents to play against, but the training queue depends on having games to draw from. Three games is the minimum useful threshold; ten games is where the queue gets really specific.
- **It's not a replacement for live human play.** Chessful has no live matchmaking and isn't planning to add it. The thesis is that the part of improvement that happens between games is under-tooled. Live play is well-tooled by Chess.com and Lichess. They're complementary categories, not competing ones.
- **It's not personalised by an opaque AI.** The motif categories are explicit, the skill buckets are explicit, the spaced-repetition schedule is well-known. Nothing about the trainer is a black box — you can read what it's doing and argue with it.

## Why publish this

Most chess apps with adaptive training don't disclose what the algorithm does. The reason isn't usually proprietary — it's that "adaptive training" usually means "we picked a difficulty curve" and saying so would deflate the marketing. Publishing the algorithm is a way of saying: there's a real mechanism here, it's based on established techniques (Stockfish + rules + Leitner-style spaced repetition), and you can verify it works on your own games over the course of a month.

It's also a way of saying that **algorithmic transparency is a Lagerland default**. Plateau detection in [GymLogger X](/apps/gymlogger-x/) is documented the same way. The pattern recognition rules in [Observa](/apps/observa/) are published. The Plan Mode template engine in [Soon.](/apps/soon/) is [documented in a separate post](/journal/how-plan-mode-builds-a-checklist/). The principle is the same across the catalogue: if the algorithm is the product, the algorithm should be readable.

---

[Chessful is available on the App Store.](https://apps.apple.com/app/id6761336870) Free tier covers 40 AI opponents, Stockfish analysis on every game, plain-language mistake summaries, and three training sessions per week. Premium unlocks unlimited deep analysis, unlimited adaptive training, full progress tracking with 90/180/365-day skill-trend graphs, and alternative-move exploration: €2.99/month, €19.99/year, or €39.99 once for lifetime access with a 7-day free trial. The companion design note on the forty AI opponents lives at [Forty chess opponents, and none of them are me](/journal/forty-chess-opponents/).
