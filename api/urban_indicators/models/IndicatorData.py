from django.contrib.gis.db import models

class IndicatorData(models.Model):
    id = models.AutoField(primary_key=True)
    indicator_name = models.CharField(max_length=100)
    indicator_hash = models.CharField(max_length=100, unique=True)
    is_geo = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.indicator_name} - {self.indicator_hash[:8]}'