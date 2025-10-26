from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def construir_modelo_lstm(look_back):
    """
    Construye una red LSTM con dos capas apiladas y una capa densa de salida.
    """
    modelo = Sequential()
    modelo.add(LSTM(50, return_sequences=True, input_shape=(look_back, 1)))
    modelo.add(LSTM(50, return_sequences=False))
    modelo.add(Dense(1))

    modelo.summary()
    return modelo
