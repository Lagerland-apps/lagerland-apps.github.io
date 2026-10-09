---
layout: app
slug: tare
name: "Tare"
tagline: "A wordless balance logic puzzle. Hang the weights, level every beam, deduce the hidden ones."

# Live since 2026-10-09 (v1.0). Facts are checked against the shipped build
# (~/Downloads/weightbalance, e2595ca) and the live en-US listing
# (marketing/app-store/metadata/en-US.json). The app hard-codes
# /apps/tare/privacy/ (UI/Settings/AppLinks.swift) and App Store Connect uses
# /apps/tare/ as both the support and marketing URL (tools/asc-metadata.py) —
# never change either URL. Screenshots are the shipped en-US App Store set
# (marketing/app-store/screenshots/iphone-6.9/en-US/, Signboard Sky), 990px.
status: live

quick_answer: "Tare is a wordless balance logic puzzle for iPhone and iPad. Each level is a painted hanging mobile: you drag weights numbered 1 to 9 onto hooks so that every beam balances at once — weight times distance from the pivot must match on both sides, and a nested beam's whole load acts at the hook it hangs from. From the first chapter some weights hide inside a bubble marked “?”, and any beam carrying an unsolved “?” sways instead of tilting, so the scale can never tell you what the secret weighs. Small picture cards show how the pieces compare, and you deduce the value from those. There are 80 handcrafted levels in four chapters, each one machine-checked to have exactly one answer. The first 20 are free to keep; one $2.99 purchase unlocks the other 60 for good, with Family Sharing. No ads, no timers, no lives, no account, fully offline, and no data collected."

category: games
platforms: ["iOS", "iPadOS"]

app_store_url: "https://apps.apple.com/app/id6806255929"

price:
  model: free
  value: "20 levels free · $2.99 unlocks 60 more"
price_currency: "USD"
schema_price: "0"
schema_high_price: "2.99"
schema_offer_count: "2"

pricing_note: "Every price is on the App Store listing. There is no subscription to cancel, and Chapter I stays free — no trial, no card."

plans_footnote: "Tare is a free download and Chapter I is free forever — it never expires and is never gated. The one purchase is a non-consumable: pay once, keep it, restore it any time from Settings or the unlock screen, and share it with up to five family members through Family Sharing. There are no subscriptions, no consumables, no ads and no energy meter. Chapters still open in order after you buy: Chapter II opens once you have solved 16 of Chapter I's 20 levels. US pricing shown; the App Store shows your local price at checkout."

plans:
  - name: "Chapter I"
    price: "Free"
    summary: "The Hang — twenty full levels, yours to keep. Not a trial, not a timer."
    features:
      - "20 handcrafted levels, including the wordless onboarding"
      - "Your first hidden weights and picture cards"
      - "Optional hints, off until you switch them on"
      - "Three gold stars to earn on every level"
      - "Sound, haptics and every accessibility option"
      - "No ads, no account, works offline"
    highlight: true
  - name: "Chapters II–IV"
    price: "$2.99 once"
    summary: "The other sixty levels. Yours forever."
    features:
      - "The Secret — reading the cards, tilted comparisons and ratios"
      - "The Cascade — mobiles three beams deep"
      - "The Exhibition — more pieces than hooks, and some belong nowhere"
      - "Three more worlds: Twilight Meadow, Deep Sea and Evening Stars"
      - "One-time purchase — no subscription, ever"
      - "Family Sharing included"

icon: "/assets/icons/tare.png"
og_image: "/assets/og/tare.png"

seo:
  title: "Tare: Balance Logic Puzzle for iPhone & iPad — 80 Levels"
  description: "Tare is a wordless balance logic puzzle: hang weights, level every beam, deduce the hidden ones. 80 levels, 20 free. Offline, no ads, no data collected."
  keywords:
    - "balance puzzle game"
    - "logic puzzle iphone"
    - "brain teaser game"
    - "hanging mobile puzzle"
    - "offline puzzle game no wifi"
    - "puzzle game no ads"
    - "deduction puzzle"
    - "math logic puzzle for adults"

hero:
  pre_headline: "Wordless balance logic puzzle for iPhone and iPad"
  headline: "Hang the weights. Balance every beam. Deduce the rest."
  secondary: "Some weights won't say what they weigh — and the scale won't tell you."
  subheadline: "Every level is a painted hanging mobile. Drag each weight onto a hook until every beam comes to rest at once — heavy near the middle, light far out, and one nudge ripples all the way up. Then the secrets arrive: weights hidden inside a “?” bubble, and little picture cards that are the only way to work out what they weigh. Twenty levels free, no timer, nothing to read."
  cta_label: "Play Chapter I free"
  cta_subline: "Free download · 20 levels free · one $2.99 unlock for the other 60 · no ads · no data collected"
  alt: "Tare on iPhone — a three-tier hanging mobile on a sky-blue board, with weights numbered 5, 2, 6, 3 and 3 on its hooks"

screenshots:
  - src: "/assets/screenshots/tare/1.png"
    caption: "A three-tier mobile in the Morning Sky. Every weight shows its number twice — as a numeral and as domino pips."
  - src: "/assets/screenshots/tare/2.png"
    caption: "Deep Sea: the top beam leans until the pieces on the shelf below find the right hooks, then the whole mobile settles."
  - src: "/assets/screenshots/tare/3.png"
    caption: "Twilight Meadow: two picture cards above the board show how the hidden “?” piece compares. Read them to work out what it weighs."
  - src: "/assets/screenshots/tare/4.png"
    caption: "Evening Stars: a cascading mobile with three hidden weights, and two cards to deduce them from."
  - src: "/assets/screenshots/tare/5.png"
    caption: "The chapter wall: four chapters of twenty mobiles, each in its own world, with the stars you earned under every level."
  - src: "/assets/screenshots/tare/6.png"
    caption: "No ads, no timers and no words. Just the mobile."

who_for:
  - "You love logic puzzles with one real answer — sudoku, nonograms, Kakuro — and want something that feels physical"
  - "You want a brain teaser you can play offline, on a plane or underground, with no sign-in"
  - "You like to take your time: no timer, no lives, no move counter, no one watching"
  - "You want a game the whole family can play in any language, because there is nothing to read"
  - "You would rather pay once for the whole thing than meet an ad or a subscription"

who_not_for:
  - "You want a physics sandbox or a reflex game — Tare is turn-free and exact, and nothing falls over"
  - "You want leaderboards or multiplayer — there is no Game Center and no score"
  - "You play on Android or Mac — Tare is iPhone and iPad only (iOS 18 or later)"
  - "You need progress to sync between devices — this version keeps it on the device you play on"

value_points:
  - title: "The scale can't be cheated"
    description: "A beam carrying an unsolved “?” never tilts truthfully — it sways, slowly, and never settles. So you can't hang a secret weight and watch which way the beam goes. The only way to know what it weighs is to read the picture cards and reason it out, which is what makes Tare a logic puzzle rather than trial and error."
  - title: "Every level has exactly one answer"
    description: "All 80 levels are built by hand and then proven by machine before they ship: exactly one arrangement balances, every hidden weight is pinned down by its cards alone, and any decoy piece fits no balanced arrangement at all. When a level clicks, it was your reasoning — never luck."
  - title: "No timer, no lives, no counting"
    description: "Take all the time you like. There is no move counter, no failure screen and no red buzzer — a complete but wrong board just gives a gentle shudder. Hints are there if you switch them on, they are free, and the only price is the third star on that level."
  - title: "Nothing to read, nothing collected"
    description: "The puzzle itself has no words at all, so anyone can play it at any age in any language. No ads, no account, no analytics and no network code — it plays exactly the same in airplane mode, and nothing about you ever leaves your device."

features:
  - title: "Painted hanging mobiles"
    description: "Each weight hangs from a notch on a chalk-white beam. A weight's pull is its number times its distance from the pivot — a 2 at the second notch balances a 4 at the first — and a nested beam's whole load acts at the hook it hangs from, so one change ripples up the whole tower."
  - title: "Hidden weights and picture cards"
    description: "Some weights hide inside a soap bubble marked “?”. Cards pinned above the board quote the pieces in miniature: this one equals that, this one outweighs that pair, these two balance on unequal arms. Hold a piece and the cards that mention it lift, so you always know which clue to read."
  - title: "Four chapters, four worlds"
    description: "The Hang in a Morning Sky, The Secret in a Twilight Meadow, The Cascade in the Deep Sea, and The Exhibition under Evening Stars — twenty levels each, from your first wobbly hang to many-layered mobiles with more pieces than hooks. Finish a chapter and its world becomes a canvas you can choose for the whole game."
  - title: "The click"
    description: "Hang the last piece right and the beams stop swaying, gold stars pop, sparks fly and the sun comes out. Turn Sound on and the whole mobile rings out in a single chord: every weight has its own note, heavier is lower, so a solved mobile sounds balanced."
  - title: "Hints, only if you want them"
    description: "Hints are off until you switch them on in Settings. Then a lantern button sits on every level, and each press draws one line from the next piece to its hook. It never hangs anything for you and it never shows the last piece, so you always finish the mobile yourself. The first hint on a level costs its third star; asking again costs nothing more."
  - title: "Three gold stars, never a gate"
    description: "Every solve earns at least one star. Solve it without ever filling the board wrongly for two, and without taking a piece back off or asking for a hint for all three. Your best is kept, the celebration is the same at any grade, and nothing is locked behind stars."
  - title: "Built for every player"
    description: "Every known weight shows both a numeral and domino pips, so colour is never the only cue. VoiceOver reads the mobile as named beams and hooks with place and return actions, in all 50 of the app's languages. The numeral grows with Dynamic Type, a High contrast switch clears 4.5:1, and Reduce Motion and Reduce Transparency are respected."
  - title: "Quiet by design"
    description: "Tare starts silent: sound is off until you turn it on, and haptics have their own switch on devices that have them. The game follows your device's light or dark appearance. A gentle parallax gives the board depth when you tilt the phone and turns itself off under Reduce Motion."

how_it_works:
  heading: "One rule, and a scale you cannot ask."
  intro: "Tare runs on one rule — a beam is level when the pull on both sides is equal, and pull is weight times distance from the pivot. Here is how a level plays out."
  steps:
    - title: "Read the mobile"
      detail: "Beams hang from a pivot, with hooks at notches one to four on either side. Weights on the shelf below carry a number from 1 to 9, shown as a numeral and as pips. Some beams hang from other beams, and a hanging beam pulls with the total of everything below it."
    - title: "Hang the pieces"
      detail: "Drag a weight near a hook and it snaps on; drop it on an occupied hook to swap. Beams with nothing hidden on them tilt honestly as you go, so you can feel your way toward balance on the easy branches."
    - title: "Deduce the hidden weights"
      detail: "A beam carrying a “?” sways and will not tell you which way it leans. Read the picture cards above the board — equal, heavier, or balanced on unequal arms — and work out what the secret must weigh before you hang the rest."
    - title: "Fill every hook, and let it rest"
      detail: "When every hook is full and every beam is level, the mobile settles and the bubbles show what they held. If the board is full but wrong, it gives one gentle shudder — no red, no buzzer — and you try again."

alternatives_to:
  - "Baba Is You"
  - "Good Sudoku"
  - "DragonBox Algebra"
  - "Nonograms Katana"
  - "Simon Tatham's Puzzles"

# Side-by-side comparison — auto-triggers the mid-page CTA and the alt-strip.
# Competitor cells come from the five alternatives pages, checked 2026-10-09.
comparison_table:
  intro: "Every row is a question a puzzle player asks before installing. Baba Is You is the celebrated rule-rewriting puzzle; Good Sudoku and Nonograms Katana are the big one-answer grid puzzles; DragonBox Algebra teaches equations as a balancing game; Simon Tatham's Puzzles is a free collection of 38 puzzle types. Most have far more content than Tare — the table is about what a level asks of you, what it costs, and what it collects."
  competitors: ["Tare", "Baba Is You", "Good Sudoku", "DragonBox Algebra", "Nonograms Katana", "Simon Tatham's Puzzles"]
  rows:
    - feature: "What a level asks"
      values: ["Balance every beam of a hanging mobile at once", "Reach the goal by rewriting the rules with word blocks", "Each digit once per row, column and box", "Isolate the box — later x — on one side", "Fill the grid from row and column clues", "Depends on which of the 38 puzzles you pick"]
    - feature: "Puzzles"
      values: ["80 handcrafted, each machine-checked to have exactly one answer", "Main game plus free New Adventures (150+) and Museum (~80) packs", "70,000+ generated, plus your own", "200 in 10 chapters, plus daily puzzles", "1001, plus puzzles from other players", "Generated fresh for each new game"]
    - feature: "Hidden values to deduce"
      values: ["Yes — “?” weights, from picture cards", "No", "No — only empty cells", "Yes — the box, which becomes x", "The hidden picture", "Varies by puzzle"]
    - feature: "Price"
      values: ["Free; 20 levels free, $2.99 once for the other 60", "$6.99 once, no in-app purchases", "Free with ads; $4.99 Full Game Unlock; or Apple Arcade", "Free to start; Kahoot! Kids $5.99/month or $35.99/year", "Free; $2.99 VIP removes ads; hint packs", "Free and open source, no in-app purchases"]
    - feature: "App Store privacy label"
      values: ["Data Not Collected", "Data Not Collected", "Data Not Linked to You, incl. third-party advertising", "Data Linked to You, incl. analytics", "Data Not Linked to You", "Data Not Collected"]
    - feature: "Platforms"
      values: ["iPhone, iPad", "iPhone, iPad, Mac, Apple Vision; Steam, Android", "iPhone, iPad, Mac", "iPhone, iPad", "iPhone, iPad, Mac", "iPhone, iPad, Mac; desktop, web, Android"]
  footnote: "Competitor details were checked on 9 October 2026 against each app's public App Store listing and release notes; prices, ads and privacy labels change, so verify before installing. Good Sudoku+ is the Apple Arcade edition. DragonBox's listing describes both a required Kahoot! Kids subscription and a free start; its comparison page has the detail."
  cta_label: "Play Chapter I Free"

faq:
  - q: "What kind of game is Tare?"
    a: "A wordless balance logic puzzle. Each of its 80 levels is a hanging mobile, and you place numbered weights on hooks so that every beam balances at the same time. From early on some weights are hidden, and you work out their values from picture-card clues. It feels physical, but it is exact: every level has one correct arrangement that can be reasoned out."
  - q: "How does balancing work?"
    a: "A beam is level when weight times distance is equal on both sides of its pivot. A 2 on the second notch balances a 4 on the first; a 3 on the fourth notch balances a 6 on the second. When one beam hangs from another, it pulls on its hook with the total weight of everything hanging below it. That is the whole rulebook — the game teaches it without a word in its first levels."
  - q: "What are the “?” weights, and why won't the beam tilt?"
    a: "They are weights hidden inside a bubble. Any beam carrying an unsolved “?” deliberately sways instead of tilting, so you cannot hang the secret and read its weight off the scale. The picture cards pinned above the board show how the pieces compare, and those cards alone are enough to pin down every hidden value. Once you solve the level, the bubbles show what they held."
  - q: "Is every level actually solvable?"
    a: "Yes. Every level is built by hand and then checked by a solver before it ships. It must have exactly one balanced arrangement, every hidden weight must be determined by its cards alone, and any decoy piece must fit no balanced arrangement at all. A level that fails any of those checks does not ship."
  - q: "Is Tare free?"
    a: "The download is free, and Chapter I — twenty full levels — is free forever. It is not a timed trial. One $2.99 purchase unlocks Chapters II, III and IV, the other sixty levels, for good. It is a one-time purchase, not a subscription, and it works for your whole family through Family Sharing. There are no ads and nothing else to buy."
  - q: "I bought the unlock. Why is Chapter II still closed?"
    a: "Chapters open in order, purchase or not. Chapter II opens once you have solved 16 of Chapter I's 20 levels, and each later chapter opens the same way from the one before it. Within a chapter you can skip ahead up to three levels past the last one you solved."
  - q: "How do I restore my purchase on a new iPhone or iPad?"
    a: "Open Settings in the game and tap Restore purchases; the unlock screen has the same button. The purchase is tied to your Apple Account, so it comes back on any device signed in to it, and to family members through Family Sharing."
  - q: "Are there hints?"
    a: "Yes, if you want them. Hints are off by default; switch on Hints in Settings and a lantern button appears on every level. Each press draws one line from the next piece to the hook it belongs on. It never places a piece for you and never shows the last one, so you always finish the mobile yourself. Hints are free, but the first one you ask for on a level costs that attempt's third star; further presses cost nothing, and restarting the level gives you a fresh attempt at all three. In the first five levels a teaching line also appears by itself if you sit idle for a while."
  - q: "What do the three stars mean?"
    a: "One star means you solved it. Two mean you solved it without ever filling the board wrongly. Three mean you also never took a piece you had hung back off and never asked for a hint. Pieces that start the level already hanging can be moved for free. Your best result is kept, the celebration is the same whatever you earn, and nothing in the game is locked behind stars."
  - q: "Does Tare work offline, and does it collect data?"
    a: "It works completely offline — the game contains no networking code, so it behaves the same in airplane mode. It has no account, no ads, no analytics and no third-party SDKs, and it collects no data. Your progress and settings stay on your device. The only things that involve Apple are the purchase itself and the standard App Store review prompt."
  - q: "Can children or people who don't read English play it?"
    a: "Yes. The puzzle itself has no words, so it plays the same in every language and at any age. The few screens around it — Settings, chapter names, the unlock screen — are translated into 50 App Store locales. There are no ads, no chat, no accounts and nothing collected, and purchases go through Apple, so Ask to Buy and Screen Time apply."
  - q: "Does it run on iPad or Mac, and does progress sync?"
    a: "Tare runs on iPhone and iPad and needs iOS or iPadOS 18 or later. On iPhone it plays in portrait. On iPad it turns with the device and the mobile sits in a centred column, and from iPadOS 26 you can resize its window. There is no Mac or Vision Pro version. Progress is stored on the device you play on and does not sync between devices in this version; the unlock itself restores on any device with your Apple Account."
  - q: "Is Tare accessible?"
    a: "Accessibility was built in, not bolted on. Every known weight shows a numeral and domino pips, so colour is never the only cue. VoiceOver reads the mobile as a tree of named beams, hooks and weights with place and return actions, in every language the app ships in. There is a High contrast switch, the numeral scales with Dynamic Type, hooks have a generous 60-point snap, and Reduce Motion and Reduce Transparency are both respected."

privacy:
  tracking: false
  account_required: false
  data_collection: "none"
  app_privacy_label: "Apple's App Store privacy label for Tare reads “Data Not Collected.” The app requests no tracking (no IDFA), links no advertising or analytics SDKs, has no networking code and no entitlements, and its Privacy Manifest declares NSPrivacyTracking false and no collected data types."
  notes:
    - "No account, no server, and no networking code anywhere in the game"
    - "Progress, star grades and settings are stored only on your device"
    - "No analytics, advertising or third-party SDKs of any kind"
    - "How many hints you ask for is never stored; a level only remembers that a hint cost its third star"
    - "The motion sensor is read live for a parallax effect and never stored; it stops under Reduce Motion"
    - "The one purchase is handled entirely by Apple; the game keeps only the fact that the chapters are unlocked"
    - "No permission prompts: no camera, photos, microphone, location, contacts or health data"
  policy_url: "/apps/tare/privacy/"

founder:
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "Tare started as a quiet museum piece — hairline beams on warm paper — and it was tasteful and dull, and its first levels were single flat beams nobody needed to think about. So the chapters were rebuilt to ramp, every screen was redrawn as a painted toy on a sky-blue board, and the win became a real payoff. The one thing that never changed is the rule I would defend over everything else: a beam with a secret on it sways instead of tilting. Without that, the hidden weights are a guessing game. With it, every level is a proof you get to finish yourself."
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "No ads, no analytics, no third-party SDKs and no networking code — every framework it links is Apple's"
    - "All 80 levels machine-proven before shipping: one solution, hidden weights fixed by their cards, decoys that fit nowhere"
    - "Every picture in the game is drawn in code with SwiftUI — the only recorded assets are its sounds"
    - "VoiceOver, Dynamic Type, High contrast, Reduce Motion and Reduce Transparency built in from the first release"
    - "Funded by one honest purchase, never by ads or data"

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
  anchor: "How to solve a balance puzzle — and how Tare proves all 80 levels"

show_body: true
about_heading: "What Tare is — a balance puzzle you solve by deduction"
---

Tare is a logic puzzle disguised as a toy. Each level is a painted hanging mobile on a sky-blue board, with a shelf of numbered weights beneath it. Your job is to hang every weight on a hook so that **every beam balances at the same time**.

The rule fits in one line: a beam is level when **weight × distance from the pivot** is equal on both sides. A 2 on the second notch balances a 4 on the first. When one beam hangs from another, it pulls on its hook with everything below it, so a single move near the bottom ripples all the way up the tower.

## The rule that makes it a logic puzzle

Early in the game, some weights arrive hidden inside a bubble marked with a **“?”**. You could expect to hang one and watch the beam tip to learn what it weighs. Tare doesn't let you: **a beam carrying an unsolved “?” sways and never tells the truth.**

What you get instead are small picture cards pinned above the board. Each one quotes a few of the pieces in miniature, showing that this one equals that one, that one outweighs a pair, or that two of them balance on unequal arms. The cards alone are enough to pin down every hidden value, and you have to reason it out. When the last piece goes on and the mobile comes to rest, you *know* why it balanced.

Every level is built by hand and then **proven by machine** before it ships. It must have exactly one balanced arrangement, every hidden weight must be fixed by its cards, and every decoy must fit no balanced arrangement at all. [How to solve a balance puzzle, and how the proof works](/journal/how-to-solve-balance-puzzles/) walks through a real level step by step.

## Four chapters

- **The Hang** (Morning Sky, free): arranging weights on every shape of mobile, your first nested beam and your first secrets.
- **The Secret** (Twilight Meadow): reading the cards, with tilted comparisons that bracket a value and ratio cards on unequal arms.
- **The Cascade** (Deep Sea): mobiles three beams deep as the norm.
- **The Exhibition** (Evening Stars): more pieces on the shelf than hooks on the mobile, so you have to prove which ones belong nowhere.

Each chapter holds twenty levels. The first chapter is free forever. One $2.99 purchase opens the other sixty, with Family Sharing and no subscription.

## What it does not do

No ads. No timer, no lives, no move counter, no score. No account and no sign-in. No analytics, no third-party SDKs and no networking code, so Tare plays the same underground as it does on Wi-Fi. Hints are off unless you switch them on, and they cost nothing but a level's third star; the game never counts how many you ask for.

Apple's App Store privacy label reads **Data Not Collected**. The app's Privacy Manifest declares no tracking, no tracking domains and no collected data types, and the only Required Reason API it declares is local settings storage. It has no entitlements at all: no iCloud, no Game Center, no Keychain sharing. The [privacy policy](/apps/tare/privacy/) sets out exactly what stays on your device and what Apple handles instead.

Tare runs on iPhone and iPad with iOS or iPadOS 18 or later, and its few words are translated into 50 App Store locales. If you like puzzles that end in a provable answer, [Millrace](/apps/millrace/) comes from the same studio: a tile-delivery puzzle whose 64 levels are each proved solvable by an exhaustive solver.
