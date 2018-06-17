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

            if nodoActual.nodosAdyacentes[j] > 0:
                
                if grafo.grafoNodos[j].nodoVisitado is -1:
                    colaVisitados.encola(grafo.grafoNodos[j])
                    grafo.grafoNodos[j].nodoVisitado =1
        colaVisitados.desencola()

    return camino
