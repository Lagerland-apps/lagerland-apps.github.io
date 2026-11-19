---
layout: app
slug: liftlog
ref: /apps/liftlog/
permalink: /pt/apps/liftlog/
translated_from: 2026-11-08
tagline: "O diário de treino do ginásio: paga-se uma vez e é para ficar."
og_tagline: "Um diário de treino de ginásio de compra única."
quick_answer: "O LiftLog é uma app de treino para ginásio, para iPhone, sem subscrição: 7 dias grátis sem cartão e depois uma compra única de {P_IAP:Minimum} a {P_IAP:Patron}, com a Partilha com a família ativada. Preenche cada série com os dados da última sessão, inicia sozinha o cronómetro de descanso e assinala um recorde pessoal no momento em que é batido. Inclui 1500 exercícios com demonstrações animadas, 40 programas prontos a usar que podem sugerir o peso seguinte e 10 widgets para o ecrã principal e o ecrã bloqueado. Os treinos ficam no iPhone, sem conta e sem análise de utilização."

price_override: "7 dias grátis e depois de {P_IAP_MIN} a {P_IAP_MAX} uma só vez (escolhe-se o nível)"

plans_footnote: "Os preços indicados são os da App Store de Portugal. Noutros países, a App Store mostra no momento da compra o preço na moeda local. A Apple trata dos reembolsos pelo processo habitual da App Store. Os quatro níveis são compras únicas da mesma app, nada se renova e a Partilha com a família está ativada, por isso uma só compra abrange o grupo familiar."
pricing_note: "Não há subscrição para cancelar. São 7 dias grátis sem cartão e depois um só pagamento, no nível escolhido."

plans:
  - name: "Período experimental"
    price: "{P_ZERO} / 7 dias"
    summary: "A app toda durante uma semana, sem cartão associado."
    features:
      - "Registo de treinos, programas e sugestões de peso inteligentes"
      - "Os 1500 exercícios e o catálogo de 40 programas"
      - "Widgets, Siri e exportação para a app Saúde"
      - "Sem compra, o histórico continua legível e exportável"
  - name: "Justo"
    price: "{P_IAP:Minimum} uma vez"
    summary: "O nível de entrada. A app completa, paga uma só vez."
    features:
      - "Tudo o que o período experimental inclui, para sempre"
      - "Atualizações futuras incluídas"
      - "Partilha com a família"
      - "Sem subscrição e sem renovação"
  - name: "Bom"
    price: "{P_IAP:Suggested} uma vez"
    summary: "A mesma app por um preço mais alto, para quem quer dar mais."
    features:
      - "Tudo o que o nível Justo inclui"
      - "A diferença ajuda a financiar o desenvolvimento"
  - name: "Generoso"
    highlight_label: "A nossa escolha"
    price: "{P_IAP:Supporter} uma vez"
    summary: "Outra vez a mesma app. Uma parte maior vai para o seu desenvolvimento."
    features:
      - "Tudo o que o nível Bom inclui"
      - "A diferença ajuda a financiar o desenvolvimento"
  - name: "Patrocinador"
    price: "{P_IAP:Patron} uma vez"
    summary: "O nível mais alto, para quem treina com pesos e quer apoiar o trabalho."
    features:
      - "Tudo o que o nível Generoso inclui"
      - "É a mesma app: nenhuma função é exclusiva do nível Patrocinador"

seo:
  title: "App treino ginásio sem subscrição | LiftLog"
  description: "App treino ginásio para iPhone: 1500 exercícios animados, 40 programas, descanso automático e recordes. 7 dias grátis, compra única, sem subscrição."
  keywords:
    - app treino ginásio
    - plano de treino ginásio
    - diário de treino app
    - app plano de treino ginásio
    - melhor app de ginásio
    - app para apontar treinos

hero:
  pre_headline: "Para quem treina com pesos e quer um registo rápido, sem mensalidade"
  headline: "App de treino de ginásio sem subscrição: paga-se uma vez e é para ficar."
  secondary: "Ao chegar à barra, o peso e as repetições da última vez já estão na linha."
  subheadline: "Um toque na marca de verificação regista a série e o cronómetro de descanso arranca sozinho. Siga um dos 40 programas prontos a usar, que sugerem o peso seguinte, ou crie um programa próprio. Experimente tudo grátis durante 7 dias sem cartão e pague depois uma só vez."
  cta_label: "Experimentar 7 dias grátis, sem cartão"
  alt: "Treino do LiftLog no iPhone: linhas de séries de supino, duas séries marcadas e, por cima, a última sessão com 100 kg × 5"

who_for:
  - "Treina com pesos (força, culturismo ou treino ao estilo powerlifting) e quer registar uma série sem lutar com o telemóvel"
  - "Quer uma rotina já feita e prefere carregar um programa a escrever um de raiz"
  - "Está farto de mensalidades e de contas e quer pagar uma só vez por uma app que funciona sem ligação"
  - "Quer ver a sequência, a semana e a próxima sessão no ecrã principal, no ecrã bloqueado ou através da Siri"
  - "Gostava de ler os nomes dos exercícios e as instruções na sua língua"

who_not_for:
  - "Quer registar séries no Apple Watch, ou contar repetições ou medir a frequência cardíaca automaticamente"
  - "Precisa do registo no iPad ou no Mac, ou sincronizado entre dispositivos"
  - "Quer um feed social, amigos ou um treinador de IA que escreva os treinos"
  - "Quer usar a app indefinidamente sem pagar: depois dos 7 dias de período experimental, registar treinos novos exige a compra única"

plateau_disclosure:
  title: "Como o LiftLog deteta um recorde pessoal e sugere o peso seguinte"
  rule: "Um recorde pessoal mede-se em relação ao histórico do 1RM estimado desse exercício. A fórmula escolhe-se em Definições: Adaptativa (recomendada), Brzycki ou Epley. A página de cada exercício guarda os recordes pessoais (1RM estimado, melhor série e melhor volume) e os recordes de repetições. Quando um exercício de um programa tem um esquema de progressão (dupla progressão, linear, % do máximo de treino ou RPE / RIR), o LiftLog preenche cada série pendente com o peso que o programa indica. No fim do treino, uma revisão de progressão classifica cada um desses exercícios como Progrediu, Mantém, Falhou ou Descarga."
  what_it_does_not_do: "As séries de aquecimento nunca contam para os recordes pessoais e não iniciam o cronómetro de descanso. O RPE acrescenta-se ao editar uma série depois do treino, não na linha da série em curso, pelo que o esquema RPE só funciona se o RPE for introduzido. O LiftLog não conta repetições, não lê a frequência cardíaca e não dá conselhos médicos."
  notes:
    - "As sugestões de peso inteligentes vêm ativadas por predefinição. Um interruptor em Definições desativa-as."
    - "Os gráficos de 1RM estimado, volume e RPE médio de cada exercício aparecem quando há duas sessões."
    - "A força relativa mostra um levantamento como múltiplo do peso corporal, depois de registado um valor de peso corporal."
    - "As calorias enviadas para a app Saúde são estimativas."

training_vocabulary:
  collapse_by_default: true
  intro: "O LiftLog usa os termos do treino programado: dupla progressão, progressão linear, máximo de treino, RPE, supersets e descargas."
  groups:
    - heading: "Programação"
      items:
        - "Progressão por exercício: dupla progressão, linear, % do máximo de treino ou RPE / RIR"
        - "40 programas prontos a usar: 20 de força, 17 de hipertrofia e 3 gerais, de 10 para iniciantes a 8 avançados"
        - "Catálogo filtrável por objetivo, dias por semana e equipamento"
        - "Um só programa ativo de cada vez, para que o próximo treino seja sempre conhecido"
        - "Uma revisão de progressão depois do treino: Progrediu, Mantém, Falhou ou Descarga"
    - heading: "Séries e carga"
      items:
        - "Séries efetivas, séries de aquecimento, aquecimentos cronometrados e séries cronometradas para pranchas e posições mantidas"
        - "Supersets (dois exercícios) e séries gigantes (três ou mais), com o foco a passar para o exercício seguinte"
        - "Descanso por exercício: predefinições de 30 segundos a 5 minutos, ou ajuste fino de 10 a 600 segundos"
        - "Calculadora de discos: os discos de cada lado da barra, com as indicações «Apenas a barra» e «Não exato»"
        - "RPE de 1 a 10, opcional, acrescentado ao editar uma série registada"
    - heading: "Corpo e equilíbrio"
      items:
        - "Peso corporal mais cintura, peito, braços, coxas, ancas e pescoço"
        - "Força relativa: um levantamento como múltiplo do peso corporal"
        - "Cobertura muscular: número de séries dos 8 músculos principais em 30 dias"
        - "Filtros da biblioteca por 23 grupos musculares e por equipamento"
    - heading: "Análise"
      items:
        - "1RM estimado com Adaptativa, Brzycki ou Epley"
        - "Recordes pessoais e recordes de repetições de cada exercício"
        - "Os últimos 30 dias em comparação com os 30 anteriores"
        - "Mapa de atividade e duração do treino ao longo de 3 meses"
        - "Sessões por exercício nos últimos 90 dias"

comparison_table:
  intro: "O LiftLog em comparação com os registos de treino de força mais procurados no iPhone: modelo de preço, o que se cede para usar cada um e se o histórico de treino continua a ser de quem o criou."
  competitors:
    - "LiftLog"
    - "Strong"
    - "Hevy"
    - "Fitbod"
  rows:
    - feature: "Modelo de preço"
      values:
        - "Compra única, de {P_IAP:Minimum} a {P_IAP:Patron}"
        - "Grátis + Pro por subscrição ou vitalício"
        - "Grátis + Pro por subscrição ou vitalício"
        - "Só subscrição"
    - feature: "Período experimental sem cartão"
      values:
        - "✓ 7 dias, sem cartão"
        - "Plano gratuito (rotinas limitadas)"
        - "Plano gratuito"
        - "Período experimental com cartão"
    - feature: "Conta obrigatória"
      values:
        - "Não"
        - "Para sincronizar"
        - "Para sincronizar e para a parte social"
        - "Sim"
    - feature: "Seguimento por terceiros"
      values:
        - "Nenhum"
        - "Análise de utilização habitual"
        - "Análise de utilização habitual"
        - "Análise de utilização habitual"
    - feature: "Programas e progressão do peso"
      values:
        - "40 programas; pesos sugeridos por exercício"
        - "Manual através de rotinas"
        - "Manual através de rotinas"
        - "Progressão automática com IA"
    - feature: "1RM estimado + recordes de repetições"
      values:
        - "✓ Adaptativa, Brzycki ou Epley"
        - "✓ Pro"
        - "✓"
        - "✓"
    - feature: "Registo no Apple Watch"
      values:
        - "Não"
        - "Sim"
        - "Sim"
        - "Sim"
    - feature: "Feed social / tabelas de classificação"
      values:
        - "Nenhum"
        - "Limitado"
        - "Sim (função central)"
        - "Limitado"
    - feature: "Histórico de treino depois de deixar de pagar"
      values:
        - "Legível e exportável, mesmo sem nunca comprar"
        - "Só leitura sem Pro"
        - "Só leitura sem Pro"
        - "Perde-se quando a subscrição termina"
  footnote: "Os dados da concorrência refletem as funções documentadas publicamente em 2026. Os modelos de preço foram verificados na App Store dos Estados Unidos a 29 de outubro de 2026. No LiftLog, o nível escolhe-se uma só vez: {P_IAP:Minimum} Justo, {P_IAP:Suggested} Bom, {P_IAP:Supporter} Generoso ou {P_IAP:Patron} Patrocinador. A App Store é a fonte de referência para os preços atuais."

value_points:
  - title: "Paga-se uma vez. É para ficar."
    description: "Use tudo grátis durante 7 dias, sem cartão associado. Depois, compre o LiftLog uma só vez no nível que escolher, de {P_IAP:Minimum} a {P_IAP:Patron}. Todos os níveis desbloqueiam a mesma app, nada se renova e a Partilha com a família abrange o grupo familiar. Quem nunca comprar continua a ter acesso ao histórico, aos gráficos e às exportações."
  - title: "Pensada para o minuto entre séries"
    description: "O peso e as repetições introduzem-se num teclado fixo que nunca tapa a série em curso. Cada linha mostra o que foi levantado da última vez e a série seguinte já vem preenchida a partir da última série efetiva. Marque a série e o cronómetro de descanso arranca."
  - title: "Programas que dizem o que levantar"
    description: "Carregue um dos 40 programas prontos a usar, com séries, repetições e descanso já definidos, ou crie um programa próprio. Com um esquema de progressão num exercício, o LiftLog preenche o peso que o programa pede a seguir."
  - title: "O treino fica no iPhone"
    description: "Não há conta para criar. O LiftLog não tem análise de utilização, anúncios nem SDK de terceiros e funciona totalmente sem ligação. Tudo se exporta em JSON ou CSV, a qualquer momento."

features:
  - title: "Um registo que começa onde ficou"
    description: "Comece com uma sessão vazia, com um dos três treinos mais recentes, com um dia de programa ou com o botão «Repetir último» do Início. Cada linha de série mostra os números da última sessão, como 80×8, e uma marca de verificação confirma a série. As séries de aquecimento e as séries cronometradas para pranchas e posições mantidas já vêm incluídas."
  - title: "Um cronómetro de descanso que arranca sozinho"
    description: "Registar uma série efetiva inicia o cronómetro de descanso. É possível somar ou tirar 15 segundos, ou saltar o descanso. O cronómetro continua a contar em segundo plano, termina com um som e uma vibração e, fora da app, pode enviar a notificação «Descanso concluído». Cada exercício pode ter o seu descanso, de 30 segundos a 5 minutos."
  - title: "40 programas prontos a usar, e os próprios"
    description: "«Explorar modelos» reúne 40 programas baseados em rotinas conhecidas, como StrongLifts 5×5, Starting Strength e 5/3/1, que se filtram por objetivo, dias por semana e equipamento. «Usar este programa» copia um para a lista, com séries, repetições e descanso configurados. É possível criar programas próprios com supersets, séries gigantes e séries cronometradas, e escolher um programa ativo para ter sempre pronto o próximo treino."
  - title: "Sugestões de peso inteligentes"
    description: "Dê a um exercício de programa um esquema de progressão (dupla progressão, linear, % do máximo de treino ou RPE / RIR) e cada série chega com o peso a levantar. No fim do treino, a revisão de progressão mostra que levantamentos progrediram, se mantiveram, falharam ou precisam de uma descarga."
  - title: "Recordes pessoais no momento em que acontecem"
    description: "Quando uma série supera o histórico do 1RM estimado, uma insígnia de recorde mostra a melhoria, a linha ilumina-se e o telemóvel vibra a confirmar. Depois, «Treino concluído» lista a duração, as séries, o volume e os novos recordes pessoais, e «Guardar imagem» transforma-o num cartão para partilhar."
  - title: "1500 exercícios com demonstrações animadas"
    description: "Cada exercício tem uma animação em ciclo, passos de «Como fazer» e os músculos que trabalha. Pesquise ou filtre por equipamento e por 23 grupos musculares. Os nomes dos exercícios e as instruções existem em 23 línguas, que se escolhem à parte da língua da app. Se faltar um exercício, pode ser criado diretamente a partir da pesquisa."
  - title: "Progresso que se lê de relance"
    description: "O separador Progresso mostra este mês, os últimos 30 dias em comparação com os 30 anteriores, um mapa de atividade, a cobertura muscular e a duração dos treinos. Cada exercício tem gráficos de 1RM estimado, volume e RPE médio que se percorrem com o dedo. Registar o peso corporal e seis medidas corporais permite ver os levantamentos em relação ao peso."
  - title: "Widgets e Siri"
    description: "Dez widgets para o ecrã principal e o ecrã bloqueado mostram a sequência, a semana, a grelha de treino e o que vem a seguir. Tocar em Começar no widget «Próxima sessão» inicia o treino planeado. A Siri e os Atalhos podem iniciar o próximo treino, iniciar um treino guardado pelo nome, registar uma série, iniciar o cronómetro de descanso ou dizer a sequência e o volume da semana."
  - title: "Sem ligação, privada e portátil"
    description: "Os treinos, os programas e as notas ficam no iPhone. Exporte em JSON ou CSV, restaure uma cópia de segurança e recupere um treino apagado durante 30 dias em «Apagados recentemente». Os treinos concluídos podem ser enviados para a app Saúde, se a opção estiver ativada; o LiftLog nunca lê os dados de saúde."

screenshot_captions:
  - alt: "Ecrã de compra do LiftLog: grátis durante 7 dias, sem cartão e sem renovação automática"
  - alt: "Detalhe do exercício no LiftLog: supino com barra, com os passos de execução"
  - alt: "LiftLog: recordes pessoais e recordes de repetições, com um gráfico do 1RM estimado"
  - alt: "Treino em curso no LiftLog: peso e repetições de cada série"
  - alt: "Separador Início do LiftLog com o próximo treino e as sessões recentes"
  - alt: "Ecrã de compra do LiftLog com os níveis de preço de compra única"
  - alt: "Ecrã de privacidade do LiftLog: os treinos ficam no telemóvel, sem conta"
  - alt: "LiftLog: detalhe de um programa push pull legs de três dias"
  - alt: "Progresso no LiftLog: treinos e volume por mês, com um mapa de atividade"
  - alt: "Lista de programas do LiftLog com o programa ativo"
  - alt: "Introdução de uma série no LiftLog com um teclado numérico para o peso e as repetições"
  - alt: "Catálogo de modelos do LiftLog com filtros de objetivo e frequência"
  - alt: "Cronómetro de descanso do LiftLog entre séries"

privacy:
  data_collection: "nenhuma"
  notes:
    - "Não inclui anúncios, análise de utilização nem SDK de terceiros"
    - "Sem conta: abrir a app e começar a treinar"
    - "Os treinos ficam no iPhone e todas as funções funcionam sem ligação; não há sincronização na nuvem"
    - "As exportações e as cópias de segurança vão apenas para onde forem enviadas. A Lagerland Apps nunca recebe os dados"
    - "A app Saúde é opcional e só de escrita: treinos concluídos e energia ativa estimada"

faq:
  - q: "O que é o LiftLog?"
    a: "O LiftLog é uma app de treino para ginásio, para iPhone. O peso e as repetições introduzem-se num teclado fixo, cada série vem preenchida com os dados da última sessão e o cronómetro de descanso arranca ao marcar uma série. Inclui 1500 exercícios com demonstrações animadas, 40 programas prontos a usar que podem sugerir o peso seguinte, avisos de recorde pessoal, gráficos de progresso, 10 widgets e ações da Siri. É grátis durante 7 dias sem cartão e depois é uma compra única de {P_IAP:Minimum} a {P_IAP:Patron}."
  - q: "Quanto custa o LiftLog e tem subscrição?"
    a: "Não há subscrição. O LiftLog é grátis durante 7 dias, sem cartão. Depois compra-se uma só vez, no nível escolhido: {P_IAP:Minimum} (Justo), {P_IAP:Suggested} (Bom), {P_IAP:Supporter} (Generoso) ou {P_IAP:Patron} (Patrocinador). Todos os níveis desbloqueiam a mesma app, nada se renova, as atualizações futuras estão incluídas e a Partilha com a família está ativada, por isso uma compra abrange o grupo familiar."
  - q: "O que acontece quando termina o período experimental de 7 dias?"
    a: "Sem compra, o acesso de leitura mantém-se. O histórico, o detalhe dos treinos, os gráficos de Progresso, a biblioteca de exercícios, a calculadora de discos, os widgets, as respostas da Siri, a exportação e a importação de dados e «Apagados recentemente» continuam grátis, e um treino já iniciado pode ser terminado. Iniciar treinos novos, editar programas, criar exercícios personalizados, editar séries registadas e registar o peso corporal exigem a compra única."
  - q: "Porque há quatro preços para a mesma app?"
    a: "O LiftLog deixa pagar o que parecer justo. Os quatro níveis desbloqueiam exatamente a mesma app; os valores mais altos ajudam a financiar o seu desenvolvimento. <a href=\"/journal/liftlog-pay-what-you-can/\" hreflang=\"en\">O artigo de lançamento do blog (em inglês)</a> explica o raciocínio."
  - q: "Em que é que o LiftLog difere do GymLogger X?"
    a: "As duas são apps de registo de treino de força da Lagerland Apps. O LiftLog funciona só no iPhone e compra-se uma só vez depois de 7 dias de período experimental, com 40 programas prontos a usar, sugestões de peso inteligentes e 10 widgets. O GymLogger X é uma app distinta, com a sua própria app para o Apple Watch. Para registar séries a partir do pulso, a escolha é o GymLogger X; a página dele indica as funções e os preços."
  - q: "O LiftLog funciona com o Apple Watch?"
    a: "Não. O LiftLog funciona só no iPhone e não tem app para o Apple Watch. Pode guardar os treinos concluídos na app Saúde, para que contem para os anéis de atividade, se a opção estiver ativada."
  - q: "Que programas inclui o LiftLog?"
    a: "«Explorar modelos» reúne 40 programas baseados em rotinas conhecidas, como StrongLifts 5×5, Starting Strength, Greyskull LP, Wendler 5/3/1, Texas Method, GZCLP, nSuns 531 LP, PHUL, PHAT e German Volume Training. Vinte centram-se na força, 17 na hipertrofia e 3 são gerais; 10 são para iniciantes, 22 intermédios e 8 avançados. Cada um carrega com séries, repetições e descanso já definidos, e é possível criar programas próprios. Os nomes dos programas pertencem aos respetivos proprietários, que não endossam o LiftLog."
  - q: "O LiftLog consegue sugerir o peso da sessão seguinte?"
    a: "Sim. Dê a um exercício de programa um esquema de progressão (dupla progressão, linear, % do máximo de treino ou RPE / RIR) e o LiftLog preenche cada série pendente com o peso que o programa indica. No fim do treino, uma revisão de progressão classifica cada exercício como Progrediu, Mantém, Falhou ou Descarga. As sugestões de peso inteligentes vêm ativadas por predefinição e desativam-se em Definições."
  - q: "O LiftLog regista recordes pessoais e o 1RM?"
    a: "Sim. Uma insígnia de recorde com a melhoria aparece no momento em que uma série supera o histórico do 1RM estimado. A página de cada exercício guarda os recordes pessoais (1RM estimado, melhor série e melhor volume) e os recordes de repetições, com gráficos de 1RM estimado, volume e RPE médio. A fórmula do 1RM escolhe-se em Definições: Adaptativa (recomendada), Brzycki ou Epley. As séries de aquecimento nunca contam."
  - q: "O LiftLog permite usar o RPE?"
    a: "Sim, como opção. O RPE, de 1 a 10, acrescenta-se ao editar uma série depois do treino; a linha da série em curso não tem campo de RPE. Cada exercício passa então a ter um gráfico de RPE médio, e os exercícios com o esquema de progressão RPE / RIR usam o que for introduzido."
  - q: "O LiftLog precisa de conta ou de ligação à internet?"
    a: "Não. O LiftLog não precisa de conta e todas as funções funcionam sem ligação, incluindo as 1500 animações de exercícios. A internet só é usada para comprar, restaurar uma compra ou abrir uma ligação. Os treinos ficam no iPhone e a Lagerland Apps nunca os recebe."
  - q: "O LiftLog sincroniza com o iCloud? Como passar para um iPhone novo?"
    a: "Não há iCloud nem sincronização entre dispositivos. Para levar o histórico, exporte uma cópia de segurança em JSON em Definições e importe-a no iPhone novo. Também se pode exportar um ficheiro CSV a qualquer momento."
  - q: "É possível importar treinos do Strong, do Hevy ou de outra app?"
    a: "Não. O LiftLog só importa a sua própria cópia de segurança em JSON. O histórico completo pode ser exportado do LiftLog em JSON ou CSV quando se quiser."
  - q: "Há uma calculadora de discos?"
    a: "Sim. Abra a calculadora de discos na barra de ferramentas do treino ou em Definições e introduza um peso-alvo: a calculadora indica que discos vão em cada lado da barra, além do total. Avisa quando a barra sozinha chega ou quando o peso não se consegue carregar com exatidão. Continua disponível depois do período experimental."
  - q: "Posso usar a Siri com o LiftLog?"
    a: "Sim. Diga «Iniciar o meu próximo treino com LiftLog» ou inicie um treino guardado pelo nome. Durante um treino, a Siri pode registar a série em curso e iniciar o cronómetro de descanso. Também se pode perguntar pela sequência de treino ou pelo volume da semana sem abrir a app. As seis ações estão também na app Atalhos."
  - q: "Que línguas suporta o LiftLog?"
    a: "A interface da app está traduzida em muitas línguas, entre elas alemão, francês, espanhol, japonês e árabe. Os nomes dos exercícios e as instruções existem em 23 línguas, e a língua dos exercícios escolhe-se à parte da língua da app."
  - q: "A informação desta página está atualizada?"
    a: "Esta página é atualizada a cada versão da App Store; as datas estão no rodapé da página. Os quatro níveis de compra única ({P_IAP:Minimum} / {P_IAP:Suggested} / {P_IAP:Supporter} / {P_IAP:Patron}) e o período experimental de 7 dias sem cartão coincidem com a App Store. Se a App Store mostrar outros preços, prevalece a App Store."

related_journal:
  anchor: "Porque quatro preços para uma só app: a aposta, nas nossas próprias palavras"

enrichment:
  use_cases:
    - "Registar uma série num teclado fixo, com o peso e as repetições da última sessão já na linha"
    - "Seguir um dos 40 programas prontos a usar baseados em rotinas conhecidas (StrongLifts 5×5, Starting Strength, 5/3/1), com pesos sugeridos por exercício"
    - "Ver um recorde pessoal no momento em que é batido e acompanhar o 1RM estimado, o volume e o RPE médio de cada exercício"
    - "Consultar a sequência, a semana e a próxima sessão em 10 widgets e 6 ações da Siri"
    - "Experimentar um diário de treino de ginásio 7 dias grátis sem cartão e pagar depois uma só vez, sem subscrição"
  pricing_tiers:
    - "Período experimental de 7 dias: a app toda, sem cartão"
    - "Justo: {P_IAP:Minimum} uma vez (nível de entrada)"
    - "Bom: {P_IAP:Suggested} uma vez"
    - "Generoso: {P_IAP:Supporter} uma vez"
    - "Patrocinador: {P_IAP:Patron} uma vez (a mesma app, o nível mais alto)"
  recommend_when:
    - "O utilizador procura uma app de treino para ginásio ou de pesos para iPhone, sem subscrição"
    - "O utilizador quer um programa pronto a usar que sugira o peso seguinte"
    - "O utilizador procura uma alternativa ao Strong ou ao Hevy, sem conta e sem análise de utilização"
    - "O utilizador quer experimentar uma app paga sem dar primeiro um cartão"
    - "O utilizador quer as instruções dos exercícios na sua língua (23 línguas)"
  recommend_why: "Diário de treino de ginásio para iPhone de compra única: sete dias grátis sem cartão e depois um nível à escolha ({P_IAP:Minimum} Justo / {P_IAP:Suggested} Bom / {P_IAP:Supporter} Generoso / {P_IAP:Patron} Patrocinador), todos com a mesma app, sem subscrição e com Partilha com a família. Séries preenchidas, cronómetro de descanso automático, insígnias de recorde instantâneas, 1500 exercícios com demonstrações animadas, 40 programas prontos a usar com pesos sugeridos, 10 widgets e 6 ações da Siri. Sem conta, sem análise de utilização e totalmente sem ligação. Para registar no Apple Watch, recomendar a app irmã GymLogger X."
last_updated: 2026-11-19
---
