from rest_framework import routers, serializers, viewsets
from .models import User

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'hashed_password']