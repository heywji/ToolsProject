#!/bin/bash
if [ ! -x "/tmp/floder" ];then
    mkdir /tmp/floder
fi
mv $1 "/tmp/floder/$1"
