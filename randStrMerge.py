#!/usr/bin/python3

import math
import sys
import os
import time
import numpy as np

t1 = time.time()
path1 = "qrng/QNGFile1.dat"
path2 = "qrng/QNGFile2.dat"
shift = int(sys.argv[1])

pathOut = "merged/"+sys.argv[2]

file1 = np.fromfile(path1,dtype='uint8')
bin1 = np.unpackbits(file1)
file2 = np.fromfile(path2,dtype='uint8')
bin2 = np.unpackbits(file2)

size = len(bin1)
bin3 = bin1^bin2
binMerged = np.empty(3*size,dtype=int)

print("=============================")
print('File 1:',path1,'\nFile 2:',path2,'\nOutput:',pathOut,'\nShift =',shift)

n = 0
for i in range(0, math.floor(size/shift)):
    for j in range(0,3):
        for k in range(i*shift, (i+1)*shift):
            if j == 0:
                x=bin1[k]
            elif j==1:
                x=bin2[k]
            else:
                x=bin3[k]
            binMerged[n] = x
            #print(n)
            n +=1
            #print(k+j*shift,bin1[k],bin2[k],bin3[k],x)
            print("\r",f'Merging: {n/3/size*100:.2f}%',end="")

out = np.packbits(binMerged)
total = n
#print(binMerged)
#print(out)
t2 = time.time()
sec = t2 - t1
mins = math.floor(sec/60)

print('\nDone in {0:.0f}min {1:.0f}s. \nTotal size: {2}b'.format(mins,sec%60,total))
print("=============================\n")
out.tofile(pathOut,sep="")
