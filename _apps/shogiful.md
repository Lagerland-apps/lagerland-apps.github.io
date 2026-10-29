---
layout: app
slug: shogiful
name: "Shogiful"
tagline: "Master shogi. Move by move."
quick_answer: "Shogiful is a shogi (Japanese chess) training and game analysis app for iPhone, iPad, and Mac. It uses YaneuraOu, the strongest open-source shogi engine, to review every move you play, explains your mistakes in plain language, and builds adaptive training from your real weaknesses, including the parts of shogi that chess apps can't teach: drops, promotions, castle defense, and tsume. Western piece sets make the board readable without knowing any kanji. It includes 10 AI opponents and a tsume-shogi puzzle library. Free, with Premium from {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime. Works fully offline, with no account, no ads, and no tracking."
category: games
status: live

app_store_url: "https://apps.apple.com/app/id6761656926"

price:
  model: freemium

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The Lifetime tier is a one-time purchase with no auto-renewal. Universal Purchase across iPhone, iPad, and Mac."

# Free / Premium-Monthly / Premium-Annual / Lifetime: same upgrade-ladder
# presentation as Chessful. Lifetime is priced against months of monthly Premium.
plans:
  - name: "Free"
    price: "$0"
    summary: "Every opponent, the core analysis loop, and daily training, with no time limit."
    features:
      - "Play all 10 AI opponents, unlimited games"
      - "2 full game analyses per day with plain-language mistake explanations"
      - "3 training puzzles per day, including tsume-shogi"
      - "Traditional kanji and Western piece sets, switchable anytime"
      - "Works fully offline, no account"
  - name: "Premium · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Premium, billed monthly. Cancel anytime."
    features:
      - "Unlimited game analysis with move-by-move coaching"
      - "Unlimited training sessions and tsume puzzles"
      - "Deep analysis: higher engine depth with multiple candidate lines"
      - "Full progress view: skill radar, rating estimate, accuracy trends"
  - name: "Premium · Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same Premium features, billed once a year. ~{SAVE_YEARLY}% cheaper than paying monthly."
    features:
      - "Everything in Premium · Monthly"
      - "~{SAVE_YEARLY}% cheaper than monthly over a year"
      - "Cancel anytime in Settings before renewal"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All Premium features for one payment."
    features:
      - "Everything in Premium · Annual"
      - "One-time purchase, no renewal"
      - "Universal Purchase across iPhone, iPad, and Mac"
      - "Restores on every device signed in with the same Apple ID"
    highlight_label: "Best long-term value"

icon: "/assets/icons/shogiful.png"
og_image: "/assets/og/shogiful.png"

seo:
  title: "Shogi Training & Analysis App: iPhone, iPad, Mac | Shogiful"
  description: "Shogi (Japanese chess) training app for iPhone, iPad & Mac. YaneuraOu analysis in plain English, Western pieces, no kanji needed. Tsume puzzles, offline."
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
  headline: "A shogi teacher that explains in plain English."
  subheadline: "Shogiful analyzes your games with YaneuraOu, explains your mistakes in plain English, and builds training around your real weaknesses: drops, promotions, castle defense, endgame attacks. With Western piece sets you never need to read kanji to play. 10 AI opponents, tsume puzzles, fully offline. Free, with Premium from {P_MONTHLY}/month."
  cta_label: "Download Free"
  alt: "Shogiful shogi game in progress on a 3D wooden board on iPhone, mid-game against the AI opponent Kiri"

who_for:
  - "You know chess and got curious about shogi (from anime, board-game nights, or nowhere in particular) but bounced off the kanji pieces"
  - "You've learned the rules but lose constantly to drops you never saw coming"
  - "You want plain-language explanations of your mistakes instead of raw engine evaluation numbers"
  - "You want structured training, tsume puzzles plus exercises built from your own games, more than endless online blitz"
  - "You prefer playing offline, at your own pace, without a server account or time pressure"
  - "You want the app on iPhone, iPad, and Mac, with one purchase covering all three"

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
  heading: "For the player who can't read the pieces yet."
  story: "We built Shogiful because outside Japan the biggest barrier to shogi is the board, more than the rules. Half the people who try shogi give up on the kanji pieces before they ever see a drop attack or build their first castle. The existing apps assume you can already read the pieces and have someone to teach you, and the online platforms put you into ranked games against humans on day one. Shogiful starts from the other end: Western piece sets with movement indicators so the board is readable immediately, a real engine (YaneuraOu, the strongest open-source shogi engine) reviewing every move you play, and explanations written the way a patient teacher would put them: which drop you missed, why that pawn push cracked your castle open, where the forced mate was. Everything runs on the device, with no server, no account, and no rate limits."
  signals:
    - "YaneuraOu NNUE runs on-device, so there is no cloud analysis, no quota, and no account"
    - "Mistake detection designed for shogi from the start: drop mistakes, promotion decisions, castle weaknesses, and missed tsume are first-class categories"
    - "English and Japanese localization from day one, with JSA-standard shogi terminology"
    - "{APP_COUNT} live apps in the Lagerland catalogue, all with the same data rules: no tracking, no ads, no required accounts"
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
  - title: "Play shogi without reading kanji"
    description: "Western piece sets with symbolic icons and movement indicators make the board readable from your first game. Switch to traditional kanji pieces whenever you're ready; the app teaches the characters gradually as you train."
  - title: "Understand why you lost"
    description: "After every game, Shogiful shows where it went wrong, in words instead of centipawns: the silver you dropped on the wrong square, the promotion you skipped, the edge-pawn push that opened your castle, the forced mate you walked past."
  - title: "Train the skills specific to shogi"
    description: "Chess training never touches drops, promotion decisions, castle maintenance, or endgame mating attacks. Shogiful tracks them separately, generates exercises from your own mistakes, and schedules them with spaced repetition so your weakest patterns get the most attention."
  - title: "Offline and private"
    description: "YaneuraOu runs on the device. There is no account, no server, no daily quota from a cloud API, and no ads, so you can play and analyze on a flight, on the subway, or anywhere without signal."

features:
  - title: "Game analysis you can actually read"
    description: "YaneuraOu, the same engine family that powers top computer shogi, reviews every move, and Shogiful explains the result in clear sentences. Blunders, missed drop tactics, promotion mistakes, castle weaknesses, and missed tsume sequences are each described so you learn from them instead of nodding at an evaluation graph."
  - title: "Coaching on drops and promotions"
    description: "Drops and promotions are where chess players lose shogi games. Shogiful's mistake detection treats them as first-class categories: it tells you when a knight drop would have forked king and rook, when promoting your silver was wrong, and when the engine found a forced mate your attack walked past."
  - title: "Tsume-shogi puzzle library"
    description: "Classical checkmate problems, where every attacker move is a check and every hand piece is used. The library starts with 76 problems verified for correctness on-device (30 one-move, 46 three-move). Problems are scheduled with spaced repetition and mixed with exercises generated from your own games."
  - title: "10 AI opponents across 4 tiers"
    description: "From Hana, who blunders like a true beginner at around 500 strength, to Sensei at roughly 1800, each opponent has a distinct style: aggressive attackers, castle builders, drop tacticians, endgame specialists. Beat one twice to unlock the next. Games are untimed, with no clock or byoyomi, so you can analyze as long as you like."
  - title: "Skill tracking across five dimensions"
    description: "Tactics, defense, positioning, endgame, and openings are each tracked separately as you play and train, with a skill radar, an estimated rating, and accuracy trends over time. Premium unlocks the full progress view."
  - title: "Universal Purchase across iPhone, iPad, and Mac"
    description: "One purchase covers all three platforms: iPhone for a quick game and puzzle session, iPad for a board-sized match, Mac for detailed post-game review with keyboard shortcuts and KIF/SFEN export."

# Methodology disclosure: emits HowTo schema via _layouts/app.html.
how_it_works:
  intro: "Shogiful's coaching loop does most of the teaching. This is what happens between you losing a game and Shogiful generating tomorrow's training session."
  steps:
    - title: "YaneuraOu reviews every move"
      detail: "When a game ends, Shogiful runs YaneuraOu locally over the full move list and evaluates every position, including the hand pieces, which in shogi are as much a part of the position as the board. The engine's 61 MB NNUE neural network runs entirely on-device, with no cloud calls, no account, and no server quota."
    - title: "Mistakes are classified in shogi terms"
      detail: "Raw evaluation loss is unreadable. Each significant mistake is classified into a shogi-specific category: hanging piece, missed drop tactic, wrong promotion decision, castle weakness, missed fork, missed tsume (forced mate), passive move, endgame error. The categories were written for shogi from scratch; drops and promotions don't exist in chess, so no chess taxonomy was reused."
    - title: "Plain-language explanation generated"
      detail: "Each classified mistake becomes one or two sentences a player can read. \"You dropped the silver to 4d, but a knight drop on 3c would have forked the king and rook\" beats a bare evaluation swing every time. Explanations adapt to mistake severity and are written in both English and Japanese."
    - title: "Patterns accumulate into your skill profile"
      detail: "Each detected mistake updates one of five skill dimensions: tactics, defense, positioning, endgame, openings. Recent games weigh more than old ones, so the profile reflects how you play now and not twenty games ago. The profile feeds your estimated rating and the skill radar."
    - title: "Training targets your weakest patterns"
      detail: "Training sessions pull exercises from your weakest areas (roughly 60% from your primary weakness, 25% from the second, 15% mixed), combining positions taken from your own games with curated tsume-shogi problems. Spaced repetition (SM-2) brings each pattern back just before you'd forget it."
    - title: "Progress updates after every session"
      detail: "Accuracy trends, the skill radar, and your estimated rating update as you play and train. Weakness trends show whether a pattern is improving or getting worse across your recent games, so you can see whether the drop-tactic work is paying off."

# Example "mistake explained" gallery: shows the USP instead of describing it.
example_insights:
  anchor: "templates"
  overline: "What Shogiful explains"
  heading: "What a plain-language shogi mistake looks like in Shogiful."
  intro: "Six worked examples of Shogiful turning an engine evaluation into something a player can use. Each is the kind of mistake the trainer then drills in tomorrow's session, and four of the six can't happen in chess."
  cards:
    - tag: "Tactics · Drop mistake"
      headline: "You dropped the silver to 4d. A knight drop on 3c forked king and rook."
      body: "Both drops looked active, but the knight on 3c attacked two targets at once: the king has to move, and the rook falls. Drops are your strongest tactical weapon in shogi, so before placing a piece, look for squares that attack two things. Pattern: drop-fork blindness."
    - tag: "Defense · Castle weakness"
      headline: "Your mino castle was solid. The edge-pawn push opened a fatal lane."
      body: "Advancing the 9th-file pawn looked harmless, but it gave your opponent's lance and pawn a lever straight into the castle. Castle walls protect your king, and every pawn you move takes a brick out. Pattern: castle-integrity lapse."
    - tag: "Tactics · Missed tsume"
      headline: "There was a forced mate in 5, starting with a gold drop on 2b."
      body: "You played a safe defensive move instead, and the attack evaporated two moves later. When the enemy king is exposed and you have pieces in hand, check for tsume before anything else. Pattern: mate-check skip."
    - tag: "Tactics · Promotion mistake"
      headline: "You promoted the silver. Unpromoted, it could have retreated to defend."
      body: "Promotion is a real decision in shogi. A promoted silver gains forward power but loses its backward diagonals, and here the retreat was the move your defense needed two turns later. Pattern: reflex promotion."
    - tag: "Tactics · Hanging piece"
      headline: "After your bishop trade, the recapturing pawn left your gold undefended."
      body: "The trade was fine; the recapture wasn't. In shogi a captured gold goes to your opponent's hand and comes back as a drop next to your king, so material mistakes hurt twice. Pattern: post-exchange blindness."
    - tag: "Endgame · Speed miscount"
      headline: "You spent a move grabbing material. Your opponent's attack was one move faster."
      body: "Shogi endgames are races. The question is \"whose mating attack lands first\", not \"who has more material.\" Taking the lance cost the tempo that let your opponent's silver drop seal the mate. Pattern: endgame tempo miscount."

# Side-by-side comparison: auto-triggers the mid-page CTA and the alt-strip.
comparison_table:
  intro: "Each row is a question a shogi-curious player asks before installing an app. Shogi Wars is the dominant online platform (the official Japan Shogi Association app), Lishogi the free open-source web platform, 81Dojo the international online dojo, and ShogiQuest the lightweight quick-play app. All four are built around online play against humans, while Shogiful is a single-player training product. Summarised from each app's public listing on 2026-06-11."
  competitors: ["Shogiful", "Shogi Wars", "Lishogi", "81Dojo", "ShogiQuest"]
  rows:
    - feature: "Fully offline (no internet required)"
      values: ["Yes, YaneuraOu runs on-device", "No, online matchmaking", "No, web platform", "No, online server", "No, online matches"]
    - feature: "Account required"
      values: ["No account ever", "Yes", "Optional for casual play", "Yes", "Yes (auto-created)"]
    - feature: "Built for players who can't read kanji"
      values: ["Yes, Western piece sets + progressive kanji learning", "Partial: internationalized UI, kanji-style pieces", "Yes, Western notation and piece options", "Partial: English community, traditional pieces", "Partial: simple UI"]
    - feature: "Engine analysis of your games"
      values: ["Yes, unlimited basic, deep on Premium", "Paid AI features (Kishin)", "Yes, server analysis", "Community + engine tools", "Limited"]
    - feature: "Plain-language mistake explanations"
      values: ["Yes, shogi-specific coaching sentences", "No, evaluation only", "No, evaluation graph", "No", "No"]
    - feature: "Training built from your games"
      values: ["Yes, spaced repetition on your detected weaknesses", "No", "Puzzle library, not drawn from your games", "No", "No"]
    - feature: "Tsume-shogi puzzles"
      values: ["Yes, bundled library with SRS", "Yes, separate features", "Yes, puzzle section", "Limited", "No"]
    - feature: "Live human matchmaking"
      values: ["No (intentional)", "Yes, millions of players", "Yes, free", "Yes, international dojo", "Yes, quick matches"]
    - feature: "Lifetime / one-time pricing"
      values: ["{P_LIFETIME} lifetime", "Subscription for unlimited play", "Free / donation", "Free (membership options)", "Free with ads/IAP"]
    - feature: "Privacy: no tracking, no third-party SDKs"
      values: ["Zero tracking SDKs, nothing collected", "Standard mobile analytics", "Open source, minimal", "Standard web analytics", "Standard mobile analytics"]
    - feature: "Platforms"
      values: ["iPhone + iPad + Mac (Universal Purchase)", "iPhone + Android", "Web", "Web + mobile apps", "iPhone + Android + web"]
  footnote: "Competitor positioning summarised from each platform's public landing page and store listing on 2026-06-11. Pricing and features change often, so check before switching. If you want ranked play against humans, those platforms are the right tools; Shogiful is for training between those games."

screenshots:
  - src: "/assets/screenshots/shogiful/1.webp"
    caption: "Play a full game on a 3D wooden board against the AI opponent roster."
  - src: "/assets/screenshots/shogiful/2.webp"
    caption: "Dashboard: rating, streak, today's training, and your last game at a glance."
  - src: "/assets/screenshots/shogiful/3.webp"
    caption: "Mistake detail: the engine shows the stronger move and explains it in plain English."
  - src: "/assets/screenshots/shogiful/4.webp"
    caption: "Game review with accuracy, blunders, mistakes and best moves after every game."
  - src: "/assets/screenshots/shogiful/5.webp"
    caption: "Daily training built around your real weaknesses, with adjustable session length."
  - src: "/assets/screenshots/shogiful/6.webp"
    caption: "Progress tracking: estimated rating, accuracy trend, and a per-skill profile."
  - src: "/assets/screenshots/shogiful/7.webp"
    caption: "Play ladder: climb a roster of named AI opponents from novice to expert."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no trackers"
    - "No account or sign-up required"
    - "All analysis runs locally on your device: YaneuraOu, mistake detection, and the coaching explanations"
    - "Works fully offline, with no cloud calls and no server"
    - "Universal Purchase across iPhone, iPad, and Mac via standard Apple infrastructure"

faq:
  - q: "What is Shogiful?"
    a: "Shogiful is a shogi training and game analysis app for iPhone, iPad, and Mac. It analyzes your games with the YaneuraOu engine, explains your mistakes in plain language, and builds training sessions around your real weaknesses across five skill dimensions (tactics, defense, positioning, endgame, and openings), with shogi-specific coaching on drops, promotions, castles, and tsume."
  - q: "Can I play shogi without knowing kanji?"
    a: "Yes, and that is one of the main reasons Shogiful exists. The Western piece set uses symbolic icons with movement indicators, so the board is readable from your first game. A piece guide is one tap away during play, and the app introduces the traditional kanji characters gradually as you train, so you can switch to traditional pieces whenever you feel ready."
  - q: "Is Shogiful good for chess players learning shogi?"
    a: "Yes, that is the player it was made for. Shogi and chess share roots but differ in important ways: captured pieces return to the board as drops, promotion is a real decision instead of an automatic queen, and endgames are attacking races instead of slow simplification. Shogiful's coaching treats these differences as first-class topics. Its mistake categories include drop mistakes, promotion mistakes, castle weaknesses, and missed tsume, none of which exist in a chess trainer."
  - q: "How is Shogiful different from Shogi Wars?"
    a: "Shogi Wars is the dominant online shogi platform: the official Japan Shogi Association app, with live matchmaking and ranked kyu/dan promotion. Shogiful is a single-player training product with no account, no server, and no clock pressure from human opponents. You play AI opponents at your own pace, get every game analyzed with plain-language explanations, and train your specific weaknesses. Many players use both, Shogiful to improve and Shogi Wars to compete."
  - q: "How is Shogiful different from Lishogi or 81Dojo?"
    a: "Lishogi and 81Dojo are online platforms built around playing humans. Lishogi is the free open-source web platform and 81Dojo the long-running international dojo, and both are excellent for matchmaking. Shogiful is offline and focused on coaching: on-device engine analysis explained in sentences, weakness tracking across five skills, and adaptive training with spaced repetition. It's somewhere to practise between tournament games."
  - q: "What engine does Shogiful use?"
    a: "Shogiful uses YaneuraOu, the strongest open-source shogi engine and the foundation of multiple World Computer Shogi Championship winners, with its 61 MB NNUE neural-network evaluation running entirely on your device. Shogiful turns the engine's output into plain-language coaching instead of showing you raw evaluation numbers."
  - q: "How is Shogiful different from PiyoShogi?"
    a: "PiyoShogi is an excellent free app and a common recommendation for beginners, with 40 finely graded AI levels, an analysis function, and daily mate problems. Shogiful focuses on coaching on top of play: every game analyzed with mistakes explained in plain-language sentences, weakness tracking across five skills, spaced-repetition training generated from your own games, and Western piece sets with gradual kanji learning for players who can't read the pieces yet. If you want free play with adjustable difficulty, PiyoShogi is great; if you want coaching from your own games in English, pick Shogiful."
  - q: "Does Shogiful have time controls?"
    a: "No, on purpose. Games against Shogiful's AI opponents are untimed, with no clock and no byoyomi countdown. Take as long as you want on any move, then analyze at the same pace. For timed practice ahead of online play, the online platforms (Shogi Wars, Lishogi, 81Dojo) are the right place."
  - q: "What is tsume-shogi, and does Shogiful include it?"
    a: "Tsume-shogi are shogi's classical checkmate puzzles: every attacking move must be a check, every piece in hand must be used, and the defender plays the longest resistance. Shogiful bundles a verified tsume library running from one-move beginner problems to multi-move calculations, scheduled with spaced repetition alongside exercises generated from your own games."
  - q: "Does Shogiful work offline?"
    a: "Yes, completely. The engine, the analysis, the coaching explanations, the training system, and all 10 AI opponents run on your device. It never needs an internet connection, and there's no account to sign into."
  - q: "Is Shogiful free? What does Premium cost?"
    a: "Shogiful is free to download and play: all 10 AI opponents with unlimited games, 2 full game analyses per day, and 3 training puzzles per day, with no ads and no account. Premium unlocks unlimited analysis, unlimited training, deep multi-line analysis, and the full progress view. Premium is {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once for lifetime access. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does Shogiful need an account?"
    a: "No. Shogiful needs no account, no sign-up, and no personal information. Your games, analysis, and training progress stay on your device. Purchases restore through your Apple ID, which is Apple's mechanism and not a Shogiful account."
  - q: "Can I play against other people in Shogiful?"
    a: "No, by design. Shogiful is a training product with 10 AI opponents in distinct styles, from true beginner to advanced strength, unlocked as you beat them. For ranked human play, Shogi Wars, Lishogi, and 81Dojo are the right tools; Shogiful is meant to make you better before and between those games."
  - q: "Does Shogiful support Japanese?"
    a: "Yes. Shogiful ships in English and Japanese from day one, with JSA-standard shogi terminology in Japanese and both Western and KIF notation styles available."
  - q: "Can I import my games from Shogi Wars or 81Dojo?"
    a: "No. Shogiful doesn't import KIF game records, the format both platforms export. It analyses the games you play in the app and builds your weakness profile from those."

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
about_heading: "What Shogiful does: shogi training, analysis, and a board you can read"

ratings:
  value: "3.4"
  count: 18
  last_synced: "2026-10-22"
related_apps: ["xiangqiful", "chessful"]
last_updated: 2026-10-29
---
Shogiful is a [shogi training & analysis app for iPhone, iPad, and Mac](#features). Shogi is the Japanese form of chess, played on a 9×9 board where captured pieces return to play. The app starts from a simple observation: outside Japan, the biggest barrier to shogi is the kanji on the pieces more than the rules. Shogiful ships [Western piece sets with movement indicators](#features) so the board is readable from your first game ([the design story is in the journal](/journal/making-shogi-readable-without-kanji/)), and adds what improving players need most: a real engine that reviews every move and explains mistakes in sentences instead of evaluation numbers.

The engine is [YaneuraOu](https://github.com/yaneurao/YaneuraOu), the strongest open-source shogi engine, running entirely on-device with its 61 MB NNUE neural network. After each game, Shogiful classifies every significant mistake into shogi-specific categories (missed drop tactics, wrong promotion decisions, castle weaknesses, missed tsume) and turns each one into [plain-language coaching](#templates). The categories were written for shogi from scratch. Drops and promotions are where chess players lose shogi games, and generic chess-style training never covers them.

From the analysis, Shogiful [builds an adaptive training queue](#how-it-works): exercises taken from your own games, mixed with a verified tsume-shogi puzzle library and scheduled with spaced repetition across five tracked skills (tactics, defense, positioning, endgame, and openings). Ten AI opponents across four tiers give you someone to play at every level, from a true beginner who blunders honestly to an advanced opponent who punishes loose castles.

Everything runs on your device. There is no cloud, no account, no daily quota from a server, and no ads. The trade-off is that Shogiful has no online play against humans; for that, Shogi Wars, Lishogi, and 81Dojo remain the right tools, and the [side-by-side comparison](#compare-heading-shogiful) says so plainly. For the full category, including PiyoShogi and the classic offline apps, see [our honest guide to the best shogi apps for iPhone](/guides/best-shogi-apps-iphone/).

Free tier: all 10 opponents with unlimited games, 2 game analyses per day, and 3 training puzzles per day. Premium adds unlimited analysis and training, deep multi-line analysis, and the full progress view for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once for [lifetime](/apps/shogiful/#pricing). [No tracking, no ads, no account](/apps/shogiful/privacy/). Its siblings use the same play, analyze, and train loop: [Chessful](/apps/chessful/) for Western chess and [Xiangqiful](/apps/xiangqiful/) for xiangqi (Chinese chess). Published by Lagerland Apps, an independent Apple developer in Finland.
