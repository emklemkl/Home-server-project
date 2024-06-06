import os
from flask import request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from dotenv import load_dotenv
load_dotenv()

class Database():
    def __init__(
            self, 
            uri: str = os.getenv("MONGO_URI"),
            db_name: str = os.getenv("DB_NAME"),
            ) -> None:
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client[db_name]
        

    def get_all_from_collection(self, col_name):
        try:
            return list(self.db[col_name].find())
        except Exception as e:
            print(e)

    def get_doc_in_collection_names(self, col_name):
        try:
            return list(self.db[col_name].find({}, {"name": 1}))
        except Exception as e:
            print(e)
            
    def get_doc_based_on_id(self, col_name: str, id: str):
        try:
            return self.db[col_name].find({"_id": ObjectId(id)}).next()
            # return list(self.db[col_name].find({"_id": ObjectId(id)}))
        except Exception as e:
            print(e)

    # Send a ping to confirm a successful connection
    def ping_db_test(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            print(self.db["projects"].find_one())
        except Exception as e:
            print(e)
