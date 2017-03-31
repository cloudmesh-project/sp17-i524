import iu.i524.S17IRP013.ncdc.weather_services as Services




def load_stations():
    limit = 25    
    offset = 0
    result = Services.get_stations(offset=offset)   
    while(result!={}):        
        print result['results']
        offset = offset + limit
        result = Services.get_stations(offset=offset)

def load_weather_data():
    limit = 25    
    offset = 0
    result = Services.get_weather_data(startDate='1968-01-01',endDate='1970-01-01',stationId='GHCND:IN001011001')   
    while(result!={}):        
        print result['results']
        offset = offset + limit
        result = Services.get_stations(offset=offset)