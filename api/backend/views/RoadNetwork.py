from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from backend.models.RoadNetwork import RoadNetwork, Street, Node
from backend.serializers.RoadNetwork import RoadNetworkSerializer, StreetSerializer, NodeSerializer

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Obtener parámetros de consulta
        lat = self.request.query_params.get('lat')
        lon = self.request.query_params.get('lon')
        distance = self.request.query_params.get('distance', 50)
        
        if lat is not None and lon is not None and distance is not None:
            # Crear un punto a partir de las coordenadas proporcionadas
            point = Point(float(lon), float(lat), srid=4326)  # Assumiendo EPSG:4326
            
            # Filtrar los nodos basados en la distancia desde el punto dado
            queryset = queryset.annotate(distance_to_point=Distance('geo_field', point)).filter(distance_to_point__lte=float(distance))
        
        return queryset
    
class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Obtener parámetros de consulta
        node_ids = self.request.query_params.get('node_ids')
        
        if node_ids:
            # Convertir los IDs de nodo a una lista de enteros
            node_ids_list = [int(id_str) for id_str in node_ids.split(',')]
            
            # Filtrar las calles basadas en los IDs de nodo proporcionados
            queryset = queryset.filter(source_id__in=node_ids_list) | queryset.filter(destination_id__in=node_ids_list)
        
        return queryset
    
class RoadNetworkViewSet(viewsets.ModelViewSet):
    queryset = RoadNetwork.objects.all()
    serializer_class = RoadNetworkSerializer

    @action(detail=True, methods=['get'])
    def streets(self, request, pk=None):
        try:
            # Obtener el objeto RoadNetwork por su clave primaria (pk)
            road_network = self.get_object()
            
            # Obtener todas las calles asociadas a la red vial
            streets = road_network.streets.all()
            
            # Serializar los datos de las calles
            serializer = StreetSerializer(streets, many=True)
            
            # Devolver la respuesta HTTP con los datos serializados
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RoadNetwork.DoesNotExist:
            # Manejar el caso donde la red vial no existe
            return Response({"error": f"No se encontró una red vial con el ID {pk}."},
                            status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True, methods=['get'])
    def nodes(self, request, pk=None):
        try:
            # Obtener el objeto RoadNetwork por su clave primaria (pk)
            road_network = self.get_object()
            
            # Obtener todas las calles asociadas a la red vial
            streets = road_network.streets.all()

            # Inicializar un conjunto para almacenar los nodos únicos
            unique_nodes = set()
            
            # Iterar sobre todas las calles y agregar los nodos únicos al conjunto
            for street in streets:
                unique_nodes.add(street.source)
                unique_nodes.add(street.destination)

            # Serializar los datos de los nodos únicos
            serializer = NodeSerializer(list(unique_nodes), many=True)
            
            # Devolver la respuesta HTTP con los datos serializados
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RoadNetwork.DoesNotExist:
            # Manejar el caso donde la red vial no existe
            return Response({"error": f"No se encontró una red vial con el ID {pk}."},
                            status=status.HTTP_404_NOT_FOUND)