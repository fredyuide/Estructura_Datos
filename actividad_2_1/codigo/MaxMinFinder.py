# MaxMinFinder.py
# Este script contiene la implementación de la búsqueda del valor máximo y mínimo en un arreglo.
# La función 'find_max_min' toma un arreglo de enteros como entrada y retorna los valores máximo y mínimo.

def find_max_min(arr):
    """
    Encuentra el valor máximo y mínimo en un arreglo de enteros.

    Parámetros:
    arr (list): Un arreglo de enteros.

    Retorna:
    tuple: El valor máximo y el valor mínimo en el arreglo.
            Si el arreglo está vacío, retorna (None, None).
    """
    if not arr:  # Verificación de caso de arreglo vacío
        return None, None
    
    # Inicializamos los valores máximo y mínimo con el primer elemento del arreglo.
    max_val = min_val = arr[0]
    
    # Recorremos el arreglo a partir del segundo elemento
    for num in arr[1:]:
        if num > max_val:  # Actualizamos el máximo si encontramos un valor mayor
            max_val = num
        if num < min_val:  # Actualizamos el mínimo si encontramos un valor menor
            min_val = num
    
    return max_val, min_val

# Pruebas unitarias
if __name__ == "__main__":
    # Casos de prueba para verificar la funcionalidad
    print(find_max_min([3, 1, 9, 7, 5, 9]))  # Esperado: (9, 1)
    print(find_max_min([1]))                # Esperado: (1, 1)
    print(find_max_min([5, 5, 5]))          # Esperado: (5, 5)
    print(find_max_min([]))                 # Esperado: (None, None)
