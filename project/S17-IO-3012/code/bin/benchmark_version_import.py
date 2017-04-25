import matplotlib.pyplot as plt
import sys
import pandas as pd


def get_parm():
    """retrieves mandatory parameter to program

    @param: none
    @type: n/a

    """
    try:
        return sys.argv[1]
    except:
        print ('Must enter file name as parameter')
        exit()


def read_file(filename):
    """reads a file into a pandas dataframe

    @param: filename The name of the file to read
    @type: string

    """
    try:
        return pd.read_csv(filename)
    except:
        print ('Error retrieving file')
        exit()

def select_data(benchmark_df, mongo_version, config_replicas, mongos_instances, shard_replicas, shards_per_replica):
    benchmark_df = benchmark_df[benchmark_df.cloud == "chameleon"]
    benchmark_df = benchmark_df[benchmark_df.test_size == "large"]

    if mongo_version != 'X':
        benchmark_df = benchmark_df[benchmark_df.mongo_version == mongo_version]

    if config_replicas != 'X':
        benchmark_df = benchmark_df[benchmark_df.config_replicas == config_replicas]

    if mongos_instances != 'X':
        benchmark_df = benchmark_df[benchmark_df.mongos_instances == mongos_instances]

    if shard_replicas != 'X':
        benchmark_df = benchmark_df[benchmark_df.shard_replicas == shard_replicas]

    if shards_per_replica != 'X':
        benchmark_df = benchmark_df[benchmark_df.shards_per_replica == shards_per_replica]

    #benchmark_df1 = benchmark_df.groupby(['cloud', 'config_replicas', 'mongos_instances', 'shard_replicas', 'shards_per_replica']).mean()

    #http://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-object-to-dataframe
    benchmark_df = benchmark_df.groupby(['cloud', 'config_replicas', 'mongos_instances', 'shard_replicas', 'shards_per_replica'], as_index=False).mean()
    #http://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-object-to-dataframe

    #print benchmark_df1['shard_replicas']
    #print benchmark_df1
    #print benchmark_df

    benchmark_df = benchmark_df.sort_values(by='shard_replicas', ascending=1)

    return benchmark_df

def make_figure(import_seconds_32, shards_32, import_seconds_34, shards_34):
    """formats and creates a line chart

    @param1: find_seconds_kilo Array with find_seconds from kilo
    @type: numpy array
    @param2: shards_kilo Array with shards from kilo
    @type: numpy array
    @param3: find_seconds_chameleon Array with find_seconds from chameleon
    @type: numpy array
    @param4: shards_chameleon Array with shards from chameleon
    @type: numpy array
    """
    fig = plt.figure()
    #plt.title('Average MongoImport Runtime with Various Numbers of Shards')
    plt.ylabel('Runtime in Seconds')
    plt.xlabel('Number of Shards')

    # Make the chart
    plt.plot(shards_32, import_seconds_32, label='Version 3.2')
    plt.plot(shards_34, import_seconds_34, label='Version 3.4')


    #http://stackoverflow.com/questions/11744990/how-to-set-auto-for-upper-limit-but-keep-a-fixed-lower-limit-with-matplotlib
    plt.ylim(ymin=0)

    plt.legend(loc='best')

    # Show the chart (for testing)
    # plt.show()
    # Save the chart
    fig.savefig('../report/version_import.png')


# Run the program by calling the functions
if __name__ == "__main__":

    filename = get_parm()
    benchmark_df = read_file(filename)

    mongo_version = 32
    config_replicas = 1
    mongos_instances = 1
    shard_replicas = 'X'
    shards_per_replica = 1
    select_df = select_data(benchmark_df, mongo_version, config_replicas, mongos_instances, shard_replicas, shards_per_replica)
    #http://stackoverflow.com/questions/31791476/pandas-dataframe-to-numpy-array-valueerror
    #percentage death=\
    import_seconds_32=select_df.as_matrix(columns=[select_df.columns[6]])
    shards_32 = select_df.as_matrix(columns=[select_df.columns[3]])
    #http://stackoverflow.com/questions/31791476/pandas-dataframe-to-numpy-array-valueerror

    mongo_version = 34
    config_replicas = 1
    mongos_instances = 1
    shard_replicas = 'X'
    shards_per_replica = 1
    select_df = select_data(benchmark_df, mongo_version, config_replicas, mongos_instances, shard_replicas, shards_per_replica)
    #http://stackoverflow.com/questions/31791476/pandas-dataframe-to-numpy-array-valueerror
    #percentage death=\
    import_seconds_34=select_df.as_matrix(columns=[select_df.columns[6]])
    shards_34 = select_df.as_matrix(columns=[select_df.columns[3]])
    #http://stackoverflow.com/questions/31791476/pandas-dataframe-to-numpy-array-valueerror

    make_figure(import_seconds_32, shards_32, import_seconds_34, shards_34)
