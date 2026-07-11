---
layout: app
slug: chessful
name: "Chessful"
tagline: "Understand your mistakes. Improve every game."
quick_answer: "Chessful is a chess training and game analysis app for iPhone, iPad, and Mac. It uses Stockfish to review every move, then explains your mistakes in plain language and builds adaptive training from your actual weaknesses — tactics, defense, openings, endgames. Includes 40 AI opponents. Free with Premium from $4.99/month, $29.99/year, or $39.99 lifetime. Fully offline, no account, no ads, no tracking."
category: games
platforms: ["iOS", "iPadOS", "macOS"]
status: live

app_store_url: "https://apps.apple.com/app/id6761336870"

price:
  model: freemium
  value: "Free — Premium from $4.99/mo"
schema_price: "0"
schema_high_price: "39.99"
schema_offer_count: "4"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The lifetime tier is a one-time purchase — no auto-renew. Universal Purchase across iPhone, iPad, and Mac."

# Free / Premium-Monthly / Premium-Annual / Lifetime — surfaces the full upgrade
# ladder. Lifetime sits at roughly 10 months of monthly Premium, which is the
# conversion math you want readers to see at a glance.
plans:
  - name: "Free"
    price: "$0"
    summary: "Stockfish analysis, 40 AI opponents, and the core training loop."
    features:
      - "Play any of the 40 AI opponents"
      - "Stockfish analysis of every move you make"
      - "Plain-language mistake summaries on each game"
      - "3 free training sessions per week"
      - "Basic skill tracking across the 5 dimensions"
      - "Works fully offline, no account"
  - name: "Premium · Monthly"
    price: "$4.99/mo"
    summary: "Full Premium, billed monthly. Cancel anytime."
    features:
      - "Unlimited deep game analysis with full move-by-move commentary"
      - "Unlimited adaptive training sessions"
      - "Full progress tracking across tactics, defense, positional play, openings, endgames"
      - "Long-term skill-trend graphs (90 / 180 / 365 days)"
      - "Alternative-move exploration with strategic reasoning"
      - "7-day free trial · cancel anytime"
  - name: "Premium · Annual"
    price: "$29.99/yr"
    summary: "Same Premium features, billed once a year. ~50% cheaper than paying monthly."
    features:
      - "Everything in Premium · Monthly"
      - "~50% cheaper than monthly over a year"
      - "7-day free trial · cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "$39.99 once"
    summary: "All Premium features. Roughly 10 months of monthly Premium — then yours."
    features:
      - "Everything in Premium · Annual"
      - "One-time purchase, no renewal"
      - "Universal Purchase across iPhone, iPad, and Mac"
      - "Restores on every device signed in with the same Apple ID"
      - "Family Sharing — share with up to 5 family members at no extra cost"
    highlight_label: "Best long-term value"

icon: "/assets/icons/chessful.png"
og_image: "/assets/og/chessful.png"

seo:
  title: "Chess Training & Analysis App for iPhone & Mac | Chessful"
  description: "Chess training app for iPhone, iPad, Mac. Stockfish analysis explained in plain language, adaptive training, 40 AI opponents. Free, fully offline."
  keywords:
    - chess training app
    - chess training app iphone
    - chess training app ipad
    - chess training app mac
    - chess game analysis
    - chess game analysis app
    - chess improvement app
    - chess tactics trainer
    - chess coach app
    - chess mistakes explained
    - chess puzzles app
    - learn chess strategy
    - chess endgame trainer
    - offline chess app
    - chess skill tracker
    - adaptive chess training
    - Stockfish iPhone
    - chess analysis without account
    - chess app no ads
    - chess.com alternative offline

hero:
  pre_headline: "Chess training & analysis app for iPhone, iPad, and Mac"
  headline: "Stop guessing. Start understanding."
  subheadline: "Chessful analyzes your games with Stockfish, explains your mistakes in plain language, and builds adaptive training around your real weaknesses — tactics, defense, openings, endgames. 40 AI opponents, fully offline. Free with Premium from $4.99/month."
  cta_label: "Download Free"
  alt: "Chessful — chess game being analyzed with Stockfish on iPhone, with plain-language commentary"

who_for:
  - "You know the rules but keep losing and don't understand why"
  - "You want plain-language explanations of your mistakes, not raw Stockfish evaluation numbers"
  - "You're stuck at a rating plateau and want training built from your own weaknesses"
  - "You prefer playing offline without a Chess.com or Lichess account"
  - "You care about pattern recognition across tactics, defense, positional play, openings, and endgames"
  - "You want the app on iPhone, iPad, and Mac — one purchase, all three"

who_not_for:
  - "You primarily want to play live online matchmaking and chase ELO"
  - "You're an absolute beginner learning how pieces move (start with a teaching app first)"
  - "You want social features, tournaments, or community play"
  - "You want a celebrity-coached experience (Magnus Trainer is built around that pitch — Chessful is not)"

# Organization-type founder block — attributes to the studio rather than a
# named person. Same pattern as allpaid.md.
founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "For the club player who wants a teacher, not a centipawn graph."
  story: "Chessful exists because we tried every chess analysis app and engine UI on iOS and Mac and kept hitting the same wall: every tool shows you a centipawn line and assumes you can read it. Most players can't, and not because they're not serious — because reading engine lines is a different skill from playing chess. Chessful was built to translate the engine output into the sentences a teacher would write, then turn that translation into spaced-repetition training on the patterns where you actually lose. Stockfish runs entirely on the device; the explanations are hand-curated motif detectors plus a small language model running locally; nothing leaves your phone."
  signals:
    - "Stockfish runs on-device — no cloud analysis, no rate-limited daily quota, no account"
    - "Forty distinct AI opponents engineered to feel like forty different players, not one engine at forty noise settings (see the [forty-opponents journal post](/journal/forty-chess-opponents/) for the design note)"
    - "Privacy Manifest declares zero tracking domains and no required-reason APIs beyond local storage"
    - "18 live apps in the Lagerland catalogue, all under the same data discipline: no tracking, no ads, no required accounts"
  external_link:
    label: "Read the Lagerland studio backstory →"
    href: "/lagerland-apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally — usually within a day."

alternatives_to:
  - "Chess.com"
  - "Lichess"
  - "Magnus Trainer"
  - "Chessis"
  - "Chessly"
  - "Chessable"
  - "Really Bad Chess"

value_points:
  - title: "Understand why you lost"
    description: "After every game, Chessful shows exactly where you went wrong, what you missed, and why it mattered — in words, not engine numbers. The hung piece, the missed fork, the prophylactic move you skipped."
  - title: "Train your real weaknesses"
    description: "Hanging pieces? Missed tactics? Weak defense? Your training adapts automatically to what you actually struggle with, using spaced repetition on patterns lifted directly from your own losses."
  - title: "Watch yourself improve"
    description: "Track progress across tactics, defense, positional play, openings, and endgames. Long-term trend graphs (90 / 180 / 365 days on Premium) show skill growth — not just rating."
  - title: "Fully offline, fully private"
    description: "Stockfish runs on the device. No account, no servers, no daily analysis quota, no ads. Just you and the board, on a flight, in a kitchen, or anywhere without signal."

features:
  - title: "Game analysis you understand"
    description: "Every move reviewed with Stockfish — but explained in clear, simple sentences. Blunders, missed tactics, weak moves, prophylactic skips, structural concessions: each described so you actually learn from them, rather than nodding at a centipawn graph."
  - title: "Training built from your games"
    description: "Chessful identifies the patterns in your mistakes — a hanging back-rank, a missed fork shape, a recurring opening lapse — and generates focused training sessions. Spaced repetition ensures your weakest areas get the most attention without flooding you."
  - title: "40 unique AI opponents"
    description: "Play against opponents engineered to feel like forty different players: each with its own opening repertoire, structural preferences, and characteristic blind spots — from club beginner to master strength. No noise-slider engine."
  - title: "Skill tracking across five dimensions"
    description: "Tactics, defense, positional play, openings, and endgames — each tracked separately over time. Premium adds 90 / 180 / 365-day trend graphs so you can see where you're growing and where you're plateauing."
  - title: "Explore better alternatives"
    description: "After analysis, browse the moves you should have played. Understand the ideas behind stronger positions — not just which square the engine prefers, but why that square mattered structurally."
  - title: "Universal Purchase across iPhone, iPad, and Mac"
    description: "One purchase covers all three platforms — iPhone for opportunistic play and training, iPad for board-sized study, Mac for serious post-game review. Progress and Premium status sync via standard iCloud Keychain."

# Methodology disclosure — the highest-leverage E-E-A-T artefact for a
# product page in a category where most competitors hide their algorithm.
# Emits HowTo schema automatically via _layouts/app.html.
how_it_works:
  intro: "Chessful's adaptive training is the part of the app that does the real teaching work. Here's exactly what happens between you losing a game and Chessful generating tomorrow's training session."
  steps:
    - title: "Stockfish reviews every move"
      detail: "When a game ends, Chessful runs Stockfish locally over the full move list and produces an evaluation per move. The engine runs on-device — no cloud calls, no rate-limited quota, no account. Same Stockfish you'd see on Chess.com or Lichess, just running on your iPhone, iPad, or Mac."
    - title: "Motif detectors classify each mistake"
      detail: "Raw centipawn loss is unreadable. A layered model — engine output combined with hand-curated motif detectors — classifies each significant mistake into one of about thirty categories: hung piece, missed fork, missed pin, weak back rank, prophylactic skip, opening repertoire lapse, endgame technique error, and so on. Each motif is mapped to one of the five skill dimensions."
    - title: "Plain-language explanation generated"
      detail: "A small on-device language model expands the motif label and engine evaluation into one or two sentences a club player can read. \"You played Nxd5 — your knight was the only defender of the back rank, and Black's queen took mate in two\" beats \"+3.8 → −8.1, line: Nxd5 Qxe1+ Kh2 Qe5+ g3 Qxd5\" every time."
    - title: "Patterns added to your skill buckets"
      detail: "Each detected mistake updates a per-skill-dimension counter. After three games where you skipped a prophylactic move, the Defense bucket gets a flag. After two missed fork shapes, the Tactics bucket gets a flag. The buckets are visible — you can see exactly which patterns are accumulating."
    - title: "Spaced-repetition training queue generated"
      detail: "Each training session pulls from the flagged buckets using a spaced-repetition schedule (positions seen most recently are seen again sooner; positions you've solved correctly twice in a row drop out). Sessions are 5–10 minutes each. The Free tier offers three sessions per week; Premium is unlimited."
    - title: "Skill graphs update"
      detail: "After each session, the five-dimension skill trend graphs update. Premium adds 90 / 180 / 365-day views so you can see whether your last three weeks of training is actually moving the dial on (say) endgame technique, or whether you're plateauing and need a different intervention."

# Example "mistake explained" gallery — the page's strongest USP, shown
# rather than described. Anchored to /apps/chessful/#templates.
example_insights:
  anchor: "templates"
  overline: "What Chessful explains"
  heading: "What a plain-language mistake looks like in Chessful."
  intro: "Six worked examples of how Chessful translates a Stockfish evaluation into something a club player can actually use. Every example is the kind of mistake the adaptive trainer then drills against tomorrow's session."
  cards:
    - tag: "Tactics · Hung piece"
      headline: "You played Nxd5. The knight was your only back-rank defender."
      body: "After Nxd5, Black plays Qxe1+ — the knight you just captured with was your only defender of the e1 square. Mate in 2. The right move was Bf4, keeping the knight on c3 where it stops the queen's path. Pattern: defender-removal blindness."
    - tag: "Tactics · Missed fork"
      headline: "You played Bd3. Black had a fork on c2."
      body: "Black's knight on b4 was one move from c2, forking your queen and rook. After Bd3, you walked into it: Nxc2+ wins the exchange. The right move was Qd2, defending c2 with the queen. Pattern: enemy-piece radius blindness."
    - tag: "Defense · Weak king"
      headline: "You castled into a half-open f-file with no defenders."
      body: "Castling short looked safe — but Black had a rook on f8 and the f-pawn was missing. Three moves later, Rxf2 cracked the position open. The right plan was to develop the knight to g3 first, blocking the f-file before castling. Pattern: structural-prerequisite skip."
    - tag: "Openings · Repertoire lapse"
      headline: "Move 7 deviated from your usual French setup."
      body: "You've played the French Defense Winawer 23 times in your games. Move 7 here was Nf6 instead of the usual Qa5+. The deviation lost a tempo and let White's bishop reach an active square. Pattern: repertoire drift — Chessful flags this for opening drill."
    - tag: "Endgame · Technique error"
      headline: "King and pawn endgame: you took the opposition the wrong way."
      body: "With pawns on e5 vs e6, you played Kd4 — losing the opposition. The right move was Kf4, taking the opposition and forcing Black's king to retreat. The pawn promotes in 7 moves. Pattern: opposition direction error — Chessful queues opposition-pattern training."
    - tag: "Tactics · Back-rank mate"
      headline: "You played h3 to give the king luft. It was three moves too late."
      body: "Black's rook had already swung to d8 and the queen was on e7 — back-rank mate was already threatened. h3 was correct prophylaxis, but the right time to play it was move 18, not move 24. Pattern: prophylactic-timing miss — Chessful drills the recognition pattern."

# Side-by-side comparison — replaces the templated alternatives card grid
# with substantive feature deltas. Auto-triggers the mid-page CTA.
comparison_table:
  intro: "Every row is a question a serious chess player asks before installing a training or analysis app. Chess.com is the dominant online platform; Lichess is the free open-source alternative; Magnus Trainer is the celebrity-coached training app (now Chess.com-owned); Chessis is the closest on-device analysis-focused peer. Verified from each app's public landing page and App Store listing on 2026-05-13."
  competitors: ["Chessful", "Chess.com", "Lichess", "Magnus Trainer", "Chessis"]
  rows:
    - feature: "Fully offline (no internet required)"
      values: ["Yes — Stockfish runs on-device", "No — cloud analysis", "Mostly cloud", "No — cloud", "Yes — Stockfish on-device"]
    - feature: "Account required"
      values: ["No account ever", "Required", "Optional but expected", "Required (Chess.com)", "No account"]
    - feature: "Daily analysis quota"
      values: ["Unlimited (Premium); unlimited basic analysis on Free", "1 game review/day on Free; unlimited on paid", "Unlimited (free)", "Lessons-based, not analysis-based", "Unlimited (Pro)"]
    - feature: "Plain-language mistake explanations"
      values: ["Yes — motif detectors + on-device LM", "Centipawn lines + Game Review (paid)", "Centipawn lines + community annotations", "Lessons rather than per-game review", "Yes — game-report sentences"]
    - feature: "Adaptive training built from your games"
      values: ["Yes — spaced repetition on detected motifs", "Lessons + puzzles, not derived from your games", "Puzzle Storm + study tool — not derived adaptively", "Curated lessons — not your-game-derived", "Mistakes report — no training queue"]
    - feature: "Number of AI opponents"
      values: ["40, distinct styles", "1 engine + bots library", "1 engine + bots", "Magnus + ~12 personality bots", "Not focused on play"]
    - feature: "Live human matchmaking"
      values: ["No (intentional)", "Yes — global", "Yes — global, free", "No", "No"]
    - feature: "Lifetime / one-time pricing"
      values: ["$39.99 lifetime", "Subscription only ($9.99–$14/mo)", "Free / donation", "$299.99 lifetime (else subscription)", "One-time Pro purchase"]
    - feature: "Privacy — no tracking, no third-party SDKs"
      values: ["Zero tracking SDKs, App Privacy: nothing collected", "Standard analytics + ads SDKs", "No ads, minimal analytics", "Standard Chess.com analytics", "Minimal — no ads on Pro"]
    - feature: "Platforms"
      values: ["iPhone + iPad + Mac (Universal Purchase)", "Web + iPhone + iPad + Mac + Android", "Web + iPhone + iPad + Android", "iPhone + iPad + Mac + Vision", "Android primary; iOS limited"]
  footnote: "Competitor positioning summarised from each app's public landing page and App Store listing on 2026-05-13. Pricing and feature claims change frequently — verify before switching."

# Roadmap — addresses the three most-asked product-gap questions
# (PGN / Lichess / Chess.com import; Apple Watch; puzzle trainer) on-page
# rather than burying them in FAQ.
roadmap:
  overline: "Roadmap"
  heading: "What's shipped, what's next."
  intro: "Chessful covers offline play, analysis, and adaptive training on iPhone, iPad, and Mac today. Below is the public roadmap for what's next. Dates are targets, not commitments — slips happen and you'll hear about them here first."
  items:
    - when: "Shipped"
      title: "Stockfish analysis + plain-language explanations"
      detail: "Live today on iPhone, iPad, and Mac. Every move reviewed, every significant mistake translated into a sentence a club player can read."
      status: "shipped"
    - when: "Shipped"
      title: "40 AI opponents + 5-dimension skill tracking"
      detail: "Forty distinct opponent personalities, each with its own opening repertoire and structural preference. Skill tracking across tactics, defense, positional play, openings, endgames."
      status: "shipped"
    - when: "Shipped"
      title: "Adaptive training queue with spaced repetition"
      detail: "Training sessions generated from the motifs detected in your own losses, scheduled with spaced repetition."
      status: "shipped"
    - when: "Targeted 2026 Q3"
      title: "PGN import — bring your existing games in"
      detail: "Import any PGN file (one game or a tournament archive) and have Chessful analyse the lot, building your skill profile from games you've already played. Standard PGN parsing — works with exports from any chess platform."
    - when: "Targeted 2026 Q4"
      title: "Chess.com & Lichess game import"
      detail: "Paste a Chess.com or Lichess username and pull your last N games into Chessful's analyser and training queue. Read-only — no posting, no syncing back. Imports are stored on-device only."
    - when: "Targeted 2026 Q4"
      title: "Apple Watch — Smart Stack complication"
      detail: "Today's training-queue card on the wrist. Tap to start a 5-minute pattern-recognition session. Sync via standard iOS pairing — no separate account."
    - when: "Under consideration"
      title: "Standalone puzzle / tactics trainer"
      detail: "A puzzle mode separate from the games-derived training queue, drawing from a curated motif library. Currently out of scope — Chessful's thesis is that training derived from your own losses outperforms generic puzzle-rush — but exploring whether a complementary mode would help users at the start before they have many games logged."
  disclaimer: "Roadmap last reviewed 2026-05-13. Targeted dates can slip; shipped items are live on the App Store."

screenshots:
  - "/assets/screenshots/chessful/1.png"
  - "/assets/screenshots/chessful/2.png"
  - "/assets/screenshots/chessful/3.png"
  - "/assets/screenshots/chessful/4.png"
  - "/assets/screenshots/chessful/5.png"
  - "/assets/screenshots/chessful/6.png"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no trackers"
    - "No account or sign-up required"
    - "All analysis runs locally on your device — Stockfish, motif detectors, and the explanation model all on-device"
    - "Works fully offline — no cloud calls, no daily analysis quota"
    - "Universal Purchase across iPhone, iPad, and Mac via standard Apple infrastructure"

faq:
  - q: "What is Chessful?"
    a: "Chessful is a chess training and game analysis app for iPhone, iPad, and Mac. It analyzes your games with Stockfish, explains your mistakes in plain language, and builds adaptive training sessions focused on your real weaknesses across five skill dimensions: tactics, defense, positional play, openings, and endgames."
  - q: "How is Chessful different from Chess.com or Lichess?"
    a: "Chess.com and Lichess are network-effect online platforms — millions of opponents, ranked play, daily analysis quota. Chessful is fully offline, on-device, no-account, and built for the player who wants a teacher rather than a community. Stockfish runs locally on your iPhone, iPad, or Mac; explanations are in plain language rather than centipawn lines; training is generated adaptively from your own losses rather than from a generic puzzle library."
  - q: "How is Chessful different from Magnus Trainer?"
    a: "Magnus Trainer is a celebrity-coached lessons app — curated content by Magnus Carlsen and his team, organised as bite-sized games and theory courses. Chessful does not ship celebrity content; instead, training is derived from the specific patterns in your own losses. The two are complementary: Magnus Trainer for structured lessons, Chessful for adaptive training on your real weaknesses. Many improving players use both."
  - q: "How is Chessful different from Chessis?"
    a: "Chessis is the closest direct peer — both ship Stockfish + on-device analysis + plain-language explanations + one-time pricing. The differences: Chessful adds the adaptive-training queue (spaced repetition on motifs from your games), 40 distinct AI opponents you can play against, and a Universal Purchase across iPhone, iPad, and Mac. Chessis is currently Android-primary with one-time Pro pricing focused tightly on the analysis flow."
  - q: "Is Chessful good for beginners?"
    a: "Chessful is ideal for players who know the rules and have played at least a few full games. If you're an absolute beginner learning how the pieces move, start with a teaching app first — Chessful's training assumes you can read a position. For players around 800-1800 rating who are stuck on a plateau and don't understand why, Chessful is built for you."
  - q: "Does Chessful work offline?"
    a: "Yes. Every part of Chessful — Stockfish analysis, motif detection, plain-language explanations, adaptive training, the 40 AI opponents — runs entirely on your device. No internet connection is needed, ever. You can play and analyse on a flight, in a kitchen, or on the subway."
  - q: "What chess engine does Chessful use?"
    a: "Chessful uses Stockfish — the same world-class open-source engine that powers Chess.com's analysis and Lichess's evaluation. It runs locally on your iPhone, iPad, or Mac at a depth tuned to the device. Chessful then translates Stockfish's centipawn output into plain-language sentences using motif detectors and a small on-device language model."
  - q: "Is Chessful free? What does Premium cost?"
    a: "Chessful is free to try with the 40 AI opponents, basic game analysis on every game, three training sessions per week, and basic skill tracking — no ads, no account. Premium unlocks unlimited deep game analysis, unlimited adaptive training, the full progress dashboard with 90/180/365-day skill-trend graphs, and alternative-move exploration. Premium is $4.99/month, $29.99/year, or $39.99 once for lifetime access with a 7-day free trial. Lifetime supports Family Sharing — one purchase covers up to 5 family members at no extra cost. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does Chessful track my improvement?"
    a: "Yes. Chessful tracks your skills across five areas — tactics, defense, positional play, openings, and endgames — showing how each improves over time. The Free tier shows basic counts; Premium adds 90 / 180 / 365-day trend graphs so you can see whether the last three weeks of training is actually moving the dial on (say) endgame technique."
  - q: "Does Chessful need an account?"
    a: "No. Chessful requires no account, no sign-up, and no personal information. Your games, analysis, and training progress stay entirely on your device. Universal Purchase status syncs via standard iCloud Keychain — Apple's mechanism, not a Chessful account."
  - q: "Can I import games from Chess.com or Lichess?"
    a: "Not yet — Chess.com and Lichess game import is targeted for 2026 Q4 (see the on-page roadmap). PGN import (the universal chess-game-exchange format) is targeted for 2026 Q3, which will be the first path. Once shipped, you'll be able to paste a Chess.com or Lichess username and pull your recent games into Chessful's analyser and training queue."
  - q: "Does Chessful have a tactics-puzzle trainer like Chess.com?"
    a: "Chessful's training queue is derived from the mistake patterns in your own games rather than from a generic puzzle pool — the thesis is that adaptive training on your real weaknesses outperforms puzzle-rush. A standalone curated puzzle mode is under consideration on the roadmap, particularly to help new users at the start before they have many games logged in the app."
  - q: "Does Chessful work on Apple Watch?"
    a: "Not yet — Apple Watch (Smart Stack complication with today's training-queue card) is targeted for 2026 Q4 (see the on-page roadmap). Dates are targets, not commitments. iPad and Mac are supported today via Universal Purchase."
  - q: "Is Chessful a replacement for Chess.com or Lichess?"
    a: "No. Chessful does not offer ranked play, live human matchmaking, or leaderboards. It is designed for the player who wants to improve quietly against varied AI opponents with readable explanations, without an account or a daily quota. For ranked human play, Chess.com and Lichess remain the right tools. Many improving players use Chessful for analysis and training and one of those platforms for matchmaking."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/chessful/support/"

release:
  first_release: "2026-04-01"
  last_updated: "2026-05-13"

ratings:
  value: "3.7"
  count: 3
  last_synced: "2026-06-13"
related_journal:
  slug: forty-chess-opponents
  anchor: "Forty chess opponents — and why no two of them are the same engine"

# Render the markdown body as a visible "About Chessful." section with
# contextual in-body internal links to the methodology, templates,
# comparison, and privacy sections. SearchPilot: in-body contextual
# links return 5–25% organic uplift.
show_body: true
about_heading: "What Chessful does — chess training, analysis, 40 opponents"
---
Chessful is a [chess training & analysis app for iPhone, iPad, and Mac](#features) — built around the idea that Stockfish's centipawn numbers don't help most players improve. The app reviews every move you make, then turns the engine's output into plain English: which piece you hung, which fork you missed, which prophylactic move would have saved the position. From there, [Chessful builds an adaptive training queue](#how-it-works) targeted at the patterns where you actually lose — tactics, defense, positional play, openings, endgames — using spaced repetition and forty AI opponents tuned to specific playing styles.

The thing that makes Chessful different from Chess.com, Lichess, and Magnus Trainer isn't the engine — they all run Stockfish or a derivative. It's the [layer that sits on top of the engine](#how-it-works): motif detectors that classify each significant mistake into one of about thirty categories (hung piece, missed fork, weak back rank, prophylactic skip, repertoire lapse, endgame technique error) and a small on-device language model that expands each classification into one or two sentences you can read. See [example explanations](#templates) for what this actually looks like in practice.

Every part of Chessful runs on your device. Stockfish, the motif detectors, the explanation model, and the forty AI opponents — all on-device. There is no cloud, no rate-limited daily analysis quota, no account to make, no daily ranking attached to your name. The trade-off is that Chessful does not offer ranked play or live human matchmaking — for that, Chess.com and Lichess remain the right tools. Chessful is designed for the player who wants a teacher, not a community. See the [side-by-side comparison](#compare-heading-chessful) for the full feature deltas vs Chess.com, Lichess, Magnus Trainer, and Chessis — or, for the whole category in one place (which app fits playing, learning openings, or understanding your losses), our [honest guide to the best chess apps for iPhone](/guides/best-chess-apps-iphone/).

The forty AI opponents took disproportionate engineering effort and are documented separately in the [forty-opponents journal post](/journal/forty-chess-opponents/) — each opponent has its own opening repertoire, structural preference, and characteristic blind spots, so games feel like playing different players rather than a single engine at forty noise settings. The [adaptive training methodology](/journal/how-chessful-builds-adaptive-training/) is documented in a separate post.

Free tier: 40 AI opponents, Stockfish analysis on every game, plain-language mistake summaries, three training sessions per week, basic skill tracking. Premium: unlimited deep analysis, unlimited adaptive training, full progress tracking with 90/180/365-day trend graphs, alternative-move exploration. $4.99/month, $29.99/year, or $39.99 once for [lifetime](/apps/chessful/#pricing) with a 7-day free trial. [No tracking, no ads, no account](/apps/chessful/privacy/) — verified by the App Store privacy nutrition label. Published by Lagerland Apps, an independent Apple developer in Finland.
