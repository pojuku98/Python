import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

# Check if Collection Exists
mycol = mydb["customers"]

print(mydb.list_collection_names())

# Check a specific collection by name
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")