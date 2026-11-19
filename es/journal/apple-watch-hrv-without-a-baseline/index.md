---
layout: journal
slug: apple-watch-hrv-without-a-baseline
ref: /journal/apple-watch-hrv-without-a-baseline/
permalink: /es/journal/apple-watch-hrv-without-a-baseline/
translated_from: 2026-11-08
last_updated: 2026-11-19
date: 2026-11-19
title: "VFC baja en el Apple Watch: sin tu referencia, la cifra casi no dice nada"
seo:
  title: "VFC baja en Apple Watch: qué significa según tu referencia"
  description: "¿VFC baja en el Apple Watch? Una lectura de 42 ms puede ser muy buena o alarmante, y solo tu referencia lo dice. Qué mide, qué no y cómo leer la tuya."
  keywords:
    - "vfc baja"
    - "vfc baja qué significa"
    - "variabilidad de la frecuencia cardiaca valores normales"
    - "vfc normal"
    - "vfc apple watch"
    - "valores de referencia vfc"
    - "vfc normal por edad"
lede: "Una VFC (HRV) de 42 ms en el Apple Watch puede ser excelente, media o alarmante, y sin contexto no hay forma de saber cuál. Por sí sola, la cifra es una de las métricas de salud de consumo que más se malinterpretan. Este artículo explica qué te dice la VFC, qué no te dice y por qué una referencia personal es el único marco que hace útil la lectura."
quick_answer: "La VFC bruta del Apple Watch (variabilidad de la frecuencia cardiaca, que el reloj da como SDNN) solo tiene sentido frente a tu propia referencia móvil, así que una cifra baja no se puede juzgar por sí sola. La VFC absoluta varía entre 3 y 10 veces de una persona a otra según la edad, el sexo, la forma física, la postura, el momento de la medición y la muñeca en la que llevas el reloj. Lee tu VFC como una desviación porcentual respecto a tu propia media de las últimas semanas; 60 días es una buena ventana. Comparar tu cifra con la de un amigo, con la media de la población o con una tabla de «rango normal» de internet casi siempre te llevará a conclusiones erróneas."
excerpt: "Una VFC de 42 ms en el Apple Watch es excelente para una persona y alarmante para otra. Este artículo explica por qué la VFC absoluta varía entre 3 y 10 veces de un cuerpo a otro, por qué tu referencia personal es el único marco que hace útil la VFC y cómo leer las tendencias como lo haría un científico del deporte."
faq:
  - q: "¿Es buena o mala una VFC de 42 ms?"
    a: "Depende por completo de quién tenga esos 42 ms. Si tu referencia de 60 días es de 38 ms, 42 ms están por encima de tu media y son una buena señal de recuperación. Si tu referencia es de 80 ms, 42 ms son la mitad de lo normal en ti y probablemente indican un estrés importante, una enfermedad o una carga de entrenamiento acumulada. La misma cifra absoluta es una buena noticia en un cuerpo y una mala en otro, y por eso cualquier app de VFC que merezca la pena te compara con tu propia referencia."
  - q: "¿Por qué la VFC del Apple Watch es tan distinta de la de una banda pectoral?"
    a: "El Apple Watch mide la VFC (SDNN) en momentos variables del día y durante la noche, cuando no te mueves, mediante fotopletismografía óptica. Una banda pectoral mide de forma continua a partir de la actividad eléctrica. Son dos mediciones distintas, tomadas en condiciones distintas, así que las cifras absolutas no se corresponden. Lo que sí es comparable es la serie de lecturas de tu reloj a lo largo del tiempo. Tu tendencia es fiable; tu cifra absoluta puesta frente a la tabla de una banda pectoral, no."
  - q: "¿Cuánto varía la VFC de un día para otro en la misma persona?"
    a: "Mucho. En un adulto sano son normales oscilaciones diarias del 10 al 25 %, así que una sola lectura baja casi nunca significa nada. Mira la media móvil de 7 días frente a tu referencia de 60 días. La VFC de un solo día es sobre todo ruido."
  - q: "¿Por qué baja la VFC en invierno?"
    a: "Es una adaptación cardiovascular estacional. La exposición al frío, la menor luz natural, la menor actividad aeróbica y los cambios en el sueño desplazan el equilibrio autónomo hacia el predominio simpático. Una bajada del 10 al 20 % en invierno es habitual y no es patológica. Uno de los errores de interpretación más comunes es leerla como «me pasa algo» cuando significa «mi VFC de invierno es más baja»."
  - q: "¿El Apple Watch da la VFC en RMSSD, en SDNN o en lnRMSSD?"
    a: "En SDNN. Salud de Apple guarda la VFC del Apple Watch como SDNN, la desviación típica de los intervalos entre latidos sucesivos, en milisegundos, y es la única métrica de VFC que expone HealthKit. La ciencia del deporte suele usar el RMSSD y su logaritmo natural, el lnRMSSD, que son cálculos distintos del SDNN, así que una lectura del Apple Watch no se puede convertir sin más en ninguno de los dos. Observa muestra el SDNN que registra Salud de Apple y lo compara con tu propia referencia."
mentioned_apps:
  - observa
read_time: "8 min de lectura"
---

El Apple Watch mide uno de los datos fisiológicos más informativos al alcance de cualquiera, y casi nadie lo usa bien.

Abre la app Salud y toca Variabilidad de la frecuencia cardiaca. Verás una columna de cifras de las últimas semanas, quizá algunos 25, algunos 45, algunos 80, y un gráfico con su «Intervalo» que parece vagamente informativo. Si has caído en el rincón equivocado de internet, puede que hayas leído que la VFC «debería» estar por encima de 50 ms o que cualquier valor por debajo de 30 es «preocupante». Eso es tan útil como decirte que tu temperatura corporal «normal» debería ser de 37 °C seas quien seas. La cifra es real. Lo que falla es el marco.

## Qué mide realmente la VFC

La VFC, o variabilidad de la frecuencia cardiaca, es la variación del tiempo que pasa entre latidos consecutivos. El Apple Watch da el SDNN, la desviación típica de los intervalos entre latidos normales sucesivos (los intervalos NN, o RR), en milisegundos. Un valor más alto suele indicar más actividad parasimpática del sistema nervioso («reposo y digestión»), y un valor más bajo suele indicar más actividad simpática («lucha o huida»). Una VFC que se mantiene más alta de forma sostenida se asocia con la forma cardiovascular, la calidad de la recuperación y el predominio parasimpático.

Hasta aquí, todo bien. El problema empieza cuando las mismas palabras se aplican a dos personas cuyas cifras absolutas difieren en un factor de tres.

## La variación entre personas es enorme

En adultos sanos, la VFC absoluta va aproximadamente de 15 a 150 ms en SDNN, una dispersión de 10 veces. Estos factores mueven la referencia de cada persona:

- **Edad.** La mayoría de los estudios longitudinales encuentran que la VFC baja entre 0,5 y 1 ms por año a partir de los 30. Una persona de 45 años con 35 ms y otra de 25 con 70 ms pueden tener ambas una salud parasimpática perfecta para su edad.
- **Sexo.** La VFC media es algo más baja en las mujeres adultas que en los hombres, aunque la variación dentro de cada sexo es mucho mayor que la diferencia entre ambos.
- **Forma física.** Las personas entrenadas en resistencia suelen mostrar una VFC en reposo entre un 50 y un 100 % más alta que las no entrenadas. Tampoco eso aporta información proporcional: los deportistas bien preparados suelen moverse en rangos que una tabla genérica llamaría «elevados».
- **Postura.** La VFC es más alta en posición tumbada que sentada, y más alta sentada que de pie.
- **Hora del día.** Más alta por la noche, más baja durante las horas de actividad.
- **Método de medición.** La fotopletismografía óptica del Apple Watch en momentos variables da cifras distintas a las de una banda pectoral o un ECG de nivel de investigación, incluso en la misma persona y en el mismo instante.

La VFC es una de esas métricas biológicas en las que *la tuya* es la única que significa algo. Comparar tus 42 ms con los 65 ms de un amigo no te dice nada.

## El marco correcto: tu propia referencia de 60 días

Las únicas lecturas de VFC que puedes interpretar con fiabilidad se parecen a una de estas:

- **«La VFC (SDNN) de hoy está un X % por encima o por debajo de mi propia media móvil de 7 días.»**
- **«La media de esta semana está un X % por encima o por debajo de mi propia media móvil de 60 días.»**

Las dos te comparan con tu propio pasado, lo que anula casi todos los factores de confusión anteriores. Tu edad y tu sexo no cambian en 60 días, tu forma física no cambia de forma drástica y tu reloj sigue siendo el mismo. Lo que sí cambia es *lo que haya movido tu fisiología esta semana respecto al último trimestre*, y esa es la pregunta que merece la pena hacerse.

Sesenta días funcionan como ventana de referencia por tres motivos. Son aproximadamente dos ciclos menstruales, así que la variación cíclica se compensa en la media. Cubren dos mesociclos de entrenamiento típicos, de modo que la adaptación a corto plazo no domina. Y dan suficientes muestras semanales sin solapamiento para que una desviación típica signifique algo; con menos, la propia desviación típica es ruidosa.

## Qué significa y qué no una lectura baja aislada

Una mañana en la que tu VFC está un 30 % por debajo de tu media de 7 días significa que *ha pasado algo*: una cena tardía, alcohol, mal sueño, una tarde estresante, el comienzo de una enfermedad, un entrenamiento duro el día anterior o el ruido biológico normal de un día a otro. Por sí sola no te dice que descanses, que entrenes fuerte, que te alarmes ni que lo celebres.

Lo revelador es un *patrón*. Tres días seguidos a más de una desviación típica por debajo de tu referencia son señal. Una bajada aislada del 25 % tras un factor de estrés conocido te habla de ese factor, no de tu salud. Una bajada del 25 % sin causa identificable que no se ha resuelto en 72 horas merece atención, la de un profesional sanitario y no la de una app de consumo.

Para tus propios experimentos, este umbral me parece más o menos acertado: **al menos 10 observaciones en las mismas condiciones dentro de una ventana de 60 días, y al menos una desviación típica de separación entre condiciones**, antes de tratar un hallazgo como algo más que ruido. Un «descubrimiento» con menos respaldo que ese suele ser una suposición.

## Por qué baja la VFC en invierno (y otro ruido estacional)

Si llevas un Apple Watch durante un invierno del hemisferio norte, cuenta con que tu referencia de VFC baje entre un 10 y un 20 % de octubre a febrero. Las causas habituales son la exposición al frío, la menor luz natural, menos actividad aeróbica, más tiempo en interiores y cambios en el sueño. Ninguna es patológica, y todas empujan la cifra hacia abajo.

Leer una bajada invernal como «me pasa algo» es uno de los errores de interpretación más comunes. La lectura correcta es «mi VFC de invierno es más baja, y esta es la nueva referencia desde la que medir las desviaciones». La referencia está hecha para desplazarse, porque tu fisiología se desplaza con el mundo.

## Qué significa esto en la práctica

De todo lo anterior se desprenden unas cuantas reglas prácticas:

1. **No compares nunca tu cifra con la de nadie.** Eso incluye la de un amigo, la de un desconocido en Reddit y cualquier infografía de «rango normal». Compara tu VFC solo con la tuya.

2. **Sigue las tendencias.** La VFC de un solo día es sobre todo ruido. La media móvil de 7 días es la señal, y la referencia de 60 días es el marco que permite interpretarla.

3. **Léela como una desviación respecto a tu propia referencia.** La VFC sigue aproximadamente una distribución lognormal, así que la misma diferencia en milisegundos pesa más con una referencia baja que con una alta. Expresar el SDNN de hoy como una desviación porcentual respecto a tu media móvil personal es lo que lo hace interpretable.

4. **Identifica tus factores de estrés.** Si tu VFC baja de forma constante después de entrenar tarde, de tomar alcohol o de pasar muchas horas ante pantallas, puedes actuar sobre eso. El problema de fondo es la causa que aún desconoces.

5. **Cuenta con la deriva estacional.** Más baja en invierno y más alta en verano es lo normal. Una pandemia, una enfermedad, el estrés del día a día o la llegada de un bebé también moverán la referencia. Trátala como un marco de referencia móvil.

[Observa](/es/apps/observa/) hace buena parte de esto por ti. Muestra tu VFC (SDNN) frente a tu propio rango habitual, con 7 días de tendencia gratis y 30, 90 o 365 días con Premium. La VFC también supone el 25 % de su puntuación de preparación diaria, y «¿Por qué esta puntuación?» te dice con palabras claras cuándo la VFC está fuera de tu rango habitual y ha movido la puntuación. El análisis se ejecuta en tu dispositivo, y la comparación que hace es *tú, hoy, frente a tu propia normalidad*, la única comparación de VFC que merece la pena.

## Lo esencial

- **La VFC absoluta varía entre 3 y 10 veces entre adultos sanos.** Comparar tu cifra con la de otra persona no tiene sentido.
- **Tu propia referencia, construida a lo largo de semanas, es el único marco que hace útil la VFC.** Las oscilaciones de un día para otro del 10 al 25 % son normales.
- **Importan las tendencias, no los puntos aislados.** Tres días seguidos a más de una desviación típica por debajo de la referencia son señal. Un solo día es ruido.
- **La VFC de invierno es más baja que la de verano.** La deriva estacional es normal, y tomarla por una enfermedad es el error habitual.
- **Lee el SDNN como una desviación respecto a tu propia referencia.** La VFC sigue aproximadamente una distribución lognormal, así que compara cada día con tu media personal en porcentaje, no con umbrales brutos en milisegundos.

La cifra siempre ha estado en tu app Salud. Lo que faltaba era una referencia con la que leerla.
