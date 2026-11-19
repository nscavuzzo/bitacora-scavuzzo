"""Utilidades que fui necesitando en el curso.

Cada función tiene su caso de prueba en `test_utilidades.py`.
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd

VALORES_FALTANTES = {"", "na", "n/a", "nan", "null", "-", "s/d", "sin dato", "."}


def limpiar_numero(valor) -> float:
    """Convierte un número escrito "a mano" en float.

    Acepta coma decimal, punto de miles, espacios, signos de moneda y porcentaje.
    Devuelve NaN si el valor es un faltante escrito como texto ("NA", "-", "s/d").

    >>> limpiar_numero("1.234,5")
    1234.5
    >>> limpiar_numero("$ 12,30")
    12.3
    """
    if valor is None:
        return np.nan
    if isinstance(valor, (int, float, np.integer, np.floating)):
        return float(valor)
    texto = str(valor).strip().lower()
    if texto in VALORES_FALTANTES:
        return np.nan
    texto = re.sub(r"[^\d,.\-]", "", texto)  # saca $, %, espacios, letras
    if "," in texto and "." in texto:
        # El último separador es el decimal: "1.234,5" o "1,234.5"
        if texto.rfind(",") > texto.rfind("."):
            texto = texto.replace(".", "").replace(",", ".")
        else:
            texto = texto.replace(",", "")
    elif "," in texto:
        texto = texto.replace(",", ".")
    elif texto.count(".") > 1:
        texto = texto.replace(".", "")  # "1.234.567" son miles
    try:
        return float(texto)
    except ValueError:
        return np.nan


def resumen_faltantes(df: pd.DataFrame) -> pd.DataFrame:
    """Tabla con cantidad y porcentaje de faltantes por columna, de mayor a menor.

    Cuenta como faltante tanto NaN como el texto vacío "" (que pandas no cuenta
    como faltante y fue la causa de un error, ver errores/04).
    """
    faltan = df.isna() | df.apply(lambda c: c.astype(str).str.strip().eq(""))
    tabla = pd.DataFrame({
        "faltantes": faltan.sum(),
        "porcentaje": (faltan.mean() * 100).round(1),
    })
    return tabla.sort_values("faltantes", ascending=False)


def utc_a_montevideo(serie: pd.Series) -> pd.Series:
    """Pasa una columna de fechas en UTC (texto o datetime) a hora de Montevideo.

    Uruguay está en UTC-3 todo el año (sin horario de verano desde 2015).
    """
    fechas = pd.to_datetime(serie, utc=True)
    return fechas.dt.tz_convert("America/Montevideo")


def normalizar_texto(serie: pd.Series) -> pd.Series:
    """Minúsculas, sin tildes ni espacios sobrantes: para unir por nombres.

    "  Tres Cruces " y "tres cruces" pasan a ser iguales.
    """
    return (
        serie.astype(str)
        .str.strip()
        .str.lower()
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("ascii")
        .str.replace(r"\s+", " ", regex=True)
    )
