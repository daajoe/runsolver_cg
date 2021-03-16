#!/bin/sh
i=0
while [ $i -le 49 ]
do
    runexec --timelimit 14400s python3 test_cpu.py > stdout_new_$i.txt 2>stderr_new_$i.txt
    i=`expr $i + 1`
done
