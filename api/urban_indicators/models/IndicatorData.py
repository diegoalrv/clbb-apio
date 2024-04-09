from django.contrib.gis.db import models
import json

class IndicatorData(models.Model):
    id = models.AutoField(primary_key=True)
    indicator_name = models.CharField(max_length=100)
    indicator_hash = models.CharField(max_length=100, unique=True)
    params = models.JSONField(default=dict, blank=True, null=True)
    is_geo = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.indicator_name} - {self.indicator_hash[:8]}'