from datetime import datetime
from pydantic import BaseModel
from utils.db import db, Collection
from typing import List, Optional
from bson.objectid import ObjectId


class AddressBilling(BaseModel):
    firstName: str
    postCode: str
    country: str
    city: str


class AddressShipping(BaseModel):
    firstName: str
    postCode: str
    country: str
    city: str


class OrderItem(BaseModel):
    item: dict
    itemPrice: str
    taxAmount: str
    buyerId: str
    shippingProvier: str
    trackingCode: str
    skuId: str
    statuses: List[str]


class Order(BaseModel):
    userId: str
    platform: str
    shippingFee: str
    paymentMethod: str
    orderId: str
    itemsCount: int
    price: str
    orderItems: List[OrderItem]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    addressBilling: AddressBilling
    addressShipping: AddressShipping


def order_helper(order: Order):
    return {
        "_id": str(order["_id"]),
        "platform": str(order["platform"]),
        "shippingFee": str(order["shippingFee"]),
        "paymentMethod": str(order["paymentMethod"]),
        "orderId": str(order["orderId"]),
        "itemsCount": int(order["itemsCount"]),
        "price": str(order["price"]),
        "orderItems": order["orderItems"],
        "createdAt": order["createdAt"],
        "updatedAt": order["updatedAt"],
        "addressBilling": order["addressBilling"],
        "addressShipping": order["addressShipping"],
    }


def create(order: Order):
    order_collection = db[Collection.ORDER]
    order_collection.find_one_and_update()
    return order_collection.insert_one(order.dict())


def get_all(user_id: str, start_date: datetime = None, end_date: datetime = None):
    order_collection = db[Collection.ORDER]
    if start_date is not None and end_date is not None:
        orders = order_collection.find(
            {"userId": user_id, "createdAt": {"$gte": start_date, "$lte": end_date}}
        )
    else:
        orders = order_collection.find({"userId": user_id})
    output = []
    for order in orders:
        order["orderItems"] = populate_order_items(order["orderItems"])
        output.append(order_helper(order))
    return output


def get_one(order_id: str):
    order_collection = db[Collection.ORDER]
    order = order_collection.find_one({"_id": ObjectId(order_id)})
    if(order == None): return "Not found"
    order["orderItems"] = populate_order_items(order["orderItems"])
    return order_helper(order)


def populate_order_items(order_items: List[OrderItem]):
    output = []
    for order_item in order_items:
        item_id = order_item["item"]
        item_collection = db[Collection.ITEM]
        item = item_collection.find_one({"_id": item_id})
        item["_id"] = str(item["_id"])
        order_item["item"] = item
        output.append(order_item)
    return output
