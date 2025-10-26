import pandas as pd

def cargar_consumo_electrico(ruta_csv):
    """
    Carga el dataset de consumo eléctrico, convierte la columna de tiempo a datetime
    y la establece como índice del DataFrame.
    """
    try:
        # Leer el CSV
        df = pd.read_csv(ruta_csv, sep=';', low_memory=False)

        # Combinar columnas de fecha y hora si existen
        if 'Date' in df.columns and 'Time' in df.columns:
            df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d/%m/%Y %H:%M:%S')
            df.drop(columns=['Date', 'Time'], inplace=True)
        elif 'Datetime' in df.columns:
            df['Datetime'] = pd.to_datetime(df['Datetime'])
        else:
            raise ValueError("No se encontró una columna de tiempo válida.")

        # Establecer índice temporal
        df.set_index('Datetime', inplace=True)

        print("✅ Dataset cargado correctamente con índice temporal.")
        return df

    except Exception as e:
        print(f"❌ Error al cargar el dataset: {e}")
        return None

