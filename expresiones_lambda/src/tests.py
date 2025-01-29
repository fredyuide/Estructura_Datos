import unittest
from arbol import Nodo, ArbolExpresion
import operator

class TestArbolExpresion(unittest.TestCase):
    def test_evaluacion(self):
        raiz = Nodo(operator.add, Nodo(operator.mul, Nodo(2), Nodo(5)), Nodo(3))
        arbol = ArbolExpresion(raiz)
        self.assertEqual(arbol.evaluar(), 13)

if __name__ == "__main__":
    unittest.main()
