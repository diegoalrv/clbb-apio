from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from interactive.models.Project import Project
from interactive.models.Plate import PlateScenario
from interactive.serializers.Project import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['get'], url_path='project-status')
    def get_project_status(self, request, pk=None):
        """
        Returns a dictionary where keys are the plate IDs and values are the indices of the currently active scenario.
        Assumes there is always one active scenario per plate.
        """
        project = self.get_object()
        plates = project.plates.all()
        project_status = {}
        
        for plate in plates:
            # Obtener directamente el Scenario activo, asumiendo que siempre hay uno.
            active_scenario = PlateScenario.objects.get(plate=plate, is_active=True)
            project_status[str(plate.id)] = active_scenario.scenario.id
        
        return Response(project_status)