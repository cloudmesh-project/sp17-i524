README
========
 
This Apache Pig project analyses airline data across the US to find the most frequently delayed airports.

Pre Requisites
================
This project was run in an Ubuntu machine with the following softwares available:
- Git
- Cloudmesh Client (with cloudmesh.yaml file configured to access chamelen cloud)
- Ansible

Deployment
==========
The virtual machines are set up using cloudmesh client with its "cm" commands. The code for this process is present in https://github.com/cloudmesh/sp17-i524/blob/master/project/S17-IR-P002/code/cloudmesh_client/cloudmesh_script.sh with inline instructions on how to run it.

Airline Analysis
================
The analysis  was done using Apache Pig setup on Apache Hadoop with a three node cluster. The Pig Latin script for the analysis is present in the reporsitory under https://github.com/cloudmesh/sp17-i524/tree/master/project/S17-IR-P002/code/pig. The file pig_script provides the actual script that takes inputs from hdfs location and outputs to a hdfs location. The script pig_del_inputs_and_outputs gives the code to rerun the pig script for benchmarking purposes, it deletes the existing results for the actual script to run smoothly.

Ansible Automation
================
The entire process of running the Pig Script, moving input data to the cloud and hdfs location and output data back to the local for viewing has been automated using Ansible. These scripts are broken down into five different playbooks for benchmarking purposes in the reporitory https://github.com/cloudmesh/sp17-i524/tree/master/project/S17-IR-P002/code/ansible. The hosts file in this repository has the ip address of name node where the pig script has to be run.

Executing the Project
================
The code to run Ansible scripts to execute the project are present in https://github.com/cloudmesh/sp17-i524/blob/master/project/S17-IR-P002/code/shell_scripts/airline_analysis.sh. Each of these steps are timed using "time" command in Ubuntu shell. 

Changes to be made
================
In order for users to run this project without any interruptions, the following changes need to be made to the codes:
1. If required, the flavour and operating system of the clouds can be changed in the cloudmesh_script.sh. This OS as to be compatible with cloudmesh client
2. ip address of namenode needs to be provided in pig script in order for the script to pick up the right input
3. Hosts file needs to be changed in ansible and the ip address of name node and port needs to be provided in the ansible scripts move_data_to_hdfs.yml and move_output_to_cloud.yml in the ansible folder, in order for the ansible scripts to move the data to right location
4. Other minor changes in locations might need to be done depending on the location of the input data files and folder structure on the users' local system.

The entire process is automated and just by running the "airline_analysis.sh" code and making the right configurations, the project will be executed and benchmarked.

