import tensorflow as tf

def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def predict_waiting_time(model, process_data):
    # Simula la predicción con datos básicos
    input_data = [[process_data['priority'], process_data['arrival_time'], process_data['execution_time']]]
    return model.predict(input_data)[0][0]

