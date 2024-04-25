from rest_framework import serializers
from interactive.models.Plate import Plate, PlateScenario

class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = '__all__'

class PlateScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlateScenario
        fields = '__all__'