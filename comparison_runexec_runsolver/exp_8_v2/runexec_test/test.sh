#!/bin/bash
i=1
while [ $i -le 10 ]
do
    runexec --output output/output_$i.log ./ffmpeg.sh > output/stdout_$i.log 2>output/stderr_$i.log
    i=`expr $i + 1`
done
