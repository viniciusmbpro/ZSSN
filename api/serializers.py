from rest_framework import serializers
from .models import Survivor

class SurvivorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = ('id', 'name', 'age', 'sex', 'latitude', 'longitude', 'infected', 'points', 'reports', 'water', 'food', 'medication', 'ammunition')