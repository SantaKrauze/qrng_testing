#!/usr/bin/python3

import math
import sys
import os
import numpy as np

path1 = "qrng/QNGFile5.dat"
path2 = "qrng/QNGFile6.dat"
shift = int(sys.argv[1])

pathOut = sys.argv[2]

file1 = np.fromfile(path1,dtype='uint8')
bin1 = np.unpackbits(file1)
file2 = np.fromfile(path2,dtype='uint8')
bin2 = np.unpackbits(file2)

size = len(bin1) 
bin3 = bin1^bin2
binMerged = np.empty(3*size,dtype=int)

print("=============================")
print('File 1:',path1,'\nFile 2:',path2,'\nOutput:',pathOut,'\nShift =',shift)

for i in range(0, math.floor(size/shift)):
    for j in range(0,2):
        for k in range(i*shift, (i+1)*shift):
            if j == 0:
                x=bin1[k]
            elif j==1:
                x=bin2[k]
            else:
                x=bin3[k]
            binMerged[k] = x
        print("\r",f'Merging: {i/(size/shift)*100:.1f}%',end="")

out = np.packbits(binMerged)
total = len(out)
print('\nDone. \nTotal size: ',len(out),'B')
print("=============================\n")
out.tofile(pathOut,sep="")
