import pymongo

myclient = pymongo.MongoClient("mongodb://drtino:password123@localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

print(myclient.list_database_names())

