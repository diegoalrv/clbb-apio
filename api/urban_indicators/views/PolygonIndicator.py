from rest_framework import viewsets
from urban_indicators.models.PolygonIndicator import PolygonIndicator
from urban_indicators.serializers.PolygonIndicator import PolygonIndicatorSerializer

class PolygonIndicatorViewSet(viewsets.ModelViewSet):
    queryset = PolygonIndicator.objects.all()
    serializer_class = PolygonIndicatorSerializer