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
lede: "Most chess apps that claim 'adaptive training' adapt to a generic difficulty curve over a fixed puzzle pool, not to your games. Chessful adapts to the mistakes in your real games. This post is the design note for how that works: how an on-device Stockfish review becomes a set of explained mistakes, how those mistakes feed your skill profile, and how they come back as daily training and spaced review."
quick_answer: "Chessful's adaptive training works in five steps. Stockfish runs on your device over a finished game and rates every move, from Brilliant to Blunder. Each mistake gets one of 10 types (such as Hanging Piece, Missed Fork, or Endgame Error) and a plain-language explanation at your level: what you played, what was best, why it works, and the line that punishes your move. Those mistakes feed five skill bars: Tactics, Defense, Positioning, Endgame, and Openings. Today's Training then picks a focus area and turns your mistakes into a 5, 10, or 15-minute puzzle session, and Review past mistakes brings old misses back on a spaced-repetition (SM-2) schedule. Free: 2 analyses, 3 puzzles, and 2 coach hints a day. Premium: no daily limits."
faq:
  - q: "What does 'adaptive training' actually mean in Chessful?"
    a: "The training you get is built from the mistakes in the games you have played, not from a fixed puzzle library. After a game, Stockfish reviews every move on your device and each mistake gets one of 10 types, such as Hanging Piece, Missed Fork, Missed Pin, Back-Rank Weakness, or Endgame Error. Those mistakes feed your skill profile, and Today's Training turns them into puzzles in the area that needs work. Review past mistakes then brings your misses back on a spaced-repetition schedule until you stop making them."
  - q: "How is this different from chess puzzles?"
    a: "A puzzle is a position with a forcing solution you have to find. Generic puzzles come from a shared pool, ordered by rating or theme. Chessful has that too: a tactics library of 15,000 puzzles in 53 themes. Its daily training starts from your own games instead, so you drill the pattern that actually cost you points, in a position you have already seen once. The trade-off is that daily training needs at least one played and analysed game before it unlocks."
  - q: "How does Chessful decide what type of mistake I made?"
    a: "Stockfish measures how much each move costs you, and Chessful labels every significant mistake with one of 10 types: Hanging Piece, Missed Fork, Missed Pin, Back-Rank Weakness, Poor King Safety, Passive Move, Tactical Oversight, Missed Tactic, Endgame Error, or Opening Inaccuracy. Severity is Inaccuracy, Mistake, or Blunder. The explanation is worded for the coaching level you choose, from 'Just learning the rules' to 'Rated player (1400+)'."
  - q: "Why does Chessful use spaced repetition?"
    a: "Chess pattern recognition is more a memory task than a calculation task. A stronger player often wins the same tactical position because they have seen the pattern often enough to recognise it in seconds. Spaced repetition is the standard tool for memorising this kind of pattern (Anki popularised it for languages; SuperMemo formalised the underlying schedule decades ago). Chessful's Review past mistakes uses the SM-2 schedule: a miss comes back soon, and a position you solve comes back at growing intervals. Review sessions don't count toward the free daily puzzles."
  - q: "How long does Chessful take to start producing useful training?"
    a: "Training unlocks after you play and analyse your first game. One game is enough to produce mistakes to drill, and each game you add gives Today's Training and your skill bars more to work with. You can also import your Chess.com or Lichess games as a PGN file to give it a head start."
mentioned_apps:
  - chessful
read_time: "7 min read"
excerpt: "The design note for Chessful's adaptive training: how an on-device Stockfish review becomes 10 types of explained mistakes, how those mistakes feed five skill bars, and how they come back as daily training and spaced review built from your own games instead of a generic puzzle pool."
last_updated: 2026-10-29
---

When a chess app says "adaptive training," it usually means one of two things: "we have a difficulty slider," or "we have a recommendation algorithm over a fixed puzzle library." Chessful does neither.

Chessful's adaptive training adapts to **your games**. The training you get is built from the mistakes in the games you have played. If you spent last weekend leaving pieces hanging, your training drills hanging pieces. If you stop doing that and start misplaying king-and-pawn endgames, the focus moves to endgames.

This is the design note for how that works, organised around the five steps between "you played a game" and "your next training session is ready." None of it is new computer science. It combines well-understood techniques (engine analysis, a fixed set of mistake types, spaced repetition), and most of the work went into the judgement calls that decide whether the feature helps.

## Step 1: Stockfish on your device

When a game ends, Game Review runs Stockfish on the same device. There is no cloud call; the app has no networking code of its own. Stockfish checks every move and rates it: Brilliant, Great move, Best move, Good, Book, Inaccuracy, Mistake, or Blunder. You get an accuracy figure, the key moments, an evaluation view, and the best line, which you can step through.

This part looks like every other chess analyser, and it's a commodity. In Chessful the engine output is the **input** to the next step and not the thing you're left with. A centipawn graph on its own tells you where a game turned, and it doesn't tell you what to practise.

Free players get 2 analyses a day; Premium removes the limit. Games you play against Chessful's opponents count, and so do games you import as a PGN file from Chess.com or Lichess.

## Step 2: Every mistake explained, with a type

This is where Chessful departs from a plain analyser. Each significant mistake opens a **Mistake Detail**: what you played, what was best, how big the evaluation drop was, a plain-language explanation, why the suggested move works, and the line that punishes your move.

Each mistake also carries one of **10 types**:

- **Hanging Piece**
- **Missed Fork**
- **Missed Pin**
- **Back-Rank Weakness**
- **Poor King Safety**
- **Passive Move**
- **Tactical Oversight**
- **Missed Tactic**
- **Endgame Error**
- **Opening Inaccuracy**

Severity is graded separately: Inaccuracy, Mistake, or Blunder.

We kept the list short on purpose. A long catalogue of fine-grained motifs sounds impressive, but it spreads your mistakes thin, and a type you see once a month gives you nothing to train. Ten types are few enough that the same ones keep showing up in your games, and that repetition is what makes them trainable.

The explanation is worded for your level. In onboarding or Settings you choose a coaching level, from "Just learning the rules" to "Rated player (1400+)", and the same mistake is explained differently for each. From any mistake, **Train This Pattern** takes you straight to practice.

## Step 3: Your skill profile

Analysed mistakes feed a **skill profile** with five skill bars: Tactics, Defense, Positioning, Endgame, and Openings. A bar says "Not measured yet" until there is data behind it. Progress also shows an estimated rating, your game stats, a rating graph, and highlight cards for your strongest area and your focus area. All of that is free.

Premium adds **Weekly Comparison** and **Weakness Trends**, so you can see whether the weaknesses you've been drilling are shrinking or holding steady.

Showing this matters because **adaptive training only works if you trust it**. If the next session drills back-rank weaknesses and you have no idea why, you lose interest. If you can see that your Defense bar is the lowest and your last games keep showing the same mistake type, you do the session, and the session works.

## Step 4: Today's Training and spaced review

**Today's Training** is a daily session built from your own mistakes. It picks a focus area (Tactics, Defense, Positioning, Endgame, or Openings), and you choose 5, 10, or 15 minutes, which is 3, 5, or 8 puzzles. A session opens with a concept card, then asks you to find the best move. If you miss a puzzle, you play the correct move yourself before moving on, and the 10 and 15-minute sessions end with a short Reflect step. Score under 70% and Chessful offers to re-drill the misses.

Alongside it, **Review past mistakes** brings positions from your old mistakes back on a spaced-repetition schedule, with "N due today" until you're caught up.

Spaced repetition is the standard memory technique for pattern recognition. Anki popularised it for languages; SuperMemo formalised the underlying schedule decades ago. Chessful uses SM-2, the SuperMemo algorithm: a position you miss comes back soon, and a position you solve comes back at growing intervals.

It suits chess because chess pattern recognition is more a **memory task than a calculation task**. A stronger player often wins the same tactical position because they've seen the pattern often enough to recognise it in seconds. Seeing the pattern again and again at growing intervals is a good way to learn it. It's dull, and it works.

**Free: 3 puzzles a day.** Today's Training, lesson practice, and the 15,000-puzzle tactics library share that one counter. Review past mistakes and retrying your misses don't use it up. Premium removes the daily limit.

## Step 5: The feedback loop

After you train and play, your skill bars and rating graph update, and with Premium, Weekly Comparison and Weakness Trends show how each weakness is moving.

That view exists for the **feedback loop**. If you've spent weeks on Defense and the same mistake types keep appearing, the drills aren't working and you need to try something else. Maybe what you keep missing is a calculation problem more than a defensive one. Maybe you're tired and rushing. Progress gives you a way to ask those questions about your own games.

This part takes longest to pay off. It only says something once you've played and analysed enough games for a trend to form.

## What adaptive training in Chessful doesn't do

- **It doesn't replace studying.** Drilling your own mistakes closes specific gaps, but structured study still matters. Chessful's 156 lessons cover the basics through to strategy, and a good endgame book or opening course adds to that. Structured study and drilling your real losses add up.
- **It doesn't replace playing.** The training needs your games to work with. Chessful has 40 opponents from 400 to 2400 Elo (the first 10 are free), and you can import your own games as PGN, but the training only knows what you've played.
- **It doesn't replace live human play.** Chessful has no online play, matchmaking, or clocks; every game is against its built-in opponents. Chess.com and Lichess cover live play well, and the two complement each other.
- **It isn't a black box.** The 10 mistake types and five skill bars are visible in the app, and spaced repetition on SM-2 is a well-known schedule. You can see what the trainer is doing and why, and argue with it.

## Why publish this

Most chess apps with adaptive training don't say what the algorithm does. Usually it isn't a trade secret. "Adaptive training" often just means "we picked a difficulty curve," and saying so would deflate the marketing. By describing ours we're saying there is a real mechanism here, built on established techniques (Stockfish, a fixed set of mistake types, SM-2 spaced repetition), and you can check over a month of your own games whether it works.

We try to explain how our apps reach their answers. [Observa](/apps/observa/) lists the weights behind its Readiness score on its app page, and [Soon.](/apps/soon/) has [a separate post on Plan mode](/journal/how-plan-mode-builds-a-checklist/). If the method is the product, people should be able to read it.

---

[Chessful is available on the App Store.](https://apps.apple.com/app/id6761336870) The free version includes all 156 lessons, the first 10 of the 40 opponents, the first endgame in each category, every mistake explanation, PGN import, and progress tracking, with 2 game analyses, 3 puzzles, and 2 coach hints a day. Premium removes the daily limits and unlocks all 40 opponents, all 96 endgames, the full opening repertoire with line drills, and Weekly Comparison and Weakness Trends. It costs {P_MONTHLY@chessful}/month or {P_YEARLY@chessful}/year, each with a {TRIAL@chessful}, or {P_LIFETIME@chessful} once for lifetime access. The companion design note on the forty opponents is [Forty chess opponents, and none of them are me](/journal/forty-chess-opponents/).
