from funcionesAux import num, file_len

class nodo:

    def __init__(self, indice):
        self.nodoIndice = num(indice)
        self.nodoVisitado = -1
        self.nodosAdyacentes = {}

    def agregarNodoAdyacente(self,vecino,ponderacion):
        self.nodosAdyacentes[vecino] = ponderacion
