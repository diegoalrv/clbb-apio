from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlertViewSet, IrregularityViewSet, JamsViewSet, SegmentViewSet, AlertRecordViewSet, IrregularityRecordViewSet, JamRecordViewSet

router = DefaultRouter()
router.register(r'alerts', AlertViewSet)
router.register(r'irregularities', IrregularityViewSet)
router.register(r'jams', JamsViewSet)
router.register(r'segments', SegmentViewSet)
router.register(r'alertrecords', AlertRecordViewSet)
router.register(r'irregularityrecords', IrregularityRecordViewSet)
router.register(r'jamrecords', JamRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]