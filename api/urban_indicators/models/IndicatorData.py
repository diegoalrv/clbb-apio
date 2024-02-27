from django.contrib.gis.db import models

class IndicatorData(models.Model):
    id = models.AutoField(primary_key=True)
    indicator_name = models.CharField(max_length=100)
    indicator_hash = models.CharField(max_length=100)
    table_name = models.CharField(max_length=100)

    def __str__(self):
        return self.indicator_hash