import string
from nodo import nodo
from grafoPesado import Grafo
from EdmondsKarp import EdmondsKarp
from FordFulkerson import FordFulkerson


def main():
    grafo = Grafo()
    grafo.mostrarNodos()
    #EdmondsKarp(grafo,grafo.grafoNodos[0])

main()
