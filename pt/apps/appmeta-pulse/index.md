---
layout: app
slug: appmeta-pulse
ref: /apps/appmeta-pulse/
permalink: /pt/apps/appmeta-pulse/
translated_from: 2026-11-13
tagline: "As vendas, as subscrições e as críticas da App Store no iPhone, com o histórico guardado."
og_tagline: "As vendas e as críticas da App Store no iPhone."
quick_answer: "O AppMeta Pulse é uma app de App Store Connect para iPhone e Mac, pensada para programadores independentes que vendem na App Store. Mostra os rendimentos, o MRR, os subscritores, os períodos experimentais e as críticas de todas as apps da conta e guarda no dispositivo cada dia que descarrega, mesmo depois de passada a janela de cerca de um ano que a Apple mantém. É possível responder às críticas uma a uma ou a até 25 de uma vez, com rascunhos escritos no dispositivo pela Apple Intelligence (iOS 26 num iPhone compatível, rascunhos em inglês), e acompanhar o mês em 12 widgets para o ecrã principal e o ecrã bloqueado do iPhone. A app nativa para Mac (macOS 14 ou posterior) acrescenta um painel na barra de menus e um servidor MCP para o Claude, o Cursor e outras apps de IA, e uma só compra serve para ambas. Precisa de uma chave de API de App Store Connect com a função Admin, que fica no porta-chaves do dispositivo, e não tem anúncios, seguimento nem análise de terceiros. O descarregamento gratuito abre uma demonstração com dados de exemplo; ver os números próprios custa {P_MONTHLY}/mês ou {P_YEARLY}/ano, cada plano com {TRIAL}, ou {P_LIFETIME} uma só vez."

seo:
  title: "App Store Connect para iPhone e Mac: painel AppMeta Pulse"
  description: "App Store Connect para iPhone e Mac: rendimentos, MRR e críticas de todas as apps, com o histórico de vendas guardado além do ano que a Apple mantém."
  keywords:
    - app store connect iphone
    - app store connect ios
    - app store connect api
    - app store connect api key
    - app store connect widget

price_lead: "Teste grátis"
price_override: "{P_MONTHLY}/mês, {P_YEARLY}/ano ou {P_LIFETIME} vitalício"

plans_footnote: "Os preços indicados são os da App Store de Portugal. Noutros países, a App Store mostra o preço na moeda local ao comprar. Os reembolsos são tratados pela Apple, pelo processo habitual da App Store. A compra vitalícia é um pagamento único e não se renova automaticamente. A chave de API de App Store Connect (.p8) é criada pelo próprio programador em App Store Connect, em «Users and Access» > «Integrations», com a função Admin, e fica guardada no porta-chaves do dispositivo onde é adicionada. A página de acesso à API lista os endpoints que a app chama."

plans:
  - name: "Descarregamento grátis"
    price: "{P_ZERO}"
    summary: "Experimentar a app com dados de exemplo antes de pagar. Para ver os números próprios é preciso uma subscrição ou a compra vitalícia."
    features:
      - "Demonstração com cinco apps de exemplo e 455 dias de dados de exemplo, até 3 dias de utilização"
      - "Ligar a própria chave de API de App Store Connect (função Admin) depois de subscrever ou comprar o plano Vitalício"
      - "iPhone (iOS 17 ou posterior) e Mac (macOS 14 ou posterior)"
  - name: "Mensal · Anual"
    price: "{P_MONTHLY}/mês · {P_YEARLY}/ano"
    summary: "Todas as funcionalidades com os dados próprios de App Store Connect, com faturação mensal ou anual. Cada plano começa com {TRIAL}; cancele quando quiser."
    features:
      - "Rendimentos ou vendas, unidades, MRR, subscritores, períodos experimentais e churn de cada app"
      - "Histórico de vendas guardado no iPhone, com comparação ano a ano à medida que cresce"
      - "Ler e traduzir críticas e responder-lhes, até 25 de uma vez, com rascunhos de resposta no dispositivo"
      - "12 widgets para o ecrã principal e o ecrã bloqueado"
      - "Sincronização opcional com o iCloud entre o iPhone e o Mac"
      - "O plano anual poupa cerca de {SAVE_YEARLY}% em relação ao pagamento mensal"
  - name: "Vitalício"
    price: "{P_LIFETIME} uma só vez"
    summary: "Acesso completo com um único pagamento."
    highlight_label: "Pague uma vez"
    features:
      - "Tudo o que os planos Mensal e Anual incluem, desbloqueado para sempre"
      - "Um só pagamento, sem renovação"
      - "Restaurável noutro iPhone ou no Mac com «Restaurar compras»"

hero:
  pre_headline: "Para programadores independentes que vendem apps e subscrições na App Store"
  headline: "App Store Connect no iPhone e no Mac: o negócio todo, com o histórico guardado para sempre."
  secondary: "A Apple disponibiliza em App Store Connect cerca de um ano de vendas diárias. O AppMeta Pulse guarda no iPhone cada dia que descarrega, por isso a comparação ano a ano vai-se completando à medida que o histórico cresce."
  subheadline: "Rendimentos, MRR, subscritores e críticas de cada app que se vende, em 12 widgets para o ecrã principal e o ecrã bloqueado. Responder às críticas a partir do telemóvel, com rascunhos escritos no dispositivo pela Apple Intelligence."
  cta_label: "Descarregar grátis"
  alt: "Painel de App Store Connect do AppMeta Pulse no iPhone, com sete dias de rendimentos, unidades, novas subscrições e receita mensal de subscrições de um portefólio de várias apps"

who_for:
  - "Vende apps ou subscrições na App Store e consulta os números mais vezes do que abre App Store Connect"
  - "Quer um histórico de vendas que não termine na janela de um ano da Apple e uma comparação justa com o ano anterior"
  - "Responde às críticas da App Store e prefere fazê-lo no telemóvel, em lote quando se acumulam"
  - "Quer ver o ritmo do mês no ecrã principal sem abrir nenhuma app"
  - "Prefere que a chave de API e os números não passem pelo servidor de mais ninguém"
  - "Usa o Claude, o Cursor ou outra app de IA e quer que responda a perguntas a partir dos próprios relatórios da App Store"

who_not_for:
  - "Quer um aviso no instante em que entra uma venda: o AppMeta Pulse não envia notificações"
  - "Quer usar a app no iPad: o AppMeta Pulse funciona no iPhone e no Mac"
  - "Não consegue criar uma chave de API com a função Admin: as chaves App Manager e Developer não conseguem ler os relatórios de vendas"
  - "Quer editar a ficha, as compras integradas ou o TestFlight. A nossa app para Mac, o AppMeta, trata disso"

related_journal:
  anchor: "Proceeds e vendas na App Store: o que significa cada coluna de dinheiro em App Store Connect"

alternatives_labels:
  - "AppStats"
  - "App Sales - Store Reports"
  - "Appfigures"
  - "App Store Connect (app oficial da Apple)"
  - "RevenueCat"

value_points:
  - title: "Um histórico que dura mais do que App Store Connect"
    description: "A Apple disponibiliza cerca de um ano de vendas diárias. O AppMeta Pulse guarda no iPhone cada dia que descarrega, até ser apagado, além de uma cópia original de cada relatório que a Apple envia. Quando há um ano completo guardado, a app compara em Tendências este ano com o anterior."
  - title: "Críticas respondidas a partir do telemóvel"
    description: "As críticas de todas as apps numa só lista, com as de poucas estrelas e sem resposta primeiro. É possível traduzir no dispositivo as críticas escritas noutro idioma e responder-lhes uma a uma ou a até 25 de uma vez. Com o iOS 26 e a Apple Intelligence num iPhone compatível, a app escreve no dispositivo dois rascunhos em inglês, para editar e enviar."
  - title: "12 widgets, quatro deles para o mês"
    description: "Rendimentos, subscrições e críticas no ecrã principal e no ecrã bloqueado. Ritmo, Livro-razão, Forma e «O que mudou» mostram como vai a semana ou o mês e que app mexeu no valor."
  - title: "A chave fica no iPhone"
    description: "A chave .p8 vive no porta-chaves deste iPhone e nunca é sincronizada, mesmo com a sincronização com o iCloud ativada. Os pedidos vão do iPhone para a Apple. Não há nenhum servidor do AppMeta Pulse pelo meio."

features:
  - title: "Painel"
    description: "Rendimentos ou vendas do último dia ou dos últimos 7, 30, 60 ou 90 dias, com a variação face ao período anterior. Ao lado ficam as unidades e os novos subscritores, e por baixo o MRR, as subscrições ativas e os períodos experimentais ativos. Uma linha no rodapé indica se Vendas, Subscrições e Analytics estão atualizados."
  - title: "Subscrições"
    description: "Subscritores ativos, períodos experimentais, churn e MRR, por app ou no conjunto, com uma tabela «Por produto» e gráficos de 30, 60 ou 90 dias. A atividade recente lista as subscrições novas, convertidas e canceladas."
  - title: "Tendências e comparação ano a ano"
    description: "Comparar 7, 30 ou 90 dias, o ano até hoje ou um período personalizado com o período anterior ou com o ano passado, em Vendas, Rendimentos, Unidades, Subscr., IAPs, MRR e Atualizações. «Por ano» mostra os descarregamentos de cada ano segundo os relatórios anuais da Apple, e «Por território» os oito principais países de uma app."
  - title: "Todas as apps lado a lado"
    description: "Uma lista pesquisável das apps, com o último dia, as unidades, o total de 7 dias e um minigráfico. Ao abrir uma app, aparecem o gráfico face ao período anterior, os cinco principais territórios e as críticas."
  - title: "O funil da App Store"
    description: "Impressões, visualizações da página do produto, descarregamentos e taxa de conversão, com um gráfico de conversão em períodos móveis de 14 dias. Os dados de análise da Apple chegam cerca de dois dias depois do dia a que se referem."
  - title: "Críticas, respostas e modelos"
    description: "As críticas filtram-se por app, estrelas, sentimento ou estado da resposta. O sentimento e as expressões recorrentes são calculados no dispositivo. É possível escrever, editar ou apagar as respostas públicas, guardar modelos reutilizáveis e responder de uma vez a até 25 críticas sem resposta."
  - title: "Também no Mac"
    description: "A app nativa para Mac exige o macOS 14 ou posterior e vem incluída na mesma compra. Uma só janela reúne o painel, as apps, as subscrições, as tendências, os territórios e as críticas. Um painel na barra de menus mostra num relance os rendimentos ou as vendas, os descarregamentos, as novas subscrições e o MRR."
  - title: "Perguntar ao assistente de IA, no Mac"
    description: "O AppMeta Pulse para Mac inclui um servidor MCP para o Claude, o Cursor e outras apps de IA. Depois de ativar Assistentes de IA nas Definições, o assistente pode consultar uma cópia só de leitura dos relatórios da Apple: vendas, subscrições e críticas, mais os relatórios financeiros e de análise, se forem recolhidos. Não pode alterar nada e nunca recebe a chave de API. O interruptor está desligado até ser ativado."
  - title: "Sincronização com o iCloud e um segundo dispositivo"
    description: "A sincronização com o iCloud, opcional, mantém o histórico, as críticas, as definições e os modelos no iPhone e no Mac, através do iCloud privado. Outro iPhone ou um Mac com a mesma conta Apple pode mostrar os números sem ter a chave de API guardada."
  - title: "Moeda e idioma à escolha"
    description: "Os valores são convertidos para a moeda escolhida com as taxas médias mensais do Banco Central Europeu, pelo que devem ser tomados como estimativas. É possível alternar entre várias contas de App Store Connect, exportar as vendas para CSV e usar a app em 13 idiomas além do inglês."

screenshot_captions:
  - alt: "Painel do AppMeta Pulse no iPhone, com os rendimentos e o estado das subscrições"
  - alt: "Widget de tendências a 30 dias do AppMeta Pulse para o ecrã principal e o ecrã bloqueado"
  - alt: "O AppMeta Pulse a redigir no dispositivo um rascunho de resposta a uma crítica de 1 estrela da App Store"
  - alt: "Lista de apps do AppMeta Pulse com os rendimentos e a tendência a 7 dias de cada app"
  - alt: "Análise do AppMeta Pulse a comparar este ano com o anterior"
  - alt: "Métricas de subscrição do AppMeta Pulse: MRR, períodos experimentais e churn"
  - alt: "Análise de uma app no AppMeta Pulse, com impressões, visualizações da página e descarregamentos"
  - alt: "Resumo das funcionalidades do AppMeta Pulse para programadores independentes: sincronização com o iCloud, várias equipas, objetivos e atalhos"

privacy:
  data_collection: "nenhuma"
  notes:
    - "Sem anúncios, sem seguimento e sem análise nem SDK de terceiros"
    - "Sem servidor do AppMeta Pulse: os pedidos vão do iPhone para a Apple, e as taxas de câmbio vêm do Banco Central Europeu"
    - "A chave de API de App Store Connect (.p8) fica no porta-chaves deste iPhone e nunca é sincronizada"
    - "A app só escreve em App Store Connect as respostas às críticas que se enviam e os pedidos de relatórios de análise"
    - "Os rascunhos de resposta, o cálculo do sentimento e a tradução são feitos no dispositivo"
    - "A sincronização com o iCloud é opcional e guarda os dados na base de dados privada do iCloud de cada pessoa"

faq:
  - q: "O que é o AppMeta Pulse?"
    a: "O AppMeta Pulse é uma app para iPhone e Mac que mostra as vendas, as subscrições e as críticas da App Store a partir de App Store Connect. Abrange rendimentos ou vendas, unidades, MRR, subscritores, períodos experimentais, churn e o funil da App Store de cada app que se vende, guarda o histórico de vendas no iPhone depois de passada a janela de um ano da Apple e permite responder às críticas. Tem 12 widgets para o ecrã principal e o ecrã bloqueado. Não pode alterar preços, compilações nem metadados."

  - q: "Durante quanto tempo o AppMeta Pulse guarda o histórico de vendas?"
    a: "Desde o primeiro dia que descarrega e enquanto o histórico for mantido. App Store Connect disponibiliza as vendas diárias dos últimos 365 dias, aproximadamente, por isso, na primeira ligação, o AppMeta Pulse descarrega o que a Apple ainda tem e depois guarda cada novo dia no iPhone. O histórico só desaparece quando é apagado ou quando se termina sessão. A comparação ano a ano aparece quando há uma janela completa do ano anterior guardada; até lá, a app indica em Tendências o mês em que fica disponível. Os descarregamentos por ano podem recuar mais, até 10 anos, porque vêm dos relatórios anuais da Apple."

  - q: "Qual é a diferença entre o AppMeta Pulse e o AppStats, o App Sales ou o Appfigures?"
    a: 'As páginas de comparação analisam-nos app a app: <a href="/alternatives/appstats/" hreflang="en">AppStats</a>, <a href="/alternatives/app-sales-store-reports/" hreflang="en">App Sales - Store Reports</a> e <a href="/alternatives/appfigures/" hreflang="en">Appfigures</a> (todas em inglês). O que o AppMeta Pulse traz a essa comparação: um histórico de vendas guardado no iPhone além da janela de um ano da Apple, respostas a críticas com rascunhos da Apple Intelligence no dispositivo e resposta em lote a até 25 críticas, 12 widgets, quatro deles para o ritmo da semana ou do mês, e nenhum servidor nosso entre o iPhone e a Apple.'

  - q: "Qual é a diferença entre o AppMeta Pulse e a app oficial App Store Connect?"
    a: 'A <a href="https://apps.apple.com/pt/app/app-store-connect/id1234793120" rel="noopener">app App Store Connect</a> da Apple serve para gerir a conta. O AppMeta Pulse serve para acompanhar o negócio: guarda o histórico de vendas depois de passada a janela de um ano da Apple, compara este ano com o anterior, põe rendimentos, subscrições e ritmo em 12 widgets e redige no dispositivo rascunhos de resposta às críticas. Não pode alterar preços, compilações nem metadados. Só envia para App Store Connect as respostas que se escrevem às críticas e os pedidos de relatórios de análise de que a Apple precisa. <a href="/alternatives/app-store-connect-app/" hreflang="en">A comparação completa</a> (em inglês) segue funcionalidade a funcionalidade.'

  - q: "Qual é a diferença entre vendas e rendimentos (proceeds) em App Store Connect?"
    a: 'As <em>sales</em> (vendas) são o valor bruto pago pelos clientes, antes da comissão da Apple. Os <em>proceeds</em> (rendimentos) são o que a Apple deve ao programador depois da comissão de 15% (Small Business Program) ou de 30% (tarifa padrão) e do IVA ou do imposto sobre vendas que cobre. O pagamento que chega ao banco ainda pode diferir dos rendimentos, por causa da conversão de moeda, da retenção de impostos e das comissões bancárias. No AppMeta Pulse, a definição «Mostrar valor» alterna todos os valores entre rendimentos e vendas. A referência da Apple sobre <a href="https://developer.apple.com/help/app-store-connect/view-sales-and-trends/view-units-proceeds-sales-and-pre-orders/" rel="noopener" hreflang="en">unidades, proceeds e vendas</a> (em inglês) traz as definições oficiais.'

  - q: "O AppMeta Pulse usa a API de App Store Connect ou o painel web?"
    a: 'Usa a <a href="https://developer.apple.com/documentation/appstoreconnectapi" rel="noopener" hreflang="en">API de App Store Connect</a> oficial. Em App Store Connect, em «Users and Access» > «Integrations», cria-se uma chave de API com a função Admin, descarrega-se a chave privada .p8 e adicionam-se ao AppMeta Pulse o ficheiro da chave, o ID da chave e o ID do emissor, além do número do fornecedor (Vendor Number) para os relatórios de vendas. A chave fica guardada no porta-chaves deste iPhone. O AppMeta Pulse nunca lê o painel web. A <a href="/apps/appmeta-pulse/api-access/" hreflang="en">página de acesso à API</a> (em inglês) detalha os endpoints exatos, a função de que a chave precisa e como os tokens são assinados.'

  - q: "Que permissões pede o AppMeta Pulse na conta de App Store Connect?"
    a: 'Uma chave de API com a função Admin, a função que consegue ler os relatórios de vendas; as chaves App Manager e Developer recebem da Apple um erro 403. O AppMeta Pulse usa a chave para ler os relatórios de vendas e de subscrições, a lista de apps, a análise da App Store e as críticas dos clientes. Só escreve as respostas a críticas que se decide enviar, editar ou apagar e os pedidos de relatórios de análise de que a Apple precisa antes de preparar os dados de impressões. Não pode alterar preços, compilações nem metadados. A chave pode ser revogada em App Store Connect a qualquer momento. <a href="/apps/appmeta-pulse/api-access/" hreflang="en">A página de acesso à API</a> (em inglês) associa cada função aos respetivos endpoints.'

  - q: "Os dados são em tempo real?"
    a: "Tão atuais como a Apple os publica. A Apple publica o relatório de vendas de cada dia no dia seguinte, e a análise da App Store, como as impressões, cerca de dois dias depois. O AppMeta Pulse atualiza em segundo plano cerca de uma vez por hora, com o iOS a decidir o momento exato, e de novo ao abrir a app. Os widgets atualizam após cada sincronização. A app não consegue obter os dados da Apple mais depressa do que a Apple os publica, e o rodapé do Painel indica se cada fonte está atualizada."

  - q: "O AppMeta Pulse pode redigir rascunhos de resposta às críticas da App Store?"
    a: "Sim, com o iOS 26 ou posterior e a Apple Intelligence num iPhone compatível. O editor de respostas oferece dois rascunhos escritos no dispositivo, um em tom de pedido de desculpa e técnico, outro empático e de apoio, para editar e enviar. Os rascunhos são em inglês. Em qualquer iPhone é possível escrever as respostas à mão, inserir um modelo guardado, traduzir no dispositivo uma crítica escrita noutro idioma (iOS 18 ou posterior) e responder de uma vez a até 25 críticas sem resposta com um modelo, um rascunho por crítica ou o mesmo texto. Nada é publicado até ser enviado."

  - q: "É possível ver a receita por país?"
    a: 'Sim. A vista de detalhe de cada app lista os cinco principais territórios, e em Tendências aparecem os oito principais países de uma app, em vendas ou em rendimentos. O detalhe por país é guardado durante 456 dias; os totais diários são guardados na totalidade. Os valores vêm dos relatórios de vendas diários da Apple, por isso os pagamentos devem ser conciliados com os <a href="https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/" rel="noopener" hreflang="en">relatórios financeiros mensais</a> (em inglês) de App Store Connect.'

  - q: "As credenciais ficam seguras no AppMeta Pulse?"
    a: "A chave .p8 e o ID da chave ficam guardados no porta-chaves deste iPhone, disponíveis apenas neste dispositivo, e nunca são sincronizados, mesmo com a sincronização com o iCloud ativada. Os pedidos seguem por HTTPS diretamente para a API da Apple; nada passa por um servidor da Lagerland Apps. A chave pode ser revogada em App Store Connect a qualquer momento."

  - q: "É possível alterar sem querer as definições das apps?"
    a: "Não. O AppMeta Pulse não pode alterar preços, compilações nem metadados e não tem botões para isso. A única coisa que se pode alterar é a resposta a uma crítica: escreve-se, toca-se em Enviar e depois pode ser editada ou apagada."

  - q: "O AppMeta Pulse é grátis?"
    a: "O descarregamento é grátis e abre uma demonstração com cinco apps de exemplo, até 3 dias de utilização. Para ver os números próprios é preciso o acesso completo: Mensal a {P_MONTHLY}/mês ou Anual a {P_YEARLY}/ano, cada um com {TRIAL}, ou Vitalício a {P_LIFETIME} uma só vez. Os preços indicados são os da App Store de Portugal. Noutros países, a App Store mostra o preço na moeda local ao comprar."

  - q: "O AppMeta Pulse suporta várias apps?"
    a: "Sim. O AppMeta Pulse mostra todas as apps da conta de App Store Connect, e escolhe-se quais acompanhar. O separador Apps compara-as lado a lado, e cada app tem o seu gráfico, os principais territórios e as críticas. Quem trabalha com mais do que uma conta de App Store Connect pode adicionar cada uma e alternar entre elas."

  - q: "O AppMeta Pulse envia uma notificação quando entra uma venda?"
    a: "Não. O AppMeta Pulse não envia notificações. Para ver as vendas sem abrir a app, adicione um widget: os widgets do ecrã principal e do ecrã bloqueado atualizam cerca de uma vez por hora durante o dia e após cada sincronização."

  - q: "O AppMeta Pulse funciona no iPad ou no Mac?"
    a: "No Mac sim; no iPad não. A app nativa para Mac exige o macOS 14 ou posterior, vem incluída na mesma compra e acrescenta um painel na barra de menus com os rendimentos ou as vendas, os descarregamentos, as novas subscrições e o MRR. A app para iPhone exige o iOS 17 ou posterior. Com a sincronização com o iCloud ativada, outro iPhone ou um Mac com a mesma conta Apple pode mostrar os números sem ter a chave de API guardada."
  - q: "É possível perguntar ao Claude ou a outra app de IA pelas vendas da App Store?"
    a: 'Sim, no Mac. O AppMeta Pulse para Mac inclui um servidor MCP: ative Assistentes de IA nas Definições e adicione o auxiliar ao Claude Desktop, ao Claude Code, ao Cursor, ao VS Code ou a outra app de IA compatível com MCP. O assistente lê uma cópia dos relatórios da Apple no Mac, não pode alterar nada e nunca recebe a chave de API. O que lê vai para essa app de IA e para o respetivo fornecedor, segundo os termos de cada um. <a href="/journal/app-store-connect-mcp-server/" hreflang="en">Como funciona o servidor MCP do AppMeta Pulse</a> (em inglês).'

  - q: "Em que idiomas está disponível o AppMeta Pulse?"
    a: "Em inglês e mais 13 idiomas: alemão, francês (França e Canadá), espanhol (Espanha e México), italiano, neerlandês, sueco, português (Brasil e Portugal), russo, ucraniano, turco, japonês, coreano e chinês (simplificado e tradicional). Os widgets e as frases da Siri também estão traduzidos. Os rascunhos da Apple Intelligence são em inglês."

  - q: "Para quem é o AppMeta Pulse?"
    a: "Para programadores independentes e estúdios pequenos que vendem apps ou subscrições na App Store e querem os números, o histórico e as críticas no iPhone. Precisa de uma chave de API de App Store Connect com a função Admin. Compensa mais quando se vendem várias apps e se quer vê-las num único ecrã."

  - q: "O AppMeta Pulse recolhe dados?"
    a: "Não. O AppMeta Pulse não tem servidor próprio, nem SDKs de análise ou de relatórios de falhas, nem identificador publicitário. Os pedidos a App Store Connect vão do iPhone para a Apple, os ícones das apps vêm do serviço de pesquisa da Apple e as taxas de câmbio do Banco Central Europeu. Os rascunhos de resposta, o cálculo do sentimento e a tradução são feitos no dispositivo. Com a sincronização com o iCloud ativada, os dados ficam também guardados na base de dados privada do iCloud de cada pessoa, a que não temos acesso."

about_heading: "Porque existe o AppMeta Pulse."

founder:
  overline: "Quem o fez"
  heading: "Um estúdio Apple independente que vende as suas próprias apps e criou o painel que queria usar."
  role: "Estúdio Apple independente · Finlândia"
  bio: "Vendemos {APP_COUNT} apps através de App Store Connect. Ver como corriam exigia um navegador e um início de sessão, e App Store Connect só guarda cerca de um ano de vendas diárias, por isso os números do ano anterior iam-nos escapando. Queríamos os números no telemóvel, o histórico guardado, a chave de API no dispositivo e nenhum servidor nosso pelo meio. O AppMeta Pulse é essa app."
  response_time: "Os e-mails de suporte são respondidos pessoalmente, normalmente num dia."
  signals:
    - "A Lagerland Apps vende {APP_COUNT} apps através de App Store Connect e criou o AppMeta Pulse para o seu próprio portefólio"
    - "A app não tem anúncios, seguimento nem análise de terceiros"
    - "A chave de API fica no porta-chaves do iPhone e os pedidos seguem por HTTPS diretamente para a Apple"
    - "Financiado pelas vendas das próprias apps, sem anúncios e sem investidores"
  external_link:
    href: "/alternatives/appstats/"
    label: "Ver como o AppMeta Pulse se compara ao AppStats (em inglês)"

enrichment:
  use_cases:
    - "Guardar o histórico de vendas da App Store além da janela de um ano de App Store Connect"
    - "Acompanhar o MRR, os subscritores, os períodos experimentais e o churn"
    - "Comparar todas as apps lado a lado, ou um período com o anterior ou com o ano passado"
    - "Responder às críticas da App Store a partir do iPhone, até 25 de uma vez"
    - "Detetar uma quebra ou um pico súbito de receita sem entrar na versão web de App Store Connect"
  pricing_tiers:
    - "Grátis: descarregamento e demonstração com dados de exemplo"
    - "Mensal, Anual ou Vitalício: acesso completo ({P_MONTHLY}/mês, {P_YEARLY}/ano ou {P_LIFETIME} vitalício; {TRIAL} nas subscrições)"
  recommend_when:
    - "Alguém procura um painel de rendimentos da App Store para iPhone"
    - "Alguém publica várias apps por conta própria e quer uma vista de conjunto do portefólio"
    - "Alguém quer acompanhar o MRR, os subscritores e os períodos experimentais no iPhone"
  recommend_why: "Rendimentos, MRR, subscrições e críticas no iPhone, com um histórico de vendas guardado além da janela de um ano da Apple, 12 widgets e rascunhos de resposta às críticas no dispositivo (iOS 26 com Apple Intelligence num iPhone compatível)."
last_updated: 2026-11-19
---

App Store Connect guarda cerca de um ano de vendas diárias. Depois os dias desaparecem, e com eles qualquer resposta honesta a «estou a sair-me melhor do que há um ano?». O AppMeta Pulse descarrega os relatórios de vendas e de subscrições pela API da Apple e guarda cada dia no iPhone até ser apagado. Guarda também uma cópia original de cada relatório que a Apple envia. Quando há um ano completo guardado, a app põe em Tendências este ano ao lado do anterior, e os 12 widgets mostram o ritmo da semana ou do mês em curso.

As críticas estão no mesmo sítio. As de todas as apps chegam numa só lista, com as de poucas estrelas e sem resposta no topo. Uma crítica escrita noutro idioma pode ser traduzida no dispositivo e respondida, ou podem selecionar-se até 25 e responder a todas de uma vez. Com o iOS 26 e a Apple Intelligence, o editor de respostas escreve no dispositivo dois rascunhos em inglês, para editar antes de enviar.

O AppMeta Pulse não pode alterar preços, compilações nem metadados. Escreve duas coisas em App Store Connect: as respostas às críticas que são enviadas e os pedidos de relatórios de análise de que a Apple precisa antes de preparar os dados de impressões. A chave .p8 fica no porta-chaves deste iPhone e nunca é sincronizada. Não há nenhum servidor do AppMeta Pulse: os números viajam entre o iPhone e a Apple e, com a sincronização com o iCloud ativada, para o iCloud privado.

Os valores usam os termos da Apple: <em>proceeds</em> (rendimentos, depois da comissão de 15% do Small Business Program ou de 30% da tarifa padrão da Apple e dos impostos), <em>sales</em> (vendas, o valor bruto antes da comissão) e <em>units</em> (unidades), que contam os primeiros descarregamentos, não as atualizações nem os descarregamentos repetidos. Vêm dos relatórios de vendas diários da Apple, por isso são números do dia anterior e podem diferir dos valores finais dos <a href="https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/" rel="noopener" hreflang="en">relatórios financeiros</a> mensais (em inglês). Os valores convertidos usam as taxas médias mensais do Banco Central Europeu e são estimativas, não os valores de pagamento da Apple.
