from rest_framework.decorators import api_view
from rest_framework.response import Response

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
