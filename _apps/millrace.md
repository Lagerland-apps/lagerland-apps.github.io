---
layout: app
slug: millrace
name: "Millrace"
tagline: "A delivery puzzle: one inlet, one exact target, one move budget."
redirect_from:
  - /apps/zen-2048/
  - /apps/calm-2048/
quick_answer: "Millrace is a tile-delivery puzzle for iPhone and iPad. Each of its 64 levels gives you a fixed board, a queue of tiles you can see before they arrive, and a move budget. Tiles enter one at a time through a single marked inlet on the edge of the grid, and you have to build one exact value on one marked cell before the budget runs out. You lose in one of two ways, both of them your own doing: slide a tile over the inlet so the next arrival has nowhere to land, or overshoot the target by building a 128 when the level asked for a 64. Nothing is random. Every level was found by search and proved solvable by an automated solver before it shipped, so the shortest solution is known exactly. A separate Freeplay mode holds the endless merge board. The whole game is free, with no ads, subscription, or account, and it works fully offline and collects no data."
category: games
status: live

app_store_url: "https://apps.apple.com/app/id6759511759"

price:
  model: free
price_override: "Free, with optional theme packs & undo tokens"

plans_footnote: "The whole game is free: all 64 levels, Freeplay, the daily board, Hint, the Coach, and Game Center. Every purchase below is optional, and none is ever required to finish a level. Theme packs are one-time, non-consumable unlocks restorable with your Apple Account. Undo bundles are consumable tokens. There is also an optional {P_IAP:Millrace Tip Jar} “Support the Developer” tip, which unlocks nothing. US pricing shown; Apple derives other storefronts and shows your local currency at checkout. Refunds go through the standard App Store flow. There are no subscriptions."

pricing_note: "Every price is on the App Store listing. There is no subscription to cancel, and the free game stays free, with no trial and no card."

plans:
  - name: "Free"
    price: "$0"
    summary: "The whole game, with no ads, subscription, account, or energy meter."
    features:
      - "All 64 campaign levels across six chapters"
      - "Freeplay: the endless merge board, personal bests, and streaks"
      - "A daily board identical for every player in the world"
      - "Unlimited hints, and the Coach"
      - "Game Center leaderboards and achievements (optional)"
      - "The Classic theme"
      - "Fully offline, with no sign-in and no tracking"
    highlight_label: "The whole game"
  - name: "Theme packs"
    price: "{P_IAP:Millrace Designer Pack 1} each"
    summary: "Optional 3D material themes for the board, bought à la carte and kept for good."
    features:
      - "Designer Pack 1: Studio Clay, Paper &amp; Ink, Sakura Pastel, Amber, Heartwood"
      - "Designer Pack 2: Concrete Studio, Sunset Dunes, Glacier Ice, Brushed Metal, Midnight Neon"
      - "Summer Pack: Lido, Riviera, Agrumi"
      - "Winter Pack: Hygge Hearth, Aurora Drift, Evergreen Noël"
      - "One-time purchase, restorable with your Apple Account"
  - name: "Complete Collection"
    price: "{P_IAP:Millrace Complete Collection}"
    summary: "All sixteen paid themes at once, cheaper than the four packs bought separately."
    features:
      - "Every theme in all four packs"
      - "One-time purchase, no subscription"
  - name: "Undo bundles"
    price: "from {P_IAP:Millrace Undo 10}"
    summary: "Consumable undo tokens. One arrives free each day while you hold fewer than three."
    features:
      - "10 undos: {P_IAP:Millrace Undo 10}"
      - "50 undos: {P_IAP:Millrace Undo 50}"
      - "200 undos: {P_IAP:Millrace Undo 200}"
      - "Or earn them: daily-streak milestones at 3, 7, 14 and 30 days pay out 2, 5, 10 and 20 undos"
      - "Optional; you never need them to finish a level"

icon: "/assets/icons/millrace.png"
og_image: "/assets/og/millrace.png"

seo:
  title: "Millrace: Tile Delivery Puzzle for iPhone & iPad"
  description: "A tile delivery puzzle for iPhone and iPad with one inlet, an exact target, and a move budget. 64 solver-verified levels, free, offline, and ad-free."
  keywords:
    - "tile delivery puzzle"
    - "logic puzzle game iphone"
    - "merge puzzle with levels"
    - "puzzle game no ads"
    - "offline puzzle game"
    - "number puzzle ipad"
    - "games like threes"
    - "puzzle game with a solution"

hero:
  pre_headline: "Tile delivery puzzle for iPhone and iPad"
  headline: "Sixty-four levels, one inlet, and nothing random."
  secondary: "A delivery puzzle where every level was found by search and proved solvable before it shipped."
  subheadline: "Each level hands you a fixed board, a queue of tiles you can see in advance, and a move budget. Tiles arrive one at a time at a single marked inlet on the edge of the grid, and you have to build one exact value on one marked cell before the budget runs out. Slide a tile over the inlet and the next arrival has nowhere to land. Overshoot the target and that value is gone for good. The endless merge board is still here as Freeplay, one tap from the level list."
  cta_label: "Download Free"
  alt: "Millrace on iPhone, Level 58 in progress: build exactly 64 on the marked cell with 8 moves left, and the queue of arriving tiles shown under the 3D board"

screenshots:
  - src: "/assets/screenshots/millrace/1.png"
    caption: "A level in progress: build exactly 64 on the marked cell, 8 moves left, the next arrivals queued below."
  - src: "/assets/screenshots/millrace/2.png"
    caption: "The app opens on the campaign: six chapters, progress per chapter, Freeplay one tap away."
  - src: "/assets/screenshots/millrace/3.png"
    caption: "Solved: your move count, your best, and the shortest solution when you missed it."
  - src: "/assets/screenshots/millrace/4.png"
    caption: "Deep Water: every level shows how many tiles will arrive and your best solve."
  - src: "/assets/screenshots/millrace/5.png"
    caption: "Hint draws the suggested move on the board and says why."
  - src: "/assets/screenshots/millrace/6.png"
    caption: "After a game, the Coach names one habit, and only once it keeps showing up."
  - src: "/assets/screenshots/millrace/7.png"
    caption: "Stats: the lesson you are working on, personal bests, daily results, and streaks."
  - src: "/assets/screenshots/millrace/8.png"
    caption: "Glacier Ice, one of 17 themes on a real 3D board you can tilt."
  - src: "/assets/screenshots/millrace/9.png"
    caption: "Midnight Neon on Freeplay, the endless board."

who_for:
  - "You want puzzles that have a real answer, where an endless grid and a high-score table leave you cold"
  - "You like planning several moves ahead, with a proven shortest solution to chase on each level"
  - "You like a difficulty curve that is measured"
  - "You want a game that works on a plane or underground, with no sign-in"
  - "You care that a game collects nothing about you"

who_not_for:
  - "You want competitive or real-time multiplayer; Millrace is single-player and turn-based"
  - "You want hundreds of quick levels to tap through; the campaign is 64 levels, each built to need real lookahead"
  - "You want a native Mac app. Millrace is made for iPhone and iPad (Apple silicon Macs can install the iPad version, which Apple marks as not verified for macOS)"
  - "You want progress to sync across devices; it is stored locally and does not sync"

alternatives_to:
  - "Threes"
  - "KAMI 2"
  - "Flow Free"
  - "Two Dots"
  - "Suika Game"

value_points:
  - title: "Nothing is random"
    description: "You see the queue of arriving tiles before they land, the board is fixed, and the target is exact, so a level is a closed problem you can reason all the way through. Freeplay keeps the random endless board for when you want that."
  - title: "Levels found by search"
    description: "Every level is generated by search and then put through an automated gate before it ships. It must be solvable, its shortest solution must be confirmed by exhaustive search, and it must resist thoughtless play: any level a no-lookahead policy could stumble through is thrown away. A level in the app has a real answer and no cheap one."
  - title: "A difficulty curve that is measured"
    description: "The six chapters are pinned to the exact length of the optimal solution: five moves in Warm-up, then six, seven, eight, nine, and ten or more in Mastery. Each chapter asks you to hold exactly one more move in your head than the one before, and the curve follows search depth."
  - title: "Collects nothing, and can prove it"
    description: "There is no account, server, analytics, advertising, or third-party SDK, and the app contains no networking code at all. Apple's App Store privacy label reads “Data Not Collected”, and the Privacy Manifest declares no tracking, no tracking domains, and no collected data types."

features:
  - title: "The campaign"
    description: "Sixty-four levels across six chapters: Warm-up (4 levels), then Tactics, Pressure, Precision, Deep Water, and Mastery at 12 each. Every one is a fixed board, a visible queue, a move budget, and one exact value to deliver to one marked cell."
  - title: "Two ways to lose"
    description: "Block the inlet and the next tile has nowhere to land. Overshoot the target (a 128 where the level asked for 64) and that value is gone for good. Both failures come from your own moves, not from luck."
  - title: "A hint that comes from the solver"
    description: "In a campaign level, Hint asks the same exhaustive solver that verified the level for the first move of a winning line from where you stand now, and draws it on the board with a short reason. In Freeplay it looks ahead from your current board instead. Hints are never rationed or sold."
  - title: "The Coach"
    description: "After a Freeplay game, the Coach can name one habit worth fixing: corners, crowding, or ordering. It only speaks once a pattern keeps showing up across your recent games, works on one lesson at a time, retires the lesson when you fix it, and tells you when you get it right. It never interrupts play, and Coaching notes can be switched off in Settings."
  - title: "Freeplay and the daily board"
    description: "One tap from the level list is an endless board with no goal and no move limit. Slide, combine matching numbers, and see how far it goes. It keeps personal bests, a daily board that is identical for every player in the world, and a daily streak whose milestones pay out free undos."
  - title: "Seventeen themes on a real 3D board"
    description: "The board is an actual 3D scene. Tilt the device and light moves across ceramic, glass, walnut, paper, brushed metal, and neon. Classic is free; the other sixteen come in optional packs."
  - title: "iPhone and iPad"
    description: "On iPad the layout is native: the board is re-framed for the wider canvas, the controls stay a comfortable width, and the game turns with you into landscape. Requires iOS or iPadOS 18."
  - title: "Sound, music and haptics"
    description: "Haptics, sound effects, and a quiet ambient soundtrack, each with its own switch in Settings. Audio respects the silent switch and never interrupts music you are already playing."
  - title: "Fully translated"
    description: "Every player-facing string is translated into 34 languages across 40 App Store locales. No text is hard-coded, and chapter names match between the app and the store."

how_it_works:
  heading: "What a level has to survive before it ships."
  intro: "Millrace's levels are generated and tested by software instead of designed by feel. Each one passes these steps before it reaches you."
  steps:
    - title: "A candidate level is found by search"
      detail: "A generator searches for board-and-queue configurations that produce an interesting delivery problem. That is how the library reaches 64 levels that differ from one another, instead of 64 variations on one idea."
    - title: "An exhaustive solver confirms it has an answer"
      detail: "Each candidate is run through a breadth-first search that finds the true shortest solution. A level with no solution cannot ship, and the optimal move count is known exactly, which is how the result card can tell you the best possible count when you miss it."
    - title: "Levels a thoughtless policy could win are thrown away"
      detail: "The gate then plays each candidate with a battery of 280 no-lookahead strategies: one direction forever, fixed cycles, fixed priority orders, greedy play under every tiebreak, and rule-aware players that keep the inlet clear. If any of them stumbles into a win, the level is discarded, so no level can be beaten by luck or by mashing one direction."
    - title: "What survives is pinned to a chapter by its depth"
      detail: "The verified optimal length decides where a level lives: five moves in Warm-up, six in Tactics, seven in Pressure, eight in Precision, nine in Deep Water, ten or more in Mastery. The chapter tells you how deep you need to think."

example_insights:
  anchor: "coach"
  overline: "What the Coach actually says"
  heading: "One habit at a time, in one sentence."
  intro: "The Coach never reacts to a single bad game. A lesson is only taken up once its pattern has shown up repeatedly across your last five Freeplay games, only one lesson is ever active, and it retires once you fix it. These are the app's own lines."
  cards:
    - tag: "Lesson 1 · Corners"
      headline: "“Your 512 left the corner when another move would have kept it there.”"
      body: "The principle that comes with it: “Your biggest tile is safest in a corner. Build around it.” It is only said when another legal move really would have kept the tile in place, which the app checks against the board."
    - tag: "Lesson 2 · Crowding"
      headline: "“Your board was nearly full for much of the game.”"
      body: "Principle: “Clear small tiles early — a full board has nowhere to go.” It fires only in a real game, when more than a third of the moves were played with two or fewer empty cells."
    - tag: "Lesson 3 · Order"
      headline: "“Your big tiles ended up spread around the board.”"
      body: "Principle: “Keep your big tiles together in one row, in size order.” It is taught last on purpose, since size order is no use to someone who cannot hold a corner yet."
    - tag: "Praise"
      headline: "“Your 512 stayed in its corner the whole game.”"
      body: "A coach who only speaks when you fail is a critic. When a game shows you doing the thing, it says so, and a lesson you have learned retires for good."
    - tag: "Hint"
      headline: "“Keeps your 1024 safe in the corner.”"
      body: "Hint draws the suggested move on the board with a one-line reason. In a campaign level the move comes from the solver itself: the first step of a line that still wins."

comparison_table:
  intro: "Every row is a question a puzzle player asks before installing. Threes is the original number slider; KAMI 2 and Flow Free are level-based logic classics with a move count to beat; Two Dots is the long-running move-limit saga. Each has far more content than Millrace. The table covers what a level asks of you, what it costs, and what it collects."
  competitors: ["Millrace", "Threes!", "KAMI 2", "Flow Free", "Two Dots"]
  rows:
    - feature: "What a level asks"
      values: ["Build one exact value on one marked cell", "No levels; survive an endless board", "Flood the whole sheet to one color", "Connect every color pair and fill the board", "Meet the level's objectives"]
    - feature: "Levels"
      values: ["64, each with a proven shortest solution", "None; one endless mode", "100+ hand-crafted", "2,500+ free, plus paid packs", "More than 5,000"]
    - feature: "Move limit"
      values: ["A budget within two moves of the proven shortest", "None; play until no move is left", "A move target for a 'Perfect'", "None in Free Play; moves are counted", "Yes, on every level"]
    - feature: "What you can see coming"
      values: ["The whole arrival queue, before your first move", "The kind of tile that comes next", "The whole sheet; nothing arrives", "The whole board; nothing arrives", "New dots drop in unseen"]
    - feature: "Lives, boosters or paid help"
      values: ["None; Hint and the Coach are free", "None", "Hints from reward videos or packs", "Hint packs; optional Time Trial", "5 lives, power-ups and boosters"]
    - feature: "Ads"
      values: ["None", "None in the $5.99 app; the free Freeplay edition has ads", "Yes, per its release notes and player reviews", "Yes; $4.99 removes them", "Yes, including a video spinner for extra moves"]
    - feature: "Price"
      values: ["Free; optional themes and undos", "$5.99 once, no in-app purchases", "Free with in-app purchases", "Free; $4.99 unlocks packs and removes ads", "Free; in-app purchases from $0.99"]
    - feature: "App Store privacy label"
      values: ["Data Not Collected", "Data Not Collected (paid app)", "Data Used to Track You", "Data Used to Track You", "Data Used to Track You"]
    - feature: "Platforms"
      values: ["iPhone, iPad", "iPhone, iPad, Android, Steam, web", "iPhone, iPad, Android, Steam, Switch", "iPhone, iPad, Android", "iPhone, iPad, Android"]
  footnote: "Competitor details were checked on 24 September 2026 against each app's public App Store listing, release notes, and help pages; prices, ads, and privacy labels change, so verify before installing. Threes!+ and Flow Free+ are Apple Arcade editions with no ads or in-app purchases. Suika Game, a physics merge game and not a level-based puzzle, is compared on its own page."
  cta_label: "Download Millrace Free"

faq:
  - q: "What kind of puzzle is Millrace?"
    a: "A delivery puzzle. You get a fixed board, a queue of tiles you can see before they arrive, and a move budget. Tiles enter through one marked inlet on the edge of the grid, and you must build one exact value on one marked cell before the budget runs out. It uses merge mechanics (matching numbers combine), but unlike an endless merge game the board is fixed, the arrivals are known, and there is a specific right answer."
  - q: "How can you be sure every level is solvable?"
    a: "A solver checks before the level ships. Each one is run through an exhaustive breadth-first search that finds the shortest solution, and anything without a solution never makes it into the app. The same process throws away levels that a thoughtless, no-lookahead strategy could stumble through, so a level in Millrace has a real answer and no cheap one. The move budget is set from that proven shortest solution: never more than two moves above it, and on two levels exactly equal to it."
  - q: "What are the two ways to lose?"
    a: "Blocking the inlet, and overshooting. If you slide a tile over the marked inlet, the next arriving tile has nowhere to land. If you build a value past the target (a 128 when the level asked for a 64), that value is gone for good and the delivery can no longer be made. Both come from your own moves, which is the point."
  - q: "Is there an endless mode?"
    a: "Yes: Freeplay, one tap from the level list. It has no goal and no move limit; you slide, combine matching numbers, and see how far you get. It keeps personal bests, a daily streak, and a daily board that is the same for every player in the world. The app opens on the campaign, but Freeplay gets the same care."
  - q: "How much does Millrace cost?"
    a: "Nothing, for the whole game. All 64 levels, Freeplay, the daily board, Hint, the Coach and Game Center are free, with no ads and no subscription. The only purchases are optional: theme packs at {P_IAP:Millrace Designer Pack 1} each or all sixteen paid themes for {P_IAP:Millrace Complete Collection}, undo bundles from {P_IAP:Millrace Undo 10}, and a {P_IAP:Millrace Tip Jar} tip that unlocks nothing."
  - q: "Do I need to buy undo tokens?"
    a: "No. No level requires them and you can restart any level as many times as you like. They are a consumable safety net, mostly for Freeplay, sold in bundles of 10, 50 or 200. One free token arrives each day while you are holding fewer than three, and daily-streak milestones at 3, 7, 14 and 30 days pay out 2, 5, 10 and 20 more."
  - q: "What does the Coach do, and can I turn it off?"
    a: "After a Freeplay game it can name one habit worth fixing: keeping your biggest tile in a corner, not letting the board fill up, or keeping big tiles together in size order. It only speaks once a pattern has shown up repeatedly across your recent games, teaches one lesson at a time, and retires a lesson when you fix it. It never interrupts play, and you can switch Coaching notes off in Settings."
  - q: "Does Millrace work offline?"
    a: "Completely. The app contains no networking code at all and never uploads or downloads anything itself, so it behaves the same in airplane mode. Game Center and in-app purchases, if you use them, are the only parts that talk to Apple."
  - q: "Does Millrace collect any data about me?"
    a: "No. Apple's App Store privacy label for Millrace reads “Data Not Collected”. There is no account, analytics, advertising, or third-party SDK of any kind. The Privacy Manifest declares no tracking, an empty tracking-domain list, and no collected data types; the only Required Reason API is local settings storage. Progress stays on your device. The privacy policy has the full detail."
  - q: "Does it run on iPad and Mac, and does progress sync?"
    a: "Millrace runs natively on iPhone and iPad and requires iOS or iPadOS 18; on iPad the board is re-framed for the larger screen and works in landscape too. There is no Mac version, though Apple silicon Macs can install the iPad app, which Apple marks as not verified for macOS. Progress is stored on each device and does not sync; Game Center carries leaderboard entries and achievements, since Apple stores those."
  - q: "Why is it called Millrace?"
    a: "A millrace is the channel that carries water to a mill wheel: a steady flow arriving at one point. That is the game's mechanic. Tiles keep arriving at the inlet, and you have to keep the channel clear while you build the delivery."

privacy:
  tracking: false
  account_required: false
  data_collection: "none"
  app_privacy_label: "Apple's App Store privacy label for Millrace reads “Data Not Collected.” The app requests no tracking (no IDFA), links no advertising or analytics SDKs, and contains no networking code; its Privacy Manifest declares NSPrivacyTracking false, an empty tracking-domains list, and no collected data types."
  notes:
    - "No account, no server, and no networking code in the app"
    - "Progress and settings are stored locally with UserDefaults and SwiftData; the single declared Required Reason API is UserDefaults (CA92.1)"
    - "No third-party SDKs of any kind; every framework it links is Apple's"
    - "No iCloud, no CloudKit, no Keychain, no App Group; the only entitlement is Game Center"
    - "The app requests no permissions and shows no permission prompts"
    - "Game Center is optional and no feature depends on it; declining it sends nothing"
    - "Purchases are handled entirely by Apple, with no developer-side identifier attached"
  policy_url: "/apps/millrace/privacy/"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  photo: "/assets/icons/lagerland-mark.png"
  overline: "Why I built this"
  heading: "An endless grid can be tuned forever and still not be a game you finish."
  bio: "This started as a merge game and kept failing the only test that mattered: after twenty minutes it had nothing left to say. An endless random grid can be tuned forever and still not be a game you finish. So the random board became Freeplay, and the app now opens on a campaign of 64 levels found by search, each proved solvable and screened so a thoughtless strategy could not stumble through it. That last check is the one I would keep if I could only keep one, because without it you have a grid that sometimes lets you win."
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "No ads, analytics SDKs, advertising SDKs, or other third-party dependencies; every linked framework is Apple's"
    - "Built with SwiftUI, SwiftData, and RealityKit; the board is a real 3D scene, not a sprite sheet"
    - "All 64 levels are machine-verified before shipping: solvable, shortest solution confirmed, and screened against no-lookahead strategies"
    - "Localised into 34 languages across 40 App Store locales, with no hardcoded player-facing strings"
    - "Paid for by optional cosmetic packs, never by ads or data"
    - "{APP_COUNT} live apps in the Lagerland catalogue follow the same data rules: no tracking, no ads, and no required accounts"
  external_link:
    label: "Read the Lagerland studio backstory"
    href: "/lagerland-apps/"

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/millrace/support/"

related_apps: ["tare", "chessful", "shogiful"]

related_journal:
  slug: "how-millrace-levels-are-made"
  anchor: "Sixty-four levels, none written by hand: how Millrace proves them"

release:
  first_release: "2026-09-24"
  last_updated: "2026-09-24"
  version: "1.0"

show_body: true
about_heading: "What Millrace is: a delivery puzzle with merge mechanics"
last_updated: 2026-10-26
---

Millrace is a delivery puzzle for iPhone and iPad. It uses merge mechanics, where matching numbers combine when they collide, but each of its 64 levels is a closed problem with a specific right answer.

A level gives you three things: a **fixed board**, a **queue of tiles you can see before they arrive**, and a **move budget**. Tiles enter the grid one at a time through a single marked **inlet** on its edge. Your job is to build one exact value on one marked cell before the budget runs out. Nothing about it is random. The arrivals are known in advance, so you can reason a level all the way through.

There are two ways to lose, and both come from moves you chose. Slide a tile over the inlet and the next arrival has nowhere to land. Overshoot the target, building a 128 when the level asked for a 64, and that value is gone for good.

## The levels are manufactured, then tested

The part I would defend hardest is how the campaign is built. Nobody draws the levels by hand. They are **found by search**, and then each candidate has to survive an automated gate before it can ship:

- It must be **solvable**, checked by exhaustive breadth-first search, which also returns the genuine shortest solution.
- That shortest solution becomes the level's **known optimal**, so the par you are chasing is computed, not estimated. Solve a level in more moves than it needed and the result card tells you the best possible count. The move budget is set from it too, and it is tight: two moves of slack on 56 levels, one on six, and none at all on two.
- It must **resist thoughtless play**. The gate runs each candidate against 280 no-lookahead strategies, and if any of them stumbles into a win, the level is thrown away. Random play gets the same treatment: its exact odds of winning are computed, and anything above 2% is discarded.

That last check matters most. Every level that ships requires actual lookahead, because anything beatable without it was discarded. The full story of the generator, the solver and the sixteen checks is in the journal: [how Millrace's levels are made](/journal/how-millrace-levels-are-made/).

The six chapters are then pinned to the verified optimal length: five moves in **Warm-up**, six in **Tactics**, seven in **Pressure**, eight in **Precision**, nine in **Deep Water**, and ten or more in **Mastery**. The difficulty curve is search depth, so moving up a chapter means holding exactly one more move in your head than before. Warm-up is deliberately short at four levels; the other five chapters hold twelve each.

## Freeplay, and help when you want it

The endless board is still there as **Freeplay**, one tap from the level list. It has no goal or move limit, and it keeps personal bests and a daily board that is identical for every player in the world, with a daily streak whose milestones pay out free undos.

Two optional aids sit alongside both modes. **Hint** proposes a strong next move and tells you why; inside a campaign level it comes straight from the solver, as the first step of a line that still wins. **The Coach** watches your Freeplay games and, once a habit keeps showing up, names it (corners, crowding, or ordering), one lesson at a time. It never interrupts play, and it can be switched off.

## What it does not do

Millrace has no ads, subscription, account, sign-up, email address, or energy meter. It has no analytics, advertising SDKs, or third-party dependencies at all; every framework it links is Apple's. The app contains **no networking code**, so it never uploads or downloads anything itself; it works the same underground as it does on Wi-Fi.

Apple's App Store privacy label reads **Data Not Collected**. The app's Privacy Manifest declares no tracking, an empty tracking-domain list, and no collected data types, and the single Required Reason API it declares is local settings storage. There is no iCloud, no CloudKit, no Keychain, and no App Group. The only entitlement in the app is Game Center, which is optional and nothing depends on it. The [full privacy policy](/apps/millrace/privacy/) sets out exactly what is stored and what Apple handles instead.

The game is free in full. Optional purchases are cosmetic theme packs and consumable undo tokens, and no level ever requires a token to finish.

Millrace runs natively on iPhone and iPad, requires iOS or iPadOS 18, and is localised into 34 languages across 40 App Store locales.

If you like puzzles that end in a provable answer, [Tare](/apps/tare/) comes from the same studio: a wordless balance puzzle of hanging mobiles where hidden weights are deduced from picture cards, and every one of its 80 levels is machine-checked to have exactly one solution. For how both compare with Threes, Flow Free, Baba Is You and the rest, see [the best logic puzzle games for iPhone](/guides/best-logic-puzzle-games-iphone/).
