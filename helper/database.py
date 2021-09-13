import pymongo 
import os

DB_NAME = os.environ.get("DB_NAME","my")
DB_URL = os.environ.get("DB_URL","mongodb+srv://s1com:s1com@cluster0.wrrwz.mongodb.net/Cluster0?retryWrites=true&w=majority")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["USER"]

def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id,"group_id":None}
            try:
            	dbcol.insert_one(user_det)
            except:
            	pass



def getid():
    values = []
    for key  in dbcol.find():
         id = key["_id"]
         values.append((id)) 
    return values
