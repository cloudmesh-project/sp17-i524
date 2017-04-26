
from __future__ import print_function

import sys

import numpy as np
from numpy import array
from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans


def parseVectorAndDropLastColumn(line):
    arr=[]
    for x in range(len(line.split(','))-1):
        arr.append(float(line.split(',')[x]))
    return np.array(arr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: kmeans <file> <k>", file=sys.stderr)
        exit(-1)
    sc = SparkContext(appName="KMeans")
    lines = sc.textFile('../data136.csv')
    data = lines.map(parseVectorAndDropLastColumn)
    k = int(2)
    model = KMeans.train(data, k)
    with open('../data136.csv') as file:
       rows=file.readlines();

    rowOfDataPoints=[]
    arrayOfPredictedValues=[]
    arrayOfActualValues=[]
    for row in rows:
       row=row.rstrip("\n")

       #array of each row of output file
       rowsInOutputFile=[]

       #adding the feature vectors
       for x in range(len(row.split(','))-1):
          rowsInOutputFile.append(float(row.split(',')[x]))

       #predicted class value for each input datapoint
       predictedclassValue= float(model.predict(array(rowsInOutputFile)))

       #adding predicted class value in the outputfile
       rowsInOutputFile.append(predictedclassValue)

       # adding real class value in the outputfile
       rowsInOutputFile.append(float(row.split(',')[-1]))

       #Inserting the predicted ClassValue
       arrayOfPredictedValues.append(predictedclassValue)

       #Inserting the Actual class Value
       arrayOfActualValues.append(float(row.split(',')[-1]))

       #arrayOfActual class Value
       rowOfDataPoints.append(rowsInOutputFile)

    a = np.asarray(rowOfDataPoints)
    np.savetxt("output.csv", a, delimiter=",",fmt="%1.3f")


    print(arrayOfPredictedValues)
    print(arrayOfActualValues)


    PV=np.array(arrayOfPredictedValues)
    AV=np.array(arrayOfActualValues)

    cl1=np.array(AV[PV==0.0])
    cl2=np.array(AV[PV==1.0])

    percent1= float(sum(cl1)/len(cl1))

    if percent1 <0.5:
    	predictions = np.array(PV == AV)
        truematches =predictions[predictions]
        accuracy= float((len(truematches) * 100)/len(AV))
        print('accuracy: ',str(accuracy))
    else:

        predictions = np.array(PV != AV)
        truematches =predictions[predictions]
        accuracy= float((len(truematches) * 100)/len(AV))
 	print('accuracy: ',str(accuracy))




    #accuracyincluster0=numberOfCorrectMappingincluster0/totalnumberofitemsincluster0;
    #accuracyincluster1=numberOfCorrectMappingincluster1/totalnumberofitemsincluster1;
    ##print(accuracyincluster0)
    #print(accuracyincluster1)

    '''
    print("-----")
    print(model.predict(array([1,1,7,2,19,0,19,0,0,0,348,276,403,9,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,1,0])))
    print("-----")
    '''
    #print("Final centers: " + str(model.clusterCenters))

    #print("1st cluster center"+str(model.clusterCenters[0]))
    #print("2nd cluster center"+str(model.clusterCenters[1]))

    #print("Total Cost: " + str(model.computeCost(data)))
sc.stop()
