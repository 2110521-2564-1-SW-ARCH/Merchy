from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from utils.decorators import jwt_verified
from utils.http_common import create_requests_with_header
from ordertracking.adapter import OrderService

OrderService = OrderService()


@api_view(['POST'])
@jwt_verified(["GET", "POST"])
def shipping_status_list(request):
    if request.method == 'POST':
        body = JSONParser().parse(request)
        barcodes = body['barcodes']
        params = {"barcodes": barcodes}
        
        r = create_requests_with_header(request)
        data = r.get(f'http://localhost:3003/trackbybarcodes/thpost', params=params).json()
        return JsonResponse(data, safe=False)


@api_view(["GET", "POST"])
@jwt_verified(["GET", "POST"])
def order_list(request):
    user_id = str(request.decoded_user["id"])
    if request.method == "GET":
        orders = OrderService.get_all_orders(user_id)
        return JsonResponse(orders, safe=False)


@api_view(["GET", "PUT", "DELETE"])
@jwt_verified(["GET", "PUT", "DELETE"])
def order_detail(request, id):
    if request.method == "GET":
        order = OrderService.get_one_order(id)
        return JsonResponse(order, safe=False)
