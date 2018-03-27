#!/bin/bash
# function:detect host

# declare $i
declare host_file="/srv/file/faigo_hosts.txt"
declare host_list="/srv/file/faigo_lists.txt"

prepare(){
  touch /tmp/detect.txt
  cat /dev/null > /tmp/detect.txt
}

final(){
  printf -- "\n\n"
  cat /tmp/detect.txt
}

detect_nslookup(){
  nslookup "$i" 223.5.5.5 | awk -F 'Address:' '{ print $2 }' | tail -n2 | head -n1 | cut -c 2- 
}

detect_tcping(){
  tcping $(detect_nslookup) 5366 &>/tmp/detect_tcping.txt
  grep --color=auto -E "(closed|failure)" /tmp/detect_tcping.txt && return 1 || return 0
}

core(){
  for i in $(cat $host_file);do
    number="$(echo $i | cut -d. -f1)"
    grep $number $host_list
    tcping $(detect_nslookup) 5366 2>/dev/null
      if [ "$?" -ne "0" ];then
        echo "DNS current search result failure but background CONTINUE."
      fi
    detect_tcping
      if [ "$?" -ne "0" ];then
        echo "$i" | tee >> /tmp/detect.txt
      fi
  done
}

prepare
core
final
