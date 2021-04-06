#!/bin/sh
i=1
while [ $i -le 50 ]
do
    runexec --timelimit 7200s python3 test_cpu.py > std_out/stdout_$i.txt 2>std_err/stderr_$i.txt
    i=`expr $i + 1`
    sleep 2
done
