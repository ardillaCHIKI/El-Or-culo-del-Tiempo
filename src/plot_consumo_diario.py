import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graficar_consumo_diario(df_diario):
    plt.figure(figsize=(10, 5))
    plt.plot(df_diario.index, df_diario.values, color='steelblue')
    plt.title("Consumo diario")
    plt.xlabel("Fecha")
    plt.ylabel("Consumo")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("grafico_consumo_diario.png")
    print("📊 Gráfico guardado como 'grafico_consumo_diario.png'.")
