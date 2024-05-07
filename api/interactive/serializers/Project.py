from rest_framework import serializers
from interactive.models.Project import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'