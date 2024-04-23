from rest_framework import viewsets
from interactive.models.Scenario import Scenario
from interactive.serializers.Scenario import ScenarioSerializer

class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
