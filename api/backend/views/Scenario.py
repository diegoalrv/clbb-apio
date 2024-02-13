# views.py
from rest_framework import viewsets
from backend.models.Scenario import Scenario
from backend.serializers.Scenario import ScenarioSerializer

class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
