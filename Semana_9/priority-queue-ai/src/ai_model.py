import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Cargar datos de entrenamiento
data = pd.read_csv('data/training_data.csv')
X = data[['priority', 'arrival_time', 'execution_time']]
y = data['waiting_time']

# Crear modelo de red neuronal
model = Sequential([
    Dense(16, input_dim=3, activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='linear')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Entrenar el modelo
model.fit(X, y, epochs=50, batch_size=8, verbose=1)

# Guardar el modelo entrenado
model.save('models/priority_model.h5')
print("Modelo guardado en 'models/priority_model.h5'")
