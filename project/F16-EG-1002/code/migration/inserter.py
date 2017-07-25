from pymongo import errors
from antelope.datascope import TrdataError
 
def joinLoad(antedb, mongodb, antelope_table, fields, *join_tables):
    try:
        collection = mongodb[antelope_table]
        print('collection %s will be created' % antelope_table)
    except errors.CollectionInvalid, e:
        print('Collection %s is not valid' % e)
        return

    try:
        print('Collection %s has following fields:' % antelope_table)
        print(fields)
        counter = 0
        for join_table in join_tables:
            joined_view = antedb.join(join_table)
        
        values = []
        chanid = []
        wfid = []
        for joined_view.record in range(joined_view.query('dbRECORD_COUNT')):
            wfid.append(joined_view.getv('wfid')[0])
            chanid.append(joined_view.getv('chanid')[0])
            if 3 == len(wfid):
                values = joined_view.getv('sta', 'time', 'arid', 'jdate', 'stassid', 'chan', 'iphase', 'stype', 'deltim', 'azimuth', 'delaz', 'slow', 'delslo', 'ema', 'rect', 'amp', 'per', 'logat', 'clip', 'fm', 'snr', 'qual', 'auth', 'commid', 'lddate')
                dic = dict(zip(fields, values))
                dic['wfid'] = wfid
                dic['chanid'] = chanid
                #print(dic)
                r = collection.save(dic)
                #print(r)
                counter += 1
                chanid = []
                wfid = []
                #break
        print('%d records are added to collection %s' % (counter, antelope_table))
    except errors.ExecutionTimeout, e:
        print('Operation execution timeout %s' % e)
        return

def load(antedb, antedbptr, mongodb, antelope_table, fields):
    try:
        #module name 'site' has been taken
        if 'mysite' == antelope_table:
            antelope_table = 'site'
        collection = mongodb[antelope_table]
        print('collection %s will be created' % antelope_table)
    except errors.CollectionInvalid, e:
        print('Collection %s is not valid' % e)
        return
    
    try:
        print('Collection %s has following fields:' % antelope_table)
        print(fields)
        counter = 0
        wfcounter = 0
        #create gridfs file descripter
        import gridfs
        fs = gridfs.GridFS(mongodb)
        import pickle 
        for antedbptr.record in range(antedbptr.query("dbRECORD_COUNT")):
            result = antedbptr.get()
            #print(result)
            values = filter(None, [x.strip('\t\n\r') for x in result.split(' ')])
            dic = dict(zip(fields, values))
            if 'wfdisc' == antelope_table:
                starttime = dic['time']
                endtime = dic['endtime']
                sta = dic['sta']
                chan = dic['chan']
                try:
                    tr = antedbptr.trloadchan(starttime, endtime, sta, chan)
                    if tr.query("dbRECORD_COUNT") > 1:
                        print("More than one records found in station %s channel %s" % (sta, chan))
                        return
                    tr.record = 0
                    r = tr.trdata()
   
                    f = dic['dir'] + '/' + dic['dfile'] + '.' + chan
                
                    with fs.new_file(filename=f, content_type='chunks') as fp:
                        fp.write(pickle.dumps(r))
                    print("%d %s" % (wfcounter, f))
                    wfcounter += 1
                except TrdataError as e:
                    print('TrdataError %s' % e)
                    continue
                finally:
                    tr.close()
            collection.save(dic)
            counter += 1
        print('%d records are added to collection %s' % (counter, antelope_table))
    except errors.ExecutionTimeout, e:
        print('Operation execution timeout %s' % e)
        return
