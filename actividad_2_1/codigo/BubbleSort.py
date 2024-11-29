# BubbleSort.py
# Este script implementa el algoritmo de ordenamiento Bubble Sort.
# La función 'bubble_sort' recibe un arreglo de enteros y lo ordena en orden ascendente.

def bubble_sort(arr):
    """
    Ordena un arreglo de enteros utilizando el algoritmo de Bubble Sort.

    Parámetros:
    arr (list): Un arreglo de enteros.

    Retorna:
    list: El arreglo ordenado en orden ascendente.
    """
    n = len(arr)
    # Recorremos el arreglo en pasadas sucesivas
    for i in range(n):
        swapped = False  # Variable para verificar si hubo intercambios en la pasada
        # Recorremos el arreglo desde el principio hasta la posición n - i - 1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # Si el elemento actual es mayor que el siguiente, se intercambian
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Si no hubo intercambios, el arreglo ya está ordenado
        if not swapped:
            break
    return arr

# Pruebas unitarias
if __name__ == "__main__":
    # Casos de prueba para verificar la funcionalidad
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # Esperado: [11, 12, 22, 25, 34, 64, 90]
    print(bubble_sort([1, 2, 3, 4, 5]))               # Esperado: [1, 2, 3, 4, 5] (arreglo ya ordenado)
    print(bubble_sort([5, 4, 3, 2, 1]))               # Esperado: [1, 2, 3, 4, 5] (arreglo en orden inverso)
    print(bubble_sort([1]))                           # Esperado: [1] (arreglo con un solo elemento)
