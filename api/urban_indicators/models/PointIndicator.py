from django.contrib.gis.db import models

class PointIndicator(models.Model):
    id = models.AutoField(primary_key=True)
    indicator_name = models.CharField(max_length=100)
    indicator_hash = models.CharField(max_length=100)
    extra_properties = models.JSONField(blank=True, null=True)
    geo_field = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.name