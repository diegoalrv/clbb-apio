from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from interactive.models.Plate import Plate, PlateScenario
from interactive.serializers.Plate import PlateSerializer, PlateScenarioSerializer

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
                    # Desactivar todos los escenarios primero
                    for ps in scenarios:
                        ps.is_active = False
                        ps.save()

                    # Activar el escenario seleccionado
                    scenarios[scenario_index].is_active = True
                    scenarios[scenario_index].save()
                else:
                    return Response({'error': f'Invalid scenario index for plate {plate_id}'}, status=status.HTTP_400_BAD_REQUEST)
            except Plate.DoesNotExist:
                return Response({'error': f'Plate with id {plate_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Scenarios updated successfully'})
    
class PlateScenarioViewSet(viewsets.ModelViewSet):
    queryset = PlateScenario.objects.all()
    serializer_class = PlateScenarioSerializer