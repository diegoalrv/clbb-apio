from rest_framework import viewsets
from backend.models.AreaOfInterest import AreaOfInterest
from backend.serializers.AreaOfInterest import AreaOfInterestSerializer

class AreaOfInterestViewSet(viewsets.ModelViewSet):
    queryset = AreaOfInterest.objects.all()
    serializer_class = AreaOfInterestSerializer