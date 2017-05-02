import sys
import csv
import sip
#import org.apache.log4j.{Level, Logger}
import matplotlib
#matplotlib.user('agg')
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
from pyspark import SparkContext, SparkConf
from datetime import datetime
from operator import add, itemgetter
from collections import namedtuple
from datetime import datetime
import os
import time
from StringIO import StringIO



#Defining the fields, Creating a Flights class with the following fields as a tuple
#Each row is converted into a list

timestarted = time.time()

fields   = ('date', 'airline', 'flightnum', 'origin', 'dest', 'dep',
            'dep_delay', 'arv', 'arv_delay', 'airtime', 'distance')

Flight   = namedtuple('Flight', fields, verbose=True)

DATE_FMT = "%Y-%m-%d"

TIME_FMT = "%H%M"

# User Defined Functions

def toCSVLine(data):
  return ','.join(str(d) for d in data)


def split(line):
    reader = csv.reader(StringIO(line))
    return reader.next()

def parse(row):
    row[0]  = datetime.strptime(row[0], DATE_FMT).time()
    row[5]  = datetime.strptime(row[5], TIME_FMT).time()
    row[6]  = float(row[6])
    row[7]  = datetime.strptime(row[7], TIME_FMT).time()
    row[8]  = float(row[8])
    row[9]  = float(row[9])
    row[10] = float(row[10])
    return Flight(*row[:11])

def notHeader(row):
    return "Description" not in row


def plot(airlinesdelays):
    airlines = [d[0] for d in airlinesdelays]
    minutes  = [d[1] for d in airlinesdelays]
    index    = list(xrange(len(airlines)))
#Above we retrieved the respective columns from the list

#Here we mention the plot as a horizontal bar plot
    fig, axe = plt.subplots()
    bars = axe.barh(index, minutes)

    # Add the total minutes to the right
    for idx, air, min in zip(index, airlines, minutes):
        if min > 0:
            bars[idx].set_color('#d9230f')
            axe.annotate(" %0.0f min" % min, xy=(min+1, idx+0.5), va='center')
        else:
            bars[idx].set_color('#469408')
            axe.annotate(" %0.0f min" % min, xy=(10, idx+0.5), va='center')

    # Set the ticks
    ticks = plt.yticks([idx+ 0.5 for idx in index], airlines)
    xt = plt.xticks()[0]
    plt.xticks(xt, [' '] * len(xt))

    # minimize chart junk
    plt.grid(axis = 'x', color ='white', linestyle='-')

    plt.title('Total Minutes Delayed per Airline')
    plt.savefig('airlines.png')


#airlines.filter(notHeader).take(10)

#main method is the entry point for the following program

if __name__ == "__main__":

  conf = SparkConf().setAppName("average")
  sc = SparkContext(conf=conf)

  #setting log level to error
 # val rootLogger = Logger.getRootLogger()
 # rootLogger.setLevel(Level.ERROR)

  #importing data from HDFS for performing analysis
  airlines = sc.textFile(sys.argv[1])
 # airlines = sc.textFile("hdfs://192.168.1.8:8020/fltdata/airlines.csv")
  flights = sc.textFile(sys.argv[2])
  airports =sc.textFile(sys.argv[3])

  
  airlinesParsed = dict(airlines.map(split).collect())
  airportsParsed= airports.filter(notHeader).map(split)
 # print "without header and spliting up", airlines.take(10)  
  # print "without header and spliting up", airlines.take(10)
  flightsParsed= flights.map(lambda x: x.split(',')).map(parse)
  #print "The average delay is "+str(sumCount[0]/float(sumCount[1]))
  airportDelays = flightsParsed.map(lambda x: (x.origin,x.dep_delay))
  # First find the total delay per airport
  airportTotalDelay=airportDelays.reduceByKey(lambda x,y:x+y)

  # Find the count per airport
  airportCount=airportDelays.mapValues(lambda x:1).reduceByKey(lambda x,y:x+y)

  # Join to have the sum, count in 1 RDD
  airportSumCount=airportTotalDelay.join(airportCount)
  # Compute avg delay per airport
  airportAvgDelay=airportSumCount.mapValues(lambda x : x[0]/float(x[1]))
  airportDelay = airportAvgDelay.sortBy(lambda x:-x[1])
  print "", airportDelay.take(10)
  airportLookup=airportsParsed.collectAsMap()  

  #airlineLookup=airlinesParsed.collectAsMap()
  airline_lookup = sc.broadcast(airlinesParsed)
  airlinesdelays  = flightsParsed.map(lambda f: (airline_lookup.value[f.airline],add(f.dep_delay, f.arv_delay)))
  airlinesdelays  = delays.reduceByKey(add).collect()
  airlinesdelays  = sorted(delays, key=itemgetter(1))
  #tenairlines = delays.map(toCSVLine)
  ten = airportAvgDelay.map(lambda x: (airportLookup[x[0]],x[1]))
  #print "", ten.take(10)
 
 for d in airlinesdelays:
      print "%0.0f minutes delayed\t%s" % (d[1], d[0])
  airportBC=sc.broadcast(airportLookup)
  topTenAirportsWithDelays = airportAvgDelay.map(lambda x: (airportBC.value[x[0]],x[1])).sortBy(lambda x:-x[1])
  lines = topTenAirportsWithDelays.take(10)
  
  topten = "/home/hadoop/"
  tenairlines = "/home/hadoop/"
 
  #For collecting the outputs into csv files  
  with open('topten', "w") as output:
      writer = csv.writer(output, lineterminator='\n')
      for val in lines:
          writer.writerows([val])
  with open('tenairlines',"w") as output:
      writer = csv.writer(output, lineterminator='\n')
      for val in delays:
          writer.writerows([val])

  plot(airlinesdelays)
  

  #Final time taken will be calculated here
  timetaken  = time.time()-timestarted
  print "", timetaken



