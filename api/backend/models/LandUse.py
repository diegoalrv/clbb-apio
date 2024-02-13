from django.contrib.gis.db import models

class LandUse(models.Model):
    id = models.AutoField(primary_key=True)
    uso = models.CharField(max_length=100)
    area_predio = models.FloatField()
    geometry = models.PolygonField()

    def __str__(self):
        return f"{self.id}: {self.uso}"