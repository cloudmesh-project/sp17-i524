#!/bin/bash
for i in `seq 1 10`;
do
num=$(($i*10000))
echo "$num iteration"
start_time=$((`date +%s%3N`))
(pig -4 /home/hadoop/log4j.properties -p num=$num /home/hadoop/outbrain_pig) 2>>benchmark_outbrain.log
end_time=$((`date +%s%3N`))
time_con=$(($end_time - $start_time))
echo $time_con
time_lapse[$(($i-1))]="$time_con"
done
echo ${time_lapse[*]}

