import string
from BFS import BFS
from cola import cola
from nodo import nodo
from grafoPeso1 import Grafo


def main():
    grafo = Grafo()
    grafo.mostrarNodos()
    #BFS(grafo, grafo.grafoNodos[1])
    nodosIngresados=grafo.tomarNodosPorConsola()
    BFS(grafo,nodosIngresados[0])
    grafo.resetear()
    BFS(grafo,nodosIngresados[1])

main()
