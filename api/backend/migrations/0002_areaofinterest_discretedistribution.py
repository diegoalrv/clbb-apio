# Generated by Django 3.2.24 on 2024-02-15 03:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaOfInterest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='DiscreteDistribution',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dist_type', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]
