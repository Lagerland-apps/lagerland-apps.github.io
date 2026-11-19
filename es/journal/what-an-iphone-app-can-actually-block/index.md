---
layout: journal
slug: what-an-iphone-app-can-actually-block
ref: /journal/what-an-iphone-app-can-actually-block/
permalink: /es/journal/what-an-iphone-app-can-actually-block/
translated_from: 2026-11-08
last_updated: 2026-11-19
date: 2026-11-19
title: "Cómo bloquear una app en iPhone: lo que una app de bloqueo puede hacer de verdad y lo que iOS no le deja"
seo:
  title: "Cómo bloquear una app en iPhone: qué permite iOS y qué no"
  description: "Cómo bloquear una app en iPhone y cómo funcionan las apps de bloqueo: los tres frameworks de Apple, los tokens opacos y por qué todas se pueden saltar."
  keywords:
    - "como bloquear una app en iphone"
    - "como bloquear una app en iphone para no usarla"
    - "bloquear una aplicacion en iphone"
    - "puedo bloquear una aplicacion en iphone"
    - "se puede bloquear instagram en iphone"
    - "family controls"
lede: "En el iPhone, ninguna app de terceros bloquea nada por sí misma. Le pide a iOS que lo haga, con tres frameworks de Apple cuyos límites son claros y están publicados. Esos límites explican por qué tu app de bloqueo no puede nombrar las apps que has bloqueado, por qué las notificaciones siguen llegando y por qué la respuesta sincera a «¿se puede saltar?» es siempre que sí."
quick_answer: "Una app se bloquea en el iPhone con Tiempo de uso, incluido en iOS, o con una app de bloqueo de terceros. Ninguna app de terceros bloquea nada por sí misma: se lo pide a iOS, con tres frameworks de Apple. FamilyControls aporta la autorización y el selector de apps del sistema, ManagedSettings dibuja el escudo sobre las apps que eliges y DeviceActivity gestiona los horarios y los umbrales de uso. El selector devuelve tokens opacos, así que la app de bloqueo nunca sabe qué apps has elegido. Puede proteger con un escudo apps, categorías enteras y dominios web en Safari. No puede silenciar las notificaciones, llegar a tus otros dispositivos ni seguir activa si retiras su autorización en Ajustes. Todo bloqueo instalado en el propio iPhone es fricción, y la única medida sincera es cuánto se tarda en salir."
excerpt: "Una app de terceros para iPhone no puede ver lo que abres, ejecutarse de forma continua en segundo plano ni dibujar nada sobre otra app. Este artículo explica qué permite la API de Tiempo de uso, qué implica el diseño con tokens opacos para la privacidad y para el producto, y todas las formas de salir de un escudo, ordenadas por esfuerzo."
faq:
  - q: "¿Se puede bloquear Instagram en el iPhone con una app?"
    a: "Sí. Con el framework ManagedSettings de Apple, una app de terceros puede proteger con un escudo la app de Instagram, de modo que al tocar su icono aparece una pantalla que impide abrirla, y puede proteger instagram.com en Safari si incluyes el contenido web en la selección. Lo que no puede hacer es impedir que lleguen las notificaciones de Instagram, bloquear Instagram en tu iPad o tu portátil ni impedir que retires la autorización de la app de bloqueo en Ajustes, lo que quita todos los escudos de golpe."
  - q: "¿Existe una app de bloqueo que no se pueda saltar?"
    a: "No en tu propio iPhone. Apple deja a propósito la revocación en manos del usuario: siempre puedes retirar la autorización de Family Controls en Ajustes, lo que invalida los tokens de la app de bloqueo y quita todos los escudos. Una app de bloqueo puede impedir que la borres y añadir fricción, como un cálculo o una espera, pero no puede hacerse permanente. El único caso difícil es un dispositivo cuyo código de Tiempo de uso tiene otra persona, y eso es control parental, no limitar tu propio uso."
  - q: "¿Qué es la API Family Controls?"
    a: "FamilyControls es el framework de Apple que controla el acceso a toda la API de Tiempo de uso. Hace dos cosas: pide autorización al usuario, en modo individual (para limitar tu propio uso) o en modo hijo (un progenitor de En familia que gestiona a un menor), y presenta FamilyActivityPicker, la interfaz del sistema donde el usuario elige apps, categorías y dominios web. Devuelve una FamilyActivitySelection formada por tokens opacos. Para distribuirlo en el App Store hace falta un permiso restringido (entitlement) que Apple concede previa solicitud."
  - q: "¿Funcionan las apps de bloqueo sin conexión a internet?"
    a: "Las de Family Controls, sí. El estado de los escudos vive en un ManagedSettingsStore local y lo aplica el propio iOS, así que el modo Avión no cambia nada. Los filtros de contenido por DNS o VPN son el caso contrario: solo ven el tráfico de red, así que no hacen nada contra una app que funciona sin conexión ni contra contenido que ya está en la caché del dispositivo, y desactivar el perfil en Ajustes los quita sin más. Funcionar sin conexión es una de las diferencias más claras entre los dos enfoques."
  - q: "¿Puede una app de bloqueo ver qué apps he bloqueado?"
    a: "No, y lo impone iOS: no es solo una promesa del desarrollador. El selector de Apple devuelve tokens, que la propia documentación de Apple describe como representaciones que no revelan la identidad de una actividad. La app de bloqueo guarda un token, se lo devuelve a ManagedSettings para aplicar un escudo y nunca recibe un identificador de bundle ni un nombre visible. No puede registrar tu selección, venderla ni filtrarla, porque nunca la tuvo."
  - q: "¿Tiempo de uso o una app de bloqueo de terceros?"
    a: "Tiempo de uso, incluido en iOS, es gratis, cubre todos los dispositivos con la misma cuenta de Apple cuando «Compartir entre dispositivos» está activado y puede bloquearse con un código que tenga otra persona. Su punto débil es la salida: tu propio código, o el botón que te deja ignorar el límite. Una app de bloqueo de terceros usa el mismo mecanismo de iOS para bloquear, pero puede cambiar lo que cuesta desbloquear y dibujar un escudo mucho más útil. A muchas personas les va mejor con las dos a la vez."
mentioned_apps:
  - earnlock
read_time: "15 min de lectura"
---

Pregunta a casi cualquiera cómo funciona una app de bloqueo en el iPhone y te dará alguna versión de esto: la app se queda en segundo plano, vigila lo que abres y cierra la puerta de golpe cuando ve Instagram.

Nada de eso es posible. Una app de iOS de terceros no puede ver qué apps abres, no puede ejecutarse de forma continua en segundo plano para vigilar una y no puede dibujar ni un solo píxel sobre otra app. Todas las apps de bloqueo del App Store le piden a iOS que bloquee por ellas, con tres frameworks que Apple presentó en 2021 y ha ido ampliando poco a poco.

Ese detalle decide qué puede hacer tu app de bloqueo, qué no hará nunca por mucho que pagues y cómo se sale exactamente, que es la parte que nadie pone en las capturas del App Store. Los pasos con Tiempo de uso, del primer ajuste al código, están en nuestra guía para [limitar el tiempo de pantalla en el iPhone](/es/guides/limitar-tiempo-de-pantalla-iphone/).

## ¿Qué bloquea de verdad una app en un iPhone?

Tres frameworks, que juntos forman la API de Tiempo de uso (Screen Time API), presentada en la sesión de la WWDC21 [Meet the Screen Time API](https://developer.apple.com/videos/play/wwdc2021/10123/){: hreflang="en"} (en inglés). Un cuarto, ManagedSettingsUI, solo controla el aspecto de la pantalla que bloquea la app. En esta página la llamamos «escudo» (shield, en la documentación de Apple): es lo que aparece en lugar de la app.

| Framework | Su única función | Los tipos que se usan en la práctica | Lo que no puede hacer |
|---|---|---|---|
| [FamilyControls](https://developer.apple.com/documentation/familycontrols){: hreflang="en"} (documentación en inglés) | Conseguir el permiso y dejar que el usuario elija apps | `AuthorizationCenter`, [`FamilyActivityPicker`](https://developer.apple.com/documentation/familycontrols/familyactivitypicker){: hreflang="en"}, [`FamilyActivitySelection`](https://developer.apple.com/documentation/familycontrols/familyactivityselection){: hreflang="en"} | Decirle a tu código qué apps se eligieron |
| [ManagedSettings](https://developer.apple.com/documentation/managedsettings){: hreflang="en"} | Aplicar la restricción | `ManagedSettingsStore`, [`ShieldSettings`](https://developer.apple.com/documentation/managedsettings/shieldsettings){: hreflang="en"} (`.applications`, `.applicationCategories`, `.webDomains`), [`ApplicationSettings`](https://developer.apple.com/documentation/managedsettings/applicationsettings){: hreflang="en"} (`denyAppRemoval`) | Sobrevivir a la autorización que lo creó |
| [DeviceActivity](https://developer.apple.com/documentation/deviceactivity){: hreflang="en"} | Todo lo relacionado con el tiempo | `DeviceActivityCenter`, `DeviceActivitySchedule`, [`DeviceActivityEvent`](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent){: hreflang="en"}, `DeviceActivityMonitor` | Ejecutar tu código de forma continua: la extensión solo se despierta con eventos |
| [ManagedSettingsUI](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration){: hreflang="en"} | Dar estilo al escudo | `ShieldConfigurationDataSource`, `ShieldActionDelegate` | Nada que no sea dibujar un título, un subtítulo, un icono y hasta dos botones |

En una app real, la secuencia es corta. Se pide la autorización con `AuthorizationCenter.shared`, en modo `.individual` para limitar tu propio uso o en modo `.child` para un progenitor de En familia. Se muestra el selector. Lo que devuelve se guarda en un `ManagedSettingsStore` como `store.shield.applications`. Se registra un horario con `DeviceActivityCenter` y se deja que iOS despierte la extensión `DeviceActivityMonitor` al comienzo y al final de los intervalos y al alcanzar los umbrales de uso, para que modifique el almacén.

Dos límites prácticos hacen la categoría más pequeña de lo que parece. La capacidad Family Controls añade el permiso (entitlement) [`com.apple.developer.family-controls`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls){: hreflang="en"} (en inglés), y para distribuir en el App Store una app que lo use hay que pedírselo a Apple. Y la extensión `DeviceActivityMonitor` no es un proceso residente (daemon): iOS la despierta, le da un breve intervalo de tiempo y la suspende. Todo lo que una app de bloqueo dice hacer «de forma continua» ocurre en los momentos que elige Apple.

## Por qué la app de bloqueo nunca sabe qué apps has elegido

De todas las decisiones de diseño de la API, esta es la que tiene más consecuencias.

La interfaz para elegir apps es `FamilyActivityPicker`, y es de Apple, no del desarrollador. Se dibuja fuera del proceso de la app, muestra tus apps instaladas y devuelve una `FamilyActivitySelection` con conjuntos de tokens: `ApplicationToken`, `ActivityCategoryToken`, `WebDomainToken`. La documentación de Apple sobre [`Token`](https://developer.apple.com/documentation/managedsettings/token){: hreflang="en"} (en inglés) lo describe como una representación de una app o un sitio web que no revela su identidad, y la página de `ApplicationToken` dice que el objetivo es restringir y filtrar apps sin acceder a datos personales del usuario.

Así que una app de bloqueo guarda un bloque opaco, que le devuelve a ManagedSettings para activar un escudo. Nunca recibe un identificador de bundle ni un nombre visible, y no hay forma de averiguar a qué app corresponde el token. Además, un token solo significa algo para la app que lo recibió, y deja de funcionar en cuanto retiras la autorización en Ajustes, porque la revocación invalida los tokens de la app junto con su permiso.

Para la privacidad, esto significa que una app de tiempo de pantalla no puede, físicamente, registrar que has bloqueado Grindr, una app de inversión o la app favorita de tu ex. No ha prometido no hacerlo: no puede. Es privacidad por construcción, y la garantía de este tipo más fuerte de todas las categorías en las que he publicado apps.

Para el producto es un impuesto real, que paga todo desarrollador de esta categoría:

- No puedes ofrecer, al empezar, un «bloquea de un toque a los sospechosos habituales», porque no puedes nombrarlos.
- No puedes decirle al usuario, en tus propios textos, qué apps están protegidas con un escudo en este momento.
- No puedes comprobar con tus propios datos que un usuario haya seleccionado algo, así que las consultas de soporte («no bloquea nada») acaban en sesiones guiadas de capturas de pantalla.

Esa decisión la tomó Apple, no el desarrollador, y creo que acertó.

## ¿Qué enfoque bloquea qué?

Cinco enfoques se venden como «bloqueo de apps» y interceptan en capas completamente distintas. Aquí importa menos el precio que el lugar que ocupa cada uno en la pila.

| Enfoque | Qué bloquea | Qué no puede bloquear | Cómo se salta | Funciona sin conexión | A quién le sirve de verdad |
|---|---|---|---|---|---|
| **Tiempo de uso, incluido en iOS** ([guía de Apple](https://support.apple.com/es-es/guide/iphone/iphbfa595995/ios)) | Límites de tiempo por app y por categoría («Límites de tiempo» en iOS 27, «Límites de uso de apps» en iOS 26 y versiones anteriores), horas sin pantalla («Horario de tiempo de uso» en iOS 27, «Tiempo de inactividad» en iOS 26 y versiones anteriores), clasificaciones de contenido, contenido web; se sincroniza entre tus dispositivos con «Compartir entre dispositivos» | Nada más allá de las categorías de Apple; ninguna condición de desbloqueo personalizada | Tu propio código, o el botón que te deja ignorar el límite | Sí | A cualquiera que aún no lo haya probado: es gratis y cubre también el Mac y el iPad |
| **App de escudo con Family Controls** ([Opal](/es/alternatives/opal/), [one sec](/es/alternatives/one-sec/), [ScreenZen](/es/alternatives/screenzen/), [Jomo](/alternatives/jomo/){: hreflang="en"} (en inglés), [EarnLock](/es/apps/earnlock/)) | Cualquier app o categoría de Apple que selecciones en este iPhone, además de dominios web de Safari en las apps que lo admiten | Las notificaciones, otros dispositivos y todo lo que ocurra después de retirar la autorización | La salida de emergencia que traiga la app y, después, retirar la autorización en Ajustes | Sí, porque el estado es local y lo aplica iOS | A quien quiere una condición de desbloqueo distinta de «esperar» o «escribir tu código» |
| **Filtro de contenido por DNS o VPN** ([NetworkExtension](https://developer.apple.com/documentation/networkextension){: hreflang="en"} (en inglés)) | Dominios y patrones de tráfico en todo el sistema, también de apps que no has seleccionado | Cualquier cosa por datos móviles si el perfil está desactivado, el DNS cifrado dentro de una app o un servicio que comparte CDN con algo que necesitas | Desactivar la VPN en Ajustes, unos tres toques | No, es por definición un mecanismo de red | Para bloquear clases enteras de contenido (anuncios, sitios para adultos), no una app concreta |
| **Dispositivo aparte o caja con cierre** (móvil básico, caja fuerte con temporizador, la etiqueta NFC de Brick) | Todo lo que hay en el dispositivo que has dejado | Cualquier otra pantalla del edificio | Recuperar físicamente el objeto | Sí | A quien tiene un problema de una hora en un sitio: sesiones de escritura, cenas, sueño |
| **Escala de grises y fricción** («Filtros de color», modos de concentración, apps fuera de la pantalla de inicio) | Nada; solo hace el móvil más apagado y más lento de alcanzar | Cualquier cosa, si de verdad quieres usarla | Tres toques en Ajustes, o Spotlight | Sí | A quien se distrae más que a quien tiene una compulsión: quien abre una app sin motivo y se queda 40 minutos |

Dos notas sobre la tabla. El filtro DNS es la única fila que toca apps que no has incluido en la lista, lo que lo convierte en la herramienta adecuada para bloquear contenido para adultos y en la equivocada para «mantenme fuera de X entre las 9 y las 17». Y las propias normas de revisión de Apple limitan la fila de la VPN: la [directriz 5.4 de las App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/){: hreflang="en"} (en inglés) exige que las apps de VPN usen `NEVPNManager` y procedan de un desarrollador inscrito como organización, y el permiso de filtro de contenido se concede caso por caso, por eso hay tan pocas.

## ¿Puede una app bloquear Instagram en el iPhone?

Sí, con tres matices que importan más que el sí.

**La app, del todo.** Selecciona Instagram en el selector, pon el token en `store.shield.applications` y al tocar el icono aparece un escudo en lugar de abrirse la app. La app no se abre en segundo plano, no se actualiza y no obtiene sus cinco segundos.

**El sitio web, casi.** `ShieldSettings.webDomains` cubre Safari. Seleccionar el contenido web en el selector es lo que hace que instagram.com en Safari se comporte igual que la app. La cobertura en navegadores de terceros y en las vistas web dentro de las apps es menos predecible, y yo no montaría un plan sobre ella.

**Las notificaciones, no.** Un escudo detiene un arranque, no la entrega de avisos. Si lo que te atrae es un globo y un banner, el escudo arregla la mitad equivocada del bucle, y un modo de concentración es mejor herramienta, o las dos juntas.

**Tus otras pantallas, tampoco.** El almacén es local del dispositivo. Tu iPad, tu Mac y el portátil del trabajo quedan intactos. Family Controls no existe en macOS en una forma que admita este mecanismo, así que cualquier app de escudo que cubra también el Mac usa allí otro mecanismo.

## ¿Existe una app de bloqueo que no se pueda saltar?

No, no en un dispositivo que es tuyo y que controlas, y es deliberado. Si una app de terceros pudiera restringir tu móvil de forma permanente, la primera app maliciosa que se publicara dejaría inservibles muchos móviles, así que Apple mantiene la salida en tus manos.

Siempre hay una salida. La pregunta útil es cuánto se tarda y si el esfuerzo va a parar a algo útil. Esta es la escalera, de la más barata a la más cara.

| Salida | Cuánto se tarda, aproximadamente | Qué te cuesta | ¿Puede saberlo la app? |
|---|---|---|---|
| Botón para seguir adelante o «De verdad lo necesito», si la app lo trae | De 1 a 2 toques, menos de 5 segundos | Nada | Sí, la acción pasa por ella |
| Esperar a que acabe un temporizador o una pausa para respirar | De 5 a 60 segundos | Atención, la moneda que estabas defendiendo | Sí |
| Resolver una prueba: un cálculo, una frase larga que escribir | De 20 a 60 segundos | Concentración, que es justo el objetivo | Sí |
| Borrar la app de bloqueo | Unos 10 segundos, salvo que `denyAppRemoval` esté activado | Tus ajustes, tu historial, tu racha | No, ya no está |
| Retirar Family Controls en Ajustes | Unos 15 segundos si conoces la ruta | Todos los escudos caen a la vez; los tokens quedan invalidados | Sí, [`authorizationStatus`](https://developer.apple.com/documentation/familycontrols/authorizationcenter/authorizationstatus){: hreflang="en"} (en inglés) se puede observar |
| Desactivar Tiempo de uso por completo | Unos 20 segundos | Tus límites y tu historial de uso | Sí |
| Borrar y restaurar el dispositivo | 30 minutos o más | Todo | No |
| Otra persona tiene el código de Tiempo de uso | No está a tu alcance | La autonomía, un coste real que a veces compensa pagar | No procede |

Dos filas piden comentario. `ApplicationSettings.denyAppRemoval` existe de verdad: una app de bloqueo puede impedir que se borren apps en todo el dispositivo, lo que cierra la salida más barata. Y la revocación se puede observar, así que una app puede vigilar el estado de su propia autorización y saber al instante que te has ido. Si debe hacer algo con eso más allá de anotarlo para ti es una cuestión de diseño con una respuesta equivocada evidente.

Recorre esa escalera y «imposible de saltar» deja de significar nada. Lo que varía es cuántos segundos hay entre el impulso y la app, y si esos segundos te aportan algo.

## Lo que la realidad de la API implica para el diseño

Escribí hace un tiempo que [el coste de desbloquear tiene que pagarse fuera de la app](/journal/unlock-cost-outside-the-app/){: hreflang="en"} (en inglés): un coste que te fijas tú, dentro del software, es un coste que tu antojo puede renegociar en pleno antojo. Los hechos de la API llevan al mismo argumento en el plano de la plataforma. La revocación está siempre a unos quince segundos, así que el muro no es el producto. El precio, sí.

Y ese precio debería pagarse en algo de lo que se beneficie tu yo futuro. Esperar no pasa esa prueba: pagas con atención, justo lo que querías proteger, y no recibes nada a cambio. Mover el cuerpo sí la pasa, porque el coste cae en el resto de tu vida.

Eso no quiere decir que los otros diseños estén equivocados. Varios sirven para problemas que el mío no resuelve:

**[one sec](/es/alternatives/one-sec/)** te interrumpe *antes* de que se abra la app, con una respiración, una pausa o una pregunta. Si tu dedo llega antes que tu intención, te encaja mejor que una puerta cerrada, porque apunta al reflejo. Una puerta que ya te has ganado el derecho a cruzar no hace nada contra un reflejo. one sec funciona además en Android, algo que ninguna de nuestras apps hace.

**[Brick](/alternatives/brick/){: hreflang="en"} (en inglés)** mete en el bucle una etiqueta NFC física, que se paga una sola vez. Dejar la etiqueta en casa es un compromiso que no puedes deshacer desde el sofá, y es el único diseño de la categoría donde la fricción está hecha de átomos y no de software que tú has autorizado. El coste es un objeto que comprar, llevar encima y perder. [Unpluq](/alternatives/unpluq/){: hreflang="en"} (en inglés) funciona con el mismo principio físico, junto con una suscripción.

**[ScreenZen](/es/alternatives/screenzen/)** es gratis, con pausas cada vez más largas, y ser gratis es una ventaja real que el plan de por vida de EarnLock, a {P_LIFETIME@earnlock}, no borra. **[Opal](/es/alternatives/opal/)** y **[Jomo](/alternatives/jomo/){: hreflang="en"} (en inglés)** están más pulidas que nuestra app, y Jomo cubre iPhone, iPad y Mac.

[EarnLock](/es/apps/earnlock/) usa exactamente los mismos tres frameworks que todas ellas y no hace nada que Apple no publique. Lo que cambia es el precio: las apps que eliges siguen bloqueadas hasta que alcances un objetivo diario de actividad que lee de Salud de Apple (pasos en el plan gratis; minutos de actividad o calorías activas con Premium). Con la mitad del objetivo, algunas se abren durante una hora más o menos, una vez al día, y con el objetivo completo se abren todas hasta medianoche. Los sitios web que bloqueas en el mismo selector solo se abren con el objetivo completo. Su escudo sustituye la pantalla de restricción genérica de Apple por el número que te falta. *2026 pasos para desbloquear* te dice adónde vas; una pantalla que solo avisa de que la app está restringida se limita a pararte. Con Premium, la app para el Apple Watch lee sus propios datos de Salud y muestra cuánto te falta para desbloquear, mientras el iPhone se encarga del bloqueo. Qué número fijar es otra pregunta, que trata [lo que respaldan los estudios sobre el número de pasos](/es/journal/how-many-steps-a-day-to-aim-for/). Bloquear una app es gratis; Premium cuesta {P_MONTHLY@earnlock}/mes, {P_YEARLY@earnlock}/año o {P_LIFETIME@earnlock} una sola vez.

EarnLock tiene las mismas limitaciones que todo lo demás de esta página. Tampoco puede ver qué apps has bloqueado. No detiene las notificaciones. Es una app para iPhone, con una app para el Apple Watch en Premium, y no tiene versión para iPad ni para Mac. Tiene un «Desbloqueo de emergencia» al día, protegido por un cálculo, a propósito, porque la gente borra una herramienta que no tiene salida. Y si abres Ajustes y retiras su autorización, todos los escudos caen y no puede hacer nada al respecto. Lo mismo vale para cada app de Family Controls que se nombra en esta página, y conviene saberlo antes de pagar a cualquiera de nosotros. (Las reglas sobre datos que hay detrás, y detrás de todas las demás apps de Lagerland, están en la [página de transparencia](/es/transparency/).)

## Lo esencial

- **Ninguna app de terceros para iPhone bloquea nada por sí misma.** Se lo pide a iOS, con FamilyControls (el permiso y el selector), ManagedSettings (el escudo) y DeviceActivity (horarios y umbrales).
- **El selector devuelve tokens opacos, no nombres de apps.** Tu app de bloqueo no puede registrar, vender ni filtrar qué apps has elegido, porque iOS nunca le da los nombres. La misma regla le impide rellenarte una lista recomendada.
- **Un escudo bloquea el arranque, no el aviso.** Cubre la app y, con los dominios web, Safari. No cubre tu iPad, tu Mac ni el banner que te hizo entrar.
- **Nada es imposible de saltar, por diseño de Apple.** Retirar Family Controls en Ajustes lleva unos quince segundos e invalida todos los escudos a la vez. `denyAppRemoval` cierra la salida más barata; nada cierra la última.
- **Así que compara el precio, no el muro.** Lo que varía es lo que se interpone entre el impulso y la app (un toque, una espera, una etiqueta física o un número de pasos) y si pagarlo te deja en mejor situación.
