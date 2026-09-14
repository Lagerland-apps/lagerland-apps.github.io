---
layout: app
slug: tare
name: "Tare"
tagline: "A wordless balance logic puzzle. Hang the weights, level every beam, deduce the hidden ones."

# ── UNLISTED — PRE-LAUNCH ─────────────────────────────────────────────────────
# Tare is not released yet. `status` is deliberately NOT "live": every listing on
# this site filters on `where: "status", "live"` (home, /apps/, llms.txt,
# llms-full.txt, ai-index.json, ai-sitemap.xml, footer, you-might-like,
# /lagerland-apps/, the /for/ hubs), so this page exists at its URL and appears
# nowhere else. `sitemap: false` keeps it out of sitemap.xml too.
#
# The URLs are not optional: the app hard-codes /apps/tare/privacy/
# (UI/Settings/AppLinks.swift) and App Store Connect uses /apps/tare/ as both the
# support and marketing URL (tools/asc-metadata.py).
#
# NO IMAGES YET (owner decision 2026-09-14): no screenshots, no OG card, no QR,
# and assets/icons/tare.png does not exist yet. hero.html reads page.icon
# unguarded and falls back to it when there are no screenshots, so add the icon
# (weightbalance/Assets.xcassets/AppIcon.appiconset/AppIcon-light.png, 1024²)
# before sharing the URL. Screenshots must be captured against Signboard Sky —
# the images in ~/Downloads/tare-design-screenshots/ are the superseded
# Quiet Gallery look.
#
# ON LAUNCH: set status to "live" and delete `sitemap: false` here and in
# apps/tare/privacy/index.html; add icon, screenshots, og_image
# (scripts/generate-og.py), QR (scripts/generate-qr.py), the Apple privacy-label
# callout (`privacy.app_privacy_label`, only once the label is live), the
# support page, llms.txt routing and the app-count bumps. Set release dates to
# the real release day.
status: upcoming
sitemap: false
# ──────────────────────────────────────────────────────────────────────────────

quick_answer: "Tare is a wordless balance logic puzzle for iPhone and iPad. Each level is a painted hanging mobile: you drag weights numbered 1 to 9 onto hooks so that every beam balances at once — weight times distance from the pivot must match on both sides, and a nested beam's whole load acts at the hook it hangs from. From the first chapter some weights hide inside a bubble marked “?”, and any beam carrying an unsolved “?” sways instead of tilting, so the scale can never tell you what the secret weighs. Small picture cards show how the pieces compare, and you deduce the value from those. There are 80 handcrafted levels in four chapters, each one machine-checked to have exactly one answer. The first 20 are free to keep; one $2.99 purchase unlocks the other 60 for good, with Family Sharing. No ads, no timers, no lives, no account, fully offline, and no data collected."

category: games
platforms: ["iPhone", "iPad"]

app_store_url: "https://apps.apple.com/app/id6806255929"

price:
  model: free
  value: "20 levels free · $2.99 unlocks 60 more"
schema_price: "0"
schema_high_price: "2.99"
schema_offer_count: "2"

plans_footnote: "Tare is a free download and Chapter I is free forever — it never expires and is never gated. The one purchase is a non-consumable: pay once, keep it, restore it any time from Settings or the unlock screen, and share it with up to five family members through Family Sharing. There are no subscriptions, no consumables, no ads and no energy meter. Chapters still open in order after you buy: Chapter II opens once you have solved 16 of Chapter I's 20 levels. US pricing shown; the App Store shows your local price at checkout."

plans:
  - name: "Chapter I"
    price: "Free"
    summary: "The Hang — twenty full levels, yours to keep. Not a trial, not a timer."
    features:
      - "20 handcrafted levels, including the wordless onboarding"
      - "Your first hidden weights and picture cards"
      - "The Lantern hint — free and unlimited"
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
  alt: "Tare on iPhone — a painted hanging mobile on a sky-blue board, with numbered weights on hooks and a “?” bubble beside its picture card"

who_for:
  - "You love logic puzzles with one real answer — sudoku, nonograms, Kakuro — and want something that feels physical"
  - "You want a brain teaser you can play offline, on a plane or underground, with no sign-in"
  - "You like to take your time: no timer, no lives, no move counter, no one watching"
  - "You want a game the whole family can play in any language, because there is nothing to read"
  - "You would rather pay once for the whole thing than meet an ad or a subscription"

who_not_for:
  - "You want a physics sandbox or a reflex game — Tare is turn-free and exact, and nothing falls over"
  - "You want leaderboards or multiplayer — there is no Game Center and no score"
  - "You play on Android or Mac — Tare is iPhone and iPad only, and needs iOS 26.5"
  - "You need progress to sync between devices — this version keeps it on the device you play on"

value_points:
  - title: "The scale can't be cheated"
    description: "A beam carrying an unsolved “?” never tilts truthfully — it sways, slowly, and never settles. So you can't hang a secret weight and watch which way the beam goes. The only way to know what it weighs is to read the picture cards and reason it out, which is what makes Tare a logic puzzle rather than trial and error."
  - title: "Every level has exactly one answer"
    description: "All 80 levels are built by hand and then proven by machine before they ship: exactly one arrangement balances, every hidden weight is pinned down by its cards alone, and any decoy piece fits no balanced arrangement at all. When a level clicks, it was your reasoning — never luck."
  - title: "No timer, no lives, no counting"
    description: "Take all the time you like. There is no move counter, no failure screen and no red buzzer — a complete but wrong board just gives a gentle shudder. The Lantern hint is free and unlimited, and nobody records how often you use it."
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
    description: "Hang the last piece right and the beams stop swaying, the whole mobile rings out in a single chord, gold stars pop, sparks fly and the sun comes out. Every weight has its own note — heavier is lower — so a solved mobile literally sounds balanced."
  - title: "The Lantern"
    description: "Stuck? The Lantern lights the way one small step at a time: first the card that matters, then the value of one hidden weight, then a ghost showing where a piece goes. It never places anything for you, and you always hang the final piece yourself."
  - title: "Three gold stars, never a gate"
    description: "Every level can earn up to three stars: Hung (it balanced), Unshaken (no complete-but-wrong board on the way) and Once (no piece you hung had to come back off). Your best is kept, the celebration is the same at any grade, and nothing is locked behind stars."
  - title: "Built for every player"
    description: "Every known weight shows both a numeral and domino pips, so colour is never the only cue. VoiceOver reads the mobile as named beams and hooks with place and return actions, the numeral grows with Dynamic Type, a High contrast switch clears 4.5:1, and Reduce Motion and Reduce Transparency are respected."
  - title: "Quiet by design"
    description: "Sound and haptics each have their own switch, and the game follows your device's light or dark appearance. A gentle parallax gives the board depth when you tilt the phone and turns itself off under Reduce Motion."

how_it_works:
  intro: "Tare runs on one rule — a beam is level when the pull on both sides is equal, and pull is weight times distance from the pivot. Here is how a level plays out."
  steps:
    - title: "Read the mobile"
      detail: "Beams hang from a pivot, with hooks at notches one to four on either side. Weights on the shelf below carry a number from 1 to 9, shown as a numeral and as pips. Some beams hang from other beams, and a hanging beam pulls with the total of everything below it."
    - title: "Hang the pieces"
      detail: "Drag a weight near a hook and it snaps on; drop it on an occupied hook to swap. Beams with nothing hidden on them tilt honestly as you go, so you can feel your way toward balance on the easy branches."
    - title: "Deduce the hidden weights"
      detail: "A beam carrying a “?” sways and will not tell you which way it leans. Read the picture cards above the board — equal, heavier, or balanced on unequal arms — and work out what the secret must weigh before you hang the rest."
    - title: "Fill every hook, and let it rest"
      detail: "When every hook is full and every beam is level, the mobile settles, rings out in one chord and shows its secrets. If the board is full but wrong, it gives one gentle shudder — no red, no buzzer — and you try again."

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
    a: "Open Settings in the game and tap Restore purchases, or tap Restore on the unlock screen. The purchase is tied to your Apple Account, so it comes back on any device signed in to it, and to family members through Family Sharing."
  - q: "Are there hints?"
    a: "Yes — the Lantern. It is free, unlimited and never counted. It works in small steps: it lights the clue card that matters, then reveals one hidden weight, then shows a ghost of where a piece goes. It never places a piece for you, and you always hang the final one yourself."
  - q: "What do the three stars mean?"
    a: "Hung means the mobile balanced. Unshaken means you never filled the board wrongly on that visit. Once means no piece you hung had to be taken back off. Your best result is kept, the celebration is the same whatever you earn, and nothing in the game is locked behind stars."
  - q: "Does Tare work offline, and does it collect data?"
    a: "It works completely offline — the game contains no networking code, so it behaves the same in airplane mode. It has no account, no ads, no analytics and no third-party SDKs, and it collects no data. Your progress and settings stay on your device. The only things that involve Apple are the purchase itself and the standard App Store review prompt."
  - q: "Can children or people who don't read English play it?"
    a: "Yes. There are no words anywhere in the puzzle, so it plays the same in every language and at any age. There are no ads, no chat, no accounts and nothing collected. The one screen with words is the unlock screen, and purchases go through Apple, so Ask to Buy and Screen Time apply."
  - q: "Does it run on iPad or Mac, and does progress sync?"
    a: "Tare runs on iPhone and iPad and needs iOS 26.5 or later. It plays in portrait, and on iPad the mobile sits in a centred column. There is no Mac version. Progress is stored on the device you play on and does not sync between devices in this version; the unlock itself restores on any device with your Apple Account."
  - q: "Is Tare accessible?"
    a: "Accessibility was built in, not bolted on. Every known weight shows a numeral and domino pips, so colour is never the only cue. VoiceOver reads the mobile as a tree of named beams, hooks and weights with place and return actions (spoken labels are English at launch). There is a High contrast switch, the numeral scales with Dynamic Type, hooks have a generous 60-point snap, and Reduce Motion and Reduce Transparency are both respected."

privacy:
  tracking: false
  account_required: false
  data_collection: "none"
  notes:
    - "No account, no server, and no networking code anywhere in the game"
    - "Progress, star grades and settings are stored only on your device"
    - "No analytics, advertising or third-party SDKs of any kind"
    - "Hint use is never recorded — not even on your device"
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

release:
  first_release: "2026-09-14"
  last_updated: "2026-09-14"
  version: "1.0"

show_body: true
about_heading: "What Tare is — a balance puzzle you solve by deduction"
---

Tare is a logic puzzle disguised as a toy. Each level is a painted hanging mobile on a sky-blue board, with a shelf of numbered weights beneath it. Your job is to hang every weight on a hook so that **every beam balances at the same time**.

The rule fits in one line: a beam is level when **weight × distance from the pivot** is equal on both sides. A 2 on the second notch balances a 4 on the first. When one beam hangs from another, it pulls on its hook with everything below it, so a single move near the bottom ripples all the way up the tower.

## The rule that makes it a logic puzzle

Early in the game, some weights arrive hidden inside a bubble marked with a **“?”**. You could expect to hang one and watch the beam tip to learn what it weighs. Tare doesn't let you: **a beam carrying an unsolved “?” sways and never tells the truth.**

What you get instead are small picture cards pinned above the board. Each one quotes a few of the pieces in miniature, showing that this one equals that one, that one outweighs a pair, or that two of them balance on unequal arms. The cards alone are enough to pin down every hidden value, and you have to reason it out. When the last piece goes on and the mobile rings out, you *know* why it balanced.

Every level is built by hand and then **proven by machine** before it ships. It must have exactly one balanced arrangement, every hidden weight must be fixed by its cards, and every decoy must fit no balanced arrangement at all.

## Four chapters

- **The Hang** (Morning Sky, free): arranging weights on every shape of mobile, your first nested beam and your first secrets.
- **The Secret** (Twilight Meadow): reading the cards, with tilted comparisons that bracket a value and ratio cards on unequal arms.
- **The Cascade** (Deep Sea): mobiles three beams deep as the norm.
- **The Exhibition** (Evening Stars): more pieces on the shelf than hooks on the mobile, so you have to prove which ones belong nowhere.

Each chapter holds twenty levels. The first chapter is free forever. One $2.99 purchase opens the other sixty, with Family Sharing and no subscription.

## What it does not do

No ads. No timer, no lives, no move counter, no score. No account and no sign-in. No analytics, no third-party SDKs and no networking code, so Tare plays the same underground as it does on Wi-Fi. The Lantern hint is free and unlimited, and nobody counts how often you use it, including the game itself.

Tare runs on iPhone and iPad with iOS 26.5 or later. The [privacy policy](/apps/tare/privacy/) sets out exactly what stays on your device and what Apple handles instead.
