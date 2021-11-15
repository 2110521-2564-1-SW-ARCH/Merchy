#  for grpc
import grpc
from inventory import merchy_pb2, merchy_pb2_grpc
from google.protobuf.json_format import MessageToDict, MessageToJson

channel = grpc.insecure_channel("127.0.0.1:3002")  # should be closed by channel.close()
stub = merchy_pb2_grpc.InventoryServiceStub(channel)

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from utils.decorators import jwt_verified


@api_view(["GET", "POST"])
@jwt_verified(["GET", "POST"])
# /inventory
def entry_list(request):
    user_id = str(request.decoded_user["id"])
    if request.method == "GET":
        entries = stub.GetAllEntries(merchy_pb2.UserId(id=user_id))
        entries = MessageToDict(entries)
        return JsonResponse(entries)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        created_entry = stub.CreateEntry(merchy_pb2.Entry(**data, userId=user_id))
        created_entry = MessageToDict(created_entry)
        return JsonResponse(created_entry)


@api_view(["GET", "PUT", "DELETE"])
@jwt_verified(["GET", "PUT", "DELETE"])
# /inventory/:entry_id
def entry_detail(request, id):
    if request.method == "GET":
        entry = stub.GetEntry(merchy_pb2.EntryId(id=id))
        entry = MessageToDict(entry)
        return JsonResponse(entry)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        updated_entry = stub.UpdateEntry(merchy_pb2.Entry(**data, id=id))
        updated_entry = MessageToDict(updated_entry)
        return JsonResponse(updated_entry)
    elif request.method == "DELETE":
        response = stub.DeleteEntry(merchy_pb2.EntryId(id=id))
        response = MessageToDict(response)
        return JsonResponse(response)


@api_view(["GET", "POST"])
@jwt_verified(["GET", "POST"])
def item_list(request):
    user_id = str(request.decoded_user["id"])
    if request.method == "GET":
        items = stub.GetAllItems(merchy_pb2.UserId(id=user_id))
        items = MessageToDict(items)
        return JsonResponse(items)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        created_item = stub.CreateItem(merchy_pb2.Item(**data, userId=user_id)) 
        created_item = MessageToDict(created_item)
        return JsonResponse(created_item)


@api_view(["GET", "PUT", "DELETE"])
@jwt_verified(["GET", "PUT", "DELETE"])
def item_detail(request, id):
    if request.method == "GET":
        item = stub.GetItem(merchy_pb2.ItemId(id=id))
        item = MessageToDict(item)
        return JsonResponse(item)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        updated_item = stub.UpdateItem(merchy_pb2.Item(**data, id=id))
        updated_item = MessageToDict(updated_item)
        return JsonResponse(updated_item)
    elif request.method == "DELETE":
        response = stub.DeleteItem(merchy_pb2.ItemId(id=id))
        response = MessageToDict(response)
        return JsonResponse(response)
