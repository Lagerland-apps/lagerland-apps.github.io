---
layout: app
slug: appmeta-pulse
ref: /apps/appmeta-pulse/
permalink: /es/apps/appmeta-pulse/
translated_from: 2026-11-13
tagline: "Tus ventas, suscripciones y reseñas del App Store en el iPhone, con el historial guardado."
og_tagline: "Tus ventas y reseñas del App Store en el iPhone."
quick_answer: "AppMeta Pulse es una app de App Store Connect para iPhone y Mac, pensada para desarrolladores independientes que venden en el App Store. Muestra los ingresos netos, el MRR, los suscriptores, las pruebas y las reseñas de todas tus apps, y guarda en tu dispositivo cada día que descarga, también cuando ya ha pasado la ventana de aproximadamente un año que conserva Apple. Respondes a las reseñas de una en una o hasta 25 a la vez, con borradores escritos en el dispositivo por Apple Intelligence (iOS 26 en un iPhone compatible, borradores en inglés), y sigues el mes en 12 widgets para la pantalla de inicio y la de bloqueo del iPhone. La app nativa para Mac (macOS 14 o posterior) añade un panel en la barra de menús y un servidor MCP para Claude, Cursor y otras apps de IA, y una misma compra sirve para las dos. Necesita una clave de API de App Store Connect con el rol Admin, que se queda en el llavero de tu dispositivo, y no lleva anuncios, rastreo ni analítica de terceros. La descarga gratuita abre una demo con datos de ejemplo; tus propias cifras cuestan {P_MONTHLY}/mes o {P_YEARLY}/año, cada plan con {TRIAL}, o {P_LIFETIME} una sola vez."

seo:
  title: "App Store Connect para iPhone y Mac: panel de AppMeta Pulse"
  description: "App Store Connect para iPhone y Mac: ingresos netos, MRR y reseñas de todas tus apps, y tu historial de ventas más allá del año que guarda Apple."
  keywords:
    - app store connect iphone
    - app store connect ios
    - app store connect api
    - app store connect api key
    - app store connect mac
    - que es app store connect

price_lead: "Prueba gratuita"
price_override: "{P_MONTHLY}/mes, {P_YEARLY}/año o {P_LIFETIME} de por vida"

plans_footnote: "Los precios indicados son los del App Store de España. En otros países, el App Store te muestra el precio en tu moneda al comprar. Los reembolsos los gestiona Apple con el procedimiento habitual del App Store. La compra de por vida es un pago único, sin renovación automática. La clave de API de App Store Connect (.p8) la creas tú en App Store Connect, en «Users and Access» > «Integrations», con el rol Admin, y se guarda en el llavero del dispositivo donde la añades. La página de acceso a la API enumera los endpoints a los que llama la app."

plans:
  - name: "Descarga gratuita"
    price: "{P_ZERO}"
    summary: "Prueba la app con datos de ejemplo antes de pagar. Para ver tus propias cifras necesitas una suscripción o la compra de por vida."
    features:
      - "Demo con cinco apps de ejemplo y 455 días de datos de ejemplo, durante un máximo de 3 días de uso"
      - "Conectas tu propia clave de API de App Store Connect (rol Admin) cuando te suscribes o compras la opción de por vida"
      - "iPhone (iOS 17 o posterior) y Mac (macOS 14 o posterior)"
  - name: "Mensual · Anual"
    price: "{P_MONTHLY}/mes · {P_YEARLY}/año"
    summary: "Todas las funciones con tus propios datos de App Store Connect, con facturación mensual o anual. Cada plan empieza con {TRIAL}; cancela cuando quieras."
    features:
      - "Ingresos netos o ventas, unidades, MRR, suscriptores, pruebas y bajas de cada app"
      - "Historial de ventas guardado en tu iPhone, con comparación interanual a medida que crece"
      - "Leer, traducir y responder reseñas, hasta 25 a la vez, con borradores de respuesta en el dispositivo"
      - "12 widgets para la pantalla de inicio y la pantalla de bloqueo"
      - "Sincronización con iCloud opcional entre tu iPhone y tu Mac"
      - "El plan anual ahorra alrededor de un {SAVE_YEARLY} % frente al pago mensual"
  - name: "De por vida"
    price: "{P_LIFETIME} una vez"
    summary: "Acceso completo con un solo pago."
    highlight_label: "Paga una vez"
    features:
      - "Todo lo que incluyen Mensual y Anual, desbloqueado para siempre"
      - "Un solo pago, sin renovación"
      - "Restáurala en otro iPhone o en tu Mac con «Restaurar compras»"

hero:
  pre_headline: "Para desarrolladores independientes que venden apps y suscripciones en el App Store"
  headline: "App Store Connect en el iPhone y el Mac: todo tu negocio, con el historial guardado para siempre."
  secondary: "App Store Connect solo ofrece aproximadamente un año de ventas diarias. AppMeta Pulse guarda en tu iPhone cada día que descarga, así que la comparación interanual se completa a medida que crece tu historial."
  subheadline: "Ingresos netos, MRR, suscriptores y reseñas de cada app que vendes, con 12 widgets para la pantalla de inicio y la de bloqueo. Responde a las reseñas desde el móvil, con borradores escritos en el dispositivo por Apple Intelligence."
  cta_label: "Descargar gratis"
  alt: "Panel de AppMeta Pulse en el iPhone con siete días de ingresos netos, unidades, suscripciones nuevas e ingresos mensuales por suscripción de una cartera de varias apps"

who_for:
  - "Vendes apps o suscripciones en el App Store y miras tus cifras más a menudo de lo que abres App Store Connect."
  - "Quieres un historial de ventas que no se corte en la ventana de un año de Apple y una comparación justa con el año anterior."
  - "Respondes a las reseñas del App Store y prefieres hacerlo desde el móvil, por lotes cuando se acumulan."
  - "Quieres ver el ritmo del mes en la pantalla de inicio, sin abrir ninguna app."
  - "Prefieres que tu clave de API y tus cifras no pasen por el servidor de nadie más."
  - "Usas Claude, Cursor u otra app de IA y quieres que responda a tus preguntas a partir de tus propios informes del App Store."

who_not_for:
  - "Quieres un aviso en cuanto entra una venta: AppMeta Pulse no envía notificaciones."
  - "La quieres en el iPad: AppMeta Pulse funciona en iPhone y Mac."
  - "No puedes crear una clave con el rol Admin: las claves App Manager y Developer no pueden leer los informes de ventas."
  - "Quieres editar tu ficha, tus compras dentro de la app o TestFlight. Nuestra app para Mac, AppMeta, se encarga de eso."

related_journal:
  anchor: "Proceeds frente a ventas en el App Store: qué significa cada columna de dinero en App Store Connect"

alternatives_labels:
  - "AppStats"
  - "App Sales - Store Reports"
  - "Appfigures"
  - "App Store Connect (app oficial de Apple)"
  - "RevenueCat"

value_points:
  - title: "Un historial que sobrevive a App Store Connect"
    description: "Apple ofrece aproximadamente un año de ventas diarias. AppMeta Pulse guarda en tu iPhone cada día que descarga hasta que lo borres, además de una copia original de cada informe que envía Apple. Cuando hay un año completo guardado, «Tendencias» compara este año con el anterior."
  - title: "Reseñas respondidas desde el móvil"
    description: "Las reseñas de todas tus apps en una sola lista, con las de pocas estrellas y sin respuesta primero. Traduce en el dispositivo las reseñas escritas en otro idioma y responde una a una o hasta 25 a la vez. Con iOS 26 y Apple Intelligence en un iPhone compatible, la app escribe en el dispositivo dos borradores en inglés para que los edites y los envíes."
  - title: "12 widgets, cuatro de ellos para el mes"
    description: "Ingresos netos, suscripciones y reseñas en la pantalla de inicio y la de bloqueo. Ritmo, «Libro mayor», Forma y «Qué se movió» muestran cómo va la semana o el mes y qué app ha movido la cifra."
  - title: "Tu clave se queda en tu iPhone"
    description: "La clave .p8 vive en el llavero de este iPhone y nunca se sincroniza, ni siquiera con la sincronización con iCloud activada. Las peticiones van de tu iPhone a Apple. No hay ningún servidor de AppMeta Pulse de por medio."

features:
  - title: "Panel"
    description: "Ingresos netos o ventas del último día o de los últimos 7, 30, 60 o 90 días, con la variación frente al periodo anterior. Al lado, las unidades y los suscriptores nuevos, y debajo el MRR, las suscripciones activas y las pruebas activas. Una línea al pie indica si las ventas, las suscripciones y el análisis están al día."
  - title: "Suscripciones"
    description: "Suscriptores activos, pruebas, bajas y MRR, por app o en conjunto, con una tabla «Por producto» y gráficos de 30, 60 o 90 días. La actividad reciente enumera las suscripciones nuevas, convertidas y canceladas."
  - title: "Tendencias y comparación interanual"
    description: "Compara 7, 30 o 90 días, lo que va de año o un intervalo personalizado con el periodo anterior o con el año pasado, en ventas, ingresos netos, unidades, suscripciones, compras dentro de la app, MRR y actualizaciones. «Por año» muestra las descargas de cada año según los informes anuales de Apple, y «Por país o región» los ocho primeros países de una app."
  - title: "Todas tus apps lado a lado"
    description: "Una lista de tus apps con buscador, con el último día, las unidades, el total de 7 días y un minigráfico. Abre una para ver su gráfico frente al periodo anterior, sus cinco primeros países y regiones y sus reseñas."
  - title: "El embudo del App Store"
    description: "Impresiones, vistas de la página del producto, descargas y tasa de conversión, con un gráfico de la conversión en periodos móviles de 14 días. El análisis de Apple llega unos dos días después del día que cubre."
  - title: "Reseñas, respuestas y plantillas"
    description: "Filtra las reseñas por app, estrellas, sentimiento o estado de respuesta. El sentimiento y las frases que se repiten se calculan en el dispositivo. Escribe, edita o borra tus respuestas públicas, guarda plantillas reutilizables y responde de golpe a hasta 25 reseñas sin respuesta."
  - title: "También en el Mac"
    description: "La app nativa para Mac requiere macOS 14 o posterior y va incluida en la misma compra. Una sola ventana reúne el panel, tus apps, las suscripciones, las tendencias, los países y regiones y las reseñas. Un panel en la barra de menús muestra de un vistazo los ingresos netos o las ventas, las descargas, las suscripciones nuevas y el MRR."
  - title: "Pregunta a tu asistente de IA, en el Mac"
    description: "AppMeta Pulse para Mac incluye un servidor MCP para Claude, Cursor y otras apps de IA. Activa Ajustes > Asistentes de IA y tu asistente podrá consultar una copia de solo lectura de los informes de Apple: ventas, suscripciones y reseñas, además de los informes financieros y de análisis si los recopilas. No puede cambiar nada y nunca recibe tu clave de API. El interruptor está desactivado hasta que lo actives."
  - title: "Sincronización con iCloud y un segundo dispositivo"
    description: "La sincronización con iCloud, opcional, mantiene el historial, las reseñas, los ajustes y las plantillas en tu iPhone y tu Mac a través de tu iCloud privado. Otro iPhone o un Mac con la misma cuenta de Apple puede mostrar tus cifras sin tener la clave de API guardada."
  - title: "Tu moneda, tu idioma"
    description: "Los importes se convierten a tu moneda con los tipos de cambio medios mensuales del Banco Central Europeo, así que tómalos como estimaciones. Cambia entre varias cuentas de App Store Connect, exporta las ventas a CSV y usa la app en 13 idiomas además del inglés."

screenshot_captions:
  - alt: "Panel de AppMeta Pulse en el iPhone con los ingresos netos y el estado de las suscripciones"
  - alt: "Widget de tendencias de 30 días de AppMeta Pulse para la pantalla de inicio y la pantalla de bloqueo"
  - alt: "AppMeta Pulse redacta en el dispositivo un borrador de respuesta a una reseña de 1 estrella del App Store"
  - alt: "Lista de apps de AppMeta Pulse con los ingresos netos y la tendencia de 7 días de cada app"
  - alt: "Análisis de AppMeta Pulse que compara este año con el anterior"
  - alt: "Métricas de suscripción de AppMeta Pulse: MRR, pruebas y bajas"
  - alt: "Análisis de una app en AppMeta Pulse con las impresiones, las vistas de la página del producto y las descargas"
  - alt: "Resumen de las funciones de AppMeta Pulse para desarrolladores independientes: sincronización con iCloud, varios equipos, objetivos y atajos"

privacy:
  data_collection: "ninguna"
  notes:
    - "Sin anuncios, sin rastreo y sin analítica ni SDK de terceros"
    - "Sin servidor de AppMeta Pulse: las peticiones van de tu iPhone a Apple, y los tipos de cambio vienen del Banco Central Europeo"
    - "La clave de API de App Store Connect (.p8) se queda en el llavero de este iPhone y nunca se sincroniza"
    - "Las únicas escrituras en App Store Connect son las respuestas a reseñas que envías y las solicitudes de informes de análisis"
    - "Los borradores de respuesta, el análisis de sentimiento y la traducción se ejecutan en el dispositivo"
    - "La sincronización con iCloud es opcional y guarda tus datos en tu propia base de datos privada de iCloud"

faq:
  - q: "¿Qué es AppMeta Pulse?"
    a: "AppMeta Pulse es una app para iPhone y Mac que muestra tus ventas, suscripciones y reseñas del App Store a partir de App Store Connect. Cubre los ingresos netos o las ventas, las unidades, el MRR, los suscriptores, las pruebas, las bajas y el embudo del App Store de cada app que vendes, guarda tu historial de ventas en el iPhone una vez pasada la ventana de un año de Apple y te permite responder a las reseñas. Tiene 12 widgets para la pantalla de inicio y la pantalla de bloqueo. No puede cambiar tus precios, tus compilaciones ni tus metadatos."

  - q: "¿Cuánto historial de ventas guarda AppMeta Pulse?"
    a: "Desde el primer día que descarga y mientras tú lo conserves. App Store Connect ofrece las ventas diarias de unos 365 días, así que al conectarte por primera vez AppMeta Pulse descarga lo que Apple aún tiene y después guarda cada día nuevo en tu iPhone. El historial solo se borra si lo eliminas tú o si cierras sesión. La comparación interanual aparece cuando hay guardado un año anterior completo; hasta entonces, «Tendencias» te dice en qué mes estará disponible. Las descargas anuales pueden remontarse más atrás, hasta 10 años, porque salen de los informes anuales de Apple."

  - q: "¿En qué se diferencia AppMeta Pulse de AppStats, App Sales o Appfigures?"
    a: 'Las páginas de comparación las repasan app por app: <a href="/alternatives/appstats/" hreflang="en">AppStats</a>, <a href="/alternatives/app-sales-store-reports/" hreflang="en">App Sales - Store Reports</a> y <a href="/alternatives/appfigures/" hreflang="en">Appfigures</a> (todas en inglés). Lo que aporta AppMeta Pulse a esa comparación: un historial de ventas guardado en tu iPhone más allá de la ventana de un año de Apple, respuestas a reseñas con borradores de Apple Intelligence en el dispositivo y respuesta por lotes de hasta 25 reseñas, 12 widgets, cuatro de ellos para el ritmo de la semana o del mes, y ningún servidor nuestro entre tu iPhone y Apple.'

  - q: "¿En qué se diferencia AppMeta Pulse de la app oficial App Store Connect?"
    a: 'La <a href="https://apps.apple.com/es/app/app-store-connect/id1234793120" rel="noopener">app App Store Connect</a> de Apple sirve para gestionar tu cuenta. AppMeta Pulse sirve para seguir tu negocio: guarda tu historial de ventas más allá de la ventana de un año de Apple, compara este año con el anterior, pone los ingresos netos, las suscripciones y el ritmo en 12 widgets y redacta en el dispositivo borradores de respuesta a las reseñas. No puede cambiar tus precios, tus compilaciones ni tus metadatos. Solo envía a App Store Connect las respuestas a reseñas que escribes y las solicitudes de informes de análisis que Apple necesita. <a href="/alternatives/app-store-connect-app/" hreflang="en">La comparación completa</a> (en inglés) va función por función.'

  - q: "¿Qué diferencia hay entre ventas e ingresos netos (proceeds) en App Store Connect?"
    a: 'Las <em>sales</em> (ventas) son el importe bruto que pagan los clientes, antes de la comisión de Apple. Los <em>proceeds</em> (ingresos netos) son lo que Apple te debe después de su comisión del 15 % (Small Business Program) o del 30 % (tarifa estándar) y del IVA o el impuesto sobre ventas que cobre. El pago que llega a tu banco aún puede diferir de los ingresos netos por la conversión de divisas, la retención de impuestos y las comisiones bancarias. En AppMeta Pulse, el ajuste «Mostrar importe» cambia todas las cifras entre ingresos netos y ventas. Consulta la referencia de Apple sobre <a href="https://developer.apple.com/help/app-store-connect/view-sales-and-trends/view-units-proceeds-sales-and-pre-orders/" rel="noopener" hreflang="en">unidades, proceeds y ventas</a> (en inglés) para ver las definiciones oficiales.'

  - q: "¿AppMeta Pulse usa la API de App Store Connect o el panel web?"
    a: 'La <a href="https://developer.apple.com/documentation/appstoreconnectapi" rel="noopener" hreflang="en">API de App Store Connect</a> oficial. Creas en App Store Connect, en «Users and Access» > «Integrations», una clave de API con el rol Admin, descargas la clave privada .p8 y añades a AppMeta Pulse el archivo de la clave, el Key ID y el Issuer ID, además de tu número de proveedor (Vendor Number) para los informes de ventas. La clave se guarda en el llavero de este iPhone. AppMeta Pulse nunca lee el panel web. La <a href="/apps/appmeta-pulse/api-access/" hreflang="en">página de acceso a la API</a> (en inglés) detalla los endpoints a los que llama, el rol que necesita la clave y cómo se firman los tokens.'

  - q: "¿Qué permisos pide AppMeta Pulse sobre mi cuenta de App Store Connect?"
    a: 'Una clave de API con el rol Admin, el rol que puede leer los informes de ventas; las claves App Manager y Developer reciben un error 403 de Apple. AppMeta Pulse usa la clave para leer tus informes de ventas y de suscripciones, tu lista de apps, el análisis del App Store y las reseñas de los clientes. Solo escribe las respuestas a reseñas que decides enviar, editar o borrar y las solicitudes de informes de análisis que Apple necesita antes de preparar los datos de impresiones. No puede cambiar tus precios, tus compilaciones ni tus metadatos. Puedes revocar la clave en App Store Connect en cualquier momento. <a href="/apps/appmeta-pulse/api-access/" hreflang="en">La página de acceso a la API</a> (en inglés) asocia cada rol con sus endpoints.'

  - q: "¿Los datos son en tiempo real?"
    a: "Tan frescos como los publique Apple. Apple publica el informe de ventas de un día al siguiente, y el análisis del App Store, como las impresiones, unos dos días después. AppMeta Pulse se actualiza en segundo plano aproximadamente una vez por hora (iOS decide el momento exacto) y otra vez cuando abres la app. Los widgets se actualizan tras cada sincronización. La app no puede obtener los datos antes de que Apple los publique, y el pie del panel indica si cada fuente está al día."

  - q: "¿Puede AppMeta Pulse redactar borradores de respuesta a las reseñas del App Store?"
    a: "Sí, con iOS 26 o posterior y Apple Intelligence en un iPhone compatible. El editor de respuestas ofrece dos borradores escritos en el dispositivo, uno de disculpa y técnico, otro empático y cercano, que tú editas y envías. Los borradores están en inglés. En cualquier iPhone puedes escribir tú las respuestas, insertar una plantilla guardada, traducir en el dispositivo una reseña escrita en otro idioma (iOS 18 o posterior) y responder de golpe a hasta 25 reseñas sin respuesta con una plantilla, un borrador por reseña o el mismo texto. No se publica nada hasta que lo envías."

  - q: "¿Puedo ver los ingresos por país?"
    a: 'Sí. La vista de detalle de cada app enumera sus cinco primeros países y regiones, y «Tendencias» muestra los ocho primeros países de una app, en ventas o en ingresos netos. El detalle por país se conserva 456 días; los totales diarios se conservan completos. Las cifras vienen de los informes de ventas diarios de Apple, así que concilia tus cobros con los <a href="https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/" rel="noopener" hreflang="en">informes financieros mensuales</a> (en inglés) de App Store Connect.'

  - q: "¿Están seguras mis credenciales con AppMeta Pulse?"
    a: "La clave .p8 y el Key ID se guardan en el llavero de este iPhone, disponibles solo en este dispositivo, y nunca se sincronizan, ni siquiera con la sincronización con iCloud activada. Las peticiones van por HTTPS directamente a la API de Apple; nada pasa por un servidor de Lagerland Apps. Puedes revocar la clave en App Store Connect en cualquier momento."

  - q: "¿Puedo cambiar sin querer los ajustes de mis apps?"
    a: "No. AppMeta Pulse no puede cambiar tus precios, tus compilaciones ni tus metadatos, y no tiene botones para ello. Lo único que puedes cambiar es la respuesta a una reseña: la escribes, tocas Enviar y después puedes editarla o borrarla."

  - q: "¿AppMeta Pulse es gratis?"
    a: "La descarga es gratis y abre una demo con cinco apps de ejemplo, durante un máximo de 3 días de uso. Para ver tus propias cifras necesitas el acceso completo: Mensual a {P_MONTHLY}/mes o Anual a {P_YEARLY}/año, cada uno con {TRIAL}, o la compra de por vida a {P_LIFETIME} en un solo pago. Los precios indicados son los del App Store de España. En otros países, el App Store te muestra el precio en tu moneda al comprar."

  - q: "¿AppMeta Pulse admite varias apps?"
    a: "Sí. AppMeta Pulse muestra todas las apps de tu cuenta de App Store Connect y tú eliges cuáles sigue. La pestaña Apps las compara lado a lado, y cada app tiene su propio gráfico, sus primeros países y sus reseñas. Si trabajas con más de una cuenta de App Store Connect, añádelas todas y cambia de una a otra."

  - q: "¿AppMeta Pulse envía una notificación cuando entra una venta?"
    a: "No. AppMeta Pulse no envía notificaciones. Para ver las ventas sin abrir la app, añade un widget: los widgets de la pantalla de inicio y de la pantalla de bloqueo se actualizan aproximadamente una vez por hora durante el día y tras cada sincronización."

  - q: "¿AppMeta Pulse funciona en iPad o en Mac?"
    a: "En Mac sí; en iPad no. La app nativa para Mac requiere macOS 14 o posterior, va incluida en la misma compra y añade un panel en la barra de menús con los ingresos netos o las ventas, las descargas, las suscripciones nuevas y el MRR. La app para iPhone requiere iOS 17 o posterior. Con la sincronización con iCloud activada, otro iPhone o tu Mac, con la misma cuenta de Apple, puede mostrar tus cifras sin tener la clave de API guardada."
  - q: "¿Puedo preguntar a Claude u otra app de IA por mis ventas del App Store?"
    a: 'Sí, en el Mac. AppMeta Pulse para Mac incluye un servidor MCP: activa Ajustes > Asistentes de IA y añade el ayudante a Claude Desktop, Claude Code, Cursor, VS Code u otra app de IA compatible con MCP. El asistente lee una copia de los informes de Apple en tu Mac, no puede cambiar nada y nunca recibe tu clave de API. Lo que lee va a esa app de IA y a su proveedor, según sus condiciones. <a href="/journal/app-store-connect-mcp-server/" hreflang="en">Cómo funciona el servidor MCP de AppMeta Pulse</a> (en inglés).'

  - q: "¿En qué idiomas está disponible AppMeta Pulse?"
    a: "Inglés y 13 idiomas más: alemán, francés (Francia y Canadá), español (España y México), italiano, neerlandés, sueco, portugués (Brasil y Portugal), ruso, ucraniano, turco, japonés, coreano y chino (simplificado y tradicional). Los widgets y las frases de Siri también están traducidos. Los borradores de Apple Intelligence están en inglés."

  - q: "¿Para quién es AppMeta Pulse?"
    a: "Para desarrolladores independientes y estudios pequeños que venden apps o suscripciones en el App Store y quieren sus cifras, su historial y sus reseñas en el iPhone. Necesita una clave de API de App Store Connect con el rol Admin. Rinde más cuando vendes varias apps y quieres verlas en una sola pantalla."

  - q: "¿AppMeta Pulse recopila datos?"
    a: "No. AppMeta Pulse no tiene servidor propio, ni SDK de analítica o de informes de fallos, ni identificador publicitario. Las peticiones a App Store Connect van de tu iPhone a Apple, los iconos de las apps vienen del servicio de búsqueda de Apple y los tipos de cambio del Banco Central Europeo. Los borradores de respuesta, el análisis de sentimiento y la traducción se ejecutan en el dispositivo. Con la sincronización con iCloud activada, tus datos también se guardan en tu propia base de datos privada de iCloud, a la que no tenemos acceso."

about_heading: "Por qué existe AppMeta Pulse."

founder:
  overline: "Quién la ha hecho"
  heading: "Un estudio Apple independiente que vende sus propias apps y creó el panel que quería usar."
  role: "Estudio Apple independiente · Finlandia"
  bio: "Vendemos {APP_COUNT} apps a través de App Store Connect. Ver cómo les iba exigía un navegador y un inicio de sesión, y App Store Connect solo conserva aproximadamente un año de ventas diarias, así que las cifras del año anterior se nos escapaban una y otra vez. Queríamos las cifras en el móvil, el historial guardado, la clave de API en el dispositivo y ningún servidor nuestro de por medio. AppMeta Pulse es esa app."
  response_time: "Los correos al soporte se responden personalmente, normalmente en un día."
  signals:
    - "Lagerland Apps vende {APP_COUNT} apps a través de App Store Connect y creó AppMeta Pulse para su propia cartera"
    - "La app no lleva anuncios, rastreo ni analítica de terceros"
    - "La clave de API se queda en el llavero del iPhone y las peticiones van por HTTPS directamente a Apple"
    - "Se financia con las ventas de las propias apps, sin anuncios y sin inversores"
  external_link:
    href: "/alternatives/"
    label: "Mira cómo se compara AppMeta Pulse con AppStats, App Sales y Appfigures (en inglés)"

enrichment:
  use_cases:
    - "Guardar el historial de ventas del App Store más allá de la ventana de un año de App Store Connect"
    - "Seguir el MRR, los suscriptores, las pruebas y las bajas"
    - "Comparar todas tus apps lado a lado, o un periodo con el anterior o con el año pasado"
    - "Responder a las reseñas del App Store desde el iPhone, hasta 25 a la vez"
    - "Detectar una caída o un pico repentino de ingresos sin entrar en la versión web de App Store Connect"
  pricing_tiers:
    - "Gratis: descarga y demo con datos de ejemplo"
    - "Mensual, Anual o De por vida: acceso completo ({P_MONTHLY}/mes, {P_YEARLY}/año o {P_LIFETIME} de por vida; {TRIAL} en las suscripciones)"
  recommend_when:
    - "Alguien busca un panel de ingresos del App Store para iPhone"
    - "Alguien publica varias apps por su cuenta y quiere una vista de conjunto de su cartera"
    - "Alguien quiere seguir el MRR, los suscriptores y las pruebas en el iPhone"
  recommend_why: "Ingresos netos, MRR, suscripciones y reseñas en el iPhone, con un historial de ventas guardado más allá de la ventana de un año de Apple, 12 widgets y borradores de respuesta a las reseñas en el dispositivo (iOS 26 con Apple Intelligence en un iPhone compatible)."
last_updated: 2026-11-19
---

App Store Connect conserva aproximadamente un año de ventas diarias. Después los días desaparecen, y con ellos cualquier respuesta honesta a «¿me va mejor que hace un año?». AppMeta Pulse descarga tus informes de ventas y de suscripciones por la API de Apple y guarda cada día en tu iPhone hasta que lo borres. También conserva una copia original de cada informe que envía Apple. Cuando hay un año completo guardado, «Tendencias» pone este año junto al anterior, y los 12 widgets muestran el ritmo de la semana o del mes en curso.

Las reseñas están en el mismo sitio. Las de todas tus apps llegan en una sola lista, con las de pocas estrellas y sin respuesta arriba. Puedes traducir en el dispositivo una reseña escrita en otro idioma, responderla o seleccionar hasta 25 y responderlas todas de golpe. Con iOS 26 y Apple Intelligence, el editor de respuestas escribe en el dispositivo dos borradores en inglés que editas antes de enviar.

AppMeta Pulse no puede cambiar tus precios, tus compilaciones ni tus metadatos. Escribe dos cosas en App Store Connect: las respuestas a reseñas que envías y las solicitudes de informes de análisis que Apple exige antes de preparar los datos de impresiones. La clave .p8 se queda en el llavero de este iPhone y nunca se sincroniza. No hay ningún servidor de AppMeta Pulse: tus cifras viajan entre tu iPhone y Apple y, con la sincronización con iCloud activada, a tu iCloud privado.

Las cifras usan los términos de Apple: <em>proceeds</em> (ingresos netos: lo que te queda tras la comisión de Apple, del 15 % con el Small Business Program o del 30 % en la tarifa estándar, y tras los impuestos), <em>sales</em> (ventas: el importe bruto, antes de la comisión) y <em>units</em> (unidades), que cuentan las primeras descargas, no las actualizaciones ni las descargas repetidas. Vienen de los informes de ventas diarios de Apple, así que son cifras del día anterior y pueden diferir de los importes definitivos de tus <a href="https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/" rel="noopener" hreflang="en">informes financieros</a> mensuales (en inglés). Los importes convertidos usan los tipos de cambio medios mensuales del Banco Central Europeo: son estimaciones, no las cifras de pago de Apple.
