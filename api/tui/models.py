# Create your models here. 
from backend.models.Plate import Plate
from django.contrib.gis.db import models

class Table(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    plates = models.ManyToManyField(Plate, null=True, blank=True)
    polygon = models.PolygonField()

    def __str__(self):
        return self.name