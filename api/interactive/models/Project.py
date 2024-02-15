from django.contrib.gis.db import models
from interactive.models.Plate import Plate
from backend.models.AreaOfInterest import AreaOfInterest
from backend.models.DiscreteDistribution import DiscreteDistribution

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    plates = models.ManyToManyField(Plate, blank=True)
    area_of_interest = models.ForeignKey(AreaOfInterest, related_name='projects', null=True, blank=True, on_delete=models.SET_NULL)
    discrete_distributions = models.ManyToManyField(DiscreteDistribution, blank=True)

    geometry = models.PolygonField()

    def __str__(self):
        return self.name