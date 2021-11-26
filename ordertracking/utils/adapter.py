import grpc
import os
import merchy_pb2, merchy_pb2_grpc
from google.protobuf.json_format import MessageToDict


class InventoryService:
    def __init__(self):
        inventory_service_ip = os.getenv("INVENTORY_SERVICE_IP")
        inventory_service_port = os.getenv("INVENTORY_SERVICE_PORT")
        inventory_service_url = f"{inventory_service_ip}:{inventory_service_port}"
        channel = grpc.insecure_channel(
            inventory_service_url
        )  # should be closed by channel.close()
        self.stub = merchy_pb2_grpc.InventoryServiceStub(channel)

    ##### Utility Function for Items #####

    def get_all_items(self, user_id):
        items = self.stub.GetAllItems(merchy_pb2.UserId(userId=user_id))
        items = MessageToDict(items)
        return items

    def get_one_item(self, item_id):
        item = self.stub.GetItem(merchy_pb2.ItemId(id=item_id))
        item = MessageToDict(item)
        return item

    def create_item(self, user_id, data):
        created_item = self.stub.CreateItem(merchy_pb2.Item(**data, userId=user_id))
        created_item = MessageToDict(created_item)
        return created_item

    def update_item(self, item_id, data):
        updated_item = self.stub.UpdateItem(merchy_pb2.Item(**data, id=item_id))
        updated_item = MessageToDict(updated_item)
        return updated_item

    def delete_item(self, item_id):
        response = self.stub.DeleteItem(merchy_pb2.ItemId(id=item_id))
        response = MessageToDict(response)
        return response

    def get_item_id_by_sku_id(self, sku_id):
        response = self.stub.GetItemIdBySkuId(merchy_pb2.SkuId(id=sku_id))
        response = MessageToDict(response)
        return response
    
    
    def refresh_items(self, item_id, quantities):
        response = self.stub.RefreshItems(merchy_pb2.RefreshItemList(itemList=quantities))
        response = MessageToDict(response)
        return response