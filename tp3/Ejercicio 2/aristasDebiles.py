
def aristasDebiles(grafoAuxiliar,f_aumenting_path):

    aristasDebiles = []
    vectorAuxiliar = []

    for i in f_aumenting_path:
        for key in grafoAuxiliar.grafoNodos[i].nodosAdyacentes.keys():
            if i < len(f_aumenting_path)-1:
                for j in f_aumenting_path:
                    if key == j and key != i:
                        vectorAuxiliar.append(grafoAuxiliar.grafoNodos[i].nodosAdyacentes[key])

    aristasDebiles.append(max(vectorAuxiliar))
    vectorAuxiliar.remove(max(vectorAuxiliar))
    aristasDebiles.append(max(vectorAuxiliar))
    return aristasDebiles
