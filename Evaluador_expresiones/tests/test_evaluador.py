import unittest
from src.evaluador import evaluar_expresion

class TestEvaluador(unittest.TestCase):
    
    def test_expresion_simple(self):
        expresion = "3 + 5"
        self.assertEqual(evaluar_expresion(expresion), 8)

    def test_expresion_con_parentesis(self):
        expresion = "3 + (2 - 8)"
        self.assertEqual(evaluar_expresion(expresion), -3)

    def test_expresion_multiplicacion(self):
        expresion = "3 * 5"
        self.assertEqual(evaluar_expresion(expresion), 15)

    def test_expresion_compleja(self):
        expresion = "3 + 5 * (2 - 8)"
        self.assertEqual(evaluar_expresion(expresion), -13)

    def test_expresion_division(self):
        expresion = "10 / 2"
        self.assertEqual(evaluar_expresion(expresion), 5)

if __name__ == '__main__':
    unittest.main()
