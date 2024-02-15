from rest_framework import viewsets
from backend.models.Amenity import Amenity
from backend.serializers.Amenity import AmenitySerializer

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer