#!/bin/bash
#author:jiwenkangatech@foxmail.com
#function:$1 can help to forward ssh port.

lsPort(){
    ss -antlp | grep ':22222' 1>/dev/null 2>&1
    if [ ! $? -eq 0 ];then
        lsPort="No"
    fi
}
start(){
    if [ $lsPort=="No" ];then
        /srv/shell/sshForward.sh.x
        echo "Opening"
    else
        echo "Defeated"
    fi
}
main(){
lsPort && start
echo "$0 end."
}

