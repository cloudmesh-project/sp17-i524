import hbase_connect as dao_parent

table_name = 'stations'

def get_cf():
    cf = {
        'station' : dict(),
        'date_range' :  dict() ,
        'location' : dict(),
    }
    return cf;

def get_cell(station_data):
    cell = {b'station:name':str(station_data['name']), b'station:id':str(station_data['id']) , \
            b'date_range:min_date': str(station_data['mindate']), b'date_range:max_date':str(station_data['maxdate']), \
            b'location:latitude' :  str(station_data['latitude']), b'location:longitude':str(station_data['longitude'])   }
    return cell

def insert(row_key,cell):
    table = dao_parent.hb_conn.table(table_name)
    table.put(row_key, cell)


dao_parent.create_table(table_name, get_cf())