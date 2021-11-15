from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from authentication.models import User
from authentication.serializers import UserSerializer
from utils.http_local import create_requests_with_header, AuthService
from utils.auth import verify_token
from utils.decorators import jwt_verified
from rest_framework.decorators import api_view

import requests,os

# MUST implement authorization header for every path

AuthService = AuthService()

# /user one_user
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@jwt_verified(['GET', 'PUT', 'DELETE'])
def user_list(request):
    id = request.decoded_user["id"] if request.decoded_user else None
    
    if request.method == 'GET':
        data = AuthService.get_one_user(id)
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        created_user = AuthService.create_user(user_data)
        return JsonResponse(created_user, status=status.HTTP_201_CREATED) 

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request) 
        updated_user = AuthService.update_user(id, user_data)
        return JsonResponse(updated_user)

    elif request.method == 'DELETE':
        data = AuthService.delete_user(id)
        return JsonResponse(data)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
@jwt_verified(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    r = create_requests_with_header(request)
 
    # GET / PUT / DELETE
    if request.method == 'GET':
        user = r.get(f'http://localhost:3001/api/user/{pk}').json()
        return JsonResponse(user)

    elif request.method == 'PUT':
        token = request.COOKIES.get('token')
        user_data = JSONParser().parse(request) 
        updated_user = r.put(f'http://localhost:3001/api/user/{pk}', data=user_data).json()
        return JsonResponse(updated_user)

    elif request.method == 'DELETE': 
        data = r.delete(f'http://localhost:3001/api/user/{pk}').json()
        return JsonResponse(data)

@api_view(['POST'])
def login(request):
    r = create_requests_with_header(request)
    if request.method == 'POST':
        credential = JSONParser().parse(request)
        data = AuthService.login(credential)
        # data = r.post('http://localhost:3001/api/login',data=credential)
        if data.text == "Unauthorized": return JsonResponse({"message": data.text})
        else: 
            response = JsonResponse(data.json())
            token = data.json()['token']
            response.set_cookie(key='token', value=token)
            return response

@api_view(['GET'])
def logout(request):
    response = JsonResponse({'message': "Logout sucessful"})
    response.delete_cookie('token')
    return response
