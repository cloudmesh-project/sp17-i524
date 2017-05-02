import iu.i524.S17IRP013.hadoop.hbase_to_hdfs as hb2hdfs
import iu.i524.S17IRP013.data.data_service as DataService

DataService.load_stations();
DataService.load_weather_data()
hb2hdfs.write_all_keys()

