# views.py
from rest_framework import viewsets
from backend.models.LandUse import LandUse
from backend.serializers.LandUse import LandUseSerializer

class LandUseViewSet(viewsets.ModelViewSet):
    queryset = LandUse.objects.all()
    serializer_class = LandUseSerializer
