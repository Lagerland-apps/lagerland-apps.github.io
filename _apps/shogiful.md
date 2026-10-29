---
layout: app
slug: shogiful
name: "Shogiful"
tagline: "Play shogi, see why you lost, and train on it."
quick_answer: "Shogiful is a shogi (Japanese chess) app for iPhone, iPad, and Mac where you play, review your games, and train in one place. You can play 40 engine opponents with kanji pieces, kanji with movement arrows, or chess-style pieces with no kanji at all; afterwards YaneuraOu checks every move on your device and explains each mistake, and your training aims at the weaknesses it finds, with 501 tsume problems, 99 drop drills, and 80 lessons. It is free with daily limits (2 analyses, 3 puzzles, and 2 coach hints a day); Premium is {P_MONTHLY}/month or {P_YEARLY}/year, each with a {TRIAL}, or {P_LIFETIME} once. There is no account, and the app has no ads or tracking."
category: games
status: live

app_store_url: "https://apps.apple.com/app/id6761656926"

price:
  model: freemium

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew."

# Free / Premium-Monthly / Premium-Annual / Lifetime: same upgrade-ladder
# presentation as Chessful. Features per tier from the blueprint (section 3).
plans:
  - name: "Free"
    price: "$0"
    summary: "Every opponent, every piece style, and a daily allowance of analysis and training."
    features:
      - "Unlimited games against all 40 opponents, unlocked as you win"
      - "2 game analyses, 3 training puzzles, and 2 coach hints a day"
      - "381 tsume problems, from 1-move to 5-move mates"
      - "31 lessons, including the whole Fundamentals track"
      - "All three piece styles, Western or Japanese notation, and the 3D board"
      - "KIF import and export"
      - "Estimated rating, kyu/dan rank, accuracy trend, and milestones"
  - name: "Premium · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Premium, billed monthly. Cancel anytime."
    features:
      - "Unlimited game analysis, training, and coach hints"
      - "Deep Lines: the engine's top three lines for any position"
      - "All 501 tsume problems, including 7-move and 9-move mates"
      - "Every drill, card, and handicap scenario, and all 80 lessons"
      - "Skill Profile and Weakness Trends"
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
      - "Family Sharing included"

icon: "/assets/icons/shogiful.png"
og_image: "/assets/og/shogiful.png"

seo:
  title: "Shogi Training & Analysis App: iPhone, iPad, Mac | Shogiful"
  description: "Shogi app for iPhone, iPad & Mac. Play without kanji, see each mistake explained by on-device YaneuraOu, and train with 501 tsume problems."
  keywords:
    - shogi app
    - shogi app iphone
    - shogi app english
    - learn shogi app
    - shogi for beginners
    - japanese chess app
    - shogi training app
    - shogi game analysis
    - shogi without kanji
    - western shogi pieces
    - tsume shogi puzzles
    - tsume shogi app
    - shogi puzzles app
    - shogi engine ios
    - YaneuraOu iphone
    - shogi ai opponent
    - play shogi offline
    - shogi app no account
    - shogi app ipad
    - shogi app mac
    - shogi improvement app
    - shogi coach app
    - shogi kif import
    - shogi wars alternative offline
    - learn shogi from chess
    - shogi drops explained

hero:
  pre_headline: "Shogi training and game analysis for iPhone, iPad, and Mac"
  headline: "Play shogi without reading kanji, then see where each game went wrong."
  secondary: "YaneuraOu checks every move on your device. Each mistake shows what you played, what was best, what it cost in pawns, and a coach's tip."
  subheadline: "Your top weakness shapes each day's training. Behind it sit 501 tsume problems, 99 drop drills, 62 castle drills, and 80 lessons. Climb a ladder of 40 opponents, with no account and no connection needed to play."
  cta_label: "Download Free"
  alt: "Shogiful shogi game in progress on a 3D wooden board on iPhone, mid-game against the opponent Kiri"

who_for:
  - "You know chess, got curious about shogi, and the kanji on the pieces stopped you"
  - "You know the rules but keep losing to drops you never saw coming"
  - "You want each mistake explained in a sentence, beyond an engine number"
  - "You want structured practice: tsume, drops, castles, openings, and endgames"
  - "You play on a train or a plane and want an engine that works without a connection"
  - "You want the same app on iPhone, iPad, and Mac"

who_not_for:
  - "You mainly want ranked online games against people (Shogi Wars, 81Dojo, and Lishogi are built for that)"
  - "You want to play with a clock or byoyomi (Shogiful games are untimed)"
  - "You want a board-game collection (Shogiful is shogi only)"
  - "You want social features, tournaments, or community chat"
  - "You're looking for a kifu database of professional games"
  - "You want a light theme (the app is always dark)"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "For the player who can't read the pieces yet."
  story: "Outside Japan, many people who try shogi stop at the pieces. Each one is the same wedge shape, told apart only by its characters. Shogiful lets you choose: traditional kanji, kanji with arrows that show how each piece moves, or chess-style pieces with no kanji. After a game, YaneuraOu checks every move on your device, and each mistake gets a card with what you played, what was best, and a tip. Training then aims at the weaknesses your games show, from drops and castles to tsume. The engine is built into the app, so playing, analysis, and training need no account and no connection."
  signals:
    - "YaneuraOu and its NNUE evaluation file are built into the app, so analysis runs on your device"
    - "Mistake types written for shogi, including Drop Mistake, Promotion Mistake, Castle Weakness, and Missed Tsume"
    - "The privacy manifest declares no tracking, and the app contains no third-party SDKs"
    - "{APP_COUNT} live apps in the Lagerland catalogue, all built without tracking, ads, or required accounts"
  external_link:
    label: "Read the Lagerland studio backstory →"
    href: "/lagerland-apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally, usually within a day."

alternatives_to:
  - "Shogi Wars"
  - "Lishogi"
  - "81Dojo"
  - "ShogiQuest"
  - "Kanazawa Shogi"
  - "PiyoShogi"

value_points:
  - title: "Read the board from your first game"
    description: "Pick Traditional for kanji pieces, International for kanji with movement arrows, or Chess for chess-style pieces with no kanji. Switch any time in Settings. Moves can be shown in Western notation (P-7f) or Japanese notation (▲７六歩)."
  - title: "See where each game turned"
    description: "YaneuraOu labels every move from Best move to Blunder and gives each side an accuracy score. Each mistake shows what you played, what was best, what it cost in pawns, and a coach's tip."
  - title: "Practise the parts of shogi chess never taught you"
    description: "99 drop drills, 62 castle drills across 12 castles, 55 joseki drills, 62 endgame races, and 501 tsume problems. Today's Training builds each session around your level and your top weakness."
  - title: "Your engine travels with you"
    description: "Playing, analysis, and training all work offline, because the engine is part of the app. There is no account to create, and the app has no ads or tracking."

features:
  - title: "Game review with on-device YaneuraOu"
    description: "YaneuraOu evaluates every move of a game and labels each one: Best move, Great move, Good move, Inaccuracy, Mistake, or Blunder. You get an accuracy score for each side, the key moments, and an Insights tab, and the review names which of 12 castles you built. Free players get 2 analyses a day; Premium is unlimited."
  - title: "Every mistake explained"
    description: "Each mistake card shows what you played, what was best, the cost in pawns, and a coach's tip. Mistakes are sorted into 12 types, among them Drop Mistake, Promotion Mistake, Castle Weakness, and Missed Tsume. Each explanation is built from a template written for its mistake type."
  - title: "Daily training aimed at your weaknesses"
    description: "Today's Training picks from a rotating mix of modules, tuned to your level and your top weakness, in sessions from 1 to 12 puzzles. Spaced repetition brings back the puzzles you missed. From any reviewed game, Train These Weaknesses jumps straight to practice on the mistakes you repeat."
  - title: "Tsume Trail: 501 mate problems"
    description: "Five levels of forced-mate problems: 100 one-move, 161 three-move, 120 five-move, 80 seven-move, and 40 nine-move. Any move that really mates counts, even when it differs from the book answer. Every puzzle can tell you why its answer works, and a hint ladder gives you a nudge, then the move, then the reason."
  - title: "Drop Drills and Castle Atelier"
    description: "99 drop drills across 10 motifs, from drop forks and pins to anti-air drops, teach shogi's most surprising weapon. Castle Atelier covers 12 castles, Mino, Yagura, and Anaguma among them, in 62 drills on building, repairing, and breaking through."
  - title: "Joseki, endgames, tesuji, and handicap play"
    description: "Joseki Lab drills 11 opening families in 55 lines. Yose Trainer has 62 endgame races where you decide whether to attack, defend, trade, or hold before you choose the move. Add 30 Tesuji Cards and 40 Komaochi handicap scenarios, from lance odds to eight pieces, started from the Training tab."
  - title: "80 lessons and a starting rank"
    description: "Eight tracks, from Fundamentals to Advanced, with quizzes, demos, and practice puzzles. The whole Fundamentals track is free. A 12-puzzle Skill Assessment places you on a kyu/dan ladder from 15-kyu to 5-dan, an in-app estimate that sets the level of your lessons and daily plan."
  - title: "40 opponents and an in-game coach"
    description: "Climb a ladder of 40 opponents in eight tiers, from Koishi in Novice to Meijin in Master. Beat one twice to unlock the next. Opponents play in seven styles, from castle builders to drop tacticians. On the 2D board, the coach can show the best move on your turn or put an evaluation on every legal square. Live games can also be played on a 3D wooden board."
  - title: "Progress you can read"
    description: "Track an Estimated Rating, your win and loss record, an accuracy trend, and milestones, all free. Premium adds a Skill Profile across Tactics, Defense, Positioning, Endgame, and Openings, plus Weakness Trends that show which mistakes are improving. The rating is a formula from your analysis accuracy, separate from Elo or any official grade."
  - title: "iPhone, iPad, Mac, and KIF files"
    description: "Shogiful runs on iPhone, iPad, and Mac. The Mac app has menus, keyboard shortcuts, and multiple windows. Import KIF games from a file or the clipboard to review them, and export any game as KIF."

# Methodology disclosure: emits HowTo schema via _layouts/app.html.
how_it_works:
  intro: "This is what happens between the end of a game and your next training session."
  steps:
    - title: "Play a game or import one"
      detail: "Play one of the 40 opponents as Sente or Gote, or import a KIF game from a file, the clipboard, or pasted text. Imported games are reviewed like any other game."
    - title: "YaneuraOu checks every move"
      detail: "The engine runs on your iPhone, iPad, or Mac and evaluates every move. You see an accuracy score for each side, a label for every move from Best move to Blunder, the key moments, and the castle you built."
    - title: "Each mistake is explained"
      detail: "For every mistake you get what you played, what was best, the cost in pawns, and a coach's tip. Each one is tagged with one of 12 mistake types written for shogi, such as Drop Mistake or Missed Tsume."
    - title: "Your weaknesses set the training"
      detail: "Train These Weaknesses opens practice on the mistakes you repeat. Today's Training builds a session of 1 to 12 puzzles around your level and your top weakness. Free players get 3 puzzles a day; Premium is unlimited."
    - title: "Spaced repetition brings misses back"
      detail: "Puzzles you miss come back on a spaced-repetition schedule. When you are stuck, the hint ladder gives a nudge, then the move, then the reason, and a puzzle solved with a hint gets a lower repetition grade."
    - title: "Progress shows what changed"
      detail: "Your Estimated Rating, accuracy trend, and milestones update as you play and train. Premium adds the Skill Profile and Weakness Trends, which compare your last five games with the five before."

# Example mistake cards: shows the format instead of describing it.
example_insights:
  anchor: "templates"
  overline: "What Shogiful explains"
  heading: "What a mistake card in Shogiful looks like."
  intro: "Six illustrations written for this page to show the format of a mistake card. Your own games produce your own cards, and Train These Weaknesses sends you to practice on the mistakes you repeat."
  cards:
    - tag: "Drop Mistake · Mistake"
      headline: "You played S*4d. Best was N*3c."
      body: "From 3c the dropped knight would have attacked the king and the rook at once. The card shows both moves on the board, what the silver drop cost in pawns, and a tip on looking for drops that hit two targets."
    - tag: "Castle Weakness · Mistake"
      headline: "You played P-1e. Best was G-5h."
      body: "Pushing the edge pawn beside your Mino castle gave the opponent a target for an edge attack with pawn and lance. The card shows the cost in pawns and a tip on which castle pawns to leave where they stand."
    - tag: "Missed Tsume · Blunder"
      headline: "You played K-3h. Best was G*2b."
      body: "The gold drop started a forced mate, and the defensive king move let the attack fade. The card shows the mating move and a tip to check for mate first when the enemy king is exposed and you hold pieces in hand."
    - tag: "Promotion Mistake · Inaccuracy"
      headline: "You played S-3c+. Best was S-3c=."
      body: "A promoted silver loses its backward diagonals, and this one was needed for defense two moves later. The card shows both options and a tip on when to keep a silver unpromoted."
    - tag: "Hanging Piece · Mistake"
      headline: "You played Px7d. Best was Gx7d."
      body: "Recapturing with the pawn left your gold undefended. A captured gold goes into your opponent's hand and can come back as a drop next to your king. The card shows the cost and a tip on checking what each recapture leaves loose."
    - tag: "Endgame Error · Blunder"
      headline: "You played Bx1a+. Best was N*2e."
      body: "Taking the lance cost the tempo your attack needed, and the opponent's mate landed first. The card shows the faster attacking move and a tip on counting whose mate arrives sooner."

# Side-by-side comparison: auto-triggers the mid-page CTA and the alt-strip.
comparison_table:
  intro: "Each row is a question a shogi-curious player asks before installing an app. Shogi Wars is the dominant online platform (the official Japan Shogi Association app), Lishogi the free open-source web platform, 81Dojo the international online dojo, and ShogiQuest the lightweight quick-play app. All four are built around online play against humans, while Shogiful is a single-player training app. Competitor columns summarised from each app's public listing on 2026-06-11."
  competitors: ["Shogiful", "Shogi Wars", "Lishogi", "81Dojo", "ShogiQuest"]
  rows:
    - feature: "Play and analysis work offline"
      values: ["Yes, YaneuraOu runs on-device", "No, online matchmaking", "No, web platform", "No, online server", "No, online matches"]
    - feature: "Account required"
      values: ["No account", "Yes", "Optional for casual play", "Yes", "Yes (auto-created)"]
    - feature: "Playable without reading kanji"
      values: ["Yes, International (kanji with arrows) and Chess (no kanji) piece styles", "Partial: internationalized UI, kanji-style pieces", "Yes, Western notation and piece options", "Partial: English community, traditional pieces", "Partial: simple UI"]
    - feature: "Engine analysis of your games"
      values: ["Yes, 2 games a day free; unlimited plus Deep Lines on Premium", "Paid AI features (Kishin)", "Yes, server analysis", "Community + engine tools", "Limited"]
    - feature: "Plain-language mistake explanations"
      values: ["Yes, a card per mistake in 12 shogi mistake types", "No, evaluation only", "No, evaluation graph", "No", "No"]
    - feature: "Training aimed at your mistakes"
      values: ["Yes, daily plan tuned to your top weakness, with spaced repetition", "No", "Puzzle library, not drawn from your games", "No", "No"]
    - feature: "Tsume-shogi puzzles"
      values: ["Yes, 501 problems from 1-move to 9-move", "Yes, separate features", "Yes, puzzle section", "Limited", "No"]
    - feature: "Live human matchmaking"
      values: ["No", "Yes, millions of players", "Yes, free", "Yes, international dojo", "Yes, quick matches"]
    - feature: "Lifetime / one-time pricing"
      values: ["{P_LIFETIME} lifetime", "Subscription for unlimited play", "Free / donation", "Free (membership options)", "Free with ads/IAP"]
    - feature: "Privacy: no tracking, no third-party SDKs"
      values: ["No ads, tracking, or third-party SDKs", "Standard mobile analytics", "Open source, minimal", "Standard web analytics", "Standard mobile analytics"]
    - feature: "Platforms"
      values: ["iPhone + iPad + Mac", "iPhone + Android", "Web", "Web + mobile apps", "iPhone + Android + web"]
  footnote: "Competitor positioning summarised from each platform's public landing page and store listing on 2026-06-11. Pricing and features change often, so check before switching. If you want ranked play against humans, those platforms are the right tools; Shogiful is for training between those games."

screenshots:
  - src: "/assets/screenshots/shogiful/1.webp"
    caption: "Play a full game on a 3D wooden board against one of 40 opponents."
  - src: "/assets/screenshots/shogiful/2.webp"
    caption: "Dashboard: rating, streak, today's training, and your last game at a glance."
  - src: "/assets/screenshots/shogiful/3.webp"
    caption: "Mistake detail: what you played, what was best, and a coach's tip."
  - src: "/assets/screenshots/shogiful/4.webp"
    caption: "Game review with accuracy, key moments, and a label for every move."
  - src: "/assets/screenshots/shogiful/5.webp"
    caption: "Daily training built around your top weakness, with a choice of session length."
  - src: "/assets/screenshots/shogiful/6.webp"
    caption: "Progress tracking: estimated rating, accuracy trend, and a per-skill profile."
  - src: "/assets/screenshots/shogiful/7.webp"
    caption: "Play ladder: climb a roster of named opponents, tier by tier."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No account or sign-up"
    - "No ads, tracking, analytics, or third-party SDKs"
    - "YaneuraOu runs on your device, and your games and training history are stored there"
    - "Playing, analysis, and training work offline; purchases and the optional Game Center sign-in use Apple's servers"

faq:
  - q: "What is Shogiful?"
    a: "Shogiful is a shogi training and game analysis app for iPhone, iPad, and Mac. You play 40 engine opponents, YaneuraOu checks every move of your games on the device, and each mistake is explained with what you played, what was best, and a coach's tip. Training then aims at your top weakness, with 501 tsume problems, 99 drop drills, 62 castle drills, 55 joseki drills, 62 endgame races, and 80 lessons."
  - q: "Can I play shogi without knowing kanji?"
    a: "Yes. Shogiful has three piece styles: Traditional (kanji), International (kanji with arrows that show how each piece moves), and Chess (chess-style pieces with no kanji). You can switch between them any time in Settings. Tap a piece and every legal move and drop is highlighted, and moves can be written in Western notation such as P-7f."
  - q: "Is Shogiful good for chess players learning shogi?"
    a: "Yes. Choose the Chess piece style and Western notation, and the board reads much like a chess board. Shogi differs where it matters most: captured pieces come back as drops, promotion is a choice, and endgames are races to mate. Shogiful's mistake types include Drop Mistake, Promotion Mistake, Castle Weakness, and Missed Tsume, and there are 99 drop drills and 62 castle drills to practise them."
  - q: "Is Shogiful good for beginners?"
    a: "Yes. The first launch includes an interactive tutorial on drops, and the full Fundamentals lesson track is free. The opponent ladder starts at Koishi, a gentle beginner, and full shogi rules, including drops, promotion, and repetition, are enforced for you. An optional 12-puzzle Skill Assessment sets the level of your lessons and daily training."
  - q: "How is Shogiful different from Shogi Wars?"
    a: "Shogi Wars is the dominant online shogi platform: the official Japan Shogi Association app, with live matchmaking and ranked kyu/dan promotion. Shogiful is a single-player training app with no account and no clock. You play engine opponents at your own pace, review every game with YaneuraOu, and train on the mistakes you make. You can use both: Shogiful to practise, and Shogi Wars to compete."
  - q: "How is Shogiful different from Lishogi or 81Dojo?"
    a: "Lishogi and 81Dojo are online platforms built around playing people. Lishogi is the free open-source web platform and 81Dojo the long-running international dojo. Shogiful works offline and focuses on training: on-device analysis with a card for each mistake, a daily plan aimed at your top weakness, and drills for tsume, drops, castles, joseki, and endgames. Use it to practise between your online games."
  - q: "What engine does Shogiful use?"
    a: "YaneuraOu, with its NNUE evaluation file built into the app. It runs on your iPhone, iPad, or Mac, so analysis needs no connection. It checks every move of your games, plays your 40 opponents, and powers the coach and the Deep Lines view. Shogiful turns its evaluations into mistake cards in plain words."
  - q: "How is Shogiful different from PiyoShogi?"
    a: "PiyoShogi is a free app that is often recommended to beginners, with graded computer levels and its own analysis. Shogiful is built around training: every mistake gets a card with what you played, what was best, and a tip, your daily plan aims at your top weakness, and you get 501 tsume problems, 99 drop drills, 62 castle drills, and 80 lessons. It also offers piece styles with arrows or with no kanji at all."
  - q: "Does Shogiful have time controls?"
    a: "No. Games against Shogiful's opponents are untimed, with no clock and no byoyomi, so take as long as you like on any move. For timed practice ahead of online play, use an online platform such as Shogi Wars, Lishogi, or 81Dojo."
  - q: "What is tsume-shogi, and does Shogiful include it?"
    a: "Tsume-shogi are shogi's classic checkmate problems: every attacking move must give check, and you mate the king with the pieces on the board and in hand. Shogiful's Tsume Trail has 501 problems in five levels, from 1-move to 9-move mates. The 381 problems in the 1-, 3-, and 5-move levels are free; Premium adds the 7- and 9-move levels. Any move that really mates counts, even when it differs from the book answer."
  - q: "Can I import my games from Shogi Wars or 81Dojo?"
    a: "Yes, as KIF files. Go to Settings, then Data & Privacy, then Import KIF, and import from a file, the clipboard, or pasted text, in UTF-8 or Shift-JIS. You see a preview with the players, handicap, and move count before you import. Imported games are reviewed like any other game, from the Sente side, and the review counts toward the free 2 analyses a day."
  - q: "Does Shogiful work offline?"
    a: "Yes, for everything you do with shogi. Playing, analysis, training, and review run on the device with a built-in engine. Buying or restoring Premium and Game Center need a connection."
  - q: "Is Shogiful free? What does Premium cost?"
    a: "Shogiful is free to download, and playing is never limited: all 40 opponents, unlocked as you win, with all piece styles and the 3D board. The free version includes 2 game analyses, 3 training puzzles, and 2 coach hints a day, 381 tsume problems, and 31 lessons. Premium removes the daily limits and opens Deep Lines, all 501 tsume problems, every drill, all 80 lessons, and the Skill Profile and Weakness Trends. It costs {P_MONTHLY}/month or {P_YEARLY}/year, each with a {TRIAL}, or {P_LIFETIME} once for lifetime access. Family Sharing is included. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does Shogiful need an account?"
    a: "No. There is no sign-up and no Shogiful account. Your games, analysis, and training history are stored on your device. Game Center is optional, and purchases go through your Apple Account."
  - q: "Can I play against other people in Shogiful?"
    a: "No. Every game is against Shogiful's 40 opponents, which run from a gentle beginner to master level and unlock as you beat them. For ranked games against people, use Shogi Wars, Lishogi, or 81Dojo, and import those games as KIF to review them in Shogiful."
  - q: "Can I play handicap shogi?"
    a: "Yes, through Komaochi in the Training tab. It has 40 handicap scenarios across 8 handicaps, from lance odds to eight pieces, each with a goal such as mate or material. Begin practice opens a game from that handicap position. Handicap games start only from Komaochi, not from the Play tab."
  - q: "Does Shogiful support Japanese?"
    a: "Yes. Shogiful has 39 localizations, Japanese among them, and follows your device language. Japanese users get their own first-launch flow that asks for a kyū or dan level, and moves can be shown in Japanese notation (▲７六歩) or Western notation (P-7f)."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/shogiful/support/"

release:
  first_release: "2026-06-11"
  last_updated: "2026-06-11"

related_journal:
  slug: making-shogi-readable-without-kanji
  anchor: "Shogi pieces in English: how to read the board without learning kanji"

show_body: true
about_heading: "What Shogiful does: shogi play, game analysis, and training"

ratings:
  value: "3.4"
  count: 18
  last_synced: "2026-10-22"
related_apps: ["xiangqiful", "chessful"]
last_updated: 2026-10-29
---
Shogiful is a [shogi training and analysis app for iPhone, iPad, and Mac](#features). Shogi is the Japanese form of chess, played on a 9×9 board where captured pieces come back into play as drops. Shogiful puts play, review, and training in one app, and it starts with the board itself. You can play with traditional kanji pieces, with kanji plus arrows that show how each piece moves, or with chess-style pieces that have no kanji at all ([the design story is in the journal](/journal/making-shogi-readable-without-kanji/)).

After a game, [YaneuraOu](https://github.com/yaneurao/YaneuraOu) checks every move on your device and labels each one from Best move to Blunder. Each mistake gets a card with what you played, what was best, the cost in pawns, and a coach's tip, sorted into 12 types written for shogi, among them Drop Mistake, Promotion Mistake, Castle Weakness, and Missed Tsume. The [example mistake cards](#templates) show the format.

Those mistakes [shape your training](#how-it-works). Today's Training builds each session around your level and your top weakness, and spaced repetition brings back the puzzles you miss. The library behind it holds 501 tsume problems, 99 drop drills, 62 castle drills, 55 joseki drills, 62 endgame races, 30 tesuji cards, 40 handicap scenarios, and 80 lessons. If you are just starting with openings, our [beginner's guide to Static Rook and Ranging Rook](/journal/shogi-openings-for-beginners/) pairs well with the Joseki Lab.

You play 40 opponents in eight tiers, from Koishi to Meijin, and each one unlocks when you beat the one before it twice. Games from other apps come in as KIF files. Shogiful has no online play, so for ranked games against people, Shogi Wars, Lishogi, and 81Dojo remain the right tools; the [side-by-side comparison](#compare-heading-shogiful) sets out the differences. For the whole category, including PiyoShogi and the classic offline apps, see our [guide to the best shogi apps for iPhone](/guides/best-shogi-apps-iphone/).

The free version never limits play and includes 2 analyses, 3 puzzles, and 2 coach hints a day. Premium removes those limits and opens every drill and lesson, for {P_MONTHLY}/month or {P_YEARLY}/year with a {TRIAL}, or {P_LIFETIME} once for [lifetime](/apps/shogiful/#pricing). There is [no account, and the app has no ads or tracking](/apps/shogiful/privacy/). Lagerland Apps also makes [Chessful](/apps/chessful/) for chess and [Xiangqiful](/apps/xiangqiful/) for xiangqi (Chinese chess). Shogiful is published by Lagerland Apps, an independent Apple developer in Finland.
