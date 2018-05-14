import string
from Dijkstra import dijkstra
from nodo import nodo
from grafoPesado import Grafo


def main():
    grafo = Grafo()
    grafo.mostrarNodos()
    nodosIngresados=grafo.tomarNodosPorConsola()
    #dijkstra(grafo, grafo.grafoNodos[1].nodoIndice-1)
    dijkstra(grafo,nodosIngresados[0].nodoIndice-1)
    grafo.resetear()
    #dijkstra(grafo, grafo.grafoNodos[3].nodoIndice-1)
    dijkstra(grafo,nodosIngresados[1].nodoIndice-1)

main()
