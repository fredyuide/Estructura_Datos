# Evaluador de Expresiones Postfijas

## **Descripción del Proyecto**
Este proyecto implementa una estructura de datos tipo pila mediante dos enfoques: listas enlazadas y arreglos. Posteriormente, utiliza estas implementaciones para evaluar expresiones aritméticas en notación posfija (postfijo). El objetivo es aprender a trabajar con pilas, entender su funcionamiento y aplicarlas en un problema práctico.

## **Objetivo**
Diseñar e implementar una estructura de datos tipo pila utilizando:
1. **Listas enlazadas** como base para almacenar los datos.
2. **Arreglos** para gestionar los elementos.

Y emplear una de estas pilas en un programa para evaluar expresiones en notación posfija.

---

## **Estructura del Proyecto**

### **Archivos**
1. **`pila_linked_list.py`**: Implementación de la pila basada en listas enlazadas.
2. **`pila_array.py`**: Implementación de la pila basada en arreglos.
3. **`evaluator.py`**: Contiene la función `evaluate_postfix` para evaluar expresiones posfijas utilizando cualquiera de las implementaciones de pila.
4. **`main.py`**: Programa principal que permite al usuario ingresar una expresión y elegir el tipo de pila.
5. **`README.md`**: Documento de descripción del proyecto.

---

## **Explicación Técnica**

### **Pila**
La pila es una estructura de datos que sigue el principio **LIFO** (Last In, First Out). Es decir, el último elemento en entrar es el primero en salir. Las operaciones básicas son:

- **`push(value)`**: Añade un elemento a la pila.
- **`pop()`**: Elimina y devuelve el elemento en la cima de la pila.
- **`peek()`**: Consulta el elemento en la cima sin eliminarlo.
- **`is_empty()`**: Verifica si la pila está vacía.

### **Notación Postfija**
La notación posfija es una forma de escribir expresiones aritméticas en la que los operadores se colocan después de sus operandos. Por ejemplo:

- **Expresión infija**: `(3 + 4) * 2 / 7`
- **Expresión posfija**: `3 4 + 2 * 7 /`

---

## **Implementaciones**

### **1. Pila con Listas Enlazadas**
La pila basada en listas enlazadas usa nodos que contienen un valor y una referencia al siguiente nodo. Es útil cuando se requiere una pila dinámica con tamaño variable.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

```python
class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        ...

    def pop(self):
        ...

    def peek(self):
        ...

    def is_empty(self):
        ...
```

### **2. Pila con Arreglos**
La pila basada en arreglos utiliza una lista para almacenar los elementos. Es más rápida en acceso directo, pero requiere un límite de capacidad.

```python
class StackArray:
    def __init__(self, capacity=100):
        self.stack = []
        self.capacity = capacity

    def push(self, value):
        ...

    def pop(self):
        ...

    def peek(self):
        ...

    def is_empty(self):
        ...
```

---

## **Evaluación de Expresiones Postfijas**
La evaluación se realiza recorriendo la expresión posfija token por token:
1. Si el token es un número, se apila.
2. Si el token es un operador, se desapilan dos números, se aplica el operador y se apila el resultado.

Ejemplo:
- Expresión: `3 4 + 2 *`
- Operaciones:
  1. Apilar `3`, luego `4`.
  2. Encontrar `+`, desapilar `4` y `3`, calcular `3 + 4 = 7`, y apilar `7`.
  3. Apilar `2`.
  4. Encontrar `*`, desapilar `2` y `7`, calcular `7 * 2 = 14`, y apilar `14`.

Resultado: `14`.

---

## **Ejecución del Programa**

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tuusuario/nombre-del-repositorio](https://github.com/fredyuide/Estructura_Datos/tree/main/PilaPosfija.git
   cd nombre-del-repositorio
   ```

2. **Ejecutar el programa**
   ```bash
   python main.py
   ```

3. **Ingresar datos**
   - Expresión en notación posfija (separada por espacios). Ejemplo: `3 4 + 2 * 7 /`
   - Tipo de pila a usar: `array` o `linked_list`.

---

## **Ejemplo de Uso**

### **Entrada**
```
Ingresa una expresión en notación posfija (separada por espacios): 3 4 + 2 * 7 /
Elige el tipo de pila ('array' o 'linked_list'): array
```

### **Salida**
```
El resultado de la expresión es: 2.0
```

---

## **Pruebas Realizadas**
### **Casos de Prueba**
1. **Expresiones básicas**
   - Entrada: `5 3 +`
   - Resultado: `8`

2. **Expresiones con múltiples operaciones**
   - Entrada: `6 3 2 + *`
   - Resultado: `30`

3. **División y decimales**
   - Entrada: `10 3 /`
   - Resultado: `3.3333...`

4. **Errores manejados**
   - Entrada vacía: Muestra un mensaje de error.
   - División por cero: Muestra un mensaje de error.

---

## **Requisitos Técnicos**
- Python 3.7+
- Librerías estándar (no se requieren dependencias externas).

---

## **Contribuciones**
Se aceptan contribuciones para mejorar el código y la documentación. Por favor, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama para tu cambio (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m "Añadir nueva funcionalidad"`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request.

---

## **Autor**
Proyecto desarrollado por **[Tu Nombre]**.

---

## **Licencia**
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.
