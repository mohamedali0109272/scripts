#!/usr/bin/bash

while true; do
	rx1=$(cat /sys/class/net/wlan0/statistics/rx_bytes)
	sleep 1
	rx2=$(cat /sys/class/net/wlan0/statistics/rx_bytes)
	ico=$(python -c "print(($rx2 - $rx1) // 1024)")
	if [[ $ico -ge "1024" ]]; then
		ico=$(python -c "print($ico // 1024)")
		echo  $ico m
	else
		echo   $ico k
	fi
done
