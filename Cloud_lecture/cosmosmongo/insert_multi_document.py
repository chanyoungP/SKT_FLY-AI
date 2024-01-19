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
books = [
    {
    "_id":1,
    "category":"Marketing, Sales",
    "name":"마케팅 불변의 법칙",
    "author":"알 리스 잭 트라우트",
    "publisher": "비즈니스"
},
    {
    "_id":2,
    "category":"Marketing, Sales",
    "name":"정상에서 만납시다",
    "author":"지그지글러",
    "publisher": "김도언"
},
]




result = collection.insert_many(books)
print("추가된 문서_id : {}\n".format(result.inserted_ids))