from rest_framework import viewsets
from backend.models.StreetNetwork import StreetNetwork
from backend.serializers.StreetNetwork import StreetNetworkSerializer

class StreetNetworkViewSet(viewsets.ModelViewSet):
    queryset = StreetNetwork.objects.all()
    serializer_class = StreetNetworkSerializer