# Clase 10 · ¿El tránsito ensucia el aire?

**Qué se intentó.** Unir el conteo vehicular con NO2 y PM2.5 por estación y hora, junio de 2024.

**Qué falló.** El NO2 se mide solo en dos de las tres estaciones, y en Tres Cruces falta casi el 60 % de las horas. Además, al pasar las horas de UTC a hora local el tránsito subía a las 3 de la mañana (`errores/06`).

**Qué se decidió.** Elegir la estación por los datos que tiene, no por el nombre. Controlar la zona horaria contra algo conocido; dejar las horas como vienen y anotarlo como pendiente.
