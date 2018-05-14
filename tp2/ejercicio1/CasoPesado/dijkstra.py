import sys
def dijkstra(grafo, nodoInicial):
    nodo_k = nodoInicial
    #caminoRecorrido = {}
    #caminoMinimo = {}
    menor = sys.maxint
    caminoMinimo = []


    print grafo.grafoNodos[nodo_k].nodosAdyacentes
    #for i in range (len(grafo.grafoNodos[nodo_k].nodosAdyacentes)):
    for i in grafo.grafoNodos[nodo_k].nodosAdyacentes:
    #for i in range (grafo.grafoGrado-1):
        #caminoRecorrido[i] = 0
        #for j in grafoNodos[nodo_k].nodosAdyacentes:
        #caminoMinimo[i]=grafo.grafoNodos[nodo_k].nodosAdyacentes.get(i)
        caminoMinimo.append(grafo.grafoNodos[nodo_k].nodosAdyacentes.get(i))
    #caminoRecorrido[0] = grafo.grafoNodos[nodo_k].nodoIndice

    #print caminoRecorrido[0]
    print "caminiitooooo",caminoMinimo
    for i in range (grafo.grafoGrado-2):
        vector = Menor(grafo,caminoMinimo,nodo_k, menor)
        menor = vector[0]#Menor(grafo,caminoMinimo,nodo_k, menor)
        nodo_k = vector[1]
        print "el nodo k ahora es el",nodo_k+1
        print " la distancia menor es", menor
        #caminoRecorrido[i] = grafo.grafoNodos[nodo_k].nodoIndice
        grafo.grafoNodos[nodo_k].nodoVisitado = 1
        #for j in range(len(grafo.grafoNodos[nodo_k].nodosAdyacentes)):
        for j in grafo.grafoNodos[nodo_k].nodosAdyacentes:
            if grafo.grafoNodos[j-1].nodoVisitado == -1 :#caminoRecorrido[j] == 0 :
                #print type(caminoMinimo[nodo_k])
                print "CAMINOMINIMI[Jotasa]",caminoMinimo[j-1]
                print " pesos de las aristas del nodo actual",grafo.grafoNodos[nodo_k].nodosAdyacentes.get(j)
                print "el camino minimo en la posicion nodo k",caminoMinimo[nodo_k]
                #min( caminoMinimo[j], caminoMinimo[nodo_k]+ grafo.grafoNodos[nodo_k].nodosAdyacentes.get(j))
                print "suma caminoMin[nodo_k]+nodoAdj del nodo k.get(j)",caminoMinimo[nodo_k]+ grafo.grafoNodos[nodo_k].nodosAdyacentes.get(j)
                #caminoMinimo[j] = minimo( caminoMinimo[j], caminoMinimo[nodo_k]+ grafo.grafoNodos[nodo_k].nodosAdyacentes.get(j))
                caminoMinimo.append(minimo( caminoMinimo[j-1], caminoMinimo[nodo_k]+ grafo.grafoNodos[nodo_k].nodosAdyacentes.get(j)))
    print caminoMinimo
    return caminoMinimo

def Menor(grafo, caminoMinimo, nodo_k, menor):
    #menor = sys.maxint
    #for i in range (len(grafo.grafoNodos[nodo_k].nodosAdyacentes)):
    vectorAuxiliar = []
    for i in grafo.grafoNodos[nodo_k].nodosAdyacentes:
        print "I",i
        if grafo.grafoNodos[i-1].nodoVisitado is -1:
            #print "entro a la comparacion"
            #print "yyyy",grafo.grafoNodos[i-1].nodoIndice-1
            #print "que onda wacho",caminoMinimo[grafo.grafoNodos[i-1].nodoIndice-1]
            for j in range(len(caminoMinimo)):
                if caminoMinimo[j] < menor:#caminoMinimo[grafo.grafoNodos[i-1].nodoIndice-1]:#caminoMinimo[i] < menor:
                    #print "entrooooo"
                    menor = caminoMinimo[j]#[grafo.grafoNodos[i-1].nodoIndice-1]#[i]
                    nodo_k = i
                    #print "nodo k dentro de la funcion MENOR",nodo_k
    vectorAuxiliar.append(menor)
    vectorAuxiliar.append(nodo_k)
    #print "returneoo"
    #return menor

    return vectorAuxiliar

def minimo (valor1, valor2):
    if valor1 < valor2:
        return valor1
    elif valor1 > valor2:
        return valor2
    else:
        return valor1
