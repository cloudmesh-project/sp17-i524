import hbase_connect as dao_parent

table_name = 'weather'
##############################################################################################################################
def get_cf(datatype, station_id):
    cf = b'weather:' + station_id + ':' + datatype
    return cf;
##############################################################################################################################
def get_cell(weather_data_list, station_id, latitude, longitude):    
    prcp = 0;tmax = 0;tmin = 0;tavg = 0;
    cf_data_types = dict()
    for weather_data in weather_data_list : 
        dataType = weather_data['datatype']
        if(dataType == 'PRCP'):
            prcp = float(weather_data['value'])
            if(prcp != 0):
                cf_data_types[get_cf(station_id=station_id, datatype='PRCP')] = str(prcp)
        elif(dataType == 'TMAX'):
            tmax = float(weather_data['value'])
            if(tmax != 0):
                cf_data_types[get_cf(station_id=station_id, datatype='TMAX')] = str(tmax) 
        elif(dataType == 'TMIN'):
            tmin = float(weather_data['value'])
            if(tmin != 0):
                cf_data_types[get_cf(station_id=station_id, datatype='TMIN')] = str(tmin)
        elif(dataType == 'TAVG'):
            tavg = float(weather_data['value'])
            if(tavg != 0):
                cf_data_types[get_cf(station_id=station_id, datatype='TAVG')] = str(tavg)            
    if(len(cf_data_types) != 0):        
        cf_data_types[get_cf(station_id=station_id, datatype='LAT')] = str(latitude)
        cf_data_types[get_cf(station_id=station_id, datatype='LON')] = str(longitude)
    return cf_data_types
##############################################################################################################################
def insert_list(row_key, cell_list):  
    tb_batch = table.batch(batch_size=10)  
    for cell in cell_list:
        tb_batch.put(row_key, cell)

def insert(row_key, cell):
    table.put(row_key, cell)
##############################################################################################################################    
def get_weather_data(start_row=''):   
    st_list = dict()
    count = 0    
    if(start_row == ''):    
        for key, data in table.scan(limit=10):
            st_list[key] = {'min_date':data['date_range:min_date'], 'max_date':data['date_range:max_date']}            
    else:
        for key, data in table.scan(limit=11, row_start=start_row):            
            count = count + 1
            if(count > 1):
                st_list[key] = {'min_date':data['date_range:min_date'], 'max_date':data['date_range:max_date']}    
    return st_list   
##############################################################################################################################             
dao_parent.create_table(table_name, {'weather':dict()})
table = dao_parent.hb_conn.table(table_name)
