from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from utils.decorators import jwt_verified

from inventory.adapter import InventoryService

InventoryService = InventoryService()


@api_view(["GET", "POST"])
@jwt_verified(["GET", "POST"])
# /inventory
def entry_list(request):
    user_id = str(request.decoded_user["id"])
    if request.method == "GET":
        entries = InventoryService.get_all_entries(user_id)
        return JsonResponse(entries)
    # elif request.method == "POST":
    #     data = JSONParser().parse(request)
    #     created_entry = stub.CreateEntry(merchy_pb2.Entry(**data, userId=user_id))
    #     created_entry = MessageToDict(created_entry)
    #     return JsonResponse(created_entry)


@api_view(["GET", "PUT", "DELETE"])
@jwt_verified(["GET", "PUT", "DELETE"])
# /inventory/:entry_id
def entry_detail(request, id):
    if request.method == "GET":
        entry = InventoryService.get_one_entry(id)
        return JsonResponse(entry)
    # elif request.method == "PUT":
    #     data = JSONParser().parse(request)
    #     updated_entry = stub.UpdateEntry(merchy_pb2.Entry(**data, id=id))
    #     updated_entry = MessageToDict(updated_entry)
    #     return JsonResponse(updated_entry)
    # elif request.method == "DELETE":
    #     response = stub.DeleteEntry(merchy_pb2.EntryId(id=id))
    #     response = MessageToDict(response)
    #     return JsonResponse(response)

@api_view(["GET", "POST"])
@jwt_verified(["GET", "POST"])
def item_list(request):
    user_id = str(request.decoded_user["id"])
    if request.method == "GET":
        items = InventoryService.get_all_items(user_id)
        return JsonResponse(items)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        created_item = InventoryService.create_item(user_id, data)
        return JsonResponse(created_item)

@api_view(["GET", "PUT", "DELETE"])
@jwt_verified(["GET", "PUT", "DELETE"])
def item_detail(request, id):
    if request.method == "GET":
        item = InventoryService.get_one_item(id)
        return JsonResponse(item)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        updated_item = InventoryService.update_item(id,data)
        return JsonResponse(updated_item)
    elif request.method == "DELETE":
        response = InventoryService.delete_item(id)
        return JsonResponse(response)
