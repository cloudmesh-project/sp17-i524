from pymongo import MongoClient
import requests
import time

import pandas as pd

client = MongoClient("mongodb://localhost:27017")

db = client.TestUSGS
vals = []

def doGetData():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minlatitude=-60.522&minlongitude=-166.992&maxlatitude=72.006&maxlongitude=-25.664&starttime=2015-01-01&endtime=2017-01-01&minmagnitude=4"
    resp = None

    try:
        r = requests.get(url)
        resp = r.json()
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        print ("Timed out")
        sys.exit(1)
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print ("Too many redirects")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print (e)
        sys.exit(1)

    db.usgsdata.drop()
    if resp is not None:
        db.usgsdata.insert_many(resp["features"])
        print ("Total " + str(db.usgsdata.count()) + " records downloaded." )

sess = requests.Session()
#### TME: Get start time
start_time = time.time()

doGetData()

#### TME: Elapsed time taken to download USGS data
elapsed = time.time() - start_time
line = "="*60
print (line)
print(str(elapsed) + " secs required to download " + str(db.usgsdata.count()) + " records from USGS.")
print (line)

client.close()

