from arbol import Nodo, ArbolExpresion
import operator

if __name__ == "__main__":
    raiz = Nodo(operator.add, Nodo(operator.mul, Nodo(2), Nodo(5)), Nodo(3))
    arbol = ArbolExpresion(raiz)
    print("Resultado:", arbol.evaluar())  # Salida esperada: 13
