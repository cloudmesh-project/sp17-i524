#!/usr/bin/env python

import sys
import logging
import iu.i524.S17IRP013.hadoop.hbase_to_hdfs as h2h


DEFAULT_STATION_ID = 'DST:IND000DEF'

logging.basicConfig(format = '%(asctime)s %(message)s',\
                    datefmt = '%m/%d/%Y %I:%M:%S %p',\
                    filename = 'wda_app.log',\
                    level=logging.DEBUG)
    
        
def get_default_result():
    result = dict()
    result['TMAX'] = [DEFAULT_STATION_ID,0]
    result['PRCP'] = [DEFAULT_STATION_ID,0]
    result['TAVG'] = [DEFAULT_STATION_ID,0]
    result['TMIN'] = [DEFAULT_STATION_ID,100]
    return result

def compare_props(prop,result):
    logging.info(prop)
    if prop['parameter'] == 'TMAX':
        if float(prop['value']) >  float(result['TMAX'][1]) or result['TMAX'][1] == 0:
            result['TMAX'][0] = prop['station_id']
            result['TMAX'][1] = prop['value']
    elif prop['parameter'] == 'TAVG':
        if float(prop['value']) >  float(result['TAVG'][1]) or result['TAVG'][1] == 0:
            result['TAVG'][0] = prop['station_id']
            result['TAVG'][1] = prop['value']
    elif prop['parameter'] == 'PRCP':
        if float(prop['value']) >  float(result['PRCP'][1]) or result['PRCP'][1] == 0:
            result['PRCP'][0] = prop['station_id']
            result['PRCP'][1] = prop['value']
    elif prop['parameter'] == 'TMIN':
        if float(prop['value']) <  float(result['TMIN'][1]) or result['TMIN'][1] == 0:
            result['TMIN'][0] = prop['station_id']
            result['TMIN'][1] = prop['value']
    return result
# input comes from STDIN (standard input)
index = 0
for year_month in sys.stdin:    
    year_month = year_month.strip()   
    data_list = h2h.find_by_id(row_key=year_month)
    tmax = 70
    tmin=-70
    tavg=0
    prcp=0
    result = get_default_result()
    ## Run analysis
    for prop in data_list:
        result = compare_props(prop=prop,result=result)    
    #print  '%s\t%s' % (index, str(result))
    print  str(result)  
   
    