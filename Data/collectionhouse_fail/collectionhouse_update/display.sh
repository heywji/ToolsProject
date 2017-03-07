#!/bin/bash
#author:jiwenkangatech##foxmail.com.

# run python3 testmp.py
while [ "1" -eq "1" ];
    do
        python3 testmp.py &
        sleep 15s
        skill -KILL \
        $(ps -ef | grep "python3 testmp.py" | awk '{print $2}')
        printf "this was stop\n"
        sleep 2s
    done
