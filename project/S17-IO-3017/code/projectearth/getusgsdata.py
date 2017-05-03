import sys
import requests
import time
import dblayer
import testfile

def doGetData():
    sess = requests.Session()
    dbobj = dblayer.classDBLayer()
    #### TME: Get start time
    start_time = time.time()

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minlatitude=-60.522&minlongitude=-166.992&maxlatitude=72.006&maxlongitude=-25.664&starttime=2015-01-01&endtime=2017-01-01&minmagnitude=4"
    resp = None
    resp_text=""
    try:
        r = requests.get(url)
        resp = r.json()
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        resp_text = "Timed out"
        sys.exit(1)
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        resp_text = "Too many redirects"
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        resp_text = str(e)

        sys.exit(1)

    dbobj.dropdb()

    if resp is not None:
        dbobj.insertdata(resp["features"])
        resp_text = "Total " + str(dbobj.count()) + " records downloaded."

    fileobj=testfile.classFileWrite()
    #### TME: Elapsed time taken to download USGS data
    elapsed = time.time() - start_time

    fileobj.writeline()
    str1 = str(elapsed) + " secs required to download " + str(dbobj.count()) + " records from USGS."
    fileobj.writelog(str1)
    fileobj.writeline()
    fileobj.closefile()

    dbobj.closedb()
    sess.close()
    return resp_text

