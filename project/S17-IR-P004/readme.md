Using Hadoop and Spark for Big Data Analytics: Predicting Readmission of Diabetic patients:
Deployment of Spark on Chameleon, Jetstream and VirtualBox.


1. download the github repository by typing the following command:
	
        https://github.com/cloudmesh/diabetic.git 

2. Install Ansible(ignore if latest ansible is already installed)

        2.1. make sure ansible is installed using the command :
             <apt-get install ansible>


--------------------------Cloudmesh Set Up-------------------------------------


3. Open the inventory file:
         a. replace the <username> with your preferred localhost username

4. Run the ansible playbook using : 
   
         ansible-playbook -i inventory playbook-cloudmesh-first-time-install.yml -vvvv

5. Run the following command :
         $ cm 
       
   exit out by typing ctrl+c

6. Open the file ~/.cloudmesh/cloudmesh.yml and edit the following entry:

        6.1 Edit the following section,the entry with < > should be customized as per your credentials:

		 profile:
		      firstname: <first name>
		      lastname: <last name>
		      email: <email id>
		      user: <chameleon/jetsream/other cloud username>

        6.2. Change the entry of active cloud to use your preferred cloud,only( perform only for chameleon cloud):
 

        a. only for chameleon cloud:

		 active:
		 - chameleon
		 clouds:
		 ...

		                                       
	 		                                            
        b. only for jetstream cloud:

		 active:
		 - jetstream
		 clouds:
		 ...


        c. for both jetstream and chameleon cloud: 


	         active:
		 - chameleon
                 - jetstream
		 clouds:
		 ...



      6.3.Under the preferred cloud change the following entry, the entry with < > should be customized as per your credentials:

        a. for chameleon:

		 credentials:
		 OS_PASSWORD: <cloud password>
		 OS_TENANT_NAME: CH-818664
		 OS_TENANT_ID: CH-818664
		 OS_PROJECT_NAME: CH-818664
		 OS_USERNAME: <cloud username>
 
        b. for jetstream 
                
                credentials:
		OS_PROJECT_DOMAIN_NAME: tacc
		OS_USER_DOMAIN_NAME: tacc
		OS_PROJECT_NAME: TG-CIE170003
		OS_TENANT_NAME: TG-CIE170003
		OS_USERNAME: <cloud username>
		OS_PASSWORD: <cloud password>
		OS_AUTH_URL: https://jblb.jetstream-cloud.org:35357/v3
		OS_IDENTITY_API_VERSION: 3
		OS_VERSION: kilo




      6.4. (Step only for Chameleon cloud configuration for hadoop/spark deployment) Change the type of OS and flavor you want for hadoop/spark cluster(recommended) under your preferred cloud:

                default:
	            flavor: m1.medium
		     image: CC-Ubuntu14.04

      6.5 (Step only for Jetstream cloud configuration for hadoop/spark deployment) Change the type of OS and flavor you want for hadoop/spark cluster(recommended) under your preferred cloud:


              default:
	 	flavor: m1.medium
	 	image: ubuntu-14.04-trusty-server-cloudimg


7. Open the file 'playbook-cloudmesh-first-time-configure.yml'. We need to configure file as per our credentials. It will upgrade all the pre-requiste of cloudmesh-client:
  
         a. Change  <cloud provider name> to name of the preferred cloud

         b. Change the <cloud username> to preferred/active cloud username


------------------------- Cloudmesh Client upgrade(Optional) -----------------------------------

8. Skip this step. Open the file 'upgrade-cloudmesh'. We need to configure file as per our credentials. It will upgrade all the pre-requiste of cloudmesh-client:
  
         a. Change  <cloud provider name> to name of the preferred cloud

         b. Change the <cloud username> to preferred cloud username




------------------------Benchmarking: Spark Deployment -------------------------------------------



9. Go to 'hadoop-spark-deployment' deployment folder:

10. open the inventory file:

        a. replace the <username> with your preferred localhost username


11. We have created a 'inputfileandpythoncode.tar.gz' which contains the python code and the input file need to be transferred on the remote machine.
   So, open transfer file remotely
 
        a. replace the <absolute path> with the absolute path where the file inputfileandpythoncode.tar.gz.
 

12. open the deplyment-playbook.yml:

        a. change the --count <number-of-vms> to number of node you wants to be deployed for the spark cluster. Eg. --count 3

13. run the tranferfile-benchmark.sh file. Make sure it has been changed to executable by typing the following command:
   
        a. chown 600 deployment-benchmark.sh
        b. ./600 deployment-benchmark.sh

14. The benchmark for deployment is the time elapsed in deployment.The output is found in 'benchmark_deployment_jetstream'



----------------------------------Benchmarking:Spark Deployment ENDS------------------------------------




----------------------------Benchmarking:Transfer time of python script and input files------------------


15. Go to 'file-transfer' folder: 

16. open the inventory file:

         a. replace the <username> with your preferred localhost username
         b. replace <spark-master-node-ip-address> with the ipaddress or the hostname of the target master node
   

17. We have created a 'inputfileandpythoncode.tar.gz' which contains the python code and the input file need to be transferred on the remote machine.
   So, open transfer file remotely
 
         a. replace the <absolute path> with the absolute path where the file inputfileandpythoncode.tar.gz.
 
 
18. run the tranferfile-benchmark.sh file. Make sure it has been changed to executable by typing the following command:
   
         a. chown 600 tranferfile-benchmark.sh
         b. ./600 tranferfile-benchmark.sh

19. The time elapsed in transfering the file is considered as bench mark for network connectivity.The output is found in 'bechmark_filtransfer_jetstream'

---------------------------Benchmarking:Transfer time of python script and input files ENDS-----------



-----------------------------------Benchmarking: Runtime of ML algorithms------------------------------

20. Go to 'codes'-> 'ml-pyspark' directory:

        Each directory indicates the pyspark algorthm which we will be running and finding the run time and accuracy of the algorithm.

21. Go to 'input' folder to check out the input files we used for the project


22. After step 17 , we will be logging the cloud vm which would be acting as the SPARK/Hadoop master by 'hadoop' user to find file 'inputfileandpythoncode.tar.gz'. 

23. Untar it using the following command:
    tar -xvf inputfileandpythoncode.tar.gz

24. upload the data to hdfs by using the following command:

    hdfs dfs -put inputfiles/data136.csv /inputfiles/data136.csv

25. We will show example to run only 1 algorithm(naive bayes). The steps are same to run other algorithm:

         a. Go to 'naive-bayes' directory:
      
         b. Run the command, <localhost-ip> with your actual ip address:

        time spark-submit --master yarn --deploy-mode client --executor-memory 1g --name naive-bayes --conf "spark.app.id=naive-bayes"           naive-bayes.py hdfs://<localhost-ip>:8020/inputfiles/data136.csv > hdfs://<localhost-ip>/output-naive-bayes-out.txt

   Using the above command we will come to know the time taken by each algorithm to run.

26. The logs will be giving the following output as the very last step:

        real	1m55.845s
    
    The above signifies that it took 1 min 55.84 sec to run the algorithm using spark-submit.
  
28. Note down the real time for each algorithm. 

29. The output file generated by the running step 23. will contain the accuracy of the algorithm.


30. Repeat the steps from 23. to 27. for each of the algorithm and for each of the cloud that are  chameleon vs jetstream vs virtualbox regularly 
    
-----------------------------------Benchmarking: Runtime of ML algorithms ENDS------------------------------








