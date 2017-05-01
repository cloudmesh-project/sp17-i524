#!/bin/bash
spark_master=`hostname -i`

/opt/spark/bin/spark-submit --master yarn --deploy-mode client --executor-memory 1g \
--conf "spark.app.id=churn_prediction" /opt/predict/code/customer_churn_prediction.py \
hdfs://${spark_master}:8020/predict/Customer_Data.csv \
/opt/predict/data/output.txt  
