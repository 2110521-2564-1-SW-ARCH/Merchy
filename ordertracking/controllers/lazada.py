import lazop
import os
import requests
from models import order as Order
from models.enum import Platform
from datetime import datetime
from utils.adapter import InventoryService

APP_KEY = os.getenv("LAZADA_APP_KEY")
APP_SECRET = os.getenv("LAZADA_APP_SECRET")
ACCESS_TOKEN = os.getenv("MY_ACCESS_TOKEN")
URL = "https://api.lazada.co.th/rest"

AUTHENTICATION_SERVICE_IP = os.getenv("AUTHENTICATION_SERVICE_IP")
AUTHENTICATION_SERVICE_PORT = os.getenv("AUTHENTICATION_SERVICE_PORT")
AUTHENTICATION_SERVICE_PROTOCOL = os.getenv("AUTHENTICATION_SERVICE_PROTOCOL")
AUTHENTICATION_SERVICE_URL = f"{AUTHENTICATION_SERVICE_PROTOCOL}://{AUTHENTICATION_SERVICE_IP}"
if AUTHENTICATION_SERVICE_PORT is not "": AUTHENTICATION_SERVICE_URL += f":{AUTHENTICATION_SERVICE_PORT}"

client = lazop.LazopClient(URL, APP_KEY, APP_SECRET)
InventoryService = InventoryService()


def get_access_token_by_user_id(user_id: str):
    response = requests.get(f"{AUTHENTICATION_SERVICE_URL}/api/lazada/access-token/{user_id}")
    return response.json()["accessToken"]


def get_user_id_by_seller_id(seller_id: str):
    response = requests.get(f"{AUTHENTICATION_SERVICE_URL}/api/lazada/user-id/{seller_id}")
    return response.json()["userId"]


def get_item_id_by_sku_id(sku_id):
    try:
        return InventoryService.get_item_id_by_sku_id(str(sku_id))["id"]
    except Exception as e:
        print(e)
        return -1


def get_iso_from_lazada_date(string):
    [date, time, tzd] = string.split()
    tzd = f"{tzd[:3]}:{tzd[3:]}"
    result = f"{date}T{time}{tzd}"
    return result


def create_or_update_order(body):
    seller_id = body["seller_id"]
    trade_order_id = body["data"]["trade_order_id"]
    order_status = body["data"]["order_status"]
    update_time = body["data"]["status_update_time"]
    user_id = get_user_id_by_seller_id(seller_id)
    
    refresh_items(user_id)

    existing_order = Order.get_one_by_trade_order_id(trade_order_id)
    # create
    if existing_order == None:
        order = get_order(trade_order_id, user_id)["data"]
        order_items = get_order_items(trade_order_id, user_id)["data"]

        new_order_items = []
        for order_item in order_items:
            item_id = get_item_id_by_sku_id(order_item["sku_id"])
            if item_id == -1: return {}
            new_order_items.append(
                {
                    "orderItemId": order_item["order_item_id"],
                    "item": {"id": item_id},
                    "itemPrice": order_item["item_price"],
                    "taxAmount": order_item["tax_amount"],
                    "buyerId": order_item["buyer_id"],
                    "shipmentProvider": order_item["shipment_provider"],
                    "trackingCode": order_item["tracking_code"],
                    "skuId": order_item["sku_id"],
                }
            )

        new_order = Order.Order(
            userId=user_id,
            platform=Platform.LAZADA,
            status=order_status,
            shippingFee=order["shipping_fee"],
            paymentMethod=order["payment_method"],
            orderId=trade_order_id,
            itemsCount=order["items_count"],
            price=order["price"],
            orderItems=new_order_items,
            createdAt=get_iso_from_lazada_date(order["created_at"]),
            updatedAt=get_iso_from_lazada_date(order["updated_at"]),
            addressBilling={
                "firstName": order["address_billing"]["first_name"],
                "postCode": order["address_billing"]["post_code"],
                "country": order["address_billing"]["country"],
                "city": order["address_billing"]["city"],
            },
            addressShipping={
                "firstName": order["address_shipping"]["first_name"],
                "postCode": order["address_shipping"]["post_code"],
                "country": order["address_shipping"]["country"],
                "city": order["address_shipping"]["city"],
            },
        )
        Order.delete_one_by_trade_order_id(trade_order_id)
        return Order.create(new_order)
    # update
    else:
        return Order.update_order_status_by_trade_order_id(
            trade_order_id, order_status, datetime.fromtimestamp(update_time)
        )
    
    


def get_order(order_id, user_id):
    access_token = get_access_token_by_user_id(user_id)
    request = lazop.LazopRequest("/order/get", "GET")
    request.add_api_param("order_id", order_id)
    response = client.execute(request, access_token)
    return response.body


def get_orders(user_id):
    access_token = get_access_token_by_user_id(user_id)
    request = lazop.LazopRequest("/orders/get", "GET")
    request.add_api_param("created_after", "1999-11-12T00:00:00")
    response = client.execute(request, access_token)
    return response.body


def get_order_items(order_id, user_id):
    access_token = get_access_token_by_user_id(user_id)
    request = lazop.LazopRequest("/order/items/get", "GET")
    request.add_api_param("order_id", order_id)
    response = client.execute(request, access_token)
    return response.body


def refresh_items(user_id):
    # return
    access_token = get_access_token_by_user_id(user_id)
    request = lazop.LazopRequest("/products/get", "GET")
    request.add_api_param("filter", "all")
    response = client.execute(request, access_token)
    
    if response.body["code"] != "0" : return
    
    quantities = []
    
    try:
        items = response.body["data"]["products"]
    except:
        print("error here")
        return
    
    for item in items:
        temp = {"itemId": str(item["item_id"]), "skus": []}
        for sku in item["skus"]:
            temp["skus"].append({
                "skuId": str(sku["SkuId"]),
                "quantity": str(sku["quantity"])
            })
        quantities.append(temp)
    return InventoryService.refresh_items(user_id, quantities)


def remove_item(request):
    print("removing")
    pass
