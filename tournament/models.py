from django.db import models
from prototype.models import EventUser

class Tournament(models.Model):
    count_users = models.IntegerField(
        default=0
    )
class Match(models.Model):
    user1_id = models.IntegerField(null=True)
    user2_id = models.IntegerField(null=True)
    tour_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    user1_goals = models.IntegerField(null=True)
    user2_goals = models.IntegerField(null=True)

    
