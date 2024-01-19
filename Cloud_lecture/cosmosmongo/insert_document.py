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
book = {
    "category":"Computer, Technology",
    "name":"MongoDB The Definitive guide",
    "quantiy":2,
    "sale":False
},

result = collection.insert_many(book)
print("추가된 문서_id : {}\n".format(result.inserted_ids[0]))