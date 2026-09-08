import re

import nltk
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# NLTK convierte las palabras a su raíz.
stemmer = SnowballStemmer("spanish")


def limpiar(texto):
    palabras = re.findall(r"[a-záéíóúüñ]+", str(texto).lower())
    return " ".join(stemmer.stem(palabra) for palabra in palabras)


# 1. Cargar el archivo de opiniones.
datos = pd.read_csv("tienda_tecnologica_limpio.csv", encoding="utf-8-sig")

# 2. Convertir la calificación en sentimiento.
datos["calificacion"] = pd.to_numeric(
    datos["calificacion"].astype(str).str.replace(",", ".", regex=False),
    errors="coerce",
)
datos = datos.dropna(subset=["calificacion", "opinion_usuario"])
datos = datos[datos["calificacion"].between(1, 5)]

datos["sentimiento"] = datos["calificacion"].apply(
    lambda nota: "POSITIVO" if nota >= 4 else "NEGATIVO" if nota <= 2 else "NEUTRO"
)

# 3. Separar datos para aprender y probar.
opiniones_entrenamiento, opiniones_prueba, sentimientos_entrenamiento, sentimientos_prueba = train_test_split(
    datos["opinion_usuario"],
    datos["sentimiento"],
    test_size=0.2,
    random_state=42,
)

# 4. Convertir texto en números y entrenar el modelo.
vectorizador = TfidfVectorizer(preprocessor=limpiar)
x_entrenamiento = vectorizador.fit_transform(opiniones_entrenamiento)
x_prueba = vectorizador.transform(opiniones_prueba)

modelo = LogisticRegression(max_iter=1000)
modelo.fit(x_entrenamiento, sentimientos_entrenamiento)

print("Precisión:", round(modelo.score(x_prueba, sentimientos_prueba) * 100, 2), "%")

# 5. Predecir una opinión nueva.
opinion_nueva = "El pedido llegó rápido y el repartidor fue amable"
x_nueva = vectorizador.transform([opinion_nueva])
sentimiento = modelo.predict(x_nueva)[0]
probabilidad = modelo.predict_proba(x_nueva).max() * 100

print("Opinión:", opinion_nueva)
print("Sentimiento:", sentimiento)
print("Probabilidad:", round(probabilidad), "%")
