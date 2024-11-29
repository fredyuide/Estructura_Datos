import time
from original_code.bubble_sort import bubble_sort
from optimized_code.quick_sort import quick_sort

# Generar una lista aleatoria para pruebas
arr = [64, 34, 25, 12, 22, 11, 90, 23, 45, 78, 89, 1]

# Medir el tiempo de ejecución de Bubble Sort
start = time.time()
bubble_sort(arr)
end = time.time()
print("Bubble Sort time:", end - start)

# Medir el tiempo de ejecución de Quick Sort
start = time.time()
quick_sort(arr)
end = time.time()
print("Quick Sort time:", end - start)
