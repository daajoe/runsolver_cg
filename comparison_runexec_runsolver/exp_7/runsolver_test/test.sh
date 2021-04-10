#!/bin/sh
i=1
while [ $i -le 10 ]
do
    runsolver/src/runsolver -W 900s -w output/watcher_$i.txt python3 test.py > stdout/stdout_$i.txt 2>stderr/stderr_$i.txt
    i=`expr $i + 1`
done
