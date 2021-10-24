from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from authentication.models import User
from authentication.serializers import UserSerializer
from rest_framework.decorators import api_view

import requests

# MUST implement authorization header for every path

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    auth = request.META.get('HTTP_AUTHORIZATION', '')
    headers = {'Authorization': auth}
    # GET list of users
    if request.method == 'GET':
        data = requests.get('http://localhost:3001/api/user', headers=headers).json()
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
        created_user = requests.post('http://localhost:3001/api/user',data=user_data, headers=headers).json()
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
def user_detail(request, pk):
    auth = request.META.get('HTTP_AUTHORIZATION', '')
    headers = {'Authorization': auth}
    # find tutorial by pk (id)
    # try: 
    #     user = User.objects.get(pk=pk) 
    # except User.DoesNotExist: 
    #     return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    if request.method == 'GET':
        user = requests.get(f'http://localhost:3001/api/user/{pk}', headers=headers).json()
        return JsonResponse(user)
        # user_serializer = UserSerializer(user) 
        # return JsonResponse(user_serializer.data)

    elif request.method == 'PUT': 
        user_data = JSONParser().parse(request) 
        updated_user = requests.put(f'http://localhost:3001/api/user/{pk}', data=user_data, headers=headers).json()
        return JsonResponse(updated_user)
        # user_serializer = UserSerializer(user, data=user_data) 
        # if user_serializer.is_valid(): 
        #     user_serializer.save() 
        #     return JsonResponse(user_serializer.data) 
        # return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        data = requests.delete(f'http://localhost:3001/api/user/{pk}', headers=headers).json()
        return JsonResponse(data)
        # user.delete() 
        # return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        credential = JSONParser().parse(request)
        data = requests.post('http://localhost:3001/api/login',data=credential).json()
        return JsonResponse(data)
