from rest_framework_gis import serializers
from backend.models.Amenity import Amenity

class AmenitySerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'
        geo_field = 'geo_field'