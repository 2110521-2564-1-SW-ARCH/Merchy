from dotenv import load_dotenv

load_dotenv()
import os
import uvicorn
from typing import List
from fastapi import FastAPI, Query
from models.enum import Courier, Platform
from models import order as Order
from controllers import thpost, lazada
from utils.db import close_conn
from datetime import datetime

app = FastAPI(on_shutdown=[close_conn])
PORT = int(os.getenv("PORT"))
HOST = str(os.getenv("IP"))


@app.get("/")
def read_root():
    return "order tracking works"


@app.get("/get_order/{order_id}")
def test1(order_id: str):
    return lazada.get_order(order_id)


@app.get("/get_orders")
def test1():
    return lazada.get_orders()


@app.get("/get_order_items/{order_id}")
def test2(order_id: str):
    return lazada.get_order_items(order_id)

@app.get("/find_one/{order_id}")
def test2(order_id: str):
    a = Order.get_one_by_trade_order_id(order_id)
    print("here", a)
    return a


@app.get("/trackbybarcodes/{courier}")
def thpost_track_by_barcodes(courier: Courier, barcodes: List[str] = Query(...)):
    if courier == Courier.THPOST:
        return thpost.track_by_barcodes(barcodes)


@app.get("/orders")
def get_all_orders(user_id: str, start_date: str = None, end_date: str = None):
    if start_date is not None and end_date is not None:
        return {
            "orders": Order.get_all(
                user_id,
                datetime.fromisoformat(start_date),
                datetime.fromisoformat(end_date),
            )
        }
    return {"orders": Order.get_all(user_id)}


@app.get("/orders/{order_id}")
def get_one_order(order_id: str):
    return Order.get_one(order_id)


@app.post("/webhook/{platform}", status_code=200)
def handle_webhook(platform: Platform, body: dict):
    print(body)
    if platform == Platform.LAZADA:
        # trade order
        if body["message_type"] == 0: lazada.create_or_update_order(body)
    return "OK"


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
