from django.contrib import admin
from backend.models.LandUse import LandUse
from backend.models.Plate import Plate
from backend.models.Scenario import Scenario

# Register your models here.

admin.site.register(Scenario)
admin.site.register(Plate)
admin.site.register(LandUse)

