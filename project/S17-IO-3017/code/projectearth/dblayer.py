from pymongo import MongoClient

class classDBLayer:
    client = None
    db = None

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client.TestUSGS

    def dropdb(self):
        return self.db.usgsdata.drop()

    def insertdata(self, data=[]):
        return self.db.usgsdata.insert_many(data)

    def count(self):
        return self.db.usgsdata.count()

    def doaggregate(self, projection=[]):
        return self.db.usgsdata.aggregate(projection)

    def closedb(self):
        self.client.close()


