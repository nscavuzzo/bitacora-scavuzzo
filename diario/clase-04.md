# Clase 4 · De la fuente al DataFrame

**Qué se intentó.** Cargar datos abiertos en R y en Python, con rutas a las carpetas de cada clase.

**Qué falló.** Las rutas de los scripts de clase (`os.chdir("clases/clase4")`) no existían en mi carpeta: `FileNotFoundError` (`errores/05`).

**Qué se decidió.** Armar las rutas desde la ubicación del script con `pathlib` (`recetas/03`). Documentar de cada fuente el origen y la cantidad de registros.
