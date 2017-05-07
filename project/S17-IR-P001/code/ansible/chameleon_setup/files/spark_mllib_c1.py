import string
import json

import shutil
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
import unicodedata

from pyspark import SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import NaiveBayes
from pyspark.sql import SQLContext
from pyspark.sql import Row
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import random
from operator import itemgetter

# Module-level global variables for the `tokenize` function below
PUNCTUATION = set(string.punctuation)
STOPWORDS = set(stopwords.words('english'))
STEMMER = PorterStemmer()

# Function to break text into "tokens", lowercase them, remove punctuation and stopwords, and stem them
def tokenize(text):
    tokens = word_tokenize(text)
    lowercased = [t.lower() for t in tokens]
    no_punctuation = []
    for word in lowercased:
        punct_removed = ''.join([letter for letter in word if not letter in PUNCTUATION])
        no_punctuation.append(punct_removed)
    no_stopwords = [w for w in no_punctuation if not w in STOPWORDS]
    stemmed = [STEMMER.stem(w) for w in no_stopwords]
    return [w for w in stemmed if w]


import os
os.environ["SPARK_HOME"] = "/home/sowmya/spark-2.1.0-bin-hadoop2.7"

def f(x):
    d = {}
    for i in range(len(x)):
        d[str(i)] = x[i]
    return d

# Initialize a SparkContext
sc = SparkContext()

# SQL Context
sqlc = SQLContext(sc)

# Import full dataset of newsgroup posts as text file
#data_raw = sc.textFile('/home/sowmya/Documents/tweets-1.txt')

users_df = sqlc.read.json('/home/sowmya/Documents/WorldTweets-1.txt')

# Parse JSON entries in dataset
#data = data_raw.map(lambda line: json.loads(json.dumps(line)))
#unicoded = data.map(lambda line: line.encode("utf-8"))


# Extract relevant fields in dataset -- category label and text content
data_pared = users_df.select('text')

data_pared_rdd = data_pared.rdd

#data_json_dump = data_pared_rdd.map(lambda line: json.loads(json.dumps(line)))

data_pared_text = data_pared_rdd.map(lambda row: (row['text']))

remove_none = data_pared_text.filter(lambda text: text is not None)

remove_nonascii = remove_none.map(lambda text: text.encode('ascii', 'ignore'))


# Prepare text for analysis using our tokenize function to clean it up
data_cleaned = remove_nonascii.map(lambda text: tokenize(text))


# Hashing term frequency vectorizer with 50k features
htf = HashingTF(50000)

# Create an RDD of LabeledPoints using category labels as labels and tokenized, hashed text as feature vectors
data_hashed = data_cleaned.map(lambda text: htf.transform(text))

# Split data 70/30 into training and test data sets
cnt = data_hashed.count()

# Add random labels to data
label = []
for i in range (cnt):    
    label.append(random.randrange(-1,1,1))  
label_rdd = sc.parallelize(label)


data_hashed.collect()
label_rdd.collect()

# Get number of Partitions
label_rdd.getNumPartitions()
data_hashed.getNumPartitions()

#Zip the two data sets
label_rdd_1 = label_rdd.zipWithIndex().map(lambda (a,b): (b,a))
data_hashed_1 =data_hashed.zipWithIndex().map(lambda (a,b): (b,a))
merged_hash = label_rdd_1.join(data_hashed_1)
print merged_hash.collect()

data_labelled = merged_hash.map(lambda (a,b): b)

#Labelled point data
data_fin = data_labelled.map(lambda (label,text): LabeledPoint(label,text))
train_hashed, test_hashed = data_fin.randomSplit([0.7, 0.3])

#print data_fin.collect()


# Ask Spark to persist the RDD so it won't have to be re-created later
data_fin.persist()


# Train a Naive Bayes model on the training data
model = NaiveBayes.train(train_hashed)

# Compare predicted labels to actual labels
prediction_and_labels = test_hashed.map(lambda point: (model.predict(point.features), point.label))

# Filter to only correct predictions
correct = prediction_and_labels.filter(lambda (predicted, actual): predicted == actual)

# Calculate and print accuracy rate
accuracy = correct.count() / float(test_hashed.count())

print prediction_and_labels.collect()

print "Classifier correctly predicted category " + str(accuracy * 100) + " percent of the time" 

prediction_and_labels.saveAsTextFile("/usr/local/spark/target/tmp1/test_result/output_1node")

# Save Model  output
output_dir = '/usr/local/spark/target/tmp1/test_result/output_1node/naiveBayes'
shutil.rmtree(output_dir, ignore_errors=True)
model.save(sc, output_dir)


