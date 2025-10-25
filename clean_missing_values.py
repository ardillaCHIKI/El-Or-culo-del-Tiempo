import pandas as pd

def imputar_valores_faltantes(df):
    """
    Detecta valores nulos, los imputa usando forward fill y valida que no queden nulos.
    """
    print("🔍 Valores nulos por columna antes de imputar:")
    print(df.isna().sum())

    # Imputación con forward fill
    df_imputado = df.fillna(method='ffill')

    # Validación
    nulos_restantes = df_imputado.isna().sum().sum()
    if nulos_restantes == 0:
        print("✅ No quedan valores nulos tras la imputación.")
    else:
        print(f"⚠️ Quedan {nulos_restantes} valores nulos tras la imputación.")

    return df_imputado

