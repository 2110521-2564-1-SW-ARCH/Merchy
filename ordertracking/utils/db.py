from pymongo import MongoClient
from enum import Enum
import os
from signal import signal, SIGINT

DB_URL = os.getenv("DB_URL")
DB_NAME = "sa"
ORDER_COLLECTION = "orders"
TOKEN_COLLECTION = "tokens"

class Collection(str, Enum):
    ORDER = "orders"
    TOKEN = "tokens"


conn = MongoClient(DB_URL)
db = conn[DB_NAME]

def close_conn():
    print("Database disconnected")
    conn.close()