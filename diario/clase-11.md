# Clase 11 · Asistentes de IA para leer datos

**Qué se intentó.** Mandar la foto de un ticket a un modelo (Groq) por su API y recibir una tabla.

**Qué falló.** La clave de la API se guarda en un `.txt` en la misma carpeta: si esa carpeta se sube a GitHub, la clave queda pública.

**Qué se decidió.** Las claves nunca van al repositorio: `.gitignore` con `*clave*.txt`. Y toda salida de la IA se verifica contra el ticket.
