# serializers.py
from rest_framework import serializers
from backend.models.LandUse import LandUse

class LandUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandUse
        fields = '__all__'
        geo_field = 'geo_field'
