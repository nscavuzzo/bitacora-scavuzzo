# 03 · Objeto no encontrado en R

**Qué pasó.** En mi script de prueba de la Clase 3 (`prueba1.R`) comenté la
línea que creaba `objeto2` y más abajo lo seguí usando:

```r
#objeto2 <- objeto1*3
df <- cbind(objeto1, objeto2, objeto_caracter)
```

**Cómo se manifiesta.**

```
Error: objeto 'objeto2' no encontrado
```

**Cómo se detectó.** El error dice el nombre del objeto que falta. Con `ls()` se
ve qué objetos existen en el entorno.

**Por qué es traicionero.** Si en la sesión `objeto2` había quedado creado de
antes, el script anda en mi RStudio pero falla en cualquier otra PC. Funciona
"de casualidad".

**Cómo se arregló.** Descomentando la línea y, sobre todo, corriendo el script
entero en una sesión limpia (*Session > Restart R*) antes de darlo por bueno.

**Otro detalle del mismo script.** `cbind()` arma una matriz, que admite un solo
tipo: al juntar números con un factor, el factor queda como sus códigos
numéricos. Para mezclar tipos hay que usar `data.frame()`.
