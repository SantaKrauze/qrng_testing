#!/bin/bash

unset one
declare -i c
c=1

mkdir -p res_merged

echo "Testing merged files"
for f in merged/mer*;
    do
        file=$(basename "$f")
        echo "Testing file $file (no. $c)"
        ./bat $f 28000000 1 > res_merged/res_$file
        echo "No. $c done"
        c+=1
        
    done

echo "Done!"
