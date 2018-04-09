import random
from random import randint

import time
import sys

SIZE_ARRAY = 10000
MAX_NUM = 10000
NUM_ARRAYS = 10

sys.setrecursionlimit(15000000)

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
    start = end // 2 - 1 
    for i in range(start, -1, -1):   
        heapify(end, i, arr)   
    for i in range(end-1, 0, -1):   
        swap(i, 0, arr)   
        heapify(i, 0, arr)   



#########################################################################

def mergeSort(nlist):
    #print("Dividiendo ",nlist)
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
    #print("Mergeando ",nlist)

########################################################################

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


########################################################################

def insertionSort(myList, first_position, last_position):
  for i in range(first_position+1,last_position):
    aux=myList[i]
    j=i-1
    while j>=first_position and aux<myList[j]:
      myList[j+1]=myList[j]
      j=j-1
    myList[j+1]=aux


########################################################################

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


def analyzeOrderingAlgorithms(arr, i, j):
  arr1 = arr[:]
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




def main():
  #nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
  arrays = [0,1,2,3,4,5,6,7,8,9]

  #inicializamos los 10 arreglos...
  for i in range(0, NUM_ARRAYS):
      arrays[i] = randomIntegerArray(SIZE_ARRAY)

  for i in range(0, NUM_ARRAYS):
    for j in [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]:
      slicedArray = arrays[i][:j]
      analyzeOrderingAlgorithms(slicedArray, i, j)




main()