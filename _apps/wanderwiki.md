---
layout: app
slug: wanderwiki
name: "WanderWiki"
tagline: "Swipe through Wikipedia, one idea at a time."
quick_answer: "WanderWiki is an iPhone and iPad app (iOS 18.2 or later) that turns Wikipedia into a deck you swipe: random articles from the whole encyclopedia, 16 topics to browse, and a clean reader for the full article, in 32 Wikipedia language editions. It is free for 20 articles a day with no account. Premium adds For You, Today in History, and unlimited swiping for {P_MONTHLY}/month or {P_YEARLY}/year, each with a {TRIAL} for new subscribers, or {P_LIFETIME} once. It shows no ads and does no tracking, and your saved articles, likes, and reading progress stay on your device."
category: education
status: live

app_store_url: "https://apps.apple.com/app/id6758459119"

price:
  model: freemium
price_lead: "Free (20 articles a day)"
price_tier: "Premium"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew. The App Store also lists an older weekly plan, which still renews for existing subscribers but is no longer sold in the app, and an optional {P_IAP:Support the developer} tip in Settings that unlocks nothing."
pricing_note: "Cancel anytime in your Apple Account settings. The free plan needs no card and no account: 20 articles a day, reset at local midnight."

plans:
  - name: "Free"
    price: "$0"
    summary: "20 articles a day, every day, with no card and no account."
    features:
      - "Random and Browse (16 topics): 20 articles a day, reset at local midnight"
      - "Save, like, search, and folders within the daily 20"
      - "All 32 Wikipedia language editions"
      - "Listen, reader themes, and all five widgets"
  - name: "Premium · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Premium, billed monthly. Cancel anytime."
    features:
      - "For You: a feed built around the topics you pick"
      - "Today in History: Wikipedia's On This Day, in five categories"
      - "Unlimited swiping"
      - "Family Sharing included"
      - "Everything in Free"
  - name: "Premium · Yearly"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "The same Premium, billed once a year. ~{SAVE_YEARLY}% cheaper than paying monthly."
    features:
      - "Everything in Premium · Monthly"
      - "~{SAVE_YEARLY}% cheaper than monthly over a year"
      - "Cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "Premium for one payment."
    features:
      - "Everything in Premium"
      - "One-time purchase, no renewal"
      - "Family Sharing included"
      - "Restores on any iPhone or iPad signed in with the same Apple Account"
    highlight_label: "Pay once"

icon: "/assets/icons/wanderwiki.png"
og_image: "/assets/og/wanderwiki.png"

seo:
  title: "WanderWiki: Swipe Random Wikipedia Articles on iPhone"
  description: "Swipe random Wikipedia articles in 32 languages on iPhone and iPad. No ads, no account, offline saves, and five widgets. Free for 20 articles a day."
  keywords:
    - swipe Wikipedia app
    - random Wikipedia articles app
    - Wikipedia discovery app iPhone
    - WikiScroll alternative
    - Wiki Rabbit alternative
    - swipe through Wikipedia
    - Today in History app
    - Wikipedia reader iPhone no ads
    - multilingual Wikipedia app
    - 32 Wikipedia languages
    - Wikipedia widget iPhone
    - On This Day widget
    - read Wikipedia offline iPhone
    - Wikipedia read aloud app
    - curiosity learning app
    - daily learning app
    - calm Wikipedia reader
    - doomscroll replacement app

hero:
  pre_headline: "For people who read Wikipedia for fun"
  headline: "Wander Wikipedia one swipe at a time, in 32 languages."
  secondary: "Random articles, 16 topics to browse, and today's history, as a deck of cards. No ads, no account, and your reading stays on your device."
  subheadline: "Tap a card to read the full article, follow a Where next chip to a related one, or save it to read offline. Free for 20 articles a day; Premium unlocks For You, Today in History, and unlimited swiping."
  cta_label: "Download Free"
  alt: "WanderWiki on iPhone showing a full-screen Wikipedia article card with a picture and the opening lines, ready to swipe"
  video: "/assets/videos/wanderwiki_preview.mov"
  video_poster: "/assets/videos/wanderwiki-poster.jpg"

who_for:
  - "You read Wikipedia for fun and would rather swipe than think of something to search"
  - "You miss clicking Random article on desktop Wikipedia and want that habit on iPhone or iPad"
  - "You read Wikipedia in more than one language, or want to start; WanderWiki carries 32 editions"
  - "You want something worth reading in a spare few minutes, without ads or an account"
  - "You want saved articles that open offline, sorted into folders, for flights and commutes"
  - "You want today's history, or two articles to choose between, on your Home Screen"

who_not_for:
  - "You need citations and source-checking for research; WanderWiki is a reading deck without research tools"
  - "You edit Wikipedia and need talk pages, watchlists, or other editor tools (use Wikipedia's official app)"
  - "You want the whole encyclopedia stored offline; Kiwix downloads full archives, WanderWiki saves the articles you pick"
  - "You want your reading synced across devices; WanderWiki keeps everything on the device you read on"
  - "You want a free Wikipedia feed with nothing to install; WikiTok is free, open source, and runs in any browser"
  - "You read a Wikipedia edition outside WanderWiki's 32, such as Bengali, Persian, or Urdu"

alternatives_to:
  - "WikiScroll"
  - "WikiTok"
  - "Wikiwand"
  - "Wikipedia app"
  - "Kiwix"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "Wikipedia, the way Random article used to feel."
  story: "We made WanderWiki because Wikipedia is one of the great free things on the internet, and we wanted to read it for fun again. The spare minutes that used to go to Random article on a desktop now go to feeds tuned for time on the app. We wanted that random click back on the phone, made for swiping: you tap Random and end up reading about the history of fountain pens at 11 p.m. WanderWiki came to iPhone in February 2026 and runs on iPad too. It reads 32 Wikipedia language editions, lets you browse 16 topics, remembers where you stopped in every article, and saves articles to read offline. The apps we compared it with, WikiScroll and Wiki Rabbit, are free with ads, and each does something well. We chose to charge for Premium instead, so WanderWiki has no ads and no reason to keep you scrolling. Twenty articles a day stay free."
  signals:
    - "Articles, search, categories, and the On This Day feed come from Wikipedia's official APIs, and images from Wikimedia. There is no Lagerland server in between"
    - "The Privacy Manifest declares no tracking, no tracking domains, and no collected data; the app carries no third-party SDKs"
    - "Paid for by people who buy Premium, with no ads and no investors"
    - "{APP_COUNT} live apps in the catalogue, all with the same data rules: no tracking or ads, and never a required account"
  external_link:
    label: "Read the Lagerland studio backstory"
    href: "/lagerland-apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally, usually within a day."

value_points:
  - title: "Wander instead of search"
    description: "Random pulls from the whole encyclopedia. Browse drops you into one of 16 topics, from Space to Food. Under each article, Where next offers three related ones, so one idea leads to the next, and Back to discovery returns you to the feed."
  - title: "Your reading stays on your device"
    description: "Nobody sees ads in WanderWiki, on any plan. You never sign in, and the app has no analytics and no developer server. Your interests, saved articles, likes, and reading history live on your device, and Delete My Data in Settings erases them in one tap. Like any Wikipedia reader, the app fetches articles from Wikipedia, so Wikimedia sees those requests."
  - title: "A reader that remembers"
    description: "Reopen an article and you are back where you stopped. The reader shows how many minutes an article takes, and your saved and liked lists show how far you got. Listen reads any article aloud, with controls on the Lock Screen, and the reader comes in Sepia, Solarized, or True Black."
  - title: "Five widgets and two controls"
    description: "On This Day puts the day's history, with a photograph, on your Home Screen or Lock Screen. Reading Year, Continue Reading, Got a Minute, and Two Doors fill the rest. Surprise Me and Continue Reading also sit in Control Center, on the Lock Screen, or on the Action button."
  - title: "32 Wikipedia editions"
    description: "Read English, German, Japanese, Arabic, Finnish, and 27 more Wikipedia editions. Today in History uses the edition's own feed in 19 of them and English in the rest. The app's own interface, widgets included, is translated into 33 languages."

how_it_works:
  intro: "WanderWiki is a Wikipedia card deck for iPhone and iPad (iOS 18.2 or later). Articles come from Wikipedia's official APIs, and everything you do with them stays on your device. A session goes like this."
  steps:
    - title: "Pick your Wikipedia language (one of 32)"
      detail: "Choose the Wikipedia edition in Settings, under Language. Random, Browse, and search all read from it. Today in History uses the edition's own On This Day feed in 19 editions and the English one elsewhere. Where For You isn't available for an edition yet, the app shows Random and says so."
    - title: "Pick a few interests from 16 topics"
      detail: "Science, Technology, History, Arts, Music, Sports, Nature, Space, Philosophy, Geography, Literature, Movies, Food, Architecture, Mathematics, and Politics. You pick them at the start and can change them on your Profile. For You builds its feed from them; Browse dives into one."
    - title: "Swipe the deck"
      detail: "Each card shows an article's picture and opening lines. Switch between Random, For You, and Today at the top of the feed, or open Browse for a single topic. On the free plan a chip shows how many of today's 20 articles are left."
    - title: "Tap to read the whole article"
      detail: "The reader shows the full Wikipedia article and how many minutes it takes. Its ••• menu holds Move to folder, Open in Wikipedia, Share, and Reader Theme (System, Sepia, Solarized, True Black). Close an article and reopen it later, and you are back where you stopped; Jump to top takes you to the start. Tap Listen to hear it read aloud."
    - title: "Follow a thread"
      detail: "Under an article, Where next offers three related articles. Tap one to follow the thread; the trail remembers where you came from, and Back to discovery returns you to the feed."
    - title: "Save, sort, and read offline"
      detail: "Save an article and WanderWiki downloads its full text, so it opens without a connection. Saved articles sort into folders with their own colour and icon, and they show up in Spotlight search. Settings shows how much space downloads use and removes them in one tap."
    - title: "Steer the feed"
      detail: "Press and hold a card for Show less like this, Not interested in a topic, or Hide this article. Those choices shape For You and stay on your device."
    - title: "Add widgets and controls"
      detail: "Add On This Day, Reading Year, Continue Reading, Got a Minute, or Two Doors to your Home Screen; most also come in Lock Screen sizes. Put Surprise Me or Continue Reading in Control Center, on the Lock Screen, or on the Action button. Or ask Siri: Surprise me with WanderWiki."

features:
  - title: "Random: the whole encyclopedia"
    description: "Each swipe brings a random article from the Wikipedia edition you chose, with its picture and opening lines. Tap the card to read the rest. Wiki Rabbit draws only from Wikipedia's Good Articles; WanderWiki draws from the full edition."
  - title: "Browse 16 topics"
    description: "Pick Science, History, Space, Food, or any of the other 12 topics, and swipe an endless deck of just that subject. Browse is free and counts toward the daily 20."
  - title: "For You (Premium)"
    description: "A feed built from the topics you picked. Press and hold a card to see less of a topic or hide an article, and For You takes that into account. All of it is worked out on your device. In Wikipedia editions where For You isn't available yet, the app shows Random and tells you."
  - title: "Today in History (Premium)"
    description: "Wikipedia's On This Day for today's date, from <a href=\"https://en.wikipedia.org/api/rest_v1/#/Feed/onThisDay\" rel=\"noopener\" target=\"_blank\">Wikipedia's official feed</a>. Switch between Highlights, Events, Births, Deaths, and Holidays. It uses your edition's own feed in 19 of the 32 editions and English elsewhere."
  - title: "A reader that picks up where you stopped"
    description: "The full article in a clean reading view, with the reading time at the top and four themes: System, Sepia, Solarized, and True Black. Reopen an article and you are back at your place. Saved and liked lists show a progress ring and mark what you finished. Open in Wikipedia is in the ••• menu."
  - title: "Listen"
    description: "Have any article read aloud in the best voice installed for its language. Play and pause from the Lock Screen, and keep listening with the screen locked."
  - title: "Saved articles offline, in folders"
    description: "Saving an article downloads its full text, so it opens on a plane or in a tunnel; an Offline copy badge marks it. Sort saves into folders and find them from Spotlight. The swipe feed itself needs a connection."
  - title: "Five widgets and two controls"
    description: "On This Day (the day's history with a photograph; shuffle it or choose events, births, deaths, or holidays), Reading Year (your streak and every day you finished an article), Continue Reading, Got a Minute (choose 2, 5, 10, or 20 minutes and it picks a saved or started article that fits), and Two Doors (one article near your interests, one far from them). On iOS 27, On This Day and Reading Year can fill a whole page. Surprise Me and Continue Reading work as controls in Control Center, on the Lock Screen, and on the Action button."
  - title: "Search, Where next, Siri, and sharing"
    description: "Search your Wikipedia edition from the feed. Where next offers three related articles under each one. Siri and Shortcuts can open a random article, today's history, or one of your topics. Share an article as a link or as a card image in Story or Square format."
  - title: "A streak and a daily article, if you want them"
    description: "WanderWiki counts the days in a row you read something, on your Profile and in the Reading Year widget, and a weekly recap shows your week of discovery. Turn on notifications and a daily one, at 9:00 unless you change it, names the day's featured article; an optional reminder warns you when a streak is about to break. Set quiet hours or turn both off in Settings."

screenshots:
  - src: "/assets/screenshots/wanderwiki/1.webp"
    alt: "WanderWiki feed on iPhone showing one Wikipedia article as a full-screen card to swipe"
  - src: "/assets/screenshots/wanderwiki/2.webp"
    alt: "WanderWiki Browse screen with tiles for the 16 topics"
  - src: "/assets/screenshots/wanderwiki/3.webp"
    alt: "WanderWiki Where next chips suggesting three related articles to the one you are reading"
  - src: "/assets/screenshots/wanderwiki/4.webp"
    alt: "WanderWiki For You feed built from the topics you picked"
  - src: "/assets/screenshots/wanderwiki/5.webp"
    alt: "WanderWiki Today in History showing what happened on this day"
  - src: "/assets/screenshots/wanderwiki/6.webp"
    alt: "WanderWiki saved articles downloaded for offline reading"
  - src: "/assets/screenshots/wanderwiki/7.webp"
    alt: "WanderWiki extra-large On This Day widget showing a whole page of history"

comparison_table:
  intro: "Each row is a question readers ask when picking a swipe-Wikipedia app. WikiScroll is the closest native rival and runs on ads; Wiki Rabbit is free with ads and draws only from Good Articles; Wikipedia's official app is the encyclopedia itself."
  competitors: ["WanderWiki", "WikiScroll", "Wiki Rabbit", "Wikipedia (official)"]
  rows:
    - feature: "Number of Wikipedia language editions"
      values: ["32", "Multiple; count not published", "Not published; English-only listing", "All 300+, but made for search, not swipe"]
    - feature: "Pricing model"
      values: ["Free for 20 articles a day; Premium {P_MONTHLY}/mo · {P_YEARLY}/yr · {P_LIFETIME} lifetime", "Free with ads; premium from $4.99/week", "Free with ads", "Free, no ads"]
    - feature: "Source article scope"
      values: ["The full Wikipedia edition you choose", "Random Wikipedia articles", "Good Articles collection only", "Full Wikipedia"]
    - feature: "Today in History (this day in the past)"
      values: ["Yes: Highlights, Events, Births, Deaths, Holidays (Premium)", "Yes, Timeline Mode", "No", "Yes, in the Explore feed"]
    - feature: "Interest-based discovery"
      values: ["Yes: 16 topics you pick; Browse one topic free", "Yes: personalised feed from topics you choose", "Yes: 'Session For You', adapts to what you open, skip, and linger on", "Limited: Explore feed"]
    - feature: "Widgets"
      values: ["Yes: 5 widgets, Lock Screen sizes, Control Center controls", "Yes: Home Screen", "No", "Yes"]
    - feature: "Picture of the Day support"
      values: ["No (use Wikipedia's official app)", "Not listed", "No", "Yes, in Explore feed and widget"]
    - feature: "Offline saved articles + folders"
      values: ["Yes: full text offline, sorted into folders", "Save for later; offline not listed", "Bookmarks only", "Yes: reading lists"]
    - feature: "Ads and tracking"
      values: ["No ads or tracking, and no account; your choices stay on the device", "App Store label: Data Used to Track You", "Session-scoped personalisation (resets each session)", "No. Official app, no ads"]
    - feature: "Platforms"
      values: ["iPhone and iPad (iOS 18.2+)", "iPhone (iOS 15+)", "iPhone (iOS 17.6+)", "iPhone, iPad, Mac, Web"]
  footnote: "Competitor pricing and features reflect each app's public App Store page as of 2026-10-25. WikiScroll shows ads and sells premium options in the app; Wiki Rabbit is free and shows ads; Wikipedia's official app is free, ad-free, and built and operated by the Wikimedia Foundation. Apps change often, so check before switching. WanderWiki is independent and is not affiliated with or endorsed by the Wikimedia Foundation; Wikipedia content is used under the Creative Commons Attribution-ShareAlike 4.0 license."

plateau_disclosure:
  title: "What WanderWiki won't do for you"
  rule: "WanderWiki is a Wikipedia reading deck for iPhone and iPad. It leaves out research and editing tools on purpose, which keeps it focused on reading."
  what_it_does_not_do: "WanderWiki gives you no Wikipedia edit access, talk pages, or watchlists; Wikipedia's official app does that. It runs on iPhone and iPad only, with no Mac, Apple Watch, Android, or web version. It reads 32 of Wikipedia's editions and gets Today in History in the edition's own language in 19 of them, in English elsewhere. It does not translate articles. It has no highlights, notes, or citation tools, and no export. It does not sync between devices: your saved articles, likes, and progress stay on the device you use, and deleting the app deletes them. Articles are live Wikipedia content, so they can change, and they can be wrong. It shows no ads on any plan."
  notes:
    - "Want a free Wikipedia feed on a laptop, or in any browser? WikiTok runs at wikitok.io, free and open source, in 41 editions."
    - "Want article-level explanations of why each article was chosen? Wiki Rabbit ships that today, on a free-with-ads tier."
    - "Want Wikipedia editor tools (edit, talk, watchlist, contributions)? Wikipedia's official app is built for that."
    - "Want Picture of the Day or trending articles? Wikipedia's official app shows both in its Explore feed and widget. WanderWiki sticks to swipeable article discovery."
    - "Want all of Wikipedia stored offline? Kiwix downloads full archives."

training_vocabulary:
  overline: "Speaks Wikipedia's language, in 32 of them"
  heading: "The 32 Wikipedia editions, 16 topics, and 5 Today in History categories."
  intro: "WanderWiki reads 32 Wikipedia language editions, offers 16 interest topics, and shows Wikipedia's On This Day in five categories."
  groups:
    - heading: "32 Wikipedia language editions"
      items:
        - "European (Latin script): en, de, fr, es, it, pt, nl, pl, fi, sv, da, no (Bokmål), cs, sk, hu, ro, hr, ca, tr"
        - "European (non-Latin script): ru, uk, el, he"
        - "Asian: ja, zh, ko, hi, vi, id, th, ms"
        - "Middle Eastern: ar"
    - heading: "16 interest topics"
      items:
        - "Science · Technology · History · Arts"
        - "Music · Sports · Nature · Space"
        - "Philosophy · Geography · Literature · Movies"
        - "Food · Architecture · Mathematics · Politics"
    - heading: "5 Today in History categories"
      items:
        - "Highlights: Wikipedia's curated picks for the date"
        - "Events: what happened on this date in any year"
        - "Births: notable people born on this date"
        - "Deaths: notable people who died on this date"
        - "Holidays: holidays observed on this date"
        - "Edition's own feed in 19 editions (en, de, fr, es, it, pt, nl, pl, fi, sv, tr, ru, uk, cs, ja, zh, ko, hi, ar); English elsewhere"
    - heading: "Data sources and privacy"
      items:
        - "Wikipedia REST API for summaries, article text, random articles, and On This Day"
        - "Wikipedia Action API for categories, search, and related pages"
        - "Images from Wikimedia's image server"
        - "Content licensed CC BY-SA 4.0; the license is shown in Settings, and Open in Wikipedia is in the reader"
        - "Privacy Manifest: no tracking, no tracking domains, no collected data; no third-party SDKs"

example_insights:
  overline: "What WanderWiki shows you"
  heading: "Sample cards from real Wikipedia data"
  intro: "Today in History reads Wikipedia's official On This Day feed, the same data Wikipedia shows on its own front page, in your edition's language in 19 editions and in English elsewhere. Here is what a few cards look like."
  cards:
    - tag: "May 13 · Births"
      headline: "Stevie Wonder was born on May 13, 1950."
      body: "Born in Saginaw, Michigan, he signed to Motown at 11 and went on to make Songs in the Key of Life. Other May 13 birthdays include Daphne du Maurier (1907), Bea Arthur (1922), and Robert Pattinson (1986)."
    - tag: "May 13 · Events"
      headline: "The United States declared war on Mexico on May 13, 1846."
      body: "The Mexican-American War followed the US annexation of Texas. Other May 13 entries include Brazil's Golden Law abolishing slavery (1888) and the first Formula One World Championship race, at Silverstone (1950)."
    - tag: "Got a Minute · Widget"
      headline: "Five minutes before the bus? Pick 5."
      body: "Set the Got a Minute widget to 2, 5, 10, or 20 minutes and it picks one of your saved, started, or downloaded articles that fits the time. The reading time comes from the article's length."
    - tag: "Folders · Habit"
      headline: "A flights folder that fills up as you read."
      body: "Save articles as you come across them, and their full text downloads for offline reading. Sort them into folders, such as flights, before bed, or philosophy, and the flights folder becomes a reading list for the next trip."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads on any plan, and no third-party trackers or analytics SDKs"
    - "No account or sign-up"
    - "No WanderWiki server: articles come straight from Wikipedia's official APIs, so Wikimedia sees those requests, as with any Wikipedia reader"
    - "Interests, saved articles, folders, likes, hidden articles, reading progress, and your streak stay on your device; Delete My Data in Settings erases them"
    - "Where a one-line AI summary appears (it needs Apple Intelligence), it is written on the device and never sent anywhere"
    - "Purchases go through Apple; the app never sees your payment details"
    - "Wikipedia content is used under the <a href=\"https://creativecommons.org/licenses/by-sa/4.0/\" rel=\"noopener\" target=\"_blank\">Creative Commons CC BY-SA 4.0</a> license, shown in Settings; every article opens in Wikipedia from the reader"
    - "See the per-app <a href=\"/transparency/#wanderwiki\">Privacy Manifest</a> for the declared API usage and tracking-domain list (it's empty)"

faq:
  - q: "What is WanderWiki?"
    a: "WanderWiki is an iPhone and iPad app (iOS 18.2 or later) for reading Wikipedia by swiping instead of searching. Random brings articles from the whole encyclopedia, Browse narrows the deck to one of 16 topics, and tapping a card opens the full article in a clean reader that remembers where you stopped. It covers 32 Wikipedia language editions. Saved articles download for offline reading, any article can be read aloud, and five widgets bring it to the Home Screen and Lock Screen. It is free for 20 articles a day; Premium adds For You, Today in History, and unlimited swiping for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once. There are no ads and no account."
  - q: "How is WanderWiki different from WikiScroll?"
    a: "Both let you swipe through random Wikipedia articles, and both have a this-day-in-history mode, topic picks, saves, and widgets. WikiScroll is free with ads, sells premium in the app, and its App Store privacy label says data may be used to track you; it runs on iPhones back to iOS 15. WanderWiki shows no ads and does no tracking. It is free for 20 articles a day, with Premium from {P_MONTHLY}/month or {P_LIFETIME} once, and adds saved articles that open offline, folders, read-aloud, and 32 Wikipedia editions, on iPhone and iPad from iOS 18.2. The full comparison is on the <a href=\"/alternatives/wikiscroll/\">WikiScroll alternative page</a>."
  - q: "How is WanderWiki different from Wiki Rabbit?"
    a: "Wiki Rabbit is free with ads and draws only from Wikipedia's curated Good Articles. WanderWiki has no ads on any plan and draws from the full Wikipedia edition you choose, in 32 languages. Wiki Rabbit adapts during a session to what you open, skip, and linger on, and explains why each article was picked. WanderWiki's For You starts from the 16 topics you choose and the topics or articles you ask it to hide, all worked out on your device. Pick Wiki Rabbit for the explanations; pick WanderWiki for no ads, full Wikipedia, several languages, offline saves, and widgets."
  - q: "Is WanderWiki an official Wikipedia app?"
    a: "No. WanderWiki is an independent app from Lagerland Apps. It reads Wikipedia content through Wikipedia's official APIs under the Creative Commons Attribution-ShareAlike 4.0 license, which is shown in Settings, and every article opens in Wikipedia from the reader. WanderWiki is not affiliated with or endorsed by the Wikimedia Foundation. For editing, talk pages, and watchlists, use Wikipedia's official app."
  - q: "Which Wikipedia language editions does WanderWiki support?"
    a: "Thirty-two: English, German, French, Spanish, Italian, Portuguese, Dutch, Polish, Finnish, Swedish, Danish, Norwegian Bokmål, Czech, Slovak, Hungarian, Romanian, Croatian, Catalan, Turkish, Russian, Ukrainian, Greek, Hebrew, Japanese, Chinese, Korean, Hindi, Vietnamese, Indonesian, Thai, Malay, and Arabic. Random, Browse, and search read from the edition you pick. Today in History uses the edition's own feed in 19 of them and English elsewhere. Where For You isn't available for an edition yet, the app shows Random and tells you."
  - q: "How does the For You mode work?"
    a: "You pick interests from 16 topics: Science, Technology, History, Arts, Music, Sports, Nature, Space, Philosophy, Geography, Literature, Movies, Food, Architecture, Mathematics, and Politics. For You then builds a feed from the Wikipedia categories behind those topics. Press and hold a card to see less like it, mark a topic as not interesting, or hide an article, and For You adjusts. Those choices stay on your device. For You is part of Premium; Browse, which dives into one topic, is free."
  - q: "How does Today in History work?"
    a: "Today in History shows Wikipedia's On This Day feed for today's date. Switch between five categories: Highlights (Wikipedia's picks for the date), Events, Births, Deaths, and Holidays. It reads your edition's own feed in 19 of the 32 editions and the English feed elsewhere. In the app it is part of Premium. The On This Day widget, with a photograph of the day's history, is free."
  - q: "Does WanderWiki have widgets?"
    a: "Yes, five, all free: On This Day (the day's history with a photograph), Reading Year (your streak and every day you finished an article), Continue Reading (articles you're partway through), Got a Minute (choose 2, 5, 10, or 20 minutes and it picks an article that fits), and Two Doors (one article near your interests, one far from them). Most also come in Lock Screen sizes, and on iOS 27 On This Day and Reading Year can fill a whole page. Surprise Me and Continue Reading are also controls for Control Center, the Lock Screen, and the Action button."
  - q: "Can I read articles offline?"
    a: "Yes, the ones you save. Saving an article downloads its full text, so it opens without a connection, and you can sort saved articles into folders and find them from Spotlight. A setting turns the downloads off, and Settings shows how much space they use. The swipe feed itself loads live from Wikipedia and needs a connection. Saved articles stay on the device that saved them; there is no iCloud sync."
  - q: "Does WanderWiki use a recommendation algorithm?"
    a: "Only in a small, visible way. Random is random, and Browse sticks to the topic you chose. For You starts from the topics you pick and adjusts when you press and hold a card to see less of something or hide it. That all happens on your device. WanderWiki has no analytics and no server of its own, so nothing about what you read is collected."
  - q: "Does WanderWiki have streaks or notifications?"
    a: "Yes, and both are optional. WanderWiki counts the days in a row you read something, on your Profile and in the Reading Year widget. If you allow notifications (the app asks the first time you save an article), a daily one, at 9:00 unless you change it, names the day's featured article, and a reminder can warn you when a streak is about to break. Change the time, set quiet hours, or turn them off in Settings."
  - q: "Is WanderWiki free?"
    a: "Yes, for 20 articles a day, with no card and no account. The free plan covers Random and Browse, with save, like, search, and folders, plus Listen and all five widgets, in all 32 editions. When you reach 20, the app asks you to upgrade or come back after local midnight, when the count resets. Premium unlocks For You, Today in History, and unlimited swiping for {P_MONTHLY}/month or {P_YEARLY}/year, each with a {TRIAL} for new subscribers, or {P_LIFETIME} once, with Family Sharing. No plan shows ads. The only other purchase is an optional {P_IAP:Support the developer} tip. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does WanderWiki work on iPad, Mac, or Vision Pro?"
    a: "It runs on iPhone and iPad with iOS or iPadOS 18.2 or later, and on iPad it uses a sidebar layout. There is no Mac, Apple Vision Pro, Apple Watch, or web version. For a Wikipedia feed in any browser, WikiTok is a free option."
  - q: "Does WanderWiki track my reading?"
    a: "No. WanderWiki carries no analytics or third-party SDKs, needs no account, and has no server of its own. Your saved articles, likes, folders, reading progress, and streak stay on your device, and Delete My Data in Settings erases them. The app's network requests go to Wikipedia, for articles, search, and the On This Day feed, and to Wikimedia's image server for pictures, so Wikimedia sees them as it would for any Wikipedia reader. Purchases go through Apple."

related_journal:
  slug: reading-without-a-feed
  anchor: "Why WanderWiki exists: replacing the social feed with Wikipedia"

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/wanderwiki/support/"

release:
  first_release: "2026-02-07"
  last_updated: "2026-10-23"
  last_audited: "2026-10-25"
  audit_round: "5 (every claim checked against the app source and the live App Store listing)"

ratings:
  value: "5.0"
  count: 2
  last_synced: "2026-04-15"
last_updated: 2026-10-29
---
WanderWiki is a Wikipedia app for iPhone and iPad (iOS 18.2 or later) built for reading without a plan. Instead of a search box, it opens on a deck of cards. Random draws from the whole encyclopedia, Browse narrows the deck to one of 16 topics, and Where next offers three related articles under each one, so a single swipe can turn into an evening's thread.

Tap a card and the full article opens in a clean reader. It shows how long the article takes, remembers where you stopped, and reads aloud when you tap Listen. Save an article and its full text downloads for offline reading; sort your saves into folders and find them from Spotlight. Five widgets and two controls put the day's history, your reading year, and a one-tap Surprise Me on the Home Screen, the Lock Screen, and the Action button.

WanderWiki reads 32 Wikipedia language editions. It shows no ads on any plan, needs no account, and has no analytics or server of its own, so your reading stays on your device. Twenty articles a day are free. Premium adds For You, Today in History, and unlimited swiping for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once. WikiScroll and Wiki Rabbit, its closest rivals, are free with ads. WanderWiki charges for Premium instead, so it has no reason to keep you scrolling.
