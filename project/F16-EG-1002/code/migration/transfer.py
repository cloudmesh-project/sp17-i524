import sys

"""
Waveform transfer main entrance, accepting arguments and transfer all waveform data into GridFS.
"""
def usage():
    print 'python transfer.py [OPTIONS]\n\
    \t -h --help\t\t\tPrint this help screen\n\
    \t -i --mongodb_host\t\tMongoDB server host (default: localhost)\n\
    \t -p --mongodb_port\t\tMongoDB server port (default: 27017)\n\
    \t -w --waveform_path\t\tWaveform absolute path\n'

def createMongoClient(mongodb_host, mongodb_port):
    from pymongo import MongoClient
    try:
        mongoclient = MongoClient('mongodb://' + mongodb_host + ':' + mongodb_port)
        mongodb = mongoclient['local']
        return mongodb
    except pymongo.errors.ConnnectionFailure, e:
        print('Could not connect to MongoDB: %s' % e)
        sys.exit(2)

def main(argv):
    import getopt
    try:
        opts, args = getopt.getopt(argv, "w:i:p:h", ["waveform_path=", \
        "mongodb_host=", "mongodb_port=", "help"])
        if not opts:
            usage()
            sys.exit(2)
        mongodb_host = '127.0.0.1'
        mongodb_port = '27017'
        waveform_path = ''
        for opt, arg in opts:
            if opt in ('-w', '--waveform_path'):
                waveform_path = arg
            elif opt in ('-i', '--mongodb_host'):
                mongodb_host = arg
            elif opt in ('-p', '--mongodb_port'):
                mongodb_port = arg
            elif opt in ('-h', '--help'):
                usage()
                sys.exit(2)

    except getopt.GetoptError:
        usage()
        sys.exit(2)
    if '' == waveform_path:
        usage()
        sys.exit(2)
    
    #init mongodb collection
    mongodb = createMongoClient(mongodb_host, mongodb_port)
    try:
        collection = mongodb['wfdisc']
    except errors.CollectionInvalid, e:
        print('Collection %s is not valid' % e)
        return


    #create gridfs file descripter
    import gridfs
    fs = gridfs.GridFS(mongodb)
    
    from obspy.core import read
    cursor = collection.find()
    count = 0
    for wf in cursor:
        if '2011' in wf['dir']: continue
        name = waveform_path + '/' + wf['dir'] + '/' + wf['dfile']
        print(name)
        traces = read(name)
        for ts in traces:
            f = wf['dir'] + '/' + wf['dfile'] + '.' + ts.stats['channel']
            print(f)
            #break
            with fs.new_file(filename=f, content_type='chunks') as fp:
                fp.write(ts.data)
        count += 1
        #break
    print('%d files have been transfered into GridFS' % count)

    
if __name__ == "__main__":
    main(sys.argv[1:])
