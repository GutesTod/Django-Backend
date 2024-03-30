import json

from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status

from .backends import PlayersSingleton, MatchSingleton, TournamentsSingleton
        
@api_view(['POST'])
def GetMatchs(request):
    data = MatchSingleton.get_matchs(t_id=request.data['id'])
    if data != False:
        return Response(data=data, status=status.HTTP_200_OK)
    return Response({'status': 'error!', 'result': data}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def RegisterTournament(request):
    data = request.data["token"]
    data_name = request.data['name']
    if (TournamentsSingleton.register_tournament(data, data_name)):
        return Response(json.dumps({'status': 'OK'}), status=status.HTTP_201_CREATED)
    else:
        return Response(json.dumps({'status': 'error'}), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def GetTournamentsById(request):
    data = request.data['token']
    json_data = TournamentsSingleton.get_tournaments(token=data)
    return Response(json_data, status=status.HTTP_200_OK)

@api_view(['POST'])
def GetTournaments(request):
    json_data = TournamentsSingleton.get_tournaments()
    return JsonResponse(json_data, safe=False)
        
@api_view(['POST'])
def AddPlayersToMatch(request):
    if(PlayersSingleton.add_player_to_match(t_id=request.data['tour_id'], token=request.data['token'])):
        return Response({'status': 'OK'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def AddPlayersToStage(request):
    if(PlayersSingleton.add_player_to_stage(
        t_id = request.data['tour_id'],
        token = request.data['token'],
        to_stage = request.data['to_stage'],
        from_stage = request.data['from_stage']
    )):
        return Response({'status': 'OK'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)