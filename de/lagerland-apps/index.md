---
layout: default
ref: /lagerland-apps/
permalink: /de/lagerland-apps/
translated_from: 2026-10-29
title: "Über Lagerland Apps"
quick_answer: "Lagerland Apps ist ein Ein-Personen-Studio für Apple-Apps in Finnland. Ein einziger unabhängiger Entwickler entwirft, programmiert, testet und betreut alle {APP_COUNT} Apps für iPhone, iPad, Apple Watch und Mac. Keine App enthält Werbe- oder Analyse-SDKs, fragt nach der IDFA oder verlangt ein Konto, und keine schickt deine Daten an einen Server des Studios. Finanziert wird das Studio von den Menschen, die für die Apps bezahlen."
seo:
  title: "Lagerland Apps: Indie-Entwickler aus Finnland"
  description: "Ein-Personen-Studio aus Finnland mit {APP_COUNT} Apps für iPhone, iPad, Apple Watch und Mac, ohne Werbung, Tracking und Konto. Finanziert durch bezahlte Apps."
  keywords:
    - lagerland apps
    - indie entwickler
    - indie entwickler finnland
    - unabhängiger apple entwickler
    - ein-personen-studio
    - ios apps ohne tracking
faq:
  - q: "Wer steckt hinter Lagerland Apps?"
    a: "Lagerland Apps ist ein unabhängiges Ein-Personen-Studio für Apple-Apps in Finnland. Eine einzige Person entwirft, programmiert, testet, veröffentlicht und betreut jede App. Es gibt kein Team, keine Investoren und keine Werbekunden."
  - q: "Wo sitzt Lagerland Apps?"
    a: "Lagerland Apps sitzt in Finnland, also in der EU, und veröffentlicht seine Apps weltweit im App Store unter der Entwickler-ID 1855943133."
  - q: "Wie finanziert sich Lagerland Apps ohne Werbung?"
    a: "Die Menschen, die die Apps nutzen, bezahlen dafür. Die meisten Apps sind kostenlos, mit einem optionalen Upgrade als Abo, als Einmalkauf oder in beiden Formen. Mockly ist die einzige App, die du vorab kaufst. Das Studio verkauft weder Werbung noch Daten."
  - q: "Wie viele Apps hat Lagerland Apps?"
    a: "Lagerland Apps hat {APP_COUNT} Apps für Apple-Plattformen im App Store: für Gesundheit und Training, Tagesplanung, Rechnungen, Lesen, Brettspiele und Logikrätsel, Werkzeuge für App-Store-Entwickler und das Umwandeln von Dateien."
  - q: "Sammelt Lagerland Apps Daten über mich?"
    a: "Keine App enthält ein Analyse- oder Werbe-SDK von Drittanbietern, keine verlangt ein Konto, und keine schickt deine Daten an einen Server des Studios. Deine Daten bleiben auf deinem Gerät, und Apps mit Synchronisierung nutzen deine eigene iCloud. Apps, die für ihre Aufgabe das Internet brauchen, etwa WanderWiki für Wikipedia oder die Entwicklerwerkzeuge für App Store Connect, verbinden sich direkt mit diesem Dienst."
  - q: "Für welche Geräte entwickelt Lagerland Apps?"
    a: "Lagerland Apps entwickelt native Apps für iPhone, iPad, Apple Watch und Mac mit Apples eigenen Frameworks, ohne plattformübergreifende Wrapper und ohne Electron. Auf jeder App-Seite steht, auf welchen Geräten die App läuft."
last_updated: 2026-10-29
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
      Lagerland Apps ist ein Ein-Personen-Studio in Finnland. Ein einziger unabhängiger Apple-Entwickler entwirft, programmiert, testet, veröffentlicht und betreut jede App. Rechenschaft schuldig ist das Studio den Menschen, die für die Apps bezahlen, und weder Investoren noch Werbekunden.
    </p>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Die Haltung dahinter</h2>
  <div class="grid grid-2 stagger">
    <div class="card">
      <div class="card-title">Standardmäßig privat</div>
      <div class="card-text">Keine App enthält ein Werbe- oder Analyse-SDK oder fragt nach der IDFA, und keine schickt deine Daten an einen Server von uns. Deine Daten bleiben auf deinem Gerät, und jede Synchronisierung läuft über deine eigene iCloud. Was jede App angibt, steht auf der <a href="{% include l.html url="/transparency/" %}"{% if l_en %} hreflang="en"{% endif %}>Transparenzseite{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>.</div>
    </div>
    <div class="card">
      <div class="card-title">Wie die Apps bezahlt werden</div>
      <div class="card-text">Die meisten Apps sind kostenlos, mit einem optionalen Upgrade als Abo, als Einmalkauf oder in beiden Formen. Mockly ist die einzige App, die du vorab kaufst. Jeder Kauf läuft über Apple: Du siehst den Preis, bevor du bestätigst, und ein Abo verwaltest oder kündigst du auf iPhone oder iPad in den Einstellungen, auf dem Mac in der App „App Store“.</div>
    </div>
    <div class="card">
      <div class="card-title">Eine App, eine Aufgabe</div>
      <div class="card-text">Jede App erledigt eine Aufgabe: den Tag planen, ein Training eintragen, an eine Rechnung erinnern, ein Brettspiel lernen. Du installierst die, die du brauchst, und sonst nichts.</div>
    </div>
    <div class="card">
      <div class="card-title">Nativ für Apple-Geräte</div>
      <div class="card-text">Entwickelt mit Apples eigenen Frameworks, ohne plattformübergreifende Wrapper und ohne Electron. Die Apps nutzen, was dein Gerät schon mitbringt, etwa Apple Health, Widgets, Siri und iCloud, wo die App sie braucht.</div>
    </div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Plattformen</h2>
  <div class="grid grid-4 stagger">
    <div class="card"><div class="card-title">iPhone</div><div class="card-text">Fast jede App, von Gesundheit und Planung bis zu Rechnungen, Lesen und Spielen.</div></div>
    <div class="card"><div class="card-title">iPad</div><div class="card-text">Die Brettspiele, beide Logikrätsel, Observa, Pawza, Taskful Day und WanderWiki.</div></div>
    <div class="card"><div class="card-title">Apple Watch</div><div class="card-text">GymLogger X, Observa und Taskful Day, dazu die Apple-Watch-App von EarnLock mit Premium.</div></div>
    <div class="card"><div class="card-title">Mac</div><div class="card-text">AppMeta und Mockly für App-Store-Entwickler, MediaKit, Taskful Day und die drei Brettspiele.</div></div>
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
