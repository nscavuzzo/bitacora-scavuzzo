"""Receta 02 · Unir dos fuentes por fecha y hora.

Problema (Clases 7 a 10): el conteo de tránsito y la calidad de aire vienen en
archivos distintos, con frecuencias distintas (el aire cada pocos minutos, el
tránsito por hora) y las fechas en UTC. Para compararlas hay que llevarlas a la
misma escala de tiempo antes de unir.

Pasos:
1. Pasar las fechas a datetime y controlar la zona horaria contra el dato.
2. Llevar la serie más fina a la frecuencia de la más gruesa (resample a 1 hora).
3. Unir por estación y hora con un merge explícito y validar que no se dupliquen
   filas (validate="one_to_one").
4. Contar cuántas horas quedaron sin dato de cada lado.

Usa datos/transito_aire_junio2024.csv si está (ver datos/README.md); si no,
genera una muestra sintética con la misma estructura.
"""
import sys
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")  # sin ventana: el gráfico se guarda en salidas/
import matplotlib.pyplot as plt  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "funciones"))
from utilidades import utc_a_montevideo  # noqa: E402

ARCHIVO = RAIZ / "datos" / "transito_aire_junio2024.csv"
SALIDAS = RAIZ / "salidas"
SALIDAS.mkdir(exist_ok=True)


def datos_de_partida() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Devuelve (transito por hora, aire cada 10 minutos)."""
    if ARCHIVO.exists():
        d = pd.read_csv(ARCHIVO)
        transito = d[["estacion", "hora", "transito"]]
        # El archivo de clase ya viene por hora; lo paso a cada 10 minutos para
        # practicar el caso real, en que el aire viene más fino que el tránsito.
        aire = d[["estacion", "hora", "no2", "pm25"]].copy()
        aire["hora"] = pd.to_datetime(aire["hora"], utc=True)
        aire = aire.loc[aire.index.repeat(6)].copy()
        aire["hora"] += pd.to_timedelta(aire.groupby(level=0).cumcount() * 10, unit="min")
        print(f"Usando {ARCHIVO.name}")
        return transito, aire

    print("No está datos/transito_aire_junio2024.csv: uso una muestra sintética")
    rng = np.random.default_rng(314)
    horas = pd.date_range("2024-06-01", periods=24 * 7, freq="h", tz="UTC")
    filas_t, filas_a = [], []
    for est in ["Tres Cruces", "Curva de Maronias"]:
        hora_local = (horas.hour - 3) % 24
        nivel = 200 + 600 * np.exp(-((hora_local - 13) ** 2) / 20)
        filas_t.append(pd.DataFrame({"estacion": est, "hora": horas,
                                     "transito": rng.poisson(nivel)}))
        minutos = pd.date_range(horas[0], horas[-1], freq="10min")
        h_loc = (minutos.hour - 3) % 24
        no2 = 15 + 25 * np.exp(-((h_loc - 13) ** 2) / 20) + rng.normal(0, 3, len(minutos))
        filas_a.append(pd.DataFrame({"estacion": est, "hora": minutos, "no2": no2,
                                     "pm25": rng.gamma(2, 4, len(minutos))}))
    return pd.concat(filas_t), pd.concat(filas_a)


def unir(transito: pd.DataFrame, aire: pd.DataFrame) -> pd.DataFrame:
    # 1. Fechas con zona horaria
    transito = transito.assign(hora=pd.to_datetime(transito["hora"], utc=True))
    aire = aire.assign(hora=pd.to_datetime(aire["hora"], utc=True))

    # 2. Aire a promedios por hora
    aire_h = (aire.set_index("hora")
                  .groupby("estacion")[["no2", "pm25"]]
                  .resample("1h").mean()
                  .reset_index())

    # 3. Merge explícito y validado
    unido = transito.merge(aire_h, on=["estacion", "hora"], how="left",
                           validate="one_to_one")
    # La "Z" del archivo dice UTC, pero el perfil diario muestra que las horas
    # ya son locales (ver errores/06). Por eso no convierto: uso la hora como
    # viene. Si la fuente estuviera de verdad en UTC, iría utc_a_montevideo().
    unido["hora_local"] = unido["hora"].dt.tz_localize(None)
    return unido


def control_zona_horaria(unido: pd.DataFrame) -> None:
    """Chequea que el tránsito mínimo caiga de madrugada (entre 0 y 5 h)."""
    perfil = unido.groupby(unido["hora_local"].dt.hour)["transito"].mean()
    hora_min = perfil.idxmin()
    print(f"Control: el tránsito mínimo es a las {hora_min} h")
    assert 0 <= hora_min <= 5, "el mínimo no cae de madrugada: revisar zona horaria"
    convertida = utc_a_montevideo(unido["hora"])
    hora_min_conv = unido.groupby(convertida.dt.hour)["transito"].mean().idxmin()
    print(f"         si convirtiera desde UTC, sería a las {hora_min_conv} h")


if __name__ == "__main__":
    transito, aire = datos_de_partida()
    unido = unir(transito, aire)
    assert len(unido) == len(transito), "el merge duplicó o perdió filas"
    control_zona_horaria(unido)

    # 4. Cuántas horas quedaron sin dato de aire
    print(unido.groupby("estacion")[["no2", "pm25"]]
               .apply(lambda g: g.isna().mean().mul(100).round(1))
               .rename(columns=lambda c: f"% sin {c}"))

    # Perfil diario: tránsito y NO2 promedio por hora local
    est = unido.dropna(subset=["no2"])["estacion"].value_counts().idxmax()
    perfil = (unido[unido["estacion"] == est]
              .groupby(unido["hora_local"].dt.hour)[["transito", "no2"]].mean())
    fig, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(perfil.index, perfil["transito"], color="tab:gray", label="Tránsito")
    ax1.set_xlabel("Hora del día (Montevideo)")
    ax1.set_ylabel("Vehículos por hora")
    ax2 = ax1.twinx()
    ax2.plot(perfil.index, perfil["no2"], color="tab:red", label="NO2")
    ax2.set_ylabel("NO2")
    ax1.set_title(f"{est}: tránsito y NO2 promedio por hora")
    fig.tight_layout()
    fig.savefig(SALIDAS / "perfil_diario_transito_no2.png", dpi=120)
    print(f"\nGráfico en salidas/perfil_diario_transito_no2.png ({est})")
