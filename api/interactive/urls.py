# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from interactive.views.Plate import PlateViewSet
from interactive.views.Scenario import ScenarioViewSet

router = DefaultRouter()

router.register(r'scenario', ScenarioViewSet)
router.register(r'plate', PlateViewSet)

from interactive.views.Project import ProjectViewSet
router.register(r'project', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]