class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        previo = None
        while actual is not None:
            if actual.dato == dato:
                if previo is None:
                    self.cabeza = actual.siguiente
                else:
                    previo.siguiente = actual.siguiente
                return True
            previo = actual
            actual = actual.siguiente
        return False

    def buscar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos
