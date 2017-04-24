#!/bin/bash

#Parse input (if exists) otherwise default to 1 virtual machine  
if [ "$#" -eq 0 ]; then
    num_nodes=1
else 
    num_nodes=$1
fi

timing_info=""

#loop through from 1 to num_nodes 
#time each task
for i in `seq 1 $num_nodes`;
do
    START_iter=$(date +%s)
    echo ***Benchmarking with num_nodes=$i***
    START=$(date +%s)
    make deploy num_nodes=$i
    END=$(date +%s)
    DIFF=$(( $END - $START ))
    timing_info=$timing_info"Time (seconds) \"make deploy num_nodes=$i\": $DIFF\n"
    START=$(date +%s)
    make install
    END=$(date +%s)
    DIFF=$(( $END - $START ))
    timing_info=$timing_info"Time (seconds) \"make install num_nodes=$i\": $DIFF\n"
    START=$(date +%s)
    make run
    END=$(date +%s)
    DIFF=$(( $END - $START ))
    timing_info=$timing_info"Time (seconds) \"make run num_nodes=$i\": $DIFF\n"
    START=$(date +%s)
    make view
    END=$(date +%s)
    DIFF=$(( $END - $START ))
    timing_info=$timing_info"Time (seconds) \"make view num_nodes=$i\": $DIFF\n"
    START=$(date +%s)
    make delete
    END=$(date +%s)
    DIFF=$(( $END - $START ))
    timing_info=$timing_info"Time (seconds) \"make delete num_nodes=$i\": $DIFF\n"
    DIFF=$(( $END - $START_iter ))
    timing_info=$timing_info"Time (seconds) \"Full Benchmark num_nodes=$i\": $DIFF\n"
done

#print timing results to the screen
echo -e $timing_info
