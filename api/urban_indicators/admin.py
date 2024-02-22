from django.contrib import admin

# Register your models here.

from urban_indicators.models.PointIndicator import PointIndicator
admin.site.register(PointIndicator)

from urban_indicators.models.LineIndicator import LineIndicator
admin.site.register(LineIndicator)

from urban_indicators.models.PolygonIndicator import PolygonIndicator
admin.site.register(PolygonIndicator)

from urban_indicators.models.NumericIndicator import NumericIndicator
admin.site.register(NumericIndicator)
