import matplotlib.pyplot as plt

def entrenar_modelo(modelo, X_train, y_train, X_test, y_test, epochs=75, batch_size=32):
    """
    Entrena el modelo LSTM y grafica la evolución de la pérdida (train vs. validation).
    Guarda el historial y la figura como evidencia.
    """
    history = modelo.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(X_test, y_test),
        verbose=1
    )

    # Graficar la pérdida
    plt.figure(figsize=(10, 5))
    plt.plot(history.history['loss'], label='Entrenamiento', color='steelblue')
    plt.plot(history.history['val_loss'], label='Validación', color='orange')
    plt.title('Evolución de la pérdida durante el entrenamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Error (MSE)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafico_entrenamiento.png")
    print("📉 Gráfico de pérdida guardado como 'grafico_entrenamiento.png'.")

    return history
