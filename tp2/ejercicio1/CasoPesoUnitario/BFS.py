from cola import cola
def BFS(grafo, nodoInicial):
    colaVisitados = cola()
    colaVisitados.encola(nodoInicial)
    camino = []
    nodoInicial.nodoVisitado = 1
    while colaVisitados.cantidad > 0:
        nodoActual = colaVisitados.primero
        camino.append(nodoActual.nodoIndice)
        for j in nodoActual.nodosAdyacentes:
            if grafo.grafoNodos[j-1].nodoVisitado is -1:
                colaVisitados.encola(grafo.grafoNodos[j-1])
                grafo.grafoNodos[j-1].nodoVisitado =1
        colaVisitados.desencola()
    print("\n")
    print camino
