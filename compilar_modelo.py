def compilar_modelo(modelo):
    """
    Compila el modelo LSTM para regresión usando el optimizador Adam y la pérdida MSE.
    """
    modelo.compile(optimizer='adam', loss='mean_squared_error')
    print("✅ Modelo compilado correctamente y listo para entrenamiento.")
