from grafo import Grafo
from a_star import a_star
from optimizacion_ia import a_star_optimizado
from visualizacion import dibujar_grafo

# Crear el grafo
grafo = Grafo()
nodos = [1, 2, 3, 4, 5]
for nodo in nodos:
    grafo.agregar_nodo(nodo)

grafo.agregar_arista(1, 2, 2)
grafo.agregar_arista(2, 3, 3)
grafo.agregar_arista(3, 4, 1)
grafo.agregar_arista(4, 5, 4)
grafo.agregar_arista(1, 5, 10)

# Ejecutar A* estándar
camino_a_star = a_star(grafo, 1, 5)
print("Camino encontrado con A*: ", camino_a_star)

# Ejecutar A* optimizado con IA
historial = {2: [2, 2.5], 3: [3, 3.2], 4: [1, 1.1]}
camino_a_star_opt = a_star_optimizado(grafo, 1, 5, historial)
print("Camino encontrado con A* optimizado: ", camino_a_star_opt)

# Dibujar el grafo y la ruta encontrada
dibujar_grafo(grafo, camino_a_star)
dibujar_grafo(grafo, camino_a_star_opt)
