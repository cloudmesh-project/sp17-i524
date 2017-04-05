import iu.i524.S17IRP013.ncdc.weather_services as Services
import iu.i524.S17IRP013.dao.stations_dao as stations


###############################################################
def load_stations():
    limit = 25    
    offset = 0
    nbr_of_records = 0
    result = Services.get_stations(offset=offset)   
    while(result!={}):       
        nbr_of_records = nbr_of_records + insert_station(result['results'])
        offset = offset + limit
        result = Services.get_stations(offset=offset)
    print str(nbr_of_records) + ' stations loaded successfully !!'    
###############################################################
def insert_station(results):
    count = 0 
    for data in results:
        cell = stations.get_cell(data)
        row_key = str(data['id'])
        stations.insert(row_key, cell)
        count = count + 1
    return count    
###############################################################
def load_weather_data():
    limit = 25    
    offset = 0
    result = Services.get_weather_data(startDate='1968-01-01',endDate='1970-01-01',stationId='GHCND:IN001011001')   
    while(result!={}):        
        print result['results']
        offset = offset + limit
        result = Services.get_stations(offset=offset)
###############################################################