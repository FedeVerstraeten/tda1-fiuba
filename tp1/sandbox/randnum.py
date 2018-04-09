#!/usr/bin/env python
import sys
import random
import numpy as np

LIM_INIT=0
#LIM_F=200

def rand_chart(name,maxsize):
  randfile = open(name, "w" )
  
  randarray = random.sample(range(LIM_INIT,maxsize),maxsize)
  randline = np.asarray(randarray)
  randline.tofile(randfile,sep=",",format='%1.f')

  randfile.close()

if __name__ == '__main__':

  if (len(sys.argv)) == 3:
    file_name = str(sys.argv[1])
    file_name = file_name
    file_lines = int(sys.argv[2])
    rand_chart(file_name,file_lines)
  else:
    print("Execute with arguments: python randnum.py <file_name> <file_size>")