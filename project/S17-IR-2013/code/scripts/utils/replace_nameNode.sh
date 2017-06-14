floating_ip=`cm cluster nodes |cut -d " " -f 2|head -1`
vm_name=`cm cluster nodes |cut -d " " -f 1|head -1`
echo $physical_ip
echo $floating_ip
physical_ip=`cm vm list|grep $vm_name |cut -d "|" -f 6|tr -d [:blank:]`
`sed -i "s/<Name Node Ip Address>/$floating_ip/g" hosts`
#`sed -i "s/<Name Node Ip Address>/$floating_ip/g" hosts`
`sed -i "s/<IP>:<port>/$physical_ip:8020/g" outbrain_pig`
`cat hosts`
