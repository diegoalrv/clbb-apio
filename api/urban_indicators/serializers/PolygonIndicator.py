from rest_framework_gis import serializers
from urban_indicators.models.PolygonIndicator import PolygonIndicator

class PolygonIndicatorSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = PolygonIndicator
        fields = '__all__'
        geo_field = 'geo_field'