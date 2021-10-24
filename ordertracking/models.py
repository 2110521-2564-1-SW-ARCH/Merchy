from datetime import datetime
from pydantic import BaseModel

class Order(BaseModel):
    arg1: str
    arg2: int

    def __str__ (self):
        return f"Haha {self.arg1} {self.arg2}"