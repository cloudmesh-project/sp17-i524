# Each of these commands must be run individually in an Ubuntu shell in the location where these yml files are present along with the hosts file

time ansible-playbook copy_data.yml --ask-sudo-pass
time ansible-playbook move_data_to_hdfs.yml --ask-sudo-pass
time ansible-playbook run_pig_script.yml --ask-sudo-pass
time ansible-playbook move_output_to_cloud.yml --ask-sudo-pass
time ansible-playbook move_output_to_local.yml --ask-sudo-pass
