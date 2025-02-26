import numpy as np

def heuristica_adaptativa(nodo, objetivo, historial):
    peso_historial = np.mean(historial.get(nodo, [1]))  # Promedio de pesos previos
    return abs(nodo - objetivo) / peso_historial

def a_star_optimizado(grafo, inicio, objetivo, historial):
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
                prioridad = nuevo_costo + heuristica_adaptativa(vecino, objetivo, historial)
                heapq.heappush(cola_prioridad, (prioridad, vecino))
                ruta[vecino] = nodo_actual
    return None
