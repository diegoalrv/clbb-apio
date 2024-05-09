from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from interactive.models.Project import Project
from interactive.models.Scenario import Scenario
from interactive.models.Plate import Plate, PlateScenario
from interactive.serializers.Project import ProjectSerializer
from backend.serializers.AreaOfInterest import AreaOfInterestSerializer
from backend.models.DiscreteDistribution import DiscreteDistribution
from backend.models.Amenity import Amenity
from backend.serializers.DiscreteDistribution import DiscreteDistributionSerializer
from interactive.utils.config import data_mapping
from django.shortcuts import get_object_or_404
from django.db import transaction

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

    @action(detail=False, methods=['get'], url_path='get-project-id-by-name')
    def get_project_id_by_name(self, request):
        """
        Returns the project ID for a project with the specified name.
        """
        project_name = request.query_params.get('name')
        if not project_name:
            return Response({'error': 'Name parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            project = Project.objects.get(name=project_name)
            return Response({'project_id': project.id})
        except Project.DoesNotExist:
            return Response({'error': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True, methods=['get'], url_path='area-of-interest')
    def get_area_of_interest(self, request, pk=None):
        """
        Returns the area of interest associated with the specified project.
        """
        project = self.get_object()
        area_of_interest = project.area_of_interest
        if area_of_interest:
            serializer = AreaOfInterestSerializer(area_of_interest)
            return Response(serializer.data)
        else:
            return Response({'error': 'No area of interest associated with this project.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path='discrete-distributions')
    def get_discrete_distributions(self, request, pk=None):
        """
        Returns the discrete distributions associated with the specified project,
        with optional filtering by distribution type and level.
        """
        project = self.get_object()
        distributions = project.discrete_distributions.all()

        # Get filters from query parameters
        dist_type = request.query_params.get('dist_type')
        level = request.query_params.get('level')

        # Apply filters if provided
        if dist_type:
            distributions = distributions.filter(dist_type=dist_type)
        if level:
            distributions = distributions.filter(level=level)

        serializer = DiscreteDistributionSerializer(distributions, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='update-plate-scenarios')
    def update_plate_scenarios(self, request, pk=None):
        """
        Updates scenarios for all plates in the specified project based on provided scenario indices.
        """
        project = self.get_object()
        data = request.data  # data should be a dict where key is plate_id and value is the scenario index

        for plate_id, scenario_index in data.items():
            try:
                # Ensure the plate belongs to the project
                plate = project.plates.get(id=plate_id)
                scenarios = list(plate.platescenario_set.all())
                
                if scenario_index < len(scenarios):
                    # Set all to inactive then activate the selected one
                    for ps in scenarios:
                        ps.is_active = False
                        ps.save()

                    scenarios[scenario_index].is_active = True
                    scenarios[scenario_index].save()
                else:
                    return Response({'error': f'Invalid scenario index for plate {plate_id}'}, status=status.HTTP_400_BAD_REQUEST)
            except Plate.DoesNotExist:
                return Response({'error': f'Plate with id {plate_id} does not exist in this project'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Scenarios updated successfully for project plates'})

    @action(detail=True, methods=['post'], url_path='associate-amenities')
    def associate_amenities(self, request, pk=None):
        plate_id = request.data.get('plate_id')
        scenario_id = request.data.get('scenario_id')
        amenity_ids = request.data.get('amenity_ids', [])

        # Validar que el Plate y Scenario pertenecen al Project
        plate = get_object_or_404(Plate, id=plate_id, project=pk)
        scenario = get_object_or_404(Scenario, platescenario__plate=plate, id=scenario_id)

        # Encontrar las Amenities y asociarlas al Scenario
        with transaction.atomic():
            amenities = Amenity.objects.filter(id__in=amenity_ids)
            scenario.amenities.add(*amenities)
            scenario.save()

        return Response({'message': f'Amenities successfully associated with scenario {scenario_id} of plate {plate_id}'})

