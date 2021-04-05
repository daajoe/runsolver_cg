#!/bin/sh
i=1
while [ $i -le 15 ]
do
    runsolver/src/runsolver -M 5120 -w output/watcher_$i.txt ./test_run.sh > std_out/stdout_$i.txt 2>std_err/stderr_$i.txt
    i=`expr $i + 1`
    sleep 5
done
