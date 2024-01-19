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

find_docs = collection.find({
    "category":"Marketing, Sales"
})

for doc in find_docs:
    print(doc)


# print(find_doc)

