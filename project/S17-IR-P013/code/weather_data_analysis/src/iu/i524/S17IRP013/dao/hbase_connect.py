import happybase as hbase

hb_conn = hbase.Connection('localhost', table_prefix='wda')

##############################################################
def create_table(table_name, families):
    is_table_exists = False;
    try:
        is_table_exists = hb_conn.is_table_enabled(table_name)
    except:
        is_table_exists = False;
    if(is_table_exists == False):
        hb_conn.create_table(table_name, families)
        print 'Table ' + table_name + ' created successfully !!'    
        return True
    else:
        print 'Table ' + table_name + ' exists !!'    
        return False
##############################################################

def delete_table(table_name):
    is_table_exists = True;
    try:
        is_table_exists = hb_conn.is_table_enabled(table_name)
        if(is_table_exists):
            hb_conn.disable_table(table_name)
        hb_conn.delete_table(table_name)
    except:
        is_table_exists = False;
    if(is_table_exists == False):        
        print 'Table ' + table_name + ' deleted successfully !!'    
        return True
    else:
        print 'Table ' + table_name + ' does not exists !!'    
        return False

print hb_conn.tables()
