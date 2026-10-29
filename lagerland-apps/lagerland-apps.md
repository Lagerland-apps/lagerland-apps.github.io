---
layout: default
permalink: /lagerland-apps/
title: "About Lagerland Apps"
quick_answer: "Lagerland Apps is a one-person Apple studio in Finland. One independent developer designs, codes, tests, and supports all {APP_COUNT} of its apps for iPhone, iPad, Apple Watch, and Mac. No app contains advertising or analytics SDKs, requests the IDFA, or asks you to create an account, and none sends your data to a server run by the studio. The studio is funded by the people who pay for the apps."
seo:
  title: "About Lagerland Apps: Indie Apple Developer in Finland"
  description: "A one-person Apple studio in Finland with {APP_COUNT} apps for iPhone, iPad, Apple Watch, and Mac, with no ads, trackers, or accounts. Funded by paid apps."
  keywords:
    - Lagerland Apps
    - independent Apple developer Finland
    - indie Apple app studio
    - privacy-first iOS developer
    - indie macOS developer
    - one-person iOS studio
    - indie developer
faq:
  - q: "Who is behind Lagerland Apps?"
    a: "Lagerland Apps is a one-person Apple studio in Finland run by a single independent developer. One person designs, codes, tests, ships, and supports every app. There is no team, no investor, and no advertiser."
  - q: "Where is Lagerland Apps based?"
    a: "Lagerland Apps is based in Finland, in the EU, and publishes its apps worldwide on the App Store under developer ID 1855943133."
  - q: "How is Lagerland Apps funded if there are no ads?"
    a: "The people who use the apps pay for them. Most apps are free to download, with an optional paid upgrade sold as a subscription, a one-time purchase, or both. Mockly is the one app you pay for up front. The studio sells no advertising and no data."
  - q: "How many apps does Lagerland Apps publish?"
    a: "Lagerland Apps publishes {APP_COUNT} live apps for Apple platforms, covering health and training, daily planning, bills, reading, board games and logic puzzles, tools for App Store developers, and file conversion."
  - q: "Does Lagerland Apps collect any user data?"
    a: "No app contains a third-party analytics or advertising SDK, none requires an account, and none sends your data to a server run by the studio. Your data stays on your device, and the apps that sync use your own iCloud. Apps that need the internet for their job, such as WanderWiki for Wikipedia or the developer tools for App Store Connect, connect to that service directly."
  - q: "What platforms does Lagerland Apps build for?"
    a: "Lagerland Apps builds native apps for iPhone, iPad, Apple Watch, and Mac with Apple's own frameworks, without cross-platform wrappers or Electron. Each app page lists the devices that app runs on."
last_updated: 2026-10-29
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "AboutPage",
      "@id": "{{ site.url }}/lagerland-apps/#webpage",
      "url": "{{ site.url }}/lagerland-apps/",
      "name": "About Lagerland Apps",
      "description": "Lagerland Apps is a one-person Apple studio in Finland building privacy-first iOS and macOS apps.",
      "isPartOf": { "@id": "{{ site.url }}/#website" },
      "about": { "@id": "{{ site.url }}/#organization" },
      "mainEntity": { "@id": "{{ site.url }}/#organization" },
      "breadcrumb": {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Lagerland Apps", "item": "{{ site.url }}/" },
          { "@type": "ListItem", "position": 2, "name": "About", "item": "{{ site.url }}/lagerland-apps/" }
        ]
      }
    },
    {
      "@type": "FAQPage",
      "@id": "{{ site.url }}/lagerland-apps/#faq",
      "mainEntity": [
      {%- for item in page.faq -%}
        {
          "@type": "Question",
          "name": {{ item.q | jsonify }},
          "acceptedAnswer": {
            "@type": "Answer",
            "text": {{ item.a | jsonify }}
          }
        }{%- unless forloop.last -%},{%- endunless -%}
      {%- endfor -%}
      ]
    }
  ]
}
</script>

<section class="hero hero--home">
  <div class="hero-left reveal">
    <p class="overline">Independent Apple developer · One-person studio · Finland</p>
    <h1 class="h1">
      Built by <span class="gradient-text">one person</span><br>for people who miss calm software.
    </h1>
    <p class="lead">
      Lagerland Apps is a one-person studio in Finland. One independent Apple developer designs, codes, tests, ships, and supports every app, and answers to the people who pay for them, with no investors or advertisers in between.
    </p>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">The philosophy</h2>
  <div class="grid grid-2 stagger">
    <div class="card">
      <div class="card-title">Private by default</div>
      <div class="card-text">No app carries an advertising or analytics SDK or requests the IDFA, and none sends your data to a server of ours. Your data stays on your device, and any sync uses your own iCloud. The <a href="/transparency/">transparency page</a> lists what each app declares.</div>
    </div>
    <div class="card">
      <div class="card-title">How the apps are paid for</div>
      <div class="card-text">Most apps are free to download, with an optional upgrade sold as a subscription, a one-time purchase, or both. Mockly is the one app you pay for up front. Every purchase goes through Apple, so you see the price before you confirm, and you manage or cancel a subscription in Settings on iPhone or iPad or in the App Store app on Mac.</div>
    </div>
    <div class="card">
      <div class="card-title">Single-purpose tools</div>
      <div class="card-text">Each app does one job: plan the day, log a workout, remember a bill, learn a board game. You install the ones you need and nothing else.</div>
    </div>
    <div class="card">
      <div class="card-title">Native to Apple devices</div>
      <div class="card-text">Built with Apple's own frameworks, without cross-platform wrappers or Electron. The apps use what your device already has, such as Apple Health, widgets, Siri, and iCloud, where the app needs them.</div>
    </div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Platforms</h2>
  <div class="grid grid-4 stagger">
    <div class="card"><div class="card-title">iPhone</div><div class="card-text">Almost every app, from health and planning to bills, reading, and games.</div></div>
    <div class="card"><div class="card-title">iPad</div><div class="card-text">The board games, both logic puzzles, Observa, Pawza, Taskful Day, and WanderWiki.</div></div>
    <div class="card"><div class="card-title">Apple Watch</div><div class="card-text">GymLogger X, Observa, and Taskful Day, plus EarnLock's Watch app with Premium.</div></div>
    <div class="card"><div class="card-title">Mac</div><div class="card-text">AppMeta and Mockly for App Store developers, MediaKit, Taskful Day, and the three board games.</div></div>
  </div>
</section>

{%- assign live_apps = site.apps | where: "status", "live" -%}
<section class="section reveal">
  <h2 class="h2">The catalogue: {{ live_apps.size }} apps</h2>
  <p class="lead">Every live app from Lagerland Apps. Browse by category on the <a href="/apps/">full catalogue page</a>, or explore them individually below.</p>
  <div class="grid grid-2 stagger">
    {%- for app in live_apps -%}{% include app-card.html app=app %}{%- endfor -%}
  </div>
</section>

<section id="faq" class="section reveal">
  <div class="section-center"><p class="overline">Questions</p><h2 class="h2">Frequently asked about Lagerland Apps</h2></div>
  <div class="faq">
    {%- for item in page.faq -%}
    <details class="faq-item"{% if forloop.first %} open{% endif %}>
      <summary>{{ item.q }}</summary>
      <div class="faq-a">{{ item.a }}</div>
    </details>
    {%- endfor -%}
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Contact</h2>
  <div class="card">
    <p>For press, partnerships, bug reports, or general questions:</p>
    <div class="actions" style="margin-top:var(--s-4);">
      <a class="btn btn-primary" href="mailto:lagerland.apps@proton.me">lagerland.apps@proton.me</a>
      <a class="btn btn-secondary" href="/support/">General support</a>
    </div>
  </div>
</section>
