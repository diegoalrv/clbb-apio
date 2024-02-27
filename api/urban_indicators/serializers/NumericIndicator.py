from rest_framework_gis import serializers
from urban_indicators.models.NumericIndicator import NumericIndicator

class NumericIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumericIndicator
        fields = '__all__'