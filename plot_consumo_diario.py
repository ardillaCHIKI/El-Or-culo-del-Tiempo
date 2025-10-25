import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graficar_consumo_diario(df_diario):
    """
    Genera un gráfico de línea del consumo eléctrico diario.
    Identifica visualmente tendencias, picos y estacionalidad.
    Guarda la figura como 'grafico_consumo_diario.png'.
    """
    if not isinstance(df_diario.index, pd.DatetimeIndex):
        raise ValueError("El índice debe ser datetime para graficar series temporales.")

    plt.figure(figsize=(14, 6))
    sns.lineplot(data=df_diario, x=df_diario.index, y=df_diario.iloc[:, 0], color='steelblue')

    plt.title("Consumo eléctrico diario", fontsize=16)
    plt.xlabel("Fecha", fontsize=12)
    plt.ylabel("Consumo total", fontsize=12)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("grafico_consumo_diario.png")
    print("📊 Gráfico guardado como 'grafico_consumo_diario.png'.")
