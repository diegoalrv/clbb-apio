from rest_framework import viewsets
from backend.models.DiscreteDistribution import DiscreteDistribution
from backend.serializers.DiscreteDistribution import DiscreteDistributionSerializer

class DiscreteDistributionViewSet(viewsets.ModelViewSet):
    queryset = DiscreteDistribution.objects.all()
    serializer_class = DiscreteDistributionSerializer