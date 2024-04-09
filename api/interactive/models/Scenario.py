from django.contrib.gis.db import models
from backend.models.LandUse import LandUse
from backend.models.RoadNetwork import RoadNetwork

class Scenario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    land_uses = models.ManyToManyField(LandUse, blank=True)
    street_network = models.ForeignKey(RoadNetwork, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name