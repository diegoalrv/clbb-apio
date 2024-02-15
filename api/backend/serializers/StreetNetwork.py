from rest_framework_gis import serializers
from backend.models.StreetNetwork import StreetNetwork

class StreetNetworkSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = StreetNetwork
        fields = '__all__'