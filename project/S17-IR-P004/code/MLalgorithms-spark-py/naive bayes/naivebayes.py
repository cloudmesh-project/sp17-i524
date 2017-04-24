from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext

def parseLine(line):
    parts = line.split(',')
    #print(len(parts))
    label = float(parts[-1])
    features = Vectors.dense([float(parts[x]) for x in range(0,len(parts)-1)])
    return LabeledPoint(label, features)

sc = SparkContext(appName="naivebayes2")
data = sc.textFile('data136.csv').map(parseLine)

# Split data aproximately into training (60%) and test (40%)
training, test = data.randomSplit([0.8, 0.2], seed=0)

# Train a naive Bayes model.
model = NaiveBayes.train(training, 1.0)

# Make prediction and test accuracy.
predictionAndLabel = test.map(lambda p: (model.predict(p.features), p.label))

accuracy = 1.0 * predictionAndLabel.filter(lambda (x, v): x == v).count() / test.count()
print(accuracy)
# Save and load model
#model.save(sc, "target/tmp/myNaiveBayesModel")
#sameModel = NaiveBayesModel.load(sc, "target/tmp/myNaiveBayesModel")
