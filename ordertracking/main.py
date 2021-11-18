from dotenv import load_dotenv

load_dotenv()
from typing import List
from fastapi import FastAPI, Query
from models.enum import Courier
from models import order as Order
import os
import uvicorn
from controllers import thpost
from utils.db import close_conn

app = FastAPI(on_shutdown=[close_conn])
PORT = int(os.getenv("PORT"))


@app.get("/")
def read_root():
    return "order tracking works"


@app.get("/trackbybarcodes/{courier}")
def thpost_track_by_barcodes(courier: Courier, barcodes: List[str] = Query(...)):
    if courier == Courier.THPOST:
        return thpost.track_by_barcodes(barcodes)


@app.get("/orders")
def get_all_orders(user_id: str):
    return {"orders": Order.get_all(user_id)}


if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, reload=True)
