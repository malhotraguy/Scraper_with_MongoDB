import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
print(x.inserted_id)

dblist = myclient.list_database_names()
collist = mydb.list_collection_names()
print(dblist)
print(collist)
if "mydatabase" in dblist:
  print("The database exists.")
else:
    print("mydatabase doesnt exist")
if "customers" in collist:
  print("The collection exists.")
