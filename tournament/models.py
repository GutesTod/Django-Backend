from django.db import models
from prototype.models import EventUser
from django.utils.translation import gettext_lazy as _

class Tournament(models.Model):
    name = models.CharField(
        max_length = 100
    )
    count_users = models.IntegerField(
        default=0
    )
class Match(models.Model):
    match_id = models.IntegerField()
    user1_id = models.IntegerField(null=True)
    user2_id = models.IntegerField(null=True)
    tour_id = models.IntegerField(null=False)
    user1_goals = models.IntegerField(null=True)
    user2_goals = models.IntegerField(null=True)
    
    class EnumStage(models.TextChoices):
        START = 'ST', _('Start')
        HALF_FINAL = 'HF', _('Half-Final')
        FINAL = 'FI', _('Final')
        
    enum_stage = models.CharField(
        max_length = 2,
        choices = EnumStage.choices,
        default=EnumStage.START
    )
    is_end = models.BooleanField(default=False)

    
