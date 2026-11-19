---
layout: journal
slug: convertir-mkv-a-mp4
permalink: /es/journal/convertir-mkv-a-mp4/
local_only: true
last_updated: 2026-11-19
date: 2026-11-19
title: "Convertir MKV a MP4: remux sin pérdida, VLC, online o MediaKit"
seo:
  title: "Convertir MKV a MP4 sin perder calidad: VLC o MediaKit"
  description: "Convertir MKV a MP4 en Mac o iPhone: remux sin pérdida o recodificación, VLC gratis, convertidor online con archivos grandes o MediaKit en el dispositivo."
  keywords:
    - "convertir mkv a mp4"
    - "convertir mkv a mp4 con vlc"
    - "convertir mkv a mp4 archivos grandes"
    - "convertir mkv a mp4 gratis"
    - "convertir mkv a mp4 sin perder calidad"
    - "convertir mkv a mp4 online"
    - "convertir mkv a mp4 iphone"
lede: "Un archivo MKV es un contenedor, no un códec, así que convertirlo a MP4 puede reducirse a cambiar el envoltorio sin tocar la imagen. Este artículo explica la diferencia entre remux y recodificación, qué se puede hacer con VLC, qué implica un convertidor online con un archivo grande y cómo abre MediaKit un MKV en Mac y en iPhone, con los formatos de audio que pasan y los que se omiten."
quick_answer: "Para convertir un MKV a MP4 sin perder calidad hace falta un remux: el vídeo y el audio se copian a un contenedor MP4 sin recodificarlos, y eso solo funciona si los códecs son compatibles. VLC es gratis y convierte desde Media > Convert/Save, mientras que un convertidor online exige subir el archivo entero. MediaKit hace el remux en el dispositivo, en Mac y en iPhone: H.264, HEVC, AAC y AC-3 pasan tal cual, pero el audio DTS, E-AC-3 y MP3 se omite, con un aviso. «Convertir» es gratis durante los 3 primeros días y después requiere Pro; «Comprimir vídeo» sigue siendo gratis, pero recodifica el vídeo al pasarlo a MP4."
excerpt: "Convertir MKV a MP4: qué es un contenedor, remux o recodificación, VLC y los convertidores online con un archivo grande, y cómo abre y convierte MediaKit un MKV en Mac y en iPhone."
faq:
  - q: "¿Cómo convertir MKV a MP4 gratis?"
    a: "VLC es gratis y sabe convertir: su documentación describe un asistente que se abre con Media > Convert/Save. En MediaKit, «Comprimir vídeo» sigue siendo gratis pasados los 3 primeros días, con un archivo cada vez, y convierte un MKV en un MP4; recodifica, así que no es una conversión sin pérdida. «Convertir», que sí puede hacer un remux, es gratis durante los 3 primeros días y después requiere Pro."
  - q: "¿Se puede convertir MKV a MP4 sin perder calidad?"
    a: "Sí, cuando los códecs lo permiten: un remux copia el vídeo y el audio a un contenedor nuevo sin recodificarlos. MediaKit hace así el remux de los MKV con vídeo H.264 o HEVC y audio AAC o AC-3. En cambio, el audio DTS, E-AC-3 o MP3 de un MKV se omite, con un aviso."
  - q: "¿Cómo convertir MKV a MP4 con VLC?"
    a: "El wiki de VideoLAN, que avisa de que su página está desactualizada, describe un asistente que se abre con Media > Convert/Save, donde se elige un códec de vídeo, un códec de audio y un contenedor. Indica además que transcodificar puede ser muy lento y que no hace falta hacerlo cuando los flujos ya tienen el códec que quieres. La documentación actual de VLC 3.0 resume los pasos: Convert/Save, Add, archivo de destino, perfil de conversión y Start. Ninguna de las dos páginas dice qué perfil hace un remux; para saber qué códecs lleva el resultado, reprodúcelo y abre Tools > Codec Information."
  - q: "¿Sirve un convertidor online para un MKV muy grande?"
    a: "Un convertidor online trabaja en servidores ajenos, así que tienes que subir el MKV entero antes de convertirlo. Para un archivo grande, una conversión en el dispositivo evita esa subida: sirven VLC o MediaKit. Un remux además es mucho más rápido que recodificar, según la documentación de VLC."
  - q: "¿Cómo convertir MKV a MP4 en el iPhone?"
    a: "MediaKit abre archivos MKV en iPhone (iOS 17 o posterior) y ofrece la herramienta «Convertir» a MP4, MOV o M4V. Para un remux, elige «Mantener el original (remux)» en Códec: MediaKit copia entonces tal cual, sin recodificar, el vídeo H.264 o HEVC y el audio AAC o AC-3. El audio DTS, E-AC-3 o MP3 se omite, con un aviso."
  - q: "¿Cómo convertir MKV a MP4 en el Mac?"
    a: "En el Finder, abre el menú contextual del MKV, elige «Abrir con» y, en la lista, MediaKit, que aparece para los MKV. Elige «Convertir», el formato MP4 y «Mantener el original (remux)». MediaKit requiere macOS 14.6 o posterior. QuickTime Player no sirve para este paso: según Apple, no exporta vídeos como MP4."
mentioned_apps:
  - mediakit
read_time: "7 min de lectura"
---

Un archivo MKV es un contenedor: envuelve flujos de vídeo, audio y subtítulos. Por eso convertir un MKV a MP4 puede reducirse a cambiar el envoltorio, sin recodificar la imagen ni el sonido y sin perder calidad. Eso solo es posible cuando los códecs que van dentro encajan en el contenedor MP4, y ahí está la diferencia entre una conversión sin pérdida y otra que degrada el archivo. El artículo sigue ese hilo y después compara VLC, los convertidores online y [MediaKit](/es/apps/mediakit/), una app de Lagerland Apps, el estudio que publica este sitio.

## ¿Qué es un MKV y en qué se diferencia de un MP4?

El proyecto Matroska, que mantiene el formato, aclara en su web que el contenedor [no es un formato de compresión de vídeo ni de audio](https://www.matroska.org/what_is_matroska.html){: hreflang="en"} (en inglés). Lo describe como un envoltorio que puede contener varios flujos de audio, vídeo y subtítulos, de modo que una película entera cabe en un solo archivo. Entre los contenedores existentes de los que Matroska quiere ser la alternativa abierta cita MP4, que por tanto también es un contenedor.

Dos archivos pueden tener la misma imagen y el mismo sonido y distinguirse solo por el envoltorio. Cambiar de envoltorio no toca el contenido; cambiar de códec obliga a decodificar y volver a codificar.

## Por qué un MKV no siempre se abre en un iPhone o un Mac

Apple lo explica en una página de soporte sobre [archivos multimedia que no se abren](https://support.apple.com/es-es/102644): apps como Fotos, iMovie, Safari, Keynote y QuickTime Player funcionan con muchos formatos, pero los más antiguos o especializados pueden fallar si el dispositivo, el sistema o la app no los admiten. Entre las extensiones que sugiere buscar para encontrar otra app compatible figura .mkv, junto con .avi y .wmv. En el Mac, la misma página indica que el Finder puede mostrar «Tipo: Archivo de vídeo de Matroska»: selecciona el archivo y pulsa Comando-I.

Para el Mac, Apple añade un dato en su guía de QuickTime Player sobre [exportar vídeos](https://support.apple.com/es-es/guide/quicktime-player/qtp20e395859/mac): exporta en formato QuickTime (.mov) con H.264 o HEVC y no exporta vídeos como MP4. Si buscas cómo convertir MKV a MP4 en el Mac, esa app no es la vía.

## Remux o recodificación: cuándo no se pierde nada

La documentación de VLC define el [remux](https://docs.videolan.me/vlc-user/desktop/3.0/en/advanced/streaming/remuxing.html){: hreflang="en"} (en inglés) como tomar los flujos ya codificados y meterlos en otro contenedor. Lo distingue de la transcodificación, que sí recodifica. El remux solo cambia el contenedor, es más rápido porque no hay que codificar y deja el tamaño del archivo casi igual.

La misma página pone la condición: como no se recodifica, los códecs originales tienen que ser compatibles con el contenedor nuevo, y si no lo son el remux falla. En MediaKit, eso es la opción «Mantener el original (remux)» de la herramienta «Convertir». La ventaja es que no se recomprime nada: la imagen que sale es la que entró.

En MediaKit pasan tal cual el vídeo H.264 y HEVC y el audio AAC y AC-3. El audio DTS, E-AC-3 y MP3 de un MKV se omite, con un aviso: se conserva el vídeo, pero no esas pistas de audio. Si tu película lleva una pista DTS, lee el aviso de MediaKit.

Una recodificación, en cambio, genera una compresión nueva. Es lo que hacen la compresión a un tamaño objetivo o el cambio a otro códec. Conviene cuando el remux no es posible o cuando quieres un archivo más pequeño, pero, al recomprimir, puede perder calidad.

## Convertir MKV a MP4 con VLC

VLC es gratis. La [web de VideoLAN](https://www.videolan.org/vlc/){: hreflang="en"} (en inglés) lo presenta como un reproductor multimedia libre y de código abierto y cita MKV entre los formatos que reproduce. Para convertir, la [documentación de VLC 3.0](https://docs.videolan.me/vlc-user/desktop/3.0/en/basic/tipsandtricks/index.html){: hreflang="en"} (en inglés) da estos pasos: elige Media > Convert/Save, pulsa Add y selecciona el archivo, indica el archivo de destino, elige un perfil de conversión en la lista Profile y pulsa Start. La documentación consultada no detalla pasos aparte para Mac.

El [wiki de VideoLAN sobre transcodificación](https://wiki.videolan.org/Transcode/){: hreflang="en"} (en inglés) describe el mismo asistente, que pide un códec de vídeo, un códec de audio y un contenedor. Añade que no hace falta transcodificar si los flujos de entrada ya tienen el códec que quieres, y su autor cree, sin estar seguro, que la interfaz llama «keep the original track» a esa opción. El wiki avisa también de que la página está desactualizada y de que transcodificar puede ser muy lento.

Ninguna de las dos páginas dice qué perfil concreto de la lista hace un remux, así que no se puede asegurar que el asistente lo haga por defecto. Para saber qué códecs lleva tu archivo, la documentación de VLC propone reproducirlo y abrir Tools > Codec Information.

Si VLC ya forma parte de tus herramientas, hace el trabajo sin gastar nada y en el ordenador. Este artículo no cubre su uso en el iPhone.

## Convertidores online y archivos grandes

Un convertidor online recibe tu archivo en sus servidores, lo convierte y te lo devuelve. Con un MKV grande, eso significa subirlo entero antes de empezar, y el contenido sale de tu dispositivo. Antes de subir nada, mira los límites de tamaño y las condiciones que publica el servicio que elijas. Dos páginas de este sitio detallan ese compromiso: el artículo sobre [qué pasa con tus archivos en un convertidor online](/es/journal/your-photos-shouldnt-ride-the-elevator/) y la [comparativa con CloudConvert](/es/alternatives/cloudconvert/).

Para un archivo grande, el remux juega a favor: según la documentación de VLC, es mucho más rápido que transcodificar y no cambia casi el tamaño.

## Convertir MKV a MP4 con MediaKit

MediaKit es una app para iPhone y Mac que trabaja en el dispositivo: el archivo no se envía a ningún sitio. Abre los archivos MKV directamente, porque los desempaqueta ella misma. Sus otras herramientas de vídeo aparecen en el artículo sobre [las herramientas multimedia que ya trae el Mac](/journal/every-media-tool-already-on-your-mac/){: hreflang="en"} (en inglés).

En Mac (macOS 14.6 o posterior), abre el menú contextual del MKV en el Finder, elige «Abrir con» y selecciona MediaKit, que aparece en la lista para los MKV. También puedes soltar el archivo en el icono del Dock.

En iPhone (iOS 17 o posterior), abre MediaKit y elige el archivo desde la app Archivos.

En los dos casos:

1. Elige la herramienta «Convertir».
2. Elige MP4 como formato de salida (MOV y M4V también existen).
3. Para un remux, elige «Mantener el original (remux)» en Códec. H.264, HEVC y ProRes son las otras opciones, y recodifican.
4. Pulsa Ejecutar.

Si aparece un aviso de audio omitido, esa pista no estará en el MP4: según la página de MediaKit, la app descarta el audio DTS, E-AC-3 y MP3 al abrir un MKV. Si esa pista te importa, conserva el original o usa otra herramienta.

«Comprimir vídeo» también acepta un MKV: los orígenes MP4, MOV y M4V conservan su contenedor y los demás pasan a MP4. Recodifica según una calidad o un tamaño objetivo: sirve para aligerar un archivo, pero no es una conversión sin pérdida. El artículo sobre [comprimir un vídeo para enviarlo por correo](/es/journal/compress-a-video-for-email/) detalla el tamaño objetivo, y la [comparativa con HandBrake](/es/alternatives/handbrake/) explica en qué se diferencian las dos opciones.

### Qué es gratis

«Comprimir vídeo» es una de las cinco herramientas que siguen siendo gratis sin límite de tiempo, con un archivo cada vez. «Convertir» funciona gratis durante los 3 primeros días tras instalar la app, con una exportación por ejecución, y después requiere Pro: {P_MONTHLY@mediakit}/mes, {P_YEARLY@mediakit}/año o {P_LIFETIME@mediakit} en un solo pago, según los precios del App Store de España. Si solo vas a convertir un archivo al año, te basta un convertidor gratuito como VLC.

## ¿Qué método elegir?

Decide primero entre remux y recodificación. Si quieres conservar la imagen tal cual, busca una opción que copie los flujos y comprueba que no omita ninguna pista de audio. Si quieres un archivo más ligero, lo normal es recodificar, y entonces puede haber pérdida de calidad.

VLC y MediaKit no se excluyen. VLC sigue siendo un reproductor gratis que ya lee el MKV tal cual, y puede bastar si solo quieres verlo en un ordenador. MediaKit sirve cuando el archivo tiene que acabar en MP4, MOV o M4V en un iPhone o en un Mac, por ejemplo para abrirlo en las apps de Apple.

| Necesidad | Vía |
|---|---|
| Un archivo, sin gastar, en el ordenador | VLC |
| Un MKV privado o muy grande, sin subirlo | VLC o MediaKit |
| Un remux sin recodificar, en Mac o iPhone | MediaKit, «Convertir», «Mantener el original (remux)» |
| Aligerar un archivo demasiado pesado | MediaKit, «Comprimir vídeo» |
