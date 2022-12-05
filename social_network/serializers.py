from rest_framework import serializers
from .models import SocialNetwork, Antimatter, Universe, Unity

class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ('__all__')


class AntimatterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antimatter
        fields = ('__all__')

class UniverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universe
        fields = ('__all__')

class UnitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Unity
        fields = ('__all__')
