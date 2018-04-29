README
------

Desarrollo en SO: Linux - Ubuntu 16.04
Lenguaje: Python 2.7

Bibliotecas necesarias:
* random
* time
* sys
* csv
* numpy
* pprint

Parte 1 (uno)
-------------

# Modo de ejecución

Generación de 10 set random y ejecución de los Algoritmos de ordenamiento.
Los sets de números se generan en el mismo código de `all_sorting`
Output por salida standard.

`../tp1$ python all_sorting.py dataset`

Generación de peores casos y ejecución de los Algoritmos de ordenamiento.

* Array con todos elementos repetidos ("repeated_array").
* Array ordenado ascendente ("ascending_array").
* Array ordenado descendente ("descending_array").

Output por salida standard.

`../tp1$ ./all_sorting.py worstcase`

Se puede guardar la salida a un archivo y parsear los datos a CSV con el script `parser_result_sorting.sh`
El script generará un archivo por cada algoritmo de ordenamiento, donde las columnas representan la cantidad de corridas y las filas los set de datos.

Ejemplos:

```
../tp1$ python all_sorting.py dataset >> results_dataset_punto_1
../tp1$ bash parser_result_sorting.sh results_dataset_punto_1 
```

```
../tp1$ python all_sorting.py worstcase >> results_worstcase_punto_1
../tp1$ bash parser_result_sorting.sh results_worstcase_punto_1 worstcase
```


Parte 2 (dos)
-------------

# Modo de ejecución 

El programa imprime por la salida standard todo el proceso del "Matching Stable", mostrando al finalizar el estado final.
Para su funcionamiento deben estar precargado los csv con la información de Acceptors (Team) y Proporsers (Players).
En el código se adjuntan los archivos de preferencia para los 200 Players y los 10 Team.

`../tp1$ python gale_shapley.py`


# Generación de sets Player/Team aleatorios

Los sets de datos necesarios para la ejecución el Gale-Shapley, fueron generados con el algoritmo `randnum.py`. El mismo recibe como argumentos el nombre que se desee para el archivo y el largo del arreglo de números aleatorios.

```
../tp1/csv$ python randnum.py <file_name> <file_size>
```