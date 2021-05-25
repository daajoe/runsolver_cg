#!/bin/bash
i=1
while [ $i -le 100 ]
do
    /usr/bin/time -v ffmpeg -y -nostdin -i ../sampleVideo.mp4 ../sampleVideo_converted.avi > stdout_ffmpeg/ffmpeg_$i.log 2>stderr_ffmpeg/ffmpeg_$i.log
    i=`expr $i + 1`
done
echo "ffmpeg ran $SECONDS seconds for `expr $i - 1` times"
echo "execution complete"
