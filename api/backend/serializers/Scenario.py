# serializers.py
from rest_framework_gis import serializers
from backend.models.Scenario import Scenario

class ScenarioSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'
