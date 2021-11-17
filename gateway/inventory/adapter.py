import grpc
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

    ##### Utility Function for Entry #####

    def get_all_entries(self,user_id):
        entries = self.stub.GetAllEntries(merchy_pb2.UserId(userId=user_id))
        entries = MessageToDict(entries)
        return entries

    def get_one_entry(self,entry_id):
        entry = self.stub.GetEntry(merchy_pb2.EntryId(id=id))
        entry = MessageToDict(entry)
        return entry
