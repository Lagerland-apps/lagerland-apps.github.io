---
layout: journal
slug: making-2048-a-real-3d-board
title: "Making 2048 a real 3D board"
date: 2026-06-22
seo:
  title: "Making 2048 a Real 3D Board: A Design Story"
  description: "How we rebuilt flat 2048 as a real 3D board you can tilt — keeping it instantly readable, turning tiles into materials, and funding craft, not ads."
  keywords:
    - 3d 2048
    - 2048 in 3d
    - 2048 game design
    - how 2048 works
    - ad-free game design
    - mobile puzzle design
    - 2048 board
    - tactile game design
lede: "2048 is a flat game. It has always been a flat game: a 4×4 grid of coloured squares that slide and add up. The obvious question, building Zen 2048, was whether it had to stay flat — and the harder question was whether making it three-dimensional would ruin the one thing that makes 2048 work."
quick_answer: "Zen 2048 renders the classic 2048 puzzle as a real 3D board you can tilt and spin, rather than a flat grid with a drop shadow. The design constraint was legibility: a swipe-merge puzzle has to be readable at a glance, so the 3D camera returns to a clean top-down view the instant you swipe, and the depth is there for appreciation and tilt, not for playing blind. Each of the 17 themes is a real material — glass, ceramic, paper, metal, neon, pastel, monochrome — with its own lighting, tile physics, and merge animation, not a recoloured copy. The work is funded by optional theme packs rather than ads, which is the whole point: a number puzzle this small should never cost you a video ad per game."
faq:
  - q: "Is there a 3D version of 2048?"
    a: "Yes — Zen 2048 renders the board in real 3D. You can tilt your phone or drag to rotate the board to any angle and watch the tiles catch the light, and it snaps back to a clean top-down view the moment you swipe so play is never harder than on a flat board. It's genuine, interactive depth rather than a fixed 3D-styled picture. The classic 2048 rules are unchanged; only the way the board looks and feels is new."
  - q: "Doesn't making 2048 3D make it harder to read?"
    a: "It would, if the camera stayed tilted while you played — which is exactly why it doesn't. The core insight is that 2048 lives or dies on instant legibility: you have to read the whole board in a fraction of a second to plan a swipe. So in Zen 2048 the 3D tilt is something you opt into between moves, and the board returns to a clean, near-top-down read the instant you swipe. You get the depth without paying for it in playability."
  - q: "What makes each Zen 2048 theme different — is it just a colour swap?"
    a: "No. Each of the 17 themes is treated as a real material with its own properties: the gloss and refraction of glass, the matte grain of ceramic, the soft fibre of paper, the brushed sheen of metal, the glow of neon. Beyond colour, a theme defines its own tile lighting, drop-shadow geometry, rim light, the spring physics of how tiles slide, the timing and softness of the merge flash, and a slow atmospheric drift in the background. Switching theme changes how the board moves and lights, not just its palette."
  - q: "Why does Zen 2048 charge for themes instead of just showing ads?"
    a: "Because the alternative is worse for the game. Almost every free 2048 on the App Store is funded by advertising — pre-roll video, interstitials, reward loops — which actively degrades the act of playing. Zen 2048 keeps the whole puzzle free and ad-free, and funds the work with optional theme packs and undo tokens that you never need to buy. Charging a little for craft you can opt into is honest; charging your attention with a video ad per game is not."
  - q: "What is Zen 2048 built with?"
    a: "The board is rendered in true 3D on Apple's own graphics stack — the same kind of real-time 3D rendering behind Apple's AR — wrapped in a SwiftUI interface. Everything runs on the device: the rendering, the themes, the physics, the haptics. There's no server, no account, and no tracking, and the game works fully offline. The only network touch is optional App Store purchases and Game Center, both handled by Apple."
  - q: "Does Zen 2048 work offline?"
    a: "Yes, completely. All the rendering, themes, animation, and game logic run locally on your iPhone. Your scores, best tile, streak, and unlocked themes are stored on the device, and no connection is ever required to play. The 3D board is not streamed or downloaded per-session — it's part of the app."
mentioned_apps:
  - zen-2048
read_time: "7 min read"
excerpt: "The design story behind Zen 2048 — why we rebuilt the flat 2048 puzzle as a real 3D board you can tilt, how we kept it instantly readable, what it means to treat a tile as a material rather than a colour, and why the work is funded by optional themes instead of ads."
---

2048 is a flat game. It has always been a flat game: a 4×4 grid of coloured squares that slide in one direction and add up when they match. Gabriele Cirulli built it that way in a weekend in 2014, and the flatness is part of why it spread — it costs almost nothing to render, runs anywhere, and reads instantly. You look at the board, you see the situation, you swipe.

So the first question, building [Zen 2048](/apps/zen-2048/), was almost a dare: does it *have* to be flat? And the second, harder question was the one that actually mattered: if we make it three-dimensional, do we break the thing that makes 2048 work?

## The legibility problem

Here is the constraint that shaped everything. 2048 is a game of instant reading. Before every swipe you take in the entire board — sixteen cells, the values, the gaps, where a merge will cascade — and you do it in a fraction of a second, dozens of times a session. Anything that slows that read down doesn't make the game prettier; it makes it worse.

A tilted 3D board is, on its face, *terrible* for this. Perspective makes far tiles smaller than near ones. Tall stacks can occlude what's behind them. A number you could read at a glance on a flat grid now sits at an angle, foreshortened. Every 3D-styled 2048 we looked at had quietly paid this tax: they looked three-dimensional in a screenshot and played like a slightly harder version of the flat game.

We didn't want a board that looked 3D in a screenshot. We wanted a board that *was* 3D — one you could pick up and turn — without the play ever getting harder. Those are different goals, and reconciling them is the whole design.

## The answer: depth you opt into

The resolution turned out to be simple to state and fussy to tune: **the 3D is for between moves, and the board comes home before every move.**

In Zen 2048 you can tilt the phone or drag to rotate the board to any angle. The tiles are real objects with real depth; the light moves across them as you turn. It's genuinely nice, and on a glass or metal theme it's the kind of thing you do absent-mindedly while thinking. But the instant you swipe, the camera returns to a clean, near-top-down read — the same legibility the flat game has always had. The depth is an affordance you reach for when you want it, not a handicap you fight while you play.

That single rule — *appreciate in 3D, play from the top* — is what let the board be honestly three-dimensional without charging the player for it. Almost everything else followed from protecting it.

## A tile is a material, not a colour

Once the board had real depth and real light, the tiles stopped being coloured rectangles and started being *objects*. And an object is made of something.

That reframing produced the part of Zen 2048 people notice first: the themes. There are 17 of them, and they're built from seven material families — glass, ceramic, paper, metal, neon, pastel, and monochrome. The important thing is that these aren't palettes. Switching from Amber to Glacier Ice to Midnight Neon doesn't just recolour the board; it changes the material the board is made of, and a material behaves differently under light and motion.

Concretely, a theme in Zen 2048 carries far more than a colour ramp. Each one defines:

- its **tile lighting and rim light** — the directional highlight that rides the top edge of a glass tile but is absent on matte paper;
- its **drop-shadow geometry** — how high each tile floats above the board;
- the **spring physics of a slide** — the exact stiffness and damping of how tiles travel and settle when you swipe, so ceramic feels weightier than neon;
- the **merge flash** — the duration, peak brightness, and softness of the little bloom when two tiles combine, hard and electric on neon, soft and warm on clay;
- and a slow **atmospheric drift** in the background — a barely-perceptible movement of light and hue, on the order of tens of seconds per cycle, that keeps the board feeling alive without ever distracting from it.

Glacier Ice catches cold light like glass because it *is* glass, in every property that matters to the eye. Studio Clay is hand-thrown ceramic fired from sand to terracotta. Paper & Ink is soft fibre with a single stroke. Designing seventeen of these is slow, and that slowness is the point: a theme is a small designed object, not a config value.

## The thing the ads crowd out

Here's the part that connects the craft to the business model, because they're the same decision.

When 2048 was open-sourced, the App Store filled with clones, and because the puzzle is trivial to copy, nearly all of them monetised the only way a copied commodity can: advertising. Pre-roll video before a game. An interstitial every few merges. Lives you refill by watching. Reward wheels bolted onto a number puzzle. We've [written before](/journal/a-2048-game-for-an-attentional-cease-fire/) about what that does to a small calm game — it turns five quiet minutes into an attention extraction loop.

But there's a quieter cost, too: ad-funded games don't tend to invest in *feel*. Why would they? The metric is impressions, not how a merge lands in your hand. The 3D board, the per-material physics, the tuned haptics that are present without buzzing at you constantly — none of that moves an ad-impression number. It only matters if the thing you're selling is the game itself.

So Zen 2048 is free, with no ads and no tracking, and it funds its own craft the honest way: optional theme packs and undo tokens you can buy if you want them and never need to play or win. Charge a little for a designed object someone chooses to own; don't charge everyone their attention with a video ad per game. The free Classic board is the whole game, complete on its own. The 3D and the seventeen materials are there because someone cared about how a number puzzle feels — which is exactly the thing the ad model has no reason to pay for.

## Was it worth making 2048 3D?

The honest answer is that 3D was never the goal; it was the means. The goal was to make the classic puzzle feel like a crafted object you'd want on your Home Screen, instead of a disposable clone you tolerate for a coffee-queue. Real depth, real materials, and real restraint about ads were how we got there.

If you want to feel the difference, the [free Classic board](/apps/zen-2048/) is the place to start — tilt it once, then swipe, and notice that the game underneath is exactly the 2048 you already know. That was always the constraint: change everything about how it feels, and nothing about how it plays. For the wider category — the Ketchapp version, the original, Threes — we keep an honest [guide to the best 2048 apps for iPhone](/guides/best-2048-apps-iphone/).

Published by Lagerland Apps, an independent Apple developer in Finland. No ads, no tracking, no account.
