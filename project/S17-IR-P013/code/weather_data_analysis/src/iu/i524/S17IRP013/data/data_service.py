import iu.i524.S17IRP013.ncdc.weather_services as Services
import iu.i524.S17IRP013.dao.stations_dao as stations
import iu.i524.S17IRP013.dao.weather_dao as weather
import iu.i524.S17IRP013.util.app_util as AppUtil


###############################################################
def load_stations():
    limit = 25    
    offset = 0
    nbr_of_records = 0
    result = Services.get_stations(offset=offset)   
    while(result != {}):       
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
    st_list = stations.get_station_data(start_row='')
    for key, value in st_list.items():
        get_weather_data(startDate=value['min_date'], endDate=value['max_date'], stationId=key, station_details=value) 

###############################################################
def get_weather_data(station_details, startDate='1968-01-01', endDate='1970-01-01', stationId='GHCND:IN001011001'):
    date_range_list = AppUtil.get_year_list(start_date=startDate, end_date=endDate)
    for date_range in date_range_list:
        limit = 25    
        offset = 0
        result = Services.get_weather_data(startDate=date_range['min_date'], endDate=date_range['max_date'], stationId=stationId, offset=offset)   
        while(result != {}):        
            #print result['results']
            insert_result(result['results'], station_details)
            offset = offset + limit
            result = Services.get_weather_data(startDate=date_range['min_date'], endDate=date_range['max_date'], stationId=stationId, offset=offset)
###############################################################
def insert_result(result_list, station_details):
    station_id = station_details['station_id']
    latitude = station_details['latitude']
    longitude = station_details['longitude']
    grouped_weather_data = groub_weather_data(result_list)
    for key, value in grouped_weather_data.items():
        cell = weather.get_cell(value, station_id, latitude, longitude)
        if(cell != {}):            
            print 'Inserting record -> '+str(cell)
            weather.insert(key, cell)            
###############################################################            
def groub_weather_data(result_list):
    group_data = dict()    
    for result in result_list:
        year_month = AppUtil.format_date(result['date'], target_format='')
        if year_month in group_data.keys():
            group_data[year_month].append(result)
        else:
            data_list = list()    
            data_list.append(result)
            group_data[year_month] = data_list
    return group_data
