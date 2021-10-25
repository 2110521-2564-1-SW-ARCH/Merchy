from dotenv import load_dotenv

load_dotenv()
from typing import List
from fastapi import FastAPI, Query
from models.enum import Courier
import os
import uvicorn
from controllers import thpost
from utils.db import close_conn

app = FastAPI(on_shutdown=[close_conn])
PORT = int(os.getenv("PORT"))

# first use
# user -> register -> retrieve orders from selling platforms -> get order status -> insert orders to db along with status

# later
# webhook -> update(append) orders status

@app.get("/")
def read_root():
    return "order tracking works"


@app.get("/trackbybarcodes/{courier}")
def thpost_track_by_barcodes(courier: Courier, barcodes: List[str] = Query(...)):
    if courier == Courier.THPOST:
        return thpost.track_by_barcodes(barcodes)


if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, reload=True)
