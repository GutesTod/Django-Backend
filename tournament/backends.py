from prototype.models import EventUser
from tournament.models import Tournament, Match
from prototype.models import EventUser
import json

class PlayersSingleton:
    def add_player_to_match(t_id: int = None, user_id: int = None):
        data_player = EventUser.objects.filter(tour_id = t_id, user = user_id)
        if data_player.exists():
            for match in Match.objects.filter(tour_id=t_id, enum_stage="ST"):
                if match.user1_id == None:
                    Match.objects.filter(tour_id=t_id, match_id=match.pk).update(user1_id = user_id)
                    return True
                elif match.user2_id == None:
                    Match.objects.filter(tour_id=t_id, match_id=match).update(user2_id = user_id)
                    return True
        return False
    
    def add_player_to_stage(t_id: int = None, user_id: int = None, to_stage: str = None, from_stage: str = None):
        for match in Match.objects.filter(tour_id=t_id, enum_stage=from_stage): 
            if match.is_end == True and match.user1_goals > match.user2_goals:
                Match.objects.filter(tour_id=t_id, match_id=match.pk, enum_stage=to_stage).update(user1_id = user_id)
                return True
            elif match.user2_id == None and match.user1_goals > match.user2_goals:
                Match.objects.filter(tour_id=t_id, match_id=match.pk, enum_stage=to_stage).update(user2_id = user_id)
                return True
        return False
    
class MatchMixin:
    def make_matchs(t_id: int = None):
        if t_id:
            for count in range(1,5):
                Match.objects.create(match_id=count, tour_id = t_id, enum_stage="ST")
            for count in range(5,7):
                Match.objects.create(match_id=count, tour_id = t_id, enum_stage="HF")
            Match.objects.create(match_id=count, tour_id = t_id, enum_stage="FI")
        else:
            return False
    def get_matchs(t_id: int = None):
        data_get = Match.objects.filter(tour_id = t_id).values()
        return json.dumps(data_get)
    