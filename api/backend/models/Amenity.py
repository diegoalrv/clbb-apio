from django.contrib.gis.db import models

class Amenity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    category = models.CharField(max_length=500, null=True, blank=True)
    subcategory = models.CharField(max_length=500, null=True, blank=True)
    tags = models.JSONField(blank=True, null=True)
    geo_field = models.PointField()

    def __str__(self):
        return self.name