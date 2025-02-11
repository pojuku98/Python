import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Delete the document with the address "Mountain 21":
myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)

# Delete all documents were the address starts with the letter S:
myquery_1 = { "address": {"$regex": "^S"} }

x_1 = mycol.delete_many(myquery_1)

print(x_1.deleted_count, " documents deleted.")

# Delete all documents in the "customers" collection:
x_2 = mycol.delete_many({})

print(x_2.deleted_count, " documents deleted.")