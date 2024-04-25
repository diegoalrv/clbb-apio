from django.contrib import admin
from interactive.models.Plate import Plate, PlateScenario
from interactive.models.Scenario import Scenario

# Register your models here.
admin.site.register(Scenario)
admin.site.register(Plate)
admin.site.register(PlateScenario)

from interactive.models.Project import Project
admin.site.register(Project)