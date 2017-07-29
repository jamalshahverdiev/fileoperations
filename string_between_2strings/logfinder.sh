#!/usr/local/bin/bash

file="`pwd`/logfile_20160324100401.log"

erstr="ERROR Database error"
lastline="`cat -n $file | grep "$erstr" | awk '{ print $1 }'`"
errlinenum=$(cat -n `pwd`/logfile_20160324100401.log | awk '/===========================================================================/ || /ERROR Database error/{print}' | nl | grep error | awk '{ print $1 }')
fdline=`expr $errlinenum - 1`

fline=$(cat -n logfile_20160324100401.log | awk '/===========================================================================/ || /ERROR Database error/{print}' | nl | grep -w "$fdline" | awk '{ print $2 }')
plus2=`expr $fline + 2`

cat -n $file | grep -w "$plus2" | awk '{ print $7 }'
#sed -n ''"$fline"','"$lastline"'p' $file
