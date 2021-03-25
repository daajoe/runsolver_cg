#!/bin/sh
i=1
while [ $i -le 50 ]
do
    runexec --memlimit 6442450944 --output output/output_$i python3 test_memory.py > std_out/stdout_$i.txt 2>std_err/stderr_$i.txt
    i=`expr $i + 1`
    sleep 10
done
