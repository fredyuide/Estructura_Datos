# SelectionSort.py
# Este script implementa el algoritmo de ordenamiento Selection Sort.
# La función 'selection_sort' recibe un arreglo de enteros y lo ordena en orden ascendente.

def selection_sort(arr):
    """
    Ordena un arreglo de enteros utilizando el algoritmo de Selection Sort.

    Parámetros:
    arr (list): Un arreglo de enteros.

    Retorna:
    list: El arreglo ordenado en orden ascendente.
    """
    n = len(arr)
    # Recorremos el arreglo
    for i in range(n):
        min_index = i  # Inicializamos el índice del mínimo como el índice actual
        # Buscamos el elemento más pequeño en el resto del arreglo
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Si encontramos un valor menor, actualizamos el índice
                min_index = j
        # Intercambiamos el valor mínimo encontrado con el valor en la posición actual
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Pruebas unitarias
if __name__ == "__main__":
    # Casos de prueba para verificar la funcionalidad
    print(selection_sort([64, 34, 25, 12, 22, 11, 90]))  # Esperado: [11, 12, 22, 25, 34, 64, 90]
    print(selection_sort([1, 2, 3, 4, 5]))               # Esperado: [1, 2, 3, 4, 5] (arreglo ya ordenado)
    print(selection_sort([5, 4, 3, 2, 1]))               # Esperado: [1, 2, 3, 4, 5] (arreglo en orden inverso)
    print(selection_sort([1]))                           # Esperado: [1] (arreglo con un solo elemento)
