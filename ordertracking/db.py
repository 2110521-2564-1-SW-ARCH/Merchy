from pymongo import MongoClient
from models import Order, Token
import os

DB_URL = os.getenv("DB_URL")
DB = "sa"
ORDER_COLLECTION = "orders"
TOKEN_COLLECTION = "tokens"

# first use
# user -> register -> retrieve orders from selling platforms -> get order status -> insert orders to db along with status

# later
# webhook -> update(append) orders status


def insert_order(order: Order):
    with MongoClient(DB_URL) as client:
        order_collection = client[DB][ORDER_COLLECTION]
        return order_collection.insert_one(order.dict())


def find_order():
    with MongoClient(DB_URL) as client:
        order_collection = client[DB][ORDER_COLLECTION]
        return list(order_collection.find())


def insert_or_update_token(token: Token):
    with MongoClient(DB_URL) as client:
        token_collection = client[DB][TOKEN_COLLECTION]
        t = token_collection.find_one_and_update(
            {"name": token.name}, {"$set": token.dict()}
        )
        return t if t != None else token_collection.insert_one(token.dict())