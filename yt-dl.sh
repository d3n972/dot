#!/bin/bash
if [[ -z $1 ]]; then
    echo "Usage: $0 <title> <playlist_id>"
else
archive=$(echo $1|md5sum|awk -F' ' '{print $1}')
title=$1
destination=$(echo $1 |sed 's/ /-/g')
path="/home/server/Download"
touch $path/archive/$destination.db
screen youtube-dl --download-archive $path/archive/$destination.db --all-subs --embed-subs -o "$path/$destination/%(title)s.%(ext)s" "https://www.youtube.com/playlist?list="$2
fi
read -n 1 -s
