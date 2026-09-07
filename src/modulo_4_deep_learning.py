import os
import pickle
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def limpiar_calificacion(valor):
    if valor == "Desconocido":
        return np.nan
    return abs(float(str(valor).replace(",", ".")))


def entrenar_modelo_dl(data_path="../data/processed/tienda_tecnologica_limpio.csv"):
    """Entrena la red neuronal y el modelo de comparación, guarda ambos en disco."""
    df = pd.read_csv(data_path)
    df["calificacion_limpia"] = df["calificacion"].apply(limpiar_calificacion)
    df = df.dropna(subset=["calificacion_limpia"])
    df["sentimiento"] = (df["calificacion_limpia"] >= 3).astype(int)

    X_raw = df["opinion_usuario"].fillna("").astype(str)
    y = df["sentimiento"].values

    vectorizer = TfidfVectorizer(max_features=5000)
    X_vectorized = vectorizer.fit_transform(X_raw).toarray()

    X_train, X_test, y_train, y_test = train_test_split(
        X_vectorized, y, test_size=0.2, random_state=42, stratify=y
    )

    model = keras.Sequential([
        layers.Input(shape=(X_train.shape[1],)),
        layers.Dense(128, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(64, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(1, activation="sigmoid")
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2, verbose=1)
    loss, accuracy = model.evaluate(X_test, y_test)

    modelo_tradicional = LogisticRegression(max_iter=1000)
    modelo_tradicional.fit(X_train, y_train)
    accuracy_tradicional = modelo_tradicional.score(X_test, y_test)

    os.makedirs("../models", exist_ok=True)
    model.save("../models/neural_network.h5")
    with open("../models/tfidf_vectorizer_dl.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    return {"accuracy_red_neuronal": accuracy, "accuracy_tradicional": accuracy_tradicional}


def predecir_sentimiento_dl(texto):
    """Carga el modelo y vectorizador ya entrenados, predice sentimiento de un texto nuevo."""
    model = keras.models.load_model("../models/neural_network.h5")
    with open("../models/tfidf_vectorizer_dl.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    X = vectorizer.transform([texto]).toarray()
    probabilidad = model.predict(X)[0][0]
    sentimiento = "POSITIVO" if probabilidad >= 0.5 else "NEGATIVO"
    return sentimiento, float(probabilidad)