#!/bin/bash

SORTING_LIST=("InsertionSort" "SelectionSort" "HeapSort" "MergeSort" "QuickSort")
WORSTCASE_LIST=("repeated_array" "ascending_array" "descending_array")
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

parser_result_worst(){
  for sorting in "${SORTING_LIST[@]}";do
    echo "Set/Samples,50,100,500,1000,2000,3000,4000,5000,7000,10000,">> ${sorting}.csv
    for case in "${WORSTCASE_LIST[@]}";do
      echo -n "Set_${case}," >> ${sorting}.csv
      grep "$sorting" -B 2 $RESULTS | grep "'Numero de Set', '$case'" -A 2 |  \
      grep "tLength $sorting:" | sed -r 's/.*\,.(.*)\)/\1/' | tr '\n' ',' >> ${sorting}.csv
      echo "" >> ${sorting}.csv
    done
  done 
}

main(){
  file_parse=$1
  mode=$2
  echo $file_parse
  if [ -z $file_parse ]; then
    echo "Ingrese archivo a pasear"
  else
    if [ $mode == "worstcase" ]; then
      parser_result_worst $file_parse
    else
      parser_result $file_parse
    fi
  fi
}

main $1 $2

exit 0 
