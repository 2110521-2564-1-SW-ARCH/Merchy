from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from utils.decorators import jwt_verified

from inventory.adapter import InventoryService

InventoryService = InventoryService()


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
        updated_item = InventoryService.update_item(id, data)
        return JsonResponse(updated_item)
    elif request.method == "DELETE":
        response = InventoryService.delete_item(id)
        return JsonResponse(response)
