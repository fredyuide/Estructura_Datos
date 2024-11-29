# Bubble Sort Algorithm
def bubble_sort(arr):
    """
    Ordena una lista de números usando el algoritmo Bubble Sort.

    Parámetros:
    arr (list): Lista de números a ordenar.

    Retorna:
    list: Lista ordenada de números.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
