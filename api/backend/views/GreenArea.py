from rest_framework import viewsets
from api.backend.models.GreenArea import GreenArea
from backend.serializers.GreenArea import GreenAreaSerializer

class GreenAreaViewSet(viewsets.ModelViewSet):
    queryset = GreenArea.objects.all()
    serializer_class = GreenAreaSerializer