# Clase 3 · Objetos, tipos y errores

**Qué se intentó.** Probar en R vectores, factores y data frames (`prueba1.R`) y leer los errores en vez de saltearlos. Renderizar los `.qmd` de clase con Quarto.

**Qué falló.** Comenté la línea que creaba `objeto2` y lo seguí usando: *objeto no encontrado* (`errores/03`). Quarto no estaba en el PATH (`errores/02`). Y `""` no es lo mismo que `NA` (`errores/04`).

**Qué se decidió.** Antes de dar un script por bueno, correrlo entero en una sesión limpia. Leer el mensaje de error completo: casi siempre dice qué falta.
