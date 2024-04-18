from rest_framework_gis import serializers
from api.backend.models.GreenArea import GreenArea

class GreenAreaSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = GreenArea
        fields = '__all__'
        geo_field = 'geometry'