import requests
import iu.i524.S17IRP013.util.app_util as AppUtil

NCDC_API = 'https://www.ncdc.noaa.gov/cdo-web/api/v2'

NCDC_SERVICES = AppUtil.enum(DATASETS='/datasets', DATA_CATEGORIES='/datacategories', DATA_TYPE='/datatypes', \
                             LOCATION_CATEORIES='/locationcategories' , LOCATIONS='/locations', \
                             STATIONS='/stations', WEATHER_DATA='/data')

TOKEN = 'uBsxpIavTKiqKAMlyMrwkkvemOQQfpTg'

def get_stations(country='FIPS:IN', offset=0):
    url = NCDC_API + NCDC_SERVICES.STATIONS + '?locationid=' + country + '&offset=' + str(offset)
    headers = {'token':TOKEN}
    response = requests.get(url, headers=headers)
    return response.json()
