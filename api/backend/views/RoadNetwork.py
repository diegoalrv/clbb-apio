from rest_framework import viewsets
from backend.models.RoadNetwork import RoadNetwork, Street, Node
from backend.serializers.RoadNetwork import RoadNetworkSerializer, StreetSerializer, NodeSerializer

class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    
class RoadNetworkViewSet(viewsets.ModelViewSet):
    queryset = RoadNetwork.objects.all()
    serializer_class = RoadNetworkSerializer
