# Clase 7 · Carga y transformación: calidad del aire

**Qué se intentó.** Cargar las mediciones de ozono de Montevideo, resumirlas (media y percentil 95) y hacer un mapa.

**Qué falló.** Los archivos venían en `latin1`, y con la codificación equivocada las tildes de las estaciones se rompían (`errores/07`).

**Qué se decidió.** Indicar siempre la codificación al leer y mirar las primeras filas antes de seguir. Para el aire, reportar el percentil 95 además de la media: los picos importan.
