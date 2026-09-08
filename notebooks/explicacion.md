### ¿Qué va a ir aquí?

Un notebook por módulo, para explorar y prototipar antes de pasar el
código ya probado a `src/`. Aquí SÍ se permite ensayo y error — no hace
falta que quede "limpio", es tu espacio de trabajo.

### Notebooks del proyecto

- `modulo_1.ipynb` — Limpieza de `tienda_tecnologica.csv`, cálculos
  (ventas totales, promedio, producto más vendido, categoría más
  rentable) y dashboard estadístico.

- `modulo_2.ipynb` — Entrena y compara Regresión Lineal, Random Forest
  y Decision Tree para predecir ventas.

- `modulo_3.ipynb` — NLP con NLTK + Scikit-Learn para clasificar
  comentarios como POSITIVO/NEGATIVO.

- `modulo_4.ipynb` — Red neuronal con TensorFlow/Keras para la misma
  tarea de sentimientos, comparada contra el Módulo 3.

- `modulo_5_pruebas_estadisticas.ipynb` — Pruebas de hipótesis (p-value)
  que respaldan las conclusiones del informe final.

### Reglas

- Todos los nombres de archivo van en minúsculas, sin acentos ni
  mayúsculas — evita problemas al clonar el repo entre distintos
  sistemas operativos (Windows/Mac no distinguen mayúsculas de
  minúsculas en rutas, Linux sí).
- Cada quien trabaja en el notebook de su módulo — evita tocar el de
  otro sin avisar, para no generar conflictos al subir a git.
- Cuando una función ya funciona y la vas a necesitar en otro módulo o
  en la app de Streamlit, muévela a `src/` como función reutilizable —
  no la dejes solo dentro del notebook.
- Antes de subir cambios, corre el notebook completo de arriba a abajo
  una vez ("Restart & Run All") para confirmar que funciona en orden y
  no solo porque ejecutaste las celdas en un orden distinto sin darte
  cuenta.
- No subas notebooks con celdas que fallan o con salidas de error
  visibles.