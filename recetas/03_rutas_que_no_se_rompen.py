"""Receta 03 · Rutas que no se rompen.

Problema (Clases 3 y 4): un script que funciona en la PC de la profesora falla
en la mía con FileNotFoundError, porque usa rutas relativas a "donde estoy
parado" (os.getcwd()) y cada uno lo corre desde una carpeta distinta, o porque
usa os.chdir("clases/clase4"), que depende de dónde se abrió la terminal.

Solución: armar las rutas a partir de la ubicación del propio script
(__file__), con pathlib. Así el script corre igual desde cualquier carpeta.
"""
import os
from pathlib import Path

# Mal: depende de desde dónde se corre
print("Carpeta actual (cambia según dónde abra la terminal):", os.getcwd())

# Bien: depende de dónde está el archivo, que no cambia
AQUI = Path(__file__).resolve().parent      # .../recetas
RAIZ = AQUI.parent                          # raíz de la bitácora
DATOS = RAIZ / "datos"
print("Raíz de la bitácora (siempre la misma):", RAIZ)

# Buscar archivos sin escribir rutas a mano
scripts = sorted(p.name for p in AQUI.glob("*.py"))
print("Recetas encontradas:", scripts)

# Antes de leer, chequear que exista y dar un mensaje que sirva
archivo = DATOS / "transito_aire_junio2024.csv"
if archivo.exists():
    print("Datos encontrados:", archivo.relative_to(RAIZ))
else:
    print(f"Falta {archivo.relative_to(RAIZ)}: ver datos/README.md para obtenerlo")

assert AQUI.name == "recetas"
