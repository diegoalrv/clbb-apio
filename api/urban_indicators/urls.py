# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from urban_indicators.views.PointIndicator import PointIndicatorViewSet
router.register(r'pointindicator', PointIndicatorViewSet)

from urban_indicators.views.LineIndicator import LineIndicatorViewSet
router.register(r'lineindicator', LineIndicatorViewSet)

from urban_indicators.views.PolygonIndicator import PolygonIndicatorViewSet
router.register(r'polygonindicator', PolygonIndicatorViewSet)

from urban_indicators.views.NumericIndicator import NumericIndicatorViewSet
router.register(r'numericindicator', NumericIndicatorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]