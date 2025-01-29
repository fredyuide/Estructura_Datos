import operator

class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho

class ArbolExpresion:
    def __init__(self, raiz):
        self.raiz = raiz

    def evaluar(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if isinstance(nodo.valor, (int, float)):
            return nodo.valor
        izquierda = self.evaluar(nodo.izquierdo)
        derecha = self.evaluar(nodo.derecho)
        return nodo.valor(izquierda, derecha)
