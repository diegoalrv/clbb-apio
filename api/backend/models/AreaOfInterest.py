from django.contrib.gis.db import models

class AreaOfInterest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    geo_field = models.PolygonField()

    def __str__(self):
        return self.name