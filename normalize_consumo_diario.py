import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def escalar_consumo_diario(df_diario):
    """
    Escala los valores del consumo diario al rango [0, 1] usando MinMaxScaler.
    Guarda los parámetros de normalización y verifica el rango.
    """
    if not isinstance(df_diario.index, pd.DatetimeIndex):
        raise ValueError("El índice debe ser datetime para mantener la estructura temporal.")

    # Seleccionar la columna de consumo (asumimos que es la primera)
    consumo = df_diario.iloc[:, 0].values.reshape(-1, 1)

    # Escalado
    scaler = MinMaxScaler()
    consumo_normalizado = scaler.fit_transform(consumo)

    # Crear nuevo DataFrame con índice original
    df_normalizado = pd.DataFrame(consumo_normalizado, index=df_diario.index, columns=['Consumo_normalizado'])

    # Verificación
    rango_valores = (df_normalizado.min().values[0], df_normalizado.max().values[0])
    if 0 <= rango_valores[0] <= 1 and 0 <= rango_valores[1] <= 1:
        print(f"✅ Escalado correcto. Rango: {rango_valores}")
    else:
        print(f"⚠️ Rango fuera de [0, 1]: {rango_valores}")

    # Guardar parámetros de normalización
    min_valor = scaler.data_min_[0]
    max_valor = scaler.data_max_[0]
    with open("parametros_normalizacion.txt", "w") as f:
        f.write(f"Min: {min_valor}\nMax: {max_valor}\n")
    print("📄 Parámetros guardados en 'parametros_normalizacion.txt'.")

    return df_normalizado
