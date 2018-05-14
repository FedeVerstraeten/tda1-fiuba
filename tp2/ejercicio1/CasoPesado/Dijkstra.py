import sys
def dijkstra(grafo, nodoInicial):
    nodo_k = nodoInicial
    menor = sys.maxint
    caminoMinimo = []

    for i in grafo.grafoNodos[nodo_k].nodosAdyacentes:
        caminoMinimo.append(grafo.grafoNodos[nodo_k].nodosAdyacentes.get(i))

    for i in range (grafo.grafoGrado-2):
        vector = Menor(grafo,caminoMinimo,nodo_k, menor)
        menor = vector[0]
        nodo_k = vector[1]

        grafo.grafoNodos[nodo_k].nodoVisitado = 1

        for j in grafo.grafoNodos[nodo_k].nodosAdyacentes:
            if grafo.grafoNodos[j-1].nodoVisitado == -1 :#caminoRecorrido[j] == 0 :
                caminoMinimo.append(minimo( caminoMinimo[j-1], caminoMinimo[nodo_k]+ grafo.grafoNodos[nodo_k].nodosAdyacentes.get(j)))
    #print caminoMinimo
    return caminoMinimo

def Menor(grafo, caminoMinimo, nodo_k, menor):

    vectorAuxiliar = []
    for i in grafo.grafoNodos[nodo_k].nodosAdyacentes:

        if grafo.grafoNodos[i-1].nodoVisitado is -1:

            for j in range(len(caminoMinimo)):
                if caminoMinimo[j] < menor:
                    menor = caminoMinimo[j]
                    nodo_k = i

    vectorAuxiliar.append(menor)
    vectorAuxiliar.append(nodo_k)


    return vectorAuxiliar

def minimo (valor1, valor2):
    if valor1 < valor2:
        return valor1
    elif valor1 > valor2:
        return valor2
    else:
        return valor1
