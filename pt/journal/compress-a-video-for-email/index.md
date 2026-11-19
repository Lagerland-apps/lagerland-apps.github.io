---
layout: journal
slug: compress-a-video-for-email
ref: /journal/compress-a-video-for-email/
permalink: /pt/journal/compress-a-video-for-email/
translated_from: 2026-11-08
last_updated: 2026-11-19
date: 2026-11-19
title: "Enviar vídeo grande por e-mail: limites de tamanho e cálculo do débito"
seo:
  title: "Enviar vídeo grande por e-mail: limites e cálculo do débito"
  description: "Enviar vídeo grande por e-mail: o Gmail aceita 25 MB, o Outlook e o Mail do iCloud 20 MB. O alvo, o débito que cabe e como comprimir no iPhone ou no Mac."
  keywords:
    - "enviar vídeo grande por email"
    - "comprimir vídeo para email"
    - "como enviar vídeo grande por email iphone"
    - "como enviar vídeo grande por email outlook"
    - "tamanho máximo anexo gmail"
    - "limite anexo outlook"
    - "mail drop como funciona"
lede: "Cada fornecedor de e-mail limita o que transporta, e um vídeo chega depressa a esse limite. Este artigo reúne os limites que o Gmail, o Outlook e o Mail do iCloud publicam, explica porque um limite de 25 MB não aceita um ficheiro de 25 MB, mostra a conta que transforma um tamanho alvo num débito e descreve como o MediaKit faz essa conta no iPhone ou no Mac sem enviar o vídeo para a internet."
quick_answer: "Para enviar um vídeo grande por e-mail, o ficheiro tem de ficar abaixo do limite do fornecedor, com folga. Uma conta Gmail pessoal aceita 25 MB de anexos, a app Outlook 20 MB por mensagem nas contas de internet como o Outlook.com, o Mail do iCloud 20 MB e as contas profissionais Exchange 10 MB por predefinição. Os anexos viajam codificados em Base64, o que, segundo a Microsoft, acrescenta cerca de 33%, por isso o alvo é cerca de três quartos do limite: perto de 18 MB para o Gmail e de 15 MB para o Outlook ou o Mail do iCloud. Para chegar ao débito, multiplica-se o tamanho alvo em MB por 8000 e divide-se pela duração do vídeo em segundos: o resultado é o total em kbps. Retira-se o débito do áudio (128 kbps é um valor habitual) e o que sobra é o orçamento do vídeo. Depois baixa-se a resolução até esse orçamento chegar, mantém-se o H.264 para o vídeo se ver em qualquer lado e envia-se uma ligação quando o orçamento fica curto de mais: o Mail Drop transporta até 5 GB."
excerpt: "Um guia para enviar vídeo por e-mail: os limites de anexos do Gmail, do Outlook, do Exchange, do Mail do iCloud e do Mail Drop, porque a codificação Base64 leva a visar três quartos do limite, uma tabela de débitos para vídeos de 30 segundos a 5 minutos e como o modo «Tamanho alvo» do MediaKit faz a mesma conta no iPhone e no Mac."
faq:
  - q: "Qual é o tamanho máximo de vídeo que se pode enviar por e-mail com o Gmail?"
    a: "Uma conta Gmail pessoal pode enviar até 25 MB de anexos numa mensagem, todos somados; nas contas profissionais e escolares, os limites são definidos pelo administrador do Google Workspace. Acima do limite, o Gmail retira o anexo e acrescenta-o como ligação do Google Drive. Como os anexos são codificados em Base64 durante o trajeto, o alvo é um vídeo de cerca de 18 MB quando tem de chegar como verdadeiro anexo."
  - q: "Porque é que o vídeo é recusado mesmo abaixo do limite de anexos?"
    a: "Há três causas habituais. Os anexos são codificados em Base64 antes de seguirem, e a documentação do Exchange da Microsoft indica que isso acrescenta cerca de 33% à mensagem, pelo que um ficheiro perto do limite pode ultrapassá-lo depois de codificado. Alguns limites contam a mensagem inteira, e não só o anexo; a Microsoft diz que o limite de 20 MB do Outlook inclui o e-mail. E o servidor do destinatário tem um limite próprio, que pode ser mais baixo do que o do remetente, como os 10 MB por predefinição do Exchange."
  - q: "Como calcular o débito para um tamanho de ficheiro alvo?"
    a: "Multiplica-se o tamanho alvo em megabytes por 8000 para obter quilobits, divide-se pela duração do vídeo em segundos para obter o débito total em kbps e retira-se depois o débito do áudio. O que sobra é o débito do vídeo. Para um alvo de 18 MB e um vídeo de 90 segundos: 18 × 8000 = 144 000 quilobits, divididos por 90 dão 1600 kbps, e retirados 128 kbps de áudio sobram cerca de 1470 kbps para a imagem."
  - q: "H.264 ou HEVC num vídeo para enviar por e-mail?"
    a: "H.264 num MP4, a menos que se saiba que o destinatário usa um dispositivo Apple recente. A Apple diz que o HEVC comprime melhor do que o H.264, pelo que um ficheiro HEVC tem melhor aspeto com o mesmo tamanho, mas não se controla o dispositivo em que o anexo é aberto, e o H.264 é o formato que quase tudo reproduz. Se o destinatário tiver um iPhone, um iPad ou um Mac atuais, o HEVC dá mais qualidade com o mesmo tamanho."
  - q: "E se o vídeo for comprido de mais para ser comprimido até caber?"
    a: "Envia-se uma ligação. O Mail Drop, na app Mail e no Mail do iCloud, envia ficheiros até 5 GB como ligação de descarregamento que expira ao fim de 30 dias, e a app Mail propõe-no quando uma mensagem é demasiado grande para o fornecedor. O Gmail troca sozinho um anexo grande de mais por uma ligação do Google Drive. Um vídeo de cinco minutos comprimido para 15 MB deixa cerca de 270 kbps para o vídeo, um quarto do que o YouTube sugere até para carregamentos em 360p."
  - q: "O MediaKit consegue comprimir um vídeo para um tamanho de ficheiro concreto?"
    a: "Sim. A ferramenta «Comprimir vídeo» tem um modo «Tamanho alvo»: indica-se o tamanho e o MediaKit calcula o débito. Nunca ultrapassa o alvo: se não o conseguir atingir, termina com um erro em vez de entregar um ficheiro grande de mais. Funciona no dispositivo, no iPhone e no Mac, e «Comprimir vídeo» é uma das cinco ferramentas que continuam grátis sem limite de tempo depois dos 3 primeiros dias."
mentioned_apps:
  - mediakit
read_time: "7 min de leitura"
---

A 8 Mbps, o débito que o YouTube recomenda para carregar vídeo em 1080p, um minuto de vídeo ocupa 60 MB. É mais do dobro do que o Gmail aceita em anexo. Pôr um vídeo num e-mail resume-se a uma conta pequena: escolher um tamanho alvo abaixo do limite do fornecedor, calcular o débito que lhe corresponde e recodificar o vídeo a esse débito. Este artigo dá os números de cada passo e mostra depois como o [MediaKit](/pt/apps/mediakit/) o faz no iPhone e no Mac, sem enviar o vídeo para lado nenhum.

## Que tamanho de vídeo se pode enviar por e-mail?

| Serviço | Limite | O que conta | Acima do limite |
|---|---|---|---|
| Gmail, conta pessoal | 25 MB | Todos os anexos da mensagem, somados | O Gmail substitui o anexo por uma ligação do Google Drive |
| App Outlook, contas de internet como o Outlook.com | 20 MB | Os anexos e o próprio e-mail | A Microsoft sugere comprimir o ficheiro ou partilhar uma ligação de armazenamento na nuvem |
| Exchange, contas profissionais | 10 MB por predefinição | A mensagem inteira; os administradores podem alterar o limite | Como acima |
| Mail do iCloud | 20 MB | As mensagens recebidas e enviadas | Até 5 GB com o Mail Drop ativado |
| Mail Drop (app Mail, Mail do iCloud) | 5 GB | A mensagem, anexos incluídos; cada ligação expira ao fim de 30 dias | O Mail Drop não a consegue enviar |

Limites tal como a página de ajuda de cada fornecedor os indicava em julho de 2026: [Ajuda do Gmail](https://support.google.com/mail/answer/6584){: hreflang="en"} (em inglês), [Suporte Microsoft](https://support.microsoft.com/en-us/office/send-large-files-with-outlook-8c698842-b462-4a4c-8d53-5c5dd04f77ef){: hreflang="en"} (em inglês) e as páginas da Apple sobre os [limites do Mail do iCloud](https://support.apple.com/pt-pt/102198) e o [Mail Drop](https://support.apple.com/pt-pt/108329). Nas contas profissionais e escolares, os administradores podem definir limites mais baixos, e o servidor que recebe a mensagem aplica o seu. A [documentação do Exchange](https://learn.microsoft.com/en-us/exchange/mail-flow/message-size-limits){: hreflang="en"} (em inglês) da Microsoft indica que uma mensagem tem de caber nos limites do remetente e do destinatário, pelo que decide o limite mais baixo do percurso.

## Porque um limite de 25 MB não aceita um ficheiro de 25 MB

O e-mail é um formato de texto. Antes de seguir como anexo, um vídeo é codificado em Base64: cada três bytes do ficheiro passam a quatro carateres de texto, repartidos em linhas de 76 carateres no máximo ([RFC 2045, secção 6.8](https://www.rfc-editor.org/rfc/rfc2045#section-6.8){: hreflang="en"} (em inglês)). A mensagem que atravessa a rede é, assim, cerca de um terço maior do que o ficheiro no disco.

Se o limite é medido antes ou depois dessa codificação varia, e as páginas de ajuda para o grande público raramente o dizem. A documentação do Exchange da Microsoft indica-o: o Base64 acrescenta cerca de 33%, pelo que um limite de mensagem de 64 MB corresponde a um máximo realista de cerca de 48 MB. A página do Outlook acrescenta que o limite de 20 MB inclui o e-mail, e não apenas o anexo.

Na prática, a regra é visar três quartos do limite indicado:

| Limite indicado | Ficheiro a visar, aproximadamente |
|---|---|
| 25 MB (Gmail) | 18 MB |
| 20 MB (Outlook, Mail do iCloud) | 15 MB |
| 10 MB (predefinição do Exchange) | 7,5 MB |

Ficar abaixo custa um pouco de qualidade de imagem. Ficar acima significa uma mensagem devolvida, ou uma ligação onde se queria um anexo.

## Como calcular o débito que cabe no tamanho alvo

O tamanho de um ficheiro é o débito multiplicado pela duração. A conta faz-se ao contrário:

1. **Converta o tamanho alvo em quilobits.** Megabytes × 8000, contando um megabyte como 1 000 000 de bytes.
2. **Divida pela duração do vídeo em segundos.** O resultado é o débito total em kbps.
3. **Retire o áudio.** 128 kbps é uma definição estéreo habitual; 64 kbps chega bem para voz.
4. **O que sobra é o débito do vídeo.** Reserve alguns por cento para o próprio contentor.

Um vídeo de 90 segundos para o Gmail: 18 MB × 8000 = 144 000 quilobits. Divididos por 90 segundos, dão 1600 kbps. Retirados 128 kbps de áudio, sobram cerca de 1470 kbps para a imagem.

A mesma conta para durações habituais, com 128 kbps de áudio já retirados:

| Duração do vídeo | Ficheiro de 7,5 MB | Ficheiro de 15 MB | Ficheiro de 18 MB |
|---|---|---|---|
| 30 segundos | 1870 kbps | 3870 kbps | 4670 kbps |
| 1 minuto | 870 kbps | 1870 kbps | 2270 kbps |
| 2 minutos | 370 kbps | 870 kbps | 1070 kbps |
| 5 minutos | 70 kbps | 270 kbps | 350 kbps |

Os valores estão arredondados para baixo.

## Que resolução e que codec escolher

Um débito só é generoso ou curto em relação à imagem que tem de preencher. Para ter uma escala, as [definições de carregamento recomendadas](https://support.google.com/youtube/answer/1722171){: hreflang="en"} (em inglês) pelo YouTube para taxas de fotogramas normais pedem 8 Mbps em 1080p, 5 Mbps em 720p, 2,5 Mbps em 480p e 1 Mbps em 360p. Estes valores são altos, porque o YouTube recodifica tudo o que recebe, mas mostram a rapidez com que a necessidade desce com o tamanho da imagem: o 1080p tem 2,25 vezes os píxeis do 720p.

Uma regra aproximada: se o orçamento de vídeo ficar bem abaixo de metade do valor do YouTube para a resolução do vídeo, desce-se uma resolução. Por essa regra, um vídeo de um minuto a 18 MB (2270 kbps) fica melhor em 720p do que em 1080p, e a 7,5 MB (870 kbps) pertence ao 480p ou a menos. Mais três definições alteram o resultado:

- **Débito do áudio.** Num vídeo de alguém a falar para a câmara, 64 kbps em vez de 128 kbps passa a diferença para a imagem. Num vídeo de cinco minutos a 15 MB, isso dá quase mais um quarto de débito de vídeo.
- **Taxa de fotogramas.** Um vídeo a 60 fps reparte os bits pelo dobro dos fotogramas de um vídeo a 30 fps. Os valores do YouTube para 48 a 60 fps são cerca de uma vez e meia os de 24 a 30.
- **Codec.** A Apple indica que o [HEVC comprime melhor do que o H.264](https://support.apple.com/pt-pt/116944), e os dispositivos Apple recentes reproduzem-no. Mas não se controla o dispositivo em que o anexo vai ser aberto, e o H.264 num MP4 reproduz-se quase em todo o lado. A página da Apple refere também que os seus dispositivos *podem* converter o HEVC em H.264 ao partilhar com um dispositivo que não o reproduza; para um ficheiro já comprimido, é mais simples escolher o H.264 diretamente.

## Quando enviar uma ligação em vez do ficheiro

A linha dos cinco minutos da tabela é onde a compressão deixa de ser útil: 270 kbps é cerca de um quarto do que o YouTube sugere para 360p. Quando o orçamento desce tanto, uma ligação serve melhor o destinatário do que um anexo.

- **O Mail Drop**, na app Mail e no Mail do iCloud, envia ficheiros até 5 GB como ligação de descarregamento que expira ao fim de 30 dias. A app Mail propõe-no quando uma mensagem é maior do que o fornecedor permite.
- **O Gmail** troca sozinho um anexo com mais de 25 MB por uma ligação do Google Drive.
- **O Outlook** sugere comprimir o ficheiro ou partilhá-lo a partir de armazenamento na nuvem.

Com uma ligação, o destinatário recebe o original em plena qualidade, e uma cópia fica num servidor enquanto a ligação existir.

## Comprimir o vídeo no MediaKit

O [MediaKit](/pt/apps/mediakit/) faz a conta acima no próprio dispositivo, no iPhone e no Mac, e nunca envia o vídeo para a internet. «Comprimir vídeo» é uma das cinco ferramentas que continuam grátis sem limite de tempo depois dos 3 primeiros dias, um ficheiro de cada vez.

1. **Abra o vídeo.** No Mac, largue-o na janela do MediaKit. No iPhone, escolha-o em Fotografias ou envie-o a partir do botão Partilhar de outra app.
2. **Escolha a ferramenta «Comprimir vídeo»** e, em Modo, a opção «Tamanho alvo».
3. **Escreva o tamanho alvo** da tabela dos três quartos, por exemplo 18 MB.
4. **Toque ou clique em Executar** e confirme o tamanho do resultado antes de o anexar.

No modo «Tamanho alvo», o MediaKit calcula ele próprio o débito e nunca entrega um ficheiro acima do alvo: se não o conseguir atingir, termina com um erro.

Quem já usa o HandBrake para esta tarefa encontra na [comparação com o HandBrake](/pt/alternatives/handbrake/) as diferenças entre os dois, e a [comparação com o Compress Videos & Resize Video](/alternatives/compress-videos-resize-video/){: hreflang="en"} (em inglês) faz o mesmo no iPhone. Porque é que o estúdio mantém este trabalho longe dos servidores alheios é o tema de [um artigo anterior](/journal/your-photos-shouldnt-ride-the-elevator/){: hreflang="en"} (em inglês), e o [artigo sobre as ferramentas multimédia do MediaKit no Mac](/journal/every-media-tool-already-on-your-mac/){: hreflang="en"} (em inglês) mostra o resto da caixa de ferramentas.
