#!/bin/bash


echo "setting up environment, copying files installing dependencies ..."
ansible-playbook predict_setup.yaml
echo "setting up environment, copying files installing dependencies ... done"

echo "running predict application ..."
ansible-playbook predict_execute.yaml
echo "running predict application ... done"

echo "result output files are located in /tmp/predict_results"
