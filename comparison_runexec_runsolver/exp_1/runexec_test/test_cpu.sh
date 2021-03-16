#!/bin/sh
i=0
while [ $i -le 49 ]
do
    runexec --timelimit 14400s --output output/output_$i.log python3 test_cpu.py > output/stdout_$i.txt 2>output/stderr_$i.txt
    i=`expr $i + 1`
    sleep 2
done
