---
layout: journal
slug: descomprimir-rar-mac
permalink: /es/journal/descomprimir-rar-mac/
local_only: true
last_updated: 2026-11-19
date: 2026-11-19
title: "Descomprimir RAR en Mac y iPhone: opciones gratis y de pago"
seo:
  title: "Descomprimir RAR en Mac: opciones gratis y de pago"
  description: "Cómo descomprimir un RAR en Mac o iPhone: lo que documenta Apple, RAR for macOS en la Terminal, The Unarchiver, que es gratuita, Keka y MediaKit."
  keywords:
    - "descomprimir rar mac"
    - "descomprimir rar mac gratis"
    - "descomprimir rar macbook"
    - "abrir rar mac"
    - "abrir rar en mac gratis"
    - "winrar mac"
    - "the unarchiver mac"
lede: "Te han enviado un archivo .rar y quieres ver lo que lleva dentro. Las páginas de soporte de Apple solo hablan del ZIP, así que la vía práctica es una app que lea RAR. Estas son las opciones para Mac y iPhone, con lo que pide y lo que cuesta cada una."
quick_answer: "Para descomprimir un RAR en Mac, usa una app que lea ese formato, porque las páginas de soporte de Apple que hemos consultado solo describen el ZIP. The Unarchiver se presenta en su web como gratuita y con soporte de RAR, y Keka incluye el RAR entre los formatos que extrae. La web de WinRAR (RARLAB) solo ofrece para macOS RAR for macOS, de línea de comandos y en versión de prueba. MediaKit extrae RAR4 y RAR5 en Mac y iPhone sin subir el archivo. Su herramienta «Extraer» funciona sin pagar durante los 3 primeros días, con una exportación por ejecución, y después requiere Pro. Un sitio de extracción en línea, en cambio, recibe el archivo en sus servidores."
excerpt: "Descomprimir RAR en Mac y iPhone: lo que documenta Apple, lo que ofrece RARLAB para macOS, The Unarchiver y Keka, la extracción en línea y cómo abre MediaKit un RAR sin subirlo."
faq:
  - q: "¿Cómo descomprimir un RAR en Mac?"
    a: "Con una app que lea RAR. La página de Apple sobre el Mac explica el doble clic en un archivo .zip y no menciona el RAR. The Unarchiver y Keka anuncian el RAR en sus webs. MediaKit también extrae RAR4 y RAR5: en el Finder, haz clic en el archivo con la tecla Control pulsada, selecciona «Abrir con» y elige MediaKit. Después usa la herramienta «Extraer»."
  - q: "¿Hay WinRAR para Mac?"
    a: "No con interfaz gráfica. En la página de descargas de RARLAB, lo único para macOS es RAR for macOS (ARM64), solo de línea de comandos y en versión de prueba, así que se usa desde la Terminal. WinRAR, con interfaz gráfica, figura en la misma lista, pero ninguna versión con interfaz gráfica es para macOS."
  - q: "¿Cómo abrir un archivo RAR en iPhone?"
    a: "La página de Apple sobre la app Archivos explica cómo abrir un ZIP con un toque y no menciona el RAR. MediaKit extrae RAR4 y RAR5 en iPhone con iOS 17 o posterior: abre la app y elige el archivo desde Archivos, o envíaselo desde el menú de compartir, y usa la herramienta «Extraer»."
  - q: "¿Se puede abrir un RAR en iPad?"
    a: "Con MediaKit, no: la app no tiene versión para iPad. Las instrucciones de Apple para la app Archivos del iPad tratan el ZIP y no mencionan el RAR, así que en el iPad hace falta otra app que anuncie ese formato."
  - q: "¿Hay alguna forma gratuita de descomprimir un RAR en Mac?"
    a: "Sí. The Unarchiver dice en su web que es gratuita, sin compras dentro de la app, y que lee RAR. Keka incluye el RAR entre los formatos que extrae; se descarga desde su web, que propone donar o comprarla en el App Store. RAR for macOS, de RARLAB, se ofrece en versión de prueba y solo funciona en línea de comandos. En MediaKit, «Extraer» funciona sin pagar durante los 3 primeros días, con una exportación por ejecución, y después requiere Pro."
  - q: "¿MediaKit abre RAR con contraseña?"
    a: "No. Si el RAR está protegido con contraseña, MediaKit lo avisa y no lo extrae. Tampoco crea archivos RAR; solo extrae RAR4 y RAR5. Según su web, The Unarchiver sí admite el RAR cifrado."
mentioned_apps:
  - mediakit
read_time: "5 min de lectura"
---

Las páginas de soporte de Apple que hemos consultado para este artículo describen el ZIP, y ninguna habla del RAR. Para un RAR en el Mac o en el iPhone, lo más sencillo es una app que lea ese formato. Repasamos lo que ofrece RARLAB para macOS, dos apps para Mac, la extracción en línea y [MediaKit](/es/apps/mediakit/), la app de Lagerland Apps, el estudio que publica este sitio.

## Qué describen las páginas de soporte de Apple

En el Mac, la página [Comprimir y descomprimir archivos y carpetas en el Mac](https://support.apple.com/es-es/guide/mac-help/mchlp2528/mac) (consultada el 19 de noviembre de 2026) explica que un archivo .zip se descomprime con un doble clic. Solo habla de archivos .zip.

En el iPhone, la página [Crear o abrir archivos ZIP en el iPhone, iPad o Apple Vision Pro](https://support.apple.com/es-es/102532) describe la app Archivos: al tocar un archivo ZIP, se crea una carpeta con lo que contiene. Da los mismos pasos para el iPad y tampoco cita otro formato.

Ninguna de las dos dice que el RAR esté admitido ni que no lo esté: solo describen el ZIP. Si el doble clic no abre tu RAR, necesitas una app que lo haga.

## WinRAR en Mac: qué publica RARLAB

Según su [página de inicio](https://www.rarlab.com/){: hreflang="en"} (en inglés), WinRAR, de RARLAB, abre archivos RAR y ZIP y crea archivos en esos dos formatos. La [página de descargas](https://www.rarlab.com/download.htm){: hreflang="en"} (en inglés) lista WinRAR, con interfaz gráfica y línea de comandos, en versión de prueba. Para macOS solo aparece RAR for macOS, para ARM64, también de prueba y solo de línea de comandos. Ninguna versión con interfaz gráfica es para macOS, así que en un Mac la herramienta de RARLAB se usa desde la Terminal.

La [página de extras](https://www.rarlab.com/rar_add.htm){: hreflang="en"} (en inglés) incluye un UnRAR gratuito de línea de comandos para Mac OS X de 64 bits, pero en la sección de aportaciones de usuarios. RARLAB avisa ahí de que esos archivos pueden partir de código antiguo al que le faltan correcciones importantes de errores y de seguridad, y de que no da soporte a los UnRAR de esa lista que no son para Windows. Según la misma página, los UnRAR oficiales para OS X van dentro de los paquetes de RAR y WinRAR. Allí publica también la descripción del formato RAR 5.0.

## The Unarchiver y Keka, dos apps para Mac

Dos apps para Mac indican en sus propias webs que extraen RAR:

- The Unarchiver: su [web](https://theunarchiver.com/){: hreflang="en"} (en inglés) la presenta como gratuita, sin compras dentro de la app, y dice que el soporte de RAR incluye el cifrado y los archivos de varios volúmenes. Pide macOS 10.13 o posterior.
- Keka: su [web en español](https://www.keka.io/es/) incluye el RAR entre los formatos que extrae. Ofrece la descarga directa y propone donar o comprar la app en el App Store. Pide Mac OS X 10.10 o posterior.

Para un RAR de vez en cuando en el Mac, cualquiera de las dos puede bastar. The Unarchiver anuncia además un caso que MediaKit rechaza, el RAR cifrado (más abajo). No hemos probado estas apps para el artículo: lo que dice esta sección sale de sus webs.

## Extraer un RAR en línea

Un sitio de extracción en línea recibe el archivo en sus servidores, lo procesa allí y te devuelve los ficheros. Para eso tienes que subir el archivo entero, y su contenido sale de tu dispositivo. Aquí no valoramos ningún servicio en concreto. Si el RAR guarda documentos personales, merece la pena pensarlo antes de subirlo.

El recorrido de un archivo por un convertidor en línea, paso a paso, está en el artículo sobre [convertir HEIC a JPG sin subir la foto](/es/journal/your-photos-shouldnt-ride-the-elevator/), y la [comparativa con CloudConvert](/es/alternatives/cloudconvert/) pone un servicio en línea frente a MediaKit.

## Descomprimir un RAR con MediaKit

MediaKit es una app para iPhone y Mac cuyas herramientas funcionan en el dispositivo, sin subir el archivo a ningún sitio. Su herramienta «Extraer» abre archivos ZIP, TAR, TAR.GZ, GZIP, XZ y BZIP2, y también extrae RAR4 y RAR5. Antes de extraer te enseña el contenido, y pone límites contra el path traversal y las bombas zip.

**En el Mac** (macOS 14.6 o posterior): en el Finder, haz clic en el RAR con la tecla Control pulsada, selecciona «Abrir con» y elige MediaKit. También puedes soltar el archivo sobre el icono de MediaKit en el Dock.

**En el iPhone** (iOS 17 o posterior): abre MediaKit y elige el archivo desde la app Archivos, o envíaselo desde el menú de compartir.

Después, en los dos:

1. Elige la herramienta «Extraer».
2. Revisa el contenido que muestra.
3. Haz clic en Ejecutar en el Mac, o tócalo en el iPhone.

Lo que MediaKit no hace:

- No crea archivos RAR, solo los extrae. Para crear archivos comprimidos ofrece ZIP, TAR, TAR.GZ, GZIP, XZ y BZIP2.
- Rechaza los RAR cifrados. Si tu archivo tiene contraseña, usa una app cuya web anuncie ese caso, como The Unarchiver.
- No tiene versión para iPad.

Para el iPhone y el iPad, nuestra [comparativa con iZip](/es/alternatives/izip/) trata otra app de archivos comprimidos, que también funciona en iPad. Y si quieres ver qué más hace MediaKit, el artículo [por qué el Mac ya traía todas las herramientas multimedia](/journal/every-media-tool-already-on-your-mac/){: hreflang="en"} (en inglés) recorre sus herramientas.

### Qué es gratis en MediaKit

«Extraer» no está entre las cinco herramientas que siguen siendo gratis sin límite de tiempo. Durante los 3 primeros días tras instalar la app funciona sin pagar, con una exportación por ejecución. Después requiere Pro: {P_MONTHLY@mediakit}/mes, {P_YEARLY@mediakit}/año o {P_LIFETIME@mediakit} de por vida, según los precios del App Store de España. Si solo tienes un RAR que abrir en el Mac, The Unarchiver, gratuita según su web, puede bastarte.

## ¿Qué opción elegir?

| Necesidad | Opción |
|---|---|
| Un RAR de vez en cuando en el Mac, con interfaz | The Unarchiver o Keka |
| Te manejas en la Terminal | RAR for macOS, de RARLAB |
| Un RAR cifrado | Una app cuya web anuncie el cifrado, como The Unarchiver |
| Un RAR en el iPhone, sin subirlo | MediaKit, herramienta «Extraer» |
| Un archivo delicado, sin enviarlo a ningún sitio | Una app local antes que un sitio en línea |

Para un uso ocasional en el Mac, The Unarchiver o Keka. MediaKit encaja si también abres RAR en el iPhone o si vas a usar sus otras herramientas.
