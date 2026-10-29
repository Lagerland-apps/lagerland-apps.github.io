---
layout: app
slug: xiangqiful
name: "Xiangqiful"
tagline: "Learn Chinese chess from your first move, then play, review, and train."

# Live since 2026-09-30. Copy rebuilt on 2026-10-29 from APP_BLUEPRINT.md in the
# app's source folder (verified against code 2026-10-29, v1.1.6); §10 is the only
# claims source. Rules from it: 40 opponents in 8 tiers, the first 10 free; moves
# graded "from best to blunder" (no step count); "a strong open-source engine",
# never "tops the rating lists"; no engine file size; no "movement guide" wording;
# "VoiceOver support", never "throughout"; no Dynamic Type, light mode, sound,
# sync claims; the rating is Xiangqiful's own estimate. Family Sharing on Monthly,
# Yearly, and Lifetime comes from MASTER.md (2026-10-29), which beats the blueprint.
status: live

quick_answer: "Xiangqiful is a xiangqi (Chinese chess) app for iPhone, iPad, and Mac that teaches you from your first move, then has the Pikafish engine review your games on your device and builds your training from the mistakes it finds. It has 80 free lessons, 902 mate puzzles (708 of them from eight classical manuals), and 40 opponents with distinct play styles, and its western and hybrid piece sets let you play before you can read the characters. The free tier includes the first 10 opponents and 2 game analyses, 3 puzzles, and 2 coach hints a day; Premium is {P_MONTHLY}/month or {P_YEARLY}/year, each with a {TRIAL}, or {P_LIFETIME} once. It works offline and needs no account, and the app shows no ads and collects no data."

category: games

app_store_url: "https://apps.apple.com/app/id6794340136"

price:
  model: freemium

plans_footnote: "Prices in USD; the App Store shows your local price at checkout. Monthly and Yearly each start with a {TRIAL} for new subscribers; cancel before it ends and you are not charged. They renew automatically unless turned off at least 24 hours before the current period ends; manage or cancel them in your Apple Account settings. Lifetime is a one-time purchase with nothing to renew. Monthly, Yearly, and Lifetime all support Family Sharing. Apple handles refunds through the standard App Store refund flow."

# Free / Monthly / Yearly / Lifetime. The Free column lists only the limits in
# blueprint §3 (2 analyses, 3 puzzles, 2 coach hints a day; first 10 opponents;
# first drill bank of each module). Lessons and the assessment are uncapped.
# "Best value" is the badge the in-app paywall puts on Yearly.
plans:
  - name: "Free"
    price: "$0"
    summary: "Every lesson, the first ten opponents, and a daily allowance of engine review."
    features:
      - "All 80 lessons and the 15-position skill assessment"
      - "Unlimited games against the first 10 of the 40 opponents"
      - "2 game analyses a day, each mistake named in xiangqi terms"
      - "3 training puzzles a day, mate puzzles included"
      - "2 in-game coach hints a day"
      - "The first drill set in each of the nine drill modules"
      - "Estimated rating, game import, the 3D board, and Game Center"
  - name: "Premium · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Premium, billed monthly after a {TRIAL}. Cancel anytime."
    features:
      - "All 40 opponents, open at once"
      - "Unlimited game analysis, with deep multi-line engine analysis"
      - "Unlimited training puzzles and coach hints"
      - "Every drill in every module, including the 30 Classical Studies"
      - "Skill profile, weakness trends, and this week against last"
      - "{TRIAL} for new subscribers"
  - name: "Premium · Yearly"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "The same Premium, billed once a year after a {TRIAL}. About {SAVE_YEARLY}% less than paying monthly."
    features:
      - "Everything in Premium · Monthly"
      - "About {SAVE_YEARLY}% less than twelve months of Monthly"
      - "{TRIAL} · cancel anytime in your Apple Account settings"
    highlight_label: "Best value"
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All of Premium for one payment."
    features:
      - "Everything in Premium"
      - "One-time purchase with nothing to renew or cancel"
      - "Family Sharing included"

icon: "/assets/icons/xiangqiful.png"
og_image: "/assets/og/xiangqiful.png"

seo:
  title: "Xiangqi (Chinese Chess) App for iPhone & Mac | Xiangqiful"
  description: "Learn xiangqi (Chinese chess) on iPhone, iPad, and Mac: 80 free lessons, 902 mate puzzles, 40 opponents, and on-device Pikafish game review."
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
  pre_headline: "Xiangqi (Chinese chess) lessons, training, and game review for iPhone, iPad, and Mac"
  headline: "Learn Chinese chess from your first move, even before you can read the pieces."
  secondary: "Start with western symbols, learn the rules that catch chess players out, and let the Pikafish engine review every game on your device."
  subheadline: "Each mistake comes back named in xiangqi's own terms, such as a screenless cannon or a trapped horse, and goes into tomorrow's training. Around that loop sit 80 free lessons, 902 mate puzzles from mate in 1 to mate in 7, and 40 opponents with their own styles, the first 10 of them free."
  cta_label: "Download Free"
  cta_subline: "Free download · 80 lessons and 10 opponents free · no ads · no account · works offline"
  alt: "Xiangqiful on iPhone: a game against Shīfu on the 3D board with classic wooden discs, Red to move"

screenshots:
  - src: "/assets/screenshots/xiangqiful/1.webp"
    caption: "A game against Shīfu on the optional 3D board with classic wooden discs."
  - src: "/assets/screenshots/xiangqiful/2.webp"
    caption: "80 lessons in 8 tracks, from the board to the classics, all free."
  - src: "/assets/screenshots/xiangqiful/3.webp"
    caption: "The hybrid piece set: each western symbol sits on its Chinese character, so you can play now and learn the characters as you go."
  - src: "/assets/screenshots/xiangqiful/4.webp"
    caption: "Game Review: every move graded, accuracy for both sides, and the key moments of the game."
  - src: "/assets/screenshots/xiangqiful/5.webp"
    caption: "A mate puzzle in progress: mate in 3, where every move must give check."
  - src: "/assets/screenshots/xiangqiful/6.webp"
    caption: "Today's plan, built from your own mistakes, then mixed practice."
  - src: "/assets/screenshots/xiangqiful/7.webp"
    caption: "The opponent ladder by tier, starting with Xiǎobǎo, the kid who just learned the moves."
  - src: "/assets/screenshots/xiangqiful/8.webp"
    caption: "Progress: Xiangqiful's own estimated rating, accuracy over time, and the five-axis skill profile."
  - src: "/assets/screenshots/xiangqiful/9.webp"
    caption: "Home: today's training and what to work on next."

who_for:
  - "You play chess and are curious about xiangqi, but the characters on the pieces stopped you before your first game"
  - "You keep losing xiangqi games and want to know why, move by move"
  - "You want your mistakes named in words (the horse with nowhere to go, the cannon that lost its screen) instead of bare evaluation numbers"
  - "You like structure: lessons, drills, and mate puzzles chosen from your own weak spots"
  - "You want the classical manuals: mate puzzles and endgame studies from the Qing-dynasty books"
  - "You want a trainer that works offline, without an account or ads"

who_not_for:
  - "You want to play other people: Xiangqiful is single-player, with no online games"
  - "You want a database of master games or an opening explorer; Xiangqiful has neither"
  - "You need your progress to sync between devices; each device keeps its own games and progress"
  - "You're on Android or Windows: Xiangqiful needs iOS 18 or iPadOS 18 or later, or a Mac"
  - "You're looking for janggi (Korean chess), a different game with its own rules"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "For the player who can't read the pieces yet, and the one who has played for years."
  story: "Outside Asia, many people stop at xiangqi's first look: thirty-two wooden discs, each painted with a Chinese character. Xiangqiful starts there. Symbols come first, and the characters follow when you're ready. The lessons teach the rules that trip up chess players, such as the loss you take for having no legal move. The opponents play styles, from a grandmother who never leaves her palace to a twin-cannon fanatic. After each game, Pikafish reviews your moves on your own device and names what went wrong in xiangqi's own terms, and those mistakes become your next training session. It is the third app in the series after Chessful and Shogiful. Nothing runs on a server, and there is no account to make."
  signals:
    - "Pikafish, a strong open-source engine (GPL-3), runs inside the app, so analysis needs no cloud and no account"
    - "Mistakes are tagged with 26 xiangqi pattern names, among them the screenless cannon, the trapped horse, broken advisors, and the Iron Bolt"
    - "902 mate puzzles: 708 from eight classical manuals, each line re-checked by the app's own solver, and any book problem that doesn't work left out"
    - "40 localizations and VoiceOver support"
    - "The app links no ad, analytics, or tracking SDKs and collects nothing"
  external_link:
    label: "Read the Lagerland studio backstory →"
    href: "/lagerland-apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally, usually within a day."

value_points:
  - title: "Play before you can read the pieces"
    description: "Choose traditional characters, western symbols, or a hybrid that shows both. The lessons introduce the characters one piece at a time, so you can switch to the traditional set when you're ready, or never."
  - title: "Find out why you lost"
    description: "After a game, Pikafish grades every move from best to blunder, gives both sides an accuracy score, and picks out the key moments. Each mistake comes with the better move, a line you can play through, and a name from xiangqi itself."
  - title: "Train on your own mistakes"
    description: "Today's plan is built from the mistakes in your analyzed games, followed by mixed practice. Spaced repetition brings the problems you missed back until they stick."
  - title: "Offline, with no account"
    description: "Lessons, games, the engine, analysis, and training all run on your device, so the app works the same in airplane mode. You never create an account, and the app collects nothing."

features:
  - title: "80 lessons in 8 tracks, all free"
    description: "Fundamentals, Openings, Palace Defense, Cannon Tactics, Horse Technique, Middlegame, Endgame, and Advanced, ten lessons each, with the rules shown on the board. The first lesson every chess player needs: in xiangqi, having no legal move is a loss, and so is checking forever. When either happens in one of your games, the app explains it on the spot."
  - title: "Game Review with on-device Pikafish"
    description: "Pikafish grades every move from best to blunder and gives each side an accuracy score. You see the key moments of the game, the better move, and a best line you can play through on the board. Free players get 2 analyses a day; Premium makes it unlimited and adds deep multi-line analysis."
  - title: "Mistakes named in xiangqi's own language"
    description: "Mistakes are sorted into 13 categories and tagged with 26 xiangqi patterns, among them the screenless cannon, the trapped horse, broken advisors, the Empty-Head Cannon, the palace breach, the Iron Bolt, the missed mate, and the lost initiative. Each one sends you to practice on the same pattern."
  - title: "40 opponents with their own styles"
    description: "Climb a ladder of 40 named opponents in eight tiers, from Novice to Master. Each plays a style: aggressive, defensive, cannoneer, horse specialist, river controller, positional, endgame grinder, or balanced. Shīfu sits on rung 33, and above him wait the Shadow Horse, the Iron Abacus, the Divine Cannon, and the Sage. Beat an opponent twice to mark it defeated. The first 10 are free with unlimited games, and Premium opens all 40 at once."
  - title: "902 mate puzzles from the classical manuals"
    description: "Mate Trail holds 902 consecutive-check puzzles, xiangqi's native puzzle form, where every move must give check, from mate in 1 to mate in 7. 708 come from eight classical manuals, the Shiqing Yaqu supplying the most, and 194 are original compositions. Every line was re-checked by the app's own solver, and any book problem that does not really work was left out."
  - title: "Nine drill modules, more than 150 drills"
    description: "Mate Trail, Opening Lab (mainlines and refutations for ten opening families), Palace Workshop, Cannon Range, Horse Trails, Endgame Studio, Tactic Cards, Tactics Yard, and Handicap House, where you play a real game against an opponent who concedes a chariot, a horse, two horses, or the first move. The first drill set in every module is free."
  - title: "Thirty classical endgame studies"
    description: "Classical Studies in Endgame Studio holds thirty studies from the Qing-dynasty manuals, such as Seven Stars Gather and A Thousand Miles Alone. Play each one out against the engine; any sound move counts. Tap Book and it first points to the piece, then shows the move, and afterwards you can step through the book's own line. Part of Premium."
  - title: "A board you can read"
    description: "Traditional, western, or hybrid pieces; traditional or simplified characters; WXF or Chinese notation; a boxwood or rosewood board; coordinates on or off. Live games can use an optional 3D board with the Classic Discs or the Carved Set, while review, analysis, and training use the 2D board."
  - title: "Progress and a skill profile"
    description: "An estimated rating from your analyzed games, with rating and accuracy over time, your streak, and what to work on next on Home. A 15-position assessment gives you a starting rating. Premium adds a five-axis skill profile (tactics, defense, positioning, endgame, openings), weakness trends, and this week against last."
  - title: "iPhone, iPad, and Mac"
    description: "The Mac version adds menu commands and keyboard shortcuts for a new game, flipping the board, analyzing a game, and copying the position as FEN. Import games as WXF or ICCS movetext and review them too. Game Center adds 8 leaderboards and 62 achievements if you want them. The app comes in 40 localizations, with VoiceOver support."

# Methodology disclosure: emits HowTo schema via _layouts/app.html. Every step
# traces to blueprint §4 (Game Review, Named mistakes, Daily plan, Progress).
how_it_works:
  heading: "From your last move to tomorrow's training."
  intro: "This is what happens between the end of a game and your next training session."
  steps:
    - title: "Play a game or import one"
      detail: "Play one of the 40 opponents as Red, Black, or a random side, or import a game record as WXF or ICCS movetext from a file or the clipboard."
    - title: "Pikafish reviews every move"
      detail: "Tap Analyze and Pikafish goes through the game on your device. Each move is graded from best to blunder, each side gets an accuracy score, and the key moments are marked with the better move and a best line you can play through. Free players get 2 analyses a day; Premium is unlimited and adds deep multi-line analysis."
    - title: "Mistakes are named in xiangqi terms"
      detail: "Each significant mistake goes into one of 13 categories, such as missed mate, missed cannon tactic, palace weakness, or trapped piece, and is tagged with the pattern behind it: a screenless cannon, broken advisors, a palace breach, or a classical mate such as the Iron Bolt."
    - title: "Your mistakes become today's plan"
      detail: "Today's plan starts with a focus drawn from your own mistakes and ends with mixed practice. Choose a short, medium, or long session. Free players get 3 puzzles a day; Premium is unlimited."
    - title: "Spaced repetition brings misses back"
      detail: "The problems you fail are scheduled with spaced repetition (SM-2), so they come back as reviews due on a given day until you solve them."
    - title: "Progress shows what changed"
      detail: "Your estimated rating and accuracy trend update as you play and analyze. Premium adds the five-axis skill profile, weakness trends that show whether each weakness is improving, steady, or worsening, and this week against last. The rating is Xiangqiful's own estimate from your analyzed games, not an official or federation rating."

# Example coaching: each card is assembled from the app's own English strings
# (Localizable.xcstrings: pattern.* details, mistake.* bodies and tips; checked
# 2026-10-29).
example_insights:
  overline: "What Xiangqiful explains"
  heading: "What a xiangqi mistake looks like, explained."
  intro: "Six examples of what Xiangqiful shows in Game Review, in the app's own words. Each names what happened, says why it matters in xiangqi, and ends with something to try in your next game."
  cards:
    - tag: "Tactics · Screen tactic"
      headline: "Your horse stepped into the line and handed the enemy cannon the screen it needed."
      body: "A cannon can only capture by jumping exactly one piece, so every cannon tactic is really about the piece in between. Adding a screen turns a quiet cannon into a threat; removing one defuses it. Before moving anything else, check what the cannons would hit if one piece moved."
    - tag: "Tactics · Missed mate"
      headline: "The middle cannon holds the file while the chariot bars the palace gate: the Iron Bolt, mate in 3."
      body: "A forced sequence ends the game whatever your opponent does, and once one exists nothing else on the board matters. Mating patterns repeat: a handful of shapes finish most games. When the enemy general is short of advisors, exhaust the forcing moves before playing anything quiet."
    - tag: "Positioning · Trapped piece"
      headline: "Your horse has no square left that it can safely reach."
      body: "A horse blocked at the leg, or a cannon with nothing left to jump over, is material you own but cannot use. Xiangqi pieces are slower than they look, and a badly placed one rarely recovers. Next game, before advancing a horse, count the intersections it can leave from."
    - tag: "Defense · Palace weakness"
      headline: "Stepping the advisor off its post left the palace one wall short."
      body: "Two advisors and two elephants are the walls of the fortress, and an advisor's worth is not its material value: a general behind two of them cannot be mated by half the standard patterns. Move an advisor or elephant only after counting what it stops defending."
    - tag: "Positioning · Passive move"
      headline: "That move asked nothing of your opponent."
      body: "Xiangqi rewards whoever is asking the questions. Losing the initiative hands your opponent a free move to improve their worst piece, and over several such moves a level position slowly becomes a worse one. Prefer a move that creates a threat over one that merely improves a piece."
    - tag: "Endgame · Endgame error"
      headline: "The endgame technique slipped."
      body: "Xiangqi endgames are a codified science: the result of most material balances is known exactly, so the winning method is a matter of knowledge rather than calculation. And in the endgame the horse outweighs the cannon, because screens are scarce once the board empties."

alternatives_to:
  - "Xiangqi.com"
  - "PyChess"
  - "Club Xiangqi"
  - "PlayOK"
  - "Chinese Chess - Best XiangQi"

# Side-by-side comparison: auto-triggers the mid-page CTA and the alt-strip.
# Competitor cells are unchanged from the 2026-10-01 summary.
comparison_table:
  intro: "Every row is a question a xiangqi-curious player asks before installing an app. Xiangqi.com is the English-language online platform; PyChess is the free open-source web platform; Club Xiangqi is the bilingual English and Vietnamese online club; Chinese Chess - Best XiangQi is a popular free offline opponent. Xiangqiful is a single-player training app. Summarised from each app's public listing on 2026-10-01."
  competitors: ["Xiangqiful", "Xiangqi.com", "PyChess", "Club Xiangqi", "Chinese Chess - Best XiangQi"]
  rows:
    - feature: "Fully offline (no internet required)"
      values: ["Yes, Pikafish runs on-device", "Offline mode vs computer; online features need a connection", "No, web platform", "No, web club", "Yes"]
    - feature: "Account required"
      values: ["No account", "Account-based online service", "Sign-in via Lichess, Lishogi, Google or Discord", "Free account (resets after 4 months idle)", "No"]
    - feature: "Engine review of your games"
      values: ["Pikafish, every move graded from best to blunder", "In-app engine analysis (Pikafish credited)", "Fairy-Stockfish analysis", "Not a listed feature", "Hints during play"]
    - feature: "Mistakes named in xiangqi terms"
      values: ["Yes: screenless cannon, trapped horse, broken advisors, missed mates", "Not a listed feature", "No, engine lines", "No", "No"]
    - feature: "Live play against people"
      values: ["No, single-player", "Yes", "Yes, free", "Yes, novice to master", "No"]
    - feature: "Price"
      values: ["Free; {P_MONTHLY}/mo or {P_YEARLY}/yr ({TRIAL}), or {P_LIFETIME} lifetime", "Free; optional ad-free subscription", "Free, donation-funded", "Free; optional paid membership", "Free, no IAP; ad tracking"]
  footnote: "Competitor positioning summarised from each platform's public listing or site on 2026-10-01. Pricing and features change, so verify before switching. If you want to play people, use those platforms; Xiangqiful is for training between games."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  app_privacy_label: "Xiangqiful collects no data and runs no servers of its own. Its privacy manifest declares no tracking and no collected data types, and the app links no advertising or analytics SDKs."
  notes:
    - "No account, and no servers of the developer"
    - "Pikafish, the analysis, and the coaching all run on your device"
    - "Games, lessons, drills, and progress are stored only on your device"
    - "No analytics, advertising, or tracking SDKs"
    - "No camera, photos, microphone, location, or contacts access"
    - "Purchases and the optional Game Center are handled by Apple"
  policy_url: "/apps/xiangqiful/privacy/"

faq:
  - q: "What is Xiangqiful?"
    a: "Xiangqiful is a xiangqi (Chinese chess) app for iPhone, iPad, and Mac built around one loop: learn, play, find out why, and train. It teaches the game from your first move with 80 free lessons, lets you play 40 opponents with distinct styles, and has the Pikafish engine review every move on your device. The mistakes it finds are named in xiangqi's own terms and become your next training session, alongside 902 mate puzzles and more than 150 drills. It works offline, without an account or ads."
  - q: "What is xiangqi, and how is it different from chess?"
    a: "Xiangqi is the traditional Chinese form of chess, played across China, in Vietnam as cờ tướng, and throughout the Chinese diaspora. The pieces stand on the intersections of a 9×10 grid instead of in squares, a river splits the board, and each general is confined to a 3×3 palace with its two advisors. Several pieces catch chess players out: the cannon moves like a rook but can only capture by jumping exactly one piece, the horse can be blocked at the leg, elephants cannot cross the river, and the two generals may never face each other on an open file. Most surprising of all, a player with no legal move loses (stalemate is a loss, not a draw), and perpetual check loses for the side giving it."
  - q: "Can I play without reading Chinese characters?"
    a: "Yes, and that is one of the main reasons Xiangqiful exists. Choose the western set, which uses symbols, or the hybrid set, which shows each symbol together with its character so you learn them as you play. The lessons introduce the characters one piece at a time, and you can switch to the traditional set whenever you're ready."
  - q: "Is Xiangqiful good for complete beginners?"
    a: "Yes. The Fundamentals track starts with the board and the pieces, and the lessons cover the rules that surprise newcomers. When one of them happens in your own game, such as a stalemate or a perpetual check, the app explains it on the spot. The opponent ladder starts in the Novice tier with a kid who has just learned the moves. If you already play, the 15-position skill assessment gives you a starting rating."
  - q: "What engine does Xiangqiful use?"
    a: "Pikafish, a strong open-source xiangqi engine derived from Stockfish. It is built into the app with its neural network and runs entirely on your device, so analysis needs no cloud and no account. Xiangqiful turns its output into graded moves and named mistakes. Pikafish is licensed under the GPL-3; the Licences screen in Settings names it and includes the license text."
  - q: "How strong are the opponents?"
    a: "There are 40 opponents in eight tiers, from Novice to Master. The strength shown for each is Xiangqiful's own scale, not an Elo rating from any federation. Each opponent plays a style rather than a weakened copy of the engine: aggressive, defensive, cannoneer, horse specialist, river controller, positional, endgame grinder, or balanced. Shīfu sits on rung 33, and the Sage waits at the top. The first 10 opponents are free with unlimited games, and Premium opens all 40 at once. Beat an opponent twice to mark it defeated. You can play Red, Black, or a random side."
  - q: "Can I play against other people?"
    a: "No. Xiangqiful is a single-player training app with no accounts, servers, or online matches. It is meant to make you better between the games you play with people, whether at a club, online, or in the park."
  - q: "Does Xiangqiful work offline?"
    a: "Yes. Lessons, games, the engine, analysis, training, and progress all run on your device. A connection is needed only for things Apple handles: loading prices, buying or restoring Premium, and Game Center if you use it."
  - q: "Is Xiangqiful free? What does Premium cost?"
    a: "Xiangqiful is free to download, and the free tier has no time limit: all 80 lessons, the skill assessment, unlimited games against the first 10 opponents, the first drill set in every module, 2 game analyses a day, 3 training puzzles a day (mate puzzles included), and 2 in-game coach hints a day. Premium opens all 40 opponents and every drill, removes the daily limits, and adds deep multi-line analysis, the skill profile, and weakness trends. It costs {P_MONTHLY} a month or {P_YEARLY} a year, each with a {TRIAL} for new subscribers, or {P_LIFETIME} once, and all three support Family Sharing. Prices are in USD; the App Store shows your local price. There are no ads in either tier."
  - q: "Where do the mate puzzles come from?"
    a: "There are 902 of them, from mate in 1 to mate in 7, and every one is a consecutive-check problem: each attacking move must give check. 708 come from eight classical manuals, with the Shiqing Yaqu supplying the most, and 194 are original compositions. Every line was re-checked by the app's own solver, and a book problem that does not really work was left out."
  - q: "What are the tips in Settings?"
    a: "Optional ways to support the app: Coffee, Supporter, and Huge Support. They unlock nothing, because Premium already includes every feature. They are one-time purchases handled by Apple."
  - q: "Can I analyze games I played somewhere else?"
    a: "Yes, with limits. Paste a game from the clipboard or choose a text file, as ICCS (H2-E2) or WXF (C2=5) movetext, preview it, and analyze it like any other game. Other formats such as XQF are not supported, and records from some sites may need tidying first. On the Mac you can also copy the current position as FEN or copy the game record."
  - q: "Which rules does Xiangqiful use for draws and repetition?"
    a: "Checkmate wins, and so does stalemate: having no legal move is a loss in xiangqi. Perpetual check loses for the side giving it. Threefold repetition and sixty moves without a capture are draws. The rule against perpetual chasing is not adjudicated."
  - q: "Does it support Chinese notation and simplified characters?"
    a: "Yes. Moves can be shown in WXF notation (C2=5) or in Chinese notation, and the pieces can carry traditional or simplified characters. The app comes in 40 localizations, including Simplified and Traditional Chinese, Vietnamese, Japanese, Korean, and Thai."
  - q: "Does my progress sync between iPhone, iPad and Mac?"
    a: "No. Your games, analysis, and training progress are stored on the device you use, and there is no account or server to sync through. To unlock Premium on another iPhone or iPad, use Restore purchases there."
  - q: "Does Xiangqiful use Game Center?"
    a: "Only if you want it to; signing in is optional. Your results feed 62 achievements and eight leaderboards: estimated rating, best game accuracy, accuracy this week, longest win streak, opponents defeated, training streak, puzzles solved, and overall skill. The app also has its own Achievements screen."
  - q: "Is Xiangqiful accessible?"
    a: "Xiangqiful supports VoiceOver, with labels on the board's points, the opponent cards, the skill chart, and the controls. Arabic and Hebrew get a right-to-left setting for the board. The app is available in 40 localizations. It does not support Dynamic Type, and it uses a dark theme only."

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
  anchor: "902 xiangqi mate problems, eight old books, and the ones I left out"

show_body: true
about_heading: "What Xiangqiful is: xiangqi lessons, training, and game review"

ratings:
  value: "5.0"
  count: 2
  last_synced: "2026-10-24"
last_updated: 2026-10-29
---
Xiangqiful is a [xiangqi app for iPhone, iPad, and Mac](#features) that teaches the game from your first move and then helps you get better at it. Xiangqi is Chinese chess: two armies of sixteen pieces on the intersections of a nine-by-ten board, a river across the middle, and a palace at each end that the generals may never leave. Outside Asia, many people stop at the first look, because every piece is a Chinese character painted on a wooden disc.

You can play with traditional characters, western symbols, or a hybrid of both, and the lessons introduce the characters one piece at a time. All 80 lessons are free, in eight tracks from the board to the classics, and they teach the rules that catch chess players out: having no legal move loses, and so does perpetual check.

Then you play. Forty opponents in eight tiers each play a style of their own, from a kid who has just learned the moves to the Sage at the top, and the first ten are free. After a game, [Pikafish](https://github.com/official-pikafish/Pikafish), a strong open-source engine, reviews it on your device. It grades every move from best to blunder and [names each mistake in xiangqi's own terms](#insights): a screenless cannon, a trapped horse, broken advisors, a missed Iron Bolt. Those mistakes [become today's plan](#how-it-works), and spaced repetition brings back the problems you missed.

For training there are 902 mate puzzles, 708 of them from eight classical manuals and each re-checked by the app's own solver, plus nine drill modules and thirty classical endgame studies from the Qing-dynasty books.

Everything runs on your device, and the app collects nothing; the [privacy policy](/apps/xiangqiful/privacy/) explains what stays on your device and what Apple handles. Xiangqiful has no online play: it is for practice between the games you play with people. If you also play Japanese or Western chess, [Shogiful](/apps/shogiful/) and [Chessful](/apps/chessful/) follow the same loop.

The free version includes all 80 lessons, unlimited games against the first ten opponents, and the first drill set in every module, plus two game analyses, three training puzzles, and two coach hints a day. Premium opens all 40 opponents and every drill, lifts the daily limits, and adds deep multi-line analysis and the skill profile, for {P_MONTHLY} a month or {P_YEARLY} a year, each with a {TRIAL}, or {P_LIFETIME} once. Published by Lagerland Apps, an independent Apple developer in Finland.
