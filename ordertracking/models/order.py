from datetime import datetime
from pydantic import BaseModel
from utils.db import db, Collection
from typing import List, Optional


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
        "createdAt": order["createdAt"],
        "updatedAt": order["updatedAt"],
        "addressBilling": order["addressBilling"],
        "addressShipping": order["addressShipping"],
    }


def create(order: Order):
    order_collection = db[Collection.ORDER]
    order_collection.find_one_and_update()
    return order_collection.insert_one(order.dict())


def get_all(user_id: str):
    order_collection = db[Collection.ORDER]
    orders = order_collection.find({"userId": user_id})
    output = []
    for order in orders:
        for order_item in order["orderItems"]:
            item_id = order_item["item"]
            item_collection = db[Collection.ITEM]
            order_item["item"] = item_collection.find_one({"_id": item_id})
        output.append(order_helper(order))
    return output
