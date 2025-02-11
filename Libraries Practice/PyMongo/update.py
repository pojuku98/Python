import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Change the address from "Valley 345" to "Canyon 123":
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)


# Update all documents where the address starts with the letter "S":
myquery_1 = { "address": { "$regex": "^S" } }
newvalues_1 = { "$set": { "name": "Minnie" } }

x_1 = mycol.update_many(myquery_1, newvalues_1)

print(x_1.modified_count, "documents updated.")