#!/bin/sh
python3 test_cpu.py;
i=1
while [ $i -le 6 ]
do
    echo $i" instance of 1GB"
    eatmemory/eatmemory 1G & sleep 1;
    i=`expr $i + 1`
done
