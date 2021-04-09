#!/bin/sh
i=1
while [ $i -le 10 ]
do
    runexec --walltimelimit 900s --output output/output_$i.txt python3 test.py > stdout/stdout_$i.txt 2>stderr/stderr_$i.txt
    i=`expr $i + 1`
done
