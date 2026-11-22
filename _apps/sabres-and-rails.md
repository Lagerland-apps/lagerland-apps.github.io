---
layout: app
slug: sabres-and-rails
name: "Sabres & Rails"
tagline: "Civil War strategy for iPhone and iPad. Plan the war on the map, then fight every battle yourself, by touch."

# ── UNLISTED: PRE-LAUNCH ──────────────────────────────────────────────────────
# Sabres & Rails is not released yet. `status` is deliberately NOT "live": every
# listing on this site filters on `where: "status", "live"` (home, /apps/,
# llms.txt, llms-full.txt, ai-index.json, ai-sitemap.xml, footer,
# you-might-like, /lagerland-apps/, the /for/ hubs, the language hubs), so this
# page exists at its URL and appears nowhere else. `sitemap: false` keeps it
# out of sitemap.xml and `noindex: true` keeps it out of search results.
#
# The URLs are needed before release: App Store Connect's Privacy Policy URL
# is /apps/sabres-and-rails/privacy/ and its Support URL is
# /apps/sabres-and-rails/support/, and App Review opens them.
#
# Facts: ~/Downloads/northsouth/ios/APP_BLUEPRINT.md (§2, §3, §6, §8, §10) and
# the approved en-US listing (store/listing/en-US.md). House rules from the
# blueprint §8 that apply to every language: never name the 1989 original, its
# publisher or the comic, no "inspired by" or "remake"; no Confederate flags;
# not a historical simulation (no accuracy claims, no "1861 map").
# Store name: "Sabres & Rails: Civil War". The price stays out of the prose
# until The Whole War is approved (a missing {P_IAP:...} token would print
# literally); the plan card below hides itself until then.
#
# ON LAUNCH: follow ~/Downloads/githubcode/SABRES-LAUNCH.md (outside the repo).
status: upcoming
sitemap: false
noindex: true
# Pre-launch only: MASTER.md marks iPhone and iPad as pending (⏳); the catalog lists live platforms only.
# Ignored once the catalog has them (_includes/app-facts.html). Delete on launch.
prelaunch_platforms: ["iOS", "iPadOS"]
# ──────────────────────────────────────────────────────────────────────────────

quick_answer: "Sabres & Rails is a Civil War strategy game for iPhone and iPad. You move your armies across a 25-territory map of the United States, and when they meet the enemy, the battle opens and you fight it yourself by touch, in real time: aim and fire the cannons, march the infantry and fire volleys, and send the cavalry charging. You can also rob gold trains and storm forts in action scenes, or leave those to Automatic. Play the computer at one of three difficulty ranks, or a friend on the same device, where both of you fight the same battle at once on a split screen. Start the war in 1861, 1862, 1863, or 1864, or pick Strategy mode to play the whole war on the map. The download is free, and every war is free for its first three months of game time; one purchase, The Whole War, plays it to the end. It plays offline, needs no account, shows no ads, and collects no data."
category: games

app_store_url: "https://apps.apple.com/app/id6837781099"

price:
  model: free
price_override: "Free to start · one purchase unlocks the whole war"

pricing_note: "The first three months of every war are free, with no time limit and no card. The Whole War is a one-time purchase that never renews."

plans_footnote: "Sabres & Rails is a free download. Every war is free until April of its start year, against the computer or a friend, and the guided tutorial is free in full. The Whole War is a non-consumable purchase: you buy it once, it stays yours, and you can restore it from Settings or the unlock screen. It works with Family Sharing. There are no ads or other purchases. US pricing shown; the App Store shows your local price at checkout."

plans:
  - name: "The first three months"
    price: "Free"
    summary: "Every war, every start year, and both modes, until April of the year you start in."
    features:
      - "Start in 1861, 1862, 1863, or 1864"
      - "Arcade and Strategy modes"
      - "Against the computer or a friend on the same device"
      - "The guided tutorial game, free from start to finish"
      - "No ads or account, and it plays offline"
    highlight: true
  - name: "The Whole War"
    price: "{P_IAP:The Whole War} once"
    summary: "Your war marches on past April to its end, and so does every war after it."
    features:
      - "Every war played to victory or defeat"
      - "One purchase, never renewed"
      - "Restore it any time from Settings"
      - "Family Sharing included"

icon: "/assets/icons/sabres-and-rails.png"
og_image: "/assets/og/sabres-and-rails.png"

seo:
  title: "Sabres & Rails: Civil War Strategy Game for iPhone and iPad"
  description: "Civil War strategy game for iPhone and iPad. Move armies on the map, fight real-time battles by touch, play a friend on one screen. Offline, no ads."
  keywords:
    - "civil war game iphone"
    - "civil war strategy game"
    - "turn based strategy ipad"
    - "real time battles touch"
    - "two player game one ipad"
    - "offline strategy game no ads"
    - "war strategy game iphone"

hero:
  pre_headline: "Civil War strategy for iPhone and iPad"
  headline: "Plan the war. Fight every battle yourself."
  secondary: "Move your armies across a map of the United States. When they meet the enemy, you take the field."
  subheadline: "Sabres & Rails puts two games in one. On the map you claim territories, run gold trains, and pick your attacks one turn at a time. On the battlefield you aim the cannons, fire the infantry's volleys, and lead the cavalry's charge with your own fingers, and the result goes back to the map."
  cta_label: "Start a war free"
  cta_subline: "Free download · every war free for three months · one purchase for the whole war · no ads · no data collected"
  alt: "Sabres & Rails app icon: two crossed cavalry sabres, one in a blue scabbard and one in grey, over a steam locomotive coming round a curve"

screenshots_landscape: true
screenshots:
  - src: "/assets/screenshots/sabres-and-rails/1.webp"
    alt: "Sabres & Rails: the strategy map of the United States with Union and Confederate armies on the left, and a real-time battle at a river bridge on the right"
  - src: "/assets/screenshots/sabres-and-rails/2.webp"
    alt: "Cannons firing across a battlefield in Sabres & Rails; you hold to aim and let go to fire"
  - src: "/assets/screenshots/sabres-and-rails/3.webp"
    alt: "Cavalry charging with sabres while infantry fire volleys in a Sabres & Rails battle"
  - src: "/assets/screenshots/sabres-and-rails/4.webp"
    alt: "Two players fighting the same Sabres & Rails battle at once, each on their half of the screen"
  - src: "/assets/screenshots/sabres-and-rails/5.webp"
    alt: "A soldier running along the roofs of a gold train against the clock in Sabres & Rails"
  - src: "/assets/screenshots/sabres-and-rails/6.webp"
    alt: "A soldier fighting his way across a fort's ramparts toward the flag in Sabres & Rails"
  - src: "/assets/screenshots/sabres-and-rails/7.webp"
    alt: "The five battlefields of Sabres & Rails, from a river crossing and a bayou to a mountain pass"
  - src: "/assets/screenshots/sabres-and-rails/8.webp"
    alt: "The Sabres & Rails setup screen: each side played by a person or the computer, a start year from 1861 to 1864, and the battle mode"

who_for:
  - "You like map-based war games and want to fight the battles yourself, not watch a dice roll decide them"
  - "You want a strategy game two people can play on one iPhone or iPad, sitting side by side"
  - "You play on planes, trains, or anywhere without a signal, with no account to sign into"
  - "You'd rather try a whole war's opening for free and pay once to finish it than sit through ads"
  - "You're new to war games and want a guided game that teaches the rules while you play"

who_not_for:
  - "You want online multiplayer. Two players share one device; there is no online play"
  - "You want a historical simulation. The map, start years, and rules are a game's take on the war"
  - "You play on Mac, Android, or an iPad in Split View. Sabres & Rails runs full screen in landscape on iPhone and iPad with iOS 26 or later"
  - "You play with VoiceOver and want the real-time battles. VoiceOver reads the map, menus, and battle controls, but not the battlefield itself; Strategy mode plays the war without it"

value_points:
  - title: "Every battle is yours to fight"
    description: "In Arcade mode, armies meeting on the map open a real-time battle on that territory's battlefield. Hold a finger to aim the cannons and let go to fire, drag to march the infantry and tap to fire a volley, and steer the cavalry into a sabre charge. Win, lose, or retreat, and the map plays on from what happened."
  - title: "Two players, one screen"
    description: "Hand a friend the other side. You take turns on the map, and when your armies meet, you both fight the same battle at the same time, each on your own half of the screen with your own controls."
  - title: "Free for the first three months of every war"
    description: "Download the game and start any war you like, in any start year and either mode, against the computer or a friend. When April comes, your war saves and waits. Buy The Whole War once and that war marches on to its end, along with every war after it."
  - title: "A war that fits in your pocket"
    description: "Sabres & Rails plays fully offline and saves after every move, so you can stop mid-campaign and pick it up exactly where you left off. There is no account to create, you'll never see an ad, and the game collects no data."

features:
  - title: "The campaign map"
    description: "Fight your way across a 25-territory map of the United States, one territory at a time. Claim neutral ground, attack the enemy, hold the forts, and buy new armies with the gold your trains bring in. Pinch to zoom and drag to look around."
  - title: "Real-time battles by touch"
    description: "Each side fields cannons, infantry, and cavalry. The cannons fire nine shots and break bridges; the infantry walks and fires volleys; the riders charge and slash with their sabres. A battle ends when one side has nothing left on the field, or when a commander calls the retreat."
  - title: "Five battlefields"
    description: "Battles are fought on a river crossing, a bayou, a mountain pass, a prairie gully, and farmland, each with its own ground: water and drops that swallow soldiers, mud and marsh that slow them, and bridges your own guns can bring down."
  - title: "Trains and forts"
    description: "Rob an enemy gold train by running along the roofs before the clock runs out, or storm a fort and fight your way to its flag. Prefer to stay at the map table? Set them to Automatic at setup and they're decided for you."
  - title: "Arcade or Strategy"
    description: "Arcade mode puts you on the battlefield for every clash. Strategy mode plays the whole war on the map, with each battle's result worked out for you."
  - title: "Three difficulty ranks"
    description: "Give the computer the rank of Corporal, Sergeant, or Captain. The rank sets how hard the computer plays on the map and how quickly its troops react in battle. Make both sides Computer to watch it play itself."
  - title: "Guided tutorial"
    description: "A short game of its own, with your Captain explaining each step: moving an army, claiming a territory, fighting a battle, riding the rails, and the gold train. It never touches your saved war, and it's free from start to finish."
  - title: "Made for every player"
    description: "VoiceOver reads the map, every territory and army, the menus, and the battle controls, and Strategy mode plays the whole war without the real-time battlefield. Text grows with Dynamic Type, Reduce Motion is respected, and haptics and screen shake can be turned off."

how_it_works:
  heading: "From the map table to the battlefield."
  intro: "Each war runs month by month, one side's turn at a time, from January of the year you choose until one side has won."
  steps:
    - title: "Set up your war"
      detail: "Choose who plays the Union and who plays the Confederacy, a person or the computer, and each side's rank. Pick a start year from 1861 to 1864, Arcade or Strategy battles, and whether trains and forts are played or Automatic."
    - title: "Move on the map"
      detail: "Tap one of your armies to see where it can go, then tap a territory to move there or attack. Ride the railway, reinforce an army, and spend the gold your trains bring in on new armies."
    - title: "Fight the battle"
      detail: "When armies meet in Arcade mode, the battlefield opens. Command your cannons, infantry, and cavalry by touch until one side is beaten or retreats."
    - title: "Win the war"
      detail: "The battle's result goes back to the map, and the war plays on, saved after every move, until victory or defeat."

faq:
  - q: "What kind of game is Sabres & Rails?"
    a: "Sabres & Rails is a Civil War strategy game for iPhone and iPad with two layers. On a map of the United States you move armies, claim territories, and attack one turn at a time. When armies meet, a real-time battle opens and you fight it yourself by touch, with cannons, infantry, and cavalry. It also has action scenes for robbing gold trains and storming forts."
  - q: "Is Sabres & Rails free?"
    a: "The download is free, and every war is free for its first three months of game time, until April of its start year. That covers every start year, Arcade and Strategy modes, and games against the computer or a friend. The guided tutorial is free in full. One purchase, The Whole War, lets every war play on to its end. It's a one-time purchase, it works with Family Sharing, and there are no ads."
  - q: "What happens when the free months are over?"
    a: "When April of the start year comes, your war is saved and waits on the unlock screen. Buy The Whole War and that same war carries on from where it stopped. You can also go back to the title and start another war, which is free for its first three months too."
  - q: "How do I restore The Whole War on a new iPhone or iPad?"
    a: "Open Settings from the gear on the title screen and tap Restore Purchase. The unlock screen has the same button."
  - q: "Can two people play on one iPhone or iPad?"
    a: "Yes. Set both sides to Player on the setup screen. You take turns on the map, handing the device over when it says so. When your armies meet in Arcade mode, both of you fight the same battle at the same time on a split screen, the Union on the left half and the Confederacy on the right, each with your own controls. There is no online play."
  - q: "How do the battles work?"
    a: "Tap a soldier, rider, or gun to command its group. Drag to move the cannons up and down, hold to fill the range gauge, and let go to fire. Drag to march the infantry and tap to fire a volley. Drag to steer the cavalry and gallop ahead, then tap to slash with the sabres. A battle ends when one side has no troops left on the field, or when a side retreats. The first battle of a game starts with the controls on screen."
  - q: "Can I skip the real-time battles?"
    a: "Yes. Choose Strategy instead of Arcade at setup and the whole war plays on the map, with each battle's result worked out for you. Train robberies and fort assaults can be set to Automatic on their own, too."
  - q: "How hard is the computer?"
    a: "The computer plays at one of three ranks: Corporal, Sergeant, or Captain. The rank sets how hard it plays on the map and how fast its troops react in battle. You can also give the computer both sides and watch it play itself."
  - q: "Does Sabres & Rails work offline?"
    a: "Yes. The whole game plays offline, with no account or sign-in. Only buying and restoring The Whole War go through Apple and need a connection. Your war is saved on the device after every move."
  - q: "Does Sabres & Rails collect any data?"
    a: "No. The game has no analytics, advertising, or third-party SDKs, and it never contacts a server. Your saved war and settings stay on your device. Apple handles the one purchase."
  - q: "Which devices does Sabres & Rails run on?"
    a: "iPhone and iPad with iOS or iPadOS 26 or later. The game plays in landscape, and on iPad it runs full screen, without Split View or Slide Over. There is no Mac, Apple Watch, Apple TV, or Android version."
  - q: "Which languages is Sabres & Rails in?"
    a: "The game is in English and 35 more languages, including German, French, Spanish, Italian, Portuguese, Dutch, Japanese, Korean, and Chinese. It follows your device's language."
  - q: "Is Sabres & Rails historically accurate?"
    a: "It's a strategy game set in the American Civil War, not a historical simulation. The 25 territories are drawn from today's state borders, merged into game territories, and the start years follow each January's front line only roughly. The South flies a plain grey banner with one star."
  - q: "Is Sabres & Rails accessible?"
    a: "VoiceOver reads the title, setup, settings, map, menus, and battle controls. On the map every territory is an element with its owner and army, and moves are offered as actions. The real-time battlefield can't be played with VoiceOver, so choose Strategy mode to play the whole war without it. Text grows with Dynamic Type, Reduce Motion is respected, and haptics and screen shake can be turned off in Settings."

privacy:
  tracking: false
  account_required: false
  data_collection: "none"
  app_privacy_label: "Sabres & Rails collects no data, which is the App Store privacy label “Data Not Collected.” The game does no tracking, includes no advertising or analytics SDKs, and its Privacy Manifest declares no tracking and no collected data."
  notes:
    - "No account, and the game makes no network connections of its own"
    - "Your saved war, setup choices, and settings are stored only on your device"
    - "No analytics, advertising, or third-party SDKs"
    - "Apple handles the one purchase; the game keeps only the fact that The Whole War is unlocked"
    - "No permission prompts for camera, photos, microphone, location, contacts, or health data"
  policy_url: "/apps/sabres-and-rails/privacy/"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "Sabres & Rails was built around one idea: when two armies meet on the map, you should be on the field with them, aiming the guns and timing the charge, and the map should live with whatever you managed there. Everything else follows from that. The battles had to work under a thumb on an iPhone, two players had to fit on one screen at once, and anyone who would rather stay at the map table needed Strategy mode."
  support_email: "support@lagerland.app"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "No ads, analytics, or third-party SDKs, and no network connections of its own"
    - "Paid for by one purchase, never by ads or data"
    - "VoiceOver on the map and menus, Dynamic Type, and Reduce Motion support"

support:
  email: "support@lagerland.app"
  url: "/apps/sabres-and-rails/support/"

release:
  first_release: "2026-11-22"
  last_updated: "2026-11-22"
  version: "1.0"

related_apps: ["chessful", "xiangqiful", "tare"]

show_body: true
about_heading: "What Sabres & Rails is: a war on the map, fought on the field"
last_updated: 2026-11-22
---

Sabres & Rails is a Civil War strategy game for iPhone and iPad in two layers. The first is a map of the United States split into 25 territories, where the Union and the Confederacy take turns month by month. The second opens whenever two armies meet: a battlefield where you command the cannons, infantry, and cavalry yourself, in real time.

## The map

Every war starts in January of the year you pick, 1861, 1862, 1863, or 1864, with each side holding what it held then, roughly. On your turn you move armies, claim neutral territory, attack the enemy, and ride the railway. Gold trains run your rail lines and pay for new armies, which makes the enemy's trains worth stopping.

## The battlefield

In Arcade mode every clash opens on that territory's battlefield: a river crossing, a bayou, a mountain pass, a prairie gully, or farmland. Hold a finger to aim your cannons and let go to fire. March the infantry and fire volleys. Steer the cavalry into a charge and slash with the sabres. Water and drops are deadly, mud slows everyone down, and your own guns can bring down the bridge you meant to cross. When one side is beaten or retreats, the map plays on from the result.

Rob a gold train or storm a fort and the game switches to an action scene: run along the train's roofs before the clock runs out, or fight your way across the ramparts to the flag. Set them to Automatic at setup if you'd rather they were decided for you, or pick Strategy mode to play the whole war on the map.

## How it's paid for

Sabres & Rails is a free download, and every war is free for its first three months of game time, against the computer or a friend. When April comes, the war saves and waits. One purchase, The Whole War, lets it march on to the end, along with every war after it. It works with Family Sharing, and there are no ads. The game plays offline, needs no account, and collects no data; the [privacy policy](/apps/sabres-and-rails/privacy/) has the details.

If you'd rather think in moves than in charges, [Chessful](/apps/chessful/) and [Xiangqiful](/apps/xiangqiful/) are strategy games from the same studio.
