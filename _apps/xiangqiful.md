---
layout: app
slug: xiangqiful
name: "Xiangqiful"
tagline: "Master xiangqi. Move by move."

# Live since 2026-09-30 (v1.0). Facts are checked against the app's source
# (~/Downloads/Xiangqi, main) and the live en-US listing; Docs/ASO_STRATEGY.md §4
# maps every listing claim to its source. Copy rules from that table: 902 mate
# problems (most from eight classical manuals — never "all original"), "more
# than 30 languages" (40 localizations of 33 languages), no per-game evaluation
# graph (Review shows an advantage bar), no Dynamic Type claim, no achievement
# count, and only the four detected pattern names (screenless cannon, trapped
# horse, broken advisors, Iron Bolt) when naming mistakes.
status: live

quick_answer: "Xiangqiful is a xiangqi (Chinese chess) training and game-analysis app for iPhone, iPad and Mac. You play ten AI opponents with distinct styles, from strength 400 to 1900. Afterwards Pikafish — the open-source engine that tops the computer-xiangqi rating lists — reviews every move on your device, grades it, names each mistake in xiangqi's own terms (a screenless cannon, a trapped horse, broken advisors, a missed Iron Bolt mate) and builds your next training session from what you missed. It includes 80 free lessons in 8 tracks, 902 mate problems — most from eight classical manuals — and more than 150 drills, and three piece sets — traditional characters, western symbols or a hybrid of both — so you can play without reading Chinese. Free, with Premium at $1.99/month or $9.99/year (each with a one-week free trial) or $19.99 once. Fully offline, no account, no ads, no data collected."

category: games
platforms: ["iOS", "iPadOS", "macOS"]

app_store_url: "https://apps.apple.com/app/id6794340136"

price:
  model: freemium
  value: "Free — Premium from $1.99/mo"
price_currency: "USD"
schema_price: "0"
schema_high_price: "19.99"
schema_offer_count: "4"

plans_footnote: "Prices in USD; the App Store shows your local price at checkout. Monthly and Yearly each start with a one-week free trial for new subscribers; cancel before it ends and you are not charged. They renew automatically unless turned off at least 24 hours before the current period ends — manage or cancel them in your Apple Account settings. Lifetime is a one-time purchase with nothing to renew. One purchase covers iPhone, iPad and Mac. Refunds are handled by Apple through the standard App Store refund flow."

# Free / Monthly / Yearly / Lifetime — the Shogiful ladder. The Free column
# lists only limits the app enforces (Core/Persistence/*Quota.swift,
# Store/PaywallBenefit.swift, Core/Domain/DrillAccessPolicy.swift): lessons and
# the assessment are uncapped; the first drill set of every module is free and
# the rest are Premium (since 2026-09-26); mate problems count toward the 3
# puzzles a day. Both subscriptions carry a one-week free trial (live in ASC).
# "Best value" is the badge the in-app paywall puts on Yearly.
plans:
  - name: "Free"
    price: "$0"
    summary: "Every opponent, every lesson, and a daily taste of the engine."
    features:
      - "Unlimited games against all 10 opponents"
      - "2 full game analyses a day, every mistake named and explained"
      - "3 training puzzles a day, mate problems included"
      - "2 in-game coach hints a day"
      - "All 80 lessons and the skill assessment — no daily cap"
      - "The first drill set in every one of the nine drill modules"
      - "All three piece sets and the 3D board, offline, no account"
  - name: "Premium · Monthly"
    price: "$1.99/mo"
    summary: "Full Premium, billed monthly, after a one-week free trial. Cancel anytime."
    features:
      - "One-week free trial for new subscribers"
      - "Unlimited game analysis"
      - "Unlimited training puzzles, mate problems included"
      - "Every drill in every module"
      - "Unlimited in-game coach hints"
      - "Deep multi-line engine analysis in Game Review"
      - "The full progress dashboard: skill radar, weakness trends and this week against last"
  - name: "Premium · Yearly"
    price: "$9.99/yr"
    summary: "The same Premium, billed once a year after a one-week free trial — about 58% less than paying monthly."
    features:
      - "Everything in Premium · Monthly, including the one-week free trial"
      - "About 58% less than twelve months of Monthly"
      - "Cancel anytime in your Apple Account settings before it renews"
    highlight_label: "Best value"
  - name: "Lifetime"
    price: "$19.99 once"
    summary: "All of Premium for about ten months of Monthly — then yours for good."
    features:
      - "Everything in Premium"
      - "One-time purchase — nothing to renew, nothing to cancel"
      - "One purchase for iPhone, iPad and Mac"
      - "Restores on every device signed in to the same Apple Account"

icon: "/assets/icons/xiangqiful.png"
og_image: "/assets/og/xiangqiful.png"

seo:
  title: "Xiangqi (Chinese Chess) App for iPhone & Mac | Xiangqiful"
  description: "Learn xiangqi (Chinese chess) on iPhone, iPad and Mac. Pikafish reviews every move on-device and explains your mistakes. Western pieces, offline, no ads."
  keywords:
    - "xiangqi app"
    - "chinese chess app"
    - "learn xiangqi"
    - "xiangqi for beginners"
    - "chinese chess offline"
    - "xiangqi engine analysis"
    - "xiangqi puzzles"
    - "pikafish iphone"

hero:
  pre_headline: "Xiangqi (Chinese chess) training & analysis app for iPhone, iPad and Mac"
  headline: "Chinese chess, taught properly."
  secondary: "Play a game, and the engine reads it back to you — move by move."
  subheadline: "Ten teahouse opponents with real personalities, from a park grandmother who never leaves her palace to Shīfu, the master at the top of the ladder. After every game, Pikafish reviews your moves on your device, names what went wrong in xiangqi's own terms and turns the moves you missed into tomorrow's training. Can't read the characters yet? Start with western symbols. Free, with Premium from $1.99/month."
  cta_label: "Download Free"
  cta_subline: "Free download · all 10 opponents and 80 lessons free · no ads · no account · works offline"
  alt: "Xiangqiful on iPhone — a game against Shīfu, strength 1,900, on the 3D board with traditional wooden discs, red to move"

screenshots:
  - src: "/assets/screenshots/xiangqiful/1.png"
    caption: "Playing Shīfu, the master at the top of the ladder, on the optional 3D board with classic wooden discs."
  - src: "/assets/screenshots/xiangqiful/2.png"
    caption: "80 lessons in 8 tracks, from the board and the two ways a game ends to the classical studies — all free."
  - src: "/assets/screenshots/xiangqiful/3.png"
    caption: "The hybrid piece set: each western symbol sits on its Chinese character, so you can play now and learn the characters as you go."
  - src: "/assets/screenshots/xiangqiful/4.png"
    caption: "Game Review: every move graded, accuracy for both sides, and the moments worth replaying — here, most often a missed tactic."
  - src: "/assets/screenshots/xiangqiful/5.png"
    caption: "A mate problem in progress: Piercing the Heart, mate in 3, where every move must give check."
  - src: "/assets/screenshots/xiangqiful/6.png"
    caption: "Today's training: a session built from your own mistakes — a missed pin, a palace weakness, then mixed practice."
  - src: "/assets/screenshots/xiangqiful/7.png"
    caption: "The ten opponents, by tier — from Xiǎobǎo, the kid who just learned the moves, upward. Beat one twice and the next sits down."
  - src: "/assets/screenshots/xiangqiful/8.png"
    caption: "Progress: Xiangqiful's own estimated rating, accuracy over time and the five-axis skill profile."
  - src: "/assets/screenshots/xiangqiful/9.png"
    caption: "Home: today's training, and the mistake costing you the most right now."

who_for:
  - "You play chess and are curious about xiangqi, but the characters on the pieces stopped you before your first game"
  - "You grew up with xiangqi — or cờ tướng — and want an engine to go through your own games with you, without ads or an online account"
  - "You want your mistakes explained in words (the horse you left with nowhere to go, the screen you handed a cannon), not as bare evaluation numbers"
  - "You like structure: lessons, drills and mate problems chosen from your own weaknesses, not an endless stream of random games"
  - "You play offline and at your own pace — on flights, on the commute, with no clock"
  - "You want one purchase to cover iPhone, iPad and Mac"

who_not_for:
  - "You want to play other people — Xiangqiful has no multiplayer, on purpose"
  - "You want a database of master games or an opening explorer — not in this version"
  - "You need your progress to sync between devices — this version keeps it on the device you play on"
  - "You're on Android or Windows — Xiangqiful needs iOS 18, iPadOS 18 or macOS 15 or later"
  - "You're looking for janggi (Korean chess) — a different game with its own rules"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "For the player who can't read the pieces yet — and the one who has played all their life."
  story: "Xiangqi is one of the most played board games in the world, and outside Asia almost nobody gets past the first look: thirty-two wooden discs, each painted with a Chinese character. The apps that dominate the game assume you can already read them, and they drop you into online games against strangers on day one. Xiangqiful was built the other way round, as the third sibling of Chessful and Shogiful. Symbols come first and the characters follow when you're ready. The ten opponents play like people rather than a dialled-down engine. And a real engine, Pikafish, goes through every game with you on your own device. Its verdicts come in the words a teahouse master would use — the horse with nowhere left to go, the cannon that lost its screen, the advisors broken too early — and then they become your next training session. Nothing runs on a server. There is no account to make and nothing to collect."
  signals:
    - "Pikafish runs on your device with its 53 MB neural network — no cloud analysis, no account, no server quota"
    - "Mistake detection written for xiangqi, not ported from chess: screenless cannons, trapped horses, broken advisors, the flying-general rule and stalemate-as-a-loss are all first-class"
    - "902 mate problems, most from eight classical manuals — every line re-checked by the app's own solver, and book problems that don't hold up left out"
    - "More than 30 languages and VoiceOver from the first release"
    - "No ads, no analytics, no tracking SDKs — the only outside code is the open-source Pikafish engine (GPL-3), compiled into the app"
  external_link:
    label: "Read the Lagerland studio backstory →"
    href: "/lagerland-apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally — usually within a day."

value_points:
  - title: "Play xiangqi without reading Chinese"
    description: "Three piece sets: traditional characters, western symbols, and a hybrid that carries both. Touch any piece to see how it moves. The lessons introduce the characters one piece at a time, so you can switch to the traditional set when you're ready — or never."
  - title: "Find out why you lost"
    description: "After every game Pikafish grades each move from best to blunder, gives both sides an accuracy score, and explains the key moments in sentences: the horse you left with no way out, the screen you handed an enemy cannon, the mate you walked past."
  - title: "Train what your games actually show"
    description: "Every mistake feeds a five-part skill profile — tactics, defense, positioning, endgame, openings. Your daily plan draws on the weakest parts, and spaced repetition brings each pattern back just before you would forget it."
  - title: "Offline, private, no account"
    description: "The engine, the analysis, the lessons and all ten opponents run on your device. No account, no server, no ads, no tracking — it plays the same in airplane mode."

features:
  - title: "Ten teahouse opponents"
    description: "Xiǎobǎo learned the rules last month. Nǎinai Chén has watched games in the park for forty years and never leaves her palace. Shuāngpào stacks both cannons on one file, Qiūyuè trades her way into won endgames, and Shīfu, at the top, simply plays well. Ten personalities from strength 400 to 1900, each with strengths and weaknesses you can learn to exploit. They play styles, not a weakened engine — and each one opens the next when you beat it twice."
  - title: "Analysis you can actually read"
    description: "Pikafish grades every move on seven steps — best, great, good, book, inaccuracy, mistake, blunder — with an accuracy score for both sides, an advantage bar for every position and the key moments of the game. Each mistake comes with the better move, a line to play through on the board and one thing to do differently next game. Premium adds deep multi-line analysis when you want to argue with the engine."
  - title: "Mistakes named in xiangqi's own language"
    description: "Screenless cannons, trapped horses, buried chariots, broken advisors, palace breaches, the initiative quietly handed over — and the classical mating patterns by name: the Iron Bolt, Heaven-and-Earth Cannons, Palace Suffocation, Piercing the Heart. The taxonomy was written for xiangqi, not ported from chess."
  - title: "80 lessons in 8 tracks"
    description: "Fundamentals, Openings, Palace Defense, Cannon Tactics, Horse Technique, Middlegame, Endgame and Advanced. The lesson every chess player needs first: in xiangqi, having no legal move is a loss, not a draw. The Advanced track walks classical studies — a trap from the Juzhongmi manual, a line from the Meihua Pu, and the Seven Stars endgame."
  - title: "902 mate problems and 150-plus drills"
    description: "902 consecutive-check mate problems — xiangqi's native puzzle, where every move must give check — from mate in 1 to mate in 7. Most come from eight classical manuals such as the Shiqing Yaqu of 1570; every line is re-checked by the app's own solver, and any book problem that does not really work is left out. Nine drill modules: Mate Trail, Cannon Range, Horse Trails, Opening Lab (ten opening families), Palace Workshop, Endgame Studio, Tactics Yard, Tactic Cards, and Handicap House, where you play a real game against an opponent who starts a horse, two horses or a chariot down — or simply hands you the first move. The first drill set in every module is free."
  - title: "A board you can read"
    description: "Traditional, western or hybrid pieces; traditional or simplified characters; WXF or Chinese notation; a boxwood or rosewood board; coordinates on or off. Live games can be played on a 3D board with a carved set or classic discs, while review and training use the clear 2D board."
  - title: "Progress and a skill profile"
    description: "An estimated rating from your analyzed games, accuracy over time, a five-axis skill profile and weakness trends that show what to work on this week — and whether it's working. A 15-position assessment gives you a starting point. Premium unlocks the full dashboard."
  - title: "iPhone, iPad and Mac"
    description: "Native on all three, with one purchase. The Mac version adds menu commands and keyboard shortcuts — new game, flip board, analyze, copy the position as FEN. Import games as ICCS or WXF movetext and analyze them too. More than 30 languages, VoiceOver throughout, and Game Center leaderboards and achievements if you want them."

# Methodology disclosure — emits HowTo schema via _layouts/app.html. Grading is
# BLUEPRINT §9.2 (expected-score cost, curve fitted on 300 games); the plan split
# is Training/DailyPlanGenerator.swift.
how_it_works:
  heading: "From your last move to tomorrow's training."
  intro: "The coaching loop is where Xiangqiful does its teaching. Here is exactly what happens between the end of a game and your next training session."
  steps:
    - title: "Pikafish reviews every move"
      detail: "When a game ends, tap Analyze. Pikafish goes through the whole game on your device, position by position, with its 53 MB NNUE neural network — no cloud call and no account. Free players get two full analyses a day; Premium is unlimited, and its deep multi-line analysis shows the alternatives you didn't consider."
    - title: "Each move is graded by what it cost you"
      detail: "A move is charged the share of its expected result that it gave away, not raw centipawns, and placed on a seven-step scale from best to blunder. The curve behind that was fitted on 300 xiangqi games across the whole opponent ladder. It is why a slip in an already-won position is not called a blunder while a soldier thrown away in a level game is noticed, and why a mate you had and let go is always flagged. Your accuracy for the game comes from the same number."
    - title: "Mistakes are named in xiangqi terms"
      detail: "Each significant mistake is classified — missed mate, missed cannon tactic, missed fork, pin or skewer, hanging piece, trapped piece, palace weakness, exposed general, passive move, opening inaccuracy or endgame error — and tagged with the pattern behind it: a screenless cannon, a buried chariot, broken advisors, a palace breach, or a classical mate such as the Iron Bolt."
    - title: "Explained the way a teacher would"
      detail: "Each one becomes a short explanation with the better move, a line you can play through on the board, and one concrete thing to do differently in your next game."
    - title: "Your weaknesses become the plan"
      detail: "Mistakes feed five skills — tactics, defense, positioning, endgame and openings — and your weakness trends. Today's plan spends about 60% of its exercises on one of your top weaknesses, 25% on the next and 15% on mixed practice, rotating the focus day by day so you meet your second and third weaknesses too. Spaced repetition (SM-2) brings each pattern back just before you would forget it."
    - title: "Progress you can watch"
      detail: "Your estimated rating, accuracy trend and skill profile update after every analyzed game and training session, and the weakness trends show whether each mistake is receding or creeping back. The rating is Xiangqiful's own estimate from your analyzed games, not an official or federation rating."

# Example coaching — each card is assembled from the app's own English strings
# (Localizable.xcstrings: pattern.* details, mistake.* bodies and tips).
example_insights:
  overline: "What Xiangqiful explains"
  heading: "What a xiangqi mistake looks like, explained."
  intro: "Six examples of what Xiangqiful shows in Game Review, in the app's own words. Each names what happened, says why it matters in xiangqi specifically, and ends with something to do in your next game."
  cards:
    - tag: "Tactics · Screen tactic"
      headline: "Your horse stepped into the line and handed the enemy cannon the screen it needed."
      body: "A cannon can only capture by jumping exactly one piece, so every cannon tactic is really about the piece in between. Adding a screen turns a quiet cannon into a threat; removing one defuses it. Before moving anything else, check what the cannons would hit if one piece moved."
    - tag: "Tactics · Missed mate"
      headline: "The middle cannon holds the file while the chariot bars the palace gate — the Iron Bolt, mate in 3."
      body: "A forced sequence ends the game whatever your opponent does, and once one exists nothing else on the board matters. Mating patterns repeat: a handful of shapes finish most games. When the enemy general is short of advisors, exhaust the forcing moves before playing anything quiet."
    - tag: "Positioning · Trapped piece"
      headline: "Your horse has no square left that it can safely reach."
      body: "A horse blocked at the leg, or a cannon with nothing left to jump over, is material you own but cannot use. Xiangqi pieces are slower than they look, and a badly placed one rarely recovers. Next game, before advancing a horse, count the intersections it can leave from."
    - tag: "Defense · Palace weakness"
      headline: "Stepping the advisor off its post left the palace one wall short."
      body: "Two advisors and two elephants are the walls of the fortress, and an advisor's worth is not its material value: a general behind two of them cannot be mated by half the standard patterns. Move an advisor or elephant only after counting what it stops defending."
    - tag: "Positioning · Passive move"
      headline: "That move asked nothing of your opponent."
      body: "Xiangqi rewards whoever is asking the questions. Losing the initiative hands your opponent a free move to improve their worst piece, and over several such moves a level position quietly becomes a worse one. Prefer a move that creates a threat over one that merely improves a piece."
    - tag: "Endgame · Endgame error"
      headline: "The endgame technique slipped."
      body: "Xiangqi endgames are a codified science: the result of most material balances is known exactly, so the winning method is a matter of knowledge rather than calculation. And in the endgame the horse outweighs the cannon — screens are scarce once the board empties."

# Kanban blueprint stubs in the app repo — ideas, not commitments, so no dates.
# The 1.0 rows (shipped 2026-09-30) carry no `status: shipped`: that style
# strikes the row through. Each detail starts with a space because app.html
# joins <strong>title</strong><span>detail</span> with no whitespace.
alternatives_to:
  - "Xiangqi.com"
  - "PyChess"
  - "Club Xiangqi"
  - "PlayOK"
  - "Chinese Chess - Best XiangQi"

# Side-by-side comparison — auto-triggers the mid-page CTA and the alt-strip.
comparison_table:
  intro: "Every row is a question a xiangqi-curious player asks before installing an app. Xiangqi.com is the English-language online platform; PyChess is the free open-source web platform; Club Xiangqi is the bilingual English/Vietnamese online club; Chinese Chess - Best XiangQi is a popular free offline opponent. Xiangqiful is a single-player training app. Summarised from each app's public listing on 2026-10-01."
  competitors: ["Xiangqiful", "Xiangqi.com", "PyChess", "Club Xiangqi", "Chinese Chess - Best XiangQi"]
  rows:
    - feature: "Fully offline (no internet required)"
      values: ["Yes — Pikafish runs on-device", "Offline mode vs computer; online features need a connection", "No — web platform", "No — web club", "Yes"]
    - feature: "Account required"
      values: ["No account ever", "Account-based online service", "Sign-in via Lichess, Lishogi, Google or Discord", "Free account (resets after 4 months idle)", "No"]
    - feature: "Engine review of your games"
      values: ["Pikafish — every move graded on 7 steps", "In-app engine analysis (Pikafish credited)", "Fairy-Stockfish analysis", "Not a listed feature", "Hints during play"]
    - feature: "Mistakes named in xiangqi terms"
      values: ["Yes — screenless cannon, trapped horse, broken advisors, missed mates", "Not a listed feature", "No — engine lines", "No", "No"]
    - feature: "Live play against people"
      values: ["No (intentional)", "Yes", "Yes — free", "Yes — novice to master", "No"]
    - feature: "Price"
      values: ["Free; $1.99/mo or $9.99/yr (1-week trial), or $19.99 lifetime", "Free; optional ad-free subscription", "Free, donation-funded", "Free; optional paid membership", "Free, no IAP; ad tracking"]
  footnote: "Competitor positioning summarised from each platform's public listing or site on 2026-10-01. Pricing and features change — verify before switching. If you want to play people, those platforms are the right tools; Xiangqiful is the training companion, not the arena."

roadmap:
  overline: "Roadmap"
  heading: "What shipped in 1.0, and what's being considered."
  intro: "Xiangqiful 1.0, released on 30 September 2026, covers play, engine analysis and training on iPhone, iPad and Mac. Beyond it, these are the ideas on the list. There are no dates, because an honest list is better than a slipped promise."
  items:
    - when: "Version 1.0"
      title: "Ten opponents, on-device Pikafish analysis, plain-language coaching."
      detail: " Every move graded and every key mistake explained in xiangqi's own terms, on your device, with no account."
    - when: "Version 1.0"
      title: "80 lessons, 902 mate problems, 150+ drills and spaced repetition."
      detail: " Eight lesson tracks, nine drill modules and a daily plan built from your own weaknesses."
    - when: "Version 1.0"
      title: "Three piece sets, a 3D board and more than 30 languages."
      detail: " Traditional, western and hybrid pieces, WXF and Chinese notation, and native apps for iPhone, iPad and Mac."
    - when: "Under consideration"
      title: "Opening explorer and repertoire builder."
      detail: " Build and drill your own opening lines on top of the Opening Lab's ten families."
    - when: "Under consideration"
      title: "A longer opponent ladder and an endgame classics library."
      detail: " More opponents between the existing rungs, and more of the classical endgame studies the Advanced track starts on."
    - when: "Under consideration"
      title: "XQF import, iCloud sync and widgets."
      detail: " Bringing in game records in the XQF format, syncing progress between your own devices, and training reminders on the Home Screen."
  disclaimer: "Roadmap last reviewed 2026-10-01. Items under consideration are ideas, not commitments."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  app_privacy_label: "Apple's App Store privacy label for Xiangqiful reads “Data Not Collected.” The app requests no tracking (no IDFA), links no advertising or analytics SDKs, and has no networking code of its own; its Privacy Manifest declares NSPrivacyTracking false and no collected data types."
  notes:
    - "No account, no server, and no networking code of its own"
    - "Pikafish, the analysis and the coaching all run on your device"
    - "Games, analysis and training progress are stored only on your device"
    - "No analytics, advertising or tracking SDKs"
    - "No permission prompts: no camera, photos, microphone, location or contacts"
    - "Purchases are handled by Apple; Game Center is used only if you are already signed in to it"
  policy_url: "/apps/xiangqiful/privacy/"

faq:
  - q: "What is Xiangqiful?"
    a: "Xiangqiful is a xiangqi (Chinese chess) app for iPhone, iPad and Mac built around one loop: play, find out why, train. You play ten AI opponents with distinct styles; afterwards the Pikafish engine reviews every move on your device, grades it, explains the key mistakes in plain language, and builds your next training session from what you missed. It also includes 80 lessons in 8 tracks, 902 mate problems and more than 150 drills. There is no account, no ads, and it works completely offline."
  - q: "What is xiangqi, and how is it different from chess?"
    a: "Xiangqi is the traditional Chinese form of chess, played across China, in Vietnam as cờ tướng, and throughout the Chinese diaspora. The pieces stand on the intersections of a 9×10 grid rather than in squares, a river splits the board, and each general is confined to a 3×3 palace with its two advisors. Several pieces catch chess players out: the cannon moves like a rook but can only capture by jumping exactly one piece, the horse can be blocked at the leg, elephants cannot cross the river, and the two generals may never face each other on an open file. Most surprising of all, a player with no legal move loses — stalemate is a loss, not a draw — and perpetual check loses for the side giving it."
  - q: "Can I play without reading Chinese characters?"
    a: "Yes — that is one of the main reasons Xiangqiful exists. Choose the western set, which uses symbols, or the hybrid set, which shows each symbol together with its character so you learn them as you play. Touch any piece to see how it moves. The lessons introduce the characters one piece at a time, and you can switch to the traditional set whenever you're ready."
  - q: "Is Xiangqiful good for complete beginners?"
    a: "Yes. The Fundamentals track starts with the board, the pieces and the two ways a game ends, and the app explains the rules that surprise newcomers the first time they happen in your game — your first stalemate, your first perpetual check. The two opponents at the bottom of the ladder play like real beginners. If you already play, the 15-position skill assessment gives you a starting rating instead."
  - q: "What engine does Xiangqiful use?"
    a: "Pikafish — the open-source xiangqi engine, derived from Stockfish, that tops the computer-xiangqi rating lists. It runs entirely on your device with its 53 MB NNUE neural network: no cloud, no account and no server quota. Xiangqiful turns its output into graded moves and plain-language explanations instead of showing you raw evaluation numbers. Pikafish is licensed under the GPL-3; the Licences screen in Settings names it and links to the project."
  - q: "How strong are the opponents?"
    a: "The ten opponents run from strength 400 to 1900 across four tiers — Novice, Beginner, Intermediate and Advanced. The numbers are Xiangqiful's own scale, not an Elo rating from any federation. Each plays a style rather than a weakened copy of the engine: Ā Fú grabs everything, Chūnhuā pushes her soldiers over the river, Tiěmǎ routes his horses to outposts, Shuāngpào stacks his cannons, Qiūyuè trades into won endings, and Shīfu simply plays well. The first two are open from the start; beat an opponent twice and the next one sits down. Games are untimed, and you can play Red, Black or a random side."
  - q: "Can I play against other people?"
    a: "No — by design. Xiangqiful is a single-player training app: no accounts, no servers, no matchmaking. It is meant to make you better between the games you play with people, whether that is at a club, online or in the park."
  - q: "Does Xiangqiful work offline?"
    a: "Yes, completely. The engine, the analysis, the lessons, the puzzles and all ten opponents run on your device, so it plays the same in airplane mode. A connection is needed only for things Apple handles: buying or restoring Premium, and Game Center if you use it."
  - q: "Is Xiangqiful free? What does Premium cost?"
    a: "Xiangqiful is free to download, and the free tier has no time limit: unlimited games against all ten opponents, all 80 lessons, the skill assessment, the first drill set in every drill module, 2 full game analyses a day, 3 training puzzles a day (mate problems included) and 2 in-game coach hints a day. Premium removes the daily limits, opens every drill in every module, and adds deep multi-line analysis and the full progress dashboard. It costs $1.99 a month or $9.99 a year — each with a one-week free trial for new subscribers — or $19.99 once for lifetime access. Prices are in USD; the App Store shows your local price. There are no ads in either tier."
  - q: "Where do the mate problems come from?"
    a: "There are 902 of them, from mate in 1 to mate in 7, and every one is a consecutive-check problem: each attacking move must give check. 194 were composed for Xiangqiful; most of the rest come from eight classical manuals, among them the Shiqing Yaqu of 1570 and the Juzhongmi, and the source is recorded on every problem. Every line was re-checked by the app's own solver, and the books were not corrected to make a problem fit — a book problem that does not really work was left out."
  - q: "What are the tips in Settings?"
    a: "Optional ways to support the app's development — Buy a coffee, Supporter and Huge support. They unlock nothing, because Premium already includes every feature. They are one-time purchases handled by Apple."
  - q: "Can I analyze games I played somewhere else?"
    a: "Yes. Import a game from a file, or paste it from the clipboard, as ICCS (H2-E2) or WXF (C2=5) movetext — from the standard start or from a set position — and analyze it like any other game. Other formats such as XQF are not supported in this version. You can also share or copy any game record, and on the Mac copy the current position as FEN."
  - q: "Which rules does Xiangqiful use for draws and repetition?"
    a: "Checkmate wins, and so does stalemate: having no legal move is a loss in xiangqi. If a position repeats three times, the side that gave check on every move of the cycle loses; if both sides were checking, or neither was, the game is drawn. Sixty moves without a capture is also a draw. This is a simplified form of the official repetition rules — the full rules on perpetual chasing are not adjudicated in this version."
  - q: "Does it support Chinese notation and simplified characters?"
    a: "Yes. Moves can be shown in WXF notation (C2=5) or in Chinese notation, and the pieces can carry traditional or simplified characters. Changing the notation relabels the games you have already played. The app is translated into more than 30 languages, including Simplified and Traditional Chinese, Vietnamese, Japanese, Korean and Thai."
  - q: "Does my progress sync between iPhone, iPad and Mac?"
    a: "Not in this version. Your games, analysis and training progress are stored on the device you use, and there is no account or server to sync through. Premium itself belongs to your Apple Account, so one purchase unlocks Xiangqiful on your iPhone, iPad and Mac — use Restore purchases on each device."
  - q: "Does Xiangqiful use Game Center?"
    a: "Only if you want it to. Xiangqiful never asks you to sign in. If you are already signed in to Game Center on your device, your results feed eight leaderboards — estimated rating, best game accuracy, accuracy this week, longest win streak, opponents defeated, training streak, puzzles solved and overall skill — and its achievements. The app keeps its own achievement gallery either way, and it never reads anything back from Game Center, so playing without it costs you nothing."
  - q: "Is Xiangqiful accessible?"
    a: "Yes. The board works with VoiceOver, which names every intersection and every piece, and right-to-left languages such as Arabic and Hebrew are laid out correctly. The app is available in more than 30 languages."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/xiangqiful/support/"

release:
  first_release: "2026-09-30"
  last_updated: "2026-10-01"
  version: "1.0"

related_apps: ["shogiful", "chessful"]

related_journal:
  slug: "xiangqi-mate-problems-from-classical-manuals"
  anchor: "902 xiangqi mate problems, eight old books — and the ones I left out"

show_body: true
about_heading: "What Xiangqiful is — xiangqi training, analysis, and a board you can read"
---
Xiangqiful is a [xiangqi training and analysis app for iPhone, iPad and Mac](#features). Xiangqi is Chinese chess: two armies of sixteen pieces on the intersections of a nine-by-ten board, a river across the middle, and a palace at each end that the generals may never leave. It is one of the most played board games in the world, and outside Asia most people bounce off it at first sight, because every piece is a Chinese character painted on a wooden disc.

Xiangqiful starts there. It ships three piece sets — **traditional characters, western symbols, and a hybrid that carries both** — with a movement guide on every piece you touch, and its lessons introduce the characters one piece at a time. Switch whenever you like, or never.

Then it does what an improving player actually needs: a real engine going through your games with you. [Pikafish](https://github.com/official-pikafish/Pikafish), the open-source engine that tops the computer-xiangqi rating lists, runs entirely on your device. After each game it grades every move on a seven-step scale, and the key moments are [explained in xiangqi's own terms](#insights): the horse you left with nowhere to go, the cannon you handed a screen, the advisors you broke up, the mate you walked past. Those mistakes feed a five-part skill profile, and [your daily training is built from the weakest parts](#how-it-works) — drills, mate problems (902 of them, most from the classical manuals) and reviews scheduled by spaced repetition.

Ten opponents give you someone to play at every level, from strength 400 to 1900: a kid who has just learned the moves, a park grandmother who never leaves her palace, a cannon fanatic, an endgame grinder, and Shīfu, the master at the top. They play styles, not a weakened engine, and each one opens the next when you beat it twice.

Everything runs on your device. There is no account, no server, no ads and nothing collected; the [privacy policy](/apps/xiangqiful/privacy/) sets out what stays on your device and what Apple handles instead. The trade-off is that there is no online play: Xiangqiful is the practice room, not the arena. If you also play Japanese or Western chess, [Shogiful](/apps/shogiful/) and [Chessful](/apps/chessful/) are built on the same loop.

Free: all ten opponents with unlimited games, all 80 lessons, the first drill set in every module, plus two game analyses, three training puzzles and two coach hints a day. Premium lifts the daily limits, opens every drill, and adds deep multi-line analysis and the full progress dashboard — $1.99 a month or $9.99 a year, each after a one-week free trial, or $19.99 once. Published by Lagerland Apps, an independent Apple developer in Finland.
