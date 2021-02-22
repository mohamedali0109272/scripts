#!/usr/bin/bash

while true; do
	rx1=$(cat /sys/class/net/*/statistics/rx_bytes)
	sleep 1
	rx2=$(cat /sys/class/net/*/statistics/rx_bytes)
	ico=$(expr $( expr $(echo $rx2 | sed "s/ / + /g") - $(echo $rx1 | sed "s/ / + /g")) / 1024)
	if [[ $ico -ge "1024" ]]; then
		ico=$(expr $ico / 1024 )
		echo  $ico m
	else
		echo   $ico k
	fi
done
