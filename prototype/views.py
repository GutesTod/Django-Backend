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
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
