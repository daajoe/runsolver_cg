#!/bin/bash
i=1
while true
do
    echo $i" instance of 100M"
    eatmemory 1G &
    i=`expr $i + 1`
done
