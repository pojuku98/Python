import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Check if Database Exists
print(myclient.list_database_names())

# Check a specific database by name
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")