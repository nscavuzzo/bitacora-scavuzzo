# 06 · La zona horaria de las fechas: confiar en la etiqueta o en el dato

**Qué pasó.** En `transito_aire_junio2024.csv` la hora viene como
`2024-06-01T03:00:00Z`. La `Z` dice que es UTC, así que la pasé a hora de
Montevideo (UTC-3) antes de armar el perfil diario del tránsito.

**Cómo se manifiesta.** No da error: da un resultado raro. Con la conversión,
el tránsito promedio por hora queda así (los tres puntos de conteo juntos):

| Hora | sin convertir | convertida a Montevideo |
|---|---|---|
| mínimo | 4 h | 1 h |
| sube fuerte | 5 h (12.607 veh.) | 2 a 5 h de la mañana |
| máximo | 17 h | 14 h |

Que el tránsito se dispare entre las 2 y las 5 de la mañana no tiene sentido.
Sin convertir, el perfil sí es el esperable: mínimo de madrugada, subida a las
5-6 y pico a la tarde.

**Cómo se detectó.** Graficando el perfil diario y preguntándose si era
creíble. El dato contradecía la etiqueta.

**Conclusión.** Lo más probable es que las horas ya estén en hora local y la
`Z` esté mal puesta al armar el archivo. Lo anoté como pendiente de confirmar
con la docente, y en la receta 02 uso la hora tal como viene.

**Lección.** La zona horaria no se supone por la etiqueta: se controla contra
algo que se sabe (de noche hay menos autos). La función
`funciones/utilidades.py::utc_a_montevideo` sirve cuando la fecha sí está en UTC,
pero hay que chequearlo antes.
