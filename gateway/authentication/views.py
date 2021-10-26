from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from authentication.models import User
from authentication.serializers import UserSerializer
from utils.http_local import create_requests_with_header
from utils.auth import verify_token
from utils.decorators import jwt_verified
from rest_framework.decorators import api_view

import requests,os

# MUST implement authorization header for every path

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    r = create_requests_with_header(request)

    # GET list of users
    if request.method == 'GET':
        data = r.get('http://localhost:3001/api/user').json()
        # users_serializer = UserSerializer(data, many=True)
        return JsonResponse(data, safe=False)
        
        # email = request.GET.get('email', None)
        # if email is not None:
        #     users = users.filter(email__icontains=title)
        
        # users_serializer = UserSerializer(users, many=True)
        # return JsonResponse(users_serializer.data, safe=False)
    
    # POST a new user
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        created_user = r.post('http://localhost:3001/api/user',data=user_data).json()
        # user_serializer = UserSerializer(data=user_data)
        # if user_serializer.is_valid():
            # created_user = requests.post('http://localhost:3001/api/user',data=user_data).json()
            # user_serializer.save()
            # return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
            # return JsonResponse({'msg': 'yay'}, status=status.HTTP_201_CREATED) 
        return JsonResponse(created_user, status=status.HTTP_201_CREATED) 
        # return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE all users
    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
@jwt_verified(['PUT','DELETE'])
def user_detail(request, pk):

    r = create_requests_with_header(request)
    # find tutorial by pk (id)
    # try: 
    #     user = User.objects.get(pk=pk) 
    # except User.DoesNotExist: 
    #     return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    if request.method == 'GET':
        user = r.get(f'http://localhost:3001/api/user/{pk}').json()
        return JsonResponse(user)
        # user_serializer = UserSerializer(user) 
        # return JsonResponse(user_serializer.data)

    elif request.method == 'PUT':
        token = request.COOKIES.get('token')
        user_data = JSONParser().parse(request) 
        updated_user = r.put(f'http://localhost:3001/api/user/{pk}', data=user_data).json()
        return JsonResponse(updated_user)
        # user_serializer = UserSerializer(user, data=user_data) 
        # if user_serializer.is_valid(): 
        #     user_serializer.save() 
        #     return JsonResponse(user_serializer.data) 
        # return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        data = r.delete(f'http://localhost:3001/api/user/{pk}').json()
        return JsonResponse(data)

@api_view(['POST'])
def login(request):
    r = create_requests_with_header(request)
    if request.method == 'POST':
        credential = JSONParser().parse(request)
        data = r.post('http://localhost:3001/api/login',data=credential)
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
