### ¿Qué va a ir aquí?

La aplicación final en Streamlit — lo que la empresa realmente va a usar.
Esta carpeta NO entrena ni calcula nada desde cero: solo carga los modelos
ya guardados en `models/` y las funciones ya listas en `src/`, y las
muestra en una interfaz.

### Archivos y estructura

- `main.py` — Punto de entrada de la app. Arma el menú de navegación entre
  las páginas de `pages/`.
- `pages/` — Streamlit convierte automáticamente cada archivo de aquí en
  una página con su propio botón de navegación. El número al inicio del
  nombre define el orden en el menú:
  - `1_Dashboard.py` — usa `src/dashboard.py` (Módulo 1)
  - `2_Prediccion.py` — usa `src/ml_models.py` + `models/ml_model.pkl` (Módulo 2)
  - `3_Analisis_Opiniones.py` — usa `src/sentiment_analysis.py` +
    `models/sentiment_model.pkl` + `models/tfidf_vectorizer.pkl` (Módulo 3)
  - `4_Asistente_Decisiones.py` — usa `src/recommendations.py`, combina
    resultados de varios módulos
- `utils.py` — Helpers específicos de la interfaz (formateo de textos,
  widgets repetidos entre páginas). No lógica de negocio ni de modelos.

### Reglas

- No entrenar modelos aquí — si una página necesita un modelo, debe cargar
  el `.pkl`/`.h5` ya guardado en `models/`, nunca reentrenar al vuelo.
- No poner lógica de cálculo directo en los archivos de `pages/` — esa
  lógica va en `src/`; aquí solo se llama y se muestra.
- Si agregas una página nueva, sigue la convención de numeración
  (`5_algo.py`) para que aparezca en el orden correcto del menú.