# Selection Sort Algorithm
def selection_sort(arr):
    """
    Ordena una lista de números usando el algoritmo Selection Sort.

    Parámetros:
    arr (list): Lista de números a ordenar.

    Retorna:
    list: Lista ordenada de números.
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr