import matplotlib.pyplot as plt
import time
from original_code.bubble_sort import bubble_sort
from optimized_code.quick_sort import quick_sort

# Lista de tamaños de entrada
sizes = [100, 1000, 10000]
bubble_sort_times = []
quick_sort_times = []

for size in sizes:
    arr = list(range(size, 0, -1))  # Crear lista de tamaño 'size' en orden descendente

    # Medir el tiempo de ejecución de Bubble Sort
    start = time.time()
    bubble_sort(arr)
    end = time.time()
    bubble_sort_times.append(end - start)

    # Medir el tiempo de ejecución de Quick Sort
    start = time.time()
    quick_sort(arr)
    end = time.time()
    quick_sort_times.append(end - start)

# Crear el gráfico
plt.plot(sizes, bubble_sort_times, label="Bubble Sort")
plt.plot(sizes, quick_sort_times, label="Quick Sort")
plt.xlabel("Tamaño de lista (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de tiempos de ejecución")
plt.legend()
plt.show()
