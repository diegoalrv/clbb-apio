# urls.py
from rest_framework.routers import DefaultRouter
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

from backend.views.GreenArea import GreenAreaViewSet
router.register(r'greenarea', GreenAreaViewSet)

from backend.views.Globals import UploadFileView, success_view

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload'),
    path('success/', success_view, name='success'),
    path('', include(router.urls)),
]