from pymongo import MongoClient
from enum import Enum
import os

DB_URL = os.getenv("DB_URL")
DB_NAME = "sa"

class Collection(str, Enum):
    ORDER = "orders"
    TOKEN = "tokens"
    ITEM = "items"


conn = MongoClient(DB_URL)
db = conn[DB_NAME]

def close_conn():
    print("Database disconnected")
    conn.close()