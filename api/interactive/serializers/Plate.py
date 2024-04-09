from rest_framework_gis.serializers import GeoFeatureModelSerializer
from interactive.models.Plate import Plate

class PlateGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Plate
        fields = '__all__'
        geo_field = 'polygon'