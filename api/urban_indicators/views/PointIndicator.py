from rest_framework import viewsets
from urban_indicators.models.PointIndicator import PointIndicator
from urban_indicators.serializers.PointIndicator import PointIndicatorSerializer

class PointIndicatorViewSet(viewsets.ModelViewSet):
    queryset = PointIndicator.objects.all()
    serializer_class = PointIndicatorSerializer