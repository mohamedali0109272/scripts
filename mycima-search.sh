#!/bin/bash


var=$1
var=$(echo $var | dmenu -l 10)

curl  -sL  https://mycima.onl/AjaxCenter/Searching/$var/ |\
  grep -Eoi '<a [^>]+>' |\
  cut -d\" -f2 |\
  dmenu -l 10
#curl -s https://mycima.onl/AjaxCenter/Searching/$1/ \
#	|sed "s/\" /\"\n/g"\
#	|grep -o 'href=..https:....mycima.*$' \
#	|sed 's/href=..//g' \
#	| sed "s/\\\//g" \
#	| sed "s/\\\"//g" \
#	| fzf \
#	| xargs -i python downloadurl.py "{}"
