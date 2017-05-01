#!/bin/bash


touch ../benchmarking/benchmark
echo 'Benchmark' >> ../benchmarking/benchmark


echo "***Configuring Environment, Copying files and installing dependencies ***"
start=$(date +%s)
ansible-playbook predict_setup.yaml
end=$(date +%s)
time_setup=$((end-start))

echo time_setup $time_setup >> ../benchmarking/benchmark
echo "***Configuring Environment, Copying files and installing dependencies - done***"

echo "***Running predict application***"
start=$(date +%s)

ansible-playbook predict_execute.yaml

end=$(date +%s)
time_spark_job=$((end-start))
echo time_spark_job $time_spark_job >> ../benchmarking/benchmark
echo "***Running predict application - done***"

echo "***Running data analysis application***"
start=$(date +%s)
ansible-playbook analysis_execute.yaml
end=$(date +%s)
time_spark_job2=$((end-start))
echo time_spark_job2 $time_spark_job2 >> ../benchmarking/benchmark
echo "***Running data analysis  application - done***"


echo "Ouput files, model accuracy and plots are stored at local: /tmp"
