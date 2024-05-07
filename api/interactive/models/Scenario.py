from django.contrib.gis.db import models
from backend.models.LandUse import LandUse
from backend.models.RoadNetwork import RoadNetwork
from backend.models.Amenity import Amenity
from backend.models.GreenArea import GreenArea

class Scenario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    land_uses = models.ManyToManyField(LandUse, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    green_areas = models.ManyToManyField(GreenArea, blank=True)
    road_network = models.ForeignKey(RoadNetwork, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name