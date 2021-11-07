from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from utils.db import db, Collection


class Type(str, Enum):
    THPOST_REQUEST_TOKEN = "thpost_dynamic_token"
    THPOST_WEBHOOK_TOKEN = "thpost_webhook_token"


class Token(BaseModel):
    expire: datetime
    token: str
    type: Type


def insert_or_update(token: Token):
    token_collection = db[Collection.TOKEN]
    t = token_collection.find_one_and_update({"type": token.type}, {"$set": token.dict()})
    return t if t != None else token_collection.insert_one(token.dict())

def get_dynamic_token(type: Type):
    token_collection = db[Collection.TOKEN]
    t = token_collection.find_one({"type": type})
    return t['token']