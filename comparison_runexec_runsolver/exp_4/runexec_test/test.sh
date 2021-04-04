#!/bin/sh
i=1
while [ $i -le 15 ]
do
    runexec --memlimit 5368709120 --output output/output_$i.txt ./test_run.sh > std_out/stdout_$i.txt 2>std_err/stderr.txt
    i=`expr $i + 1`
    sleep 5
done
