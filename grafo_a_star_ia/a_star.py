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
