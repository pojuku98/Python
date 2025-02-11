import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Find One
x = mycol.find_one()

print(x)

# Find all
for x in mycol.find():
  print(x)

# Return only the names and addresses, not the _ids:
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

# Exclude "address" from the result:
for x in mycol.find({},{ "address": 0 }):
  print(x)