from rest_framework import viewsets, status
from interactive.models.Scenario import Scenario
from interactive.serializers.Scenario import ScenarioSerializer
from interactive.utils.config import data_mapping
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

    @action(detail=True, methods=['get'], url_path='data/(?P<data_type>[^/.]+)')
    def get_data(self, request, pk=None, data_type=None):
        """
        This custom action returns data associated with a specific scenario based on the data type.
        """
        if data_type in data_mapping:
            relation_type = data_mapping[data_type].get('relation_type', 'many_to_many')

            model = data_mapping[data_type]['model']
            serializer_class = data_mapping[data_type]['serializer']
            
            scenario = get_object_or_404(Scenario, pk=pk)
            if relation_type == 'many_to_many':
                data = getattr(scenario, data_type).all()
            elif relation_type == 'foreign_key' or relation_type == 'one_to_one':
                data = getattr(scenario, data_type)
                if not data:
                    return Response({"error": "No data found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"error": "Invalid relation type"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            serializer = serializer_class(data, many=(relation_type == 'many_to_many'))
            return Response(serializer.data)
        else:
            return Response({"error": "Invalid data type"}, status=status.HTTP_400_BAD_REQUEST)