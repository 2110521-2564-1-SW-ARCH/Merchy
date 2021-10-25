from datetime import datetime
from enum import Enum
from pydantic import BaseModel
import db

class TokenName(str, Enum):
    THPOST_REQUEST_TOKEN = "thpost_dynamic_token"
    THPOST_WEBHOOK_TOKEN = "thpost_webhook_token"


class Order(BaseModel):
    arg1: str
    arg2: int

    def __str__ (self):
        return f"Haha {self.arg1} {self.arg2}"

class Token(BaseModel):
    expire: datetime
    token: str
    name: TokenName

    def insert_or_update(self):
        return db.insert_or_update_token(self)