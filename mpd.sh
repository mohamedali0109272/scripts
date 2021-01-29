#!/bin/bash

#mpd=$(echo -e "\n\n" |dmenu -c -l 1 -g 3 -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=17  -p "$(mpc |head -1)")

while true; do
	m=$(mpc |head -1 |cut -c1-30)
	mpd=$(echo -e "\n\n\n\n\nX" |dmenu -c -g 3 -l 2 -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=17  )
	if [[ $mpd == "" ]]; then
		mpc toggle &
	elif [[ $mpd == "" ]]; then
		mpc prev &
	elif [[ $mpd == "" ]]; then
		mpc next &
	elif [[ $mpd == "X" ]]; then
		break	
	fi
done
