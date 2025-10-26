import numpy as np

def dividir_temporalmente(X, y, porcentaje_entrenamiento=0.8):
    """
    Divide los datos en entrenamiento y prueba de forma temporal (no aleatoria).
    Usa el porcentaje indicado para calcular el punto de corte.
    """
    total_muestras = len(X)
    corte = int(total_muestras * porcentaje_entrenamiento)

    X_train = X[:corte]
    y_train = y[:corte]
    X_test = X[corte:]
    y_test = y[corte:]

    print(f"📊 División temporal realizada:")
    print(f"- Total de muestras: {total_muestras}")
    print(f"- Entrenamiento: {len(X_train)} muestras")
    print(f"- Prueba: {len(X_test)} muestras")
    print("✅ No hay solapamiento: los datos de entrenamiento preceden cronológicamente a los de prueba.")

    return X_train, X_test, y_train, y_test
