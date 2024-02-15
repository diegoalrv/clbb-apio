# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from backend.views.LandUse import LandUseViewSet
router.register(r'landuse', LandUseViewSet)

from backend.views.DiscreteDistribution import DiscreteDistributionViewSet
router.register(r'discretedistribution', DiscreteDistributionViewSet)

from backend.views.AreaOfInterest import AreaOfInterestViewSet
router.register(r'areaofinterest', AreaOfInterestViewSet)

from backend.views.StreetNetwork import StreetNetworkViewSet
router.register(r'streetnetwork', StreetNetworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
