# Lista Circular Doblemente Enlazada en Python

Este proyecto implementa una **Lista Circular Doblemente Enlazada** en Python. La lista permite realizar operaciones como insertar, eliminar y recorrer sus elementos en ambas direcciones. Además, incluye un menú interactivo para facilitar su uso.

## Características

La lista circular doblemente enlazada permite realizar las siguientes operaciones:

1. **Insertar un elemento en una posición específica**: 
   - Puedes especificar la posición en la que deseas insertar un elemento (0 para el inicio).
2. **Eliminar el primer elemento**:
   - Elimina el nodo en la cabeza de la lista.
3. **Eliminar el último elemento**:
   - Elimina el nodo al final de la lista.
4. **Mostrar los elementos recorriendo hacia adelante**:
   - Muestra todos los elementos desde la cabeza hasta el final en dirección hacia adelante.
5. **Mostrar los elementos recorriendo hacia atrás**:
   - Muestra todos los elementos desde el último nodo hasta la cabeza en dirección hacia atrás.
6. **Menú interactivo**:
   - Permite al usuario ejecutar las operaciones anteriores mediante un sistema de opciones.

## Estructura del Código

El proyecto consta de las siguientes clases y funciones:

- **Clase `Node`**:
  Representa un nodo en la lista, que contiene:
  - `data`: Los datos almacenados en el nodo.
  - `next`: Puntero al siguiente nodo.
  - `prev`: Puntero al nodo anterior.

- **Clase `CircularDoublyLinkedList`**:
  Implementa las operaciones de la lista circular doblemente enlazada:
  - `insert_at_position(data, position)`: Inserta un nodo en una posición específica.
  - `delete_first()`: Elimina el nodo en la cabeza.
  - `delete_last()`: Elimina el último nodo.
  - `display_forward()`: Muestra los elementos en dirección hacia adelante.
  - `display_backward()`: Muestra los elementos en dirección hacia atrás.

- **Función `menu()`**:
  Proporciona un menú interactivo para realizar las operaciones en la lista.

## Requisitos

- Python 3.7 o superior.

