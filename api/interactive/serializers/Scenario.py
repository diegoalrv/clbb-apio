from rest_framework_gis import serializers
from interactive.models.Scenario import Scenario

class ScenarioSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'
