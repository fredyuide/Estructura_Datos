import networkx as nx
import matplotlib.pyplot as plt

def dibujar_grafo(grafo, ruta=None):
    pos = nx.spring_layout(grafo.mostrar_grafo())
    nx.draw(grafo.mostrar_grafo(), pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)

    if ruta:
        ruta_edges = list(zip(ruta, ruta[1:]))
        nx.draw_networkx_edges(grafo.mostrar_grafo(), pos, edgelist=ruta_edges, edge_color='red', width=2)

    plt.show()
