#!/bin/bash

#cat $1 | grep -A1 -i  " 1 events processed so far"
#cat $1 | grep -A1 -i  " 99 events processed so far"
#cat $1 | grep -A1 -i  " 100 events processed so far"
#cat $1 | grep -A1 -i  " 101 events processed so far"
cat $1 | grep -B2 -i  "records written"
cat $1 | grep  -i "cObjR_ALL"
cat $1 | grep -i "ChronoStatSvc "
#cat $1 | grep -A15 -i " memory inf"
cat $1 | grep  -i "vmpeak"
cat $1 | grep  -i "setoption"

[ -z "$2" ] && exit
MEM_1ST=`cat $2 | grep -i buffers/cache | cut -d" " -f9 | head -n1`
MEM_MAX=`cat $2 | grep -i buffers/cache | cut -d" " -f9 | sort -u | tail -n1`
MEM=$((MEM_MAX - $MEM_1ST))
echo "RSS profile with free -m -s 1: $MEM"
