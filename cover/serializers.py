from rest_framework import serializers
from .models import Cover

class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = ('__all__')