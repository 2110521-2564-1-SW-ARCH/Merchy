from typing import Optional
from fastapi import FastAPI
import thpost

app = FastAPI()

@app.get("/")
def read_root():
    a = 123
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
