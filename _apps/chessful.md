---
layout: app
slug: chessful
name: "Chessful"
tagline: "Understand your mistakes. Improve every game."
quick_answer: "Chessful is a chess training and game analysis app for iPhone, iPad, and Mac. It uses Stockfish to review every move, explains your mistakes in plain language, and builds adaptive training from your actual weaknesses in tactics, defense, openings, and endgames. It includes 40 AI opponents. Free, with Premium from {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime. Works fully offline, with no account, no ads, and no tracking."
category: games
status: live

app_store_url: "https://apps.apple.com/app/id6761336870"

price:
  model: freemium

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The lifetime tier is a one-time purchase with no auto-renewal. Universal Purchase across iPhone, iPad, and Mac."

# Free / Premium-Monthly / Premium-Annual / Lifetime: surfaces the full upgrade
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
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Premium, billed monthly. Cancel anytime."
    features:
      - "Unlimited deep game analysis with full move-by-move commentary"
      - "Unlimited adaptive training sessions"
      - "Full progress tracking across tactics, defense, positional play, openings, endgames"
      - "Long-term skill-trend graphs (90 / 180 / 365 days)"
      - "Alternative-move exploration with strategic reasoning"
      - "7-day free trial · cancel anytime"
  - name: "Premium · Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same Premium features, billed once a year. ~{SAVE_YEARLY}% cheaper than paying monthly."
    features:
      - "Everything in Premium · Monthly"
      - "~{SAVE_YEARLY}% cheaper than monthly over a year"
      - "7-day free trial · cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All Premium features, paid once. Costs about the same as {LIFETIME_MONTHS} months of monthly Premium."
    features:
      - "Everything in Premium · Annual"
      - "One-time purchase, no renewal"
      - "Universal Purchase across iPhone, iPad, and Mac"
      - "Restores on every device signed in with the same Apple ID"
      - "Family Sharing: share with up to 5 family members at no extra cost"
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
  headline: "Find out why you lost, then train on it."
  subheadline: "Chessful analyzes your games with Stockfish, explains your mistakes in plain language, and builds adaptive training around your real weaknesses in tactics, defense, openings, and endgames. It has 40 AI opponents and works fully offline. Free, with Premium from {P_MONTHLY}/month."
  cta_label: "Download Free"
  alt: "Chessful analyzing a chess game with Stockfish on iPhone, with plain-language commentary"

who_for:
  - "You know the rules but keep losing and don't understand why"
  - "You want plain-language explanations of your mistakes, not raw Stockfish evaluation numbers"
  - "You're stuck at a rating plateau and want training built from your own weaknesses"
  - "You prefer playing offline without a Chess.com or Lichess account"
  - "You care about pattern recognition across tactics, defense, positional play, openings, and endgames"
  - "You want the app on iPhone, iPad, and Mac, with one purchase covering all three"

who_not_for:
  - "You primarily want to play live online matchmaking and chase ELO"
  - "You're an absolute beginner learning how pieces move (start with a teaching app first)"
  - "You want social features, tournaments, or community play"
  - "You want a celebrity-coached experience (Magnus Trainer is built around that pitch; Chessful is not)"

# Organization-type founder block: attributes to the studio rather than a
# named person. Same pattern as allpaid.md.
founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "For the club player who wants mistakes explained in words."
  story: "We built Chessful after trying every chess analysis app and engine UI on iOS and Mac. Each one shows you a centipawn line and assumes you can read it. Most players can't, and that has nothing to do with how serious they are: reading engine lines is a different skill from playing chess. Chessful translates the engine output into the sentences a teacher would write, then turns them into spaced-repetition training on the patterns where you actually lose. Stockfish runs entirely on the device, and the explanations come from hand-curated motif detectors plus a small language model running locally. Nothing leaves your phone."
  signals:
    - "Stockfish runs on-device, so there is no cloud analysis, no rate-limited daily quota, and no account"
    - "Forty AI opponents, each built to play like a different person instead of one engine at forty noise settings (design notes in the [forty-opponents journal post](/journal/forty-chess-opponents/))"
    - "Privacy Manifest declares zero tracking domains and no required-reason APIs beyond local storage"
    - "{APP_COUNT} live apps in the Lagerland catalogue, all with the same data rules: no tracking, no ads, no required accounts"
  external_link:
    label: "Read the Lagerland studio backstory →"
    href: "/lagerland-apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally, usually within a day."

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
    description: "After every game, Chessful shows where you went wrong, what you missed, and why it mattered, in words instead of engine numbers: the hung piece, the missed fork, the prophylactic move you skipped."
  - title: "Train your real weaknesses"
    description: "Hanging pieces, missed tactics, weak defense: your training adapts to what you actually struggle with, using spaced repetition on patterns taken from your own losses."
  - title: "Watch yourself improve"
    description: "Track progress across tactics, defense, positional play, openings, and endgames. Long-term trend graphs (90 / 180 / 365 days on Premium) show how each skill grows, which a rating alone can't."
  - title: "Offline and private"
    description: "Stockfish runs on the device. There is no account, no server, no daily analysis quota, and no ads, so it works on a flight, in a kitchen, or anywhere without signal."

features:
  - title: "Game analysis you understand"
    description: "Stockfish reviews every move, and Chessful explains the result in clear, simple sentences. Blunders, missed tactics, weak moves, prophylactic skips, and structural concessions are each described so you learn from them instead of nodding at a centipawn graph."
  - title: "Training built from your games"
    description: "Chessful finds the patterns in your mistakes (a hanging back rank, a missed fork shape, a recurring opening lapse) and generates focused training sessions. Spaced repetition gives your weakest areas the most attention without flooding you."
  - title: "40 unique AI opponents"
    description: "Each opponent plays like a different person, with its own opening repertoire, structural preferences, and blind spots, from club beginner to master strength. None of them is the engine with a noise slider."
  - title: "Skill tracking across five dimensions"
    description: "Tactics, defense, positional play, openings, and endgames are each tracked separately over time. Premium adds 90 / 180 / 365-day trend graphs so you can see where you're growing and where you've plateaued."
  - title: "Explore better alternatives"
    description: "After analysis, browse the moves you should have played and the ideas behind them: which square the engine prefers, and why that square mattered structurally."
  - title: "Universal Purchase across iPhone, iPad, and Mac"
    description: "One purchase covers all three platforms: iPhone for quick games and training, iPad for board-sized study, Mac for detailed post-game review. Progress and Premium status sync via standard iCloud Keychain."

# Methodology disclosure: the highest-leverage E-E-A-T artefact for a
# product page in a category where most competitors hide their algorithm.
# Emits HowTo schema automatically via _layouts/app.html.
how_it_works:
  intro: "Chessful's adaptive training does most of the teaching. This is what happens between you losing a game and Chessful generating tomorrow's training session."
  steps:
    - title: "Stockfish reviews every move"
      detail: "When a game ends, Chessful runs Stockfish locally over the full move list and records an evaluation for each move. The engine runs on-device, with no cloud calls, no rate-limited quota, and no account. It is the same Stockfish you'd see on Chess.com or Lichess, running on your iPhone, iPad, or Mac."
    - title: "Motif detectors classify each mistake"
      detail: "Raw centipawn loss is unreadable. A layered model, engine output combined with hand-curated motif detectors, sorts each significant mistake into one of about thirty categories: hung piece, missed fork, missed pin, weak back rank, prophylactic skip, opening repertoire lapse, endgame technique error, and so on. Each motif maps to one of the five skill dimensions."
    - title: "Plain-language explanation generated"
      detail: "A small on-device language model turns the motif label and engine evaluation into one or two sentences a club player can read. \"You played Nxd5, but your knight was the only defender of the back rank, and Black's queen took mate in two\" beats \"+3.8 → −8.1, line: Nxd5 Qxe1+ Kh2 Qe5+ g3 Qxd5\" every time."
    - title: "Patterns added to your skill buckets"
      detail: "Each detected mistake updates a counter for its skill dimension. After three games where you skipped a prophylactic move, the Defense bucket gets a flag; after two missed fork shapes, the Tactics bucket does. The buckets are visible, so you can see which patterns are piling up."
    - title: "Spaced-repetition training queue generated"
      detail: "Each training session pulls from the flagged buckets on a spaced-repetition schedule: positions seen most recently come back sooner, and positions you've solved correctly twice in a row drop out. Sessions take 5 to 10 minutes. The Free tier allows three sessions per week; Premium is unlimited."
    - title: "Skill graphs update"
      detail: "After each session the five skill trend graphs update. Premium adds 90 / 180 / 365-day views, so you can check whether the last three weeks of training actually moved (say) your endgame technique, or whether you've plateaued and need to try something else."

# Example "mistake explained" gallery: the page's strongest USP, shown
# rather than described. Anchored to /apps/chessful/#templates.
example_insights:
  anchor: "templates"
  overline: "What Chessful explains"
  heading: "What a plain-language mistake looks like in Chessful."
  intro: "Six worked examples of Chessful turning a Stockfish evaluation into something a club player can use. Each is the kind of mistake the adaptive trainer then drills in tomorrow's session."
  cards:
    - tag: "Tactics · Hung piece"
      headline: "You played Nxd5. The knight was your only back-rank defender."
      body: "After Nxd5, Black plays Qxe1+, because the knight you just captured with was your only defender of the e1 square. Mate in 2. The right move was Bf4, keeping the knight on c3 where it stops the queen's path. Pattern: defender-removal blindness."
    - tag: "Tactics · Missed fork"
      headline: "You played Bd3. Black had a fork on c2."
      body: "Black's knight on b4 was one move from c2, forking your queen and rook. After Bd3, you walked into it: Nxc2+ wins the exchange. The right move was Qd2, defending c2 with the queen. Pattern: enemy-piece radius blindness."
    - tag: "Defense · Weak king"
      headline: "You castled into a half-open f-file with no defenders."
      body: "Castling short looked safe, but Black had a rook on f8 and the f-pawn was missing. Three moves later, Rxf2 cracked the position open. The right plan was to develop the knight to g3 first, blocking the f-file before castling. Pattern: structural-prerequisite skip."
    - tag: "Openings · Repertoire lapse"
      headline: "Move 7 deviated from your usual French setup."
      body: "You've played the French Defense Winawer 23 times in your games. Move 7 here was Nf6 instead of the usual Qa5+. The deviation lost a tempo and let White's bishop reach an active square. Pattern: repertoire drift. Chessful flags this for opening drill."
    - tag: "Endgame · Technique error"
      headline: "King and pawn endgame: you took the opposition the wrong way."
      body: "With pawns on e5 vs e6, you played Kd4 and lost the opposition. The right move was Kf4, taking the opposition and forcing Black's king to retreat. The pawn promotes in 7 moves. Pattern: opposition direction error. Chessful queues opposition-pattern training."
    - tag: "Tactics · Back-rank mate"
      headline: "You played h3 to give the king luft. It was three moves too late."
      body: "Black's rook had already swung to d8 and the queen was on e7, so back-rank mate was already threatened. h3 was correct prophylaxis, but the right time to play it was move 18, not move 24. Pattern: prophylactic-timing miss. Chessful drills the recognition pattern."

# Side-by-side comparison: replaces the templated alternatives card grid
# with substantive feature deltas. Auto-triggers the mid-page CTA.
comparison_table:
  intro: "Each row is a question a serious chess player asks before installing a training or analysis app. Chess.com is the dominant online platform, Lichess the free open-source alternative, Magnus Trainer the celebrity-coached training app (now owned by Chess.com), and Chessis the closest on-device, analysis-focused peer. Checked against each app's public landing page and App Store listing on 2026-05-13."
  competitors: ["Chessful", "Chess.com", "Lichess", "Magnus Trainer", "Chessis"]
  rows:
    - feature: "Fully offline (no internet required)"
      values: ["Yes, Stockfish runs on-device", "No, cloud analysis", "Mostly cloud", "No, cloud", "Yes, Stockfish on-device"]
    - feature: "Account required"
      values: ["No account ever", "Required", "Optional but expected", "Required (Chess.com)", "No account"]
    - feature: "Daily analysis quota"
      values: ["Unlimited (Premium); unlimited basic analysis on Free", "1 game review/day on Free; unlimited on paid", "Unlimited (free)", "Lessons-based, not analysis-based", "Unlimited (Pro)"]
    - feature: "Plain-language mistake explanations"
      values: ["Yes, motif detectors + on-device LM", "Centipawn lines + Game Review (paid)", "Centipawn lines + community annotations", "Lessons rather than per-game review", "Yes, game-report sentences"]
    - feature: "Adaptive training built from your games"
      values: ["Yes, spaced repetition on detected motifs", "Lessons + puzzles, not derived from your games", "Puzzle Storm + study tool, not adaptive", "Curated lessons, not drawn from your games", "Mistakes report, no training queue"]
    - feature: "Number of AI opponents"
      values: ["40, distinct styles", "1 engine + bots library", "1 engine + bots", "Magnus + ~12 personality bots", "Not focused on play"]
    - feature: "Live human matchmaking"
      values: ["No (intentional)", "Yes, global", "Yes, global and free", "No", "No"]
    - feature: "Lifetime / one-time pricing"
      values: ["{P_LIFETIME} lifetime", "Subscription only ($9.99 to $14/mo)", "Free / donation", "$299.99 lifetime (else subscription)", "One-time Pro purchase"]
    - feature: "Privacy: no tracking, no third-party SDKs"
      values: ["Zero tracking SDKs, App Privacy: nothing collected", "Standard analytics + ads SDKs", "No ads, minimal analytics", "Standard Chess.com analytics", "Minimal, no ads on Pro"]
    - feature: "Platforms"
      values: ["iPhone + iPad + Mac (Universal Purchase)", "Web + iPhone + iPad + Mac + Android", "Web + iPhone + iPad + Android", "iPhone + iPad + Mac + Vision", "Android primary; iOS limited"]
  footnote: "Competitor positioning summarised from each app's public landing page and App Store listing on 2026-05-13. Pricing and features change often, so check before switching."

screenshots:
  - src: "/assets/screenshots/chessful/1.png"
    alt: "Chessful game review on iPhone with an accuracy score and key moments"
  - src: "/assets/screenshots/chessful/2.png"
    alt: "Chessful mistake detail showing the better move on the board with an explanation"
  - src: "/assets/screenshots/chessful/3.png"
    alt: "Chessful 3D chess board mid-game against an opponent"
  - src: "/assets/screenshots/chessful/4.png"
    alt: "Chessful daily training built from your own games"
  - src: "/assets/screenshots/chessful/5.png"
    alt: "Chessful progress screen with a rating chart and achievements"
  - src: "/assets/screenshots/chessful/6.png"
    alt: "Chessful play screen listing computer opponents by level"
  - src: "/assets/screenshots/chessful/7.png"
    alt: "Chessful dashboard with rating, skills and today training"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no trackers"
    - "No account or sign-up required"
    - "All analysis runs locally on your device: Stockfish, the motif detectors, and the explanation model"
    - "Works fully offline, with no cloud calls and no daily analysis quota"
    - "Universal Purchase across iPhone, iPad, and Mac via standard Apple infrastructure"

faq:
  - q: "What is Chessful?"
    a: "Chessful is a chess training and game analysis app for iPhone, iPad, and Mac. It analyzes your games with Stockfish, explains your mistakes in plain language, and builds adaptive training sessions focused on your real weaknesses across five skill dimensions: tactics, defense, positional play, openings, and endgames."
  - q: "How is Chessful different from Chess.com or Lichess?"
    a: "Chess.com and Lichess are online platforms that run on network effects: millions of opponents, ranked play, a daily analysis quota. Chessful is fully offline, runs on-device, needs no account, and is made for the player who wants a teacher more than a community. Stockfish runs locally on your iPhone, iPad, or Mac, explanations come in plain language instead of centipawn lines, and training is generated from your own losses instead of a generic puzzle library."
  - q: "How is Chessful different from Magnus Trainer?"
    a: "Magnus Trainer is a celebrity-coached lessons app, with content curated by Magnus Carlsen and his team and organised as bite-sized games and theory courses. Chessful has no celebrity content; its training comes from the specific patterns in your own losses. The two complement each other, Magnus Trainer for structured lessons and Chessful for adaptive training on your real weaknesses, and many improving players use both."
  - q: "How is Chessful different from Chessis?"
    a: "Chessis is the closest direct peer: both have Stockfish, on-device analysis, plain-language explanations, and a one-time purchase option. Chessful adds the adaptive training queue (spaced repetition on motifs from your games), 40 distinct AI opponents to play against, and Universal Purchase across iPhone, iPad, and Mac. Chessis is currently Android-primary, with one-time Pro pricing and a tight focus on the analysis flow."
  - q: "Is Chessful good for beginners?"
    a: "Chessful suits players who know the rules and have played at least a few full games. If you're an absolute beginner learning how the pieces move, start with a teaching app, because Chessful's training assumes you can read a position. It is aimed at players rated around 800 to 1800 who are stuck on a plateau and don't understand why."
  - q: "Does Chessful work offline?"
    a: "Yes. Every part of Chessful runs entirely on your device: Stockfish analysis, motif detection, plain-language explanations, adaptive training, and the 40 AI opponents. It never needs an internet connection, so you can play and analyse on a flight, in a kitchen, or on the subway."
  - q: "What chess engine does Chessful use?"
    a: "Chessful uses Stockfish, the open-source engine behind Chess.com's analysis and Lichess's evaluation. It runs locally on your iPhone, iPad, or Mac at a depth tuned to the device. Chessful then turns Stockfish's centipawn output into plain-language sentences using motif detectors and a small on-device language model."
  - q: "Is Chessful free? What does Premium cost?"
    a: "Chessful is free to try with the 40 AI opponents, basic analysis of every game, three training sessions per week, and basic skill tracking, with no ads and no account. Premium unlocks unlimited deep game analysis, unlimited adaptive training, the full progress dashboard with 90/180/365-day skill-trend graphs, and alternative-move exploration. Premium is {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once for lifetime access, with a 7-day free trial. Lifetime supports Family Sharing, so one purchase covers up to 5 family members at no extra cost. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does Chessful track my improvement?"
    a: "Yes. Chessful tracks five skill areas (tactics, defense, positional play, openings, and endgames) and shows how each changes over time. The Free tier shows basic counts; Premium adds 90 / 180 / 365-day trend graphs so you can see whether the last three weeks of training actually moved (say) your endgame technique."
  - q: "Does Chessful need an account?"
    a: "No. Chessful needs no account, no sign-up, and no personal information. Your games, analysis, and training progress stay on your device. Universal Purchase status syncs through standard iCloud Keychain, which is Apple's mechanism and not a Chessful account."
  - q: "Can I import games from Chess.com or Lichess?"
    a: "No. Chessful doesn't import games from Chess.com or Lichess, or PGN files. It analyses the games you play in the app against its 40 AI opponents and builds your training queue from those."
  - q: "Does Chessful have a tactics-puzzle trainer like Chess.com?"
    a: "Chessful's training queue comes from the mistake patterns in your own games, not from a generic puzzle pool, on the view that adaptive training on your real weaknesses works better than puzzle-rush. There is no standalone puzzle mode."
  - q: "Does Chessful work on Apple Watch?"
    a: "No. Chessful has no Apple Watch app. It runs on iPhone, iPad, and Mac, with one Universal Purchase covering all three."
  - q: "Is Chessful a replacement for Chess.com or Lichess?"
    a: "No. Chessful has no ranked play, live human matchmaking, or leaderboards. It is for the player who wants to improve against varied AI opponents with readable explanations, without an account or a daily quota. For ranked human play, Chess.com and Lichess remain the right tools, and many improving players use Chessful for analysis and training alongside one of them for matchmaking."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/chessful/support/"

release:
  first_release: "2026-04-01"
  last_updated: "2026-05-13"

ratings:
  value: "4.2"
  count: 16
  last_synced: "2026-10-28"

related_journal:
  slug: forty-chess-opponents
  anchor: "Forty chess opponents, and why no two of them are the same engine"

# Render the markdown body as a visible "About Chessful." section with
# contextual in-body internal links to the methodology, templates,
# comparison, and privacy sections. SearchPilot: in-body contextual
# links return 5 to 25% organic uplift.
show_body: true
about_heading: "What Chessful does: chess training, analysis, and 40 opponents"
related_apps: ["shogiful", "xiangqiful"]
last_updated: 2026-10-26
---
Chessful is a [chess training & analysis app for iPhone, iPad, and Mac](#features), built on the observation that Stockfish's centipawn numbers don't help most players improve. The app reviews every move you make, then turns the engine's output into plain English: which piece you hung, which fork you missed, which prophylactic move would have saved the position. From there, [Chessful builds an adaptive training queue](#how-it-works) aimed at the patterns where you actually lose (tactics, defense, positional play, openings, endgames), using spaced repetition and forty AI opponents tuned to specific playing styles.

The engine is not what separates Chessful from Chess.com, Lichess, and Magnus Trainer, since they all run Stockfish or a derivative. The difference is the [layer on top of the engine](#how-it-works): motif detectors that sort each significant mistake into one of about thirty categories (hung piece, missed fork, weak back rank, prophylactic skip, repertoire lapse, endgame technique error), and a small on-device language model that expands each one into one or two sentences you can read. The [example explanations](#templates) show what this looks like in practice.

Every part of Chessful runs on your device: Stockfish, the motif detectors, the explanation model, and the forty AI opponents. There is no cloud, no rate-limited daily analysis quota, no account to make, and no daily ranking attached to your name. The trade-off is that Chessful has no ranked play or live human matchmaking; for those, Chess.com and Lichess remain the right tools. Chessful is for the player who wants a teacher more than a community. The [side-by-side comparison](#compare-heading-chessful) lists the full feature differences against Chess.com, Lichess, Magnus Trainer, and Chessis. For the whole category in one place (which app fits playing, learning openings, or understanding your losses), see our [honest guide to the best chess apps for iPhone](/guides/best-chess-apps-iphone/).

The forty AI opponents took a disproportionate share of the engineering work and have their own [forty-opponents journal post](/journal/forty-chess-opponents/). Each opponent has its own opening repertoire, structural preference, and blind spots, so games feel like playing different people instead of one engine at forty noise settings. The [adaptive training methodology](/journal/how-chessful-builds-adaptive-training/) is covered in a separate post.

Free users get 40 AI opponents, Stockfish analysis on every game, plain-language mistake summaries, three training sessions per week, and basic skill tracking. Premium adds unlimited deep analysis, unlimited adaptive training, full progress tracking with 90/180/365-day trend graphs, and alternative-move exploration, for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once for [lifetime](/apps/chessful/#pricing), with a 7-day free trial. [No tracking, no ads, no account](/apps/chessful/privacy/), as the App Store privacy nutrition label confirms. The same play, analyze, and train loop exists for two other chess games: [Shogiful](/apps/shogiful/) for shogi (Japanese chess) and [Xiangqiful](/apps/xiangqiful/) for xiangqi (Chinese chess). Published by Lagerland Apps, an independent Apple developer in Finland.
