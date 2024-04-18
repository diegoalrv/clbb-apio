from django.contrib.gis.db import models

class GreenArea(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    category = models.CharField(max_length=500, null=True, blank=True)
    subcategory = models.CharField(max_length=500, null=True, blank=True)
    tags = models.JSONField(blank=True, null=True)
    geometry = models.PolygonField()

    def calculate_area(self):
        return self.geometry.area

    area_sqm = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.area_sqm = self.calculate_area()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name