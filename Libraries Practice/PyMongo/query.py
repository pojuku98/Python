import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Filter
myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

#address greater than S:
myquery_1 = { "address": {"$gt": "S"} }

mydoc_1 = mycol.find(myquery_1)

for x in mydoc_1:
  print(x)

#address starts with S:
myquery_2 = { "address": { "$regex": "^S" } }

mydoc_2 = mycol.find(myquery_2)

for x in mydoc_2:
  print(x)