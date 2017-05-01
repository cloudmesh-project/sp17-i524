echo Benchmark 1
echo "PySpark Dependencies Installation" 
start=`date +%s`
 ansible-playbook -i inventory.txt -c ssh test1.yml
end=`date +%s`
time_for_local_setup=$((end-start))
echo $time_for_local_setup

