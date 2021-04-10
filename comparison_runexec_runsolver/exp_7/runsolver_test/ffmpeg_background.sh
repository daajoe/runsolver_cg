#!/bin/bash
#end=$((SECONDS+10000))
while true
do
    i=1
    while [ $i -le 2 ]
    do
        ffmpeg -y -nostdin -i ../sampleVideo.mp4 ../sampleVideo_converted.avi > stdout/stdout_ffmpeg_$i.log 2>stderr/stderr_ffmpeg_$i.log
        i=`expr $i + 1`
    done
    echo "ffmpeg ran $SECONDS seconds for `expr $i - 1` times"
sleep 60
done
