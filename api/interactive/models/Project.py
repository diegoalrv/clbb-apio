from django.contrib.gis.db import models
from interactive.models.Plate import Plate
from backend.models.AreaOfInterest import AreaOfInterest
from backend.models.DiscreteDistribution import DiscreteDistribution

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    status = models.CharField(max_length=50, choices=[
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('pending', 'Pending')
    ], default='active')
    plates = models.ManyToManyField(Plate, blank=True)
    discrete_distributions = models.ManyToManyField(DiscreteDistribution, blank=True)
    area_of_interest = models.ForeignKey(AreaOfInterest, related_name='projects', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name