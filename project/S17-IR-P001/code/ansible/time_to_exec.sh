echo Benchmark 2
echo "Python package and nodejs installation" 
start=`date +%s`
  ansible-playbook -i inventory.txt -c ssh test.yml
end=`date +%s`
time_for_cloud_setup=$((end-start))
echo $time_for_cloud_setup

