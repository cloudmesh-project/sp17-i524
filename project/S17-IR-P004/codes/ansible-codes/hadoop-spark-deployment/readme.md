instructions for readme files:

1. open the inventory file:

   a. replace the <username> with your preferred localhost username
   

2. We have created a 'inputfileandpythoncode.tar.gz' which contains the python code and the input file need to be transferred on the remote machine.
   So, open transfer file remotely
 
   a. replace the <absolute path> with the absolute path where the file inputfileandpythoncode.tar.gz.
 

3. open the deplyment-playbook.yml:
   a. change the --count <number-of-vms> to number of node you wants to be deployed for the spark cluster. Eg. --count 3

4. run the tranferfile-benchmark.sh file. Make sure it has been changed to executable by typing the following command:
   a. chown 600 deployment-benchmark.sh
   b. ./600 deployment-benchmark.sh

5. The bench mark for deployment is the time elapsed in deployment.The output is found in 'benchmark_deployment_jetstream'
