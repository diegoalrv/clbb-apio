from django.contrib.gis.db import models

class DiscreteDistribution(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dist_type = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    level = models.IntegerField()
    geometry = models.PolygonField()

    def __str__(self):
        return self.name