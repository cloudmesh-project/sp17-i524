import requests
import iu.i524.S17IRP013.util.app_util as AppUtil

NCDC_API = 'https://www.ncdc.noaa.gov/cdo-web/api/v2'

NCDC_SERVICES = AppUtil.enum(DATASETS='/datasets', DATA_CATEGORIES='/datacategories', DATA_TYPE='/datatypes', \
                             LOCATION_CATEORIES='/locationcategories' , LOCATIONS='/locations', \
                             STATIONS='/stations', WEATHER_DATA='/data')

DATA_TYPES = AppUtil.enum(PRECIPITATION='PRCP', SNOWFALL = 'SNOW', TEMP_AVG='TAVG' \
                          , TEMP_MAX = 'TMAX', TEMP_MIN = 'TMIN'  )

TOKEN = 'uBsxpIavTKiqKAMlyMrwkkvemOQQfpTg'
HEADERS = {'token':TOKEN}

def get_stations(country='FIPS:IN', offset=0):
    url = NCDC_API + NCDC_SERVICES.STATIONS + '?locationid=' + country + '&offset=' + str(offset)
    
    response = requests.get(url, headers=HEADERS)
    return response.json()

def prepare_dataTypeUrl():
    dataTypeId = '&datatypeid='
    url = dataTypeId+DATA_TYPES.PRECIPITATION+dataTypeId \
    + DATA_TYPES.SNOWFALL + dataTypeId + DATA_TYPES.TEMP_AVG + dataTypeId + DATA_TYPES.TEMP_MAX + dataTypeId \
    + DATA_TYPES.TEMP_MIN 
    return url

def get_weather_data(startDate,endDate,stationId,country='FIPS:IN', offset=0):
    url = NCDC_API+NCDC_SERVICES.WEATHER_DATA+'?datasetid=GSOM'+prepare_dataTypeUrl()+ \
     '&stationid=' + stationId + '&startdate=' + startDate + '&enddate=' \
     + endDate + '?locationid=' + country + '&offset=' + str(offset)
    response = requests.get(url, headers=HEADERS) 
    return response.json()

