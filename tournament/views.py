from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .backends import PlayersSingleton, MatchSingleton, TournamentsSingleton
        
@api_view(['GET'])
def GetMatchs(request):
    data = MatchSingleton.get_matchs(t_id=request.data['id'])
    if data != False:
        return Response(data=data, status=status.HTTP_200_OK)
    return Response({'status': 'error!', 'result': data}, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['POST'])
#def MakeMatchs(request):
    #if