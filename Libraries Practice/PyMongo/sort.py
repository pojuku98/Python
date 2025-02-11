import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Sort the result alphabetically by name:
mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)

# Sort the result reverse alphabetically by name:
mydoc_r = mycol.find().sort("name", -1)

for x in mydoc_r:
  print(x)