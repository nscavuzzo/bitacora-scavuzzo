# 04 · El texto vacío no es un faltante

**Qué pasó.** Estos dos vectores parecen iguales y no lo son:

```r
objeto4 <- c("silla", "mesa", "")    # "" es un texto, de largo cero
objeto5 <- c("silla", "mesa", NA)    # NA es un faltante
```

**Cómo se manifiesta.** `sum(is.na(objeto4))` da 0. En pandas pasa lo mismo:
`df.isna()` no cuenta los `""`, ni los `"s/d"`, ni un `999` usado como código.
Los conteos de faltantes dan bien "de más" y los promedios salen inflados (en la
receta 04, la edad media pasa de 32 a 225 por un `999`).

**Cómo se detectó.** Mirando los valores únicos de cada columna
(`unique()` en R, `value_counts(dropna=False)` en pandas) antes de contar.

**Cómo se arregló.** Pasando los códigos a faltante por columna, no en toda la
tabla, y contando de nuevo. Ver `funciones/utilidades.py::resumen_faltantes` y
`recetas/04_faltantes.py`.
