from pymongo import MongoClient
from models import Order

DB = "sa"
ORDER_COLLECTION = "orders"

# first use
# user -> register -> retrieve orders from selling platforms -> get order status -> insert orders to db along with status

# later
# webhook -> update(append) orders status

def insert_order(order: Order):
    with MongoClient() as client:
        order_collection = client[DB][ORDER_COLLECTION]
        return order_collection.insert_one(order.dict())

def find_order():
    with MongoClient() as client:
        order_collection = client[DB][ORDER_COLLECTION]
        return list(order_collection.find())