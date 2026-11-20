---
layout: default
ref: /lagerland-apps/
permalink: /nl/lagerland-apps/
translated_from: 2026-11-20
title: "Lagerland Apps, indie appontwikkelaar in Finland"
quick_answer: "Lagerland Apps is een Apple-studio van één persoon in Finland. Eén onafhankelijke ontwikkelaar ontwerpt, programmeert, test en ondersteunt alle {APP_COUNT} apps, voor iPhone, iPad, Apple Watch en Mac. Geen enkele app bevat reclame- of analyse-SDK’s, vraagt om de reclame-ID (IDFA) of wil dat je een account aanmaakt, en geen enkele stuurt je gegevens naar een server van de studio. De studio wordt gefinancierd door de mensen die voor de apps betalen."
seo:
  title: "Lagerland Apps: indie appontwikkelaar in Finland"
  description: "Indie apps voor iPhone, iPad, Apple Watch en Mac van één ontwikkelaar in Finland: {APP_COUNT} apps zonder reclame, trackers of accounts. Betaald door app-aankopen."
  keywords:
    - lagerland apps
    - indie apps iphone
    - indie ontwikkelaar apps
    - indie appontwikkelaar
    - apps van een kleine ontwikkelaar
faq:
  - q: "Wie maakt de apps van Lagerland Apps?"
    a: "Lagerland Apps is een Apple-studio van één persoon in Finland, gerund door één onafhankelijke ontwikkelaar. Dezelfde persoon ontwerpt, programmeert, test, publiceert en ondersteunt elke app. Er is geen team en er zijn geen investeerders of adverteerders."
  - q: "Waar zit Lagerland Apps?"
    a: "Lagerland Apps zit in Finland, in de EU, en publiceert de apps wereldwijd in de App Store onder ontwikkelaars-ID 1855943133."
  - q: "Hoe wordt Lagerland Apps betaald zonder reclame?"
    a: "De mensen die de apps gebruiken, betalen ervoor. De meeste apps zijn gratis te downloaden, met een optionele betaalde upgrade als abonnement, als eenmalige aankoop of als allebei. Mockly en OneHander zijn de twee apps waarvoor je vooraf betaalt. De studio verkoopt geen reclame of gegevens."
  - q: "Hoeveel apps heeft Lagerland Apps?"
    a: "Lagerland Apps heeft {APP_COUNT} live apps voor Apple-platforms. Ze gaan over gezondheid en training, dagplanning, rekeningen, lezen, bordspellen en logische puzzels, tools voor App Store-ontwikkelaars en bestandsconversie."
  - q: "Verzamelt Lagerland Apps gegevens over mij?"
    a: "Geen enkele app bevat een analyse- of reclame-SDK van derden of vraagt om een account, en geen enkele stuurt je gegevens naar een server van de studio. Je gegevens blijven op je apparaat, en apps die synchroniseren gebruiken je eigen iCloud. Apps die voor hun taak internet nodig hebben, zoals WanderWiki voor Wikipedia of de ontwikkelaarstools voor App Store Connect, maken rechtstreeks verbinding met die dienst."
  - q: "Voor welke platforms maakt Lagerland Apps apps?"
    a: "Lagerland Apps maakt native apps voor iPhone, iPad, Apple Watch en Mac met de eigen frameworks van Apple, zonder platformoverschrijdende wrappers of Electron. Op de pagina van elke app staat op welke apparaten die app draait."
last_updated: 2026-11-20
---
{%- include t.html -%}

{%- comment %} ===== Apps with a Dutch page, in master order (apps without one are left out) ===== {% endcomment -%}
{%- assign live_apps = site.apps | where: "status", "live" -%}
{%- assign nl_apps = "" | split: "" -%}
{%- for app in live_apps -%}
  {%- include tx-app.html app=app -%}
  {%- unless tx_en -%}{%- assign nl_apps = nl_apps | push: app -%}{%- endunless -%}
{%- endfor -%}

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "AboutPage",
      "@id": "{{ site.url }}/nl/lagerland-apps/#webpage",
      "url": "{{ site.url }}/nl/lagerland-apps/",
      "name": "Over Lagerland Apps",
      "description": "Lagerland Apps is een Apple-studio van één persoon in Finland die iOS- en macOS-apps maakt met privacy voorop.",
      "inLanguage": "nl",
      "isPartOf": { "@id": "{{ site.url }}/nl/#website" },
      "about": { "@id": "{{ site.url }}/#organization" },
      "mainEntity": { "@id": "{{ site.url }}/#organization" },
      "breadcrumb": {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Lagerland Apps", "item": "{{ site.url }}/nl/" },
          { "@type": "ListItem", "position": 2, "name": "Over ons", "item": "{{ site.url }}/nl/lagerland-apps/" }
        ]
      }
    },
    {
      "@type": "FAQPage",
      "@id": "{{ site.url }}/nl/lagerland-apps/#faq",
      "inLanguage": "nl",
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
    <p class="overline">Onafhankelijke Apple-ontwikkelaar · Studio van één persoon · Finland</p>
    <h1 class="h1">
      Gemaakt door <span class="gradient-text">één persoon</span><br>voor mensen die rustige software missen.
    </h1>
    <p class="lead">
      Lagerland Apps is een studio van één persoon in Finland. Eén onafhankelijke Apple-ontwikkelaar ontwerpt, programmeert, test, publiceert en ondersteunt elke app, en legt verantwoording af aan de mensen die ervoor betalen. Er zitten geen investeerders of adverteerders tussen.
    </p>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">De aanpak</h2>
  <div class="grid grid-2 stagger">
    <div class="card">
      <div class="card-title">Standaard privé</div>
      <div class="card-text">Geen enkele app bevat een reclame- of analyse-SDK of vraagt om de reclame-ID (IDFA), en geen enkele stuurt je gegevens naar een server van ons. Je gegevens blijven op je apparaat en synchronisatie loopt via je eigen iCloud. Wat elke app opgeeft, staat op de <a href="{% include l.html url="/transparency/" %}"{% if l_en %} hreflang="en"{% endif %}>transparantiepagina{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>.</div>
    </div>
    <div class="card">
      <div class="card-title">Hoe de apps betaald worden</div>
      <div class="card-text">De meeste apps zijn gratis te downloaden, met een optionele upgrade als abonnement, als eenmalige aankoop of als allebei. Mockly en OneHander zijn de twee apps waarvoor je vooraf betaalt. Elke aankoop loopt via Apple, dus je ziet de prijs voordat je bevestigt. Een abonnement beheer je of zeg je op in Instellingen op de iPhone of iPad, of in de App Store-app op de Mac.</div>
    </div>
    <div class="card">
      <div class="card-title">Tools met één taak</div>
      <div class="card-text">Elke app doet één ding: de dag plannen, een training bijhouden, aan een rekening denken, een bordspel leren. Je installeert wat je nodig hebt en niets anders.</div>
    </div>
    <div class="card">
      <div class="card-title">Native op Apple-apparaten</div>
      <div class="card-text">Gebouwd met de eigen frameworks van Apple, zonder platformoverschrijdende wrappers of Electron. De apps gebruiken wat je apparaat al heeft, zoals de Gezondheid-app, widgets, Siri en iCloud, waar de app dat nodig heeft.</div>
    </div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Platforms</h2>
  <div class="grid grid-4 stagger">
    <div class="card"><div class="card-title">iPhone</div><div class="card-text">Bijna elke app, van gezondheid en planning tot rekeningen, lezen en games.</div></div>
    <div class="card"><div class="card-title">iPad</div><div class="card-text">De bordspellen, beide logische puzzels, Observa, Pawza, Taskful Day en WanderWiki.</div></div>
    <div class="card"><div class="card-title">Apple Watch</div><div class="card-text">GymLogger X, Observa en Taskful Day, plus de Apple Watch-app van EarnLock met Premium.</div></div>
    <div class="card"><div class="card-title">Mac</div><div class="card-text">AppMeta en Mockly voor App Store-ontwikkelaars, MediaKit, Taskful Day en de drie bordspellen.</div></div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">De catalogus: {{ nl_apps.size }} apps</h2>
  <p class="lead">Alle live apps van Lagerland Apps. Per categorie vind je ze op de <a href="{% include l.html url="/apps/" %}"{% if l_en %} hreflang="en"{% endif %}>pagina met de volledige catalogus{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>; hieronder staan ze een voor een.</p>
  <div class="grid grid-2 stagger">
    {%- for app in nl_apps -%}{% include app-card.html app=app %}{%- endfor -%}
  </div>
</section>

<section id="faq" class="section reveal">
  <div class="section-center"><p class="overline">Vragen</p><h2 class="h2">Veelgestelde vragen over Lagerland Apps</h2></div>
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
    <p>Voor pers, samenwerkingen, bugmeldingen of andere vragen:</p>
    <div class="actions" style="margin-top:var(--s-4);">
      <a class="btn btn-primary" href="mailto:support@lagerland.app">support@lagerland.app</a>
      <a class="btn btn-secondary" href="{% include l.html url="/support/" %}"{% if l_en %} hreflang="en"{% endif %}>Algemene ondersteuning{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>
    </div>
  </div>
</section>
