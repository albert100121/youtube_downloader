#!/usr/bin/env bash

VID_PATH=$1
AUD_PATH=${2:-"sample.mp3"}
ffmpeg -i $VID_PATH -q:a 0 -map a $AUD_PATH
