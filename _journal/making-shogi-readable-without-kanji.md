---
layout: journal
slug: making-shogi-readable-without-kanji
title: "Making shogi readable — designing a board you can play before you can read it"
date: 2026-06-11
lede: "The hardest problem in building a shogi app for Western players isn't the engine, the drop rules, or uchifuzume edge cases. It's that half your prospective users cannot read the pieces — and every existing app treats that as the user's problem."
quick_answer: "Shogiful ships a Western piece set with symbolic icons and movement indicators so the shogi board is readable from the first game, defaults to it outside Japanese locales, keeps a piece guide one tap from every game, and introduces the traditional kanji progressively through training — treating the kanji as the destination, not the entry fee. This post is the design story behind those decisions."
faq:
  - q: "Why do shogi pieces use kanji instead of distinct shapes?"
    a: "All shogi pieces share the same pentagonal wedge shape, differentiated only by the characters written on them — direction is shown by which way the wedge points, and ownership changes when a captured piece is reused, so shape and color can't encode identity the way chess pieces do. The characters are the identity. That's elegant if you read them and a wall if you don't."
  - q: "Can you really learn shogi without learning the kanji?"
    a: "You can learn shogi without learning kanji first. Shogiful's Western set encodes each piece's identity and movement in the icon itself, so the game is playable immediately. The kanji are then introduced progressively while you train — most players find they've absorbed the eight base characters within a few weeks of play, because they learned the pieces' behavior first and attached the symbol afterward."
  - q: "Do serious shogi players use Western piece sets?"
    a: "Mostly no — and that's fine. Printed material, Japanese apps, and real boards all use kanji pieces, so anyone continuing into the shogi world needs them eventually. Shogiful treats the Western set as a ramp, not a replacement: it defaults to Western outside Japanese locales, but the traditional set is always one toggle away and the training system actively teaches the characters."
  - q: "What's different about Shogiful's Western pieces compared to other internationalized sets?"
    a: "Two things: movement indicators and promotion design. Each Shogiful icon carries a small movement diagram, so the piece teaches its own legal moves — important in shogi, where golds, promoted silvers, promoted knights, and promoted lances all move identically and need to be visually related. Promoted pieces get a distinct icon state rather than just a color swap, mirroring how traditional sets flip to red characters."
mentioned_apps:
  - shogiful
read_time: "6 min read"
excerpt: "The design story behind Shogiful's Western piece set: why kanji pieces are the single biggest barrier to shogi outside Japan, what a readable board actually requires, and how the app teaches you the traditional characters anyway — after you can already play."
---

I built [Shogiful](/apps/shogiful/) after watching the same thing happen three times: a chess-playing friend gets curious about shogi — an anime, a YouTube video, the fact that captured pieces come back — installs an app, opens it, stares at a 9×9 grid of wooden wedges with characters they cannot read, and quietly closes it. Not because the rules are hard. They never got to the rules.

Chess players are the natural audience for shogi outside Japan, and the kanji pieces filter most of them out at the door. Every product decision in Shogiful starts from that fact.

## Why shogi pieces can't just be redrawn like chess pieces

The obvious question is: why not just draw a knight as a horse, like chess? The answer is that shogi's piece design is load-bearing in ways chess's isn't.

All forty pieces are the same shape — a pentagonal wedge — and the same color. There are no black and white armies. Ownership is shown by which way the wedge points, because that has to survive the defining rule of shogi: when you capture a piece, it joins *your* hand and can be dropped back onto the board fighting for you. A piece changes sides several times in a normal game. Fixed colors would lie about ownership; the rotating wedge can't.

So the characters are doing all the identity work. 歩 is a pawn, 銀 is a silver, 飛 is a rook. Flip a piece over on promotion and the character changes — usually to red — because promotion in shogi is a state change, not a piece swap. It's a beautifully compact system *if you read the characters*. If you don't, every piece on the board is the same piece.

Chess never has this problem, which is why "I'll just learn the six piece shapes" works there and nothing equivalent works in shogi. Eight base pieces, six of which promote, all sharing one silhouette: that's fourteen states to distinguish by character alone.

## What a readable board actually requires

The fix sounds trivial — "use Western icons" — and several apps offer internationalized piece options. Building one that actually works taught me it has three separate requirements, and most sets stop after the first.

**Identity.** Each piece needs a distinct, instantly-parseable symbol. This is the easy part.

**Movement.** This is the part that matters. A chess player meeting shogi for the first time doesn't know that a lance only moves straight forward, that a knight has exactly two squares it can ever jump to, or that a silver can't step sideways. Shogiful's Western icons carry a small movement diagram in the piece itself — the icon teaches its own legal moves. This pays off most with the promoted pieces: a promoted silver, promoted knight, promoted lance, and promoted pawn all move identically to a gold, and the icons make that family resemblance visible instead of asking you to memorize four arbitrary facts.

**Promotion state.** Traditional sets flip the piece to red characters. A Western set needs an equally unmissable state change — Shogiful uses a distinct promoted icon, not just a tint, because "did that silver promote?" is exactly the question you can't afford to get wrong when you're calculating whether it can retreat. (It can't step diagonally backward anymore. Ask me how I learned to double-check that.)

There's one more decision hiding in plain sight: the default. Shogiful defaults to the Western set outside Japanese locales. A defaults screen on first launch asking a brand-new player to choose between "traditional" and "Western" pieces is asking them to make an informed decision before they've seen the board. The locale already answered the question; the toggle in Settings is for when they're ready to change their mind.

## The kanji are the destination, not the entry fee

Here's where I'll be honest about the trade-off, because it's real: the broader shogi world runs on kanji. Books, problem collections, Japanese apps, real boards, every diagram on every shogi site — all kanji. A player who stays on Western pieces forever has a ceiling on what they can read.

So Shogiful is built to make its own Western set temporary. The piece guide is one tap away in every game, showing each piece in both styles side by side. Training sessions introduce the characters progressively — you learn 銀 *after* you already know how a silver behaves, which turns out to be dramatically easier than learning the symbol and the behavior at once. The traditional set is always one toggle away, and the app quietly expects you to flip it eventually.

That sequencing — behavior first, symbol second — is the entire thesis. Nobody learns chess by memorizing the letters K, Q, R, B, N before their first game. Shogi outside Japan has effectively been demanding the equivalent for decades, and then wondering why the game doesn't travel.

## Where this fits in the bigger app

The readable board is the front door; the reason Shogiful exists is what's behind it — every game analyzed on-device by [YaneuraOu](https://github.com/yaneurao/YaneuraOu), mistakes explained in plain-language sentences (the missed knight-drop fork, the edge pawn that cracked your castle), and training generated from your own recurring errors. None of that coaching works if the player bounced off the board on day one. The piece set isn't a feature; it's the precondition for all the other features.

Shogiful is on the [App Store](https://apps.apple.com/app/id6761656926) for iPhone, iPad, and Mac — free to try, with the full coaching loop from $1.99/month or $19.99 once. The [app page](/apps/shogiful/) has the methodology, the honest comparison with the online platforms, and six worked examples of what a plain-language shogi mistake looks like.
