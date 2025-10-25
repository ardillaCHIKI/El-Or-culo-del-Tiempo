import pandas as pd

def convertir_a_consumo_diario(df):
    """
    Convierte datos horarios en consumo diario total usando resample('D').sum().
    Verifica la coherencia de fechas y guarda el resultado.
    """
    if not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("El índice del DataFrame debe ser de tipo datetime.")

    # Re-sampleo diario
    df_diario = df.resample('D').sum()

    # Verificación de discontinuidades
    dias_faltantes = df_diario.index.to_series().diff().dt.days.gt(1).sum()
    if dias_faltantes > 0:
        print(f"⚠️ Se detectaron {dias_faltantes} discontinuidades en la serie temporal.")
    else:
        print("✅ Serie temporal diaria generada sin discontinuidades.")

    # Guardar el resultado
    df_diario.to_csv("consumo_diario.csv")
    print("📁 Archivo 'consumo_diario.csv' guardado correctamente.")

    return df_diario
