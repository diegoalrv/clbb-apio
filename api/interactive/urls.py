# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from interactive.views.Plate import PlateViewSet, PlateScenarioViewSet
from interactive.views.Scenario import ScenarioViewSet
router.register(r'scenario', ScenarioViewSet)
router.register(r'plate', PlateViewSet)
router.register(r'platescenario', PlateScenarioViewSet)

from interactive.views.Project import ProjectViewSet
router.register(r'project', ProjectViewSet)

urlpatterns = [    
    path('', include(router.urls)),
    path('project/create/', ProjectViewSet.as_view({'post': 'create_project'}), name='project-create'),
    path('project/form-plate/', ProjectViewSet.as_view({'get': 'plate_form'}), name='project-form-plate'),
    path('plate/create/', PlateViewSet.as_view({'post': 'create_plate'}), name='plate-create'),
    path('plate/associate/', PlateViewSet.as_view({'post': 'associate_plate'}), name='plate-associate'),
]