#!/bin/bash

#mpd=$(echo -e "\n\n" |dmenu -c -l 1 -g 3 -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=17  -p "$(mpc |head -1)")

while true; do
	w=$(nmcli  radio wifi)
	if [[ $w == "enabled" ]]; then
		wi=$(echo -e "wifi \n$(nmcli device wifi |grep -v SSID|sed "s/..:..:..:..:..:..//g" | sed "s/Infra.*//g" |grep -v "\-\-")" |dmenu -c -l 7 -g 1 -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=17)
		if [[ $wi == "wifi " ]]; then
			nmcli  radio wifi off
		fi
	elif [[ $w == "disabled" ]]; then
		wi=$(echo -e "wifi " |dmenu -c -l 1 -g 3 -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=17)
		if [[ $wi == "wifi " ]]; then
			nmcli  radio wifi on
		fi
	fi
done
