# 05 · Rutas relativas que se rompen

**Qué pasó.** Los scripts de clase traen rutas como
`os.chdir("clases/clase4")` o `Path.cwd() / "clases/clase10"`. En mi carpeta
la estructura es otra, así que fallaban.

**Cómo se manifiesta.**

```
FileNotFoundError: [WinError 2] El sistema no puede encontrar el archivo especificado: 'clases/clase4'
```

O peor: el script corre una vez y la siguiente falla, porque `os.chdir` ya había
cambiado la carpeta de trabajo.

**Cómo se detectó.** Imprimiendo `os.getcwd()` justo antes de leer: la carpeta
actual no era la que el script suponía.

**Cómo se arregló.** Armando las rutas desde la ubicación del script, no desde
la carpeta actual:

```python
from pathlib import Path
RAIZ = Path(__file__).resolve().parent
datos = RAIZ / "datos" / "archivo.csv"
```

Ver `recetas/03_rutas_que_no_se_rompen.py`.
