#!/usr/bin/python 

import random
from random import randint
import time
import sys
import csv
import pprint

SIZE_ARRAY = 10000
MAX_NUM = 10000
NUM_ARRAYS = 10


sys.setrecursionlimit(15000000)

###################### Heap Sort ##################################

def swap(i, j, arr):                    
    arr[i], arr[j] = arr[j], arr[i] 


def heapify(end, i, arr):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if (l < end and arr[i] < arr[l]):   
        max = l   
    if (r < end and arr[max] < arr[r]):   
        max = r   
    if (max != i):   
        swap(i, max, arr)   
        heapify(end, max, arr)   


def heapSort(arr):     
    end = len(arr)   
    start = end // 2 - 1 # division entera
    for i in range(start, -1, -1):   
        heapify(end, i, arr)   
    for i in range(end-1, 0, -1):   
        swap(i, 0, arr)   
        heapify(i, 0, arr)   



###################### Merge Sort ##################################


def mergeSort(nlist):
  if (len(nlist)>1):
    mid = len(nlist)//2
    lefthalf = nlist[:mid]
    righthalf = nlist[mid:]

    mergeSort(lefthalf)
    mergeSort(righthalf)
    i=j=k=0       
    while (i < len(lefthalf) and j < len(righthalf)):
      if (lefthalf[i] < righthalf[j]):
        nlist[k]=lefthalf[i]
        i=i+1
      else:
        nlist[k]=righthalf[j]
        j=j+1
      k=k+1

    while (i < len(lefthalf)):
      nlist[k]=lefthalf[i]
      i=i+1
      k=k+1

    while (j < len(righthalf)):
      nlist[k]=righthalf[j]
      j=j+1
      k=k+1

###################### Quick Sort ##################################

def quickSort(array):
  less = []
  equal = []
  greater = []
  if len(array) > 1:
    pivot = array[0]
    for x in array:
      if x < pivot:
        less.append(x)
      if x == pivot:
        equal.append(x)
      if x > pivot:
        greater.append(x)
    return quickSort(less) + equal + quickSort(greater)
  else:
      return array


###################### Insertion Sort ##################################

def insertionSort(myList, first_position, last_position):
  for i in range(first_position+1,last_position):
    aux=myList[i]
    j=i-1
    while j>=first_position and aux<myList[j]:
      myList[j+1]=myList[j]
      j=j-1
    myList[j+1]=aux


###################### Selection Sort ##################################

def selectionSort(myList, first_position, last_position):
  for i in range(first_position,last_position-1):
    swap2(myList,i,posMin(myList,i,last_position))


def swap2(myList,i,j):
  aux=myList[i]
  myList[i]=myList[j]
  myList[j]=aux


def posMin(myList,i,j):
  pmin=i
  for k in range(i+1,j):
    if myList[k]<myList[pmin]:
      pmin=k

  return pmin



########################################################################

def randomIntegerArray(n):
  nlist = [randint(0, MAX_NUM) for _ in range(n)]
  return nlist


def analyzeSortingAlgorithms(arr, i, j):
  arr1 = arr[:]     #hacemos una copia del array
  tStart = time.time()
  heapSort(arr1)
  tEnd = time.time()
  print("Numero de Set", i)
  print("Cantidad elementos", j)
  print("tLength HeapSort:", tEnd - tStart)
  print("-------------")
  
  arr2 = arr[:]
  tStart = time.time()
  mergeSort(arr2)
  tEnd = time.time()
  print("Numero de Set", i)
  print("Cantidad elementos", j)
  print("tLength MergeSort:", tEnd - tStart)
  print("-------------")

  arr3 = arr[:]
  tStart = time.time()
  quickSort(arr3)
  tEnd = time.time()
  print("Numero de Set", i)
  print("Cantidad elementos", j)
  print("tLength QuickSort:", tEnd - tStart)
  print("-------------")

  arr4 = arr[:]
  tStart = time.time()
  insertionSort(arr4, 0, len(arr4))
  tEnd = time.time()
  print("Numero de Set", i)
  print("Cantidad elementos", j)
  print("tLength InsertionSort:", tEnd - tStart)
  print("-------------")

  arr5 = arr[:]
  tStart = time.time()
  selectionSort(arr5, 0, len(arr5))
  tEnd = time.time()
  print("Numero de Set", i)
  print("Cantidad elementos", j)
  print("tLength SelectionSort:", tEnd - tStart)
  print("-------------")

def worstcaseSortingAlgorithms():
  
  # Repeated array
  array = [1] * SIZE_ARRAY
  for j in [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, SIZE_ARRAY]:
    slicedArray = array[:j]
    analyzeSortingAlgorithms(slicedArray,"repeated_array",j)

  # Array ordered ascending
  array = [i for i in xrange(SIZE_ARRAY)]
  for j in [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, SIZE_ARRAY]:
    slicedArray = array[:j]
    analyzeSortingAlgorithms(slicedArray,"ascending_array",SIZE_ARRAY)
  
  # Array ordered descending
  array = [(SIZE_ARRAY-1)-i for i in xrange(SIZE_ARRAY)]
  for j in [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, SIZE_ARRAY]:
    slicedArray = array[:j]
    analyzeSortingAlgorithms(slicedArray,"descending_array",SIZE_ARRAY)

def datasetSortingAlgorithms():
  
  # Array initialization
  arrays = [0,1,2,3,4,5,6,7,8,9]
  for i in range(0, NUM_ARRAYS):
    arrays[i] = randomIntegerArray(SIZE_ARRAY)

  for i in range(0, NUM_ARRAYS):
    for j in [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]:
      slicedArray = arrays[i][:j]
      analyzeSortingAlgorithms(slicedArray, i, j)

########################################################################

def RunPunto1(mode):

  if mode == "worstcase":
    worstcaseSortingAlgorithms()
  elif mode == "dataset":
    datasetSortingAlgorithms()


############################## MAIN ####################################

def main():

  # Exec options
  if len(sys.argv) > 1:
    execMode = sys.argv[1]

    if execMode == "worstcase":
      print "Analysis of the worst case."
      RunPunto1("worstcase")

    elif execMode == "dataset":
      print "Analysis for the data set."
      RunPunto1("dataset")
    else:
      print "Invalid option."
 
  # Default case
  else:
    RunPunto1("dataset")

if __name__ == '__main__':
  main()