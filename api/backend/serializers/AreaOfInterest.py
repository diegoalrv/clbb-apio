from rest_framework_gis import serializers
from backend.models.AreaOfInterest import AreaOfInterest

class AreaOfInterestSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = AreaOfInterest
        fields = '__all__'
        geo_field = 'geo_field'