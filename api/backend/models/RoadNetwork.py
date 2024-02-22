from django.contrib.gis.db import models

class Street(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    osm_id = models.BigIntegerField(default=0)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='source_of_street')
    destination = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='destination_of_street')
    geo_field = models.LineStringField()
    tags = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'Edge {self.osm_id} : {self.source.osm_id} --> {self.destination.osm_id}'

class Node(models.Model):
    osm_id = models.BigIntegerField(primary_key=True)
    geo_field = models.PointField()
    tags = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Node {self.osm_id}"

class RoadNetwork(models.Model):
    name = models.CharField(max_length=100)
    streets = models.ManyToManyField(Street)
    mode = models.CharField(max_length=100)
    h5_file = models.FileField(upload_to='h5_files/', blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name