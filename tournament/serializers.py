from rest_framework import serializers
from .models import Tournament, Match
from prototype.models import EventUser
from .backends import PlayersMixin

class RegistrationTournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ('name',)

    def create(self, validated_data):
        return Tournament.objects.create_user(**validated_data)
    
class CreateMatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Match
        fields = ('tour_id', 'enum_stage')
    
    def create(self, validated_data):
        return Match.objects.create_user(**validated_data) 
    
class AddPlayerToMatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Match
        fields = ()
        