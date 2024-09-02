from rest_framework import serializers
from .models import Movidata

class MoviSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movidata

        fields = ['id', 'name', 'duration', 'rating', 'image']