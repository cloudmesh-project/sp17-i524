#!/usr/bin/env python

import sys
import logging
import ast

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

def compare_results(result,final_result):
    if float(result['TMAX'][1]) > float(final_result['TMAX'][1]):
        final_result['TMAX'] = (result['TMAX'][0], result['TMAX'][1])
    if float(result['PRCP'][1]) > float(final_result['PRCP'][1]):
        final_result['PRCP'] = (result['PRCP'][0], result['PRCP'][1])
    if float(result['TAVG'][1]) > float(final_result['TAVG'][1]):
        final_result['TAVG'] = (result['TAVG'][0], result['TAVG'][1])
    if float(result['TMIN'][1]) < float(final_result['TMIN'][1]):
        final_result['TMIN'] = (result['TMIN'][0], result['TMIN'][1])
    return final_result

final_result = get_default_result()                 
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    #year_month, data = line.split('\t', 1)
    result = ast.literal_eval(line)
    final_result = compare_results(result,final_result)


print '%s\t%s' % (None, str(final_result))
