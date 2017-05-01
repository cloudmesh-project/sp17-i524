import csv
import StringIO
import sys
from pyspark import SparkContext,SparkConf
from pyspark.sql import SQLContext, Row
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.evaluation import BinaryClassificationEvaluator

from pyspark.ml import Pipeline
from pyspark.ml.classification import RandomForestClassifier
from pyspark.sql.types import *

if __name__ == "__main__":

    # if len(sys.argv) != 3:
    #     print("Usage: wordcount <input> <output>")
    #     exit(-1)

    conf = SparkConf().setAppName("Churn Prediction")
    sc = SparkContext(conf=conf)
    sqlcontext = SQLContext(sc)
    input = sc.textFile(sys.argv[1])
    parts = input.map(lambda l: l.split(","))
    Customer = parts.map(
        lambda p: (p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13],
                   p[14], p[15], p[16], p[17], p[18], p[19], p[20]))

    print Customer.take(1)


    # Defining schema from the CSV file
    schemaString = "customerID,gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService," \
                   "MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection," \
                   "TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling," \
                   "PaymentMethod,MonthlyCharges,TotalCharges,Churn"

    fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split(',')]

    schema = StructType(fields)

    Customer_data = sqlcontext.createDataFrame(Customer, schema)
    Customer_data.registerTempTable("df")
    df_proper = sqlcontext.sql("SELECT NVL(cast(SeniorCitizen as int),0) as SeniorCitizen,\
                                NVL(cast(tenure as int),0) as tenure,\
                                NVL(cast(MonthlyCharges as int),0) as MonthlyCharges,\
                                 NVL(cast(TotalCharges as int),0) as TotalCharges, Churn from df")
    print df_proper.first()
    print df_proper.printSchema()

    labelIndexer = StringIndexer(inputCol='Churn', outputCol='label')

    assembler = VectorAssembler(inputCols=["SeniorCitizen","tenure","MonthlyCharges","TotalCharges"],
                                outputCol="features")

    featureIndexer = VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4)

    (train, test) = df_proper.randomSplit([0.7, 0.3])

    classifier = RandomForestClassifier(labelCol = 'label', featuresCol = 'features')

    pipeline = Pipeline(stages=[labelIndexer,assembler, classifier])

    model = pipeline.fit(train)

    predictions = model.transform(test)

    evaluator = BinaryClassificationEvaluator()

    auroc = evaluator.evaluate(predictions, {evaluator.metricName: "areaUnderROC"})
    test = int(auroc)
    print auroc

    f = open(sys.argv[2],'w')
    f.write("the area under curve for Random Forest Classifier is: " + str(auroc))
    f.close()


