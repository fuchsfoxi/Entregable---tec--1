### ¿Qué va a ir aquí?

Versión **limpia** de `tienda_tecnologica.csv`, después de:
- tratar valores nulos
- revisar y corregir duplicados o valores anómalos
- calcular columnas nuevas (ej. totales, agregaciones)

Estos archivos SÍ se pueden regenerar y sobrescribir las veces que sea
necesario — a diferencia de `raw/`, aquí no hay problema en modificar.

### Cómo se genera

No se edita a mano. Sale de un notebook o de `src/data_processing.py`,
que lee desde `data/raw/tienda_tecnologica.csv` y escribe aquí el
resultado ya limpio.

### Reglas

- Si cambias la lógica de limpieza, vuelve a correr el proceso completo
  para regenerar el archivo — no edites el csv a mano para "parchar" un dato.
- Usa un nombre que dista qué transformación tiene, si terminas con más
  de una versión (ej. `tienda_tecnologica_limpio.csv`).