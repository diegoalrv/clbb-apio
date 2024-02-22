from rest_framework_gis import serializers
from urban_indicators.models.LineIndicator import LineIndicator

class LineIndicatorSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = LineIndicator
        fields = '__all__'
        geo_field = 'geo_field'