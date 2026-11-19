# 01 · `pip` no se reconoce

**Qué pasó.** Al instalar paquetes con `pip install pandas` en la terminal de
Windows (PowerShell), el comando no existía.

**Cómo se manifiesta.**

```
pip : El término 'pip' no se reconoce como nombre de un cmdlet, función,
archivo de script o programa ejecutable.
```

A veces también `python --version` responde *"Python was not found; run without
arguments to install from the Microsoft Store"*: es el acceso directo de la
Microsoft Store, no el Python instalado.

**Cómo se detectó.** Probando `py --version`: si responde con la versión, Python
está instalado pero su carpeta no está en el PATH.

**Cómo se arregló.** Llamar a pip a través de Python, que siempre usa el pip del
Python correcto:

```
py -m pip install pandas        # Windows
python3 -m pip install pandas   # macOS
```

**Para no repetirlo.** Usar siempre `python -m pip` (o `py -m pip`), nunca `pip`
suelto. Referencia: guía de la Clase 2, *Problema con Python: no se reconoce el
comando pip*.
