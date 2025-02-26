# **Implementación de Algoritmo A* Optimizado con IA en Grafos**

## **Descripción**
Este proyecto implementa un grafo en Python y utiliza el algoritmo A* optimizado con inteligencia artificial para mejorar la búsqueda de rutas en grafos de gran escala. La optimización con IA permite mejorar la heurística del algoritmo mediante técnicas adaptativas, lo que reduce el tiempo de búsqueda y mejora la eficiencia computacional.

## **Ejemplo de Código**

### **Implementación del Grafo**
```python
import networkx as nx

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_nodo(self, nodo):
        self.grafo.add_node(nodo)

    def agregar_arista(self, nodo1, nodo2, peso=1):
        self.grafo.add_edge(nodo1, nodo2, weight=peso)
```

### **Algoritmo A* Estándar**
```python
import heapq

def heuristica(nodo, objetivo):
    return abs(nodo - objetivo)

def a_star(grafo, inicio, objetivo):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    costo_acumulado = {inicio: 0}
    ruta = {inicio: None}

    while cola_prioridad:
        _, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == objetivo:
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = ruta[nodo_actual]
            return camino[::-1]

        for vecino in grafo.obtener_vecinos(nodo_actual):
            nuevo_costo = costo_acumulado[nodo_actual] + grafo.obtener_peso(nodo_actual, vecino)
            if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(vecino, objetivo)
                heapq.heappush(cola_prioridad, (prioridad, vecino))
                ruta[vecino] = nodo_actual
    return None
```

### **Optimización con IA**
```python
import numpy as np

def heuristica_adaptativa(nodo, objetivo, historial):
    peso_historial = np.mean(historial.get(nodo, [1]))
    return abs(nodo - objetivo) / peso_historial
```

## **Ejemplo de Uso**
```python
from grafo import Grafo
from a_star import a_star
from optimizacion_ia import a_star_optimizado

grafo = Grafo()
nodos = [1, 2, 3, 4, 5]
for nodo in nodos:
    grafo.agregar_nodo(nodo)

grafo.agregar_arista(1, 2, 2)
grafo.agregar_arista(2, 3, 3)
grafo.agregar_arista(3, 4, 1)
grafo.agregar_arista(4, 5, 4)
grafo.agregar_arista(1, 5, 10)

camino_a_star = a_star(grafo, 1, 5)
print("Camino encontrado con A*: ", camino_a_star)
```

