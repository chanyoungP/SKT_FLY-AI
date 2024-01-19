import os
import sys
import pymongo
from dotenv import load_dotenv
import collections


load_dotenv()
CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
DB_NAME = "products"
COLLECTION_NAME = "books"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client[DB_NAME]

collection = db[COLLECTION_NAME]
# --- 유지 ---- 

findValue = {"category":"Marketing, Sales"}
newValue = {"$set":{"category":"Business, Money"}}

collection.update_one(findValue,newValue)
