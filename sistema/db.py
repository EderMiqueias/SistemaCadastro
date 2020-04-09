import pymongo

url = "35.193.200.100"
port = 2323
client = pymongo.MongoClient(host=url,port=port)

def getdb():
    db = client['sistemaweb']
    return db
