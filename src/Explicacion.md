### ¿Qué va a ir aquí?

Código ya probado y reutilizable, "graduado" desde los notebooks. Aquí no
se experimenta — si algo todavía está en pruebas, va en `notebooks/`, no
aquí.

### Archivos y a qué módulo pertenecen

- `data_processing.py` — Limpieza, nuevas columnas, agregaciones. Es
  transversal: todos los módulos dependen de datos ya procesados por
  aquí (lee de `data/raw/`, escribe en `data/processed/`).
- `dashboard.py` — Funciones de gráficos del Módulo 1 (Matplotlib/Seaborn),
  usadas luego por `app/pages/1_Dashboard.py`.
- `ml_models.py` — Entrenamiento y predicción de los 3 algoritmos del
  Módulo 2 (Regresión Lineal, Random Forest, Decision Tree).
- `sentiment_analysis.py` — Vectorización de texto y clasificación de
  sentimientos del Módulo 3.
- `deep_learning.py` — Definición y entrenamiento de la red neuronal del
  Módulo 4.
- `stats_tests.py` — Pruebas estadísticas con SciPy, soporta al notebook
  `05_pruebas_estadisticas_scipy.ipynb`.
- `recommendations.py` — No corresponde a ningún módulo del curso: lógica
  propia que combina resultados de varios módulos para el "Asistente de
  Decisiones" (`app/pages/4_Asistente_Decisiones.py`).

### Reglas

- Cuando una función de un notebook ya funciona y la necesitas en otro
  módulo o en la app, muévela aquí en vez de copiar/pegar el código.
- Cada archivo aquí debe