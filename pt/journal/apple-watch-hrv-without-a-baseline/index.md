---
layout: journal
slug: apple-watch-hrv-without-a-baseline
ref: /journal/apple-watch-hrv-without-a-baseline/
permalink: /pt/journal/apple-watch-hrv-without-a-baseline/
translated_from: 2026-11-08
last_updated: 2026-11-19
date: 2026-11-19
title: "VFC baixa no Apple Watch: porque é que o valor quase nada diz sem uma linha de base"
seo:
  title: "VFC baixa no Apple Watch: o que significa e como a ler"
  description: "VFC baixa no Apple Watch? Uma leitura de 42 ms pode ser ótima ou alarmante, e só a linha de base diz qual. O que mede, o que lhe escapa e como a ler."
  keywords:
    - "vfc baixa"
    - "vfc baixa o que significa"
    - "vfc baixa o que fazer"
    - "vfc valores normais"
    - "variabilidade da frequência cardíaca valores normais"
    - "linha de base vfc"
lede: "Uma VFC (HRV) de 42 ms no Apple Watch pode ser excelente, média ou alarmante, e sem contexto não há maneira de saber qual. Sozinho, o número é uma das métricas mais mal interpretadas entre as que os aparelhos de saúde de consumo mostram. Este artigo explica o que a VFC indica, o que não indica e porque é que uma linha de base pessoal é a única referência que torna a leitura útil."
quick_answer: "Uma VFC baixa no Apple Watch só tem significado comparada com a linha de base da própria pessoa, a sua média móvel. A VFC (variabilidade da frequência cardíaca, que o Apple Watch indica em SDNN) varia em valor absoluto de 3 a 10 vezes entre pessoas, consoante a idade, o sexo, a forma física, a postura, o momento da medição e o pulso em que o relógio está. Lê-se como um desvio percentual em relação à média da própria pessoa nas últimas semanas; 60 dias é uma boa janela. Comparar o valor com o de um amigo, com uma média da população ou com uma tabela de «intervalo normal» da internet induz quase sempre em erro."
excerpt: "Uma VFC de 42 ms no Apple Watch é excelente para uma pessoa e alarmante para outra. Este artigo explica porque é que a VFC absoluta varia de 3 a 10 vezes de corpo para corpo, porque é que a linha de base pessoal é a única referência que torna útil a VFC do Apple Watch e como ler as tendências como um cientista do desporto."
faq:
  - q: "Uma VFC de 42 ms é boa ou má?"
    a: "Depende inteiramente de quem tem esses 42 ms. Para quem tem uma linha de base de 38 ms nos últimos 60 dias, 42 ms estão acima da média e são um bom sinal de recuperação. Para quem tem uma linha de base de 80 ms, 42 ms são metade do normal e sinalizam provavelmente stress significativo, doença ou carga de treino acumulada. O mesmo valor absoluto é uma boa notícia num corpo e uma má notícia noutro, e é por isso que qualquer app de VFC que valha a pena compara cada pessoa consigo própria."
  - q: "Porque é que a VFC do Apple Watch é tão diferente da de uma cinta cardíaca?"
    a: "O Apple Watch mede a VFC (SDNN) em momentos variáveis do dia e durante a noite, quando a pessoa está imóvel, por fotopletismografia ótica. Uma cinta cardíaca mede de forma contínua, a partir da atividade elétrica do coração. São duas medições diferentes, feitas em condições diferentes, pelo que os valores absolutos de uma não correspondem aos da outra. Já as leituras que o mesmo relógio faz da mesma pessoa ao longo do tempo são comparáveis entre si. A tendência é fiável; o valor absoluto posto ao lado de uma tabela feita com cintas cardíacas não é."
  - q: "Quanto varia a VFC de um dia para o outro na mesma pessoa?"
    a: "Muito. Oscilações de 10 a 25% de um dia para o outro são normais num adulto saudável, pelo que uma única leitura baixa quase nunca é significativa. O que conta é a média móvel de 7 dias em relação à linha de base de 60 dias. A VFC de um dia isolado é sobretudo ruído."
  - q: "Porque é que a VFC desce no inverno?"
    a: "Por adaptação cardiovascular sazonal. A exposição ao frio, menos luz do dia, menos atividade aeróbica e alterações do sono deslocam o equilíbrio autonómico para o predomínio simpático. Uma descida de 10 a 20% no inverno é comum e não é patológica. Um dos erros de interpretação mais frequentes é ler essa descida como «há algo de errado comigo», quando significa «no inverno, a minha VFC anda mais baixa»."
  - q: "O Apple Watch indica a VFC em RMSSD, SDNN ou lnRMSSD?"
    a: "Em SDNN. A app Saúde guarda a VFC do Apple Watch como SDNN, o desvio padrão dos intervalos entre batimentos cardíacos sucessivos, em milissegundos, e é a única métrica de VFC que o HealthKit disponibiliza. A ciência do desporto usa muitas vezes o RMSSD e o seu logaritmo natural, o lnRMSSD, que são cálculos diferentes do SDNN, pelo que uma leitura do Apple Watch não se converte simplesmente em nenhum dos dois. O Observa mostra o SDNN que a app Saúde regista e compara-o com a linha de base de cada pessoa."
mentioned_apps:
  - observa
read_time: "8 min de leitura"
---

O Apple Watch mede um dos valores fisiológicos mais informativos ao alcance de um aparelho de consumo e quase ninguém o usa bem.

Abra a app Saúde e toque em «Variabilidade da frequência cardíaca». Aparece uma coluna de valores das últimas semanas, talvez uns 25, uns 45, uns 80, e um gráfico de Intervalo que parece vagamente informativo. Quem tenha caído no canto errado da internet pode ter lido que a VFC «deve» estar acima de 50 ms ou que tudo o que fique abaixo de 30 é «preocupante». Isso é mais ou menos tão útil como ouvir que a temperatura corporal «normal» devia ser de 37 °C, seja quem for a pessoa. O número é real. A referência é que está errada.

## O que a VFC mede realmente

A VFC, ou variabilidade da frequência cardíaca, é a variação do tempo entre batimentos cardíacos consecutivos. O Apple Watch indica o SDNN, o desvio padrão dos intervalos entre batimentos normais sucessivos (os intervalos NN, ou RR), em milissegundos. Em geral, um valor mais alto corresponde a mais atividade parassimpática («repouso e digestão») do sistema nervoso e um valor mais baixo a mais atividade simpática («luta ou fuga»). Uma tendência persistentemente mais alta está associada à forma cardiovascular, à qualidade da recuperação e ao predomínio parassimpático.

Até aqui, tudo bem. Os problemas começam quando as mesmas palavras se aplicam a duas pessoas cujos valores absolutos diferem num fator de três.

## A variação entre pessoas é enorme

Nos adultos saudáveis, a VFC absoluta vai de cerca de 15 ms a 150 ms em SDNN, uma amplitude de 10 vezes. Estes fatores deslocam a linha de base de cada pessoa:

- **Idade.** A maioria dos estudos longitudinais conclui que a VFC desce cerca de 0,5 a 1 ms por ano depois dos 30 anos. Uma pessoa de 45 anos com 35 ms e uma de 25 anos com 70 ms podem ambas estar em perfeita saúde parassimpática para a idade que têm.
- **Sexo.** A VFC média é um pouco mais baixa nas mulheres adultas do que nos homens, embora a variação dentro de cada sexo seja muito maior do que a diferença entre os dois.
- **Forma física.** As pessoas com treino de resistência aeróbia mostram habitualmente uma VFC em repouso 50 a 100% mais alta do que as não treinadas. Também isso não é informativo em proporção: atletas em boa forma situam-se muitas vezes em intervalos que uma tabela genérica classificaria como «elevados».
- **Posição do corpo.** A VFC é mais alta na posição deitada do que sentada, e mais alta sentada do que de pé.
- **Hora do dia.** Mais alta durante a noite, mais baixa nas horas de atividade.
- **Método de medição.** A PPG ótica do Apple Watch, feita em momentos variáveis, dá valores diferentes dos de uma cinta cardíaca ou de um ECG de qualidade de investigação, mesmo na mesma pessoa e no mesmo instante.

A VFC é uma daquelas métricas biológicas em que só *a de cada pessoa* quer dizer alguma coisa. Comparar 42 ms com os 65 ms de um amigo não diz nada.

## A referência certa: a própria linha de base de 60 dias

As únicas leituras de VFC que se podem interpretar com fiabilidade têm este aspeto:

- **«A VFC (SDNN) de hoje está X% acima ou abaixo da minha própria média móvel de 7 dias.»**
- **«A média desta semana está X% acima ou abaixo da minha própria média móvel de 60 dias.»**

Ambas comparam a pessoa consigo própria, o que anula quase todos os fatores de confusão acima. A idade e o sexo não mudam em 60 dias, a forma física não muda de forma dramática e o relógio é o mesmo. O que muda é *aquilo que alterou a fisiologia esta semana em comparação com o último trimestre*, e essa é a pergunta que vale a pena fazer.

Sessenta dias funcionam como janela da linha de base por três razões. Equivalem a cerca de dois ciclos menstruais, pelo que a variação cíclica se dilui na média. Cobrem dois mesociclos de treino típicos, pelo que a adaptação de curto prazo não domina. E dão amostras semanais não sobrepostas em número suficiente para o desvio padrão (DP) significar alguma coisa; com menos, o próprio DP tem demasiado ruído.

## O que uma leitura baixa isolada significa e o que não significa

Uma manhã em que a VFC está 30% abaixo da média de 7 dias significa que *aconteceu alguma coisa*: uma refeição tardia, álcool, sono fraco, uma noite de stress, o início de uma doença, treino intenso na véspera ou o ruído biológico normal de um dia para o outro. Por si só, não diz para descansar, treinar a fundo, entrar em pânico ou festejar.

Um *padrão* é que tem valor de diagnóstico. Três dias seguidos a mais de um desvio padrão abaixo da linha de base são um sinal. Uma descida isolada de 25% depois de um fator de stress conhecido diz algo sobre esse fator, não sobre a saúde. Uma descida de 25% sem causa identificável que não se tenha resolvido em 72 horas merece atenção, de um profissional de saúde e não de uma app de consumo.

Para a autoexperimentação, este limiar parece-me aproximadamente certo: **pelo menos 10 observações nas mesmas condições ao longo de uma janela de 60 dias, e pelo menos um desvio padrão de separação entre condições**, antes de tratar uma conclusão como algo mais do que ruído. Uma «descoberta» com menos suporte do que isto costuma ser um palpite.

## Porque é que a VFC desce no inverno (e outro ruído sazonal)

Quem usa um Apple Watch durante um inverno do hemisfério norte deve contar que a linha de base da VFC desça 10 a 20% entre outubro e fevereiro. As causas habituais são a exposição ao frio, menos luz do dia, menos atividade aeróbica, mais tempo em espaços interiores e alterações do sono. Nenhuma é patológica e todas puxam o número para baixo.

Ler uma descida de inverno como «há algo de errado comigo» é um dos erros de interpretação mais comuns. A leitura certa é «no inverno, a minha VFC anda mais baixa, e esta é a nova linha de base para medir os desvios». A linha de base deve variar, porque a fisiologia varia com o mundo à volta.

## O que isto significa na prática

Daqui saem algumas regras práticas:

1. **Nunca comparar o valor com o de outra pessoa.** Nem com o de um amigo, nem com o de um desconhecido no Reddit, nem com uma infografia de «intervalo normal». Cada pessoa compara-se consigo própria.

2. **Acompanhar as tendências.** A VFC de um único dia é sobretudo ruído. A média móvel de 7 dias é o sinal, e a linha de base de 60 dias é a referência que torna o sinal interpretável.

3. **Ler o valor como um desvio em relação à própria linha de base.** A VFC tem uma distribuição aproximadamente log-normal, pelo que a mesma diferença em milissegundos pesa mais numa linha de base baixa do que numa alta. Exprimir o SDNN de hoje como desvio percentual em relação à média móvel pessoal é o que o torna interpretável.

4. **Identificar os fatores de stress.** Se a VFC desce de forma consistente depois de treinos tardios, de álcool ou de muito tempo de ecrã, é possível agir sobre isso. O problema está na causa desconhecida, não na descida.

5. **Contar com uma deriva sazonal.** Mais baixa no inverno e mais alta no verão é normal. Uma pandemia, uma doença, o stress pessoal ou o nascimento de um bebé também deslocam a linha de base. É uma referência que se move.

O [Observa](/pt/apps/observa/) faz grande parte deste trabalho. Mostra a VFC (SDNN) em relação ao intervalo habitual de cada pessoa, com 7 dias de tendência grátis e 30, 90 ou 365 dias com o Premium. A VFC pesa também 25% na pontuação de prontidão diária, e «Porquê esta pontuação?» explica em linguagem simples quando a VFC está fora do intervalo habitual e fez mexer a pontuação. A análise corre no dispositivo, e a comparação que faz é *a pessoa, hoje, em relação ao seu próprio normal*, a única comparação de VFC que vale a pena fazer.

## O essencial

- **A VFC absoluta varia de 3 a 10 vezes entre adultos saudáveis.** Comparar o valor com o de qualquer outra pessoa não tem significado.
- **A linha de base de cada pessoa, construída ao longo de semanas, é a única referência que torna a VFC útil.** Oscilações de 10 a 25% de um dia para o outro são normais.
- **As tendências contam; os pontos isolados não.** Três dias seguidos a mais de um DP abaixo da linha de base são um sinal. Um dia é ruído.
- **A VFC de inverno anda mais baixa do que a de verão.** A deriva sazonal é normal, e tratá-la como doença é o erro comum.
- **Ler o SDNN como desvio em relação à própria linha de base.** A VFC tem uma distribuição aproximadamente log-normal, por isso cada dia compara-se com a média pessoal em percentagem, e não com limiares brutos em milissegundos.

O número esteve sempre na app Saúde. Faltava uma linha de base para o ler.
