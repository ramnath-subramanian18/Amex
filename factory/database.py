from pymongo import MongoClient
from bson.objectid import ObjectId
client=MongoClient()
import pymongo
import ssl
client=pymongo.MongoClient('mongodb+srv://ramnath1:ramnath1@cluster0.agxnajm.mongodb.net/',ssl=True,ssl_cert_reqs=ssl.CERT_NONE)

db = client['split_up']
collection = db["bank statement"]
def insert_data(data,file_name_pdf):
    search_query = {"FilenameUserId": file_name_pdf}
    result = collection.find(search_query)
    if result.count() == 0:
        collection.insert_many(data) 
def find(fileNameUserId):
    resultFromDbTransactionData=[]
    search_query = {"FilenameUserId": fileNameUserId}
    result = collection.find(search_query)
    for results in result:
        if(results['Deleted']==0):
            resultFromDbTransactionData.append(results)
    return resultFromDbTransactionData

def update(id):
    search_query = {"_id": ObjectId(id)}
    update_operation = {"$set": {"Deleted": 1}}
    result = collection.update_one(search_query, update_operation)

