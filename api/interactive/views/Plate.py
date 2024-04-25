from rest_framework import viewsets
from interactive.models.Plate import Plate, PlateScenario
from interactive.serializers.Plate import PlateSerializer, PlateScenarioSerializer

class PlateViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer

class PlateScenarioViewSet(viewsets.ModelViewSet):
    queryset = PlateScenario.objects.all()
    serializer_class = PlateScenarioSerializer