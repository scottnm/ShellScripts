#!/bin/bash

MyRepo=ClassRepo/ClassProjects/C/Syr2k
CollabRepo=MattCollab/

for file in $(find "$CollabRepo" -name *.pdf -o -name *.c -o -name *.h -o -name *.m)
do
    if [ -f "$file" ];
    then
        CommonFileName=${file#$CollabRepo}
        if [ -f "$MyRepo/$CommonFileName" ];
        then
            cp $MyRepo/$CommonFileName $CollabRepo/$CommonFileName
            echo "Updating... $CommonFileName"
        fi
    fi
done
