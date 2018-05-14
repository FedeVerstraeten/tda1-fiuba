import math
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def num(s):
        return int(s)

def calcularDistancia(posX1,posY1,posX2,posY2):
    distanciaX = abs(posX2-posX1)
    distanciaY = abs(posY2-posY1)
    pesoCamino = math.sqrt(distanciaX*distanciaX+distanciaY*distanciaY)
    return pesoCamino
