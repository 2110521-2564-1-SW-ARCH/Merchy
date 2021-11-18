from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from utils.http_common import create_requests_with_header

# body
# {
#     barcodes: []
# }

@api_view(['POST'])
def get_ordertracking_detail(request):
    if request.method == 'POST':
        body = JSONParser().parse(request)
        barcodes = body['barcodes']
        params = {"barcodes": barcodes}
        
        r = create_requests_with_header(request)
        data = r.get(f'http://localhost:3003/trackbybarcodes/thpost', params=params).json()
        return JsonResponse(data, safe=False)
    