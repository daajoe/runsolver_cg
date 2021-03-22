#!/bin/sh
i=1
while [ $i -le 50 ]
do
    ~/runsolver_cg/comparison_runexec_runsolver/exp_1/runsolver_test/runsolver/src/runsolver -C 14400s -w output/watcher_$i.txt python3 test_cpu.py > std_out/stdout_$i.txt 2>std_err/stderr_$i.txt
    i=`expr $i + 1`
    sleep 2
done
