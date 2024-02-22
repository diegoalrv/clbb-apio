from django.contrib.gis.db import models

class LineIndicator(models.Model):
    id = models.AutoField(primary_key=True)
    indicator_name = models.CharField(max_length=100)
    indicator_hash = models.CharField(max_length=100)
    extra_properties = models.JSONField(blank=True, null=True)
    geo_field = models.LineStringField(null=True, blank=True)

    def __str__(self):
        return self.name