# 02 · Quarto no está en el PATH

**Qué pasó.** Para renderizar los `.qmd` de clase, `quarto render` no funcionaba
desde la terminal aunque Quarto estaba instalado.

**Cómo se manifiesta.** `quarto --version` da "no se reconoce como nombre de un
cmdlet", igual que el error 01.

**Cómo se detectó.** Buscando el ejecutable en el disco:

```powershell
Get-ChildItem "C:\Program Files","$env:LOCALAPPDATA\Programs" -Filter quarto.exe -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
```

Si aparece, está instalado pero no en el PATH; si no aparece, no está instalado
(`winget install --id Posit.Quarto`).

**Cómo se arregló.** Agregando la carpeta `...\Quarto\bin` al PATH del usuario
una sola vez, y recargando el PATH en la ventana abierta (o cerrándola y
abriendo otra).

**Lección.** "No se reconoce el comando" casi nunca significa "no está
instalado": primero hay que buscar dónde está.
