from rest_framework import serializers
from interactive.models.Scenario import Scenario
from backend.serializers import Amenity, AreaOfInterest, GreenArea

class ScenarioSerializer(serializers.ModelSerializer):
    amenities = Amenity.AmenitySerializer(many=True, read_only=True)
    green_areas = GreenArea.GreenAreaSerializer(many=True, read_only=True)
    area_of_interest = AreaOfInterest.AreaOfInterestSerializer(many=True, read_only=True)

    class Meta:
        model = Scenario
        fields = '__all__'
