import hbase_connect as dao_parent

table_name = 'stations'
##############################################################################################################################
def get_cf():
    cf = {
        'station' : dict(),
        'date_range' :  dict() ,
        'location' : dict(),
    }
    return cf;
##############################################################################################################################
def get_cell(station_data):
    cell = {b'station:name':str(station_data['name']), b'station:id':str(station_data['id']) , \
            b'date_range:min_date': str(station_data['mindate']), b'date_range:max_date':str(station_data['maxdate']), \
            b'location:latitude' :  str(station_data['latitude']), b'location:longitude':str(station_data['longitude'])   }
    return cell
##############################################################################################################################
def insert(row_key, cell):    
    table.put(row_key, cell)
##############################################################################################################################    
def get_station_data(start_row=''):   
    st_list = dict()
    count = 0    
    if(start_row == ''):    
        for key, data in table.scan(limit=10):
            st_list[key] = {'min_date':data['date_range:min_date'], 'max_date':data['date_range:max_date'] , \
                            'station_id': data['station:id'], 'latitude':data['location:latitude'], \
                            'longitude':data['location:longitude']}            
    else:
        for key, data in table.scan(limit=11, row_start=start_row):            
            count = count + 1
            if(count > 1):
                st_list[key] = {'min_date':data['date_range:min_date'], 'max_date':data['date_range:max_date'], \
                            'station_id': data['station:id'], 'latitude':data['location:latitude'], \
                            'longitude':data['location:longitude']}    
    return st_list   
##############################################################################################################################             
dao_parent.create_table(table_name, get_cf())
table = dao_parent.hb_conn.table(table_name)
