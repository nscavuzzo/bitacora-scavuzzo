# Clase 6 · Diseño de encuestas

**Qué se intentó.** Ver cómo se pasa de un concepto a una pregunta (operacionalización), niveles de medición, preguntas filtro y tipos de faltante.

**Qué falló.** Un código como `999` o un "no sabe" mal cargado termina sumado como si fuera un dato (`recetas/04`: la edad media sube de 32 a 225).

**Qué se decidió.** En toda tabla de encuesta, revisar los valores únicos de cada columna antes de calcular nada y pasar los códigos a faltante por columna.
