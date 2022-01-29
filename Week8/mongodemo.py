import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = {"name": "John", "address": "Highway 37"}

x = mycol.insert_one(mydict)

print(mydb.list_collection_names())
