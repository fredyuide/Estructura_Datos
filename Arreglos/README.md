# Algoritmos con Arreglos

## Descripción del Proyecto

Este proyecto implementa algoritmos básicos de búsqueda y ordenación utilizando arreglos (listas en Python). Los objetivos principales son:
- Encontrar el elemento mayor y menor en un arreglo.
- Ordenar un arreglo usando dos algoritmos de ordenación: Bubble Sort y Selection Sort.

## Problemas a Resolver

1. **Búsqueda de Elementos**:
   - Encontrar el elemento mayor en un arreglo.
   - Encontrar el elemento menor en un arreglo.

2. **Ordenación de Elementos**:
   - Implementar el algoritmo Bubble Sort para ordenar un arreglo de números.
   - Implementar el algoritmo Selection Sort para ordenar un arreglo de números.

## Algoritmos Implementados

1. **Bubble Sort**: Ordena el arreglo comparando elementos adyacentes y cambiándolos de posición si están en el orden incorrecto. Este proceso se repite hasta que el arreglo esté ordenado.
2. **Selection Sort**: Encuentra el elemento mínimo en la lista y lo coloca en la primera posición. Repite el proceso para los elementos restantes hasta que la lista esté ordenada.

## Instrucciones de Ejecución

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/fredyuide/AlgoritmosConArreglos.git
   cd AlgoritmosConArreglos



Aquí tienes el archivo README.md completo con los ejemplos de casos de prueba y resultados, junto con el informe incluido:

markdown
Copiar código
# Algoritmos con Arreglos

## Descripción del Proyecto

Este proyecto implementa algoritmos básicos de búsqueda y ordenación utilizando arreglos (listas en Python). Los objetivos principales son:
- Encontrar el elemento mayor y menor en un arreglo.
- Ordenar un arreglo usando dos algoritmos de ordenación: Bubble Sort y Selection Sort.

## Problemas a Resolver

1. **Búsqueda de Elementos**:
   - Encontrar el elemento mayor en un arreglo.
   - Encontrar el elemento menor en un arreglo.

2. **Ordenación de Elementos**:
   - Implementar el algoritmo Bubble Sort para ordenar un arreglo de números.
   - Implementar el algoritmo Selection Sort para ordenar un arreglo de números.

## Algoritmos Implementados

1. **Bubble Sort**: Ordena el arreglo comparando elementos adyacentes y cambiándolos de posición si están en el orden incorrecto. Este proceso se repite hasta que el arreglo esté ordenado.
2. **Selection Sort**: Encuentra el elemento mínimo en la lista y lo coloca en la primera posición. Repite el proceso para los elementos restantes hasta que la lista esté ordenada.

## Instrucciones de Ejecución

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu_usuario/AlgoritmosConArreglos.git
   cd AlgoritmosConArreglos
Asegúrate de tener Python instalado (versión 3.6 o superior). Puedes verificar la versión con:

bash
Copiar código
python --version
Ejecuta los casos de prueba:

bash
Copiar código
python tests/test_cases.py
Esto ejecutará los algoritmos y mostrará los resultados en la consola.

Ejemplos de Casos de Prueba y Resultados
Considerando un arreglo de ejemplo [64, 34, 25, 12, 22, 11, 90]:

1. Ordenación con Bubble Sort
Entrada: [64, 34, 25, 12, 22, 11, 90]
Salida: [11, 12, 22, 25, 34, 64, 90]
2. Ordenación con Selection Sort
Entrada: [64, 34, 25, 12, 22, 11, 90]
Salida: [11, 12, 22, 25, 34, 64, 90]
3. Búsqueda del Elemento Mayor
Entrada: [64, 34, 25, 12, 22, 11, 90]
Salida: 90
4. Búsqueda del Elemento Menor
Entrada: [64, 34, 25, 12, 22, 11, 90]
Salida: 11

Informe y Observaciones
Enfoques y Observaciones
El enfoque para implementar estos algoritmos se centró en la simplicidad y claridad. Los algoritmos seleccionados, Bubble Sort y Selection Sort, son métodos básicos de ordenación que funcionan bien en listas pequeñas y son útiles para comprender conceptos fundamentales de ordenación.

Reflexiones sobre la Eficiencia
Bubble Sort: Tiene una complejidad temporal de O(n^2) y resulta ineficiente para listas grandes, ya que compara repetidamente elementos adyacentes. Es fácil de implementar y útil para aprender sobre el funcionamiento de algoritmos de ordenación, pero es menos práctico para datos grandes.

Selection Sort: También tiene una complejidad de O(n^2), pero realiza menos intercambios en comparación con Bubble Sort. Esto puede hacer que Selection Sort sea una mejor opción cuando las operaciones de intercambio son costosas. Sin embargo, sigue siendo menos eficiente en comparación con algoritmos más avanzados como Quick Sort o Merge Sort.

Desafíos Encontrados
Durante la implementación, uno de los desafíos fue optimizar las comparaciones para minimizar los intercambios innecesarios en Bubble Sort. Para Selection Sort, fue importante asegurarse de identificar correctamente el elemento mínimo en cada iteración y colocarlo en la posición correcta.

Este proyecto ha sido una buena práctica en algoritmos básicos y ofrece una base sólida para avanzar hacia algoritmos más avanzados y eficientes.
