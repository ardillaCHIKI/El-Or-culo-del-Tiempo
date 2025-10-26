import numpy as np
import pandas as pd

def create_dataset(dataset, look_back):
    """
    Transforma una serie temporal en pares (X, y) usando ventanas móviles.
    Cada X contiene 'look_back' días, y cada y el valor del día siguiente.
    """
    if isinstance(dataset, pd.DataFrame):
        serie = dataset.iloc[:, 0].values  # Asume que la serie está en la primera columna
    elif isinstance(dataset, pd.Series):
        serie = dataset.values
    else:
        raise TypeError("El dataset debe ser un DataFrame o Series de pandas.")

    X, y = [], []
    for i in range(len(serie) - look_back):
        X.append(serie[i:i + look_back])
        y.append(serie[i + look_back])

    X = np.array(X)
    y = np.array(y)

    print(f"✅ Dataset transformado con éxito:")
    print(f"- X shape: {X.shape} (muestras, {look_back})")
    print(f"- y shape: {y.shape} (muestras,)")

    return X, y
