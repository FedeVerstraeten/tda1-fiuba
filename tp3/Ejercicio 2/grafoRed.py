from funcionesAux import num, file_len, calcularDistancia
from nodo import nodo


class Grafo:

    def __init__(self):
        self.grafoNodos = {}
        self.grafoGrado = 0
        xaux=0
        yaux=0
        fichero = open('redsecreta.txt')
        indice = 1
        for l in fichero:
            campos = l.split(' ')
            peso = num(campos[2])
            if indice == 1:
                self.grafoNodos[indice-1] = nodo(campos[0])
                self.grafoNodos[indice] = nodo(campos[1])
                #self.grafoNodos[indice].agregarNodoAdyacente(self.grafoNodos[indice-1].nodoIndice,peso)
                self.grafoNodos[indice-1].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,peso)
                indice+=1
            else :
                nodosExistentes = self.nodosExistentesEncontrados(campos)
                if len(nodosExistentes) == 0:
                    self.grafoNodos[indice] = nodo(campos[0])
                    self.grafoNodos[indice+1] = nodo(campos[1])
                    self.grafoNodos[indice].agregarNodoAdyacente(self.grafoNodos[indice+1].nodoIndice,peso)
                    #self.grafoNodos[indice+1].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,peso)
                    indice+=2
                else :
                    if  len(nodosExistentes) == 1:
                        if nodosExistentes[0].nodoIndice == num(campos[0]) :#aca a veces anda y a veces no :/
                            self.grafoNodos[indice] = nodo(campos[1])
                            #self.grafoNodos[indice].agregarNodoAdyacente(nodosExistentes[0].nodoIndice,peso)
                            nodosExistentes[0].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,peso)
                            indice+=1
                        if nodosExistentes[0].nodoIndice == num(campos[1]):
                            self.grafoNodos[indice] = nodo(campos[0])
                            self.grafoNodos[indice].agregarNodoAdyacente(nodosExistentes[0].nodoIndice,peso)
                            #nodosExistentes[0].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,peso)
                            indice+=1
                    if len(nodosExistentes) == 2:
                        nodosExistentes[0].agregarNodoAdyacente(nodosExistentes[1].nodoIndice,peso)
                        #nodosExistentes[1].agregarNodoAdyacente(nodosExistentes[0].nodoIndice,peso)

        self.grafoGrado = indice
        print self.grafoGrado



    def nodosExistentesEncontrados(self , campos):
        nodosExistentes = {}
        for j in range(len(self.grafoNodos)):
            if  (num(campos[0]) == self.grafoNodos[j].nodoIndice) :
                nodosExistentes[0] = self.grafoNodos[j]
            elif   (num(campos[1]) == self.grafoNodos[j].nodoIndice) :
                nodosExistentes[1] = self.grafoNodos[j]
        return nodosExistentes




    def mostrarNodos(self):
        for i in range(self.grafoGrado):
            print "nodo",self.grafoNodos[i].nodoIndice,"conectado a:",self.grafoNodos[i].nodosAdyacentes#.keys()
            print "\n"

    def vincularNodos(self,nodo1,nodo2):
        self.grafoNodos[nodo1-1].agregarNodoAdyacente(self.grafoNodos[nodo2-1].nodoIndice,1)

    def resetear(self):
        for i in range(self.grafoGrado):
            self.grafoNodos[i].nodoVisitado = -1




    def generarDigrafo(self):
        self.grafoNodos = {}
        self.grafoGrado = 0

        fichero = open('redsecreta.txt')
        indice = 1
        for l in fichero:
            campos = l.split(' ')
            peso = num(campos[2])
            if indice == 1:
                self.grafoNodos[indice-1] = nodo(campos[0])
                self.grafoNodos[indice] = nodo(campos[1])
                self.grafoNodos[indice].agregarNodoAdyacente(self.grafoNodos[indice-1].nodoIndice,0)
                self.grafoNodos[indice-1].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,peso)
                indice+=1
            else :
                nodosExistentes = self.nodosExistentesEncontrados(campos)
                if len(nodosExistentes) == 0:
                    self.grafoNodos[indice] = nodo(campos[0])
                    self.grafoNodos[indice+1] = nodo(campos[1])
                    self.grafoNodos[indice].agregarNodoAdyacente(self.grafoNodos[indice+1].nodoIndice,peso)
                    self.grafoNodos[indice+1].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,0)
                    indice+=2
                else :
                    if  len(nodosExistentes) == 1:
                        if nodosExistentes[0].nodoIndice == num(campos[0]) :#aca a veces anda y a veces no :/
                            self.grafoNodos[indice] = nodo(campos[1])
                            self.grafoNodos[indice].agregarNodoAdyacente(nodosExistentes[0].nodoIndice,0)
                            nodosExistentes[0].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,peso)
                            indice+=1
                        if nodosExistentes[0].nodoIndice == num(campos[1]):
                            self.grafoNodos[indice] = nodo(campos[0])
                            self.grafoNodos[indice].agregarNodoAdyacente(nodosExistentes[0].nodoIndice,peso)
                            nodosExistentes[0].agregarNodoAdyacente(self.grafoNodos[indice].nodoIndice,0)
                            indice+=1
                    if len(nodosExistentes) == 2:
                        nodosExistentes[0].agregarNodoAdyacente(nodosExistentes[1].nodoIndice,peso)
                        nodosExistentes[1].agregarNodoAdyacente(nodosExistentes[0].nodoIndice,0)

        self.grafoGrado = indice
        print self.grafoGrado
