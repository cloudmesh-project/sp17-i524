cm cluster define --count $1 --image CC-Ubuntu14.04 --flavor m1.xlarge --secgroup my_group_1
>~/.ssh/known_hosts
stack_xyz=`cm hadoop avail|grep '> stack-'|cut -d ' ' -f 2`
echo $stack_xyz
find $HOME/.cloudmesh/stacks/$stack_xyz -name '*.done' -exec rm '{}' \;
cm hadoop sync
echo "Time taken for deploying cluster with $1 nodes:" >>benchmark.log
time_lapse=$((`time cm hadoop deploy`))
echo "$time_lapse" >>benchmark.log
