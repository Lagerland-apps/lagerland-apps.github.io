---
layout: app
slug: chessful
name: "Chessful"
tagline: "Chess that explains your mistakes, then trains you on them."
quick_answer: "Chessful is a chess training and game analysis app for iPhone, iPad, and Mac: Stockfish checks every move of your games on the device, each mistake is explained in plain language at your level, and your mistakes become the puzzles in your daily training. It suits beginners and improving players alike, with 156 free lessons, 15,000 puzzles in 53 themes, 96 endgames, 40 opponents from 400 to 2400 Elo, and PGN import for your Chess.com or Lichess games. It is free with daily limits (2 analyses, 3 puzzles, and 2 coach hints a day); Premium is {P_MONTHLY}/month or {P_YEARLY}/year, each with a {TRIAL}, or {P_LIFETIME} once. There is no account, and the app has no ads, analytics, or tracking."
category: games
status: live

app_store_url: "https://apps.apple.com/app/id6761336870"

price:
  model: freemium

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew. Monthly, Annual, and Lifetime all support Family Sharing. Universal Purchase across iPhone, iPad, and Mac."

plans:
  - name: "Free"
    price: "$0"
    summary: "All 156 lessons, every mistake explained, and a daily allowance of the rest."
    features:
      - "All 156 lessons, from the board to strategy"
      - "2 game analyses, 3 puzzles, and 2 coach hints a day"
      - "Every mistake explained, with review of past mistakes that doesn't use up your puzzles"
      - "The first 10 opponents (400 to 700 Elo)"
      - "PGN import of your Chess.com or Lichess games"
      - "The first endgame in each of the 7 categories"
      - "Estimated rating, skill bars, rating graph, and 59 achievements"
  - name: "Premium · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Premium, billed monthly. Cancel anytime."
    features:
      - "Unlimited game analysis, puzzles, and coach hints"
      - "All 40 opponents, up to 2400 Elo"
      - "All 96 endgame positions"
      - "Your full opening repertoire with engine correction, plus line drills"
      - "Weekly Comparison and Weakness Trends"
      - "{TRIAL} · cancel anytime"
  - name: "Premium · Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same Premium features, billed once a year. ~{SAVE_YEARLY}% cheaper than paying monthly."
    features:
      - "Everything in Premium · Monthly"
      - "~{SAVE_YEARLY}% cheaper than monthly over a year"
      - "{TRIAL} · cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All Premium features for one payment."
    features:
      - "Everything in Premium · Annual"
      - "One-time purchase, no renewal"
      - "Universal Purchase across iPhone, iPad, and Mac"
      - "Restores on every device signed in with the same Apple Account"
      - "Family Sharing included"

icon: "/assets/icons/chessful.png"
og_image: "/assets/og/chessful.png"

seo:
  title: "Chess Training & Analysis App for iPhone & Mac | Chessful"
  description: "Chess app that explains every mistake in your games, then trains you on them. On-device Stockfish, 156 lessons, 15,000 puzzles. iPhone, iPad, Mac."
  keywords:
    - chess training app
    - chess training app iphone
    - chess training app ipad
    - chess training app mac
    - chess game analysis
    - chess game analysis app
    - chess improvement app
    - chess mistakes explained
    - chess coach app
    - chess puzzles app
    - chess puzzles offline
    - chess lessons app
    - learn chess app
    - chess endgame trainer
    - chess opening repertoire app
    - import pgn iphone
    - analyze lichess games iphone
    - offline chess app
    - Stockfish iPhone
    - chess app no ads

hero:
  pre_headline: "Chess training and game analysis for iPhone, iPad, and Mac"
  headline: "Find out why you lost, then train on those exact mistakes."
  secondary: "Stockfish checks every move on your device. Each mistake shows what you played, what was best, and why, in words pitched at your level."
  subheadline: "Your mistakes become the puzzles in your daily training, and spaced review brings back the ones you miss. Around that sit 156 free lessons, 15,000 puzzles, 96 endgames, and 40 opponents from 400 to 2400 Elo. Bring in your Chess.com or Lichess games as PGN files."
  cta_label: "Download Free"
  alt: "Chessful game review on iPhone with an accuracy score and the key moments of the game"

who_for:
  - "You keep losing the same way and can't see why"
  - "You want each mistake explained in a sentence you can follow"
  - "You have games on Chess.com or Lichess and want them reviewed from a PGN export"
  - "You're new to chess and want lessons that start with the board itself"
  - "You want puzzles aimed at the mistakes you actually make"
  - "You study on iPhone, iPad, and Mac, and want one purchase to cover all three"

who_not_for:
  - "You mainly want live games against people, with matchmaking and clocks"
  - "You want tournaments, chat, or a community"
  - "You need your games to sync between devices (each device keeps its own data)"
  - "You play on an Intel Mac or Apple Vision Pro"
  - "You want a celebrity-coached course (Magnus Trainer is built around that; Chessful is not)"

# Organization-type founder block: attributes to the studio rather than a
# named person. Same pattern as allpaid.md.
founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "For players who want their mistakes explained in words."
  story: "An engine can tell you a move was bad. The evaluation and the line of moves it prints rarely tell you why, and reading them is a skill of its own. Chessful puts a plain sentence next to each mistake, worded for the level you choose, and builds your training from the mistakes you actually make. Stockfish is compiled into the app, so your games are analysed on your iPhone, iPad, or Mac. The app makes no network calls of its own; only purchases and the optional Game Center sign-in talk to Apple's servers."
  signals:
    - "Stockfish runs inside the app, so analysis happens on your device and needs no account"
    - "Forty named opponents in eight tiers, each with a play style, strengths, and weaknesses (design notes in the [forty-opponents journal post](/journal/forty-chess-opponents/))"
    - "The privacy manifest declares no tracking, no tracking domains, and no collected data types"
    - "{APP_COUNT} live apps in the Lagerland catalogue, all built without tracking, ads, or required accounts"
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
  - title: "Know why you lost"
    description: "After a game, Stockfish checks every move on your device and rates each one from Brilliant to Blunder. Each mistake shows what you played, what was best, why the better move works, and the line that punishes yours."
  - title: "Train on your own mistakes"
    description: "Today's Training turns the mistakes from your analysed games into a 5, 10, or 15 minute session. Review past mistakes uses spaced repetition to bring misses back until you stop making them."
  - title: "Start from the first move"
    description: "All 156 lessons are free, from the board itself to strategy. Explanations match the level you pick, from just learning the rules to rated 1400+."
  - title: "Your games stay on your device"
    description: "There is no account to create. The app has no ads, analytics, or tracking. Playing, analysis, lessons, and puzzles all work offline."

features:
  - title: "Game Review with on-device Stockfish"
    description: "Stockfish checks every move of a game and gives you an accuracy score, the key moments, and a rating for each move from Brilliant to Blunder. Step through the engine's best line move by move. Free players get 2 analyses a day; Premium is unlimited."
  - title: "Every mistake explained"
    description: "Each mistake card shows what you played, what was best, how much the evaluation dropped, and a plain-language explanation of why. It also plays out the line that punishes your move. Mistakes are sorted into 10 types, such as Hanging Piece, Missed Fork, Missed Pin, and Endgame Error, and Train This Pattern takes you straight to practice."
  - title: "Import your Chess.com and Lichess games"
    description: "Export a PGN file from either site and open it in Chessful, or paste the PGN text. One import takes up to 500 games, flags duplicates, and lets you choose which side you played. There is no account to connect; the file is all Chessful needs."
  - title: "Daily training from your mistakes"
    description: "Today's Training picks a focus area (Tactics, Defense, Positioning, Endgame, or Openings) and builds a session of 3, 5, or 8 puzzles from your own games. Miss one and you play the right move yourself; score under 70% and it offers to re-drill the misses."
  - title: "15,000 puzzles in 53 themes"
    description: "A tactics library drawn from the Lichess open puzzle database, from forks and pins to named checkmate patterns. Every puzzle was checked with an engine, the difficulty adapts to your puzzle rating, and it all works offline."
  - title: "96 endgames against full-strength Stockfish"
    description: "Play out Lucena, Philidor, Vančura, and more across 7 categories, from basic mates to classic studies. The first position in each category is free; Premium opens all 96."
  - title: "40 opponents from 400 to 2400 Elo"
    description: "Climb a ladder of named opponents in 8 tiers, from Pebble to The Grandmaster, each with a play style, strengths, and weaknesses. Play on a 2D board or a 3D wood board. Stuck mid-game on the 2D board? Ask the Coach for the best move or the evaluation of every legal move."
  - title: "Your opening repertoire"
    description: "Chessful reads your analysed games and shows the openings you play most, how you score in each, and where you leave the book. Premium adds the full move tree, engine corrections, and drills for the lines you keep getting wrong."
  - title: "Progress you can read"
    description: "Track an estimated rating, five skill bars, a rating graph, and 59 achievements, with optional Game Center leaderboards. Premium adds Weekly Comparison and Weakness Trends. The rating is Chessful's own estimate, separate from FIDE, Chess.com, or Lichess ratings."
  - title: "iPhone, iPad, and Mac"
    description: "One Universal Purchase covers all three. On a Mac with Apple silicon you get menu commands and keyboard shortcuts for new games, moves, and copying FEN or PGN. Your games stay on the device you played them on."

# Methodology disclosure: the highest-leverage E-E-A-T artefact for a
# product page in a category where most competitors hide their algorithm.
# Emits HowTo schema automatically via _layouts/app.html.
how_it_works:
  intro: "This is what happens between the end of a game and your next training session."
  steps:
    - title: "Play a game or import one"
      detail: "Play one of the 40 opponents in the app, or import your Chess.com or Lichess games from a PGN file. Imported games can be edited or deleted later."
    - title: "Stockfish checks every move"
      detail: "Stockfish runs on your iPhone, iPad, or Mac and evaluates every move of the game. You see your accuracy, the key moments, and a rating for each move from Brilliant to Blunder."
    - title: "Each mistake is explained"
      detail: "For every mistake you get what you played, what was best, the size of the evaluation drop, a plain-language explanation worded for your coaching level, and the line that punishes your move. Each one is tagged with one of 10 mistake types."
    - title: "Your mistakes become today's training"
      detail: "Today's Training builds a session from the mistakes in your analysed games, aimed at one focus area. Choose 5, 10, or 15 minutes. Free players get 3 puzzles a day; Premium is unlimited."
    - title: "Spaced review brings misses back"
      detail: "Review past mistakes schedules the puzzles you got wrong with spaced repetition, so they come back until you solve them. These reviews don't count against the free daily puzzles."
    - title: "Progress shows what changed"
      detail: "Your estimated rating and the five skill bars (Tactics, Defense, Positioning, Endgame, and Openings) update as you play, analyse, and train. Premium adds Weekly Comparison and Weakness Trends."

# Example mistake cards: the page's strongest USP, shown rather than
# described. Anchored to /apps/chessful/#templates.
example_insights:
  anchor: "templates"
  overline: "What Chessful explains"
  heading: "What a mistake card in Chessful looks like."
  intro: "Six illustrations written for this page to show the format of a mistake card. Your own games produce your own cards, worded for the coaching level you choose, and each card can send you to practice on the same pattern."
  cards:
    - tag: "Hanging Piece · Blunder"
      headline: "You played Qxa7. Best was Be3."
      body: "Taking the pawn pulled your queen off d4, and the knight on c3 lost its only defender. The card shows how far the evaluation dropped, explains in a sentence why the knight was loose, and plays out the line that wins it."
    - tag: "Missed Fork · Mistake"
      headline: "You played h3. Best was Nd5."
      body: "From d5 your knight would have attacked the queen on c7 and the rook on e7 at once. The card names the fork, explains why Nd5 works, and Train This Pattern opens practice on forks."
    - tag: "Missed Pin · Mistake"
      headline: "You played Be2. Best was Bb5."
      body: "From b5 your bishop would have pinned the knight on c6 to the king on e8. The card shows the pin on the board, explains why the knight could no longer move, and plays out the line that wins material."
    - tag: "Poor King Safety · Mistake"
      headline: "You played g4. Best was Nf3."
      body: "Pushing the pawn in front of your castled king opened a path to it. The explanation says what the move weakened, and the refutation shows how Black's pieces get in."
    - tag: "Endgame Error · Mistake"
      headline: "You played Kd3. Best was Kf4."
      body: "In this king and pawn ending, Kd3 handed Black the opposition and the pawn could no longer promote. The card explains the idea in a sentence and shows the winning line with Kf4."
    - tag: "Opening Inaccuracy · Inaccuracy"
      headline: "You played Bd3. Best was Nf3."
      body: "A move-order slip in the opening. The card says which piece belonged on its square first and why, and the same game feeds your Opening Repertoire, which shows where you left the book."

# Side-by-side comparison: replaces the templated alternatives card grid
# with substantive feature deltas. Auto-triggers the mid-page CTA.
comparison_table:
  intro: "Each row is a question players ask before installing a chess training or analysis app. Chess.com is the largest online platform, Lichess the free open-source alternative, Magnus Trainer the celebrity-coached training app (now owned by Chess.com), and Chessis the closest on-device, analysis-focused peer. Competitor columns were checked against each app's public landing page and App Store listing on 2026-05-13."
  competitors: ["Chessful", "Chess.com", "Lichess", "Magnus Trainer", "Chessis"]
  rows:
    - feature: "Analysis works offline"
      values: ["Yes, Stockfish runs on-device", "No, cloud analysis", "Mostly cloud", "No, cloud", "Yes, Stockfish on-device"]
    - feature: "Account required"
      values: ["No account", "Required", "Optional but expected", "Required (Chess.com)", "No account"]
    - feature: "Daily analysis quota"
      values: ["Free: 2 games a day; Premium: unlimited", "1 game review/day on Free; unlimited on paid", "Unlimited (free)", "Lessons-based, not analysis-based", "Unlimited (Pro)"]
    - feature: "Plain-language mistake explanations"
      values: ["Yes, for every mistake, at your level", "Centipawn lines + Game Review (paid)", "Centipawn lines + community annotations", "Lessons rather than per-game review", "Yes, game-report sentences"]
    - feature: "Training built from your games"
      values: ["Yes, daily sessions + spaced review of misses", "Lessons + puzzles, not derived from your games", "Puzzle Storm + study tool, not adaptive", "Curated lessons, not drawn from your games", "Mistakes report, no training queue"]
    - feature: "Number of AI opponents"
      values: ["40, from 400 to 2400 Elo", "1 engine + bots library", "1 engine + bots", "Magnus + ~12 personality bots", "Not focused on play"]
    - feature: "Live human matchmaking"
      values: ["No", "Yes, global", "Yes, global and free", "No", "No"]
    - feature: "Lifetime / one-time pricing"
      values: ["{P_LIFETIME} lifetime", "Subscription only", "Free / donation", "Lifetime option, otherwise subscription", "One-time Pro purchase"]
    - feature: "Privacy: no tracking, no third-party SDKs"
      values: ["No ads, analytics, tracking, or third-party SDKs", "Standard analytics + ads SDKs", "No ads, minimal analytics", "Standard Chess.com analytics", "Minimal, no ads on Pro"]
    - feature: "Platforms"
      values: ["iPhone + iPad + Mac (Universal Purchase)", "Web + iPhone + iPad + Mac + Android", "Web + iPhone + iPad + Android", "iPhone + iPad + Mac + Vision", "Android primary; iOS limited"]
  footnote: "Competitor positioning summarised from each app's public landing page and App Store listing on 2026-05-13. Pricing and features change often, so check before switching."

screenshots:
  - src: "/assets/screenshots/chessful/1.webp"
    alt: "Chessful game review on iPhone with an accuracy score and key moments"
  - src: "/assets/screenshots/chessful/2.webp"
    alt: "Chessful mistake detail showing the better move on the board with an explanation"
  - src: "/assets/screenshots/chessful/3.webp"
    alt: "Chessful 3D chess board mid-game against an opponent"
  - src: "/assets/screenshots/chessful/4.webp"
    alt: "Chessful daily training built from your own games"
  - src: "/assets/screenshots/chessful/5.webp"
    alt: "Chessful progress screen with a rating chart and achievements"
  - src: "/assets/screenshots/chessful/6.webp"
    alt: "Chessful play screen listing computer opponents by level"
  - src: "/assets/screenshots/chessful/7.webp"
    alt: "Chessful dashboard with rating, skills, and today's training"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No account or sign-up"
    - "No ads, analytics, tracking, or third-party SDKs"
    - "Stockfish runs on your device, and your games, mistakes, and training history stay there"
    - "Playing, analysis, lessons, and puzzles work offline; purchases and the optional Game Center sign-in use Apple's servers"
    - "Settings → Reset Everything erases all Chessful data on the device"

faq:
  - q: "What is Chessful?"
    a: "Chessful is a chess training and game analysis app for iPhone, iPad, and Mac. Stockfish checks every move of your games on the device, each mistake is explained in plain language at your level, and your mistakes become the puzzles in your daily training. It also includes 156 lessons, 15,000 puzzles in 53 themes, 96 endgames to play out, an opening repertoire built from your games, and 40 opponents from 400 to 2400 Elo."
  - q: "Can I import my games from Chess.com or Lichess?"
    a: "Yes, as PGN files. Export your games from Chess.com or Lichess, then open the file in Chessful from Files, iCloud Drive, or AirDrop, or paste the PGN text. One import takes up to 500 games, flags duplicates, and lets you pick which side you played. Chessful doesn't connect to either site or fetch games by username. Importing is unlimited; analysing imported games counts toward the free 2 analyses a day."
  - q: "Is Chessful good for beginners?"
    a: "Yes. The Learn tab has 156 free lessons in seven sections, starting with the board itself and the way the pieces move, then checkmates, tactics, openings, endgames, thinking, and strategy. Set your coaching level to \"Just learning the rules\" and the mistake explanations are worded for that level. Players who already know the rules can go straight to playing and analysing games."
  - q: "Does Chessful have chess puzzles?"
    a: "Yes, two kinds. The tactics library has 15,000 puzzles in 53 themes, from forks and pins to named checkmate patterns, drawn from the Lichess open puzzle database and checked with an engine. Today's Training adds puzzles built from the mistakes in your own games. Free players get 3 puzzles a day across both; reviewing past mistakes doesn't count toward that. Premium is unlimited."
  - q: "How is Chessful different from Chess.com or Lichess?"
    a: "Chess.com and Lichess are online platforms built around playing other people. Chessful is a training app: you play its 40 built-in opponents or import your games from either site as PGN, Stockfish analyses them on your device, every mistake is explained in words, and your training is built from those mistakes. There is no account. Chessful has no online play, so you can keep your Chess.com or Lichess account for games against people and use Chessful to review those games."
  - q: "How is Chessful different from Magnus Trainer?"
    a: "Magnus Trainer teaches through courses and games built around Magnus Carlsen. Chessful has no celebrity content. It analyses your own games, explains each mistake, and builds your training from them, alongside 156 lessons, 15,000 puzzles, and 96 endgames."
  - q: "How is Chessful different from Chessis?"
    a: "Both analyse games with Stockfish on the device and explain mistakes in sentences. Chessful adds the training around the analysis: daily sessions built from your mistakes, spaced review of misses, 156 lessons, 15,000 puzzles, 96 endgames, and 40 opponents to play, with one Universal Purchase across iPhone, iPad, and Mac."
  - q: "Does Chessful work offline?"
    a: "Yes, for everything you do with chess. Playing, Stockfish analysis, lessons, the puzzle library, endgames, and openings all run on bundled content and a bundled engine. Buying or restoring Premium, loading prices, and Game Center need a connection."
  - q: "What chess engine does Chessful use?"
    a: "Stockfish, with NNUE, compiled into the app. It runs on your iPhone, iPad, or Mac. Game Review evaluates every move of your game, and the endgame trainer uses Stockfish at full strength as your opponent. Chessful then explains each mistake in plain language."
  - q: "Is Chessful free? What does Premium cost?"
    a: "Chessful is free to download with daily limits: 2 game analyses, 3 puzzles, and 2 coach hints a day, the first 10 opponents, and the first endgame in each category. All 156 lessons, every mistake explanation, PGN import, and progress tracking are free. Premium removes the daily limits and unlocks all 40 opponents, all 96 endgames, the full opening repertoire with line drills, and Weekly Comparison and Weakness Trends. It costs {P_MONTHLY}/month or {P_YEARLY}/year, each with a {TRIAL}, or {P_LIFETIME} once for lifetime access. Family Sharing is included. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does Chessful track my improvement?"
    a: "Yes. Progress shows an estimated rating, a rating graph, game stats, five skill bars (Tactics, Defense, Positioning, Endgame, and Openings), an activity view, and 59 achievements, all free. Premium adds Weekly Comparison and Weakness Trends. The rating is Chessful's own estimate, separate from FIDE, Chess.com, or Lichess ratings."
  - q: "Does Chessful need an account?"
    a: "No. There is no sign-up and no Chessful account. Your games, analysis, and training history are stored on your device. Game Center is optional, and purchases go through your Apple Account."
  - q: "Do my games sync between iPhone, iPad, and Mac?"
    a: "No. Each device keeps its own games and progress, and Chessful has no iCloud sync. Your Premium purchase does carry over: Universal Purchase covers iPhone, iPad, and Mac, and Restore Purchases brings it back on any device signed in with the same Apple Account."
  - q: "Is Chessful a replacement for Chess.com or Lichess?"
    a: "Not for playing people. Chessful has no online play, matchmaking, or clocks; every game is against its built-in opponents. It is for reviewing and training: import your Chess.com or Lichess games as PGN, see each mistake explained, and practise on them."
  - q: "Does Chessful work on Apple Watch or Apple Vision Pro?"
    a: "No. Chessful runs on iPhone, iPad, and Mac (Apple silicon only, not Intel Macs), with one Universal Purchase covering all three."
  - q: "What languages is Chessful available in?"
    a: "Chessful ships in 32 languages (38 locales counting regional variants such as UK English, Mexican Spanish, and Brazilian Portuguese), lessons included. Pick the language for Chessful in iOS Settings, or in System Settings on a Mac."

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
# comparison, and privacy sections.
show_body: true
about_heading: "What Chessful does: chess analysis, training, and lessons"
related_apps: ["shogiful", "xiangqiful"]
last_updated: 2026-10-29
---
Chessful is a [chess training and analysis app for iPhone, iPad, and Mac](#features) for players who keep losing the same way and can't see why. When a game ends, Stockfish checks every move on your device. Each mistake gets a card with what you played, what was best, a short explanation worded for your level, and the line that punishes your move. Those mistakes then become the puzzles in [your daily training](#how-it-works), and spaced review brings back the ones you miss until you solve them.

An engine evaluation on its own is a number and a line of moves. Chessful adds the sentence that explains it and sorts each mistake into one of ten types, from Hanging Piece and Missed Fork to Endgame Error and Opening Inaccuracy, so your training aims at the types you repeat. The [example mistake cards](#templates) show the format.

You can play your games in the app against 40 opponents from 400 to 2400 Elo (the [forty-opponents journal post](/journal/forty-chess-opponents/) covers how the ladder was designed), or import the games you already played on Chess.com or Lichess as PGN files. Around the analysis sit 156 lessons that start with the board itself, 15,000 puzzles in 53 themes, 96 endgames to play out against full-strength Stockfish, and an opening repertoire built from your own games. For the whole category in one place, see our [guide to the best chess apps for iPhone](/guides/best-chess-apps-iphone/), and the [side-by-side comparison](#compare-heading-chessful) with Chess.com, Lichess, Magnus Trainer, and Chessis.

Chessful has no online play, and your games stay on the device you played them on. The free version includes every lesson and every explanation, with 2 analyses, 3 puzzles, and 2 coach hints a day. Premium removes those limits and opens all 40 opponents, all 96 endgames, and the full repertoire, for {P_MONTHLY}/month or {P_YEARLY}/year with a {TRIAL}, or {P_LIFETIME} once for [lifetime](/apps/chessful/#pricing). There is [no account, and the app has no ads, analytics, or tracking](/apps/chessful/privacy/). Lagerland Apps also makes [Shogiful](/apps/shogiful/) for shogi (Japanese chess) and [Xiangqiful](/apps/xiangqiful/) for xiangqi (Chinese chess). Chessful is published by Lagerland Apps, an independent Apple developer in Finland.
