from queue import PriorityQueue
from ai_model import load_model, predict_waiting_time

def main():
    # Inicializa la cola de prioridad
    pq = PriorityQueue()

    # Carga el modelo entrenado
    model = load_model('models/priority_model.h5')

    # Ejemplo de procesos con prioridad dinámica
    processes = [
        {"id": 1, "priority": 2, "arrival_time": 0, "execution_time": 5},
        {"id": 2, "priority": 1, "arrival_time": 2, "execution_time": 3},
        {"id": 3, "priority": 3, "arrival_time": 4, "execution_time": 1},
    ]

    for process in processes:
        predicted_time = predict_waiting_time(model, process)
        pq.put((process['priority'], process['id'], predicted_time))

    while not pq.empty():
        _, process_id, predicted_time = pq.get()
        print(f"Procesando ID: {process_id} con tiempo estimado: {predicted_time}s")

if __name__ == "__main__":
    main()

