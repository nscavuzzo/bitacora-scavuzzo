# Datos

Los datos crudos no se versionan (norma del curso). Acá se documenta cada fuente.

## Tránsito y calidad de aire, Montevideo, junio de 2024

- **Archivo:** `transito_aire_junio2024.csv`
- **Origen:** archivo entregado por el docente en la Clase 10. Une, por hora, el
  conteo vehicular (archivos `autoscope_*_volumen.csv`) con las mediciones de NO2
  y PM2.5 (`no2_*.csv`, `pm_2_5_*.csv`), que el script de clase
  `transito_aire.py` carga por separado.
- **Fecha de obtención:** pendiente de confirmar (la copia local es del
  2/11/2026).
- **Registros:** 2.160 (720 horas × 3 estaciones: Curva de Maronias, Tres Cruces
  y Museo Romántico).
- **Columnas:** `hora` (UTC), `transito` (vehículos por hora), `no2` y `pm25`,
  `estacion`.
- **Faltantes:** `no2` 1.214, `pm25` 470.
- **Licencia:** pendiente de confirmar con el docente.
- **Datos personales:** no contiene.

Para usarlo, copiar el archivo a esta carpeta. La receta
`recetas/02_unir_por_fecha.py` lo busca acá; si no está, trabaja con una muestra
sintética con la misma estructura.
