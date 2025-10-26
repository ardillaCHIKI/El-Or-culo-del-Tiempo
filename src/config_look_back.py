def definir_look_back(df_diario, valor_inicial=60):
    """
    Define el parámetro look_back para modelado temporal.
    Justifica su elección y documenta su impacto en los conjuntos X e y.
    """
    look_back = valor_inicial
    print(f"📌 Parámetro look_back definido: {look_back} días")

    # Justificación
    print("🧠 Justificación:")
    print("- 60 días permiten capturar patrones mensuales y bimensuales.")
    print("- Es un punto de partida razonable para detectar estacionalidad sin sobrecargar el modelo.")
    print("- Puede ajustarse tras evaluar el rendimiento del modelo.")

    # Impacto en X e y
    total_dias = len(df_diario)
    muestras_posibles = total_dias - look_back
    print(f"\n📊 Con {total_dias} días de datos y look_back = {look_back}:")
    print(f"- Se pueden generar {muestras_posibles} pares (X, y) para entrenamiento.")
    print("- Cada X tendrá forma (look_back, 1) y cada y será un escalar del día siguiente.")

    return look_back
