# Optimización de Algoritmos - Comparación entre Bubble Sort y QuickSort

Este repositorio contiene el trabajo realizado para optimizar y comparar dos algoritmos de ordenamiento: **Bubble Sort** y **QuickSort**. El objetivo principal es mejorar la eficiencia de estos algoritmos mediante técnicas de optimización y realizar un análisis detallado de los resultados obtenidos.

## Objetivo

El propósito de este proyecto es:
- Optimizar un fragmento de código proporcionado (Bubble Sort).
- Aplicar técnicas algorítmicas avanzadas para mejorar la eficiencia del algoritmo (QuickSort).
- Realizar un análisis de la eficiencia de ambos algoritmos en términos de tiempo de ejecución y uso de recursos.

## Estructura del Repositorio

El repositorio está organizado de la siguiente manera:

- **`original_code/`**: Contiene el código original de Bubble Sort.
- **`optimized_code/`**: Contiene el código optimizado utilizando QuickSort.
- **`analysis/`**: Realiza una comparación de los tiempos de ejecución entre ambos algoritmos.
- **`visuals/`**: Incluye gráficos y visualizaciones sobre el rendimiento de los algoritmos.
- **`report/`**: Contiene el informe en formato PDF con los detalles del proceso de optimización, análisis y resultados.

## Descripción del Código

### `original_code/bubble_sort.py`

Este archivo contiene la implementación del algoritmo de ordenamiento **Bubble Sort**, un algoritmo sencillo pero ineficiente para ordenar listas. La idea básica de este algoritmo es iterar sobre la lista, comparar elementos adyacentes y cambiarlos de lugar si están en el orden incorrecto. Este proceso se repite varias veces hasta que la lista está completamente ordenada. **Bubble Sort** tiene una complejidad de tiempo de **O(n^2)**, lo que lo hace inadecuado para listas grandes.

**Funcionalidad:**
- Ordena una lista de números usando el método de intercambio de elementos adyacentes.
- El proceso se repite hasta que la lista queda ordenada.

### `optimized_code/quick_sort.py`

Este archivo contiene la implementación del algoritmo **QuickSort**, que es mucho más eficiente en comparación con **Bubble Sort**, especialmente para listas grandes. QuickSort es un algoritmo de tipo **divide y vencerás**, que selecciona un "pivote" y divide la lista en dos sublistas: una con elementos menores al pivote y otra con elementos mayores. Luego, recursivamente, se ordenan estas sublistas. **QuickSort** tiene una complejidad de tiempo promedio de **O(n log n)**.

**Funcionalidad:**
- Selecciona un pivote para dividir la lista en dos sublistas.
- Llama recursivamente a la función de ordenamiento para las sublistas.
- El proceso termina cuando las sublistas tienen un solo elemento o están vacías.

### `analysis/performance_comparison.py`

Este archivo realiza una comparación de los tiempos de ejecución entre **Bubble Sort** y **QuickSort** para diferentes tamaños de listas (n=100, 1000, 10000). Utiliza la librería `time` para medir el tiempo que tarda cada algoritmo en ordenar una lista aleatoria de números. Esta comparación muestra cómo la eficiencia de **QuickSort** mejora exponencialmente frente a **Bubble Sort**, especialmente cuando las listas son grandes.

**Funcionalidad:**
- Genera listas de números aleatorios para diferentes tamaños.
- Mide el tiempo de ejecución de ambos algoritmos de ordenamiento.
- Compara los resultados en una tabla de tiempo de ejecución.

### `visuals/visualization.py`

Este archivo genera gráficos que ilustran la comparación entre los algoritmos en cuanto a tiempo de ejecución. Utiliza la librería `matplotlib` para crear visualizaciones que muestran la diferencia en el rendimiento de **Bubble Sort** y **QuickSort** para distintos tamaños de entrada. El gráfico incluye:
- Comparación de tiempos de ejecución entre los algoritmos.
- Crecimiento exponencial del tiempo de ejecución en **Bubble Sort** frente al crecimiento logarítmico de **QuickSort**.

**Funcionalidad:**
- Genera gráficos para visualizar las diferencias en el tiempo de ejecución entre los algoritmos.
- Muestra cómo el tiempo de ejecución aumenta conforme crecen los datos de entrada.

## Cómo Ejecutar el Código

Para ejecutar el código y ver la comparación de los algoritmos:

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/fredyuide/actividad_2_4.git
