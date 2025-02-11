import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Limit the result to only return 5 documents:
myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)