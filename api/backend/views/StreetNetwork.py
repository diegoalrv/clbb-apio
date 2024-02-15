from rest_framework import viewsets
from backend.models.StreetNetwork import StreetNetwork, Street, Node
from backend.serializers.StreetNetwork import StreetNetworkSerializer, StreetSerializer, NodeSerializer

class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    
class StreetNetworkViewSet(viewsets.ModelViewSet):
    queryset = StreetNetwork.objects.all()
    serializer_class = StreetNetworkSerializer
