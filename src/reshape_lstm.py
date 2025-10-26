import numpy as np

def adaptar_para_lstm(X_train, X_test):
    """
    Reestructura los conjuntos X_train y X_test al formato requerido por LSTM: [muestras, pasos_de_tiempo, características].
    """
    # Verifica que X tiene 2 dimensiones: [muestras, pasos_de_tiempo]
    if X_train.ndim != 2 or X_test.ndim != 2:
        raise ValueError("X_train y X_test deben tener forma (muestras, pasos_de_tiempo) antes del reshape.")

    # Reshape para LSTM: se añade la dimensión de características (1)
    X_train_lstm = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_test_lstm = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

    print("✅ Datos adaptados para LSTM:")
    print(f"- X_train shape: {X_train_lstm.shape} (muestras, pasos_de_tiempo, características)")
    print(f"- X_test shape:  {X_test_lstm.shape} (muestras, pasos_de_tiempo, características)")
    print("📌 Cada muestra representa una secuencia de días con una única variable de entrada.")

    return X_train_lstm, X_test_lstm
