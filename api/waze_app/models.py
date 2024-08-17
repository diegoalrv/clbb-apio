from django.contrib.gis.db import models

# Alerts Model
class Alert(models.Model):
    pub_millis = models.BigIntegerField(null=True, blank=True)
    uuid = models.CharField(max_length=255, unique=True, primary_key=True)
    magvar = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    subtype = models.CharField(max_length=100, null=True, blank=True)
    report_description = models.TextField(null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    road_type = models.IntegerField(null=True, blank=True)
    report_rating = models.IntegerField(null=True, blank=True)
    reliability = models.IntegerField(null=True, blank=True)
    confidence = models.IntegerField(null=True, blank=True)
    report_by_municipality_user = models.BooleanField(null=True, blank=True)
    n_thumbs_up = models.IntegerField(null=True, blank=True)
    geometry = models.PointField(null=True, blank=True)  # Use PointField for geographic points

    timestamp = models.DateTimeField(null=True, blank=True)
    timezone = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.uuid

# Irregularities Model
class Irregularity(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    detection_date = models.DateTimeField(null=True, blank=True)
    detection_date_millis = models.BigIntegerField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    update_date_millis = models.BigIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    timezone = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    regular_speed = models.FloatField(null=True, blank=True)
    delay_seconds = models.IntegerField(null=True, blank=True)
    seconds = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    trend = models.FloatField(null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    severity = models.IntegerField(null=True, blank=True)
    jam_level = models.IntegerField(null=True, blank=True)
    drivers_count = models.IntegerField(null=True, blank=True)
    alerts_count = models.IntegerField(null=True, blank=True)
    n_images = models.IntegerField(null=True, blank=True)
    geometry = models.LineStringField(null=True, blank=True)  # LineStringField for line geometries (representing a street segment)
    alerts = models.ManyToManyField(Alert)

    def __str__(self):
        return f"Irregularity {self.id}"

# Segment Model
class Segment(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    from_node = models.IntegerField()
    to_node = models.IntegerField()
    is_forward = models.BooleanField()

    def __str__(self):
        return f"Segment {self.id}"

# Jams Model
class Jams(models.Model):
    pub_millis = models.BigIntegerField(null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    geometry = models.LineStringField(null=True, blank=True)  # Use LineStringField for the route line
    speed = models.FloatField(null=True, blank=True)
    speed_kmh = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    delay = models.BigIntegerField(null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    street_id = models.BigIntegerField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    road_type = models.IntegerField(null=True, blank=True)
    start_node = models.CharField(max_length=255, null=True, blank=True)
    end_node = models.CharField(max_length=255, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    uuid = models.BigIntegerField(unique=True, primary_key=True)
    turn_line = models.LineStringField(null=True, blank=True)  # LineString for turnLine geometry
    turn_type = models.CharField(max_length=100, null=True, blank=True)
    blocking_alert_uuid = models.CharField(max_length=255, null=True, blank=True)
    segments = models.ManyToManyField(Segment)

    timestamp = models.DateTimeField(null=True, blank=True)
    timezone = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.uuid}'
    
class JamRecord(models.Model):
    id = models.AutoField(primary_key=True)
    jam = models.ForeignKey(Jams, on_delete=models.CASCADE)
    sample_timestamp = models.DateTimeField()
    def __str__(self):
        return f'{self.jam.uuid} - {self.sample_timestamp}'

class AlertRecord(models.Model):
    id = models.AutoField(primary_key=True)
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    sample_timestamp = models.DateTimeField()
    def __str__(self):
        return f'{self.alert.uuid} - {self.sample_timestamp}'

class IrregularityRecord(models.Model):
    id = models.AutoField(primary_key=True)
    irregularity = models.ForeignKey(Irregularity, on_delete=models.CASCADE)
    sample_timestamp = models.DateTimeField()
    def __str__(self):
        return f'{self.irregularity.id} - {self.sample_timestamp}'
