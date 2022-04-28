#!/bin/bash

unset one
declare -i c
c=1

for f in merged/mer*;
    do
        echo "Testing file $c"
        ./bat $f 28000000 > $c
        c+=1
        pwd
    done

echo "Done!"
