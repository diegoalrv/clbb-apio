# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views.LandUse import LandUseViewSet
from backend.views.Plate import PlateViewSet
from backend.views.Scenario import ScenarioViewSet

router = DefaultRouter()
router.register(r'scenario', ScenarioViewSet)
router.register(r'plate', PlateViewSet)
router.register(r'landuse', LandUseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

