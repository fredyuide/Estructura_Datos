# Evaluador de Expresiones Matemáticas con Pila

Este proyecto implementa un **Tipo Abstracto de Datos (TDA) Pila** para evaluar expresiones matemáticas en **notación infija**. La aplicación recibe una expresión matemática como entrada, la procesa respetando las reglas de precedencia de operadores y paréntesis, y devuelve el resultado calculado.

## Descripción

El evaluador toma una expresión matemática en notación infija, como `3 + 5 * (2 - 8)`, y evalúa su resultado utilizando una pila para gestionar los operadores y operandos. La pila permite manejar de manera eficiente la precedencia de operadores y los paréntesis dentro de la expresión.

## Objetivos del Proyecto

1. **Implementar un TDA Pila**: Mostrar cómo se puede usar una pila para evaluar expresiones matemáticas.
2. **Aplicar Precedencia de Operadores**: Implementar las reglas de precedencia y asociatividad de los operadores matemáticos.
3. **Evaluación de Expresiones**: Evaluar correctamente expresiones con números, operadores, y paréntesis.
4. **Demostrar el Uso del TDA**: Usar el TDA pila de manera efectiva para almacenar operadores y operandos durante la evaluación.

## Requisitos

- **Python 3.6+**: El proyecto está implementado en Python, por lo que es necesario tener instalada la versión 3.6 o superior.
- No se requieren dependencias adicionales externas.

## Instalación

### Clonar el Repositorio

1. Clona este repositorio en tu máquina local utilizando Git:

   ```bash
   git clone https://github.com/fredyuide/evaluador_de_expresiones.git
   cd evaluador_de_expresiones

### Uso
Evaluar Expresiones Matemáticas
Para usar la aplicación, puedes llamar a la función principal evaluar_expresion(expresion) que toma una cadena de texto (la expresión matemática) y devuelve el resultado calculado.

Ejemplo de Uso:
from evaluador import evaluar_expresion

expresion = "3 + 5 * (2 - 8)"
resultado = evaluar_expresion(expresion)
print(f"El resultado de la expresión '{expresion}' es: {resultado}")


Salida esperada: El resultado de la expresión '3 + 5 * (2 - 8)' es: -13

### Expresiones válidas
La aplicación soporta expresiones en notación infija y maneja correctamente los paréntesis y operadores con diferentes niveles de precedencia.

Ejemplos de expresiones válidas:
3 + 5
3 + (2 - 8)
(1 + 2) * (3 - 4)
5 * (6 + 7) / 8

### Descripción de la Función evaluar_expresion
La función evaluar_expresion es la encargada de recibir la expresión, procesarla, y devolver el resultado. A continuación, se explica cómo funciona la evaluación:

Se eliminan los espacios en blanco de la expresión para simplificar el procesamiento.
Se recorre cada carácter de la expresión. Si el carácter es un número, se agrega directamente a los operandos; si es un operador, se coloca en la pila.
Los paréntesis se manejan de forma especial: cuando se encuentra un paréntesis de apertura (, se coloca en la pila; cuando se encuentra un paréntesis de cierre ), se realizan las operaciones hasta que se encuentra el paréntesis de apertura correspondiente.
Al final, la pila contendrá el resultado de la expresión evaluada.

def evaluar_expresion(expresion):
    # Lógica para evaluar la expresión usando la pila
    pass


### Implementación
1. TDA Pila
La pila en este proyecto es implementada utilizando una lista de Python. A continuación se presentan las funciones básicas que soporta:

class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Añade un elemento al tope de la pila."""
        self.items.append(item)
    
    def pop(self):
        """Elimina el elemento del tope de la pila y lo devuelve."""
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self):
        """Devuelve el elemento en el tope de la pila sin eliminarlo."""
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0


### 2. Evaluador de Expresiones
La función evaluar_expresion recorre la expresión, manejando operadores y operandos, y utiliza la pila para aplicar las reglas de precedencia de operadores.

Pasos del algoritmo de evaluación:

Recorrer la expresión: Analiza cada carácter de la expresión.
Operando: Si el carácter es un número, lo agrega al resultado.
Operador: Si el carácter es un operador (como +, -, *, /), se maneja según su precedencia, colocándolo en la pila.
Paréntesis: Los paréntesis abren y cierran subexpresiones. Se utilizan para modificar el orden de operaciones.
3. Comentarios en el Código
El código está comentado de manera detallada para explicar cada segmento importante o complejo, especialmente en las partes que realizan las operaciones con la pila y la evaluación de la expresión.

Por ejemplo, en la función de evaluación de la expresión:

def evaluar_expresion(expresion):
    # Eliminamos los espacios en blanco de la expresión
    expresion = expresion.replace(" ", "")
    
    # Pila para los operadores y operandos
    pila = Pila()
    
    # Lógica para procesar la expresión y evaluar el resultado
    for char in expresion:
        if char.isdigit():
            pila.push(char)  # Si es un número, lo agregamos a la pila
        elif char == "+" or char == "-":
            # Lógica para manejar los operadores de suma y resta
            pass
        # Otros operadores y paréntesis se gestionan de manera similar
    
    # Finalmente, procesamos los elementos en la pila y devolvemos el resultado
    return resultado


