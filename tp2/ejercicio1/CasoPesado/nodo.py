from funcionesAux import num, file_len

class nodo:

    def __init__(self, valorX, valorY, indice):
        self.nodoPosicionX = num(valorX)
        self.nodoPosicionY = num(valorY)
        self.nodoIndice = num(indice)
        self.nodoVisitado = -1
        self.nodosAdyacentes = {}

    def agregarNodoAdyacente(self,vecino,ponderacion):
        self.nodosAdyacentes[vecino] = ponderacion
