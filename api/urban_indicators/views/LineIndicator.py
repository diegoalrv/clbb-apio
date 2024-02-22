from rest_framework import viewsets
from urban_indicators.models.LineIndicator import LineIndicator
from urban_indicators.serializers.LineIndicator import LineIndicatorSerializer

class LineIndicatorViewSet(viewsets.ModelViewSet):
    queryset = LineIndicator.objects.all()
    serializer_class = LineIndicatorSerializer