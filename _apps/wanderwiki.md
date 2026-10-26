---
layout: app
slug: wanderwiki
name: "WanderWiki"
tagline: "Swipe Wikipedia in 32 languages. Ad-free."
quick_answer: "WanderWiki is a Wikipedia discovery app for iPhone and iPad (iOS 18.2+) that turns the encyclopedia into a swipe-based card deck. Random pulls from the whole encyclopedia, Browse narrows the deck to one of 16 topics, For You blends the topics you pick, and Today in History reads Wikipedia's official On This Day feed in five categories (Selected, Events, Births, Deaths, Holidays). It covers 32 Wikipedia language editions; in 17 of them the topics map to that edition's own categories, so German + Science queries Wissenschaft, Physik and Chemie, not translated English categories. Saved articles download for offline reading and sort into folders, any article can be read aloud, and five widgets bring On This Day, Continue Reading and more to the Home Screen and Lock Screen. Free for 20 articles a day; WanderWiki Plus adds For You, Today in History and unlimited swiping for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once. It has no ads or behavioral tracking and needs no account."
category: education
status: live

app_store_url: "https://apps.apple.com/app/id6758459119"

price:
  model: freemium
price_lead: "Free (20 articles a day)"
price_tier: "Plus"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The lifetime tier is a one-time purchase that never auto-renews. The App Store's in-app purchase list also shows a $0.99 weekly plan, kept for existing subscribers and no longer sold in the app, and an optional {P_IAP:Support the developer} tip (Support the Developer, in Settings)."
pricing_note: "All prices are listed on the App Store. Cancel anytime. The free plan needs no card and no account: 20 articles a day, reset at midnight."

plans:
  - name: "Free"
    price: "$0"
    summary: "20 articles a day, every day, with no card or account."
    features:
      - "Random and Browse (16 topics): 20 articles a day, reset at local midnight"
      - "Save, like, search, and folders"
      - "All 32 Wikipedia language editions"
      - "Widgets and read-aloud"
  - name: "Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "WanderWiki Plus, billed monthly. Cancel anytime."
    features:
      - "For You: articles from the topics you pick"
      - "Today in History: Wikipedia's On This Day feed"
      - "Unlimited swiping"
      - "Everything in Free"
  - name: "Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same features, billed once a year. ~{SAVE_YEARLY}% cheaper than monthly."
    features:
      - "Everything in Monthly"
      - "~{SAVE_YEARLY}% cheaper than monthly over a year"
      - "Free trial for new subscribers; the paywall shows its length"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "WanderWiki Plus for good, paid once, for about what a year of monthly billing costs."
    features:
      - "Everything in Annual"
      - "One-time purchase, no renewal"
      - "Family Sharing with up to 5 family members at no extra cost"
      - "Future features included"
      - "Restores on every iPhone and iPad signed in with the same Apple ID"
    highlight_label: "Best long-term value"

icon: "/assets/icons/wanderwiki.png"
og_image: "/assets/og/wanderwiki.png"

seo:
  title: "WanderWiki: Swipe Wikipedia in 32 Languages, Ad-Free"
  description: "Swipe Wikipedia in 32 languages: Random, Browse, For You and Today in History, widgets, offline folders. No ads. Free for 20 articles a day."
  keywords:
    - swipe Wikipedia app
    - Wikipedia discovery app iPhone
    - WikiScroll alternative
    - Wiki Rabbit alternative
    - swipe through Wikipedia
    - random Wikipedia articles app
    - Today in History app
    - Wikipedia reader iPhone no ads
    - multilingual Wikipedia app
    - 32 Wikipedia languages
    - educational discovery app iPhone
    - knowledge discovery iPhone
    - curiosity learning app
    - daily learning app
    - Wikipedia widget iPhone
    - On This Day app
    - calm Wikipedia reader
    - doomscroll replacement app
    - Wikipedia card stack iPhone

hero:
  headline: "Swipe. Learn. Repeat."
  secondary: "32 Wikipedia language editions with Random, Browse, For You and Today in History. No ads, no account, and no engagement algorithm."
  subheadline: "WanderWiki turns Wikipedia into a swipe-based card deck on iPhone and iPad, across 32 Wikipedia language editions (English, German, French, Japanese, Chinese, Korean, Hindi, Arabic, Finnish, and 23 more). There are four ways in (Random across the full encyclopedia · Browse one of 16 topics · For You across the topics you pick · Today in History with five subcategories from Wikipedia's official REST API), plus saved articles that download for offline reading and sort into folders, read-aloud, and five widgets. Free for 20 articles a day; WanderWiki Plus from {P_MONTHLY}/month or {P_LIFETIME} lifetime. No ads. Wikipedia content comes from its official APIs and is used under CC BY-SA 4.0."
  cta_label: "Try Free"
  alt: "WanderWiki Wikipedia article card being swiped through on iPhone, in a discovery deck"
  video: "/assets/videos/wanderwiki_preview.mov"
  video_poster: "/assets/videos/wanderwiki-poster.jpg"

who_for:
  - "You browse Wikipedia for fun and want discovery without searching first"
  - "You read Wikipedia in more than one language (or want to start); WanderWiki carries 32 language editions"
  - "You want a calm replacement for doomscrolling that doesn't sell your attention to advertisers"
  - "You loved 'Random Article' on desktop Wikipedia and want that ritual on iPhone or iPad"
  - "You want saved articles that open offline, organised in folders, for flights, commutes, or quiet reading"
  - "You want widgets that put today's history, or two articles to choose between, on your Home Screen or Lock Screen"

who_not_for:
  - "You want academic-grade citations, references, and source-checking; WanderWiki is a reading deck without research tools"
  - "You need edit access, talk pages, or other Wikipedia editor features (use Wikipedia's official app)"
  - "You want curated long-form magazine content (Curio or Apple News+ fit better)"
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
  heading: "Wikipedia, the way 'Random Article' used to feel."
  story: "We made WanderWiki because Wikipedia is the best free thing on the internet and almost nobody reads it for fun anymore. The five-minute windows that used to go to 'Random Article' on desktop now go to algorithmic feeds on the iPhone, tuned for time-on-app. We wanted Random Article back on the phone, made for swiping: the desktop ritual where you click 'Random' and end up reading about the history of fountain pens at 11pm. WanderWiki launched on iPhone in February 2026 and now runs on iPad too (iOS 18.2+): 32 Wikipedia language editions, with topics mapped to the edition's own categories in 17 of them (pick German + Science and the app queries Wissenschaft, Physik, Chemie instead of translated English categories), four ways to wander, widgets, read-aloud, and saved articles that open offline in folders. The apps we compared it with, WikiScroll and Wiki Rabbit, are both free with ads, and each does something well. We chose to charge for the app so it has no ads, no algorithm to maximise time-on-app, and no behavioral tracking. Free for 20 articles a day; WanderWiki Plus from {P_MONTHLY}/month or {P_LIFETIME} lifetime. The maker uses it every morning."
  signals:
    - "Built on Wikipedia's official APIs: the REST API for articles and the On This Day feed (api/rest_v1/feed/onthisday/), the Action API for categories, search, and related pages. Nothing is scraped or crawled, and no Lagerland server caches articles"
    - "32 Wikipedia language editions, defined once in the WanderWikiShared package that the app and its widgets share, with a unit test that keeps the two in step"
    - "Privacy Manifest declares no tracking and no tracking domains; no third-party SDKs; reading data stays on the device in SwiftData"
    - "Paid for by people buying the app, with no ads, investor pressure, or engagement telemetry"
    - "{APP_COUNT} live apps in the catalogue, all with the same data rules: no tracking, no ads, and no required accounts"
  external_link:
    label: "Read the Lagerland studio backstory"
    href: "/lagerland-apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally, usually within a day."

value_points:
  - title: "32 Wikipedia language editions"
    description: "English, German, French, Spanish, Japanese, Chinese, Korean, Italian, Portuguese, Russian, Finnish, Swedish, Dutch, Polish, Turkish, Arabic, Hindi, Vietnamese, Indonesian, Thai, Ukrainian, Czech, Danish, Norwegian (Bokmål), Malay, Hebrew, Greek, Hungarian, Romanian, Slovak, Catalan, Croatian. In the first 17, topics map to the edition's own categories; in the rest, For You and Browse fall back to random articles from that edition, and the app tells you. WikiScroll lets you pick a reading language but doesn't say how many; Wiki Rabbit's listing is English-only."
  - title: "Four ways to wander"
    description: "Random draws from the entire encyclopedia. Browse drops you into one of 16 topics. For You blends the topics you choose and uses no behavioral tracking. Today in History pulls Wikipedia's official On This Day feed (5 subcategories: Selected, Events, Births, Deaths, Holidays). Random and Browse are free; For You and Today in History come with WanderWiki Plus."
  - title: "Widgets, folders, offline reading, read-aloud"
    description: "Five widgets (On This Day, Reading Year, Continue Reading, Got a Minute, and Two Doors), most in Lock Screen sizes too, plus Surprise Me and Continue Reading controls for Control Center. Save any article and its full text downloads for offline reading; sort saves into folders; tap Listen to have it read aloud."
  - title: "No ads, no algorithm, no account"
    description: "WikiScroll and Wiki Rabbit both show ads. WanderWiki is free for 20 articles a day and charges from {P_MONTHLY}/month or {P_LIFETIME} lifetime for Plus, so the app has no commercial reason to maximise your screen time. It needs no account and does no behavioral tracking."
  - title: "{P_LIFETIME} once, about a year of monthly billing"
    description: "WanderWiki Plus is {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once with Family Sharing, and the free tier already covers all 32 editions. Wikipedia's official app carries all 300+ editions but is made for searching, not swiping; WikiTok's free web feed covers 41 editions but has no app, topics, or offline saves."

how_it_works:
  intro: "WanderWiki is a Wikipedia card deck on iPhone and iPad (iOS 18.2+). The data comes from Wikipedia's official APIs; everything you do with it stays on the device in SwiftData. A session goes like this."
  steps:
    - title: "Pick your Wikipedia language (one of 32)"
      detail: "WanderWiki starts on English Wikipedia; switch to any of the other 31 editions in Settings, including German, French, Spanish, Japanese, Chinese, Korean, Hindi, Arabic, and Finnish. The choice applies everywhere: Random pulls from that edition; in the 17 editions with mapped categories, For You and Browse query that edition's own category names (German Science queries Wissenschaft, Physik, Chemie instead of translated English categories); Today in History uses the edition's own On This Day feed where Wikipedia publishes one (19 of the 32) and the English feed otherwise. Switch any time."
    - title: "Pick interests across 16 topics"
      detail: "Sixteen topics ship in WanderWiki: Science, Technology, History, Arts, Music, Sports, Nature, Space, Philosophy, Geography, Literature, Movies, Food, Architecture, Mathematics, Politics. Each maps to a hand-picked list of Wikipedia categories: around 50 in English, about a dozen in each of the other 16 mapped editions. For You blends the topics you pick; Browse lets you dive into one."
    - title: "Open the deck and swipe"
      detail: "Swipe up for the next card; tap a card to open the article. Switch between Random, For You, and Today in History at the top of the feed, or open Browse for a single topic. Each card shows the article's lead image, title, and opening lines. When an article pulls you in, Where Next offers three related articles to follow."
    - title: "Tap to read the full article"
      detail: "Articles open in a reader built on Wikipedia's mobile HTML, with edit pencils, infoboxes, navboxes, and reference lists hidden. Pick one of four reader themes (System, Sepia, Solarized, True Black); the reader remembers where you stopped and shows the reading time. Tap Listen to hear the article read aloud. Open in Wikipedia is one tap away in the toolbar, and the CC BY-SA 4.0 content license is linked in Settings."
    - title: "Save for offline, organise in folders"
      detail: "Save any article with one tap and WanderWiki downloads its full text, so it opens without a connection on flights, in subway tunnels, or in that one corner of the cabin. Organise saved articles into folders by topic, project, or whatever shape your curiosity has this month. Saved articles also show up in Spotlight search."
    - title: "Like what you love, hide what you don't (on-device)"
      detail: "Likes collect in your Liked list. 'Show less like this' or 'Hide this article' keeps that article out of your Where Next suggestions. For You itself follows only the topics you picked. Nothing is inferred from what you like, skip, or linger on, and none of these signals leave your device."
    - title: "Today in History as a daily ritual"
      detail: "WanderWiki queries Wikipedia's REST API endpoint /api/rest_v1/feed/onthisday/<category>/<MM>/<DD> for the five canonical Wikipedia On This Day categories: Selected, Events, Births, Deaths, Holidays. In the app it's part of WanderWiki Plus; the On This Day widget brings the day's moments, with photographs, to your Home Screen, something small to read each morning."
    - title: "Five widgets"
      detail: "Five widgets: On This Day; Reading Year (your streak and every day you finished an article); Continue Reading (the articles you're partway through); Got a Minute (pick 2, 5, 10, or 20 minutes and it picks one of your articles that fits); and Two Doors (one article close to your interests, one far outside them). Most come in Lock Screen sizes. Surprise Me and Continue Reading are also controls for Control Center, the Lock Screen, and the Action button. The widgets read the same language list as the app, from the shared WanderWikiShared package."

features:
  - title: "32 Wikipedia language editions, with native-language category queries in 17"
    description: "WanderWiki reads English, German, French, Spanish, Japanese, Chinese, Korean, Italian, Portuguese, Russian, Finnish, Swedish, Dutch, Polish, Turkish, Arabic, Hindi, Vietnamese, Indonesian, Thai, Ukrainian, Czech, Danish, Norwegian (Bokmål), Malay, Hebrew, Greek, Hungarian, Romanian, Slovak, Catalan, and Croatian Wikipedia. In the first 17, each topic maps to that edition's own categories: pick German + Science and the app queries Wissenschaft, Physik, Chemie, Biologie instead of translated English category names. In the other 15, For You and Browse fall back to random articles from the edition you chose. WikiScroll doesn't publish its language count; Wiki Rabbit's listing is English-only."
  - title: "Random: the whole encyclopedia"
    description: "Each swipe brings a random article from your selected Wikipedia edition, through Wikipedia's random-article endpoint. The app skips disambiguation pages, lists, and stubs too short to summarise. Wiki Rabbit draws only from Wikipedia's Good Articles collection; WanderWiki draws from the full encyclopedia (~7 million articles in English alone)."
  - title: "Browse and For You: 16 topics, chosen by you"
    description: "Browse drops you into one topic, free within the daily 20. For You (WanderWiki Plus) blends the topics you pick: Science, Technology, History, Arts, Music, Sports, Nature, Space, Philosophy, Geography, Literature, Movies, Food, Architecture, Mathematics, Politics. It follows the topics you chose and nothing else; no recommendation algorithm learns from your dwell time, scroll velocity, likes, or behavioral profile."
  - title: "Today in History: Wikipedia's official On This Day feed, five categories"
    description: "Uses <a href=\"https://en.wikipedia.org/api/rest_v1/#/Feed/onThisDay\" rel=\"noopener\" target=\"_blank\">Wikipedia's official REST API</a> endpoint <code>/api/rest_v1/feed/onthisday/&lt;category&gt;/&lt;MM&gt;/&lt;DD&gt;</code>. Five canonical categories: Selected (curated highlights), Events, Births, Deaths, Holidays. In your edition's own language where Wikipedia publishes the feed (19 of the 32 editions), in English otherwise. Part of WanderWiki Plus in the app; the On This Day widget works on every tier."
  - title: "Five widgets and two controls"
    description: "On This Day, Reading Year, Continue Reading, Got a Minute, and Two Doors, with Lock Screen sizes for most of them and full-page layouts on iOS 27. Surprise Me and Continue Reading also work as controls in Control Center, on the Lock Screen, and on the Action button."
  - title: "Saved articles offline, in folders, and read aloud"
    description: "Save any article with one tap; its full text downloads so it reads offline (flights, transit tunnels, anywhere off-grid). Organise saved articles into folders, find them from Spotlight, and pick up where you stopped, since the reader remembers your place. Listen mode reads any article aloud, with play and pause on the Lock Screen."
  - title: "Calm formatting, linked back to Wikipedia"
    description: "Articles are reformatted for phone and tablet screens: the original Wikipedia text, properly typeset, without sidebars, infoboxes, or auto-played media, in four reader themes. Open in Wikipedia is one tap away in the reader, shared images credit Wikipedia, and the <a href=\"https://creativecommons.org/licenses/by-sa/4.0/\" rel=\"noopener\" target=\"_blank\">CC BY-SA 4.0</a> content license is linked in Settings."
  - title: "Search, Where Next, Siri, and on-device summaries"
    description: "Search the Wikipedia edition you read. Where Next offers three related articles when you want to keep going. Siri and the Shortcuts app can open a surprise article, today's history, or one of your topics. On iPhones and iPads with Apple Intelligence (iOS 26+), cards can show a one-line summary generated on the device."
  - title: "A reading streak and one daily reminder"
    description: "WanderWiki counts the days in a row you discover a new article, on your Profile and in the Reading Year widget. If you allow notifications (it asks the first time you save an article), it sends one reminder a day, at 9:00 unless you change it, usually naming one of the day's On This Day picks. Change the time, set quiet hours, or turn it off in Settings."
  - title: "Built on Wikipedia's official APIs, with no backend"
    description: "Articles, summaries, categories, search, and On This Day feeds all come from <a href=\"https://en.wikipedia.org/api/rest_v1/\" rel=\"noopener\" target=\"_blank\">Wikipedia's official REST API</a> and its Action API, and images from Wikimedia's image server. Nothing is scraped or crawled, and no Lagerland server caches your reading. Likes, saved articles, folders, reading progress, your streak, and weekly stats all live in SwiftData on your device."

screenshots:
  - src: "/assets/screenshots/wanderwiki/1.png"
    alt: "WanderWiki feed that scrolls Wikipedia like a social feed"
  - src: "/assets/screenshots/wanderwiki/2.png"
    alt: "WanderWiki browse screen with topic tiles"
  - src: "/assets/screenshots/wanderwiki/3.png"
    alt: "WanderWiki trail suggesting three related pages from the one you are reading"
  - src: "/assets/screenshots/wanderwiki/4.png"
    alt: "WanderWiki For You feed tuned to your interests"
  - src: "/assets/screenshots/wanderwiki/5.png"
    alt: "WanderWiki On This Day in history"
  - src: "/assets/screenshots/wanderwiki/6.png"
    alt: "WanderWiki saved articles available offline"
  - src: "/assets/screenshots/wanderwiki/7.png"
    alt: "WanderWiki extra-large widget showing a whole page of history"

comparison_table:
  intro: "Each row is a question readers ask when picking a swipe-Wikipedia app. WikiScroll is the closest native rival and runs on ads; Wiki Rabbit is free with ads and draws only from Good Articles; Wikipedia's official app is the encyclopedia itself."
  competitors: ["WanderWiki", "WikiScroll", "Wiki Rabbit", "Wikipedia (official)"]
  rows:
    - feature: "Number of Wikipedia language editions"
      values: ["32, 17 with native-language category queries", "Multiple; count not published", "Not published; English-only listing", "All 300+, but made for search, not swipe"]
    - feature: "Pricing model"
      values: ["Free for 20 articles a day; Plus {P_MONTHLY}/mo · {P_YEARLY}/yr · {P_LIFETIME} lifetime", "Free with ads; premium from $4.99/week", "Free with ads", "Free, no ads"]
    - feature: "Source article scope"
      values: ["Full Wikipedia (~7M articles in en alone)", "Random Wikipedia articles", "Good Articles collection only", "Full Wikipedia"]
    - feature: "Today in History (this day in the past)"
      values: ["Yes, all 5 On This Day categories (Plus)", "Yes, Timeline Mode", "No", "Yes, in the Explore feed"]
    - feature: "Interest-based discovery"
      values: ["Yes: 16 topics you pick; Browse one topic free", "Yes: personalised feed from topics you choose", "Yes: 'Session For You', adapts to what you open, skip, and linger on", "Limited: Explore feed"]
    - feature: "Widgets"
      values: ["Yes: 5 widgets, Lock Screen sizes, Control Center controls", "Yes: Home Screen", "No", "Yes"]
    - feature: "Picture of the Day support"
      values: ["No (use Wikipedia's official app)", "Not listed", "No", "Yes, in Explore feed and widget"]
    - feature: "Offline saved articles + folders"
      values: ["Yes: full text offline, sorted into folders", "Save for later; offline not listed", "Bookmarks only", "Yes: reading lists"]
    - feature: "Behavioral tracking / engagement-optimised algorithm"
      values: ["No. For You follows only the topics you pick; App Store label: Data Not Collected", "App Store label: Data Used to Track You", "Session-scoped personalisation (resets each session)", "No. Official app, no ads"]
    - feature: "Platforms"
      values: ["iPhone and iPad (iOS 18.2+); Apple-silicon Mac and Vision Pro via the iPad app", "iPhone (iOS 15+)", "iPhone (iOS 17.6+)", "iPhone, iPad, Mac, Web"]
  footnote: "Competitor pricing and features reflect each app's public App Store page as of 2026-10-25. WikiScroll shows ads and sells premium options in the app; Wiki Rabbit is free and shows ads; Wikipedia's official app is free, ad-free, and built and operated by the Wikimedia Foundation. Apps change often, so check before switching. WanderWiki is independent and is not affiliated with or endorsed by the Wikimedia Foundation; Wikipedia content is used under the Creative Commons Attribution-ShareAlike 4.0 license."

plateau_disclosure:
  title: "What WanderWiki won't do for you"
  rule: "WanderWiki is a Wikipedia reading deck for iPhone and iPad. It deliberately leaves out research and editing tools, which keeps it ad-free, on-device, and focused."
  what_it_does_not_do: "WanderWiki will not give you Wikipedia edit access, talk pages, or watchlists; use Wikipedia's official app for that. It has no web or desktop version; the App Store also offers it on Apple-silicon Macs and Apple Vision Pro, where the iPad app runs as is. It will not auto-translate articles into a language they aren't already published in, because translation is up to Wikipedia's editors. It reads 32 editions of roughly 340, maps topics to native categories in 17 of them, and gets Today in History in the edition's own language in 19 (English otherwise). It hides reference lists in the reader and offers no citation management. It does not sync between devices yet; saved articles stay on the device that saved them. It will not run a recommendation algorithm trained on your behavior; For You follows the topics you pick. It will not show banner ads on any tier."
  notes:
    - "Want a free Wikipedia feed on a laptop, or in any browser? WikiTok runs at wikitok.io, free and open source, in 41 editions."
    - "Want article-level explanations of why each article was chosen? Wiki Rabbit ships that today, on a free-with-ads tier."
    - "Want Wikipedia editor tools (edit, talk, watchlist, contributions)? Wikipedia's official app is built for that."
    - "Want Picture of the Day or trending articles? Wikipedia's official app shows both in its Explore feed and widget. WanderWiki sticks to swipeable article discovery."
    - "Want long-form curated magazine content? Curio (audio articles) and Apple News+ fit better."

training_vocabulary:
  overline: "Speaks Wikipedia's language, in 32 of them"
  heading: "The 32 Wikipedia editions, 16 topics, and 5 On This Day categories."
  intro: "WanderWiki reads 32 Wikipedia language editions, sixteen interest topics with native-language category queries in 17 of those editions, and the five canonical On This Day categories from Wikipedia's official REST API."
  groups:
    - heading: "32 Wikipedia language editions"
      items:
        - "European (Latin script): en, de, fr, es, it, pt, nl, pl, fi, sv, da, no (Bokmål), cs, sk, hu, ro, hr, ca, tr"
        - "European (non-Latin script): ru, uk, el, he"
        - "Asian: ja, zh, ko, hi, vi, id, th, ms"
        - "Middle Eastern: ar"
        - "Native category lists for For You and Browse: en, de, fr, es, it, pt, nl, pl, fi, sv, tr, ru, ja, zh, ko, hi, ar"
    - heading: "16 interest topics"
      items:
        - "Science · Technology · History · Arts"
        - "Music · Sports · Nature · Space"
        - "Philosophy · Geography · Literature · Movies"
        - "Food · Architecture · Mathematics · Politics"
        - "Each maps to around 50 Wikipedia categories in English and about a dozen in each of the other 16 mapped editions"
    - heading: "5 Today-in-History categories"
      items:
        - "Selected: Wikipedia's curated highlights for the date"
        - "Events: what happened on this date in any year"
        - "Births: notable people born on this date"
        - "Deaths: notable people who died on this date"
        - "Holidays: holidays observed on this date"
        - "Edition's own feed in 19 editions (en, de, fr, es, it, pt, nl, pl, fi, sv, tr, ru, uk, cs, ja, zh, ko, hi, ar); English elsewhere"
    - heading: "Architecture & data sources"
      items:
        - "Wikipedia REST API: /page/random/summary, /page/summary, /page/mobile-html, /feed/onthisday/&lt;category&gt;/&lt;MM&gt;/&lt;DD&gt;"
        - "Wikipedia Action API: category members, search, related pages"
        - "SwiftUI + SwiftData + StoreKit 2 + WidgetKit + App Intents"
        - "App and widget extension share one language list (WanderWikiShared), checked by a unit test"
        - "Content licensed CC BY-SA 4.0; license linked in Settings, Open in Wikipedia in the reader"
        - "Privacy Manifest declares no tracking and zero tracking domains; no third-party SDKs"

example_insights:
  overline: "What a Today-in-History card looks like"
  heading: "Sample cards from real Wikipedia data"
  intro: "Today in History pulls Wikipedia's official On This Day feed, the same data Wikipedia shows on its own homepage and serves via /api/rest_v1/feed/onthisday/. These are the kinds of cards the deck shows every day, in your edition's own language in 19 editions and in English elsewhere."
  cards:
    - tag: "May 13 · Birth"
      headline: "Stevie Wonder was born on May 13, 1950."
      body: "Born in Saginaw, Michigan, Stevie Wonder signed to Motown at 11, won 25 Grammys, and made Songs in the Key of Life. Today in History (Births) lists him alongside other May 13 birthdays in Wikipedia's feed: Daphne du Maurier (1907), Bea Arthur (1922), and Robert Pattinson (1986)."
    - tag: "May 13 · Event"
      headline: "The United States declared war on Mexico on May 13, 1846."
      body: "The Mexican-American War begins, after the US annexation of Texas. WanderWiki's Today in History (Events) lists it alongside other May 13 entries: Brazil's Golden Law abolishing slavery (1888), the first Formula One World Championship race at Silverstone (1950), and Alison Hargreaves becoming the first woman to climb Everest without bottled oxygen or Sherpa support (1995)."
    - tag: "For You · Science"
      headline: "Pick Science in German and get Wissenschaft, not 'Science'."
      body: "When you switch WanderWiki to the German Wikipedia edition and pick Science as an interest, the app queries the German category tree (Wissenschaft, Naturwissenschaft, Physik, Chemie, Biologie, Astronomie, Geowissenschaft, Medizin) instead of English category names. That's why For You and Browse return articles German editors filed under their own categories. It works this way in 17 editions; in the other 15, those modes fall back to random articles from the edition you chose."
    - tag: "Folders · Habit"
      headline: "A 'flights' folder that fills up as you read."
      body: "Save articles as you come across them (their full text downloads for offline reading) and organise them into folders (e.g., 'flights', 'before-bed', 'philosophy'). The flights folder becomes a no-WiFi reading list for the next trip; the before-bed folder is for winding down. The widgets refresh daily but the folders persist."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads on any tier, no third-party trackers, no analytics SDKs"
    - "No account or sign-up required"
    - "No WanderWiki server: articles come straight from Wikipedia's official APIs, and saved articles download to your device"
    - "Saved articles, folders, likes, hidden articles, reading progress, your streak, and weekly stats stored locally in SwiftData on your device"
    - "On-device Apple Intelligence summaries, where available, are generated on the device and never sent anywhere"
    - "Wikipedia content used under the <a href=\"https://creativecommons.org/licenses/by-sa/4.0/\" rel=\"noopener\" target=\"_blank\">Creative Commons CC BY-SA 4.0</a> license; the license is linked in Settings and every article opens in Wikipedia from the reader"
    - "See the per-app <a href=\"/transparency/#wanderwiki\">Privacy Manifest</a> for the declared API usage and tracking-domain list (it's empty)"

faq:
  - q: "What is WanderWiki?"
    a: "WanderWiki is a Wikipedia discovery app for iPhone and iPad (iOS 18.2+). It turns the encyclopedia into a swipe-based card deck with four ways in (Random across the full encyclopedia, Browse for one of 16 topics, For You across the topics you pick, and Today in History with 5 subcategories from Wikipedia's official REST API) across 32 Wikipedia language editions, 17 of them with native-language category queries. Saved articles open offline in folders, articles can be read aloud, and five widgets cover On This Day, Continue Reading, and more. Free for 20 articles a day; WanderWiki Plus adds For You, Today in History, and unlimited swiping for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime. It has no ads or behavioral tracking and needs no account."
  - q: "How is WanderWiki different from WikiScroll?"
    a: "The feeds are close: both swipe through random Wikipedia articles, both have a this-day-in-history mode, topic picks, saves, and widgets. WikiScroll is free with ads, sells premium in the app, and its App Store privacy label says data may be used to track you; it runs on iPhones back to iOS 15. WanderWiki has no ads and an App Store label of Data Not Collected; it is free for 20 articles a day, with WanderWiki Plus from {P_MONTHLY}/month or {P_LIFETIME} lifetime. WanderWiki adds saved articles that open offline, folders, read-aloud, and a published list of 32 Wikipedia editions, and runs on iPhone and iPad from iOS 18.2. The full comparison is on the WikiScroll alternative page."
  - q: "How is WanderWiki different from Wiki Rabbit?"
    a: "Wiki Rabbit is free with ads and draws only from Wikipedia's curated Good Articles collection. WanderWiki has no ads at any tier and draws from full Wikipedia (~7 million articles in English alone, across 32 language editions). Wiki Rabbit adapts during a session to what you open, skip, and linger on, and shows a rabbit-hole trail of where you've been; WanderWiki's For You uses only the topics you pick (16 to choose from) and no behavioral tracking. For a 'why this article' explanation, pick Wiki Rabbit. For no ads, full Wikipedia, multiple languages, offline saves, and widgets, pick WanderWiki."
  - q: "Is WanderWiki an official Wikipedia app?"
    a: "No. WanderWiki is an independent app built by Lagerland Apps. It uses Wikipedia content via Wikipedia's official APIs under the Creative Commons Attribution-ShareAlike 4.0 license; every article opens in Wikipedia from the reader, and the license is linked in Settings. WanderWiki is not affiliated with or endorsed by the Wikimedia Foundation. For Wikipedia editing, talk pages, watchlists, and other editor tools, use Wikipedia's own official app."
  - q: "Which Wikipedia language editions does WanderWiki support?"
    a: "Thirty-two: English (en), German (de), French (fr), Spanish (es), Italian (it), Portuguese (pt), Dutch (nl), Polish (pl), Finnish (fi), Swedish (sv), Danish (da), Norwegian Bokmål (no), Czech (cs), Slovak (sk), Hungarian (hu), Romanian (ro), Croatian (hr), Catalan (ca), Turkish (tr), Russian (ru), Ukrainian (uk), Greek (el), Hebrew (he), Japanese (ja), Chinese (zh), Korean (ko), Hindi (hi), Vietnamese (vi), Indonesian (id), Thai (th), Malay (ms), and Arabic (ar). In 17 of them (en, de, fr, es, it, pt, nl, pl, fi, sv, tr, ru, ja, zh, ko, hi, ar) topics map to the edition's own categories, so German Science returns articles from Wissenschaft, Physik, Chemie; in the others, For You and Browse fall back to random articles from that edition. Today in History uses the edition's own feed in 19 editions and English elsewhere."
  - q: "How does the For You mode work?"
    a: "Pick interests across sixteen topics: Science, Technology, History, Arts, Music, Sports, Nature, Space, Philosophy, Geography, Literature, Movies, Food, Architecture, Mathematics, Politics. WanderWiki blends articles drawn from the Wikipedia categories behind the topics you selected, in your chosen Wikipedia language edition. That's all it uses: likes, skips, and reading time don't feed it, and there is no model trained on dwell time, scroll velocity, or engagement metrics. For You is part of WanderWiki Plus; Browse, which dives into a single topic, is free."
  - q: "How does Today in History work?"
    a: "Today in History queries Wikipedia's official REST API endpoint /api/rest_v1/feed/onthisday/&lt;category&gt;/&lt;MM&gt;/&lt;DD&gt; for the current date. Five categories: Selected (Wikipedia's curated highlights), Events (notable events on this date in any year), Births (notable people born), Deaths (notable people who died), and Holidays (observed on this date). It reads your chosen edition's feed where Wikipedia publishes one (19 of the 32 editions) and the English feed otherwise. In the app it's part of WanderWiki Plus; the On This Day widget works on every tier."
  - q: "Does WanderWiki have widgets?"
    a: "Yes, five: On This Day (the day's history, with photographs), Reading Year (your streak and every day you finished an article), Continue Reading (articles you're partway through), Got a Minute (pick 2, 5, 10, or 20 minutes and it picks one of your articles that fits), and Two Doors (one article close to your interests, one far outside them). Most come in Lock Screen sizes, and Surprise Me and Continue Reading are also controls for Control Center, the Lock Screen, and the Action button. The widgets read the same language list as the app through the shared WanderWikiShared package."
  - q: "Can I read articles offline?"
    a: "Yes. Tap save on any article and WanderWiki downloads its full text, so it opens without a connection. Saved articles can be organised into folders (for flights, before bed, philosophy, whatever shape your curiosity takes this month) and found from Spotlight. They live on the device; there's no iCloud sync yet, so they move to a new device only through a device backup. The swipe feed itself loads live from Wikipedia and needs a connection."
  - q: "Does WanderWiki use a recommendation algorithm?"
    a: "Not in the sense people usually mean. Random is purely random. Browse and For You draw from the topics you choose. Likes collect in a list, and 'Show less like this' or 'Hide' only keeps an article out of your Where Next suggestions. There is no behavioural model or engagement-optimisation loop, and no dwell-time, scroll-velocity, or cross-app tracking. We don't have a backend that could receive such signals anyway."
  - q: "Does WanderWiki have streaks or notifications?"
    a: "One of each, both small. WanderWiki counts the days in a row you discover a new article, on your Profile and in the Reading Year widget. If you allow notifications (it asks the first time you save an article), it sends one reminder a day, at 9:00 unless you change it, usually naming one of the day's On This Day picks. You can change the time, set quiet hours, or turn it off in Settings."
  - q: "Is WanderWiki free?"
    a: "Yes, for 20 articles a day: Random and Browse, with save, like, search, folders, widgets, and read-aloud included, in all 32 editions. The count resets at local midnight. WanderWiki Plus unlocks For You, Today in History, and unlimited swiping for {P_MONTHLY}/month, {P_YEARLY}/year (with a free trial for new subscribers), or {P_LIFETIME} lifetime (about a year of monthly billing), which supports Family Sharing so one purchase covers up to 5 family members. No ads on any tier. The only other in-app purchase is an optional {P_IAP:Support the developer} tip. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does WanderWiki work on iPad, Mac, or Vision Pro?"
    a: "Yes on iPad: WanderWiki runs on iPhone and iPad (iOS and iPadOS 18.2+), with a sidebar layout on iPad. The App Store also offers it on Macs with Apple silicon (macOS 15.2+) and on Apple Vision Pro (visionOS 2.2+), where the iPad app runs as is rather than in a version built for those devices. There is no web version; for that, WikiTok runs in any browser."
  - q: "Does WanderWiki track my reading?"
    a: "No. WanderWiki has no third-party SDKs, no analytics, no tracking domains, no account, and no server of its own. Likes, saved articles, folders, reading progress, and your streak all live in SwiftData on your device. Its network requests go to Wikipedia: the language edition you chose (for example en.wikipedia.org) for articles, categories, search, and the On This Day feed, and Wikimedia's image server for pictures. Purchases go through Apple."

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
last_updated: 2026-10-26
---
WanderWiki is a Wikipedia discovery app for iPhone and iPad (iOS 18.2+) that turns the encyclopedia into a swipe-based card deck. It has four ways in: Random across the full encyclopedia, Browse for one of 16 topics, For You across the topics you pick (Science, Technology, History, Arts, Music, Sports, Nature, Space, Philosophy, Geography, Literature, Movies, Food, Architecture, Mathematics, Politics), and Today in History with five subcategories from Wikipedia's official On This Day feed (Selected, Events, Births, Deaths, Holidays). All of them work across 32 Wikipedia language editions. In 17 of them topics map to the edition's own categories: pick German + Science and the app queries Wissenschaft, Physik, Chemie instead of translated English categories. Articles are reformatted for calm reading, with Open in Wikipedia one tap away and the CC BY-SA 4.0 license linked in Settings. Save any article and its full text downloads for offline reading; organise saved articles into folders; have any article read aloud. Five widgets (On This Day, Reading Year, Continue Reading, Got a Minute, Two Doors) and two Control Center controls bring it to the Home Screen and Lock Screen. For You follows only the topics you choose; nothing is inferred from what you like or skip, and nothing leaves the device. It is built on Wikipedia's official APIs with SwiftUI + SwiftData + StoreKit 2, and has no ads at any tier, no third-party SDKs, no analytics, and no WanderWiki server. Free for 20 articles a day; WanderWiki Plus adds For You, Today in History, and unlimited swiping for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime. Its closest competitors, WikiScroll and Wiki Rabbit, are both free with ads and each does something well; WanderWiki charges instead, so it has no commercial reason to maximise screen time.
