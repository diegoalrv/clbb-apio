from rest_framework import viewsets
from urban_indicators.models.NumericIndicator import NumericIndicator
from urban_indicators.serializers.NumericIndicator import NumericIndicatorSerializer

class NumericIndicatorViewSet(viewsets.ModelViewSet):
    queryset = NumericIndicator.objects.all()
    serializer_class = NumericIndicatorSerializer