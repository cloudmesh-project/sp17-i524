#!/bin/bash


touch bechmark_filtransfer_jetstream
starttime=$(date +%s)
ansible-playbook tranfer-files-remotely.yml --ask-sudo-pass -vvvv
endtime=$(date +%s)
totaltime=$((endtime-starttime))
echo $totaltime

echo "transfer takes $(($totaltime / 60)) minutes and $(($totaltime % 60)) seconds elapsed in chameleon cloud" > bechmark_filtransfer_jetstream
