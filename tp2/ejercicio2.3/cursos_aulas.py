#!/usr/bin/python 

import pprint

########################### DEFINITIONS ################################

lista_cursos = [
  {
    "name": "C1",
    "time_init": 0,
    "time_finish": 3,
  },
  {
    "name": "C2",
    "time_init": 1,
    "time_finish": 4,
  },
  {
    "name": "C3",
    "time_init": 5,
    "time_finish": 6,
  },
  {
    "name": "C4",
    "time_init": 0,
    "time_finish": 2,
  },
  {
    "name": "C5",
    "time_init": 2,
    "time_finish": 6,
  },
  {
    "name": "C6",
    "time_init": 0,
    "time_finish": 1,
  },
  {
    "name": "C7",
    "time_init": 6,
    "time_finish": 8,
  },
]

########################################################################

def buscar_min_intervalo(lista_cursos):

  t_min=0

  for curso in lista_cursos:
    time_init=curso["time_init"]
    time_finish=curso["time_finish"]

    if t_min == 0:
      t_min=time_finish - time_init
  
    if (time_finish - time_init) < t_min:
      t_min=time_finish - time_init
  
  return t_min  

def buscar_tiempo_final(lista_cursos):

  t_fin=0

  for curso in lista_cursos:
    time_finish=curso["time_finish"]

    if time_finish > t_fin:
      t_fin=time_finish

  return t_fin  

def acomodar_cursos_aulas(lista_cursos):
  # Tiempo
  t_actual=0
  t_int=buscar_min_intervalo(lista_cursos)
  t_final=buscar_tiempo_final(lista_cursos)

  # Pila
  aulas=[]
  max_aulas=0

  # Recorro tiempo desde 0 hasta tiempo final
  while t_actual <= t_final:
    
    for curso in lista_cursos:      
      
      if curso["time_init"] == t_actual:
        print "Curso a apilar",curso["name"],curso["time_init"]
        aulas.append(curso["name"])

      if curso["time_finish"] == t_actual:
        print "Curso a desapilar",curso["name"],curso["time_finish"]
        aulas.remove(curso["name"])

    # Incremento tiempo actual
    print "tiempo actual:",t_actual
    print "aulas ocupadas por:",aulas
    t_actual+=t_int

    if max_aulas < len(aulas):
      max_aulas=len(aulas)
  
  return max_aulas    


############################## MAIN ####################################

def main():
  global lista_cursos
  max_aulas=acomodar_cursos_aulas(lista_cursos)
  print "Max cantidad de aulas:",max_aulas

if __name__ == '__main__':
  main()