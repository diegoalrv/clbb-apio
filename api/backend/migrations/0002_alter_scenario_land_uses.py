# Generated by Django 3.2.24 on 2024-02-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenario',
            name='land_uses',
            field=models.ManyToManyField(blank=True, to='backend.LandUse'),
        ),
    ]
