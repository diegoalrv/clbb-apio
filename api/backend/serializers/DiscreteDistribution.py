from rest_framework_gis import serializers
from backend.models.DiscreteDistribution import DiscreteDistribution

class DiscreteDistributionSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = DiscreteDistribution
        fields = '__all__'
        geo_field = 'geo_field'