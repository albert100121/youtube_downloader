#!/usr/bin/env bash

URL_PATH=$1
OUT_DIR=${2:-"downloaded_videos"}
# Download youtube-dl
if [ ! conda list | grep youtube-dl ]
then 
    pip install git+https://github.com/ytdl-org/youtube-dl.git@master#egg=youtube_dl --force-reinstall
else
    echo "youtube-dl already installed!!!"
fi

# python
python yt-download.py -u $URL_PATH -o $OUT_DIR
