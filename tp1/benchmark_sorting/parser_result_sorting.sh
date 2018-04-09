#!/bin/bash

SORTING_LIST=("InsertionSort" "SelectionSort" "HeapSort" "MergeSort" "QuickSort")
RESULTS="$1"

parser_result(){
  for sorting in "${SORTING_LIST[@]}";do
    echo "Set/Samples,50,100,500,1000,2000,3000,4000,5000,7000,10000,">> ${sorting}.csv
    for i in {0..9};do
      echo -n "Set_${i}," >> ${sorting}.csv
      grep "$sorting" -B 2 $RESULTS | grep "'Numero de Set', $i" -A 2 |  \
      grep "tLength $sorting:" | sed -r 's/.*\,.(.*)\)/\1/' | tr '\n' ',' >> ${sorting}.csv
      echo "" >> ${sorting}.csv
    done
  done 
}

main(){
  if [ -z "$1" ]; then
    echo "Ingrese archivo a pasear"
  else
    parser_result $1
  fi
}

main $1

exit 0 