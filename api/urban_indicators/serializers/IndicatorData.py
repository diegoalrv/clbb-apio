from rest_framework_gis import serializers
from urban_indicators.models.IndicatorData import IndicatorData

class IndicatorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicatorData
        fields = '__all__'