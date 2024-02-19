from rest_framework_gis import serializers
from backend.models.RoadNetwork import RoadNetwork, Street, Node

class NodeSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'
        geo_field = 'geo_field'
        

class StreetSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'
        geo_field = 'geo_field'


class RoadNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadNetwork
        fields = '__all__'