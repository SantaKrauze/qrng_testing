#!/bin/bash

echo "Starting"

./randStrMerge.py 5 merge5.dat
./randStrMerge.py 10 merge10.dat
./randStrMerge.py 50 merge50.dat
./randStrMerge.py 100 merge100.dat
./randStrMerge.py 500 merge5.dat
./randStrMerge.py 1000 merge5.dat

echo "All done"