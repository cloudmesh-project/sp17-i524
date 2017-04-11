import datetime as datetime

##########################################################################
def enum(**enums):
    return type('Enum', (), enums)

##########################################################################
def get_year_list(start_date, end_date):
    'Get list of date range with each range of one year. Date format is `yyyy-mm-dd`. Result will be a list of dictionary having \
    key as `max_date` and `min_date` '   
    start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    curr_date_obj = start_date_obj 
    year_list = list()  
    while(int(curr_date_obj.year) < int(end_date_obj.year)):        
        date_range = dict()
        if(len(year_list) > 0):
            curr_date_obj = curr_date_obj + datetime.timedelta(days=1)       
        date_range['min_date'] = curr_date_obj.strftime('%Y-%m-%d')
        curr_date_obj = curr_date_obj + datetime.timedelta(days=365)
        if(int(curr_date_obj.year) < int(end_date_obj.year)):
            date_range['max_date'] = curr_date_obj.strftime('%Y-%m-%d')
            year_list.append(date_range)
        else:
            date_range['max_date'] = end_date_obj.strftime('%Y-%m-%d')    
            year_list.append(date_range)
            break;
    if(len(year_list) == 0):
            date_range = dict()
            date_range['min_date'] = start_date_obj.strftime('%Y-%m-%d')
            date_range['max_date'] = end_date_obj.strftime('%Y-%m-%d')    
    return  year_list
##########################################################################
def format_date(dateTime,target_format,src_format='%Y-%m-%dT%H:%M:%S'):
    dateTime_obj = datetime.datetime.strptime(dateTime, src_format)
    return dateTime_obj.strftime('%Y-%m')