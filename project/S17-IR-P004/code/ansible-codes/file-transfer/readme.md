instructions for readme files:

1. open the inventory file:

   a. replace the <username> with your preferred localhost username
   b. replace <spark-master-node-ip-address> with the ipaddress or the hostname of the target master node
   

2. We have created a 'inputfileandpythoncode.tar.gz' which contains the python code and the input file need to be transferred on the remote machine.
   So, open transfer file remotely
 
   a. replace the <absolute path> with the absolute path where the file inputfileandpythoncode.tar.gz.
 
 
3. run the tranferfile-benchmark.sh file. Make sure it has been changed to executable by typing the following command:
   a. chown 600 tranferfile-benchmark.sh
   b. ./600 tranferfile-benchmark.sh

4. The time elapsed in transfering the file is considered as bench mark for network connectivity.The output is found in 'bechmark_filtransfer_jetstream'
