---
layout: app
slug: millrace
name: "Millrace"
tagline: "A delivery puzzle: one inlet, one exact target, one move budget."

# ── IN REVIEW ─────────────────────────────────────────────────────────────────
# Resubmitted 2026-08-24 after the 4.3(a) rebrand from Zen 2048. `status` is
# deliberately NOT "live": every listing on this site filters on
# `where: "status", "live"` (home, /apps/, llms.txt, llms-full.txt, ai-index.json,
# ai-sitemap.xml, footer, you-might-like, /lagerland-apps/, the /for/ hubs), so
# this page exists at its URL and appears nowhere else. `sitemap: false` keeps it
# out of sitemap.xml too.
#
# ON APPROVAL: set status to "live" and delete `sitemap: false` here, in
# apps/millrace/privacy/index.html and in apps/millrace/support/index.html. Then
# add the OG card (scripts/generate-og.py), the QR (scripts/generate-qr.py),
# screenshots, alternatives pages, llms.txt routing, and the app-count bumps.
#
# STILL OPEN: Game Center scope. Only 3 leaderboards + 18 achievements are live in
# ASC; the 4th leaderboard and the 10 campaign achievements are authored in the
# repo but not yet minted. This page therefore states no counts — add them once
# the remaining 11 entities exist.
#
# The app is free (confirmed by the developer 2026-08-25); only theme packs and
# undo bundles cost money.
status: upcoming
sitemap: false
# ──────────────────────────────────────────────────────────────────────────────

quick_answer: "Millrace is a delivery puzzle for iPhone. Each of its 64 levels gives you a fixed board, a queue of tiles you can see before they arrive, and a move budget. Tiles enter one at a time through a single marked inlet on the edge of the grid, and your job is to build one exact value on one marked cell before the budget runs out. There are two ways to lose and both are yours to avoid: slide a tile over the inlet so the next arrival has nowhere to land, or overshoot the target by building a 128 when the level asked for a 64. Nothing is random. Every level was found by search and proved solvable by an automated solver before it shipped, so the shortest solution is known exactly. A separate Freeplay mode holds the endless merge board. Millrace is offline, has no ads, no subscription and no account, and collects no data."

category: games
platforms: ["iOS"]

app_store_url: "https://apps.apple.com/app/id6759511759"

price:
  model: free
  value: "Free — optional theme packs & undo tokens"
schema_price: "0"
schema_high_price: "5.99"
schema_offer_count: "9"

plans_footnote: "The game is free in full — all 64 levels, Freeplay, the daily board, and Game Center. Every purchase below is optional and none is ever required to finish a level. Theme packs are one-time, non-consumable unlocks restorable with your Apple Account. Undo bundles are consumable tokens. US pricing shown; Apple derives other storefronts and shows your local currency at checkout. Refunds go through the standard App Store flow. There are no subscriptions."

plans:
  - name: "Free"
    price: "$0"
    summary: "The whole game — no ads, no subscription, no account, no energy meter."
    features:
      - "All 64 campaign levels across six chapters"
      - "Freeplay — the endless merge board, personal bests and streaks"
      - "A daily board identical for every player in the world"
      - "Hint and the Coach"
      - "Game Center leaderboards and achievements (optional)"
      - "The Classic theme"
      - "Fully offline — no sign-in, no tracking"
    highlight: true
  - name: "Theme packs"
    price: "$1.99 each"
    summary: "Optional 3D material themes for the board, bought à la carte and kept for good."
    features:
      - "Designer Pack 1 — Studio Clay, Paper &amp; Ink, Sakura Pastel, Amber, Heartwood"
      - "Designer Pack 2 — Concrete Studio, Sunset Dunes, Glacier Ice, Brushed Metal, Midnight Neon"
      - "Summer Pack — Lido, Riviera, Agrumi"
      - "Winter Pack — Hygge Hearth, Aurora Drift, Evergreen Noël"
      - "One-time purchase, restorable with your Apple Account"
  - name: "Complete Collection"
    price: "$5.99"
    summary: "All sixteen paid themes at once, cheaper than the four packs bought separately."
    features:
      - "Every theme in all four packs"
      - "One-time purchase, no subscription"
  - name: "Undo bundles"
    price: "from $0.99"
    summary: "Consumable undo tokens. One arrives free each day while you hold fewer than three."
    features:
      - "10 undos — $0.99"
      - "50 undos — $2.99"
      - "200 undos — $5.99"
      - "Optional — you never need them to finish a level"

icon: "/assets/icons/millrace.png"

seo:
  title: "Millrace — Tile Delivery Puzzle for iPhone, 64 Levels"
  description: "Millrace is a delivery puzzle for iPhone: one inlet, one exact target, one move budget. 64 solver-verified levels. Offline, no ads, no tracking."
  keywords:
    - "tile delivery puzzle"
    - "merge puzzle iphone"
    - "offline puzzle game iphone"
    - "puzzle game no ads"
    - "logic puzzle levels iphone"
    - "private puzzle game"

hero:
  headline: "Sixty-four levels. One inlet. Nothing is random."
  secondary: "A delivery puzzle where every level was found by search and proved solvable before it shipped."
  subheadline: "Each level hands you a fixed board, a queue of tiles you can see in advance, and a move budget. Tiles arrive one at a time at a single marked inlet on the edge of the grid, and you have to build one exact value on one marked cell before the budget runs out. Slide a tile over the inlet and the next arrival has nowhere to land. Overshoot the target and that value is gone for good. The endless merge board is still here as Freeplay, one tap from the level list."
  cta_label: "View on the App Store"
  alt: "Millrace on iPhone — a 3D puzzle board with the tile queue visible and the target cell marked"

who_for:
  - "You want puzzles with a real answer, not an endless grid and a high-score table"
  - "You like knowing the difficulty curve is measured rather than claimed"
  - "You want a game that works on a plane or underground, with no sign-in"
  - "You care that a game collects nothing about you"

who_not_for:
  - "You want competitive or real-time multiplayer — Millrace is single-player and turn-based"
  - "You want it on iPad or Mac — this release is iPhone-only, portrait-only"
  - "You want progress to sync across devices — it is stored locally and does not sync"

value_points:
  - title: "Nothing is random"
    description: "The queue of arriving tiles is visible before it lands, the board is fixed, and the target is exact. A level is a closed problem you can reason all the way through, not a grid you hope goes your way. Freeplay keeps the random endless board for when you want that instead."
  - title: "Levels found by search, not written by hand"
    description: "Every level is generated by search and then put through an automated gate before it ships: it must be solvable, its shortest solution must be confirmed by exhaustive search, and — crucially — it must resist thoughtless play. Levels a no-lookahead policy could stumble through are thrown away. If a level is in the app it has a real answer and no cheap one."
  - title: "A difficulty curve that is measured"
    description: "The six chapters are pinned to the exact length of the optimal solution — five moves in Warm-up, then six, seven, eight, nine, and ten or more in Mastery. Progressing means holding exactly one more move in your head than the chapter before. The curve is search depth, not a designer's guess."
  - title: "Collects nothing, and can prove it"
    description: "No account, no servers, no analytics, no advertising, no third-party SDKs — the app contains no networking code at all. Its Privacy Manifest declares no tracking, no tracking domains, and no collected data types, and the only Required Reason API is local settings storage."

features:
  - title: "The campaign"
    description: "Sixty-four levels across six chapters — Warm-up (4 levels), then Tactics, Pressure, Precision, Deep Water and Mastery at 12 each. Every one is a fixed board, a visible queue, a move budget, and one exact value to deliver to one marked cell."
  - title: "Two ways to lose, both avoidable"
    description: "Block the inlet and the next tile has nowhere to land. Overshoot the target — a 128 where the level asked for 64 — and that value is gone for good. Both failures are consequences of your own moves rather than bad luck."
  - title: "Freeplay"
    description: "One tap from the level list: an endless board with no goal and no move limit. Slide, combine matching numbers, and see how far it goes. Personal bests, streaks, and a daily board that is identical for every player in the world."
  - title: "Hint and the Coach"
    description: "Hint suggests a strong next move and explains why. The Coach watches a finished game and names one habit worth fixing — corners, crowding, or ordering. It never interrupts play, and you can switch it off entirely."
  - title: "Seventeen themes on a real 3D board"
    description: "The board is an actual 3D scene, not a picture of one. Tilt the phone and light travels across ceramic, glass, walnut, paper, brushed metal and neon. Classic is free; the other sixteen live in optional packs."
  - title: "Forty languages"
    description: "Millrace ships in 40 locales with every player-facing string localised — not machine-swapped at runtime."

how_it_works:
  intro: "The thing that separates Millrace from other merge games is that its levels are manufactured and tested rather than authored by feel. Here is what a level has to survive before it reaches you."
  steps:
    - title: "A candidate level is found by search"
      detail: "Levels are not hand-drawn. A generator searches for board-and-queue configurations that produce an interesting delivery problem, which is how the library reaches 64 levels that are genuinely different from one another rather than 64 variations on one idea."
    - title: "An exhaustive solver confirms it has an answer"
      detail: "Each candidate is run through a breadth-first search that finds the true shortest solution. A level with no solution cannot ship, and the optimal move count becomes a known quantity rather than an estimate — which is what makes a shared par possible."
    - title: "Levels a thoughtless policy could win are thrown away"
      detail: "The gate then plays each candidate with a large battery of no-lookahead strategies. If any of them stumbles into a win, the level is discarded. This is the step that ensures a level cannot be beaten by luck or by mashing one direction — it has to be solved."
    - title: "What survives is pinned to a chapter by its depth"
      detail: "The verified optimal length decides where a level lives: five moves in Warm-up, six in Tactics, seven in Pressure, eight in Precision, nine in Deep Water, ten or more in Mastery. The chapter you are in tells you exactly how deep you need to think."

faq:
  - q: "What kind of puzzle is Millrace?"
    a: "A delivery puzzle. You get a fixed board, a queue of tiles you can see before they arrive, and a move budget. Tiles enter through one marked inlet on the edge of the grid, and you must build one exact value on one marked cell before the budget runs out. It uses merge mechanics — matching numbers combine — but unlike an endless merge game the board is fixed, the arrivals are known, and there is a specific right answer."
  - q: "How can you be sure every level is solvable?"
    a: "Because a solver checks before the level ships. Each one is run through an exhaustive breadth-first search that finds the genuine shortest solution; anything without a solution never makes it into the app. The same process also throws away levels that a thoughtless, no-lookahead strategy could stumble through, so a level in Millrace has a real answer and no cheap one."
  - q: "What are the two ways to lose?"
    a: "Blocking the inlet, and overshooting. If you slide a tile over the marked inlet, the next arriving tile has nowhere to land. If you build a value past the target — a 128 when the level asked for a 64 — that value is gone for good and the delivery can no longer be made. Both are consequences of your own moves, which is the point."
  - q: "Is the classic endless 2048-style board still there?"
    a: "Yes, as Freeplay, one tap from the level list. No goal, no move limit — slide, combine matching numbers, and see how far you get. It keeps personal bests, streaks, and a daily board that is the same for every player in the world. The campaign is what the app opens on, but Freeplay is not an afterthought."
  - q: "Does Millrace work offline?"
    a: "Completely. The app contains no networking code at all — it never uploads or downloads anything itself, so it behaves identically in airplane mode. Game Center, if you choose to sign in, is the one part that talks to Apple."
  - q: "Does Millrace collect any data about me?"
    a: "No. There is no account, no analytics, no advertising, and no third-party SDKs of any kind. The App Store Privacy Manifest declares no tracking, an empty tracking-domain list, and no collected data types; the only Required Reason API is local settings storage. Progress stays on your device. The privacy policy has the full detail."
  - q: "Do I need to buy undo tokens?"
    a: "No. No level requires them and you can restart any level as many times as you like. They are a consumable safety net, mostly for Freeplay, sold in bundles of 10, 50 or 200. One free token arrives each day while you are holding fewer than three."
  - q: "Is it on iPad or Mac, and does it sync?"
    a: "Neither yet — this release is iPhone-only and portrait-only, and requires iOS 18. Progress is stored locally and does not sync between devices; Game Center will carry leaderboard entries and achievements since Apple stores those, but campaign progress does not transfer."

privacy:
  tracking: false
  account_required: false
  data_collection: "none"
  app_privacy_label: "Millrace requests no tracking (no IDFA), links zero advertising or analytics SDKs, and contains no networking code. Its Privacy Manifest declares NSPrivacyTracking false, an empty tracking-domains list, and no collected data types."
  notes:
    - "No account, no server, and no networking code anywhere in the app"
    - "Progress and settings are stored locally with UserDefaults and SwiftData; the single declared Required Reason API is UserDefaults (CA92.1)"
    - "No third-party SDKs of any kind — every framework it links is Apple's"
    - "No iCloud, no CloudKit, no Keychain, no App Group; the only entitlement is Game Center"
    - "The app requests no permissions and shows no permission prompts"
    - "Game Center is optional and gates no feature; declining it sends nothing"
    - "Purchases are handled entirely by Apple, with no developer-side identifier attached"
  policy_url: "/apps/millrace/privacy/"

founder:
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "This started as a merge game and kept failing the only test that mattered: after twenty minutes it had nothing left to say. An endless random grid can be tuned forever and still not be a game you finish. So the random board became Freeplay and the front door became a campaign — 64 levels found by search, each proved solvable, each one screened to make sure a thoughtless strategy could not stumble through it. That last check is the one I would keep if I could only keep one: it is the difference between a puzzle and a grid that sometimes lets you win."
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "No ads, no analytics SDKs, no advertising SDKs, and zero third-party dependencies — every linked framework is Apple's"
    - "Built with SwiftUI, SwiftData and RealityKit; the board is a real 3D scene, not a sprite sheet"
    - "All 64 levels are machine-verified before shipping: solvable, shortest solution confirmed, and screened against no-lookahead strategies"
    - "Localised into 40 languages with no hardcoded player-facing strings"
    - "Funded by honest paid software — optional cosmetic packs, never ads or data"

support:
  email: "lagerland.apps@proton.me"

release:
  first_release: "2026-08-24"
  last_updated: "2026-08-24"

show_body: true
about_heading: "What Millrace is — a delivery puzzle with merge mechanics"
---

Millrace is a delivery puzzle for iPhone. It uses merge mechanics — matching numbers combine when they collide — but it is not an endless grid with a high-score table. Each of its 64 levels is a closed problem with a specific right answer.

A level gives you three things: a **fixed board**, a **queue of tiles you can see before they arrive**, and a **move budget**. Tiles enter the grid one at a time through a single marked **inlet** on its edge. Your job is to build one exact value on one marked cell before the budget runs out. Nothing about it is random — the arrivals are known in advance, which means a level can be reasoned all the way through rather than played hopefully.

There are two ways to lose, and both are yours to avoid. Slide a tile over the inlet and the next arrival has nowhere to land. Overshoot the target — build a 128 when the level asked for a 64 — and that value is gone for good. Neither failure is bad luck. Both are consequences of moves you chose.

## The levels are manufactured, then tested

The part I would defend hardest is how the campaign is built. The levels are not hand-drawn by feel. They are **found by search**, and then each candidate has to survive an automated gate before it can ship:

- It must be **solvable** — checked by exhaustive breadth-first search, which also returns the genuine shortest solution.
- That shortest solution becomes the level's **known optimal**, so the par you are chasing is a computed fact rather than an estimate.
- It must **resist thoughtless play**. The gate runs each candidate against a large battery of no-lookahead strategies, and if any of them stumbles into a win, the level is thrown away.

That last check is the one that matters most. It is what separates a puzzle from a grid that occasionally lets you win: every level that ships requires actual lookahead, because anything beatable without it was discarded.

The six chapters are then pinned to the verified optimal length — five moves in **Warm-up**, six in **Tactics**, seven in **Pressure**, eight in **Precision**, nine in **Deep Water**, and ten or more in **Mastery**. The difficulty curve is search depth, so moving up a chapter means holding exactly one more move in your head than before. Warm-up is deliberately short at four levels; the other five chapters hold twelve each.

## Freeplay, and help when you want it

The endless board did not go away — it became **Freeplay**, one tap from the level list. No goal, no move limit, personal bests, streaks, and a daily board that is identical for every player in the world.

Two optional aids sit alongside both modes. **Hint** proposes a strong next move and tells you why. **The Coach** watches a finished game and names one habit worth fixing — corners, crowding, or ordering. It never interrupts play, and it can be switched off.

## What it does not do

No ads. No subscription. No account, no sign-up, no email address. No energy meter. No analytics, no advertising SDKs, and no third-party dependencies at all — every framework it links is Apple's. The app contains **no networking code**, so it never uploads or downloads anything itself; it works the same underground as it does on Wi-Fi.

Its App Store Privacy Manifest declares no tracking, an empty tracking-domain list, and no collected data types, and the single Required Reason API it declares is local settings storage. There is no iCloud, no CloudKit, no Keychain, and no App Group — the only entitlement in the app is Game Center, which is optional and gates nothing. The [full privacy policy](/apps/millrace/privacy/) sets out exactly what is stored and what Apple handles instead.

The game is free in full. Optional purchases are cosmetic theme packs and consumable undo tokens — and no level ever requires a token to finish.

Millrace is iPhone-only, portrait-only, requires iOS 18, and ships in 40 languages.
