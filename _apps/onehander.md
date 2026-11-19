---
layout: app
slug: onehander
name: "OneHander"
tagline: "A web browser for watching video with one hand on iPhone."

# ── UNLISTED: PRE-LAUNCH ──────────────────────────────────────────────────────
# OneHander is not released yet. `status` is deliberately NOT "live": every
# listing on this site filters on `where: "status", "live"` (home, /apps/,
# llms.txt, llms-full.txt, ai-index.json, ai-sitemap.xml, footer,
# you-might-like, /lagerland-apps/, the /for/ hubs, the language hubs), so this
# page exists at its URL and appears nowhere else. `sitemap: false` keeps it
# out of sitemap.xml and `noindex: true` keeps it out of search results.
#
# The URLs are needed before release: App Store Connect's Privacy Policy URL
# is /apps/onehander/privacy/ and its Support URL is /apps/onehander/support/,
# and App Review opens them.
#
# ON LAUNCH: follow ~/Downloads/githubcode/ONEHANDER-LAUNCH.md (outside the
# repo). In short: re-run the App Store Connect sync, set status to "live",
# delete `sitemap: false`, `noindex: true` and `prelaunch_platforms` here and on
# the sub-pages, set the release dates, add the German and French pages and the
# transparency row, build, audit, push.
status: upcoming
sitemap: false
noindex: true
# ──────────────────────────────────────────────────────────────────────────────

quick_answer: "OneHander is a web browser for iPhone built for watching web video with one hand. A scrubber runs down the edge of the screen: drag it with your thumb to seek, flick it to jump, and the video seeks once when you let go. Start a video on a page and it opens fullscreen in OneHander's own player, with back and forward 10 seconds, play and pause, fit or fill, and mute next to Back, Tabs, and Reload. Clear view hides every bar, and one tap brings them back. Every control moves to the side of the hand you use. OneHander costs {P_APP} once on the App Store and works without an account. The app collects no data and keeps no browsing history. It runs on iPhone with iOS 17 or later."
category: utilities
# Pre-launch only: MASTER.md marks iPhone as pending (⏳); the catalog lists live platforms only.
# Ignored once the catalog has them (_includes/app-facts.html). Delete on launch.
prelaunch_platforms: ["iOS"]

app_store_url: "https://apps.apple.com/app/id6836704998"

price:
  model: one-time-purchase

plans_footnote: "Price in USD; the App Store shows your local currency at checkout. OneHander is a one-time purchase and does not renew. Apple handles refunds through the standard App Store refund flow."

icon: "/assets/icons/onehander.png"
og_image: "/assets/og/onehander.png"

seo:
  title: "OneHander: One-Hand Video Browser for iPhone"
  description: "Watch web video on iPhone with one hand. A thumb scrubber on the screen edge, video and browser controls together, and Clear view. Pay once, no account."
  keywords:
    - one hand video browser iphone
    - one handed video player iphone
    - web video player iphone
    - video browser iphone
    - web video browser
    - seek video with thumb
    - fullscreen web video iphone
    - left handed video controls iphone
    - video scrubber iphone

hero:
  pre_headline: "A one-hand video browser for iPhone."
  headline: "Watch web video with one thumb."
  secondary: "In a phone browser, the video and the browser take turns. To go back, switch tabs, or find a spot in the video, you leave fullscreen and aim for a thin seek bar at the far side of the screen. OneHander keeps both under your thumb."
  subheadline: "A scrubber on the edge of the screen seeks with one drag. A video you start on a page opens fullscreen in OneHander's player, with Back, Tabs, and Reload still on screen. When you only want the picture, Clear view hides every bar."
  cta_label: "Get OneHander"
  alt: "OneHander app icon: an amber play button next to a vertical scrubber tape"

who_for:
  - "You watch a lot of video in a phone browser, often with one hand free: in bed, on a commute, or holding a baby"
  - "You watch on sites that have no app, or whose app is worse than the website"
  - "You want to seek through a long video with your thumb instead of a thin seek bar"
  - "You're left-handed and want the controls on your side of the screen"
  - "You'd rather pay once than subscribe"

who_not_for:
  - "You want to download or save videos. OneHander only plays them"
  - "You need a Picture in Picture button. OneHander has none, though a site's own player can still start Picture in Picture"
  - "You want a full ad blocker. OneHander's built-in list blocks common ad and tracking services only"
  - "You watch DRM-protected streams. OneHander can't control those players"
  - "You need iPad, Mac, or Android, or an interface in a language other than English"

value_points:
  - title: "A scrubber for your thumb"
    description: "A tape of one-second ticks runs down the edge of the screen. Drag it up to go forward and down to go back, or flick it to jump. A big timecode shows where you'll land, and the video seeks once when you let go, so it doesn't stutter while you look for the spot."
  - title: "Videos open in the player"
    description: "Tap play on a video and it opens fullscreen with OneHander's controls: back and forward 10 seconds, play and pause, fit or fill, and mute. Back, Tabs, and Reload stay on screen, so the next video is one tap away. A site's own fullscreen button opens the same player."
  - title: "Built around the hand you use"
    description: "Pick the left or right side and the scrubber and player keys move to that edge, under your thumb. In portrait, keep the keys in rows at the bottom or in one column on the side, which gives the video the full height."
  - title: "Bought once"
    description: "OneHander is {P_APP} once, a single App Store purchase that does not renew, with every feature included and nothing to sign up for. The app collects no data, and it keeps no browsing history; back and forward live in each tab's memory."

how_it_works:
  heading: "From a web page to fullscreen, one thumb the whole way."
  intro: "OneHander works like a browser until a video starts. Then it becomes a player, without taking the browser away."
  steps:
    - title: "Open a page"
      detail: "Type an address or a search into the address bar. Searches go to DuckDuckGo unless you pick another engine in Settings. Tabs, pull to refresh, and Share Page work as in any browser."
    - title: "Start a video"
      detail: "Tap play on a video and it opens fullscreen in OneHander's player. The status bar and home indicator hide, and the page stops scrolling so a stray swipe can't move it. Muted autoplay and tiny previews stay on the page. Prefer the site's own player? Turn off Open Videos in Player in Settings."
    - title: "Seek with your thumb"
      detail: "Drag the scrubber on the screen edge. The amber timecode shows the target and the jump size as you go; flick for a longer jump. Scrubber Speed in Settings sets how far a swipe moves the video: Fine, Normal, or Fast."
    - title: "Hide everything"
      detail: "Tap Clear view and every bar disappears while the video fills the screen. One tap on the Controls button brings them back."
    - title: "Move on"
      detail: "Back, Forward, and Tabs sit next to the video controls. Go to the next video or switch tabs without leaving fullscreen first."

features:
  - title: "Thumb scrubber"
    description: "A vertical tape of one-second ticks on the left or right edge. Drag to seek, flick to jump, and see the buffered range and a progress line on the screen edge. Outside fullscreen it shows only while a video is on screen or playing."
  - title: "Fullscreen player controls"
    description: "Back 10 seconds, Play and Pause, Forward 10 seconds, Fit or Fill, Mute, and Exit fullscreen. In portrait the current time shows in big amber digits with the time left and the page title beside it."
  - title: "One-Hand Side and Portrait Controls"
    description: "Switch hands from the nav bar or in Settings, and every control follows: the scrubber, the key columns, and the Clear view button. In portrait, choose keys at the bottom or a single column on the side."
  - title: "Clear view and Fill"
    description: "Clear view hides every bar and crops the video to fill the screen. Fill Screen in Landscape does the same in landscape fullscreen, and the Fit or Fill key switches back at any time."
  - title: "Keep Playing in Background"
    description: "A video's sound keeps playing when you switch apps or lock the screen, and plays through the silent switch. Turn the setting off and videos pause when you leave the app."
  - title: "A browser, too"
    description: "Tabs with snapshots, a choice of search engine, pull to refresh, Share Page, and a built-in list that blocks common ad and tracking services. Open tabs can reopen at launch, and Clear Website Data signs you out of sites and clears their cookies and cache."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No account, no ads, no analytics, and no third-party code"
    - "Browsing history is not stored; back and forward live in each tab's memory"
    - "Settings and, if you choose, your open tabs stay on the iPhone"
    - "Websites keep their own cookies and logins, as in any browser; Clear Website Data removes them"
    - "The script that finds video on a page is built into the app and is never downloaded or updated from a server"

faq:
  - q: "What is OneHander?"
    a: "OneHander is a web browser for iPhone made for watching web video with one hand. It adds a thumb scrubber on the edge of the screen, opens videos you start in its own fullscreen player with the browser controls still on screen, and has a Clear view that hides every bar."
  - q: "How does the scrubber work?"
    a: "A tape of one-second ticks runs down the left or right edge of the screen. Drag it up to go forward and down to go back, or flick it to jump further. A large timecode shows the target and the jump size while you drag, and the video seeks once when the tape settles. Scrubber Speed in Settings sets how far a swipe moves the video: Fine, Normal, or Fast."
  - q: "Does OneHander work on every website?"
    a: "It works with the HTML5 video players it can reach on a page, and a site's own fullscreen button opens OneHander's player. Players that use DRM or hide their video element can't be controlled, and some sites may behave differently. If a site works better with its own player, turn off Open Videos in Player in Settings."
  - q: "Can I use OneHander with my left hand?"
    a: "Yes. Set One-Hand Side to Left with the Switch hand key in the nav bar or in Settings, and the scrubber, the key columns, and the Clear view button move to the left edge. In portrait you can also keep the keys in rows at the bottom or in one column on the side."
  - q: "Does the sound keep playing when I lock the screen?"
    a: "Yes, with Keep Playing in Background on, which is the default. The sound continues when you switch apps or lock the screen, and it plays even with the silent switch on. Turn the setting off and videos pause when OneHander goes to the background."
  - q: "Does OneHander have Picture in Picture?"
    a: "OneHander has no Picture in Picture button of its own, because WebKit, Apple's browser engine, only starts Picture in Picture from a tap inside the page. A site's own player can still start it."
  - q: "Can OneHander download videos?"
    a: "No. OneHander plays video on web pages and does not download or save it."
  - q: "Does OneHander block ads?"
    a: "It blocks common ad and tracking services with a short built-in list, on by default, that stops requests to about 100 ad and tracking hosts when another site loads them. It isn't a full ad blocker. Turn it off in Settings with Block Ads and Trackers."
  - q: "Does OneHander collect my data?"
    a: "No. OneHander contains no analytics or third-party code, you never create an account, and Lagerland Apps runs no server for it. It keeps no browsing history. Your settings, and your open tabs if Reopen Tabs at Launch is on, stay on your iPhone. Websites you visit keep their own cookies and logins, as in any browser, and Clear Website Data in Settings removes them."
  - q: "How much does OneHander cost?"
    a: "OneHander costs {P_APP} once on the App Store. Every feature comes with it, and there are no in-app purchases. Price in USD; the App Store shows your local currency at checkout."
  - q: "What do I need to run OneHander?"
    a: "An iPhone with iOS 17 or later. OneHander works in portrait and landscape. Web pages need an internet connection; when a page can't load, OneHander shows why and offers Try Again. It isn't available for iPad or Mac."
  - q: "Which languages does OneHander support?"
    a: "OneHander's interface is in English. Web pages show in their own language."

related_apps: ["mediakit", "wanderwiki", "earnlock"]

support:
  email: "support@lagerland.app"
  url: "/apps/onehander/support/"

release:
  first_release: "2026-11-19"
  last_updated: "2026-11-19"
  version: "1.0"

show_body: true
about_heading: "What OneHander is: a browser that turns into a player"
last_updated: 2026-11-19
---
OneHander is a web browser for iPhone made for one job: watching web video with one hand. In most phone browsers the video and the browser take turns. Fullscreen hides Back and Tabs, and the seek bar is a thin line on the far side of the screen from your thumb.

OneHander keeps both on screen. Tap play on a video and it opens fullscreen in OneHander's player, with back and forward 10 seconds, play and pause, fit or fill, and mute beside Back, Forward, and Tabs. A scrubber on the edge of the screen seeks with one drag of the thumb, and Clear view hides every bar when you only want the picture. Every control moves to the side of the hand you hold the phone with.

OneHander is a one-time purchase that works without an account. The app collects no data and keeps no browsing history. Pages render with WebKit, Apple's browser engine.
