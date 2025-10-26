from flask import Flask, render_template, send_file
import os

# Importar funciones desde src/
from src.clean_missing_values import imputar_valores_faltantes
from src.resample_daily import convertir_a_consumo_diario
from src.plot_consumo_diario import graficar_consumo_diario
from src.normalize_consumo_diario import escalar_consumo_diario
from src.config_look_back import definir_look_back
from src.dataset_ventanas import create_dataset
from src.split_temporal import dividir_temporalmente
from src.reshape_lstm import adaptar_para_lstm
from src.modelo_lstm import construir_modelo_lstm
from src.compilar_modelo import compilar_modelo
from src.entrenar_modelo import entrenar_modelo
from src.evaluar_modelo import evaluar_modelo

import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/procesar')
def procesar():
    df = pd.read_csv("data/consumo.csv", parse_dates=True, index_col=0)
    df = imputar_valores_faltantes(df)
    df_diario = convertir_a_consumo_diario(df)
    graficar_consumo_diario(df_diario)
    df_normalizado = escalar_consumo_diario(df_diario)
    look_back = definir_look_back(df_normalizado)
    X, y = create_dataset(df_normalizado, look_back)
    X_train, X_test, y_train, y_test = dividir_temporalmente(X, y)
    X_train_lstm, X_test_lstm = adaptar_para_lstm(X_train, X_test)
    modelo = construir_modelo_lstm(look_back)
    compilar_modelo(modelo)
    history = entrenar_modelo(modelo, X_train_lstm, y_train, X_test_lstm, y_test)
    rmse, mae = evaluar_modelo(modelo, X_test_lstm, y_test)

    return f"""
    <h2>✅ Proceso completado</h2>
    <p>RMSE: {rmse:.4f}</p>
    <p>MAE: {mae:.4f}</p>
    <p><a href='/grafico/consumo'>Ver gráfico de consumo diario</a></p>
    <p><a href='/grafico/entrenamiento'>Ver gráfico de entrenamiento</a></p>
    <p><a href='/grafico/evaluacion'>Ver gráfico de evaluación</a></p>
    """

@app.route('/grafico/<tipo>')
def mostrar_grafico(tipo):
    rutas = {
        "consumo": "grafico_consumo_diario.png",
        "entrenamiento": "grafico_entrenamiento.png",
        "evaluacion": "grafico_evaluacion.png"
    }
    ruta = rutas.get(tipo)
    if ruta and os.path.exists(ruta):
        return send_file(ruta, mimetype='image/png')
    return f"❌ Gráfico '{tipo}' no encontrado."

if __name__ == '__main__':
    app.run(debug=True)
