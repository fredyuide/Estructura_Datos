import networkx as nx

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_nodo(self, nodo):
        self.grafo.add_node(nodo)

    def agregar_arista(self, nodo1, nodo2, peso=1):
        self.grafo.add_edge(nodo1, nodo2, weight=peso)

    def obtener_vecinos(self, nodo):
        return list(self.grafo.neighbors(nodo))

    def obtener_peso(self, nodo1, nodo2):
        return self.grafo[nodo1][nodo2]['weight']

    def mostrar_grafo(self):
        return self.grafo
