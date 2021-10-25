from pydantic import BaseModel
from pymongo import MongoClient
from utils.db import db, Collection

class Order(BaseModel):
    arg1: str
    arg2: int

    def __str__(self):
        return f"Haha {self.arg1} {self.arg2}"

    def insert_order(self):
        order_collection = db[Collection.ORDER]
        order_collection.find_one_and_update()
        return order_collection.insert_one(self.dict())


    def find_order():
        order_collection = db[Collection.ORDER]
        return list(order_collection.find())