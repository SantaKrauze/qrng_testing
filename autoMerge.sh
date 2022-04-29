#!/bin/bash

echo "Starting"

./randStrMerge.py 1 merge1.dat
./randStrMerge.py 5 merge5.dat
./randStrMerge.py 10 merge10.dat
./randStrMerge.py 50 merge50.dat
./randStrMerge.py 100 merge100.dat
./randStrMerge.py 500 merge500.dat
./randStrMerge.py 1000 merge1k.dat
./randStrMerge.py 5000 merge5k.dat
./randStrMerge.py 50000 merge50k.dat
./randStrMerge.py 500000 merge500k.dat
./randStrMerge.py 5000000 merge5M.dat

echo "All done"
