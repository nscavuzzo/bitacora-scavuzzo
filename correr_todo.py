"""Corre las pruebas de funciones/ y todas las recetas. Si algo falla, lo dice.

Uso: python correr_todo.py
"""
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
scripts = [RAIZ / "funciones" / "test_utilidades.py", *sorted((RAIZ / "recetas").glob("*.py"))]

fallaron = []
for script in scripts:
    r = subprocess.run([sys.executable, str(script)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    estado = "ok   " if r.returncode == 0 else "FALLA"
    print(f"{estado} {script.relative_to(RAIZ)}")
    if r.returncode != 0:
        fallaron.append(script.name)
        print(r.stderr[-1500:])

print(f"\n{len(scripts) - len(fallaron)} de {len(scripts)} scripts corrieron bien")
sys.exit(1 if fallaron else 0)
