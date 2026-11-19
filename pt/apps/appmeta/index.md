---
layout: app
slug: appmeta
ref: /apps/appmeta/
permalink: /pt/apps/appmeta/
translated_from: 2026-11-08
tagline: "Edite, compare e envie a ficha da app na App Store a partir do Mac."
og_tagline: "A ficha da app na App Store, a partir do Mac."
quick_answer: "O AppMeta é uma app de App Store Connect para Mac, feita para programadores independentes que gerem as suas próprias fichas. Reúne todos os idiomas numa só janela, mostra campo a campo o que muda em relação à ficha publicada antes de cada envio e mede a dificuldade e a procura das palavras-chave na App Store real, com as evidências à vista. Compras integradas, subscrições, TestFlight, Game Center, críticas e envio para análise ficam na mesma app, que fala diretamente com a Apple e guarda a chave de API no porta-chaves do Mac. A app descarrega-se grátis e funciona em modo de demonstração com dados de exemplo; ligar a conta própria exige o Pro, por {P_YEARLY}/ano ou {P_LIFETIME} uma vez. Requer macOS 14 ou posterior."

price_override: "{P_YEARLY}/ano ou {P_LIFETIME} vitalício"

plans_footnote: "Os preços indicados são os da App Store de Portugal. Noutros países, a App Store mostra o preço na moeda local ao comprar. A descarga grátis funciona em modo de demonstração com dados de exemplo; ligar a conta própria do App Store Connect exige o Pro. A subscrição anual começa com {TRIAL} para quem subscreve pela primeira vez. A Apple trata dos reembolsos pelo processo habitual de reembolso da App Store. A opção vitalícia é uma compra única e não se renova."

plans:
  - name: "Anual"
    price: "{P_YEARLY}/ano"
    summary: "Todo o AppMeta Pro, com cobrança uma vez por ano após {TRIAL}. Cancele quando quiser."
    features:
      - "Todos os idiomas num só editor, ou um campo em todos os idiomas"
      - "Um diff campo a campo com o App Store Connect antes de cada envio da ficha"
      - "Estado das palavras-chave: caracteres desperdiçados, duplicados e sobreposições"
      - "Dificuldade e procura de palavras-chave em direto, com as evidências à vista (desligadas até serem ligadas)"
      - "Tradução com IA através do Apple Intelligence no Mac, com chave própria ou com um modelo local"
      - "Compras integradas, subscrições, Game Center, TestFlight e envio para análise"
      - "Críticas, Vendas e Análises, e Diagnósticos"
  - name: "Vitalício"
    price: "{P_LIFETIME} uma vez"
    summary: "Todo o AppMeta Pro, pago uma só vez."
    features:
      - "Tudo o que inclui o plano Anual"
      - "Compra única, sem renovação"
      - "Restaure a compra nas Definições"
    highlight_label: "Pagamento único"

alternatives_labels:
  - "Itsyconnect"
  - "Interface web do App Store Connect"
  - "Fastlane deliver"
  - "AppMetaHub"
  - "ASO.dev"
  - "Helm for App Store Connect"

seo:
  title: "App Store Connect para Mac: AppMeta, metadados e ASO"
  description: "App Store Connect para Mac: o AppMeta edita todos os idiomas, mostra o diff antes de enviar e mede a dificuldade das palavras-chave."
  keywords:
    - app store connect mac app
    - app store connect macos
    - app store connect mac download
    - aso app store optimization
    - aso app store keywords
    - aso app store optimization tools
    - app store connect api key

hero:
  pre_headline: "Para programadores Apple independentes que gerem as suas próprias fichas no App Store Connect"
  headline: "Edite todos os idiomas no Mac. Veja o diff antes de enviar."
  secondary: "O AppMeta é uma app nativa de App Store Connect para Mac. A chave de API fica no porta-chaves do Mac e a app comunica diretamente com o App Store Connect, sem qualquer servidor AppMeta pelo meio."
  subheadline: "Edite o nome, o subtítulo, as palavras-chave e a descrição de todos os idiomas numa só janela, ou um mesmo campo em todos de uma vez. Antes de enviar, cada alteração aparece ao lado do valor atual no App Store Connect, e só saem os campos alterados. A dificuldade e a procura das palavras-chave vêm da App Store real, com as evidências listadas. Experimente todos os ecrãs grátis no modo de demonstração e depois ligue a conta com o Pro, a {P_YEARLY}/ano ou {P_LIFETIME} uma vez."
  cta_label: "Descarregar grátis"
  alt: "AppMeta no macOS com o campo Novidades de todos os idiomas numa só vista e as versões da app como separadores"

who_for:
  - "Gere as próprias fichas do App Store Connect em vários idiomas e se vê obrigado, na interface web, a editá-las um idioma de cada vez"
  - "Quer ver exatamente o que um envio vai alterar antes de chegar à loja"
  - "Trabalha as palavras-chave e quer as evidências por trás de uma pontuação de dificuldade, não um número solto"
  - "Trata também de compras integradas, subscrições, TestFlight, Game Center e respostas a críticas, e quer tudo numa só app para Mac"
  - "Quer a chave de API no porta-chaves do Mac e os pedidos ao App Store Connect a ir diretamente para a Apple"
  - "Prefere pagar {P_LIFETIME} uma vez a manter uma subscrição mensal de ferramentas para o App Store Connect"

who_not_for:
  - "Não tem conta do App Store Connect. Sem ela, a app só corre o modo de demonstração com dados de exemplo"
  - "Tem o processo de lançamento totalmente automatizado com Fastlane ou integração contínua e nunca edita metadados à mão"
  - "Precisa de acompanhar a posição das palavras-chave ao longo do tempo e de pesquisar as palavras-chave da concorrência, que é o que fazem o Appfigures, o AppTweak e o Sensor Tower"
  - "Precisa de licenças para equipas, ou de uma ferramenta que corra num navegador, no iPhone ou no Windows; o AppMetaHub (web) ou o ASO.dev (licenças por utilizador, mais plataformas) servem melhor"

related_journal:
  anchor: "Como funciona o campo de palavras-chave da App Store: 100 caracteres, vírgulas e as palavras que a Apple já indexa"

founder:
  role: "Programador Apple independente · Finlândia · estúdio de uma só pessoa desde 2025"
  location: "Finlândia"
  overline: "Porque criámos esta app"
  heading: "Publicamos {APP_COUNT} apps. O AppMeta é a ferramenta que criámos para gerir as fichas."
  story: "A interface web do App Store Connect serve para uma app num só idioma. Com muitas apps e dezenas de idiomas, acaba-se a editar um idioma de cada vez, sem uma ideia clara do que cada alteração guardada vai substituir. O Fastlane deliver é bom em integração contínua e incómodo para edições à mão. Por isso criámos uma app para Mac que junta todos os idiomas numa só janela, mostra o valor publicado ao lado de cada alteração antes de um envio e mede as palavras-chave na App Store real, com as evidências listadas. Corre no Mac e fala diretamente com a Apple, por isso não há nenhum servidor AppMeta a guardar a chave ou as fichas."
  signals:
    - "Criada sobre a API do App Store Connect com uma chave de equipa; o ficheiro .p8, o Issuer ID e o Key ID ficam no porta-chaves do Mac"
    - "Sem servidor AppMeta e sem SDK de análise nem de publicidade"
    - "A própria app está disponível em 17 localizações"
    - "Requer macOS 14 Sonoma ou posterior"
  external_link:
    label: "Ver todas as apps da Lagerland Apps →"
    href: "/pt/apps/"
  response_time: "Os emails de suporte chegam a uma única caixa e são respondidos pessoalmente, normalmente no espaço de um dia."

value_points:
  - title: "Veja o diff antes de enviar"
    description: "Cada campo alterado fica ao lado do valor atual no App Store Connect, com as etiquetas App Store Connect e «As suas alterações». Envia-se um campo, um idioma ou todos numa única ação confirmada. Os campos que mudaram no App Store Connect desde a última atualização aparecem assinalados, e «Descartar todas as alterações locais» repõe a ficha publicada em todos os idiomas com um só comando."
  - title: "Pesquisa de palavras-chave que mostra o cálculo"
    description: "A dificuldade é uma pontuação de 0 a 100 calculada com as dez apps com que se competiria pela posição, e «Mostrar o cálculo» lista cada app e cada número por trás dela. A procura vem das sugestões de pesquisa da própria Apple. Quando a Apple não devolve nada, a app indica-o em vez de mostrar um zero. A pesquisa em direto fica desligada até ser ligada."
  - title: "Corre no Mac e fala diretamente com a Apple"
    description: "Não há nenhum servidor AppMeta. A chave .p8, o Issuer ID e o Key ID ficam no porta-chaves desse Mac e só nele, e os pedidos vão diretamente para o App Store Connect. Um fornecedor de IA só vê o texto se for adicionada uma chave própria e esta for usada."
  - title: "Uma só app para todo o lançamento"
    description: "A ficha, as compras integradas e subscrições, o TestFlight, o Game Center, as verificações do envio para análise, as críticas e as vendas ficam numa única janela de três colunas, com atalhos de teclado para atualizar, pré-visualizar e enviar."

how_it_works:
  intro: "O AppMeta é um cliente nativo para Mac da API do App Store Connect. Assina os pedidos no Mac com a chave própria, guarda as alterações numa cópia local e compara-as com a ficha publicada antes de enviar seja o que for. Um lançamento passa por estes passos."
  steps:
    - title: "Ligue com a chave de API do App Store Connect"
      detail: "Crie uma chave de API de equipa no App Store Connect, em «Users and Access», e introduza o Issuer ID, o Key ID e o ficheiro .p8 no AppMeta. «Validar ligação» testa a chave antes de ser guardada. Os três ficam no porta-chaves do Mac como itens exclusivos desse Mac, nunca sincronizados com o iCloud. O AppMeta assina tokens de curta duração com a chave no Mac, e o ficheiro .p8 nunca sai dele. É possível juntar várias contas e alternar entre elas na barra lateral."
    - title: "Descarregue a ficha"
      detail: "«Atualizar» (⌘R) descarrega os metadados atuais de todos os idiomas da versão selecionada. As alterações ficam guardadas no Mac, por isso sobrevivem a um reinício e só chegam ao App Store Connect quando são enviadas. As apps com versões de iOS e de macOS têm uma linha por plataforma, cada uma com as suas alterações."
    - title: "Edite por idioma, ou um campo em todos os idiomas"
      detail: "O separador «Idiomas» edita, para cada idioma, o nome, o subtítulo, a descrição, as palavras-chave, o texto promocional, as Novidades e os URL de marketing, de suporte e da política de privacidade. O separador «Campos» inverte a lógica: escolhe-se um campo e edita-se em todos os idiomas ao mesmo tempo. A contagem de caracteres segue a do App Store Connect, por isso um campo de palavras-chave em hindi que uma contagem simples dá como 66/100 aparece como 99/100, tal como a Apple conta."
    - title: "Arrume as palavras-chave"
      detail: "O separador «Palavras-chave» mostra o campo de cada idioma em relação ao limite de 100 caracteres, com um «Resumo de saúde»: «Problemas», «Caracteres desperdiçados», «Tokens únicos» e «Eficiência». Assinala as palavras repetidas no nome, no subtítulo e nas palavras-chave, e entre idiomas. «Remover duplicados» e «Corrigir sobreposições» tratam disso. A «Cobertura de lojas» mostra quais das 57 lojas os idiomas alcançam, e a «Cobertura de pesquisa na App Store» estima a quantas pesquisas os metadados podem corresponder."
    - title: "Meça a dificuldade e a procura (opcional)"
      detail: "Ative a dificuldade em direto nas Definições e o AppMeta mede cada expressão na App Store. A dificuldade é uma pontuação de 0 a 100 calculada com as dez primeiras apps da expressão, com as evidências listadas. A procura indica se as sugestões de pesquisa da Apple devolvem a expressão e em que posição. A «Oportunidade» combina as duas e ordena a lista. «Medir combinações» testa todas as expressões que o nome, o subtítulo e as palavras-chave podem formar, mostra primeiro o plano e para assim que se pedir. Ligue uma conta Apple Ads se quiser também as pontuações de popularidade da Apple."
    - title: "Traduza e obtenha ideias de palavras-chave (opcional)"
      detail: "«Traduzir com IA» prepara rascunhos em até 20 idiomas de destino a partir de um idioma de origem, num só lote, mantendo o nome da marca e o limite de cada campo. No separador «Palavras-chave», a IA pode sugerir palavras-chave e substituir as redundantes. O fornecedor escolhe-se nas Definições: Apple Intelligence no Mac (macOS 26, num Mac compatível, sem chave), Anthropic, OpenAI ou Google com chave própria, ou um servidor local compatível com OpenAI, como o Ollama ou o LM Studio."
    - title: "Pré-visualize e envie"
      detail: "«Pré-visualizar» (⌘⇧D) lista cada campo alterado, com o App Store Connect de um lado e «As suas alterações» do outro. Envia-se um campo, um idioma (⌘↩) ou tudo (⌘⇧↩), e este último pede que se confirme quantos campos vai substituir. Os valores inválidos são bloqueados antes de saírem do Mac."
    - title: "Conclua o lançamento na mesma app"
      detail: "Associe uma compilação, adicione a versão para análise e gira o lançamento em fases da versão de iOS. O separador «Envio para análise» percorre as informações de análise da app, os direitos de conteúdo, as categorias, os preços, a disponibilidade, a classificação etária, o contrato de licença, a privacidade e os direitos de autor; a privacidade é um resumo só de leitura, com uma ligação ao App Store Connect. TestFlight, compras integradas, Game Center, críticas, vendas e diagnósticos têm cada um o seu separador."

features:
  - title: "Todos os idiomas numa só janela"
    description: "Edite, para cada idioma, o nome, o subtítulo, a descrição, as palavras-chave, o texto promocional, as Novidades e três URL, com um estado em cada campo (Modificado, Conflito, Sincronizado, Erro, Bloqueado) e uma contagem de caracteres em direto em relação ao limite da Apple. Ou abra o separador «Campos» e percorra um campo em todos os idiomas. A app gere os 50 códigos de idioma do App Store Connect, ordenados como o App Store Connect os ordena ou pela ordem que se preferir."
  - title: "Um diff campo a campo antes de cada envio da ficha"
    description: "A pré-visualização mostra as alterações ao lado do que está publicado no App Store Connect, campo a campo. Só os campos alterados são enviados: um campo, um idioma ou todos, depois de uma confirmação. Se um idioma mudou no App Store Connect desde a última atualização, um aviso indica-o, e «Aceitar remoto» adota a versão publicada."
  - title: "Dificuldade e procura de palavras-chave, com as evidências"
    description: "A dificuldade é uma pontuação de 0 a 100 calculada com as dez primeiras apps de uma expressão, a partir das classificações e dos metadados dessas apps, e «Mostrar o cálculo» lista todas as apps da amostra e todos os números usados. A procura indica se as sugestões de pesquisa da Apple devolvem a expressão e em que posição. Cada leitura indica a loja e há quanto tempo foi feita, e os resultados ficam em cache no Mac durante 7 dias. São estimativas a partir dos resultados e das sugestões públicas de pesquisa da Apple, não o volume de pesquisa oficial. A pesquisa em direto está desligada até ser ligada nas Definições."
  - title: "Verificações do estado das palavras-chave em cada idioma"
    description: "O «Resumo de saúde» conta os «Problemas», os «Caracteres desperdiçados», os «Tokens únicos» e a «Eficiência» de cada campo de palavras-chave. A app assinala as palavras repetidas no nome, no subtítulo e nas palavras-chave, e entre idiomas, e «Remover duplicados» e «Corrigir sobreposições» tratam disso. A «Cobertura de lojas» associa os idiomas a 57 lojas, o «Painel de eficiência de palavras-chave» compara idiomas e exporta para JSON ou CSV, e nada disto precisa de IA."
  - title: "Tradução com IA no Mac, ou com chave própria"
    description: "«Traduzir com IA» prepara rascunhos de vários idiomas a partir de um só, até 20 por lote, mantendo o nome da marca e o limite de cada campo. Com o <a href=\"https://www.apple.com/pt/apple-intelligence/\" rel=\"noopener\" target=\"_blank\">Apple Intelligence</a> selecionado (macOS 26, num Mac compatível), o texto fica no Mac e não é preciso chave. Para um modelo na nuvem, adicione uma chave própria do <a href=\"https://www.anthropic.com/claude\" rel=\"noopener\" target=\"_blank\">Anthropic Claude</a>, da <a href=\"https://platform.openai.com/\" rel=\"noopener\" target=\"_blank\">OpenAI</a> ou do <a href=\"https://ai.google.dev/\" rel=\"noopener\" target=\"_blank\">Google Gemini</a>, ou aponte para um servidor local como o <a href=\"https://ollama.com/\" rel=\"noopener\" target=\"_blank\">Ollama</a> ou o LM Studio. O pagamento é feito diretamente ao fornecedor; o AppMeta não vende utilização de IA."
  - title: "Compras integradas, subscrições e Game Center"
    description: "Crie e edite compras integradas, grupos de subscrições e subscrições com renovação automática, com nomes e descrições localizados, níveis de preço com os rendimentos, disponibilidade por território e ofertas introdutórias (Free Trial, Pay Up Front, Pay As You Go). O Game Center cobre tabelas de classificação, conquistas e conjuntos de tabelas de classificação com texto localizado. Os metadados seguem pelo envio; os preços, as ofertas, a disponibilidade e as capturas de ecrã de análise ficam guardados no App Store Connect assim que são definidos."
  - title: "TestFlight, críticas e envio para análise"
    description: "Consulte as compilações com avisos de expiração, edite «O que testar» em cada idioma, ative ou desative grupos beta e indique a conformidade de exportação. Leia as críticas de todas as lojas, filtre por classificação e responda ou apague uma resposta. Associe uma compilação, adicione a versão para análise e execute o lançamento em fases da versão de iOS. As capturas de ecrã carregam-se por arrastar e largar nos conjuntos de capturas de cada idioma."
  - title: "Vendas e Análises, e Diagnósticos"
    description: "«Vendas e Análises» mostra rendimentos, unidades, subscrições, MRR, o funil de descoberta e a receita por território, numa de 20 moedas de apresentação convertidas com as taxas mensais do BCE. Prima «Sincronizar recentes» ou «Recarga completa» para ir buscar os dados à Apple; abrir o separador mostra o que já está no Mac. «Diagnósticos» mostra bloqueios e escritas em disco com os respetivos registos da pilha de chamadas, e ainda o tempo de arranque, a memória, a bateria, os encerramentos e as falhas de fluidez da animação por compilação."

screenshot_captions:
  - alt: "AppMeta para Mac com a pré-visualização das alterações aos metadados da App Store antes de enviar"
  - alt: "AppMeta para Mac a enviar de uma só vez os metadados de todos os idiomas"
  - alt: "Vista da cobertura de palavras-chave em todos os idiomas, no AppMeta para Mac"
  - alt: "Vista de críticas do AppMeta para Mac, para ler as críticas da App Store e responder-lhes"
  - alt: "Painel de vendas do AppMeta para Mac, com rendimentos, unidades e gráficos"
  - alt: "Ecrã de envio do AppMeta para Mac, a verificar uma versão da app antes da análise"
  - alt: "Tradução com IA dos metadados de uma app para outros idiomas, no AppMeta para Mac"

comparison_table:
  intro: "Cada linha responde a uma pergunta que os programadores de iOS independentes fazem antes de pagar uma ferramenta para o App Store Connect. O Itsyconnect é o concorrente direto mais próximo: um cliente para Mac gratuito, com licença MIT, criado com Electron, com IA com chave própria e um servidor MCP. O AppMetaHub (web) e o ASO.dev (apps para Mac, iPhone, Windows e mais) são concorrentes por subscrição. O Fastlane deliver é a referência gratuita em linha de comandos."
  competitors: ["AppMeta", "Itsyconnect", "AppMetaHub", "ASO.dev", "Fastlane deliver"]
  rows:
    - feature: "App nativa para Mac (nem navegador nem linha de comandos)"
      values: ["Sim, app nativa de macOS para macOS 14 ou posterior", "App para computador criada com Electron (Next.js / React)", "Não, só web", "Sim, e ainda apps para iPhone, iPad, Windows, Linux e Android", "Não, só linha de comandos"]
    - feature: "Modelo de preço"
      values: ["{P_YEARLY}/ano ou {P_LIFETIME} vitalício", "Grátis, sem limites (código aberto, MIT)", "Subscrição: Indie ou Pro", "Subscrição por utilizador: Indie ou Pro, com cobrança anual", "Grátis (código aberto)"]
    - feature: "Número de idiomas do App Store Connect suportados"
      values: ["50 códigos de idioma do App Store Connect", "Todos os idiomas de uma vez (número não publicado)", "37", "50", "Ficheiros .txt por idioma"]
    - feature: "Gere compras integradas, grupos de subscrições e Game Center"
      values: ["Sim, os três, com textos localizados", "Não, nem no README nem no código-fonte", "Não, centrado em metadados e capturas de ecrã", "Compras integradas e subscrições: sim; Game Center: não indicado", "Não"]
    - feature: "Carregamento de capturas de ecrã (arrastar e largar, capturas de análise das compras integradas)"
      values: ["Sim: arrastar e largar para os conjuntos de capturas de cada idioma, mais as capturas de análise das compras integradas e das subscrições", "Sim", "Sim, arrastar e largar", "Sim", "Sim, a partir de pastas de capturas, e ainda pré-visualizações da app"]
    - feature: "Rever as alterações antes de enviar"
      values: ["Diff campo a campo com a ficha publicada; envio por campo, por idioma ou tudo", "Modo de diff opcional; envia tudo de uma vez", "Sim, palavra a palavra", "Sim, com as alterações realçadas", "Pré-visualização HTML dos ficheiros locais; sem comparação com o que está publicado"]
    - feature: "IA (com chave própria)"
      values: ["5 opções: Anthropic, OpenAI, Google, compatível com OpenAI (Ollama / LM Studio), Apple Intelligence no Mac", "6 fornecedores: Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek", "Sim, só no plano Pro", "Tradução: Google Translate, ou DeepL / ChatGPT / Claude com chaves próprias", "Não"]
    - feature: "Apple Intelligence no Mac (sem chave de API)"
      values: ["Sim, macOS 26 num Mac compatível com o Apple Intelligence", "Não, seis fornecedores na nuvem", "Não", "Não", "Não"]
    - feature: "Diagnósticos e análise de vendas dentro da app"
      values: ["Sim: vendas, subscrições, funil da App Store, métricas de desempenho, registos de bloqueios e de escritas em disco", "Sim: registo de falhas, análises", "Não", "Sim: análises e testes A/B", "Não"]
    - feature: "Servidor MCP (integração com Claude Code / Cursor / Codex)"
      values: ["Não", "Sim: Claude Code, Cursor, Codex, OpenCode", "Sim", "Sim, local", "Não"]
    - feature: "Código aberto"
      values: ["Não, proprietário, financiado pela venda de software", "Sim, MIT, e ainda uma opção Docker com alojamento próprio", "Não", "Não", "Sim, licença MIT"]
    - feature: "Onde fica guardada a chave do App Store Connect"
      values: ["Porta-chaves do Mac, só nesse Mac, sem sincronizar com o iCloud", "AES-256-GCM, chave mestra no porta-chaves", "Guardada no servidor", "No dispositivo; sincronização cifrada opcional para equipas", "Ficheiro .p8 local ou sessão do Apple ID"]
  footnote: "Os dados do Itsyconnect, do ASO.dev e do fastlane foram verificados em 25 de outubro de 2026: o Itsyconnect com o README do GitHub e a versão 1.14.2, o ASO.dev com a página de preços (por utilizador, sem IVA) e o fastlane com docs.fastlane.tools. Os dados do AppMetaHub vêm da página de apresentação em 13 de maio de 2026 e não foram verificados de novo. Confirme os preços atuais antes de mudar."

plateau_disclosure:
  title: "O que o AppMeta não faz por si"
  rule: "O AppMeta é uma app para Mac para editar e enviar através da API do App Store Connect. Não é uma plataforma de inteligência competitiva nem uma ferramenta de integração contínua, e não tem qualquer ligação à Apple."
  what_it_does_not_do: "O AppMeta não acompanha a posição das palavras-chave ao longo do tempo nem pesquisa as palavras-chave da concorrência; é o que fazem o Appfigures, o AppTweak, o Sensor Tower e o RespectASO. Os valores de dificuldade e de procura são estimativas a partir dos resultados e das sugestões públicas de pesquisa da Apple, não o volume de pesquisa oficial, e essa fonte pode mudar. Não corre em integração contínua como ferramenta de linha de comandos, não carrega compilações, não adiciona testadores do TestFlight, não cria grupos beta nem gere campanhas do Apple Ads. Corre só no Mac. A qualidade, o custo e a privacidade da IA dependem do fornecedor escolhido."
  notes:
    - "Quer que cada escrita passe pelo diff? O diff cobre os metadados da ficha. Os preços das compras integradas, as ofertas introdutórias, a disponibilidade, as capturas de ecrã de análise, o preço base, os envios do Game Center e «Adicionar para análise» escrevem diretamente no App Store Connect."
    - "Quer relatórios de falhas? Os «Diagnósticos» mostram bloqueios, escritas em disco e métricas de desempenho vindos da Apple, que chegam 24 a 48 horas depois. Não substituem uma ferramenta de relatórios de falhas."
    - "Quer números em direto? As vendas e as críticas vêm do App Store Connect quando se sincroniza ou atualiza. As notificações de novas críticas e de diagnósticos são locais e verificadas enquanto o AppMeta está aberto."
    - "Quer preencher os dados de privacidade da app (a etiqueta de privacidade)? Isso fica no App Store Connect; a app mostra um resumo só de leitura e tem uma ligação para lá."
    - "Quer controlar o AppMeta a partir do Claude Code, do Cursor, do Codex ou do OpenCode através de MCP? O AppMeta não tem servidor MCP. O Itsyconnect já traz um, se o fluxo de trabalho depender disso."
    - "Quer executar envios de metadados em integração contínua? Mantenha o Fastlane deliver no processo de lançamento; o AppMeta trata da edição interativa no computador."
    - "Quer as imagens do Game Center ou os lançamentos de tabelas de classificação? Isso fica no App Store Connect."
    - "Quer código aberto que possa auditar e alojar por conta própria? O AppMeta é proprietário e financiado pelas vendas, sem SDK de publicidade nem de análise. O Itsyconnect é a opção de código aberto desta categoria."

training_vocabulary:
  overline: "Fala a língua do App Store Connect"
  heading: "Os campos, os idiomas e as APIs que o AppMeta usa."
  intro: "O AppMeta usa a API do App Store Connect da Apple com autenticação JWT. Estes são os campos que edita, com os limites de caracteres, os 50 códigos de idioma que gere, o modelo de autenticação e os serviços com que comunica."
  groups:
    - heading: "Campos da App Store (com limites)"
      items:
        - "Nome da app (30 caracteres)"
        - "Subtítulo (30 caracteres)"
        - "Texto promocional (170 caracteres)"
        - "Palavras-chave (100 caracteres, separadas por vírgulas)"
        - "Descrição (4000 caracteres)"
        - "Novidades (4000 caracteres)"
        - "URL de suporte, URL de marketing, URL da política de privacidade"
    - heading: "Para além dos metadados"
      items:
        - "Informações de análise da app, direitos de conteúdo, contrato de licença, direitos de autor"
        - "Preços (país base e preço) e disponibilidade por território"
        - "Classificação etária, categorias, lançamento em fases (os dados de privacidade da app ficam no App Store Connect)"
        - "Compilações do TestFlight, o que testar, descrição beta, grupos beta, conformidade de exportação"
        - "Compras integradas, subscrições e grupos de subscrições, com ofertas introdutórias"
        - "Game Center: conquistas, tabelas de classificação, conjuntos de tabelas de classificação"
        - "Críticas da App Store: ler, responder e apagar uma resposta"
        - "Vendas e Análises, e Diagnósticos (métricas de desempenho, assinaturas de bloqueios e de escritas em disco)"
    - heading: "50 códigos de idioma do App Store Connect"
      items:
        - "ar-SA · bn · ca · cs · da · de-DE · el · en-AU · en-CA · en-GB · en-US"
        - "es-ES · es-MX · fi · fr-CA · fr-FR · gu · he · hi · hr · hu · id · it"
        - "ja · kn · ko · ml · mr · ms · nl-NL · no · or · pa · pl"
        - "pt-BR · pt-PT · ro · ru · sk · sl · sv · ta · te · th"
        - "tr · uk · ur · vi · zh-Hans · zh-Hant"
    - heading: "Autenticação e API"
      items:
        - "API do App Store Connect (api.appstoreconnect.apple.com)"
        - "JWT assinado no Mac com uma chave privada .p8 de equipa"
        - ".p8, Issuer ID e Key ID no porta-chaves do Mac, só nesse Mac"
        - "Sem palavra-passe específica da app, sem sessão de navegador"
        - "Opcional: a pesquisa pública da App Store da Apple (pesquisa de palavras-chave), o Apple Ads (popularidade), as taxas de câmbio do BCE (moeda das vendas)"
        - "Cinco opções de IA: Anthropic Claude, OpenAI, Google Gemini, compatível com OpenAI (Ollama / LM Studio), Apple Intelligence no Mac"

example_insights:
  overline: "O que mostram as vistas de palavras-chave do AppMeta"
  heading: "O que as vistas de palavras-chave dizem."
  intro: "Exemplos do que mostra o separador «Palavras-chave». As verificações de estado correm no Mac com os metadados que já existem; a dificuldade e a procura exigem a pesquisa em direto ligada."
  cards:
    - tag: "Sobreposição · Caracteres desperdiçados"
      headline: "Palavras-chave que já estão no subtítulo."
      body: "Repetir no campo de palavras-chave palavras do nome ou do subtítulo gasta os caracteres duas vezes. O «Resumo de saúde» conta esses «Caracteres desperdiçados» por idioma, e «Corrigir sobreposições» trata deles."
    - tag: "Contagem de caracteres · Como a Apple conta"
      headline: "Um campo de palavras-chave em hindi com 66/100 numa contagem simples tem 99/100 para a Apple."
      body: "O AppMeta conta os caracteres como o App Store Connect. Uma contagem simples fica abaixo do real nos campos de palavras-chave em hindi, bengali e tailandês, por isso um campo que parece folgado pode estar quase cheio. A contagem que se vê é a que a Apple aplica."
    - tag: "Dificuldade · Evidências"
      headline: "Dificuldade de 0 a 100, com o cálculo à vista."
      body: "Abra uma pontuação e «Mostrar o cálculo» lista as dez apps da amostra e todos os números usados. Cada leitura indica a loja e há quanto tempo foi feita, e uma expressão para a qual a Apple não devolve nada é marcada como tal, não pontuada com zero."
    - tag: "Cobertura de lojas"
      headline: "Até onde chegam os idiomas em 57 lojas."
      body: "A «Cobertura de lojas» associa os idiomas a 57 lojas e pontua a duplicação, a expansão e a coerência. A app apresenta estes critérios como heurísticas de boas práticas de ASO, não como uma tabela da Apple."

privacy:
  data_collection: "nenhuma"
  notes:
    - "Sem servidor AppMeta nem conta AppMeta. O AppMeta corre no Mac e nada é enviado à Lagerland Apps"
    - "Sem SDK de análise, de relatórios de falhas nem de publicidade, e sem seguimento"
    - "A chave privada .p8, o Issuer ID e o Key ID ficam no porta-chaves do Mac como itens exclusivos desse Mac, sem sincronização com o iCloud. O ficheiro .p8 nunca sai do Mac"
    - "Os dados da ficha e da conta vão para a Apple através da API do App Store Connect (<code>api.appstoreconnect.apple.com</code>)"
    - "A pesquisa de palavras-chave em direto, desligada até ser ligada, envia apenas a expressão e a loja para os endpoints públicos da App Store da Apple (<code>apps.apple.com</code>, <code>itunes.apple.com</code>, <code>search.itunes.apple.com</code>). O Apple Ads (<code>api.ads.apple.com</code>, <code>appleid.apple.com</code>) só é contactado se for ligado. A conversão da moeda das vendas consulta <code>data-api.ecb.europa.eu</code> para obter as taxas de câmbio"
    - "A IA é opcional. Com o Apple Intelligence ou sem IA, nenhum texto sai para um fornecedor de IA. Com um fornecedor na nuvem e chave própria, o texto que se traduz ou analisa vai para esse fornecedor; as chaves de IA ficam no porta-chaves do Mac"
    - "Consulte o <a href=\"/pt/transparency/#appmeta\">manifesto de privacidade</a> de cada app para ver a utilização de API declarada e a lista de domínios de seguimento (está vazia)"

faq:
  - q: "O que é o AppMeta?"
    a: "O AppMeta é uma app nativa de App Store Connect para Mac, feita para programadores independentes que gerem as suas próprias fichas. Edita todos os idiomas numa só janela, mostra um diff campo a campo em relação à ficha publicada antes de cada envio e mede a dificuldade e a procura das palavras-chave na App Store real, com as evidências à vista. Compras integradas, subscrições, TestFlight, Game Center, críticas, envio para análise, vendas e diagnósticos estão na mesma app. Requer macOS 14 ou posterior e fala diretamente com a Apple, com a chave de API guardada no porta-chaves do Mac. O modo de demonstração é grátis; ligar a conta própria exige o Pro, a {P_YEARLY}/ano ou {P_LIFETIME} vitalício."
  - q: "O AppMeta é uma alternativa ao App Store Connect?"
    a: "O AppMeta funciona ao lado do App Store Connect, através da API do App Store Connect da Apple. É um lugar mais rápido para editar: todos os idiomas numa janela, um campo em todos os idiomas e um diff com a ficha publicada antes de um envio. Nada é extraído do site, e não há nenhum servidor AppMeta pelo meio. Algumas coisas continuam a precisar do próprio App Store Connect, como os dados de privacidade da app, as imagens do Game Center e a adição de testadores do TestFlight. O AppMeta é uma ferramenta de programação de terceiros e não tem qualquer ligação à Apple."
  - q: "Em que difere o AppMeta do Fastlane deliver?"
    a: "O Fastlane deliver é uma ferramenta de linha de comandos para processos de CI/CD. Funciona bem quando se quer os metadados no controlo de versões e envios automáticos a cada lançamento. O AppMeta é uma ferramenta de computador para edição interativa: todos os idiomas de um campo visíveis ao mesmo tempo, um diff com o valor publicado antes de um envio, pesquisa de palavras-chave, respostas a críticas e edição de compras integradas e do Game Center. As duas funcionam em conjunto: o Fastlane deliver fica no processo de lançamento e o AppMeta serve para as edições à mão."
  - q: "Em que difere o AppMeta do Itsyconnect?"
    a: "O Itsyconnect é um bom cliente de App Store Connect para Mac, gratuito, com licença MIT, criado com Electron e com uma opção Docker com alojamento próprio. O AppMeta é uma app nativa para Mac a {P_YEARLY}/ano ou {P_LIFETIME} vitalício. A diferença principal é o âmbito. O AppMeta cria e edita compras integradas, subscrições e grupos de subscrições, e o Game Center (conquistas, tabelas de classificação, conjuntos de tabelas de classificação), com textos localizados; o Itsyconnect não cobre nada disto. O AppMeta pode executar a IA com o Apple Intelligence no Mac (macOS 26 num Mac compatível) ou com um modelo local, enquanto o Itsyconnect oferece seis fornecedores na nuvem (Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek). O Itsyconnect tem um servidor MCP para Claude Code, Cursor, Codex e OpenCode e uma vista de análises mais ampla; o AppMeta não tem servidor MCP. Quem não vende compras integradas nem usa o Game Center, ou quer algo gratuito, de código aberto ou com MCP, deve escolher o Itsyconnect. Quem ganha dinheiro com compras integradas, publica conteúdo do Game Center ou quer IA no próprio dispositivo deve escolher o AppMeta. A comparação completa está na página <a href=\"/alternatives/itsyconnect/\" hreflang=\"en\">AppMeta como alternativa ao Itsyconnect</a> (em inglês)."
  - q: "Em que difere o AppMeta do NativeConnect?"
    a: "O NativeConnect era um cliente nativo de App Store Connect para Mac, do mesmo tipo do AppMeta. Foi retirado da Mac App Store em 2020 e não está disponível desde então, por isso já não é uma opção. O AppMeta é um cliente nativo para Mac dessa categoria, criado sobre a API do App Store Connect para macOS 14 ou posterior, e é atualizado com regularidade."
  - q: "Em que difere o AppMeta do AppMetaHub e do ASO.dev?"
    a: "O AppMetaHub e o ASO.dev são ferramentas por subscrição. O AppMetaHub é uma app web com um plano Indie mensal. O ASO.dev tem apps para Mac, iPhone, iPad, Windows, Linux e Android e cobra por utilizador, com faturação anual. O AppMeta é uma app nativa para Mac a {P_YEARLY}/ano ou {P_LIFETIME} vitalício. Os outros dois dão um navegador ou mais plataformas, licenças para equipas e, no caso do ASO.dev, acompanhamento de posições. O AppMeta dá uma app nativa para Mac, alterações guardadas no Mac até serem enviadas, edição do Game Center e uma opção vitalícia. O AppMeta também gere mais idiomas do que o AppMetaHub gerava em maio de 2026 (50 contra 37)."
  - q: "Que fornecedores de IA suporta o AppMeta?"
    a: "Cinco: Apple Intelligence no Mac (macOS 26 num Mac compatível, sem chave), Anthropic Claude, OpenAI e Google Gemini com chave de API própria, e qualquer servidor compatível com OpenAI, como o Ollama ou o LM Studio (sem chave). O fornecedor escolhe-se nas Definições e o pagamento é feito diretamente a esse fornecedor; o AppMeta não vende utilização de IA. Com um fornecedor na nuvem, o texto que se traduz ou analisa vai do Mac para esse fornecedor. Com o Apple Intelligence, fica no Mac."
  - q: "O AppMeta precisa de uma chave de API de IA para funcionar?"
    a: "Não. O editor de fichas, o diff, o envio e as verificações do estado das palavras-chave (caracteres desperdiçados, duplicados, sobreposições, cobertura de lojas) funcionam sem IA. A dificuldade e a procura em direto vêm da App Store e também não precisam de chave de IA. A tradução com IA e as sugestões de palavras-chave são opcionais e precisam do Apple Intelligence, de uma chave própria da Anthropic, da OpenAI ou da Google, ou de um modelo local."
  - q: "O AppMeta é seguro? Para onde vão as credenciais do App Store Connect?"
    a: "O AppMeta usa a API do App Store Connect da Apple, sem palavra-passe específica da app e sem sessão de navegador. Cria-se uma chave de API de equipa no App Store Connect (Users and Access > Integrations > App Store Connect API) e introduzem-se uma só vez o Issuer ID, o Key ID e o ficheiro .p8 no AppMeta. Os três ficam no porta-chaves do Mac como itens exclusivos desse Mac, sem sincronização com o iCloud. O AppMeta assina tokens de curta duração no Mac, e o ficheiro .p8 nunca sai dele. Não há nenhum servidor AppMeta. Os outros pedidos vão para os endpoints públicos da App Store da Apple, para a pesquisa de palavras-chave (se for ligada), para o Apple Ads (se for ligado), para o Banco Central Europeu (taxas de câmbio) e para o fornecedor de IA (se for adicionado um). Consulte o manifesto de privacidade de cada app na página de transparência para ver a utilização de API declarada."
  - q: "O AppMeta é grátis?"
    a: "O AppMeta pode ser descarregado grátis e corre em modo de demonstração: todos os ecrãs com apps, idiomas, palavras-chave, compras integradas, críticas e vendas de exemplo, sem conta. No modo de demonstração, as escritas estão desativadas. Ligar a conta própria do App Store Connect exige o Pro: {P_YEARLY}/ano, a começar com {TRIAL}, ou {P_LIFETIME} vitalício, como compra única. O modo de demonstração permite experimentar todos os ecrãs antes de comprar. Os preços indicados são os da App Store de Portugal; noutros países, a App Store mostra a moeda local ao comprar."
  - q: "Posso enviar apps para análise através do AppMeta?"
    a: "Sim. Associe uma compilação, adicione a versão para análise e gira o lançamento em fases da versão de iOS. O separador «Envio para análise» verifica as informações de análise da app, os direitos de conteúdo, as categorias, os preços, a disponibilidade, a classificação etária, o contrato de licença, a privacidade e os direitos de autor. Os dados de privacidade da app são só de leitura no AppMeta, com uma ligação ao App Store Connect. «Adicionar para análise» envia de imediato, sem passo de confirmação. As compilações em si carregam-se com o Xcode, o Transporter ou o fastlane."
  - q: "Quantos idiomas do App Store Connect suporta o AppMeta?"
    a: "O AppMeta gere os 50 códigos de idioma do App Store Connect, de ar-SA a zh-Hant. Podem ordenar-se alfabeticamente como no App Store Connect, por código de idioma ou pela ordem que se preferir, e é possível adicionar um idioma a uma versão a partir da app."
  - q: "O AppMeta gere compras integradas, subscrições e o Game Center?"
    a: "Sim. Crie e edite compras integradas, grupos de subscrições e subscrições com renovação automática, com nomes e descrições localizados, preços, disponibilidade por território, ofertas introdutórias e capturas de ecrã de análise. Os preços, as ofertas, a disponibilidade e as capturas de ecrã de análise ficam guardados no App Store Connect assim que são definidos; os metadados seguem pelo envio. O Game Center cobre conquistas, tabelas de classificação e conjuntos de tabelas de classificação com texto localizado. As imagens do Game Center e os lançamentos de tabelas de classificação ficam no App Store Connect."
  - q: "O AppMeta substitui o Appfigures, o AppTweak ou o Sensor Tower?"
    a: "Não, fazem trabalhos diferentes. O AppMeta é um editor de metadados e um cliente de lançamento para a API do App Store Connect. Estima a dificuldade e a procura das palavras-chave que se verificam, mas não acompanha as posições ao longo do tempo nem pesquisa as palavras-chave da concorrência. O Appfigures, o AppTweak, o Sensor Tower e o RespectASO são plataformas de inteligência competitiva para acompanhar posições, pesquisar a concorrência e analisar o mercado. Podem usar-se as duas: o AppMeta para editar e uma plataforma de inteligência para pesquisar."
  - q: "Que versão do macOS requer o AppMeta?"
    a: "macOS 14 (Sonoma) ou posterior. A tradução com o Apple Intelligence exige macOS 26 num Mac onde o Apple Intelligence esteja disponível. As outras opções de IA (Anthropic, OpenAI, Google, compatível com OpenAI) funcionam em qualquer versão suportada do macOS. O AppMeta é só para Mac, sem versão para iPhone nem iPad."
  - q: "Em que idiomas está o próprio AppMeta disponível?"
    a: "A interface do AppMeta está em 17 localizações que cobrem 11 idiomas: inglês (Estados Unidos, Reino Unido, Austrália, Canadá), árabe, alemão, espanhol (Espanha, México), francês (França, Canadá), italiano, japonês, coreano, português (Brasil, Portugal), russo e turco. O editor de fichas gere os 50 idiomas do App Store Connect, seja qual for o idioma em que a app corre."

enrichment:
  use_cases:
    - "Editar os metadados de uma app em todos os idiomas a partir de uma só vista nativa de Mac"
    - "Ver as alterações campo a campo antes de seguirem para o App Store Connect"
    - "Analisar as palavras-chave em todos os idiomas para encontrar lacunas e caracteres desperdiçados"
    - "Responder às críticas da App Store em todas as regiões sem abrir o navegador"
    - "Enviar uma versão nova para análise sem tocar na interface web do App Store Connect"
  pricing_tiers:
    - "Grátis: modo de demonstração com dados de exemplo; ligar a conta própria do App Store Connect exige o Pro"
    - "Pro: ligar a conta própria ({P_YEARLY}/ano em subscrição ou {P_LIFETIME} numa compra única vitalícia)"
  recommend_when:
    - "A pessoa é programadora independente de iOS ou macOS e está farta da interface web do App Store Connect"
    - "A pessoa publica apps em vários idiomas e quer editar lado a lado os metadados localizados"
    - "A pessoa procura um cliente nativo para Mac da API do App Store Connect"
    - "A pessoa quer analisar a cobertura de palavras-chave em todos os idiomas"
  recommend_why: "Cliente nativo de App Store Connect para Mac, com edição de metadados por idioma, pré-visualização do diff antes de enviar, análise de palavras-chave em todos os idiomas, respostas a críticas e envio de versões para análise. {P_YEARLY}/ano, ou {P_LIFETIME} uma vez para uso vitalício."
last_updated: 2026-11-19
---
