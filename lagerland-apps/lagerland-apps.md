---
layout: default
permalink: /lagerland-apps/
title: "About Lagerland Apps"
quick_answer: "Lagerland Apps is a one-person Apple studio in Finland, run by a single independent developer. It builds {APP_COUNT} privacy-first iOS, iPadOS, watchOS, and macOS apps with no third-party tracking, no advertising SDKs, and no required accounts. The studio is funded by people paying for the software."
seo:
  title: "About Lagerland Apps: Indie Apple Developer in Finland"
  description: "One-person Apple studio in Finland building {APP_COUNT} privacy-first iOS & Mac apps with no trackers, ads, or accounts, funded by paid software."
  keywords:
    - Lagerland Apps
    - independent Apple developer Finland
    - indie Apple app studio
    - privacy-first iOS developer
    - indie macOS developer
    - SwiftUI developer
    - one-person iOS studio
faq:
  - q: "Who is behind Lagerland Apps?"
    a: "Lagerland Apps is a one-person Apple studio in Finland run by a single independent developer. One person designs, codes, tests, and ships every app. There is no team, no investor, and no advertiser."
  - q: "Where is Lagerland Apps based?"
    a: "Lagerland Apps is based in Finland and operates as an independent Apple developer with apps distributed worldwide through the Apple App Store under developer ID 1855943133."
  - q: "How is Lagerland Apps funded if there are no ads?"
    a: "People pay for the software: one-time purchases, optional Pro subscriptions, and free tiers whose core features stay free. The studio sells no advertising and no data, and uses no dark patterns."
  - q: "How many apps does Lagerland Apps publish?"
    a: "Lagerland Apps currently publishes {APP_COUNT} live apps across health, daily planning, finance, reading, fitness, games, Apple developer tools, and utilities, all for Apple platforms."
  - q: "Does Lagerland Apps collect any user data?"
    a: "No. No app includes third-party analytics or advertising SDKs, and none requires an account. User data stays on-device wherever possible; any sync uses the user's own iCloud account."
  - q: "What platforms does Lagerland Apps build for?"
    a: "Lagerland Apps builds native applications for iPhone, iPad, Apple Watch, and Mac. Apps are built with SwiftUI, HealthKit, StoreKit and CoreData/SwiftData, without cross-platform wrappers or Electron."
last_updated: 2026-10-26
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
      Lagerland Apps is a one-person studio in Finland, run by a single independent Apple developer. One person designs, codes, tests, and ships every app, with no investors or advertisers to answer to.
    </p>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">The philosophy</h2>
  <div class="grid grid-2 stagger">
    <div class="card">
      <div class="card-title">Private by default</div>
      <div class="card-text">The apps have no third-party tracking SDKs, no advertising networks, and no analytics that identify you. Data stays on your device, and any cloud sync uses your own iCloud account.</div>
    </div>
    <div class="card">
      <div class="card-title">How the apps are paid for</div>
      <div class="card-text">One-time purchases, optional Pro subscriptions, and free tiers whose core features stay free. There are no ads, no dark patterns, and no trials that start charging on their own.</div>
    </div>
    <div class="card">
      <div class="card-title">Single-purpose tools</div>
      <div class="card-text">Each app does one job. The catalogue is a set of small, focused tools you can use together or on their own.</div>
    </div>
    <div class="card">
      <div class="card-title">Apple-native engineering</div>
      <div class="card-text">Built with SwiftUI, HealthKit, StoreKit, CoreData/SwiftData, and Apple's own frameworks. The apps use no cross-platform wrappers or Electron, so they behave the way Apple software should.</div>
    </div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Platforms</h2>
  <div class="grid grid-4 stagger">
    <div class="card"><div class="card-title">iPhone</div><div class="card-text">iOS apps across productivity, health, finance, reading, and lifestyle.</div></div>
    <div class="card"><div class="card-title">iPad</div><div class="card-text">Universal apps that scale up to iPad with proper iPadOS-native layouts.</div></div>
    <div class="card"><div class="card-title">Apple Watch</div><div class="card-text">Direct-to-watch logging for workouts and quick-capture flows.</div></div>
    <div class="card"><div class="card-title">Mac</div><div class="card-text">Native macOS developer tools for App Store Connect workflows and local file conversion.</div></div>
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
