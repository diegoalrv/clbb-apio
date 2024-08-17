from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from interactive.models.Plate import Plate, PlateScenario
from interactive.serializers.Plate import PlateSerializer, PlateScenarioSerializer
from interactive.serializers.Scenario import ScenarioSerializer
from interactive.forms.PlateForm import PlateForm, AssociatePlateForm
from django.contrib.gis.geos import GEOSGeometry
import json

class PlateViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer

    @action(detail=False, methods=['post'], url_path='update-plate-scenarios')
    def update_plate_scenarios(self, request):
        data = request.data  # Asegúrate de recibir un JSON válido

        for plate_id, scenario_index in data.items():
            try:
                plate = self.get_queryset().get(id=plate_id)
                scenarios = list(plate.platescenario_set.all())
                if scenario_index < len(scenarios):
                    for ps in scenarios:
                        ps.is_active = False
                        ps.save()

                    scenarios[scenario_index].is_active = True
                    scenarios[scenario_index].save()
                else:
                    return Response({'error': f'Invalid scenario index for plate {plate_id}'}, status=status.HTTP_400_BAD_REQUEST)
            except Plate.DoesNotExist:
                return Response({'error': f'Plate with id {plate_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Scenarios updated successfully'})

    @action(detail=True, methods=['get'], url_path='scenarios')
    def get_scenarios(self, request, pk=None):
        """
        Returns all scenarios associated with a specific plate.
        """
        plate = self.get_object()
        scenarios = [ps.scenario for ps in PlateScenario.objects.filter(plate=plate)]
        serializer = ScenarioSerializer(scenarios, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'], url_path='create')
    @csrf_exempt
    def create_plate(self, request):
        form = PlateForm(request.data, request.FILES)
        if form.is_valid():
            plate = form.save()
            return JsonResponse({'success': True, 'plate': {'id': plate.id, 'name': plate.name}})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    @action(detail=False, methods=['post'], url_path='associate')
    @csrf_exempt
    def associate_plate(self, request):
        form = AssociatePlateForm(request.data, request.FILES)
        if form.is_valid():
            action_choice = form.cleaned_data['action_choice']
            project = form.cleaned_data['project']
            if action_choice == 'select':
                plate = form.cleaned_data['plate']
                project.plates.add(plate)
                message = f'Plate {plate.name} associated with Project {project.name}'
            elif action_choice == 'upload':
                upload_geojson = request.FILES.get('upload_geojson')
                if upload_geojson:
                    import geopandas as gpd
                    # Parse the uploaded GeoJSON
                    gdf = gpd.read_file(upload_geojson)
                    try:
                        name = gdf['name'][0]
                    except KeyError:
                        name = form.cleaned_data.get('name')

                    geometry = gdf['geometry'][0]
                    geometry = GEOSGeometry(json.dumps(geometry.__geo_interface__))
                    plate = Plate.objects.create(name=name, geometry=geometry)
                    project.plates.add(plate)
                    message = f'New Plate {plate.name} created and associated with Project {project.name}'
                else:
                    return JsonResponse({'success': False, 'errors': {'upload_geojson': ['This field is required.']}}, status=400)
            else:
                return JsonResponse({'success': False, 'errors': {'action_choice': ['Invalid choice']}}, status=400)

            return JsonResponse({'success': True, 'message': message})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
        
class PlateScenarioViewSet(viewsets.ModelViewSet):
    queryset = PlateScenario.objects.all()
    serializer_class = PlateScenarioSerializer