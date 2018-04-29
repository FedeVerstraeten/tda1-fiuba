TP2
---

# Ejercicio 2.3:

Una universidad quiere dictar un conjunto de cursos C1, C2 … Cn donde cada curso se puede dar solo en el intervalo de tiempo Ti, ya que los docentes tienen poca flexibilidad horaria. Puede que varios cursos se den a la vez, por ejemplo el curso 1 puede dictarse de 3 a 6 y el curso 2 de 4 a 8. Conocemos el horario de inicia y finalización de cada uno de los cursos. El objetivo es ver cuál es la menor cantidad de aulas necesarias para acomodar todos los cursos (suponer que todas las aulas son iguales).
1. Dar un algoritmo eficiente (pseudocódigo de alto nivel) que resuelva el problema. 
2. Reducir el problema a una instancia de coloreo de grafos, en su versión de optimización (minimizar la cantidad de colores). 
3. A partir de los dos puntos anteriores, ¿podemos asegurar que P = NP? ¿Por qué? 

## Resumen

Cursos: C1,C2,...,Cn
Int. Tiempo: T(Ci) = Ti = [t0;tf]

Existe superposición de cursos: Ti^Tj <> 0

Datos: t0_i,tf_i tiempos iniciales y finales de cada curso.

OPTIMIZAR: hallar la mínima cantidad de aulas necesarias para acomodar todos los cursos (NO deben superponerse)
1. Dar pseudocódigo.
2. Reducir el problema a una instancia de coloreo de grafos.
3. ¿podemos asegurar que P = NP? ¿Por qué?

---------

## Hacer:

1) Leer sobre problemas P y NP
2) Leer sobre problemas de coloreo de grafos
3) Dar pseudocódigo a la resolución del problema
..
...
....
.....
3*N^7) Lucio ayudame!!!


## Definiciones prblemas P y NP:

```
Unsolved problem in computer science: P =? NP 
If the solution to a problem is easy to check for correctness, is the problem easy to solve?
```

* *P:* solution can be quickly verified (technically, verified in polynomial time) can also be solved quickly (again, in polynomial time)

* *NP:* nondeterministic polynomial time ("tiempo polinomial no determinista")

### NP-naming convention
NP-hard problems do not have to be elements of the complexity class NP. As NP plays a central role in computational complexity, it is used as the basis of several classes:*

* NP: Class of computational decision problems for which a given solution can be verified as a solution in polynomial time by a deterministic Turing machine (or solvable by a non-deterministic Turing machine in polynomial time).
* NP-hard: Class of decision problems which are at least as hard as the hardest problems in NP. Problems that are NP-hard do not have to be elements of NP; indeed, they may not even be decidable.
* NP-complete: Class of decision problems which contains the hardest problems in NP. Each NP-complete problem has to be in NP.
* NP-easy: At most as hard as NP, but not necessarily in NP.
* NP-equivalent: Decision problems that are both NP-hard and NP-easy, but not necessarily in NP.
* NP-intermediate: If P and NP are different, then there exist decision problems in the region of NP that fall between P and the NP-complete problems. (If P and NP are the same class, then NP-intermediate problems do not exist because in this case every NP-complete problem would fall in P, and by definition, every problem in NP can be reduced to an NP-complete problem.)
