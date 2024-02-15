# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views.LandUse import LandUseViewSet

router = DefaultRouter()
router.register(r'landuse', LandUseViewSet)

from backend.views.DiscreteDistribution import DiscreteDistributionViewSet
router.register(r'discretedistribution', DiscreteDistributionViewSet)

from backend.views.AreaOfInterest import AreaOfInterestViewSet
router.register(r'areaofinterest', AreaOfInterestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]