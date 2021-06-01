#!/bin/bash
i=1
while [ $i -le 10 ]
do
    /usr/bin/time -v ffmpeg -y -nostdin -i ~/sampleBigVideo.mp4 ../sampleBigVideo_converted.avi > stdout_ffmpeg/ffmpeg_$i.log 2>stderr_ffmpeg/ffmpeg_$i.log
    i=`expr $i + 1`
done
echo "ffmpeg ran $SECONDS seconds for `expr $i - 1` times"
echo "execution complete"
