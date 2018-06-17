import string
from nodo import nodo
from grafoPesado import Grafo
from EK import EK


def main():

    grafo = Grafo()
    grafo.mostrarNodos()
    EK(grafo,grafo.grafoNodos[0])

main()
