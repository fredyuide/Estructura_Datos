class Pila:
    """
    Implementación de una pila con operaciones básicas.
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Inserta un elemento en la pila.
        """
        self.items.append(item)

    def pop(self):
        """
        Elimina y devuelve el elemento superior de la pila.
        Lanza un error si la pila está vacía.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        """
        Devuelve el elemento superior sin eliminarlo.
        Lanza un error si la pila está vacía.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        """
        Verifica si la pila está vacía.
        """
        return len(self.items) == 0

    def size(self):
        """
        Devuelve el tamaño de la pila.
        """
        return len(self.items)
