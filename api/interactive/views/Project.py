from rest_framework import viewsets
from interactive.models.Project import Project
from interactive.serializers.Project import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer