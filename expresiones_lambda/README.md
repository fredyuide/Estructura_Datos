# Árboles Binarios para Evaluación de Expresiones Lambda

Este proyecto implementa árboles binarios para la evaluación de expresiones Lambda, permitiendo representar y calcular expresiones matemáticas y lógicas de manera estructurada.

## 📁 Estructura del Proyecto

```
expresiones_lambda/
│── src/                 # Código fuente
│   ├── __init__.py      # Archivo para definir el paquete (Python)
│   ├── arbol.py         # Implementación del árbol binario
│   ├── evaluador.py     # Función para evaluar expresiones
│   └── tests.py         # Casos de prueba
│── README.md            # Explicación general del repositorio
```

## 🚀 Implementación

### 1️⃣ Construcción del Árbol Binario
Se implementó una clase `Nodo` para representar los nodos del árbol binario, y una clase `ArbolExpresion` para manejar la evaluación de expresiones Lambda usando recorrido postorden.

### 2️⃣ Evaluación de Expresiones
El árbol se evalúa de manera recursiva, operando primero los nodos hijos antes de aplicar la operación del nodo padre.

### 3️⃣ Pruebas
Se implementaron casos de prueba usando `unittest` para validar la correcta evaluación de expresiones en el árbol binario.

## 🛠️ Código Principal

### `src/arbol.py` (Definición del árbol binario)
```python
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
```

### `src/evaluador.py` (Ejemplo de Evaluación)
```python
from arbol import Nodo, ArbolExpresion
import operator

if __name__ == "__main__":
    raiz = Nodo(operator.add, Nodo(operator.mul, Nodo(2), Nodo(5)), Nodo(3))
    arbol = ArbolExpresion(raiz)
    print("Resultado:", arbol.evaluar())  # Salida esperada: 13
```

### `src/tests.py` (Casos de Prueba)
```python
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
```

## 📌 Instalación y Uso

### 🔹 Clonar el repositorio
```sh
git clone https://github.com/fredyuide/Estructura_Datos/new/main/expresiones_lambda.git
cd expresiones_lambda
```

### 🔹 Crear un entorno virtual e instalar dependencias
```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 🔹 Ejecutar el evaluador
```sh
python src/evaluador.py
```

### 🔹 Ejecutar las pruebas
```sh
python -m unittest src/tests.py
```

