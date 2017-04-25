
"""
Decision Tree Classification Example.
"""
from __future__ import print_function

from pyspark import SparkContext
# $example on$
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint



def parseLine(line):
    parts = line.split(',')
    #print(len(parts))
    label = float(parts[-1])
    features = Vectors.dense([float(parts[x]) for x in range(0,len(parts)-1)])
    return LabeledPoint(label, features)

if __name__ == "__main__":

    sc = SparkContext(appName="PythonDecisionTreeClassificationExample")

    data = sc.textFile('data136.csv').map(parseLine)
   
    # Split the data into training and test sets (30% held out for testing)
    (trainingData, testData) = data.randomSplit([0.7, 0.3])

    # Train a DecisionTree model.
    #  Empty categoricalFeaturesInfo indicates all features are continuous.
    model = DecisionTree.trainClassifier(trainingData, numClasses=2, categoricalFeaturesInfo={},
                                         impurity='gini', maxDepth=5, maxBins=32)

    # Evaluate model on test instances and compute test error
    predictions = model.predict(testData.map(lambda x: x.features))
    labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
    testErr = labelsAndPredictions.filter(lambda (v, p): v != p).count() / float(testData.count())
    print('Test Error = ' + str(testErr))
    print('Learned classification tree model:')
    print(model.toDebugString())

    # Save and load model
    #model.save(sc, "target/tmp/myDecisionTreeClassificationModel")
    #sameModel = DecisionTreeModel.load(sc, "target/tmp/myDecisionTreeClassificationModel")
# $example off$
