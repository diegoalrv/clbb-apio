# views.py
from rest_framework import viewsets
from backend.models.Plate import Plate
from backend.serializers.Plate import PlateGeoSerializer

class PlateViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateGeoSerializer
