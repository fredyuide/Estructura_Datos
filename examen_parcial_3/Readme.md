# Proyecto de Algoritmos y Estructuras de Datos

Este repositorio contiene la implementación de varios algoritmos y estructuras de datos en Python, incluyendo ordenamiento optimizado, árboles de expresiones matemáticas, grafos y colas con listas doblemente enlazadas.

## **1. Ordenamiento Optimizado con Quicksort**

### **Descripción**
El código implementa **Quicksort**, un algoritmo eficiente de ordenamiento basado en la estrategia **divide y vencerás**. Se elige un pivote, se particiona la lista en elementos menores y mayores al pivote, y luego se ordenan recursivamente ambas mitades.

### **Código: `optimized_sorting.py`**
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Ejemplo de uso
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_arr = quicksort(arr)
print(sorted_arr)
```

### **Explicación del Código**
- Se divide la lista con un pivote en tres partes: menores, iguales y mayores.
- Se llama recursivamente a la función en las partes menores y mayores.
- Se concatenan las partes ordenadas para obtener la lista final.

---

## **2. Árbol de Expresiones Matemáticas**

### **Descripción**
Este código construye un **Árbol de Expresiones Matemáticas** a partir de una expresión infija, convirtiéndola en postfija antes de construir el árbol. Se evalúa el árbol recursivamente.

### **Código: `expression_tree.py`**
```python
import operator

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def evaluate(self):
        if self.value in OPERATORS:
            left_val = self.left.evaluate()
            right_val = self.right.evaluate()
            return OPERATORS[self.value](left_val, right_val)
        else:
            return float(self.value)

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def build_expression_tree(tokens):
    stack = []
    for token in tokens:
        if token in OPERATORS:
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(token, left, right))
        else:
            stack.append(Node(token))
    return stack[0]

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    
    for token in tokens:
        if token.isnumeric() or '.' in token:
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    
    while stack:
        output.append(stack.pop())
    
    return output

# Ejemplo de uso
expression = "3 + 5 * ( 2 - 8 )"
postfix_expr = infix_to_postfix(expression)
tree = build_expression_tree(postfix_expr)
result = tree.evaluate()
print("Resultado:", result)
```

### **Explicación del Código**
- Convierte la expresión infija en postfija usando el algoritmo **Shunting Yard**.
- Construye un árbol binario utilizando una pila.
- Evalúa el árbol de manera recursiva.

---

## **3. Cola con Lista Doblemente Enlazada**

### **Descripción**
Implementa una **cola** utilizando una lista doblemente enlazada. Se pueden insertar elementos al final (`enqueue`) y eliminar desde el inicio (`dequeue`).

### **Código: `double_linked_queue.py`**
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return value

# Caso de uso práctico
dq = DoublyLinkedQueue()
dq.enqueue(10)
dq.enqueue(20)
dq.enqueue(30)
print("Dequeue:", dq.dequeue())
print("Peek:", dq.head.value if dq.head else None)
```

### **Explicación del Código**
- Se crean nodos dobles con punteros `next` y `prev`.
- `enqueue()` agrega elementos al final en **O(1)**.
- `dequeue()` elimina el primer elemento en **O(1)**.

---

## **Instrucciones de Uso**
1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Ejecutar los scripts con Python:
   ```bash
   python optimized_sorting.py
   python expression_tree.py
   python double_linked_queue.py
   ```


