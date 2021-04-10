#!/bin/bash
end=$((SECONDS+10000))

while [ $SECONDS -lt $end ]
do
    ffmpeg -y -nostdin -i ../sampleVideo.mp4 ../sampleVideo_converted.avi > stdout/stdout_ffmpeg.log 2>stderr/stderr_ffmpeg.log
done
echo "ffmpeg ran $SECONDS"
