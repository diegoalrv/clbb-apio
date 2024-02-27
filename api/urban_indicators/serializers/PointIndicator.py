from rest_framework_gis import serializers
from urban_indicators.models.PointIndicator import PointIndicator

class PointIndicatorSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = PointIndicator
        fields = '__all__'
        geo_field = 'geo_field'
