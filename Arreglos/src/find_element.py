# Find Max and Min Element in Array
def find_max(arr):
    """
    Encuentra el elemento mayor en una lista de números.

    Parámetros:
    arr (list): Lista de números.

    Retorna:
    int: El número mayor en la lista.
    """
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

def find_min(arr):
    """
    Encuentra el elemento menor en una lista de números.

    Parámetros:
    arr (list): Lista de números.

    Retorna:
    int: El número menor en la lista.
    """
    min_element = arr[0]
    for num in arr:
        if num < min_element:
            min_element = num
    return min_element
