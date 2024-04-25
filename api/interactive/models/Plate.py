from django.contrib.gis.db import models
from interactive.models.Scenario import Scenario

class Plate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code_number = models.CharField(max_length=50, null=True, blank=True)
    code_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    
class PlateScenario(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    class Meta:
        unique_together = ('plate', 'scenario')