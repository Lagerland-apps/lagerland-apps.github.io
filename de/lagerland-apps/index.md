---
layout: default
ref: /lagerland-apps/
permalink: /de/lagerland-apps/
translated_from: 2026-10-26
title: "Über Lagerland Apps"
quick_answer: "Lagerland Apps ist ein unabhängiges Ein-Personen-Studio für Apple-Apps in Finnland. Es entwickelt {APP_COUNT} datenschutzfreundliche Apps für iOS, iPadOS, watchOS und macOS, ohne Tracking durch Dritte, ohne Werbe-SDKs und ohne Pflicht zur Anmeldung. Finanziert wird das Studio von den Menschen, die die Software kaufen."
seo:
  title: "Lagerland Apps: Indie-Entwickler aus Finnland"
  description: "Ein-Personen-Studio aus Finnland mit {APP_COUNT} Apps für iPhone, iPad, Apple Watch und Mac: ohne Tracking, Werbung und Konto, finanziert durch bezahlte Software."
  keywords:
    - lagerland apps
    - indie entwickler
    - indie entwickler finnland
    - unabhängiger apple entwickler
    - ein-personen-studio
    - ios apps ohne tracking
    - swiftui entwickler
faq:
  - q: "Wer steckt hinter Lagerland Apps?"
    a: "Lagerland Apps ist ein unabhängiges Ein-Personen-Studio für Apple-Apps in Finnland. Eine einzige Person entwirft, programmiert, testet und veröffentlicht jede App. Es gibt kein Team, keine Investoren und keine Werbekunden."
  - q: "Wo sitzt Lagerland Apps?"
    a: "Lagerland Apps sitzt in Finnland und arbeitet als unabhängiger Apple-Entwickler. Die Apps erscheinen weltweit im App Store unter der Entwickler-ID 1855943133."
  - q: "Wie finanziert sich Lagerland Apps ohne Werbung?"
    a: "Die Menschen bezahlen für die Software, per Einmalkauf oder mit einem optionalen Abo. Dazu gibt es kostenlose Grundversionen, deren Kernfunktionen kostenlos bleiben. Das Studio verkauft weder Werbung noch Daten und setzt keine manipulativen Tricks ein."
  - q: "Wie viele Apps hat Lagerland Apps?"
    a: "Lagerland Apps hat derzeit {APP_COUNT} Apps im App Store, alle für Apple-Plattformen: für Gesundheit, Tagesplanung, Finanzen, Lesen, Fitness, Spiele, Apple-Entwicklerwerkzeuge und Dienstprogramme."
  - q: "Sammelt Lagerland Apps Daten über mich?"
    a: "Nein. Keine App enthält Analyse- oder Werbe-SDKs von Drittanbietern, und keine verlangt ein Konto. Deine Daten bleiben, wo immer es geht, auf dem Gerät. Wird etwas synchronisiert, dann über deinen eigenen iCloud-Account."
  - q: "Für welche Geräte entwickelt Lagerland Apps?"
    a: "Lagerland Apps entwickelt native Apps für iPhone, iPad, Apple Watch und Mac. Sie entstehen mit SwiftUI, HealthKit, StoreKit und CoreData/SwiftData, ohne plattformübergreifende Wrapper und ohne Electron."
last_updated: 2026-10-27
---
{%- include t.html -%}

{%- comment %} ===== Apps with a German page, in master order (apps without one are left out) ===== {% endcomment -%}
{%- assign live_apps = site.apps | where: "status", "live" -%}
{%- assign de_apps = "" | split: "" -%}
{%- for app in live_apps -%}
  {%- include tx-app.html app=app -%}
  {%- unless tx_en -%}{%- assign de_apps = de_apps | push: app -%}{%- endunless -%}
{%- endfor -%}

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "AboutPage",
      "@id": "{{ site.url }}/de/lagerland-apps/#webpage",
      "url": "{{ site.url }}/de/lagerland-apps/",
      "name": "Über Lagerland Apps",
      "description": "Lagerland Apps ist ein Ein-Personen-Studio in Finnland, das Apps ohne Tracking für iOS und macOS entwickelt.",
      "inLanguage": "de",
      "isPartOf": { "@id": "{{ site.url }}/de/#website" },
      "about": { "@id": "{{ site.url }}/#organization" },
      "mainEntity": { "@id": "{{ site.url }}/#organization" },
      "breadcrumb": {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Lagerland Apps", "item": "{{ site.url }}/de/" },
          { "@type": "ListItem", "position": 2, "name": "Über das Studio", "item": "{{ site.url }}/de/lagerland-apps/" }
        ]
      }
    },
    {
      "@type": "FAQPage",
      "@id": "{{ site.url }}/de/lagerland-apps/#faq",
      "inLanguage": "de",
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
    <p class="overline">Unabhängiger Apple-Entwickler · Ein-Personen-Studio · Finnland</p>
    <h1 class="h1">
      Gebaut von <span class="gradient-text">einer Person</span><br>für alle, die ruhige Software vermissen.
    </h1>
    <p class="lead">
      Lagerland Apps ist ein unabhängiges Ein-Personen-Studio für Apple-Apps in Finnland. Eine einzige Person entwirft, programmiert, testet und veröffentlicht jede App und ist dabei weder Investoren noch Werbekunden Rechenschaft schuldig.
    </p>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Die Haltung dahinter</h2>
  <div class="grid grid-2 stagger">
    <div class="card">
      <div class="card-title">Standardmäßig privat</div>
      <div class="card-text">Die Apps enthalten keine Tracking-SDKs von Drittanbietern, keine Werbenetzwerke und keine Analysetools, die dich identifizieren. Deine Daten bleiben auf deinem Gerät, und jede Synchronisierung in die Cloud läuft über deinen eigenen iCloud-Account.</div>
    </div>
    <div class="card">
      <div class="card-title">Wie die Apps bezahlt werden</div>
      <div class="card-text">Per Einmalkauf oder mit einem optionalen Abo. Dazu gibt es kostenlose Grundversionen, deren Kernfunktionen kostenlos bleiben. Es gibt keine Werbung, keine manipulativen Tricks und keine Testphasen, die ohne deine ausdrückliche Zustimmung kostenpflichtig weiterlaufen.</div>
    </div>
    <div class="card">
      <div class="card-title">Eine App, eine Aufgabe</div>
      <div class="card-text">Jede App erledigt genau eine Sache. Der Katalog besteht aus kleinen, fokussierten Werkzeugen, die du zusammen oder einzeln nutzen kannst.</div>
    </div>
    <div class="card">
      <div class="card-title">Mit Apples eigener Technik gebaut</div>
      <div class="card-text">Entwickelt mit SwiftUI, HealthKit, StoreKit, CoreData/SwiftData und Apples eigenen Frameworks. Die Apps verzichten auf plattformübergreifende Wrapper und Electron und verhalten sich deshalb so, wie man es von Apple-Software erwartet.</div>
    </div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Plattformen</h2>
  <div class="grid grid-4 stagger">
    <div class="card"><div class="card-title">iPhone</div><div class="card-text">iOS-Apps für Produktivität, Gesundheit, Finanzen, Lesen und Lifestyle.</div></div>
    <div class="card"><div class="card-title">iPad</div><div class="card-text">Universal-Apps, die auf dem iPad eigene, für iPadOS gebaute Layouts zeigen.</div></div>
    <div class="card"><div class="card-title">Apple Watch</div><div class="card-text">Workouts und schnelle Einträge direkt auf der Uhr erfassen.</div></div>
    <div class="card"><div class="card-title">Mac</div><div class="card-text">Native macOS-Werkzeuge für Entwickler: Abläufe in App Store Connect und Dateikonvertierung direkt auf dem Mac.</div></div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Der Katalog: {{ de_apps.size }} Apps</h2>
  <p class="lead">Alle veröffentlichten Apps von Lagerland Apps. Hier unten stehen sie einzeln, nach Kategorien sortiert findest du sie auf der <a href="{% include l.html url="/apps/" %}"{% if l_en %} hreflang="en"{% endif %}>Katalogseite{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>.</p>
  <div class="grid grid-2 stagger">
    {%- for app in de_apps -%}{% include app-card.html app=app %}{%- endfor -%}
  </div>
</section>

<section id="faq" class="section reveal">
  <div class="section-center"><p class="overline">Fragen</p><h2 class="h2">Häufige Fragen zu Lagerland Apps</h2></div>
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
  <h2 class="h2">Kontakt</h2>
  <div class="card">
    <p>Für Presseanfragen, Kooperationen, Fehlermeldungen oder allgemeine Fragen:</p>
    <div class="actions" style="margin-top:var(--s-4);">
      <a class="btn btn-primary" href="mailto:lagerland.apps@proton.me">lagerland.apps@proton.me</a>
      <a class="btn btn-secondary" href="{% include l.html url="/support/" %}"{% if l_en %} hreflang="en"{% endif %}>Allgemeiner Support{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>
    </div>
  </div>
</section>
