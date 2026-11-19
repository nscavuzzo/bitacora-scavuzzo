"""Casos de prueba de utilidades.py. Correr con: python funciones/test_utilidades.py

Los resultados esperados están calculados a mano.
"""
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utilidades import limpiar_numero, normalizar_texto, resumen_faltantes, utc_a_montevideo  # noqa: E402


def test_limpiar_numero():
    assert limpiar_numero("1.234,5") == 1234.5
    assert limpiar_numero("1,234.5") == 1234.5
    assert limpiar_numero("$ 12,30") == 12.3
    assert limpiar_numero("45%") == 45.0
    assert limpiar_numero("1.234.567") == 1234567.0
    assert limpiar_numero(7) == 7.0
    assert math.isnan(limpiar_numero("NA"))
    assert math.isnan(limpiar_numero("s/d"))
    assert math.isnan(limpiar_numero(None))


def test_resumen_faltantes():
    df = pd.DataFrame({
        "a": [1, np.nan, 3, np.nan],     # 2 faltantes -> 50 %
        "b": ["x", "", "y", "z"],         # 1 texto vacío -> 25 %
        "c": [1, 2, 3, 4],                # 0 faltantes
    })
    r = resumen_faltantes(df)
    assert list(r.index) == ["a", "b", "c"]
    assert list(r["faltantes"]) == [2, 1, 0]
    assert list(r["porcentaje"]) == [50.0, 25.0, 0.0]


def test_utc_a_montevideo():
    r = utc_a_montevideo(pd.Series(["2024-06-01T03:00:00Z"]))
    # 03:00 UTC son las 00:00 en Montevideo (UTC-3)
    assert r.iloc[0].hour == 0
    assert r.iloc[0].day == 1


def test_normalizar_texto():
    r = normalizar_texto(pd.Series(["  Museo Romántico ", "museo   romantico"]))
    assert r.iloc[0] == r.iloc[1] == "museo romantico"


if __name__ == "__main__":
    pruebas = [v for k, v in dict(globals()).items() if k.startswith("test_")]
    for prueba in pruebas:
        prueba()
        print(f"ok  {prueba.__name__}")
    print(f"{len(pruebas)} pruebas pasaron")
