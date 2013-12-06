#!/bin/bash
#
# cat plain | trans.sh > key_and_cipher

letters="abcdefghijklmnopqrstuvwxyz"
newltrs=""

for i in `seq 25 -1 0 | shuf`; do
    newltrs=${newltrs}${letters:$i:1}
done
for i in `seq 0 25`; do
    if [ ${newltrs:$i:1} = ${letters:$i:1} ]; then
        echo "whoops!" 1>&2
    fi
done


echo -e "$letters\n$newltrs"
echo ""

tr A-Za-z ${newltrs^^}${newltrs} <&0


    
