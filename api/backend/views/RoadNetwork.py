from rest_framework import viewsets
from api.backend.models.RoadNetwork import StreetNetwork, Street, Node
from api.backend.serializers.RoadNetwork import RoadNetworkSerializer, StreetSerializer, NodeSerializer

class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    
class RoadNetworkViewSet(viewsets.ModelViewSet):
    queryset = StreetNetwork.objects.all()
    serializer_class = RoadNetworkSerializer
