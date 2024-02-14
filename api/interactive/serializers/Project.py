from rest_framework_gis import serializers
from interactive.models.Project import Project

class ProjectSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'