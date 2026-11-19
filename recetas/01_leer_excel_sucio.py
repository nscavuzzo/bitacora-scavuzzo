"""Receta 01 · Leer un Excel sucio.

Problema: una planilla "hecha para imprimir", no para analizar. Título y notas
arriba de la tabla, encabezado en la fila 4, números con coma decimal y punto de
miles escritos como texto, faltantes escritos como "s/d" o "-", una fila de
total al final y filas vacías en el medio.

Pasos:
1. Mirar la planilla cruda (header=None) para ver dónde empieza la tabla.
2. Leer desde la fila del encabezado.
3. Sacar filas vacías y la fila de total (si no, el total se suma dos veces).
4. Pasar los números a número con limpiar_numero().
5. Controlar: la suma de lo limpio tiene que dar el total que traía la planilla.

La planilla de ejemplo se genera acá mismo, así la receta corre en cualquier PC.
"""
import sys
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "funciones"))
from utilidades import limpiar_numero, resumen_faltantes  # noqa: E402

SALIDAS = RAIZ / "salidas"
SALIDAS.mkdir(exist_ok=True)
ARCHIVO = SALIDAS / "ventas_sucio.xlsx"


def crear_planilla_sucia(ruta: Path) -> None:
    filas = [
        ["Ventas por local - primer semestre", None, None, None],
        ["Fuente: planilla interna, valores en pesos", None, None, None],
        [None, None, None, None],
        ["Local", "Mes", "Ventas ($)", "Clientes"],
        ["Centro", "Enero", "1.234,50", "120"],
        ["Centro", "Febrero", "1.100,00", "s/d"],
        [None, None, None, None],
        ["Pocitos", "Enero", "2.050,75", "210"],
        ["Pocitos", "Febrero", "-", "198"],
        ["Cordón", "Enero", "980,25", "95"],
        # El total sí incluye Pocitos-Febrero (1.850,00), que en la celda quedó "-"
        ["TOTAL", None, "7.215,50", "623"],
    ]
    pd.DataFrame(filas).to_excel(ruta, header=False, index=False)


def leer_planilla(ruta: Path) -> tuple[pd.DataFrame, float]:
    # 1. Mirar cruda para encontrar el encabezado
    cruda = pd.read_excel(ruta, header=None)
    fila_encabezado = cruda.index[cruda.iloc[:, 0].eq("Local")][0]

    # 2. Leer desde ahí, todo como texto para limpiarlo a mano
    df = pd.read_excel(ruta, header=fila_encabezado, dtype=str)
    df.columns = ["local", "mes", "ventas", "clientes"]

    # 3. Sacar filas vacías y guardar el total aparte para controlar
    df = df.dropna(how="all")
    es_total = df["local"].str.upper().eq("TOTAL")
    total_planilla = limpiar_numero(df.loc[es_total, "ventas"].iloc[0])
    df = df.loc[~es_total].reset_index(drop=True)

    # 4. Texto -> número
    for col in ["ventas", "clientes"]:
        df[col] = df[col].map(limpiar_numero)
    return df, total_planilla


if __name__ == "__main__":
    crear_planilla_sucia(ARCHIVO)
    ventas, total = leer_planilla(ARCHIVO)
    print(ventas, "\n")
    print(resumen_faltantes(ventas), "\n")

    # 5. Control: la suma limpia contra el total de la planilla.
    suma = ventas["ventas"].sum()
    print(f"Suma limpia: {suma:,.2f} · Total de la planilla: {total:,.2f}")
    # No cierra: Pocitos-Febrero está como "-" en la tabla pero sí entró en el
    # total. La diferencia hay que explicarla, no taparla.
    diferencia = total - suma
    sin_dato = ventas.loc[ventas["ventas"].isna(), ["local", "mes"]]
    print(f"Diferencia: {diferencia:,.2f}, explicada por la fila sin dato:")
    print(sin_dato.to_string(index=False))
    assert round(diferencia, 2) == 1850.00 and len(sin_dato) == 1
