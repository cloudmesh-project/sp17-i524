import iu.i524.S17IRP013.dao.weather_dao as weather_base
import os as env
import subprocess as subprocess

WDA_RK_FILE_NAME = 'wda_row_keys.txt'


def find_by_id(row_key):
    data_map = weather_base.find_by_id(row_key);
    record = list()
    for key, value in data_map.items():            
        formatted_data = dict()
        ds_array = key.split(':')
        if(is_valid_parameter(str(ds_array[3]))):
            formatted_data['station_id'] = str(ds_array[1] + ':' + ds_array[2])
            formatted_data['parameter'] = str(ds_array[3]);
            formatted_data['value'] = str(value)
            record.append(formatted_data)
    return record;


def copy_file_to_hdfs(filepath):
    FNULL = open(env.devnull, 'w')
    hdfs_cmd = get_hadoop_path() + '/bin/hdfs' 
    rm_wda = subprocess.Popen([hdfs_cmd, "dfs", "-rm", "-r", "/wda"], stdout=FNULL, stderr=subprocess.STDOUT)
    rm_wda.communicate()
    print '.',
    mkdir_wda = subprocess.Popen([hdfs_cmd, "dfs", "-mkdir", "/wda"], stdout=FNULL, stderr=subprocess.STDOUT)
    mkdir_wda.communicate()
    print '.',
    mkdir_inp = subprocess.Popen([hdfs_cmd, "dfs", "-mkdir", "/wda/input"], stdout=FNULL, stderr=subprocess.STDOUT)
    mkdir_inp.communicate()
    print '.',
    copy_inp_file = subprocess.Popen([hdfs_cmd, "dfs", "-copyFromLocal", WDA_RK_FILE_NAME, "/wda/input/"], stdout=FNULL, stderr=subprocess.STDOUT)
    copy_inp_file.communicate()
    print ' - Ok '
    FNULL.close()
    return True;

def write_all_keys():
    data_file = open(WDA_RK_FILE_NAME, 'w')
    record_count = 0
    count = 0
    print 'Getting files from hbase and flushing it to '+ WDA_RK_FILE_NAME + ' file ' 
    print 'Flushing data set ',
    for key in weather_base.get_all_row_keys():
        if record_count == 0:
            data_file.write(key)
        else:
            data_file.write('\n' + key)
        record_count = record_count + 1
        count = count + 1
        if count == 100:
            count = 0
            data_file.flush()
            print '.',
            
    data_file.close() 
    print ' Ok'       
    print ' Copying to HDFS ',
    copy_file_to_hdfs(filepath=WDA_RK_FILE_NAME)    
    env.remove(WDA_RK_FILE_NAME)

def write_weather_data_set():
    start_row = ''
    data_map = weather_base.get_weather_data(start_row)
    count = 1
    while(data_map != {} and count <= 2):         
        start_row = data_map['END_INDEX']
        for key, value in test_weather_data(data_map['RESULT']).items():
            print key, value
        data_map = weather_base.get_weather_data(start_row)
        count = count + 1

def test_weather_data(data_set):
    record_list = dict()       
    for ym_key, ym_value in data_set.items():
        record = list()
        for key, value in ym_value.items():            
            formatted_data = dict()
            ds_array = key.split(':')
            if(is_valid_parameter(str(ds_array[3]))):
                formatted_data['station_id'] = str(ds_array[1] + ':' + ds_array[2])
                formatted_data['parameter'] = str(ds_array[3]);
                formatted_data['value'] = str(value)
                record.append(formatted_data)            
        record_list[ym_key] = record
    return record_list


def is_valid_parameter(parameter):
    result = False;
    if parameter == 'TMAX':
        result = True;
    elif parameter == 'TMIN':
        result = True;
    elif parameter == 'TAVG':
        result = True;
    elif parameter == 'PRCP':
        result = True;
    return result;
        
def get_hadoop_path():
    hadoop = env.getenv('HADOOP_HOME', default='NONE')
    if(hadoop == 'NONE'):
        hadoop = env.getenv('HADOOP_INSTALL', default='NONE')
    return hadoop
            
