---
layout: journal
slug: converter-mkv-para-mp4
permalink: /pt/journal/converter-mkv-para-mp4/
local_only: true
last_updated: 2026-11-19
date: 2026-11-19
title: "Converter MKV para MP4: remux sem perder qualidade, VLC, online ou MediaKit"
seo:
  title: "Converter MKV para MP4: VLC, online ou MediaKit"
  description: "Converter MKV para MP4 no Mac ou no iPhone: remux sem perder qualidade ou recodificação, VLC grátis, conversor online ou MediaKit no dispositivo."
  keywords:
    - "converter mkv para mp4"
    - "converter mkv para mp4 grátis"
    - "converter mkv para mp4 vlc"
    - "converter mkv para mp4 sem perder qualidade"
    - "converter mkv para mp4 online"
    - "converter mkv para mp4 ficheiro grande"
    - "converter mkv para mp4 mac"
    - "converter mkv para mp4 iphone"
lede: "Um ficheiro MKV é um contentor que guarda vídeo, som e legendas, por isso convertê-lo para MP4 pode resumir-se a trocar a embalagem sem mexer na imagem. Este artigo explica a diferença entre remux e recodificação, o que o VLC permite fazer, o que implica um conversor online para um ficheiro grande e como o MediaKit abre um MKV no Mac e no iPhone, com os formatos de som que passam e os que ficam de fora."
quick_answer: "Para converter um MKV para MP4 sem perder qualidade, é preciso um remux: o vídeo e o som são copiados para um contentor MP4 sem serem recodificados, o que exige codecs compatíveis. O VLC, que é grátis, sabe converter (menu Media, Convert/Save), ao passo que um conversor online obriga a enviar o ficheiro inteiro. O MediaKit faz o remux de um MKV no dispositivo, no Mac e no iPhone: o H.264, o HEVC, o AAC e o AC-3 passam tal como estão, mas o som DTS, E-AC-3 e MP3 é excluído, com um aviso. A ferramenta «Converter» é grátis durante os 3 primeiros dias e depois fica reservada ao Pro, enquanto «Comprimir vídeo» continua grátis e gera um MP4 por recodificação."
excerpt: "Converter MKV para MP4: o que é um contentor, remux ou recodificação, o VLC e os conversores online para um ficheiro grande, e como o MediaKit abre e converte um MKV no Mac e no iPhone."
faq:
  - q: "Como converter MKV para MP4 grátis?"
    a: "O VLC é grátis e sabe converter: a wiki da VideoLAN descreve um assistente que se abre no menu Media, comando Convert/Save. No MediaKit, a ferramenta «Comprimir vídeo» continua grátis depois dos 3 primeiros dias, um ficheiro de cada vez, e transforma um MKV em MP4; como recodifica, não é uma conversão sem perdas. A ferramenta «Converter», que faz remux, é grátis durante os 3 primeiros dias e depois fica reservada ao Pro."
  - q: "É possível converter MKV para MP4 sem perder qualidade?"
    a: "Sim, quando os codecs o permitem: um remux copia o vídeo e o som para um contentor novo sem os recodificar. É assim que o MediaKit faz o remux de um MKV com vídeo H.264 ou HEVC e som AAC ou AC-3. Já o som DTS, E-AC-3 ou MP3 de um MKV é excluído, com um aviso."
  - q: "Como converter MKV para MP4 com o VLC?"
    a: "A wiki da VideoLAN, que avisa ela própria que a página está desatualizada, descreve um assistente que se abre no menu Media, comando Convert/Save, onde se escolhe um codec de vídeo, um codec de áudio e um contentor. Indica também que uma transcodificação pode ser muito lenta e que não é preciso transcodificar quando as faixas já têm o codec pretendido. Como a página está desatualizada, a referência é a documentação da versão do VLC em uso."
  - q: "Que conversor online usar para um ficheiro MKV grande?"
    a: "Qualquer conversor online recebe o ficheiro nos seus servidores antes de o converter, por isso um MKV grande tem de ser enviado por inteiro. Uma conversão no dispositivo, com o VLC ou o MediaKit, evita esse envio."
  - q: "Como converter MKV para MP4 no iPhone?"
    a: "O MediaKit abre ficheiros MKV no iPhone (iOS 17 ou posterior) e tem a ferramenta «Converter», que gera MP4, MOV ou M4V. Para um remux, escolha a opção «Manter o original (remux)»: o MediaKit copia então, sem recodificar, o vídeo H.264 ou HEVC e o som AAC ou AC-3. O som DTS, E-AC-3 ou MP3 é excluído, com um aviso."
  - q: "Como converter MKV para MP4 no Mac?"
    a: "No Finder, clique com o botão direito no MKV, escolha «Abrir com» e depois o MediaKit, que aparece nessa lista para os ficheiros MKV. A seguir, escolha «Converter», o formato MP4 e «Manter o original (remux)». O MediaKit pede macOS 14.6 ou posterior."
mentioned_apps:
  - mediakit
read_time: "6 min de leitura"
---

Um ficheiro MKV é um contentor que embrulha faixas de vídeo, de som e de legendas. Converter um MKV para MP4 pode, por isso, resumir-se a trocar a embalagem, sem recodificar a imagem nem o som e sem perder qualidade. Só é possível quando os codecs lá dentro cabem no contentor MP4, e é isso que separa uma conversão sem perdas de uma conversão que degrada o ficheiro. Este artigo parte dessa diferença e compara depois o VLC, os conversores online e o [MediaKit](/pt/apps/mediakit/).

## O que é um MKV e em que difere de um MP4

O projeto Matroska, que mantém o formato, esclarece no seu site que um contentor [não é um formato de compressão de vídeo ou de áudio](https://www.matroska.org/what_is_matroska.html){: hreflang="en"} (em inglês). Descreve-o como um envelope que pode levar várias faixas de áudio, vídeo e legendas, o que permite guardar um filme completo num único ficheiro. O projeto quer fazer do Matroska a alternativa de código aberto a contentores existentes como o AVI, o MOV e o MP4, o que mostra que o MP4 também é um contentor.

Dois ficheiros podem assim ter a mesma imagem e o mesmo som e distinguir-se só pelo envelope. Trocar de envelope faz-se sem mexer no conteúdo; trocar de codec obriga a descodificar e depois a recodificar.

## Porque é que um MKV nem sempre abre no iPhone ou no Mac

A Apple explica-o numa página de suporte sobre [ficheiros multimédia que não abrem](https://support.apple.com/pt-pt/102644). As apps da Apple, como Fotografias, iMovie, Safari, Keynote e QuickTime Player, funcionam com muitos formatos, mas os formatos mais antigos ou específicos podem não funcionar como esperado se o dispositivo, o sistema operativo ou a app em uso não os suportarem. Para encontrar outra app que suporte o formato, a Apple sugere pesquisar pela extensão do ficheiro e dá como exemplos .avi, .wmv e .mkv. No Mac, segundo a mesma página, é possível identificar o formato selecionando o ficheiro no Finder e premindo Comando+I: a janela de informações pode mostrar «Tipo: ficheiro de vídeo Matroska».

## Remux ou recodificação: quando não se perde nada

Um remux passa as faixas de vídeo e de som de um contentor para outro sem as descodificar. No MediaKit, é a opção «Manter o original (remux)» da ferramenta «Converter». O ganho está em o ficheiro não ser recomprimido: a imagem que sai é a imagem que entrou.

Um remux só funciona se o MP4 conseguir transportar os codecs do ficheiro. No MediaKit, o vídeo H.264 e HEVC e o som AAC e AC-3 passam tal como estão. O som DTS, E-AC-3 e MP3 de um MKV é excluído, com um aviso: o vídeo mantém-se, mas essas faixas de som não. Quem tiver um filme com faixa DTS deve, por isso, ler a mensagem depois da conversão.

Uma recodificação gera uma compressão nova, e é isso que acontece quando se comprime para um tamanho alvo ou se escolhe outro codec. Serve quando o remux é impossível ou quando se quer um ficheiro mais pequeno, mas custa parte da qualidade.

## Converter MKV para MP4 com o VLC

O VLC é grátis. O [site da VideoLAN](https://www.videolan.org/vlc/){: hreflang="en"} (em inglês) apresenta-o como um leitor multimédia livre e de código aberto e inclui o MKV entre os formatos que lê. Para converter, a wiki da VideoLAN descreve, numa [página sobre transcodificação](https://wiki.videolan.org/Transcode/){: hreflang="en"} (em inglês), um assistente que se abre no menu Media, comando Convert/Save, e pede um codec de vídeo, um codec de áudio e um contentor. A mesma página indica que não é preciso transcodificar quando as faixas já têm o codec pretendido; o autor julga, sem certeza, que a interface chama «keep the original track» a essa opção. A wiki avisa ainda que a página está desatualizada e que uma transcodificação pode ser muito lenta. Para os passos exatos, a referência é a documentação da versão do VLC em uso.

Quem já usa o VLC no computador converte sem gastar nada. A versão para iPhone fica fora deste artigo.

## Conversores online e o ficheiro grande

Um conversor online recebe o ficheiro nos seus servidores, converte-o e devolve-o. Num MKV grande, o ficheiro tem por isso de ser enviado primeiro por inteiro, e o conteúdo sai do dispositivo. Duas páginas deste site detalham esta troca: o artigo sobre [converter fotos HEIC sem as enviar para um servidor](/journal/your-photos-shouldnt-ride-the-elevator/){: hreflang="en"} (em inglês) e a [comparação com o CloudConvert](/pt/alternatives/cloudconvert/).

## Converter MKV para MP4 com o MediaKit

O MediaKit é uma app para iPhone e Mac que trabalha no dispositivo: o ficheiro não é enviado para lado nenhum. Abre ficheiros MKV diretamente, porque é a própria app que os desempacota, e reúne outras ferramentas de vídeo, apresentadas no artigo sobre [as ferramentas multimédia do MediaKit no Mac](/journal/every-media-tool-already-on-your-mac/){: hreflang="en"} (em inglês).

No Mac (macOS 14.6 ou posterior), clique com o botão direito no MKV, no Finder, escolha «Abrir com» e depois o MediaKit, que aparece nessa lista para os ficheiros MKV. Também se pode largar o ficheiro sobre o ícone do MediaKit no Dock.

No iPhone (iOS 17 ou posterior), abra o MediaKit e escolha o ficheiro na app Ficheiros.

Nos dois casos:

1. Escolha a ferramenta «Converter».
2. Escolha MP4 como formato de saída (também há MOV e M4V).
3. Para um remux, escolha «Manter o original (remux)» como codec. As outras opções, H.264, HEVC e ProRes, recodificam.
4. Toque ou clique em Executar e, se aparecer, leia o aviso sobre o som excluído.

Se o aviso indicar som excluído, essa faixa não está no MP4. Se era a única faixa de som, o ficheiro convertido fica sem som. Quando essa faixa faz falta, o melhor é guardar o original ou usar outra ferramenta.

A ferramenta «Comprimir vídeo» também aceita um MKV: as fontes MP4, MOV e M4V mantêm o contentor e as outras passam a MP4. Recodifica segundo uma predefinição de qualidade ou um tamanho alvo, o que serve para reduzir um ficheiro, mas não é uma conversão sem perdas. O artigo sobre [comprimir um vídeo para enviar por email](/journal/compress-a-video-for-email/){: hreflang="en"} (em inglês) explica o tamanho alvo em pormenor.

### O que é grátis

«Comprimir vídeo» é uma das cinco ferramentas que continuam grátis sem limite de tempo, um ficheiro de cada vez. «Converter» funciona grátis durante os 3 primeiros dias depois da instalação, com uma exportação por execução, e depois exige o Pro: {P_MONTHLY@mediakit}/mês, {P_YEARLY@mediakit}/ano ou {P_LIFETIME@mediakit} num único pagamento (preços da App Store de Portugal). Para quem converte um ficheiro por ano, um conversor grátis como o VLC pode chegar.

## Que método escolher

A primeira escolha é entre remux e recodificação. Para manter a imagem tal como está, é preciso uma opção que copie as faixas e confirmar que nenhuma faixa de som fica de fora. Para um ficheiro mais leve, recodifica-se e aceita-se alguma perda.

O VLC e o MediaKit não se excluem. O VLC é um leitor grátis que já lê o MKV tal como está, o que pode chegar se o objetivo for só ver o vídeo num computador. O MediaKit serve quando o ficheiro tem de acabar em MP4, MOV ou M4V num iPhone ou num Mac, por exemplo para o abrir nas apps da Apple.

| Necessidade | Opção |
|---|---|
| Um ficheiro, sem gastar nada, no computador | VLC |
| Um MKV sensível ou muito grande, sem o enviar | VLC ou MediaKit |
| Um remux sem recodificação, no Mac ou no iPhone | MediaKit, «Converter», «Manter o original (remux)» |
| Reduzir um ficheiro demasiado pesado | MediaKit, «Comprimir vídeo» |
