#!/bin/bash
i=1
while true
do
    echo $i" instance of 1GB"
    eatmemory 1G & sleep 1;
    i=`expr $i + 1`
done
