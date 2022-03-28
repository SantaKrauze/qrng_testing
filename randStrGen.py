import random

file1=open('str1.txt','a')
file2=open('str2.txt','a')

size = 10000000
for i in range(size):
    r2=str(random.randint(0,1))
    r1=str(random.randint(0,1))
    file1.write(r1)
    file2.write(r2)

file1.close()
file2.close()
