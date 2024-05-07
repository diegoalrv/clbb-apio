from django.contrib.gis.db import models
from interactive.models.Scenario import Scenario

class Plate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code_number = models.CharField(max_length=50, null=True, blank=True)
    code_type = models.CharField(max_length=50, null=True, blank=True)
    geometry = models.PolygonField(null=True)

    def __str__(self):
        return self.name
    
class PlateScenario(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=255, editable=False, blank=True)

    class Meta:
        unique_together = ('plate', 'scenario')

    def save(self, *args, **kwargs):
        # Generar el nombre antes de guardar el objeto
        if not self.name:  # Solo actualiza el nombre si no existe, o según sea necesario
            self.name = f'{self.plate.id} {self.scenario.name}'
        super(PlateScenario, self).save(*args, **kwargs)