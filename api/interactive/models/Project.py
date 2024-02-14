from django.contrib.gis.db import models
from interactive.models.Plate import Plate

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    plates = models.ManyToManyField(Plate, blank=True)
    geometry = models.PolygonField()

    def __str__(self):
        return self.name