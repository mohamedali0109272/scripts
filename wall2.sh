#!/bin/bash

while true; do
    choice=$(echo -e "exec\nfile\ncalc\nshutdown" |dmenu -c -l 15 -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=17 -p "dmenu")
    if [[ $choice == "calc" ]];then
        echo "this is calc" | dmenu -c -l 15 -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=17 |xargs -i python -c "print({})"  | dmenu -c -l 15 -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=17 -p "results"
    elif [[ $choice == "exec" ]];then
        ls /bin/ | dmenu -c -l 15 -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=17 |xargs sh -c 
    elif [[ $choice == "" ]]; then
      break
    elif [[ $choice == "shutdown" ]]; then
      shutdown now
    elif [[ $choice == "shutdown" ]]; then
      shutdown now
    elif [[ $choice == "file" ]];then
        while true; do
            file=$(ls -a |dmenu -c -l 15 -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=17 -p "file"| xargs file |awk -F: '{ print $1 }')
            dir=$(echo $file | xargs file |grep "directory" | awk '{ print $2 }')
            ext=$(echo $file |awk -F. '{print $NF}')
            if [[ $dir == "directory" ]];then
              cd $file
            elif [[ $file == "" ]]; then
              break
            elif [[ $ext == "txt" ]] || [[ $ext == "srt" ]]; then
              vim $file
            elif [[ $ext == "mkv" ]] || [[ $ext == "mp4" ]]; then
              mpv $file
            else
                op=$(echo -e "vim\nfeh\nmpv" |dmenu -c -l 15 -m dmenumon -nb "#000000" -sb "#AC0021" -fn FontAwesome:size=17 -p "open with" ) 
                if [[ $op == "vim" ]]; then
                    st vim $file
                else
                    sh -c "$op $file"
                fi 
            fi
        done
    else
        echo "this file ( $file ) is unknown"
    fi
done
 