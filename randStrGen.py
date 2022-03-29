#!/usr/bin/python3
import random
import numpy as np
import sys

pathOut = sys.argv[2]
size = int(sys.argv[1])
binMerged = np.empty(0,dtype=int)

print("==========================")
print('File :',pathOut,'\nSize =',size)

for i in range(0, size):
    a = random.randint(0,1)
    binMerged = np.append(binMerged,a)
    print("\r",f'Gen: {i/(size)*100:.1f}%',end="")

out = np.packbits(binMerged)
out.tofile(pathOut,sep="")
print('\nDone. \nTotal size:',len(binMerged),'b')
print("==========================\n")
