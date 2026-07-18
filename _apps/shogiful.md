---
layout: app
slug: shogiful
name: "Shogiful"
tagline: "Master shogi. Move by move."
quick_answer: "Shogiful is a shogi (Japanese chess) training and game analysis app for iPhone, iPad, and Mac. It uses YaneuraOu — the strongest open-source shogi engine — to review every move you play, explains your mistakes in plain language, and builds adaptive training from your real weaknesses, including the parts of shogi chess apps can't teach: drops, promotions, castle defense, and tsume. Western piece sets make the board readable without knowing any kanji. Includes 10 AI opponents and a tsume-shogi puzzle library. Free with Premium from $1.99/month, $9.99/year, or $19.99 lifetime. Fully offline, no account, no ads, no tracking."
category: games
platforms: ["iOS", "iPadOS", "macOS"]
status: live

app_store_url: "https://apps.apple.com/app/id6761656926"

price:
  model: freemium
  value: "Free — Premium from $1.99/mo"
schema_price: "0"
schema_high_price: "19.99"
schema_offer_count: "4"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The Lifetime tier is a one-time purchase — no auto-renew. Universal Purchase across iPhone, iPad, and Mac."

# Free / Premium-Monthly / Premium-Annual / Lifetime — same upgrade-ladder
# presentation as Chessful. Lifetime sits at 10 months of monthly Premium.
plans:
  - name: "Free"
    price: "$0"
    summary: "Every opponent, the core analysis loop, and daily training — forever."
    features:
      - "Play all 10 AI opponents, unlimited games"
      - "2 full game analyses per day with plain-language mistake explanations"
      - "3 training puzzles per day, including tsume-shogi"
      - "Traditional kanji and Western piece sets — switch anytime"
      - "Works fully offline, no account"
  - name: "Premium · Monthly"
    price: "$1.99/mo"
    summary: "Full Premium, billed monthly. Cancel anytime."
    features:
      - "Unlimited game analysis with move-by-move coaching"
      - "Unlimited training sessions and tsume puzzles"
      - "Deep analysis — higher engine depth with multiple candidate lines"
      - "Full progress view: skill radar, rating estimate, accuracy trends"
  - name: "Premium · Annual"
    price: "$9.99/yr"
    summary: "Same Premium features, billed once a year. ~58% cheaper than paying monthly."
    features:
      - "Everything in Premium · Monthly"
      - "~58% cheaper than monthly over a year"
      - "Cancel anytime in Settings before renewal"
    highlight: true
  - name: "Lifetime"
    price: "$19.99 once"
    summary: "All Premium features. Ten months of monthly Premium — then yours forever."
    features:
      - "Everything in Premium · Annual"
      - "One-time purchase, no renewal"
      - "Universal Purchase across iPhone, iPad, and Mac"
      - "Restores on every device signed in with the same Apple ID"
    highlight_label: "Best long-term value"

icon: "/assets/icons/shogiful.png"
og_image: "/assets/og/shogiful.png"

seo:
  title: "Shogi Training & Analysis App — iPhone, iPad, Mac | Shogiful"
  description: "Shogi (Japanese chess) training app for iPhone, iPad & Mac. YaneuraOu analysis in plain English, Western pieces — no kanji needed. Tsume puzzles, offline."
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
    - shogi wars alternative offline
    - learn shogi from chess
    - shogi drops explained

hero:
  pre_headline: "Shogi training & analysis app for iPhone, iPad, and Mac"
  headline: "The shogi teacher that speaks your language."
  subheadline: "Shogiful analyzes your games with YaneuraOu, explains your mistakes in plain English, and builds training around your real weaknesses — drops, promotions, castle defense, endgame attacks. Western piece sets mean you never need to read kanji to play. 10 AI opponents, tsume puzzles, fully offline. Free with Premium from $1.99/month."
  cta_label: "Download Free"
  alt: "Shogiful — a shogi game in progress on a 3D wooden board on iPhone, mid-game against the AI opponent Kiri"

who_for:
  - "You know chess and are curious about shogi — from anime, board-game nights, or pure curiosity — but bounced off the kanji pieces"
  - "You've learned the rules but lose constantly to drops you never saw coming"
  - "You want plain-language explanations of your mistakes, not raw engine evaluation numbers"
  - "You want structured training — tsume puzzles plus exercises built from your own games — not just endless online blitz"
  - "You prefer playing offline, at your own pace, without a server account or time pressure"
  - "You want the app on iPhone, iPad, and Mac — one purchase, all three"

who_not_for:
  - "You primarily want ranked online play against humans (Shogi Wars, 81Dojo, and Lishogi are built for that)"
  - "You want a multi-game board-game collection (Shogiful is shogi only, on purpose)"
  - "You want social features, tournaments, or community chat"
  - "You're looking for a kifu database or professional game record viewer"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "For the player who can't read the pieces yet — and shouldn't have to."
  story: "Shogiful exists because the biggest barrier to shogi outside Japan isn't the rules — it's the board. Half the people who try shogi bounce off kanji pieces before they ever experience a drop attack or build their first castle. The existing apps assume you can already read the pieces and already have someone to teach you; the online platforms throw you into ranked games against humans on day one. Shogiful was built the other way around: Western piece sets with movement indicators so the board is readable immediately, a real engine (YaneuraOu, the strongest open-source shogi engine) reviewing every move you play, and explanations written like a patient teacher — which drop you missed, why that pawn push cracked your castle open, where the forced mate was. Everything runs on the device. No server, no account, no rate limits."
  signals:
    - "YaneuraOu NNUE runs on-device — no cloud analysis, no quota, no account"
    - "Mistake detection built for shogi, not adapted from chess: drop mistakes, promotion decisions, castle weaknesses, and missed tsume are first-class categories"
    - "English and Japanese localization from day one, with JSA-standard shogi terminology"
    - "19 live apps in the Lagerland catalogue, all under the same data discipline: no tracking, no ads, no required accounts"
  external_link:
    label: "Read the Lagerland studio backstory →"
    href: "/lagerland-apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally — usually within a day."

alternatives_to:
  - "Shogi Wars"
  - "Lishogi"
  - "81Dojo"
  - "ShogiQuest"
  - "Kanazawa Shogi"
  - "PiyoShogi"

value_points:
  - title: "Play shogi without reading kanji"
    description: "Western piece sets with symbolic icons and movement indicators make the board readable from your first game. Switch to traditional kanji pieces whenever you're ready — the app teaches the characters progressively as you train, instead of demanding them up front."
  - title: "Understand why you lost"
    description: "After every game, Shogiful shows exactly where it went wrong — in words, not centipawns. The silver you dropped on the wrong square, the promotion you skipped, the edge-pawn push that opened your castle, the forced mate you walked past."
  - title: "Train the weaknesses shogi actually has"
    description: "Drops, promotion decisions, castle maintenance, and endgame mating attacks are skills chess training never touches. Shogiful tracks them separately, generates exercises from your own mistakes, and schedules them with spaced repetition so your weakest patterns get the most attention."
  - title: "Fully offline, fully private"
    description: "YaneuraOu runs on the device. No account, no servers, no daily quota from a cloud API, no ads. Play and analyze on a flight, on the subway, or anywhere without signal."

features:
  - title: "Game analysis you can actually read"
    description: "Every move reviewed by YaneuraOu — the same engine family that powers top computer shogi — then explained in clear sentences. Blunders, missed drop tactics, promotion mistakes, castle weaknesses, and missed tsume sequences: each one described so you learn from it, rather than nodding at an evaluation graph."
  - title: "Built for the hardest parts of shogi"
    description: "Drops and promotions are where chess players lose shogi games. Shogiful's mistake detection treats them as first-class categories: it tells you when a knight drop would have forked king and rook, when promoting your silver was wrong, and when the engine found a forced mate your attack walked past."
  - title: "Tsume-shogi puzzle library"
    description: "Classical checkmate problems — every attacker move a check, every hand piece used — starting with 76 problems verified for correctness on-device (30 one-move, 46 three-move) and expanding toward ~500 on the roadmap. Scheduled with spaced repetition and mixed with exercises generated from your own games."
  - title: "10 AI opponents across 4 tiers"
    description: "From Hana, who blunders like a true beginner at around 500 strength, to Sensei at roughly 1800 — each opponent has a distinct style: aggressive attackers, castle builders, drop tacticians, endgame specialists. Beat one twice to unlock the next. Games are untimed: no clock, no byoyomi pressure, analyze as long as you like."
  - title: "Skill tracking across five dimensions"
    description: "Tactics, defense, positioning, endgame, and openings — each tracked separately as you play and train, with a skill radar, an estimated rating, and accuracy trends over time. Premium unlocks the full progress view."
  - title: "Universal Purchase across iPhone, iPad, and Mac"
    description: "One purchase covers all three platforms — iPhone for a quick game and puzzle session, iPad for a board-sized match, Mac for serious post-game review with keyboard shortcuts and KIF/SFEN export."

# Methodology disclosure — emits HowTo schema via _layouts/app.html.
how_it_works:
  intro: "Shogiful's coaching loop is the part of the app that does the real teaching work. Here's exactly what happens between you losing a game and Shogiful generating tomorrow's training session."
  steps:
    - title: "YaneuraOu reviews every move"
      detail: "When a game ends, Shogiful runs YaneuraOu locally over the full move list and evaluates every position — including the hand pieces, which in shogi are as much a part of the position as the board. The engine's 61 MB NNUE neural network runs entirely on-device — no cloud calls, no account, no quota from a server."
    - title: "Mistakes are classified in shogi terms"
      detail: "Raw evaluation loss is unreadable. Each significant mistake is classified into a shogi-specific category: hanging piece, missed drop tactic, wrong promotion decision, castle weakness, missed fork, missed tsume (forced mate), passive move, endgame error. These categories were built for shogi from scratch — drops and promotions don't exist in chess, so no chess taxonomy was reused."
    - title: "Plain-language explanation generated"
      detail: "Each classified mistake becomes one or two sentences a player can read. \"You dropped the silver to 4d, but a knight drop on 3c would have forked the king and rook\" beats a bare evaluation swing every time. Explanations adapt to mistake severity and are written in both English and Japanese."
    - title: "Patterns accumulate into your skill profile"
      detail: "Each detected mistake updates one of five skill dimensions — tactics, defense, positioning, endgame, openings. Recent games weigh more than old ones, so the profile tracks who you are now, not who you were twenty games ago. The profile feeds your estimated rating and the skill radar."
    - title: "Training targets your weakest patterns"
      detail: "Training sessions pull exercises from your weakest areas — roughly 60% from your primary weakness, 25% from the second, 15% mixed — combining positions lifted from your own games with curated tsume-shogi problems. Spaced repetition (SM-2) brings each pattern back just before you'd forget it."
    - title: "Progress updates after every session"
      detail: "Accuracy trends, the skill radar, and your estimated rating update as you play and train. Weakness trends show whether a pattern is improving or worsening across your recent games — so you can see the drop-tactic work actually paying off."

# Example "mistake explained" gallery — shows the USP instead of describing it.
example_insights:
  anchor: "templates"
  overline: "What Shogiful explains"
  heading: "What a plain-language shogi mistake looks like in Shogiful."
  intro: "Six worked examples of how Shogiful translates an engine evaluation into something a player can actually use. Every example is the kind of mistake the trainer then drills in tomorrow's session — and four of the six are mistakes that can't happen in chess."
  cards:
    - tag: "Tactics · Drop mistake"
      headline: "You dropped the silver to 4d. A knight drop on 3c forked king and rook."
      body: "Both drops looked active, but the knight on 3c attacked two targets at once — the king has to move, and the rook falls. Drops are your most powerful tactical weapon in shogi: before placing a piece, scan for squares that attack two things. Pattern: drop-fork blindness."
    - tag: "Defense · Castle weakness"
      headline: "Your mino castle was solid. The edge-pawn push opened a fatal lane."
      body: "Advancing the 9th-file pawn looked harmless, but it gave your opponent's lance and pawn a lever straight into the castle. Castle walls protect your king — every pawn you move is a brick removed. Pattern: castle-integrity lapse."
    - tag: "Tactics · Missed tsume"
      headline: "There was a forced mate in 5, starting with a gold drop on 2b."
      body: "You played a safe defensive move instead — and the attack evaporated two moves later. When the enemy king is exposed and you have pieces in hand, always check for tsume before anything else. Pattern: mate-check skip."
    - tag: "Tactics · Promotion mistake"
      headline: "You promoted the silver. Unpromoted, it could have retreated to defend."
      body: "Promotion is a real decision in shogi — a promoted silver gains forward power but loses its backward diagonals, and here the retreat was the move your defense needed two turns later. Pattern: reflex promotion."
    - tag: "Tactics · Hanging piece"
      headline: "After your bishop trade, the recapturing pawn left your gold undefended."
      body: "The trade was fine; the recapture wasn't. In shogi a captured gold doesn't just leave the board — it goes to your opponent's hand and comes back as a drop next to your king. Material mistakes hurt twice. Pattern: post-exchange blindness."
    - tag: "Endgame · Speed miscount"
      headline: "You spent a move grabbing material. Your opponent's attack was one move faster."
      body: "Shogi endgames are races, not grinds — the question is never \"who has more material\" but \"whose mating attack lands first.\" Taking the lance cost the tempo that let your opponent's silver drop seal the mate. Pattern: endgame tempo miscount."

# Side-by-side comparison — auto-triggers the mid-page CTA and the alt-strip.
comparison_table:
  intro: "Every row is a question a shogi-curious player asks before installing an app. Shogi Wars is the dominant online platform (official Japan Shogi Association app); Lishogi is the free open-source web platform; 81Dojo is the international online dojo; ShogiQuest is the lightweight quick-play app. All four are built around online play against humans — Shogiful is a single-player training product. Summarised from each app's public listing on 2026-06-11."
  competitors: ["Shogiful", "Shogi Wars", "Lishogi", "81Dojo", "ShogiQuest"]
  rows:
    - feature: "Fully offline (no internet required)"
      values: ["Yes — YaneuraOu runs on-device", "No — online matchmaking", "No — web platform", "No — online server", "No — online matches"]
    - feature: "Account required"
      values: ["No account ever", "Yes", "Optional for casual play", "Yes", "Yes (auto-created)"]
    - feature: "Built for players who can't read kanji"
      values: ["Yes — Western piece sets + progressive kanji learning", "Partial — internationalized UI, kanji-style pieces", "Yes — Western notation and piece options", "Partial — English community, traditional pieces", "Partial — simple UI"]
    - feature: "Engine analysis of your games"
      values: ["Yes — unlimited basic, deep on Premium", "Paid AI features (Kishin)", "Yes — server analysis", "Community + engine tools", "Limited"]
    - feature: "Plain-language mistake explanations"
      values: ["Yes — shogi-specific coaching sentences", "No — evaluation only", "No — evaluation graph", "No", "No"]
    - feature: "Training built from your games"
      values: ["Yes — spaced repetition on your detected weaknesses", "No", "Puzzle library — not your-game-derived", "No", "No"]
    - feature: "Tsume-shogi puzzles"
      values: ["Yes — bundled library with SRS", "Yes — separate features", "Yes — puzzle section", "Limited", "No"]
    - feature: "Live human matchmaking"
      values: ["No (intentional)", "Yes — millions of players", "Yes — free", "Yes — international dojo", "Yes — quick matches"]
    - feature: "Lifetime / one-time pricing"
      values: ["$19.99 lifetime", "Subscription for unlimited play", "Free / donation", "Free (membership options)", "Free with ads/IAP"]
    - feature: "Privacy — no tracking, no third-party SDKs"
      values: ["Zero tracking SDKs, nothing collected", "Standard mobile analytics", "Open source, minimal", "Standard web analytics", "Standard mobile analytics"]
    - feature: "Platforms"
      values: ["iPhone + iPad + Mac (Universal Purchase)", "iPhone + Android", "Web", "Web + mobile apps", "iPhone + Android + web"]
  footnote: "Competitor positioning summarised from each platform's public landing page and store listing on 2026-06-11. Pricing and feature claims change frequently — verify before switching. If what you want is ranked play against humans, those platforms are the right tools; Shogiful is the training companion, not the arena."

roadmap:
  overline: "Roadmap"
  heading: "What's shipped, what's next."
  intro: "Shogiful v1 covers offline play, full-game analysis, and adaptive training on iPhone, iPad, and Mac today. Below is the public roadmap. Dates are targets, not commitments — slips happen and you'll hear about them here first."
  items:
    - when: "Shipped"
      title: "YaneuraOu analysis + plain-language coaching"
      detail: "Live today on iPhone, iPad, and Mac. Every move reviewed on-device, every significant mistake translated into a sentence you can read — in English or Japanese."
      status: "shipped"
    - when: "Shipped"
      title: "Western piece sets + traditional kanji"
      detail: "Symbolic Western pieces with movement indicators, or traditional kanji tiles — switchable any time, with a piece guide always one tap away during games."
      status: "shipped"
    - when: "Shipped"
      title: "10 AI opponents, tsume puzzles, weakness training"
      detail: "Four tiers from true beginner to advanced, bundled tsume-shogi problems, and training sessions generated from the mistakes in your own games with spaced repetition."
      status: "shipped"
    - when: "Targeted 2026 Q3"
      title: "Expanded tsume library (~500 problems)"
      detail: "Five-, seven-, and nine-move tsume shards added to the bundled one- and three-move problems — sourced from public-domain Edo-era collections and engine-verified positions."
    - when: "Targeted 2026 Q4"
      title: "More languages"
      detail: "Korean, Chinese (Simplified and Traditional), German, French, Spanish, and Portuguese on top of the English + Japanese that ship today."
    - when: "Under consideration"
      title: "KIF import, castle recognition, joseki training, handicap games"
      detail: "Importing game records from Shogi Wars and 81Dojo (KIF format) for analysis, named castle-formation detection, opening training by formation, and traditional handicap (koma-ochi) games against the AI roster."
  disclaimer: "Roadmap last reviewed 2026-06-11. Targeted dates can slip; shipped items are live on the App Store."

screenshots:
  - src: "/assets/screenshots/shogiful/1.png"
    caption: "Play a full game on a 3D wooden board against the AI opponent roster."
  - src: "/assets/screenshots/shogiful/2.png"
    caption: "Dashboard — rating, streak, today's training and your last game at a glance."
  - src: "/assets/screenshots/shogiful/3.png"
    caption: "Mistake detail — the engine shows the stronger move and explains it in plain English."
  - src: "/assets/screenshots/shogiful/4.png"
    caption: "Game review with accuracy, blunders, mistakes and best moves after every game."
  - src: "/assets/screenshots/shogiful/5.png"
    caption: "Daily training built around your real weaknesses, with adjustable session length."
  - src: "/assets/screenshots/shogiful/6.png"
    caption: "Progress tracking — estimated rating, accuracy trend and a per-skill profile."
  - src: "/assets/screenshots/shogiful/7.png"
    caption: "Play ladder — climb a roster of named AI opponents from novice to expert."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no trackers"
    - "No account or sign-up required"
    - "All analysis runs locally on your device — YaneuraOu, mistake detection, and coaching explanations all on-device"
    - "Works fully offline — no cloud calls, no server"
    - "Universal Purchase across iPhone, iPad, and Mac via standard Apple infrastructure"

faq:
  - q: "What is Shogiful?"
    a: "Shogiful is a shogi training and game analysis app for iPhone, iPad, and Mac. It analyzes your games with the YaneuraOu engine, explains your mistakes in plain language, and builds training sessions focused on your real weaknesses across five skill dimensions — tactics, defense, positioning, endgame, and openings — with shogi-specific coaching on drops, promotions, castles, and tsume."
  - q: "Can I play shogi without knowing kanji?"
    a: "Yes — this is one of the core reasons Shogiful exists. The Western piece set uses symbolic icons with movement indicators, so the board is readable from your very first game. A piece guide is always one tap away during play, and the app introduces the traditional kanji characters progressively as you train, so you can switch to traditional pieces whenever you feel ready."
  - q: "Is Shogiful good for chess players learning shogi?"
    a: "It's built for exactly that player. Shogi and chess share roots but diverge where it matters: captured pieces return to the board as drops, promotion is a real decision rather than an automatic queen, and endgames are attacking races rather than simplified grinds. Shogiful's coaching treats these differences as first-class topics — its mistake categories include drop mistakes, promotion mistakes, castle weaknesses, and missed tsume, none of which exist in a chess trainer."
  - q: "How is Shogiful different from Shogi Wars?"
    a: "Shogi Wars is the dominant online shogi platform — official Japan Shogi Association app, live matchmaking, ranked kyu/dan promotion. Shogiful is a single-player training product: no account, no server, no clock anxiety from human opponents. You play AI opponents at your pace, get every game analyzed with plain-language explanations, and train your specific weaknesses. Many players use both — Shogiful to improve, Shogi Wars to compete."
  - q: "How is Shogiful different from Lishogi or 81Dojo?"
    a: "Lishogi and 81Dojo are online platforms built around playing humans — Lishogi is the free open-source web platform, 81Dojo the long-running international dojo. Both are excellent for matchmaking. Shogiful is offline and coaching-focused: on-device engine analysis explained in sentences, weakness tracking across five skills, and adaptive training with spaced repetition. It's the practice room, not the tournament hall."
  - q: "What engine does Shogiful use?"
    a: "Shogiful uses YaneuraOu — the strongest open-source shogi engine and the foundation of multiple World Computer Shogi Championship winners — with its 61 MB NNUE neural-network evaluation running entirely on your device. Shogiful translates the engine's output into plain-language coaching rather than showing you raw evaluation numbers."
  - q: "How is Shogiful different from PiyoShogi?"
    a: "PiyoShogi is an excellent free app and a common recommendation for beginners — 40 finely-graded AI levels, an analysis function, and daily mate problems. Shogiful's focus is the coaching loop on top of play: every game analyzed with mistakes explained in plain-language sentences (not just an evaluation), weakness tracking across five skills, spaced-repetition training generated from your own games, and Western piece sets with progressive kanji learning for players who can't read the pieces yet. If you want free play with adjustable difficulty, PiyoShogi is great; if you want to be coached from your own games in English, that's Shogiful."
  - q: "Does Shogiful have time controls?"
    a: "No — by design. Games against Shogiful's AI opponents are untimed: no clock, no byoyomi countdown, no time pressure. Take as long as you want on any move, then analyze at the same pace. If you want timed practice for online play, the online platforms (Shogi Wars, Lishogi, 81Dojo) are the right place for it."
  - q: "What is tsume-shogi, and does Shogiful include it?"
    a: "Tsume-shogi are shogi's classical checkmate puzzles: every attacking move must be a check, every piece in hand must be used, and the defender plays the longest resistance. Shogiful bundles a verified tsume library from one-move beginner problems to multi-move calculations, scheduled with spaced repetition alongside exercises generated from your own games. An expanded ~500-problem library is on the roadmap."
  - q: "Does Shogiful work offline?"
    a: "Yes — completely. The engine, the analysis, the coaching explanations, the training system, and all 10 AI opponents run on your device. No internet connection is ever needed, and there's no account to sign into."
  - q: "Is Shogiful free? What does Premium cost?"
    a: "Shogiful is free to download and play: all 10 AI opponents with unlimited games, 2 full game analyses per day, and 3 training puzzles per day — no ads, no account. Premium unlocks unlimited analysis, unlimited training, deep multi-line analysis, and the full progress view. Premium is $1.99/month, $9.99/year, or $19.99 once for lifetime access. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does Shogiful need an account?"
    a: "No. Shogiful requires no account, no sign-up, and no personal information. Your games, analysis, and training progress stay on your device. Purchases restore through your Apple ID — Apple's mechanism, not a Shogiful account."
  - q: "Can I play against other people in Shogiful?"
    a: "No — and that's deliberate. Shogiful is a training product: 10 AI opponents with distinct styles from true beginner to advanced strength, unlocked as you beat them. For ranked human play, Shogi Wars, Lishogi, and 81Dojo are the right tools; Shogiful is designed to make you better before and between those games."
  - q: "Does Shogiful support Japanese?"
    a: "Yes. Shogiful ships in English and Japanese from day one, with JSA-standard shogi terminology in Japanese and both Western and KIF notation styles available. More languages are on the roadmap."
  - q: "Can I import my games from Shogi Wars or 81Dojo?"
    a: "Not yet — KIF import (the standard shogi game-record format both platforms export) is under consideration on the roadmap. Once shipped, you'll be able to bring your online games into Shogiful's analyzer and have your weakness profile built from games you've already played."

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
about_heading: "What Shogiful does — shogi training, analysis, and a board you can read"

ratings:
  value: "3.0"
  count: 2
  last_synced: "2026-07-18"
---
Shogiful is a [shogi training & analysis app for iPhone, iPad, and Mac](#features) — shogi being the Japanese form of chess, played on a 9×9 board where captured pieces return to play. It's built around a simple observation: the biggest barrier to shogi outside Japan isn't the rules, it's the kanji on the pieces. Shogiful ships [Western piece sets with movement indicators](#features) so the board is readable from your first game ([the design story is documented in the journal](/journal/making-shogi-readable-without-kanji/)), then backs the playing experience with the thing improving players actually need — a real engine reviewing every move and explaining mistakes in sentences instead of evaluation numbers.

The engine is [YaneuraOu](https://github.com/yaneurao/YaneuraOu), the strongest open-source shogi engine, running entirely on-device with its 61 MB NNUE neural network. After each game, Shogiful classifies every significant mistake into shogi-specific categories — missed drop tactics, wrong promotion decisions, castle weaknesses, missed tsume — and turns each one into [plain-language coaching](#templates). These categories were built for shogi from scratch, not adapted from chess: drops and promotions are where chess players lose shogi games, and they're exactly what generic chess-style training never covers.

From the analysis, Shogiful [builds an adaptive training queue](#how-it-works): exercises lifted from your own games, mixed with a verified tsume-shogi puzzle library, scheduled with spaced repetition across five tracked skills — tactics, defense, positioning, endgame, and openings. Ten AI opponents across four tiers give you someone to play at every level, from a true beginner who blunders honestly to an advanced opponent who punishes loose castles.

Everything runs on your device. There is no cloud, no account, no daily quota from a server, no ads. The trade-off is that Shogiful does not offer online play against humans — for that, Shogi Wars, Lishogi, and 81Dojo remain the right tools, and the [side-by-side comparison](#compare-heading-shogiful) is honest about it. Shogiful is the practice room, not the arena. For the full category view — including PiyoShogi and the classic offline apps — see [our honest guide to the best shogi apps for iPhone](/guides/best-shogi-apps-iphone/).

Free tier: all 10 opponents with unlimited games, 2 game analyses per day, 3 training puzzles per day. Premium: unlimited analysis and training, deep multi-line analysis, and the full progress view — $1.99/month, $9.99/year, or $19.99 once for [lifetime](/apps/shogiful/#pricing). [No tracking, no ads, no account](/apps/shogiful/privacy/). Published by Lagerland Apps, an independent Apple developer in Finland.
