---
layout: default
ref: /lagerland-apps/
permalink: /fr/lagerland-apps/
translated_from: 2026-10-30
title: "À propos de Lagerland Apps, développeur indépendant"
quick_answer: "Lagerland Apps est un studio Apple d’une seule personne, en Finlande. Un seul développeur indépendant conçoit, programme, teste et assure le support des {APP_COUNT} apps, pour iPhone, iPad, Apple Watch et Mac. Aucune ne contient de SDK publicitaire ou d’analyse, ne demande l’IDFA ni ne vous oblige à créer un compte, et aucune n’envoie vos données à un serveur du studio. Le studio est financé par les personnes qui paient pour les apps."
seo:
  title: "Lagerland Apps : développeur indépendant en Finlande"
  description: "Studio d’une personne en Finlande : {APP_COUNT} apps pour iPhone, iPad, Apple Watch et Mac, sans publicité, sans suivi ni compte. Financé par les achats."
  keywords:
    - lagerland apps
    - développeur indépendant
    - développeur d’applications
    - développeur apple indépendant
    - studio d’applications finlande
    - développeur ios indépendant
    - application sans pub iphone
faq:
  - q: "Qui est derrière Lagerland Apps ?"
    a: "Lagerland Apps est un studio Apple indépendant d’une seule personne, en Finlande. Une seule personne conçoit, programme, teste, publie et assure le support de chaque app. Il n’y a ni équipe, ni investisseur, ni annonceur."
  - q: "Où est basé Lagerland Apps ?"
    a: "Lagerland Apps est basé en Finlande, dans l’UE, et publie ses apps dans le monde entier sur l’App Store, sous l’identifiant de développeur 1855943133."
  - q: "Comment Lagerland Apps est-il financé sans publicité ?"
    a: "Ce sont les personnes qui utilisent les apps qui les financent. La plupart des apps sont gratuites à télécharger, avec une mise à niveau facultative proposée en abonnement, en achat unique ou les deux. Mockly est la seule app que vous payez d’emblée. Le studio ne vend ni publicité ni données."
  - q: "Combien d’apps Lagerland Apps publie-t-il ?"
    a: "Lagerland Apps publie {APP_COUNT} apps pour les plateformes Apple, qui couvrent la santé et l’entraînement, la planification de la journée, les factures, la lecture, les jeux de société et de logique, des outils pour les développeurs qui publient sur l’App Store et la conversion de fichiers."
  - q: "Lagerland Apps collecte-t-il des données sur moi ?"
    a: "Aucune app ne contient de SDK d’analyse ou de publicité tiers, aucune n’exige de compte et aucune n’envoie vos données à un serveur du studio. Vos données restent sur votre appareil, et les apps qui synchronisent utilisent votre propre iCloud. Les apps qui ont besoin d’internet pour leur fonction, comme WanderWiki pour Wikipédia ou les outils pour développeurs pour App Store Connect, se connectent directement à ce service."
  - q: "Pour quels appareils Lagerland Apps développe-t-il ?"
    a: "Lagerland Apps développe des apps natives pour iPhone, iPad, Apple Watch et Mac avec les frameworks d’Apple, sans surcouche multiplateforme ni Electron. La page de chaque app indique les appareils sur lesquels elle fonctionne."
last_updated: 2026-11-08
---
{%- include t.html -%}

{%- comment %} ===== Apps with a French page, in master order (apps without one are left out) ===== {% endcomment -%}
{%- assign live_apps = site.apps | where: "status", "live" -%}
{%- assign fr_apps = "" | split: "" -%}
{%- for app in live_apps -%}
  {%- include tx-app.html app=app -%}
  {%- unless tx_en -%}{%- assign fr_apps = fr_apps | push: app -%}{%- endunless -%}
{%- endfor -%}

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "AboutPage",
      "@id": "{{ site.url }}/fr/lagerland-apps/#webpage",
      "url": "{{ site.url }}/fr/lagerland-apps/",
      "name": "À propos de Lagerland Apps",
      "description": "Lagerland Apps est un studio d’une seule personne en Finlande qui développe des apps iOS et macOS où la vie privée passe d’abord.",
      "inLanguage": "fr",
      "isPartOf": { "@id": "{{ site.url }}/fr/#website" },
      "about": { "@id": "{{ site.url }}/#organization" },
      "mainEntity": { "@id": "{{ site.url }}/#organization" },
      "breadcrumb": {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Lagerland Apps", "item": "{{ site.url }}/fr/" },
          { "@type": "ListItem", "position": 2, "name": "À propos", "item": "{{ site.url }}/fr/lagerland-apps/" }
        ]
      }
    },
    {
      "@type": "FAQPage",
      "@id": "{{ site.url }}/fr/lagerland-apps/#faq",
      "inLanguage": "fr",
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
    <p class="overline">Développeur Apple indépendant · Studio d’une seule personne · Finlande</p>
    <h1 class="h1">
      Conçues par <span class="gradient-text">une seule personne</span><br>pour celles et ceux qui regrettent les logiciels calmes.
    </h1>
    <p class="lead">
      Lagerland Apps est un studio d’une seule personne en Finlande. Un seul développeur Apple indépendant conçoit, programme, teste, publie et assure le support de chaque app. Le studio ne répond qu’aux personnes qui achètent les apps, sans investisseurs ni annonceurs entre les deux.
    </p>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">La philosophie du studio</h2>
  <div class="grid grid-2 stagger">
    <div class="card">
      <div class="card-title">Privé par défaut</div>
      <div class="card-text">Aucune app ne contient de SDK publicitaire ou d’analyse ni ne demande l’IDFA, et aucune n’envoie vos données à un serveur du studio. Vos données restent sur votre appareil, et toute synchronisation passe par votre propre iCloud. Ce que chaque app déclare figure sur la <a href="{% include l.html url="/transparency/" %}"{% if l_en %} hreflang="en"{% endif %}>page de transparence{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>.</div>
    </div>
    <div class="card">
      <div class="card-title">Comment les apps sont financées</div>
      <div class="card-text">La plupart des apps sont gratuites à télécharger, avec une mise à niveau facultative proposée en abonnement, en achat unique ou les deux. Mockly est la seule app que vous payez d’emblée. Chaque achat passe par Apple : vous voyez le prix avant de confirmer, et vous gérez ou annulez un abonnement dans Réglages sur iPhone ou iPad, ou dans l’app App Store sur Mac.</div>
    </div>
    <div class="card">
      <div class="card-title">Une app, une tâche</div>
      <div class="card-text">Chaque app fait une seule chose : planifier la journée, noter une séance, se rappeler une facture, apprendre un jeu de société. Vous installez celles dont vous avez besoin, et rien d’autre.</div>
    </div>
    <div class="card">
      <div class="card-title">Natif sur les appareils Apple</div>
      <div class="card-text">Conçues avec les frameworks d’Apple, sans surcouche multiplateforme ni Electron. Les apps s’appuient sur ce que votre appareil offre déjà, comme l’app Santé, les widgets, Siri et iCloud, là où l’app en a besoin.</div>
    </div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Plateformes</h2>
  <div class="grid grid-4 stagger">
    <div class="card"><div class="card-title">iPhone</div><div class="card-text">Presque toutes les apps, de la santé et la planification aux factures, à la lecture et aux jeux.</div></div>
    <div class="card"><div class="card-title">iPad</div><div class="card-text">Les jeux de société, les deux jeux de logique, Observa, Pawza, Taskful Day et WanderWiki.</div></div>
    <div class="card"><div class="card-title">Apple Watch</div><div class="card-text">GymLogger X, Observa et Taskful Day, plus l’app Apple Watch d’EarnLock avec Premium.</div></div>
    <div class="card"><div class="card-title">Mac</div><div class="card-text">AppMeta et Mockly pour les développeurs qui publient sur l’App Store, MediaKit, Taskful Day et les trois jeux de société.</div></div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Le catalogue : {{ fr_apps.size }} apps</h2>
  <p class="lead">Toutes les apps publiées de Lagerland Apps. Les voici une par une ; pour les parcourir par catégorie, rendez-vous sur la <a href="{% include l.html url="/apps/" %}"{% if l_en %} hreflang="en"{% endif %}>page du catalogue{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>.</p>
  <div class="grid grid-2 stagger">
    {%- for app in fr_apps -%}{% include app-card.html app=app %}{%- endfor -%}
  </div>
</section>

<section id="faq" class="section reveal">
  <div class="section-center"><p class="overline">Questions</p><h2 class="h2">Questions fréquentes sur Lagerland Apps</h2></div>
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
    <p>Pour la presse, les partenariats, les signalements de bugs ou toute autre question :</p>
    <div class="actions" style="margin-top:var(--s-4);">
      <a class="btn btn-primary" href="mailto:support@lagerland.app">support@lagerland.app</a>
      <a class="btn btn-secondary" href="{% include l.html url="/support/" %}"{% if l_en %} hreflang="en"{% endif %}>Support général{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>
    </div>
  </div>
</section>
