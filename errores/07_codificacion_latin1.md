# 07 · Tildes rotas por la codificación

**Qué pasó.** Los archivos de datos abiertos que usa el script de la Clase 10
vienen en `latin1`, no en `utf-8`. Por eso el script de clase los lee con
`encoding="latin1"`.

**Cómo se manifiesta.** Leídos con la codificación equivocada, aparece
`UnicodeDecodeError: 'utf-8' codec can't decode byte`, o los nombres salen como
`Museo RomÃ¡ntico` o `Museo Rom�ntico`. Si después se une por nombre de
estación, esas filas no encuentran pareja y el merge pierde datos sin avisar.

**Cómo se detectó.** El nombre de la estación se veía mal al imprimir la tabla.

**Cómo se arregló.** Indicando la codificación al leer (`encoding="latin1"`) y,
para unir por nombres, normalizándolos antes (`funciones/utilidades.py::normalizar_texto`).

**Ojo.** La consola de Windows también puede mostrar mal las tildes aunque el
dato esté bien (`PYTHONIOENCODING=utf-8` lo evita). Hay que distinguir si el
problema es del archivo o de la pantalla.
