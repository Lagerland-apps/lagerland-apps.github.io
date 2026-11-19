---
layout: default
ref: /lagerland-apps/
permalink: /es/lagerland-apps/
translated_from: 2026-10-30
title: "Sobre Lagerland Apps, desarrollador independiente"
quick_answer: "Lagerland Apps es un estudio de una sola persona en Finlandia que crea apps para Apple. Un único desarrollador independiente diseña, programa, prueba y da soporte a sus {APP_COUNT} apps para iPhone, iPad, Apple Watch y Mac. Ninguna app incluye SDK de publicidad o de analítica, solicita el IDFA ni te pide crear una cuenta, y ninguna envía tus datos a un servidor del estudio. El estudio se financia con lo que pagan quienes compran las apps."
seo:
  title: "Lagerland Apps: desarrollador independiente en Finlandia"
  description: "Estudio de una sola persona en Finlandia: {APP_COUNT} apps para iPhone, iPad, Apple Watch y Mac sin anuncios, rastreadores ni cuentas. Se financia con apps de pago."
  keywords:
    - lagerland apps
    - lagerland
    - desarrollador independiente
    - desarrollador de aplicaciones
    - desarrollador de aplicaciones móviles
faq:
  - q: "¿Quién está detrás de Lagerland Apps?"
    a: "Lagerland Apps es un estudio de apps para Apple en Finlandia, y lo lleva un único desarrollador independiente. Esa persona diseña, programa, prueba, publica y da soporte a cada app. No hay equipo, inversores ni anunciantes."
  - q: "¿Dónde tiene su sede Lagerland Apps?"
    a: "Lagerland Apps tiene su sede en Finlandia, en la UE, y publica sus apps en todo el mundo en el App Store con el identificador de desarrollador 1855943133."
  - q: "¿Cómo se financia Lagerland Apps si no hay publicidad?"
    a: "Quienes usan las apps son quienes las pagan. La mayoría se descargan gratis y ofrecen una mejora opcional de pago, que se vende como suscripción, como compra única o de las dos formas. Mockly es la única que pagas al descargarla. El estudio no vende publicidad ni datos."
  - q: "¿Cuántas apps publica Lagerland Apps?"
    a: "Lagerland Apps publica {APP_COUNT} apps para las plataformas de Apple, que abarcan salud y entrenamiento, planificación del día, facturas, lectura, juegos de mesa y de lógica, herramientas para quienes publican en el App Store y conversión de archivos."
  - q: "¿Lagerland Apps recopila tus datos?"
    a: "Ninguna app incluye un SDK de analítica o de publicidad de terceros, ninguna exige una cuenta y ninguna envía tus datos a un servidor del estudio. Tus datos se quedan en tu dispositivo, y las apps que sincronizan usan tu propio iCloud. Las apps que necesitan internet para su función, como WanderWiki con Wikipedia o las herramientas para desarrolladores con App Store Connect, se conectan directamente a ese servicio."
  - q: "¿Para qué dispositivos desarrolla Lagerland Apps?"
    a: "Lagerland Apps desarrolla apps nativas para iPhone, iPad, Apple Watch y Mac con los frameworks propios de Apple, sin capas multiplataforma ni Electron. La página de cada app indica en qué dispositivos funciona."
last_updated: 2026-11-19
---
{%- include t.html -%}

{%- comment %} ===== Apps with a Spanish page, in master order (apps without one are left out) ===== {% endcomment -%}
{%- assign live_apps = site.apps | where: "status", "live" -%}
{%- assign es_apps = "" | split: "" -%}
{%- for app in live_apps -%}
  {%- include tx-app.html app=app -%}
  {%- unless tx_en -%}{%- assign es_apps = es_apps | push: app -%}{%- endunless -%}
{%- endfor -%}

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "AboutPage",
      "@id": "{{ site.url }}/es/lagerland-apps/#webpage",
      "url": "{{ site.url }}/es/lagerland-apps/",
      "name": "Sobre Lagerland Apps",
      "description": "Lagerland Apps es un estudio de una sola persona en Finlandia que crea apps para iOS y macOS respetuosas con la privacidad.",
      "inLanguage": "es-ES",
      "isPartOf": { "@id": "{{ site.url }}/es/#website" },
      "about": { "@id": "{{ site.url }}/#organization" },
      "mainEntity": { "@id": "{{ site.url }}/#organization" },
      "breadcrumb": {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Lagerland Apps", "item": "{{ site.url }}/es/" },
          { "@type": "ListItem", "position": 2, "name": "Sobre Lagerland Apps", "item": "{{ site.url }}/es/lagerland-apps/" }
        ]
      }
    },
    {
      "@type": "FAQPage",
      "@id": "{{ site.url }}/es/lagerland-apps/#faq",
      "inLanguage": "es-ES",
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
    <p class="overline">Desarrollador independiente · Estudio de una sola persona · Finlandia</p>
    <h1 class="h1">
      Apps hechas por <span class="gradient-text">una sola persona</span><br>para quienes echan de menos el software tranquilo.
    </h1>
    <p class="lead">
      Lagerland Apps es un estudio de una sola persona en Finlandia. Un único desarrollador independiente de apps para Apple diseña, programa, prueba, publica y da soporte a cada app, y responde ante quienes las pagan, sin inversores ni anunciantes por medio.
    </p>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">La filosofía del estudio</h2>
  <div class="grid grid-2 stagger">
    <div class="card">
      <div class="card-title">Privadas por defecto</div>
      <div class="card-text">Ninguna app incluye un SDK de publicidad o de analítica ni solicita el IDFA, y ninguna envía tus datos a un servidor del estudio. Tus datos se quedan en tu dispositivo, y cualquier sincronización usa tu propio iCloud. Lo que declara cada app figura en la <a href="{% include l.html url="/transparency/" %}"{% if l_en %} hreflang="en"{% endif %}>página de transparencia{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>.</div>
    </div>
    <div class="card">
      <div class="card-title">Cómo se financian las apps</div>
      <div class="card-text">La mayoría de las apps se descargan gratis y ofrecen una mejora opcional, que se vende como suscripción, como compra única o de las dos formas. Mockly es la única que pagas al descargarla. Todas las compras pasan por Apple, así que ves el precio antes de confirmar, y gestionas o cancelas una suscripción en la app Ajustes del iPhone o el iPad, o en la app App Store del Mac.</div>
    </div>
    <div class="card">
      <div class="card-title">Una app, una tarea</div>
      <div class="card-text">Cada app hace una sola cosa: planificar el día, registrar un entrenamiento, acordarte de una factura, aprender un juego de mesa. Instalas las que necesitas y nada más.</div>
    </div>
    <div class="card">
      <div class="card-title">Nativas en los dispositivos de Apple</div>
      <div class="card-text">Creadas con los frameworks propios de Apple, sin capas multiplataforma ni Electron. Las apps aprovechan lo que tu dispositivo ya ofrece, como la app Salud, los widgets, Siri e iCloud, cuando la app los necesita.</div>
    </div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Plataformas</h2>
  <div class="grid grid-4 stagger">
    <div class="card"><div class="card-title">iPhone</div><div class="card-text">Casi todas las apps, desde la salud y la planificación hasta las facturas, la lectura y los juegos.</div></div>
    <div class="card"><div class="card-title">iPad</div><div class="card-text">Los juegos de mesa, los dos juegos de lógica, Observa, Pawza, Taskful Day y WanderWiki.</div></div>
    <div class="card"><div class="card-title">Apple Watch</div><div class="card-text">GymLogger X, Observa y Taskful Day, además de la app para el Apple Watch de EarnLock con Premium.</div></div>
    <div class="card"><div class="card-title">Mac</div><div class="card-text">AppMeta y Mockly para quienes publican en el App Store, MediaKit, Taskful Day y los tres juegos de mesa.</div></div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">El catálogo: {{ es_apps.size }} apps</h2>
  <p class="lead">Todas las apps publicadas de Lagerland Apps. Aquí las tienes una por una; para explorarlas por categoría, ve a la <a href="{% include l.html url="/apps/" %}"{% if l_en %} hreflang="en"{% endif %}>página del catálogo completo{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>.</p>
  <div class="grid grid-2 stagger">
    {%- for app in es_apps -%}{% include app-card.html app=app %}{%- endfor -%}
  </div>
</section>

<section id="faq" class="section reveal">
  <div class="section-center"><p class="overline">Preguntas</p><h2 class="h2">Preguntas frecuentes sobre Lagerland Apps</h2></div>
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
  <h2 class="h2">Contacto</h2>
  <div class="card">
    <p>Para prensa, colaboraciones, avisos de errores o cualquier otra consulta:</p>
    <div class="actions" style="margin-top:var(--s-4);">
      <a class="btn btn-primary" href="mailto:support@lagerland.app">support@lagerland.app</a>
      <a class="btn btn-secondary" href="{% include l.html url="/support/" %}"{% if l_en %} hreflang="en"{% endif %}>Soporte general{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>
    </div>
  </div>
</section>
