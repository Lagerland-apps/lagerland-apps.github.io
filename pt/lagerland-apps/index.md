---
layout: default
ref: /lagerland-apps/
permalink: /pt/lagerland-apps/
translated_from: 2026-11-20
title: "Lagerland Apps, programador independente na Finlândia"
quick_answer: "A Lagerland Apps é um estúdio de apps para Apple de uma só pessoa, na Finlândia. Um único programador independente concebe, programa, testa e dá apoio a todas as suas {APP_COUNT} apps para iPhone, iPad, Apple Watch e Mac. Nenhuma app inclui SDK de publicidade ou de análise, pede o IDFA ou a criação de uma conta, e nenhuma envia os dados de quem a usa para um servidor do estúdio. O estúdio financia-se com o que pagam as pessoas que compram as apps."
seo:
  title: "Lagerland Apps: programador independente na Finlândia"
  description: "Estúdio de uma só pessoa na Finlândia: {APP_COUNT} apps para iPhone, iPad, Apple Watch e Mac, sem anúncios, sem seguimento e sem contas. Financiado por apps pagas."
  keywords:
    - lagerland apps
    - lagerland
    - programador independente
    - desenvolvedor de aplicações para ios
    - desenvolvedor independente
faq:
  - q: "Quem está por trás da Lagerland Apps?"
    a: "A Lagerland Apps é um estúdio de apps para Apple na Finlândia, dirigido por um único programador independente. Essa pessoa concebe, programa, testa, publica e dá apoio a cada app. Não há equipa, investidores nem anunciantes."
  - q: "Onde fica a sede da Lagerland Apps?"
    a: "A Lagerland Apps tem sede na Finlândia, na UE, e publica as apps em todo o mundo na App Store com o identificador de programador 1855943133."
  - q: "Como se financia a Lagerland Apps, se não há publicidade?"
    a: "Quem usa as apps é quem as paga. A maioria descarrega-se grátis e oferece uma melhoria paga opcional, vendida como subscrição, como compra única ou das duas formas. O Mockly e o OneHander são as duas que se pagam logo à partida. O estúdio não vende publicidade nem dados."
  - q: "Quantas apps publica a Lagerland Apps?"
    a: "A Lagerland Apps publica {APP_COUNT} apps disponíveis para as plataformas Apple, nas áreas de saúde e treino, planeamento do dia, contas a pagar, leitura, jogos de tabuleiro e de lógica, ferramentas para quem publica na App Store e conversão de ficheiros."
  - q: "A Lagerland Apps recolhe dados dos utilizadores?"
    a: "Nenhuma app inclui um SDK de análise ou de publicidade de terceiros, nenhuma exige uma conta e nenhuma envia dados para um servidor do estúdio. Os dados ficam no dispositivo, e as apps que sincronizam usam o iCloud de cada utilizador. As apps que precisam da internet para a sua função, como o WanderWiki com a Wikipédia ou as ferramentas para programadores com o App Store Connect, ligam-se diretamente a esse serviço."
  - q: "Para que plataformas cria a Lagerland Apps?"
    a: "A Lagerland Apps cria apps nativas para iPhone, iPad, Apple Watch e Mac com as frameworks da própria Apple, sem camadas multiplataforma nem Electron. A página de cada app indica os dispositivos em que funciona."
last_updated: 2026-11-20
---
{%- include t.html -%}

{%- comment %} ===== Apps with a Portuguese page, in master order (apps without one are left out) ===== {% endcomment -%}
{%- assign live_apps = site.apps | where: "status", "live" -%}
{%- assign pt_apps = "" | split: "" -%}
{%- for app in live_apps -%}
  {%- include tx-app.html app=app -%}
  {%- unless tx_en -%}{%- assign pt_apps = pt_apps | push: app -%}{%- endunless -%}
{%- endfor -%}

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "AboutPage",
      "@id": "{{ site.url }}/pt/lagerland-apps/#webpage",
      "url": "{{ site.url }}/pt/lagerland-apps/",
      "name": "Sobre a Lagerland Apps",
      "description": "A Lagerland Apps é um estúdio de uma só pessoa na Finlândia que cria apps para iOS e macOS que respeitam a privacidade.",
      "inLanguage": "pt-PT",
      "isPartOf": { "@id": "{{ site.url }}/pt/#website" },
      "about": { "@id": "{{ site.url }}/#organization" },
      "mainEntity": { "@id": "{{ site.url }}/#organization" },
      "breadcrumb": {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Lagerland Apps", "item": "{{ site.url }}/pt/" },
          { "@type": "ListItem", "position": 2, "name": "Sobre a Lagerland Apps", "item": "{{ site.url }}/pt/lagerland-apps/" }
        ]
      }
    },
    {
      "@type": "FAQPage",
      "@id": "{{ site.url }}/pt/lagerland-apps/#faq",
      "inLanguage": "pt-PT",
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
    <p class="overline">Programador Apple independente · Estúdio de uma só pessoa desde 2025 · Finlândia</p>
    <h1 class="h1">
      Apps feitas por <span class="gradient-text">uma só pessoa</span><br>para quem sente falta de software calmo.
    </h1>
    <p class="lead">
      A Lagerland Apps é um estúdio de uma só pessoa na Finlândia. Um único programador Apple independente concebe, programa, testa, publica e dá apoio a cada app, e responde perante quem as paga, sem investidores nem anunciantes pelo meio.
    </p>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">A filosofia do estúdio</h2>
  <div class="grid grid-2 stagger">
    <div class="card">
      <div class="card-title">Privadas por predefinição</div>
      <div class="card-text">Nenhuma app inclui um SDK de publicidade ou de análise nem pede o IDFA, e nenhuma envia dados para um servidor do estúdio. Os dados ficam no dispositivo, e qualquer sincronização usa o iCloud de cada utilizador. O que cada app declara está indicado na <a href="{% include l.html url="/transparency/" %}"{% if l_en %} hreflang="en"{% endif %}>página de transparência{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>.</div>
    </div>
    <div class="card">
      <div class="card-title">Como as apps se financiam</div>
      <div class="card-text">A maioria das apps descarrega-se grátis e oferece uma melhoria opcional, vendida como subscrição, como compra única ou das duas formas. O Mockly e o OneHander são as duas que se pagam logo à partida. Todas as compras passam pela Apple, por isso o preço aparece antes de confirmar, e uma subscrição gere-se ou cancela-se na app Definições do iPhone ou do iPad, ou na app App Store do Mac.</div>
    </div>
    <div class="card">
      <div class="card-title">Uma app, uma tarefa</div>
      <div class="card-text">Cada app faz uma só coisa: planear o dia, registar um treino, lembrar uma conta a pagar, aprender um jogo de tabuleiro. Instalam-se as que fazem falta e mais nada.</div>
    </div>
    <div class="card">
      <div class="card-title">Nativas nos dispositivos Apple</div>
      <div class="card-text">Criadas com as frameworks da própria Apple, sem camadas multiplataforma nem Electron. As apps aproveitam o que o dispositivo já tem, como a app Saúde, os widgets, a Siri e o iCloud, quando precisam.</div>
    </div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">Plataformas</h2>
  <div class="grid grid-4 stagger">
    <div class="card"><div class="card-title">iPhone</div><div class="card-text">Quase todas as apps, da saúde e do planeamento às contas a pagar, à leitura e aos jogos.</div></div>
    <div class="card"><div class="card-title">iPad</div><div class="card-text">Os jogos de tabuleiro, os dois jogos de lógica, Observa, Pawza, Taskful Day e WanderWiki.</div></div>
    <div class="card"><div class="card-title">Apple Watch</div><div class="card-text">GymLogger X, Observa e Taskful Day, e ainda a app do EarnLock para o Apple Watch, com o Premium.</div></div>
    <div class="card"><div class="card-title">Mac</div><div class="card-text">AppMeta e Mockly para quem publica na App Store, MediaKit, Taskful Day e os três jogos de tabuleiro.</div></div>
  </div>
</section>

<section class="section reveal">
  <h2 class="h2">O catálogo: {{ pt_apps.size }} apps</h2>
  <p class="lead">Todas as apps publicadas da Lagerland Apps, uma a uma. Para as explorar por categoria, abra a <a href="{% include l.html url="/apps/" %}"{% if l_en %} hreflang="en"{% endif %}>página do catálogo completo{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>.</p>
  <div class="grid grid-2 stagger">
    {%- for app in pt_apps -%}{% include app-card.html app=app %}{%- endfor -%}
  </div>
</section>

<section id="faq" class="section reveal">
  <div class="section-center"><p class="overline">Perguntas</p><h2 class="h2">Perguntas frequentes sobre a Lagerland Apps</h2></div>
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
    <p>Para imprensa, parcerias, comunicação de erros ou questões gerais:</p>
    <div class="actions" style="margin-top:var(--s-4);">
      <a class="btn btn-primary" href="mailto:support@lagerland.app">support@lagerland.app</a>
      <a class="btn btn-secondary" href="{% include l.html url="/support/" %}"{% if l_en %} hreflang="en"{% endif %}>Apoio geral{% if l_en %} <span class="en-marker">{{ t.english_marker }}</span>{% endif %}</a>
    </div>
  </div>
</section>
