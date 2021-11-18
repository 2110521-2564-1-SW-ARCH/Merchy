import grpc
import requests
import os
from inventory import merchy_pb2, merchy_pb2_grpc
from google.protobuf.json_format import MessageToDict, MessageToJson



class InventoryService:
    def __init__(self):
        channel = grpc.insecure_channel("127.0.0.1:3002")  # should be closed by channel.close()
        self.stub = merchy_pb2_grpc.InventoryServiceStub(channel)

    ##### Utility Function for Items #####

    def get_all_items(self, user_id):
        items = self.stub.GetAllItems(merchy_pb2.UserId(userId=user_id))
        items = MessageToDict(items)
        return items

    def get_one_item(self,item_id):
        item = self.stub.GetItem(merchy_pb2.ItemId(id=id))
        item = MessageToDict(item)
        return item

    def create_item(self, user_id, data):
        created_item = self.stub.CreateItem(merchy_pb2.Item(**data, userId=user_id))
        created_item = MessageToDict(created_item)
        return created_item

    def update_item(self,item_id,data):
        updated_item = self.stub.UpdateItem(merchy_pb2.Item(**data, id=item_id))
        updated_item = MessageToDict(updated_item)
        return updated_item

    def delete_item(self,item_id):
        response = self.stub.DeleteItem(merchy_pb2.ItemId(id=item_id))
        response = MessageToDict(response)
        return response


class OrderService:
    order_tracking_url: str

    def __init__(self):
        order_tracking_service_ip = os.getenv("ORDER_TRACKING_SERVICE_IP")
        order_tracking_service_port = os.getenv("ORDER_TRACKING_SERVICE_PORT")
        order_tracking_service_protocol = os.getenv("ORDER_TRACKING_SERVICE_PROTOCOL")
        self.order_tracking_service_url = f"{order_tracking_service_protocol}://{order_tracking_service_ip}:{order_tracking_service_port}"

    ##### Utility Function for Items #####

    def get_all_orders(self, user_id):
        orders = requests.get(f"{self.order_tracking_service_url}/orders", params={"user_id": user_id})
        return orders.json()

    def get_one_order(self, order_id):
        pass