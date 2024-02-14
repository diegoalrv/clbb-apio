# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views.LandUse import LandUseViewSet

router = DefaultRouter()
router.register(r'landuse', LandUseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


from backend.views.DiscreteDistribution import DiscreteDistributionViewSet
router.register(r'discretedistribution', DiscreteDistributionViewSet)
