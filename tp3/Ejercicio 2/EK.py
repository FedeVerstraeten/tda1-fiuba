import copy
from BFS import BFS
from cuelloBotella import bottleNeck
from aristasDebiles import aristasDebiles

def EK(grafo, nodoInicial):

    grafoAuxiliar = copy.deepcopy(grafo)
    nodoInicialAux = copy.deepcopy(nodoInicial)
    nodosVisitados = {}
    capacidadesAristas = []
    nodosVisitados[0] = nodoInicial
    flujoMaximo = 0

    cuelloBotella = bottleNeck(grafoAuxiliar)
    grafoAuxiliar.generarDigrafo()
    grafoAuxiliar.mostrarNodos()
    f_aumenting_path = BFS(grafoAuxiliar, nodoInicialAux)
    f_aumenting_path2 = None
    
    while f_aumenting_path == f_aumenting_path2:
        for nodos in f_aumenting_path:

            for key in grafoAuxiliar.grafoNodos[nodos].nodosAdyacentes:
                grafoAuxiliar.grafoNodos[nodos].nodosAdyacentes[key] = grafoAuxiliar.grafoNodos[nodos].nodosAdyacentes[key] - cuelloBotella
                for key2 in grafoAuxiliar.grafoNodos[key].nodosAdyacentes:
                    if nodos == key2:
                        grafoAuxiliar.grafoNodos[key].nodosAdyacentes[nodos] = grafoAuxiliar.grafoNodos[key].nodosAdyacentes[nodos] + cuelloBotella
        flujoMaximo = flujoMaximo + cuelloBotella
        f_aumenting_path2 = BFS(grafoAuxiliar, nodoInicialAux)

    print 'las aristas debiles son', aristasDebiles(grafoAuxiliar, f_aumenting_path)
