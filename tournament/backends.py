from prototype.models import EventUser
from 

class PlayersMixin:
    def add_players(t_id: int = None, user_id: int = None):
        data = EventUser.objects.filter(tour_id = t_id, user = user_id)
        return data
    
    def 
    
        
            
                
                
    
class TournamentMixin:
    def generate_matchs():
        