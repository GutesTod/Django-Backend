from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .backends import PlayersSingleton

class AddPlayersAPIView(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Добавляет игрока в сетку турнира
        """
        if (PlayersSingleton.add_player_to_match(
            t_id=request.data['t_id'],
            user_id=request.data['user_id']
        )):   
            return Response({"status": "OK"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)