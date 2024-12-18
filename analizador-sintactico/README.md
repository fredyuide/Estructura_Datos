# Analizador Sintáctico para Validación de Expresiones

## Introducción

Este proyecto implementa un analizador sintáctico diseñado para validar expresiones matemáticas y lógicas, utilizando estructuras de datos como pilas y árboles. Su objetivo principal es profundizar en los conceptos fundamentales de las estructuras de datos aplicadas y mejorar habilidades prácticas de programación.

Los analizadores sintácticos son herramientas clave en aplicaciones como compiladores, editores de texto y evaluadores de expresiones. Este trabajo se centra en desarrollar un modelo básico que valide el balanceo de paréntesis, la correcta disposición de operadores y operandos, y que opcionalmente pueda generar un árbol de expresión.

---

## Desarrollo

### Lógica del Analizador

El analizador verifica las siguientes reglas:

1. **Balanceo de Paréntesis, Corchetes y Llaves:**
   - Usa una pila para almacenar los caracteres de apertura (`(`, `[`, `{`) y los compara con sus pares correspondientes al encontrarlos en la expresión.

2. **Validación de Operadores y Operandos:**
   - Verifica que los caracteres sean válidos (letras, números o símbolos matemáticos `+`, `-`, `*`, `/`).
   - Detecta operadores mal ubicados o caracteres inválidos.

3. **Generación de Mensajes de Error:**
   - Muestra mensajes claros cuando la expresión es inválida, indicando el problema específico.

### Estructuras de Datos Utilizadas

- **Pilas:** Para manejar el balanceo de paréntesis.
- **Listas:** Para el almacenamiento temporal de tokens.
- **(Opcional) Árbol de Expresión:** Representación jerárquica de operaciones matemáticas.

### Resultados de Pruebas

#### Casos Válidos

| Expresión            | Resultado  |
|-----------------------|------------|
| `((a + b) * c)`      | Válida     |
| `5 * (3 + 2)`         | Válida     |
| `[a + b] * {c}`       | Válida     |

#### Casos Inválidos

| Expresión            | Error Detallado                   |
|-----------------------|-----------------------------------|
| `((a + b) * c`        | Paréntesis desbalanceados        |
| `(5 * [3 + 2)}`       | Paréntesis o corchetes mal cerrados |
| `5 * (3 & 2)`         | Carácter inválido: `&`           |

### Proceso de Desarrollo

1. **Diseño del Algoritmo:**
   - Se definió una pila para manejar paréntesis y listas de operadores/operandos para validar la expresión.

2. **Implementación:**
   - Se escribió la lógica en Python utilizando un enfoque modular (archivos separados para validación y pruebas).

3. **Pruebas:**
   - Se diseñaron casos de prueba simples y complejos para evaluar la funcionalidad.

### Capturas de Pantalla

- **Ejemplo de Ejecución:**
  ![Ejecución del Analizador](#)

---

## Conclusión

El desarrollo del analizador sintáctico permitió:

- Comprender la aplicación práctica de estructuras de datos como pilas y listas.
- Desarrollar un sistema modular y extensible.
- Identificar retos, como la validación de expresiones complejas, y proponer mejoras futuras, como implementar un árbol de expresión completo.

### Posibles Mejoras

- Implementar un generador de árboles de expresión para evaluación de operaciones.
- Ampliar el soporte para otras estructuras de expresiones.

---

## Referencias

- Documentación de Python: [https://docs.python.org/](https://docs.python.org/)
- Estructuras de Datos en Python: Artículos académicos y recursos educativos.

---

## Cómo Ejecutar el Proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/analizador-sintactico](https://github.com/fredyuide/Estructura_Datos/tree/main/analizador-sintactico.git
   cd analizador-sintactico
   ```

2. Ejecutar el programa:
   ```bash
   python src/main.py
   ```

3. Ejecutar pruebas automáticas:
   ```bash
   python -m unittest discover tests
   
