import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

def evaluar_modelo(modelo, X_test, y_test):
    """
    Evalúa el modelo LSTM sobre los datos de prueba.
    Calcula métricas de error y genera un gráfico comparando valores reales vs. predichos.
    """
    # Evaluación directa
    loss = modelo.evaluate(X_test, y_test, verbose=0)
    print(f"📉 Pérdida (MSE) en test: {loss:.4f}")

    # Predicciones
    y_pred = modelo.predict(X_test)

    # Métricas
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    print(f"✅ RMSE: {rmse:.4f}")
    print(f"✅ MAE:  {mae:.4f}")

    # Gráfico comparativo
    plt.figure(figsize=(12, 5))
    plt.plot(y_test, label='Real', color='steelblue')
    plt.plot(y_pred, label='Predicho', color='orange')
    plt.title('Comparación entre valores reales y predichos')
    plt.xlabel('Índice de muestra')
    plt.ylabel('Consumo normalizado')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafico_evaluacion.png")
    print("📊 Gráfico guardado como 'grafico_evaluacion.png'.")

    return rmse, mae
