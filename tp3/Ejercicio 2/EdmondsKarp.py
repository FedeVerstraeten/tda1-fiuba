#from cola import cola
import copy
def EdmondsKarp(grafo, nodoInicial):

    grafoAuxiliar = copy.deepcopy(grafo)
    nodosVisitados = {}
    capacidadesAristas = []
    nodosVisitados[0] = nodoInicial


    for i in grafoAuxiliar.grafoNodos:
        print(grafoAuxiliar.grafoNodos[i].nodosAdyacentes.values())
        for key in grafoAuxiliar.grafoNodos[i].nodosAdyacentes.keys():

            print grafoAuxiliar.grafoNodos[i].nodosAdyacentes[key]
            capacidadesAristas.append(grafoAuxiliar.grafoNodos[i].nodosAdyacentes[key])
            print capacidadesAristas
            cuelloBotella = min(capacidadesAristas)
    print 'el cuello de botella es:',cuelloBotella

    for i in grafoAuxiliar.grafoNodos:
        for key in grafoAuxiliar.grafoNodos[i].nodosAdyacentes.keys():
            if key != None :
                if grafoAuxiliar.grafoNodos[key].nodoVisitado == -1:
                    nodosVisitados[i] = key #grafoAuxiliar.grafoNodos[i].nodosAdyacentes.keys()[0]
                    grafoAuxiliar.grafoNodos[key].nodoVisitado = 1
    print 'el corte uno es :',nodosVisitados.keys()
    return nodosVisitados#cuelloBotella
