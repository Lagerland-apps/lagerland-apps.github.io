---
layout: default
permalink: /lagerland-apps/
title: "About Lagerland Apps"
seo:
  title: "About Lagerland Apps — Independent Apple Developer"
  description: "Lagerland Apps is an independent Apple developer building privacy-first iOS and macOS apps with no tracking, no ads, and no accounts — funded by honest paid software, not advertising."
  keywords:
    - Lagerland Apps
    - independent Apple developer
    - privacy-first iOS developer
    - indie macOS developer
    - SwiftUI developer
    - one-person iOS studio
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "@id": "{{ site.url }}/lagerland-apps/#webpage",
  "url": "{{ site.url }}/lagerland-apps/",
  "name": "About Lagerland Apps",
  "description": "Lagerland Apps is an independent Apple developer building privacy-first iOS and macOS apps.",
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
}
</script>

<section class="hero hero--home">
  <div class="hero-left reveal">
    <p class="overline">Independent Apple developer · One-person studio</p>
    <h1 class="h1">
      Built by <span class="gradient-text">one person.</span><br>For people who miss calm software.
    </h1>
    <p class="lead">
      Lagerland Apps is founded by an <strong>independent Apple developer</strong>. Every app is designed, coded, tested, and shipped by one person — no VC pressure, no advertiser incentives, no growth hackers.
    </p>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">The philosophy</h2>
  <div class="grid grid-2 stagger">
    <div class="card">
      <div class="card-title">Privacy is the default, not a feature</div>
      <div class="card-text">No third-party tracking SDKs. No advertising networks. No analytics that identify users. Data stays on your device; any cloud sync uses your own iCloud account.</div>
    </div>
    <div class="card">
      <div class="card-title">Honest monetization</div>
      <div class="card-text">One-time purchases, optional Pro subscriptions, and freemium models with permanently free core features. No dark patterns, no auto-charging trials, no ads.</div>
    </div>
    <div class="card">
      <div class="card-title">Single-purpose tools</div>
      <div class="card-text">Each app does one thing well. Rather than one bloated platform, the catalogue is a family of focused tools you can use together or alone.</div>
    </div>
    <div class="card">
      <div class="card-title">Apple-native engineering</div>
      <div class="card-text">Built with SwiftUI, HealthKit, StoreKit, CoreData/SwiftData, and Apple's own frameworks. No cross-platform wrappers, no Electron, no compromises on feel.</div>
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
  <h2 class="h2">The catalogue — {{ live_apps.size }} apps</h2>
  <p class="lead">Every live app from Lagerland Apps. Browse by category on the <a href="/apps/">full catalogue page</a>, or explore them individually below.</p>
  <div class="grid grid-2 stagger">
    {%- for app in live_apps -%}{% include app-card.html app=app %}{%- endfor -%}
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
