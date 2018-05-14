from funcionesAux import num, file_len
from nodo import nodo


class Grafo:

    def __init__(self):
        self.grafoNodos = {}
        self.grafoGrado = 0
        xaux=0
        yaux=0
        fichero = open('mapaCiudad')
        indice = 1
        for l in fichero:
            campos = l.split(' ')
            if indice == 1:
                self.grafoNodos[indice-1] = nodo(campos[0],campos[1],indice)
                self.grafoNodos[indice] = nodo(campos[3],campos[4],indice+1)
                #print("")
                self.grafoNodos[indice].agregarNodoAdyacente(self.grafoNodos[indice-1].nodoIndice,1)
                self.grafoNodos[indice-1].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,1)
                indice+=1
            else :
                nodosExistentes = self.nodosExistentesEncontrados(campos)
                if len(nodosExistentes) == 0:
                    self.grafoNodos[indice] = nodo(campos[0],campos[1],indice+1)
                    self.grafoNodos[indice+1] = nodo(campos[3],campos[4],indice+2)
                    self.grafoNodos[indice].agregarNodoAdyacente(self.grafoNodos[indice+1].nodoIndice,1)
                    self.grafoNodos[indice+1].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,1)
                    indice+=2
                else :
                    if  len(nodosExistentes) == 1:
                        if nodosExistentes[0].nodoPosicionX == num(campos[0]) and nodosExistentes[0].nodoPosicionY == num(campos[1]):#aca a veces anda y a veces no :/
                            self.grafoNodos[indice] = nodo(campos[3],campos[4],indice+1)
                            self.grafoNodos[indice].agregarNodoAdyacente(nodosExistentes[0].nodoIndice,1)
                            nodosExistentes[0].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,1)
                            indice+=1
                        if nodosExistentes[0].nodoPosicionX == num(campos[3]) and nodosExistentes[0].nodoPosicionY == num(campos[4]):
                            self.grafoNodos[indice] = nodo(campos[0],campos[1],indice+1)
                            self.grafoNodos[indice].agregarNodoAdyacente(nodosExistentes[0].nodoIndice,1)
                            nodosExistentes[0].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,1)
                            indice+=1
                    if len(nodosExistentes) == 2:

                        nodosExistentes[0].agregarNodoAdyacente(nodosExistentes[1].nodoIndice,1)
                        nodosExistentes[1].agregarNodoAdyacente(nodosExistentes[0].nodoIndice,1)

        self.grafoGrado = indice
        print self.grafoGrado



    def nodosExistentesEncontrados(self , campos):
        nodosExistentes = {}
        for j in range(len(self.grafoNodos)):
            if  (num(campos[0]) == self.grafoNodos[j].nodoPosicionX and num(campos[1]) == self.grafoNodos[j].nodoPosicionY) :
                nodosExistentes[0] = self.grafoNodos[j]
            elif   (num(campos[3]) == self.grafoNodos[j].nodoPosicionX and num(campos[4]) == self.grafoNodos[j].nodoPosicionY) :
                nodosExistentes[1] = self.grafoNodos[j]
        return nodosExistentes




    def mostrarNodos(self):
        for i in range(self.grafoGrado):
            print "nodo",self.grafoNodos[i].nodoIndice,"con x=",self.grafoNodos[i].nodoPosicionX,"con y=",self.grafoNodos[i].nodoPosicionY
            print "nodo",self.grafoNodos[i].nodoIndice,"conectado a:",self.grafoNodos[i].nodosAdyacentes.keys()
            print "\n"

    def vincularNodos(self,nodo1,nodo2):
        self.grafoNodos[nodo1-1].agregarNodoAdyacente(self.grafoNodos[nodo2-1].nodoIndice,1)

    def resetear(self):
        for i in range(self.grafoGrado):
            self.grafoNodos[i].nodoVisitado = -1


    def tomarNodosPorConsola(self):
        nodosPosicionesIngresadas = []
        print "indique posicionX del nodo del Espia 1"
        nodoPosicionXEspia1 = input()
        print "indique posicionY del nodo del Espia 1"
        nodoPosicionYEspia1 = input()
        print "indique posicionX del nodo del Espia 2"
        nodoPosicionXEspia2 = input()
        print "indique posicionY del nodo del Espia 2"
        nodoPosicionYEspia2 = input()
        print "indique posicionX del nodo del Aeropuerto"
        nodoPosicionXAeropuerto = input()
        print "indique posicionY del nodo del Aeropuerto"
        nodoPosicionYAeropuerto = input()
        for i in range(self.grafoGrado):
            if self.grafoNodos[i].nodoPosicionX == num(nodoPosicionXEspia1) and self.grafoNodos[i].nodoPosicionY == num(nodoPosicionYEspia1):
                #nodoEspia1 = self.grafoNodos[i]
                nodosPosicionesIngresadas.append(self.grafoNodos[i])
        for i in range(self.grafoGrado):
            if self.grafoNodos[i].nodoPosicionX == num(nodoPosicionXEspia2) and self.grafoNodos[i].nodoPosicionY == num(nodoPosicionYEspia2):
                #nodoEspia1 = self.grafoNodos[i]
                nodosPosicionesIngresadas.append(self.grafoNodos[i])
        for i in range(self.grafoGrado):
            if self.grafoNodos[i].nodoPosicionX == num(nodoPosicionXAeropuerto) and self.grafoNodos[i].nodoPosicionY == num(nodoPosicionYAeropuerto):
                #nodoEspia1 = self.grafoNodos[i]
                nodosPosicionesIngresadas.append(self.grafoNodos[i])
        return nodosPosicionesIngresadas#nodoEspia1
