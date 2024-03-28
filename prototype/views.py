import uuid
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_users': '/',
        'Search by Id': '/?id=tmp_id',
        'Add': '/add',
        'Update': '/update/pk',
        'Delete': '/user/pk/delete'
    }
 
    return Response(api_urls)

@api_view(['GET'])
def GetUsers(request):
    users_on = User.objects.all()
    serializer = UserSerializer(users_on, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def AddUsers(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        User.objects.create(
            id = uuid.uuid4(),
            name = serializer.data['name'],
            surname = serializer.data['surname'],
            hashed_password = serializer.data['hashed_password']
        )
        return Response(data = serializer.data ,status = status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DelUser(request):
    if User.objects.filter(name = request.data['name']):
        user = User.objects.get(name=request.data['name'])
        user.delete()
        return Response(status= status.HTTP_200_OK)
    else:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def FindUser(request):
    if User.objects.filter(name = request.data['name']):
        user = User.objects.get(name = request.data['name'])
        data_json = {
            'name' : user.name,
            'surname' : user.surname,
            'hashed_password' : user.hashed_password
        }
        return Response(data = data_json, status= status.HTTP_200_OK)
    else:
        return Response(data = 'User not found', status=status.HTTP_400_BAD_REQUEST)