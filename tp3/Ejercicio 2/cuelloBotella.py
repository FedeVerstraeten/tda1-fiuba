def bottleNeck(grafoAuxiliar):


    capacidadesAristas = []

    for i in grafoAuxiliar.grafoNodos:
        for key in grafoAuxiliar.grafoNodos[i].nodosAdyacentes.keys():

            capacidadesAristas.append(grafoAuxiliar.grafoNodos[i].nodosAdyacentes[key])
            cuelloBotella = min(capacidadesAristas)
    print 'el cuello de botella es:',cuelloBotella
    return cuelloBotella
