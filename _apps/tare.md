---
layout: app
slug: tare
name: "Tare"
tagline: "A wordless balance puzzle. Hang the weights, balance every beam, and deduce the hidden ones."

# Live since 2026-10-09 (v1.0). Facts are checked against the shipped build
# (~/Downloads/weightbalance, e2595ca) and the live en-US listing
# (marketing/app-store/metadata/en-US.json). The app hard-codes
# /apps/tare/privacy/ (UI/Settings/AppLinks.swift) and App Store Connect uses
# /apps/tare/ as both the support and marketing URL (tools/asc-metadata.py);
# never change either URL. Screenshots are the shipped en-US App Store set
# (marketing/app-store/screenshots/iphone-6.9/en-US/, Signboard Sky), 990px.
status: live

quick_answer: "Tare is a wordless balance logic puzzle for iPhone and iPad. Each level is a painted hanging mobile: you hang weights on its hooks until every beam balances, and you deduce the hidden “?” weights from small picture cards instead of guessing. There are 200 handcrafted levels in ten chapters, and every level is checked to have exactly one answer. The first 20 levels are free; one {P_IAP:Tare Full Access} purchase opens the other 180, with no subscription. It has no ads, timer, or lives, works offline, and collects no data."

category: games

app_store_url: "https://apps.apple.com/app/id6806255929"

price:
  model: free
price_override: "20 levels free · {P_IAP:Tare Full Access} unlocks 180 more"

pricing_note: "Every price is on the App Store listing. There is no subscription to cancel, and Chapter I stays free, with no trial and no card."

plans_footnote: "Tare is a free download, and Chapter I stays free for good. The one purchase is a non-consumable: you pay once, it stays yours, and you can restore it any time from Settings or the unlock screen. It works with Family Sharing. There are no subscriptions, ads, or other purchases. Chapters still open in order after you buy. US pricing shown; the App Store shows your local price at checkout."

plans:
  - name: "Chapter I"
    price: "Free"
    summary: "The Hang: twenty full levels, free to keep, with no time limit."
    features:
      - "20 handcrafted levels, starting with five that teach the game without a word"
      - "Your first nested beams, hidden weights, and picture cards"
      - "Up to three gold stars on every level"
      - "Hints, off until you switch them on"
      - "Optional sound, haptics on iPhone, and every accessibility setting"
      - "No ads or account, and it plays offline"
    highlight: true
  - name: "Chapters II to X"
    price: "{P_IAP:Tare Full Access} once"
    summary: "The other 180 levels, yours to keep."
    features:
      - "Nine more chapters, from The Secret to The Retrospective"
      - "More hidden weights to deduce and deeper mobiles to balance"
      - "Spare pieces from Chapter IV on, so part of the puzzle is what to leave out"
      - "Nine more painted worlds, from Twilight Meadow to Summer Fields"
      - "One purchase and no subscription"
      - "Family Sharing included"

icon: "/assets/icons/tare.png"
og_image: "/assets/og/tare.png"

seo:
  title: "Tare: Wordless Balance Logic Puzzle for iPhone and iPad"
  description: "Wordless balance logic puzzle for iPhone and iPad. Deduce hidden weights from picture cards. 200 handmade levels, 20 free, offline, no ads."
  keywords:
    - "balance puzzle game"
    - "logic puzzle iphone"
    - "brain teaser game"
    - "hanging mobile puzzle"
    - "offline puzzle game no wifi"
    - "puzzle game no ads"
    - "deduction puzzle"
    - "logic puzzle for adults"

hero:
  pre_headline: "Wordless balance puzzle for iPhone and iPad"
  headline: "Deduce every hidden weight and bring the whole mobile to rest."
  secondary: "200 handcrafted levels, each checked to have exactly one answer. The first 20 are free."
  subheadline: "Every level is a painted hanging mobile. Hang the weights from the tray and the beams tip and settle as you go: heavy pieces near the middle, light ones farther out. Some weights hide behind a “?”, and the picture cards above the board are how you work them out. There is no timer and nothing to read."
  cta_label: "Play Chapter I free"
  cta_subline: "Free download · 20 levels free · one {P_IAP:Tare Full Access} unlock for the other 180 · no ads · no data collected"
  alt: "Tare on iPhone: a three-tier hanging mobile on a sky-blue board, with weights numbered 5, 2, 6, 3, and 3 on its hooks"

screenshots:
  - src: "/assets/screenshots/tare/1.webp"
    caption: "A three-tier mobile in the Morning Sky, the first of ten painted worlds."
  - src: "/assets/screenshots/tare/2.webp"
    caption: "Deep Sea: the top beam leans until the pieces in the tray below find the right hooks, then the whole mobile settles."
  - src: "/assets/screenshots/tare/3.webp"
    caption: "Twilight Meadow: two picture cards above the board show how the hidden “?” piece compares. Read them to work out what it weighs."
  - src: "/assets/screenshots/tare/4.webp"
    caption: "Evening Stars: a cascading mobile with three hidden weights, and two cards to deduce them from."
  - src: "/assets/screenshots/tare/5.webp"
    caption: "The chapter wall: every chapter in its own world, with the stars you earned under every level."
  - src: "/assets/screenshots/tare/6.webp"
    caption: "No ads, timers, or words on screen, only the mobile."

who_for:
  - "You like logic puzzles with one real answer, such as sudoku, nonograms, or Kakuro, and want one that feels physical"
  - "You want a brain teaser that plays offline, on a plane or underground, with no sign-in"
  - "You like to take your time, with no timer, lives, or move counter"
  - "You want a game anyone can play in any language, because there is nothing to read"
  - "You would rather pay once than watch ads or keep a subscription"
  - "You play with VoiceOver, Reduce Motion, or high contrast"

who_not_for:
  - "You want a reflex game or a physics sandbox. Tare is a slow, exact logic puzzle"
  - "You want leaderboards, achievements, or multiplayer. Tare has no Game Center and no score"
  - "You play on Android or Mac. Tare is for iPhone and iPad with iOS 18 or later"
  - "You need progress to sync between devices. It stays on the device you play on"

value_points:
  - title: "The scale won't give the answer away"
    description: "A beam carrying a hidden “?” weight will not settle until you have worked out what the weight is. Hanging it and watching which way the beam tips tells you nothing. The picture cards above the board show how the pieces compare, and reading them is the only way through."
  - title: "Exactly one answer, every level"
    description: "All 200 levels are handmade, then checked by a solver: exactly one arrangement balances, every hidden weight follows from its cards, and spare pieces fit nowhere. When you are stuck, a clean answer exists."
  - title: "Take as long as you like"
    description: "There is no timer, move counter, lives, or fail screen. A full board that doesn't balance gives a small shudder and lets you keep going. Hints stay off until you switch them on, and asking for one costs that level's third star."
  - title: "Any language, and no data collected"
    description: "The puzzle has no words on it, so it plays the same in every language. Tare shows no ads, needs no account, and collects no data. Your progress stays on your device."

features:
  - title: "Painted hanging mobiles"
    description: "Drag weights from the tray onto hooks along each beam. A heavy weight near the middle balances a light one farther out. Beams hang from other beams, so one change ripples up the whole mobile, and the structures grow from a first wobbly hang to many-layered towers."
  - title: "Hidden weights and picture cards"
    description: "Some weights arrive as a frosted bubble marked “?”. Small picture cards pinned above the board show how pieces compare, and you reason out each secret weight from them. Tap a card to enlarge it. When a new kind of card first appears, a short wordless sequence shows what it means."
  - title: "Ten chapters, ten worlds"
    description: "200 levels in ten chapters, from The Hang to The Retrospective, each in a painted world of its own: Morning Sky, Twilight Meadow, Deep Sea, Evening Stars, Rose Dawn, Firefly Forest, Coral Reef, Polar Night, Sunset Hills, and Summer Fields. From Chapter IV the tray holds spare pieces that belong nowhere. Finish a chapter 20 out of 20 and its world becomes a background you can choose in Settings."
  - title: "The solve"
    description: "When the last piece finds its hook, the beams stop swaying, gold stars pop, sparks fly, and light washes over the board. Turn Sound on in Settings and the mobile rings out in a single chord. Tap to skip the celebration."
  - title: "Hints, only if you want them"
    description: "Hints are off by default. Switch them on in Settings and a hint button appears on each level. A hint draws a line showing where the next piece goes. It never shows the final piece and never reveals a hidden weight, so you always finish the mobile yourself. Asking costs that level's third star."
  - title: "Up to three gold stars"
    description: "A clean solve earns three stars. Rehang a piece or ask for a hint and it drops to two; fill the board wrongly first and it drops to one. Your best grade is kept, and stars never lock anything."
  - title: "Accessibility"
    description: "VoiceOver reads the mobile as named beams, hooks, and weights, with actions to place a piece or return it to the tray. Menus and labels grow with Dynamic Type. A High contrast switch keeps flat colours at 4.5:1 or better, Reduce Motion and Reduce Transparency are respected, and the pieces come in distinct shapes, so colour is never the only cue."
  - title: "Quiet until you choose"
    description: "Sound starts off; switch it on to hear notes as you place pieces and the chord on every solve. On iPhone, haptics let you feel each weight seat. Every world has a day and a night look that follows your device, and the painted room behind the mobile leans a little as you tilt the phone, except under Reduce Motion."

how_it_works:
  heading: "One rule, and a scale that keeps its secrets."
  intro: "A beam is level when the pull on both sides is equal, and pull is weight times distance from the pivot. Here is how a level plays out."
  steps:
    - title: "Read the mobile"
      detail: "Beams hang from a pivot, with hooks along each side. The weights wait in the tray below. Some beams hang from other beams, and a hanging beam pulls with everything below it."
    - title: "Hang the pieces"
      detail: "Drag a weight onto a hook. Beams with nothing hidden on them tip and settle as you place pieces, so you can feel your way toward balance."
    - title: "Deduce the hidden weights"
      detail: "A beam carrying a “?” won't settle until you have deduced it. Read the picture cards above the board and work out what each hidden weight must be."
    - title: "Fill every hook and let it rest"
      detail: "When every beam is level, the mobile comes to rest and the solve plays out. A full board that doesn't balance gives one small shudder, and you try again."

alternatives_to:
  - "Baba Is You"
  - "Good Sudoku"
  - "DragonBox Algebra"
  - "Nonograms Katana"
  - "Simon Tatham's Puzzles"

# Side-by-side comparison: auto-triggers the mid-page CTA and the alt-strip.
# Competitor cells come from the five alternatives pages, checked 2026-10-09.
comparison_table:
  intro: "Every row is a question a puzzle player asks before installing. Baba Is You is the celebrated rule-rewriting puzzle; Good Sudoku and Nonograms Katana are the big one-answer grid puzzles; DragonBox Algebra teaches equations as a balancing game; Simon Tatham's Puzzles is a free collection of 38 puzzle types. Most have far more content than Tare. The table covers what a level asks of you, what it costs, and what it collects."
  competitors: ["Tare", "Baba Is You", "Good Sudoku", "DragonBox Algebra", "Nonograms Katana", "Simon Tatham's Puzzles"]
  rows:
    - feature: "What a level asks"
      values: ["Balance every beam of a hanging mobile at once", "Reach the goal by rewriting the rules with word blocks", "Each digit once per row, column and box", "Isolate the box (later x) on one side", "Fill the grid from row and column clues", "Depends on which of the 38 puzzles you pick"]
    - feature: "Puzzles"
      values: ["200 handcrafted, each machine-checked to have exactly one answer", "Main game plus free New Adventures (150+) and Museum (~80) packs", "70,000+ generated, plus your own", "200 in 10 chapters, plus daily puzzles", "1001, plus puzzles from other players", "Generated fresh for each new game"]
    - feature: "Hidden values to deduce"
      values: ["Yes: “?” weights, from picture cards", "No", "No, only empty cells", "Yes: the box, which becomes x", "The hidden picture", "Varies by puzzle"]
    - feature: "Price"
      values: ["Free; 20 levels free, {P_IAP:Tare Full Access} once for the other 180", "$6.99 once, no in-app purchases", "Free with ads; $4.99 Full Game Unlock; or Apple Arcade", "Free to start; Kahoot! Kids $5.99/month or $35.99/year", "Free; $2.99 VIP removes ads; hint packs", "Free and open source, no in-app purchases"]
    - feature: "App Store privacy label"
      values: ["Data Not Collected", "Data Not Collected", "Data Not Linked to You, incl. third-party advertising", "Data Linked to You, incl. analytics", "Data Not Linked to You", "Data Not Collected"]
    - feature: "Platforms"
      values: ["iPhone, iPad", "iPhone, iPad, Mac, Apple Vision; Steam, Android", "iPhone, iPad, Mac", "iPhone, iPad", "iPhone, iPad, Mac", "iPhone, iPad, Mac; desktop, web, Android"]
  footnote: "Competitor details were checked on 9 October 2026 against each app's public App Store listing and release notes; prices, ads, and privacy labels change, so verify before installing. Good Sudoku+ is the Apple Arcade edition. DragonBox's listing describes both a required Kahoot! Kids subscription and a free start; its comparison page has the detail."
  cta_label: "Play Chapter I Free"

faq:
  - q: "What kind of game is Tare?"
    a: "Tare is a wordless balance logic puzzle for iPhone and iPad. Each of its 200 levels is a hanging mobile, and you hang weights on hooks until every beam balances at once. Some weights are hidden, and you work out their values from picture cards. It feels like a toy, but each level has exactly one correct arrangement that you can reason out."
  - q: "How does balancing work?"
    a: "A beam is level when weight times distance from the pivot is equal on both sides. A 2 on the second notch balances a 4 on the first. When one beam hangs from another, it pulls on its hook with everything hanging below it. The game teaches this in its first five levels without a word."
  - q: "What are the “?” weights?"
    a: "They are weights hidden inside a frosted bubble. A beam carrying one will not settle until you have deduced its value, so you can't read the answer off the scale. The picture cards pinned above the board show how the pieces compare, and you reason out each hidden weight from them."
  - q: "Is every level actually solvable?"
    a: "Yes. Every level is handmade and then checked by a solver. It must have exactly one balanced arrangement, every hidden weight must follow from its cards, and any spare piece must fit nowhere."
  - q: "Is Tare free?"
    a: "The download is free, and Chapter I, with its 20 levels, stays free; it is not a timed trial. One {P_IAP:Tare Full Access} purchase opens Chapters II to X, the other 180 levels, for good. It is a one-time purchase with no subscription, and it works with Family Sharing. There are no ads and nothing else to buy."
  - q: "I bought the unlock. Why is Chapter II still closed?"
    a: "Chapters open in order, purchase or not. Keep solving Chapter I and Chapter II opens, and each later chapter opens the same way. Within a chapter you can play up to three levels past the last one you solved."
  - q: "How do I restore my purchase on a new iPhone or iPad?"
    a: "Open Settings in the game and tap Restore purchases. The unlock screen has the same button."
  - q: "Are there hints?"
    a: "Yes, if you want them. Hints are off by default. Switch on Hints in Settings and a hint button appears on each level. A hint draws a line showing where the next piece goes. It never shows the final piece and never reveals a hidden weight. Asking for a hint costs that level's third star. On the first five levels, a guiding line also appears by itself if you pause for a while."
  - q: "What do the three stars mean?"
    a: "Three stars is a clean solve. Taking a piece back off or asking for a hint brings it to two, and filling the board wrongly before you solve it brings it to one. Your best grade is kept, and nothing in the game is locked behind stars."
  - q: "Does Tare work offline, and does it collect data?"
    a: "Tare works completely offline; all 200 levels are in the app. Only buying and restoring the unlock need a connection, through Apple. The game opens no network connections of its own, has no account, ads, analytics, or third-party SDKs, and collects no data. Your progress and settings stay on your device."
  - q: "Can children or people who don't read English play it?"
    a: "Yes. The puzzle has no words, so anyone can play it in any language and at any age. The few screens around it, such as Settings and the unlock screen, are translated into 50 languages."
  - q: "Does it run on iPad or Mac, and does progress sync?"
    a: "Tare runs on iPhone and iPad with iOS or iPadOS 18 or later. On iPhone it plays in portrait. On iPad it turns with the device and draws the game large in a centred column. There is no Mac, Apple Watch, or Vision Pro version. Progress stays on the device you play on and does not sync between devices."
  - q: "Is Tare accessible?"
    a: "Yes. VoiceOver reads the mobile as named beams, hooks, and weights, with actions to place a piece or return it to the tray. Menus and labels scale with Dynamic Type. A High contrast switch keeps flat colours at 4.5:1 or better, Reduce Motion and Reduce Transparency are respected, and the pieces come in distinct shapes, so colour is never the only cue."

privacy:
  tracking: false
  account_required: false
  data_collection: "none"
  app_privacy_label: "Apple's App Store privacy label for Tare reads “Data Not Collected.” The app does no tracking, includes no advertising or analytics SDKs, and its Privacy Manifest declares no tracking and no collected data."
  notes:
    - "No account, and the game opens no network connections of its own"
    - "Progress, star grades, and settings are stored only on your device"
    - "No analytics, advertising, or third-party SDKs"
    - "The motion sensor drives a background parallax effect; it switches off under Reduce Motion"
    - "Apple handles the one purchase; the game keeps only the fact that the chapters are unlocked"
    - "No permission prompts for camera, photos, microphone, location, contacts, or health data"
  policy_url: "/apps/tare/privacy/"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "Tare started as a quiet museum piece, hairline beams on warm paper. It was tasteful and dull, and its first levels were flat beams nobody needed to think about. So we rebuilt the chapters to ramp up, redrew every screen as a painted toy on a sky-blue board, and gave each solve a proper celebration. One rule never changed: a beam with a secret on it won't settle until you have worked the secret out. Without that rule the hidden weights would be a guessing game. With it, every level is a proof you finish yourself."
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "No ads, analytics, or third-party SDKs, and no network connections of its own"
    - "Every level checked by a solver before it ships: one answer, hidden weights fixed by their cards, spare pieces that fit nowhere"
    - "VoiceOver, Dynamic Type, High contrast, Reduce Motion, and Reduce Transparency support"
    - "Paid for by one purchase, never by ads or data"

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/tare/support/"

release:
  first_release: "2026-10-09"
  last_updated: "2026-10-09"
  version: "1.0"

related_apps: ["millrace", "chessful", "xiangqiful"]

related_journal:
  slug: "how-to-solve-balance-puzzles"
  anchor: "How to solve a balance puzzle, and how Tare proves all 200 levels"

show_body: true
about_heading: "What Tare is: a balance puzzle you solve by deduction"
last_updated: 2026-10-29
---

Tare is a logic puzzle that looks like a toy. Each level is a painted hanging mobile on a sky-blue board, with a tray of weights beneath it. Your job is to hang every weight on a hook so that **every beam balances at the same time**.

The rule fits in one line: a beam is level when **weight times distance from the pivot** is equal on both sides. A 2 on the second notch balances a 4 on the first. When one beam hangs from another, it pulls on its hook with everything below it, so a single move near the bottom ripples all the way up.

## The rule that makes it a logic puzzle

From the first chapter, some weights arrive hidden inside a frosted bubble marked **“?”**. Hanging one and watching the beam won't tell you what it weighs, because **a beam carrying an unsolved “?” will not settle.**

Small picture cards pinned above the board give you the clues. Each shows how a few of the pieces compare, and the cards are enough to pin down every hidden value. You have to reason it out. When the last piece goes on and the mobile comes to rest, you know why it balanced.

Every level is built by hand and then **checked by a solver** before it ships. It must have exactly one balanced arrangement, every hidden weight must follow from its cards, and every spare piece must fit nowhere. [How to solve a balance puzzle, and how the proof works](/journal/how-to-solve-balance-puzzles/) walks through a real level step by step.

## Ten chapters

- **The Hang** (Morning Sky, free): five levels that teach the game without words, then your first nested beam and your first hidden weights.
- **The Secret** (Twilight Meadow): more hidden weights, and more cards to read.
- **The Cascade** (Deep Sea): beams hanging from beams, deeper than before.
- **The Exhibition** (Evening Stars): more pieces in the tray than hooks on the mobile, so you have to work out which ones belong nowhere.
- **The Ledger, The Inventory, The Fulcrum, The Forgery, The Restoration, and The Retrospective**: six more chapters, each in a world of its own, that combine the earlier ideas into harder puzzles.

Each chapter holds twenty levels. The first chapter stays free. One {P_IAP:Tare Full Access} purchase opens the other 180, with Family Sharing and no subscription.

## What Tare leaves out

Tare has no ads, timer, lives, move counter, or score, and no account or sign-in. It has no analytics or third-party SDKs and opens no network connections of its own, so it plays the same underground as it does on Wi-Fi. Hints stay off until you switch them on, and asking for one costs that level's third star.

Apple's App Store privacy label reads **Data Not Collected**, and the app's Privacy Manifest declares no tracking and no collected data. The [privacy policy](/apps/tare/privacy/) sets out what stays on your device and what Apple handles instead.

Tare runs on iPhone and iPad with iOS or iPadOS 18 or later, and its few words are translated into 50 languages. If you like puzzles that end in a provable answer, [Millrace](/apps/millrace/) is a tile-delivery puzzle from the same studio. For how both compare with Baba Is You, Good Sudoku, Flow Free, and the rest, see [the best logic puzzle games for iPhone](/guides/best-logic-puzzle-games-iphone/).
