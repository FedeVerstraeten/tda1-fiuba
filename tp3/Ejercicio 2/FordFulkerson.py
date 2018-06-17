import copy
from EdmondsKarp import EdmondsKarp

def FordFulkerson(grafo, nodoInicial):


    grafoAuxiliar = copy.deepcopy(grafo)
    nodosVisitados = {}
    capacidadesAristas = []
    nodosVisitados[0] = nodoInicial
    flujo = 0

    f_aumenting_path = EdmondsKarp(grafo, nodoInicial)
    while f_aumenting_path != None:
        delta_p = min (f_aumenting_path)


        for i in f_aumenting_path:
            print(f_aumenting_path[i].nodosAdyacentes.values())
            for key in f_aumenting_path[i].nodosAdyacentes.keys():

                print f_aumenting_path[i].nodosAdyacentes[key]
                if key == f_aumenting_path[i+1]:
                    flujo = flujo + delta_p
                else :
                    flujo = flujo - delta_p
        f_aumenting_path = EdmondsKarp(grafo, nodoInicial)

    print 'el corte uno es :',nodosVisitados.keys()
    return nodosVisitados.keys()
