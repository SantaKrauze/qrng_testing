#!/bin/bash

echo "Testing xorg-shifted files..."

echo "Shift = 1b"
./bat merged/merge1.dat 30000000

echo "Shift = 5b"
./bat merged/merge5.dat 30000000

echo "Shift = 10b"
./bat merged/merge10.dat 30000000

echo "Shift = 100b"
./bat merged/merge100.dat 30000000

echo "Shift = 5kb"
./bat merged/merge5k.dat 30000000

echo "Testing original files..."
./bat qrng/QNGFile5.dat 10000000
./bat qrng/QNGFile6.dat 10000000

echo "Done!"
