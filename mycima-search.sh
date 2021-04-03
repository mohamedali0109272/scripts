#!/bin/bash


curl -s https://mycima.onl/AjaxCenter/Searching/$1/ \
	|sed "s/\" /\"\n/g"\
	|grep -o 'href=..https:....mycima.*$' \
	|sed 's/href=..//g' \
	| sed "s/\\\//g" \
	| sed "s/\\\"//g" \
	| fzf \
	| xargs -i python downloadurl.py "{}"
