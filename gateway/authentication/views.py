from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from utils.auth import verify_token
from utils.decorators import jwt_verified
from rest_framework.decorators import api_view
from authentication.adapter import AuthService

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
 
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        credential = JSONParser().parse(request)
        data = AuthService.login(credential)
        if data.text == "Unauthorized": return JsonResponse({"message": data.text}, status=401)
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

@api_view(['GET'])
@jwt_verified(['GET'])
def get_lazada_login_link(request):
    user_id = str(request.decoded_user["id"])
    data = AuthService.get_lazada_login_link(user_id)
    return JsonResponse(data)

@api_view(['GET'])
@jwt_verified(['GET'])
def get_lazada_access_token(request):
    user_id = str(request.decoded_user["id"])
    data = AuthService.get_lazada_access_token(user_id)
    return JsonResponse(data)
    
@api_view(['GET'])
@jwt_verified(['GET'])
def get_lazada_seller_id(request):
    user_id = str(request.decoded_user["id"])
    data = AuthService.get_lazada_seller_id(user_id)
    return JsonResponse(data)
