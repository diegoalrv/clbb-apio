# views.py
from rest_framework import viewsets
from interactive.models.Plate import Plate
from interactive.serializers.Plate import PlateGeoSerializer

class PlateViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateGeoSerializer
