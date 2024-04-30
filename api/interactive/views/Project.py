from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from interactive.models.Project import Project
from interactive.models.Plate import PlateScenario
from interactive.serializers.Project import ProjectSerializer
from interactive.utils.config import data_mapping

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
            active_scenario = PlateScenario.objects.get(plate=plate, is_active=True)
            project_status[str(plate.id)] = active_scenario.scenario.id
        
        return Response(project_status)

    @action(detail=True, methods=['get'], url_path='get-data/(?P<data_type>[^/.]+)')
    def get_data(self, request, pk=None, data_type=None):
        """
        Returns data of the specified type from all active scenarios within the plates of the project.
        """
        project = self.get_object()
        active_scenarios = PlateScenario.objects.filter(
            plate__project=project,
            is_active=True
        ).select_related('scenario')

        if data_type in data_mapping:
            model = data_mapping[data_type]['model']
            serializer_class = data_mapping[data_type]['serializer']
            
            # Collecting all data items from active scenarios
            data_items = set()
            for ps in active_scenarios:
                items = getattr(ps.scenario, data_type).all()
                for item in items:
                    data_items.add(item)
            
            data = serializer_class(list(data_items), many=True).data
            return Response(data)
        else:
            return Response({"error": "Invalid data type"}, status=status.HTTP_400_BAD_REQUEST)
