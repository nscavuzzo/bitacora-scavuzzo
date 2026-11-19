# Bitácora personal · Introducción a la Ciencia de Datos

Nicolás Scavuzzo · Universidad de Montevideo, FCEE · Agosto a noviembre de 2026

Bitácora individual del curso. La estructura sigue la que sugiere el programa:

```
bitacora-scavuzzo/
├── diario/      una entrada por clase: qué se intentó, qué falló, qué se decidió
├── funciones/   utilidades propias, documentadas y con un caso de prueba
├── recetas/     procedimientos resueltos (leer un Excel sucio, unir por fecha, ...)
├── errores/     errores cometidos, cómo se detectaron y cómo se manifiestan
└── datos/       cómo obtener los datos; los datos crudos no se versionan
```

## Cómo correrlo

Python 3.11 o superior.

```bash
pip install -r requirements.txt      # en Windows, si pip no se reconoce: py -m pip install -r requirements.txt
python funciones/test_utilidades.py  # casos de prueba de las funciones
python correr_todo.py                # ejecuta todas las recetas y las pruebas
```

Las recetas generan sus propios datos de ejemplo, salvo la de unir por fecha, que
usa los datos de tránsito y aire del curso si están en `datos/` (ver
[`datos/README.md`](datos/README.md)); si no están, usa una muestra sintética con
la misma estructura. Los gráficos se escriben en `salidas/`, que no se versiona.

## Estado de la bitácora

Las entradas que fui guardando durante el semestre se perdieron. Esta versión se
reconstruyó el 19/11/2026 a partir de los archivos de cada clase que conservo.
Por eso el historial de *commits* empieza en esa fecha y no semana a semana como
pide el programa. Lo aviso acá en lugar de esconderlo.

## Uso de asistentes de IA

Usé Claude (Anthropic) para reconstruir la bitácora: la estructura, la redacción
a partir de los archivos de cada clase y el código de `funciones/` y `recetas/`.
Todo el código se verifica con `python correr_todo.py`. Respondo por cada línea.
