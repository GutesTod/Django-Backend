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

@api_view(['POST'])
def RegisterTournament(request):
    data = request.data["token"]
    if (TournamentsSingleton.register_tournament(data)):
        return Response({'status': 'OK'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def GetTournaments(request):
    data = request.data["token"]
    json_data = TournamentsSingleton.get_tournaments(token=data)
    return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        
 