from rest_framework import serializers
from interactive.models.Scenario import Scenario

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'
