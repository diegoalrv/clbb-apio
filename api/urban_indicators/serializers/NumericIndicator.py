from rest_framework import serializers
from urban_indicators.models.NumericIndicator import NumericIndicator

class NumericIndicatorSerializer(serializers.Serializer):
    class Meta:
        model = NumericIndicator
        fields = '__all__'