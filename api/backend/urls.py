# urls.py
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from django.urls import path, include

router = DefaultRouter()

from backend.views.LandUse import LandUseViewSet
router.register(r'landuse', LandUseViewSet)

from backend.views.DiscreteDistribution import DiscreteDistributionViewSet
router.register(r'discretedistribution', DiscreteDistributionViewSet)

from backend.views.AreaOfInterest import AreaOfInterestViewSet
router.register(r'areaofinterest', AreaOfInterestViewSet)

from backend.views.RoadNetwork import RoadNetworkViewSet, StreetViewSet, NodeViewSet

router.register(r'roadnetwork', RoadNetworkViewSet)
router.register(r'street', StreetViewSet, basename='street')
router.register(r'node', NodeViewSet, basename='node')

from backend.views.Amenity import AmenityViewSet
router.register(r'amenity', AmenityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]