"""Receta 05 · Comparar grupos con un gráfico honesto.

Problema (Clases 8 y 9): comparar una variable entre grupos. Un gráfico de
barras con la media esconde cuántos datos hay y cuánto varían. Mejor mostrar
la distribución (caja o puntos) y anotar el n de cada grupo.

Pasos:
1. Mirar n, media y mediana por grupo antes de graficar.
2. Gráfico de cajas con los puntos encima.
3. Título que diga lo que se ve; ejes con unidades.
"""
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SALIDAS = Path(__file__).resolve().parents[1] / "salidas"
SALIDAS.mkdir(exist_ok=True)

rng = np.random.default_rng(2026)
df = pd.DataFrame({
    "local": np.repeat(["Centro", "Pocitos", "Cordón"], [40, 40, 8]),
    "ticket": np.concatenate([
        rng.lognormal(6.8, 0.35, 40),
        rng.lognormal(7.0, 0.35, 40),
        rng.lognormal(7.1, 0.6, 8),   # pocos datos y mucha variación
    ]).round(0),
})

# 1. Tabla antes del gráfico
resumen = df.groupby("local")["ticket"].agg(n="size", media="mean", mediana="median").round(0)
print(resumen, "\n")

# 2-3. Cajas + puntos, con el n en la etiqueta
orden = ["Centro", "Pocitos", "Cordón"]
fig, ax = plt.subplots(figsize=(7, 4))
datos = [df.loc[df["local"] == g, "ticket"] for g in orden]
ax.boxplot(datos, showfliers=False)
for i, valores in enumerate(datos, start=1):
    x = rng.normal(i, 0.05, len(valores))
    ax.scatter(x, valores, s=12, alpha=0.5, color="tab:blue")
ax.set_xticks(range(1, 4), [f"{g}\n(n = {len(v)})" for g, v in zip(orden, datos)])
ax.set_ylabel("Ticket promedio ($)")
ax.set_title("Cordón parece más alto, pero con 8 datos no alcanza para decirlo")
fig.tight_layout()
fig.savefig(SALIDAS / "comparar_grupos.png", dpi=120)
print("Gráfico en salidas/comparar_grupos.png")
assert resumen.loc["Cordón", "n"] == 8
