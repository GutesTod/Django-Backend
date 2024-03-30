import jwt
from prototype.models import EventUser
from tournament.models import Tournament, Match
from django.conf import settings
import json

class PlayersSingleton:
    def add_player_to_match(t_id: int = None, token: str = None):
        user_id = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])['id']
        data_player = EventUser.objects.create(tour = Tournament.objects.get(pk=t_id), user_id = user_id, is_staff = False)
        for match in Match.objects.filter(tour_id=t_id, enum_stage="ST"):
            if match.user1_id == None and data_player.is_staff == False:
                obj = Match.objects.get(tour_id=t_id, match_id=match.match_id)
                obj.user1_id = user_id
                obj.save()
                return True
            elif match.user2_id == None and data_player.is_staff == False:
                obj = Match.objects.get(tour_id=t_id, match_id=match.match_id)
                obj.user2_id = user_id
                obj.save()
                return True
        return False
    
    def add_player_to_stage(t_id: int = None, token: str = None, to_stage: str = None, from_stage: str = None):
        user_id = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])['id']
        data_player = EventUser.objects.get(user_id = user_id)
        for match in Match.objects.filter(tour_id=t_id, enum_stage=from_stage): 
            if match.is_end == True and match.user1_goals > match.user2_goals:
                for match_to in Match.objects.filter(tour_id=t_id, enum_stage=to_stage):
                    if match_to.user1_id == None and data_player.is_staff == False:
                        obj = Match.objects.get(tour_id=t_id, match_id=match_to.match_id, enum_stage=to_stage)
                        obj.user1_id = user_id
                        obj.save()
                        return True
            elif match.is_end == True and match.user1_goals < match.user2_goals:
                for match_to in Match.objects.filter(tour_id=t_id, enum_stage=to_stage):
                    if match_to.user2_id == None and data_player.is_staff == False:
                        obj = Match.objects.get(tour_id=t_id, match_id=match.match_id, enum_stage=to_stage)
                        obj.user2_id = user_id
                        obj.save()
                        return True
        return False
    
class MatchSingleton:
    def match_exists(t_id: int = None):
        if (Match.objects.filter(tour_id = t_id).exists()):
            return True
        else:
            return False
    def make_matchs(t_id: int = None):
        if t_id:
            for count in range(1,5):
                Match.objects.create(match_id=count, tour_id = t_id, enum_stage="ST")
            for count in range(5,7):
                Match.objects.create(match_id=count, tour_id = t_id, enum_stage="HF")
            Match.objects.create(match_id=7, tour_id = t_id, enum_stage="FI")
        else:
            return False
    def get_matchs(t_id: int = None):
        data_json = []
        data_get = Match.objects.filter(tour_id = t_id)
        for data in data_get:
            data_json.append(
                {
                    "match_id" : data.match_id,
                    "user1_id" : data.user1_id,
                    "user2_id" : data.user1_id,
                    "tour_id" : data.tour_id,
                    "user1_goals" : data.user1_goals,
                    "user2_goals" : data.user2_goals,
                    "enum_stage" : data.enum_stage
                }
            )
        return data_json
    
class TournamentsSingleton:
    def get_tournaments(token = None):
        tournaments = []
        if token:
            owner_data = EventUser.objects.filter(
                is_staff = True, 
                user_id = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])['id']
            )
            for data in owner_data:
                tournaments.append({
                    "tour_id" : data.tour.pk, 
                    "is_end" : data.tour.is_end, 
                    "count_users" : data.tour.count_users,
                    "name" : data.tour.name
                })
            return tournaments
        objs = Tournament.objects.all()
        for obj in objs:
            tournaments.append({
                    "tour_id" : obj.pk, 
                    "is_end" : obj.is_end, 
                    "count_users" : obj.count_users,
                    "name" : obj.name
                })
        return tournaments
    
    def register_tournament(token = None, tour_name = None):
        if token:
            tour = Tournament.objects.create(
                name = tour_name
            )
            tour_id_tmp = tour.pk
            EventUser.objects.create(
                tour = tour,
                is_staff = True,
                user_id = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])['id']
            )
            MatchSingleton.make_matchs(t_id=tour_id_tmp)
            return True
        else:
            return False
