from django.contrib.gis.db import models

class LandUse(models.Model):
    id = models.AutoField(primary_key=True)
    use = models.CharField(max_length=100)
    area = models.FloatField()
    geo_field = models.PolygonField()

    def __str__(self):
        return f"{self.id}: {self.use}"