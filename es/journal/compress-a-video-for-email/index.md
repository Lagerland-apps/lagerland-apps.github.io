---
layout: journal
slug: compress-a-video-for-email
ref: /journal/compress-a-video-for-email/
permalink: /es/journal/compress-a-video-for-email/
translated_from: 2026-11-08
last_updated: 2026-11-19
date: 2026-11-19
title: "Cómo comprimir un vídeo para enviarlo por correo: límites de tamaño y cálculo de la tasa de bits"
seo:
  title: "Comprimir vídeo para enviar por correo: límites y cálculo"
  description: "Comprimir un vídeo para enviarlo por correo: Gmail admite 25 MB; Outlook e iCloud Mail, 20 MB. Qué margen dejar y qué tasa de bits usar, en iPhone o Mac."
  keywords:
    - comprimir video para enviar por correo
    - enviar video pesado por correo
    - comprimir video para enviar por gmail
    - video muy pesado para enviar por correo
    - tamaño maximo archivos adjuntos gmail
    - limite archivos adjuntos outlook
    - calcular bitrate video
    - mail drop icloud
lede: "Cada servicio de correo limita lo que deja adjuntar, y un vídeo llega enseguida a ese límite. Este artículo recoge los límites que publican Gmail, Outlook e iCloud Mail, explica por qué un límite de 25 MB no admite un archivo de 25 MB, detalla la cuenta que convierte un tamaño objetivo en una tasa de bits y muestra cómo MediaKit hace esa cuenta en iPhone o Mac sin subir el vídeo a ningún sitio."
quick_answer: "Para enviar un vídeo por correo, haz que el archivo pese menos que el límite de tu servicio, con margen. Una cuenta personal de Gmail admite 25 MB de adjuntos, la app Outlook 20 MB por mensaje en cuentas de internet como Outlook.com, iCloud Mail 20 MB y las cuentas de trabajo de Exchange 10 MB por defecto. Los adjuntos viajan codificados en Base64, que según Microsoft añade un 33 % aproximadamente, así que apunta a unas tres cuartas partes del límite: unos 18 MB para Gmail y unos 15 MB para Outlook o iCloud Mail. Para hallar la tasa de bits, multiplica el tamaño objetivo en megabytes por 8000 y divide entre la duración del vídeo en segundos: el resultado es la tasa total en kbps. Réstale la del audio (128 kbps es un valor habitual) y lo que queda es el presupuesto de vídeo. Baja la resolución hasta que ese presupuesto le sirva, mantén H.264 para que el vídeo se reproduzca en cualquier sitio y envía un enlace en lugar del archivo cuando el presupuesto se quede demasiado corto: Mail Drop admite hasta 5 GB."
excerpt: "Una referencia para enviar vídeo por correo: los límites de adjuntos que publican Gmail, Outlook, Exchange, iCloud Mail y Mail Drop, por qué la codificación Base64 obliga a apuntar a tres cuartas partes del límite, una tabla de tasas de bits para vídeos de 30 segundos a 5 minutos y cómo el modo «Tamaño objetivo» de MediaKit hace la misma cuenta en iPhone y Mac."
faq:
  - q: "¿Cuál es el tamaño máximo de un vídeo que se puede enviar por Gmail?"
    a: "Las cuentas personales de Gmail pueden enviar hasta 25 MB de adjuntos en un mismo mensaje, contados todos juntos; las cuentas de trabajo y de centros educativos siguen los límites que fija su administrador de Google Workspace. Por encima del límite, Gmail quita el adjunto y lo añade como enlace de Google Drive. Como los adjuntos viajan codificados en Base64, apunta a un vídeo de unos 18 MB si tiene que llegar como adjunto de verdad."
  - q: "¿Por qué se rechaza mi vídeo si pesa menos que el límite de adjuntos?"
    a: "Hay tres motivos habituales. Los adjuntos se codifican en Base64 antes de viajar, y la documentación de Exchange de Microsoft dice que eso añade un 33 % aproximadamente al mensaje, así que un archivo cercano al límite puede superarlo una vez codificado. Algunos límites cuentan el mensaje entero y no solo el adjunto; Microsoft indica que el límite de 20 MB de Outlook incluye el correo. Y el servidor del destinatario tiene su propio límite, que puede ser más bajo que el tuyo, como los 10 MB por defecto de Exchange."
  - q: "¿Cómo calculo la tasa de bits para un tamaño de archivo concreto?"
    a: "Multiplica el tamaño objetivo en megabytes por 8000 para obtener kilobits, divide entre la duración del vídeo en segundos para obtener la tasa de bits total en kbps y réstale la del audio. Lo que queda es la tasa de bits del vídeo. Para un objetivo de 18 MB y un vídeo de 90 segundos: 18 × 8000 = 144.000 kilobits, divididos entre 90 dan 1600 kbps, y al restar 128 kbps de audio quedan unos 1470 kbps para la imagen."
  - q: "¿H.264 o HEVC para un vídeo que voy a enviar por correo?"
    a: "H.264 en un MP4, salvo que sepas que el destinatario usa un dispositivo Apple reciente. Según Apple, el HEVC comprime mejor que el H.264, así que un archivo HEVC tiene mejor aspecto con el mismo tamaño, pero no controlas en qué dispositivo se abrirá el adjunto y el H.264 es el formato que casi cualquier dispositivo reproduce. Si el destinatario tiene un iPhone, un iPad o un Mac actuales, el HEVC da más calidad con el mismo tamaño."
  - q: "¿Qué hago si el vídeo es demasiado largo para comprimirlo lo bastante?"
    a: "Envía un enlace. Mail Drop, en la app Mail y en iCloud Mail, envía archivos de hasta 5 GB como un enlace de descarga que caduca a los 30 días, y Mail lo ofrece cuando un mensaje es demasiado grande para tu proveedor. Gmail cambia por su cuenta un adjunto demasiado grande por un enlace de Google Drive. Un vídeo de cinco minutos metido en 15 MB deja unos 270 kbps para el vídeo, una cuarta parte de lo que YouTube sugiere incluso para subidas en 360p."
  - q: "¿Puede MediaKit comprimir un vídeo hasta un tamaño de archivo concreto?"
    a: "Sí. «Comprimir vídeo» tiene un modo «Tamaño objetivo» que acepta un número en KB, MB o GB. MediaKit divide el objetivo entre la duración del vídeo, resta la tasa de bits de audio que hayas elegido, reserva un 3 %, codifica, mide el archivo que ha escrito y vuelve a codificar con una tasa corregida si se ha desviado del objetivo. Si aun así no consigue bajar del objetivo, se detiene con un error en lugar de entregarte un archivo demasiado grande. Funciona en el dispositivo, en iPhone y en Mac, y «Comprimir vídeo» es una de las cinco herramientas que siguen siendo gratis sin límite de tiempo después de los 3 primeros días."
mentioned_apps:
  - mediakit
read_time: "8 min de lectura"
---

A 8 Mbps, la tasa de bits que YouTube recomienda para subir vídeo en 1080p, un minuto de vídeo pesa 60 MB. Es más del doble de lo que Gmail deja adjuntar. Meter un vídeo en un correo es una cuenta sencilla: elige un tamaño objetivo por debajo del límite de tu servicio, calcula la tasa de bits que le corresponde y vuelve a codificar el vídeo con esa tasa. Este artículo da las cifras de cada paso y luego muestra cómo lo hace [MediaKit](/es/apps/mediakit/) en iPhone y Mac sin enviar antes el vídeo a ningún sitio.

## ¿Qué tamaño de vídeo se puede enviar por correo?

| Servicio | Límite | Qué cuenta | Si se supera |
|---|---|---|---|
| Gmail, cuenta personal | 25 MB | Todos los adjuntos del mensaje, sumados | Gmail sustituye el adjunto por un enlace de Google Drive |
| App Outlook, cuentas de internet como Outlook.com | 20 MB | Los adjuntos más el propio correo | Microsoft sugiere comprimir el archivo o compartir un enlace de almacenamiento en la nube |
| Exchange, cuentas de trabajo | 10 MB por defecto | El mensaje entero; los administradores pueden cambiarlo | Igual que arriba |
| iCloud Mail | 20 MB | Los mensajes entrantes y salientes | Hasta 5 GB con Mail Drop activado |
| Mail Drop (app Mail, iCloud Mail) | 5 GB | El mensaje con sus adjuntos; cada enlace caduca a los 30 días | Mail Drop no puede enviarlo |

Límites tal como los indicaba la página de ayuda de cada proveedor en julio de 2026: la [ayuda de Gmail](https://support.google.com/mail/answer/6584?hl=es), el [soporte de Microsoft](https://support.microsoft.com/es-es/office/enviar-archivos-grandes-con-outlook-8c698842-b462-4a4c-8d53-5c5dd04f77ef) y las páginas de Apple sobre los [límites de iCloud Mail](https://support.apple.com/es-es/102198) y sobre [Mail Drop](https://support.apple.com/es-es/108329). Los administradores pueden fijar límites más bajos en las cuentas de trabajo y de centros educativos, y el servidor que recibe el mensaje aplica el suyo. La [documentación de Exchange](https://learn.microsoft.com/en-us/exchange/mail-flow/message-size-limits){: hreflang="en"} (en inglés) de Microsoft dice que un mensaje debe cumplir los límites del remitente y del destinatario, así que manda el límite más bajo del recorrido.

## Por qué un límite de 25 MB no admite un archivo de 25 MB

El correo es un formato de texto. Antes de viajar como adjunto, un vídeo se codifica en Base64: cada tres bytes del archivo se convierten en cuatro caracteres de texto, repartidos en líneas de 76 caracteres como máximo ([RFC 2045, sección 6.8](https://www.rfc-editor.org/rfc/rfc2045#section-6.8){: hreflang="en"} (en inglés)). El mensaje que cruza la red pesa, por tanto, aproximadamente un tercio más que el archivo de tu disco.

Si un límite se mide antes o después de esa codificación depende del servicio, y las páginas de ayuda para el público general casi nunca lo dicen. La documentación de Exchange de Microsoft sí: Base64 añade un 33 % aproximadamente, así que un límite de mensaje de 64 MB supone en la práctica un máximo de unos 48 MB. Su página de Outlook añade que el límite de 20 MB incluye el correo, no solo el adjunto.

La regla de trabajo es, por tanto, tres cuartas partes del límite indicado:

| Límite indicado | Apunta a un archivo de unos |
|---|---|
| 25 MB (Gmail) | 18 MB |
| 20 MB (Outlook, iCloud Mail) | 15 MB |
| 10 MB (Exchange por defecto) | 7,5 MB |

Quedarse corto cuesta un poco de calidad de imagen. Pasarse supone un rebote, o un enlace donde querías un adjunto.

## Cómo calcular la tasa de bits que encaja

El tamaño de un archivo es la tasa de bits multiplicada por la duración. Haz la cuenta al revés:

1. **Pasa el objetivo a kilobits.** Megabytes × 8000, contando un megabyte como 1.000.000 de bytes.
2. **Divide entre la duración del vídeo en segundos.** El resultado es la tasa de bits total en kbps.
3. **Resta el audio.** 128 kbps es un ajuste estéreo habitual; 64 kbps sobra para la voz.
4. **Lo que queda es la tasa de bits del vídeo.** Deja un pequeño porcentaje de margen para la sobrecarga del propio contenedor.

Un vídeo de 90 segundos para Gmail: 18 MB × 8000 = 144.000 kilobits. Divididos entre 90 segundos, son 1600 kbps. Si quitas 128 kbps de audio, quedan unos 1470 kbps para la imagen.

La misma cuenta para duraciones habituales, restando antes 128 kbps de audio:

| Duración del vídeo | Archivo de 7,5 MB | Archivo de 15 MB | Archivo de 18 MB |
|---|---|---|---|
| 30 segundos | 1870 kbps | 3870 kbps | 4670 kbps |
| 1 minuto | 870 kbps | 1870 kbps | 2270 kbps |
| 2 minutos | 370 kbps | 870 kbps | 1070 kbps |
| 5 minutos | 70 kbps | 270 kbps | 350 kbps |

Las cifras están redondeadas a la baja.

## Qué resolución y qué códec elegir

Una tasa de bits solo es generosa o escasa en relación con el fotograma que tiene que llenar. Como referencia, los [ajustes de subida recomendados](https://support.google.com/youtube/answer/1722171?hl=es) de YouTube para las velocidades de fotogramas estándar piden 8 Mbps en 1080p, 5 Mbps en 720p, 2,5 Mbps en 480p y 1 Mbps en 360p. Son cifras altas, porque YouTube vuelve a codificar todo lo que recibe, pero enseñan con qué rapidez baja la necesidad al reducir el tamaño de imagen: el 1080p tiene 2,25 veces los píxeles del 720p.

Una regla aproximada: si tu presupuesto de vídeo queda muy por debajo de la mitad de la cifra de YouTube para la resolución del vídeo, baja un escalón de resolución. Con esa regla, un vídeo de un minuto en 18 MB (2270 kbps) queda mejor en 720p que en 1080p, y en 7,5 MB (870 kbps) le corresponde 480p o menos. Otros tres ajustes cambian el resultado:

- **Tasa de bits del audio.** En un vídeo de una persona hablando a cámara, 64 kbps en lugar de 128 kbps pasa la diferencia a la imagen. En un vídeo de cinco minutos en 15 MB, supone casi una cuarta parte más de tasa de bits de vídeo.
- **Velocidad de fotogramas.** Un vídeo de 60 fps reparte sus bits entre el doble de fotogramas que uno de 30 fps. Las cifras de YouTube para 48 a 60 fps son alrededor de un 50 % más altas que para 24 a 30.
- **Códec.** Apple dice que el [HEVC comprime mejor que el H.264](https://support.apple.com/es-es/116944), y los dispositivos Apple recientes lo reproducen. Pero no controlas dónde se abrirá el adjunto, y el H.264 en un MP4 se reproduce casi en cualquier sitio. La página de Apple también indica que sus dispositivos *podrían* convertir el HEVC a H.264 al compartirlo con un dispositivo que no pueda reproducirlo; para un archivo que ya has comprimido, es más sencillo elegir H.264 desde el principio.

## Cuándo conviene enviar un enlace

La fila de cinco minutos de la tabla es el punto en que comprimir deja de servir: 270 kbps son aproximadamente una cuarta parte de lo que YouTube sugiere para 360p. Cuando el presupuesto cae tan bajo, un enlace le sirve más al destinatario que un adjunto.

- **Mail Drop**, en la app Mail y en iCloud Mail, envía archivos de hasta 5 GB como un enlace de descarga que caduca a los 30 días. Mail lo ofrece cuando un mensaje es mayor de lo que permite tu proveedor.
- **Gmail** cambia por su cuenta un adjunto de más de 25 MB por un enlace de Google Drive.
- **Outlook** te remite a comprimir el archivo o a compartirlo desde el almacenamiento en la nube.

Con un enlace, el destinatario recibe el original con la calidad completa, y una copia queda en un servidor mientras el enlace siga activo.

## Cómo hacerlo con MediaKit

[MediaKit](/es/apps/mediakit/) hace la cuenta anterior en el dispositivo, en iPhone y en Mac, y nunca sube el vídeo. «Comprimir vídeo» es una de las cinco herramientas que siguen siendo gratis sin límite de tiempo después de los 3 primeros días, un archivo cada vez.

1. **Abre el vídeo.** En un Mac, arrástralo a la ventana. En iPhone, añádelo desde la app Fotos o la app Archivos, o envíalo desde el menú Compartir de otra app.
2. **Elige la herramienta «Comprimir vídeo»** y, en **Modo**, selecciona **«Tamaño objetivo»**.
3. **Escribe el tamaño objetivo** de la tabla de las tres cuartas partes, por ejemplo 18, con la unidad en MB. MediaKit cuenta un megabyte como 1.000.000 de bytes.
4. **Abre la sección Avanzado.** Ajusta **«Resolución máx.»** según la tabla de tasas de bits, deja **Códec** en H.264 para el correo y, si el vídeo es sobre todo voz, elige **«64 kbps (voz)»** en **«Tasa de bits de audio»**.
5. **Ejecuta la herramienta y comprueba el tamaño** del resultado antes de adjuntarlo.

En el modo «Tamaño objetivo», MediaKit hace por sí mismo los pasos del uno al cuatro de la cuenta: divide el objetivo entre la duración del vídeo, resta la tasa de bits de audio que has elegido y reserva un 3 %, codifica, mide el archivo que ha escrito y vuelve a codificar con una tasa corregida si se ha desviado del objetivo. Nunca te entrega un archivo por encima del objetivo: si no consigue bajar de él, se detiene con un error. Con un vídeo de origen en 4K o 1440p, «Resolución máx.» empieza en 1080p; para un objetivo pequeño, bájala.

Si ya usas HandBrake para esto, la [comparativa con HandBrake](/es/alternatives/handbrake/) explica en qué se diferencian, y la [comparativa con Compress Videos & Resize Video](/alternatives/compress-videos-resize-video/){: hreflang="en"} (en inglés) hace lo mismo en iPhone. Por qué el estudio mantiene este trabajo lejos de servidores ajenos es el tema de [un artículo anterior](/journal/your-photos-shouldnt-ride-the-elevator/){: hreflang="en"} (en inglés), y la caja de herramientas completa está en [este otro](/journal/every-media-tool-already-on-your-mac/){: hreflang="en"} (en inglés).
