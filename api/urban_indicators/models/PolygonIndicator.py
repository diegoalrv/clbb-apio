from django.contrib.gis.db import models

class PolygonIndicator(models.Model):
    id = models.AutoField(primary_key=True)
    indicator_name = models.CharField(max_length=100)
    indicator_hash = models.CharField(max_length=100)
    value = models.FloatField(null=True, blank=True)
    extra_properties = models.JSONField(blank=True, null=True)
    geo_field = models.PolygonField(blank=True, null=True)
    
    def __str__(self):
        return self.indicator_hash