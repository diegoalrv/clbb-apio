from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import Alert, Irregularity, Jams, Segment, AlertRecord, IrregularityRecord, JamRecord

class AlertSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Alert
        geo_field = "geometry"  # Define the geographic field
        fields = '__all__'

class IrregularitySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Irregularity
        geo_field = "geometry"  # Define the geographic field
        fields = '__all__'

class JamsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Jams
        geo_field = "geometry"  # Define the geographic field
        fields = '__all__'

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = '__all__'

class AlertRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertRecord
        fields = '__all__'

class IrregularityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrregularityRecord
        fields = '__all__'

class JamRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = JamRecord
        fields = '__all__'