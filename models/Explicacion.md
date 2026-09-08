### ¿Qué va a ir aquí?

Modelos ya entrenados, guardados en disco para no reentrenar cada vez que
se abre la app de Streamlit. Cargar un modelo guardado toma milisegundos;
reentrenarlo puede tomar minutos.

### Archivos esperados

- `ml_model.pkl` — Modelo del Módulo 2 (ventas). Pendiente de decidir: si
  se guarda solo el ganador de los 3 algoritmos comparados (Regresión
  Lineal, Random Forest, Decision Tree) o los tres por separado.
- `neural_network.h5` — Red neuronal del Módulo 4 (sentimientos).
- `sentiment_model.pkl` — Modelo del Módulo 3 (sentimientos, clásico).
- `tfidf_vectorizer.pkl` — Vectorizador de texto del Módulo 3. Obligatorio
  guardarlo junto con el modelo: sin él no se puede transformar un
  comentario nuevo de la misma forma que los datos de entrenamiento, y la
  predicción sale mal o falla.

### ¿Por qué dos formatos distintos (.pkl y .h5)?

- **.pkl (Pickle)** — para los modelos de Scikit-Learn (Regresión Lineal,
  Random Forest, Decision Tree, y el modelo/vectorizador de sentimientos).
  Son modelos con una estructura simple (reglas, coeficientes, pesos de
  palabras), así que Pickle, el mecanismo genérico de Python para guardar
  cualquier objeto, es suficiente.

- **.h5 (HDF5)** — para la red neuronal de Keras/TensorFlow. Una red
  neuronal es más pesada: guarda la arquitectura (capas, neuronas,
  funciones de activación), los pesos (potencialmente millones de
  números) y el estado del optimizador. HDF5 está hecho para guardar
  de forma eficiente este tipo de dato numérico jerárquico, por eso
  Keras lo usa como formato nativo en vez de Pickle.

Regla simple: si el modelo es de Scikit-Learn → `.pkl`. Si es de
Keras/TensorFlow → `.h5`.

### Reglas

- No se edita nada aquí a mano — estos archivos se generan solo desde un
  notebook o script (`pickle.dump()` / `model.save()`).
- Si reentrenas un modelo con datos nuevos, sobrescribe el archivo
  correspondiente y avisa al equipo (la app cargará la versión más reciente
  automáticamente).
- Si cambias la arquitectura del modelo (ej. otras columnas de entrada),
  el `.pkl`/`.h5` viejo ya no sirve — bórralo y regenera, no lo dejes
  mezclado con el nuevo.