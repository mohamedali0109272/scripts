#!/bin/bash

while true; do
	status_ping=0

        packets="$(ping -q -w2 -c2 1.1.1.1 | grep -o "100% packet loss")"
        packets="$(ping -q -w2 -c2 1.1.1.1 | grep -o "100% packet loss")"
        packets="$(ping -q -w2 -c2 1.1.1.1 | grep -o "100% packet loss")"
        packets="$(ping -q -w2 -c2 1.1.1.1 | grep -o "100% packet loss")"
        packets="$(ping -q -w2 -c2 1.1.1.1 | grep -o "100% packet loss")"
        if [ ! -z "${packets}" ];
        then
                status_ping=0
        else
                status_ping=1
        fi

        if [ $status_ping -eq 0 ];
        then
                espeak 'no fucking internet'
        fi
done
