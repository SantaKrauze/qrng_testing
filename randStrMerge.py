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
binMerged = np.empty(0,dtype=int)

print("=============================")
print('File 1:',path1,'\nFile 2:',path2,'\nOutput:',pathOut,'\nShift =',shift)

for i in range(0, math.floor(size/shift)+1):
    a = bin1[i*shift:(i+1)*shift]
    b = bin2[i*shift:(i+1)*shift]
    c = bin3[i*shift:(i+1)*shift]
    d = np.concatenate((a,b,c))
    binMerged = np.concatenate((binMerged,d))    
    print("\r",f'Merging: {i/(size/shift)*100:.1f}%',end="")

out = np.packbits(binMerged)
total = len(out)
print('\nDone. \nTotal size: ',len(out),'B')
print("=============================\n")

out.tofile(pathOut,sep="")
