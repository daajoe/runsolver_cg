#!/bin/sh
i=0
while [ $i -le 1 ]
do
    #runexec --timelimit 3s python3 test_cpu_updated.py > stdout_new.txt 2>stderr_new.txt
    runexec --timelimit 24s python3 test_cpu_updated.py > stdout_new_$i.txt 2>stderr_new_$i.txt
    i=`expr $i + 1`
done