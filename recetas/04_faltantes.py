"""Receta 04 · Encontrar y tratar faltantes.

Problema (Clases 3, 4 y 6): los faltantes no siempre aparecen como NaN. En mis
pruebas de la Clase 3 en R, c("silla", "mesa", "") y c("silla", "mesa", NA)
parecen lo mismo pero no lo son: el texto vacío no cuenta como faltante. En las
planillas aparecen además "s/d", "-" o 999.

Pasos:
1. Contar los faltantes "visibles" (isna).
2. Buscar los escondidos: textos vacíos, códigos como "s/d" o 999.
3. Pasarlos todos a NaN y volver a contar.
4. Decidir qué hacer y anotarlo: no es lo mismo borrar la fila que dejarla.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "funciones"))
from utilidades import resumen_faltantes  # noqa: E402

encuesta = pd.DataFrame({
    "edad": [23, 35, 999, 41, np.nan, 29],
    "barrio": ["Pocitos", "", "Centro", "s/d", "Cordón", "Pocitos"],
    "gasto": [1200, 800, np.nan, 950, 1100, 999],
})

# 1. Lo que pandas ve
print("Faltantes según isna():\n", encuesta.isna().sum(), "\n")

# 2-3. Códigos de faltante conocidos -> NaN.
#  Ojo: 999 es faltante en edad (código del cuestionario) pero podría ser un
#  valor real en gasto. El reemplazo se hace por columna, no en toda la tabla.
codigos = {"edad": [999], "barrio": ["", "s/d"]}
limpia = encuesta.copy()
for col, valores in codigos.items():
    limpia[col] = limpia[col].replace(valores, np.nan)

print("Faltantes reales:\n", resumen_faltantes(limpia), "\n")

# 4. Decisión: no borro filas (perdería 3 de 6). Calculo cada estadística con
#    los datos que hay y digo cuántos casos usé.
media_edad = limpia["edad"].mean()
n = limpia["edad"].notna().sum()
print(f"Edad media: {media_edad:.1f} (n = {n} de {len(limpia)})")

# Con el 999 adentro la media daba otra cosa: así se detecta el error
print(f"Edad media sin limpiar: {encuesta['edad'].mean():.1f}  <- inflada por el 999")
assert n == 4 and round(media_edad, 1) == 32.0
