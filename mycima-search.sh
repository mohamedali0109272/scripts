#!/bin/bash


curl -s https://mycima.life/AjaxCenter/Searching/$1/ |sed "s/\" /\"\n/g"|grep -o 'href=..https:....mycima.*$' |sed 's/href=..//g' | sed "s/\\\//g" | sed "s/\\\"//g" | dmenu -c -l 10  -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=10  -p "search" | xargs -i python downloadurl.py "{}"
