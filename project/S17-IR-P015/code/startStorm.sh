#!/bin/bash

readarray -t hosts < hosts.txt
ip=$(<ip)
start=$(date +%s.%N)

#start storm
if [ "$ip" == "${hosts[0]}" ] ; then
	st/bin/storm nimbus &
else
	st/bin/storm supervisor &
fi

dur=$(echo "$(date +%s.%N) - $start" | bc)
echo $dur > $HOME/stormTime.txt

exit 0
