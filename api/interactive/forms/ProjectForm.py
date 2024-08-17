# forms.py
from django import forms
from django.contrib.gis.geos import GEOSGeometry
from interactive.models.Project import Project
from backend.models.AreaOfInterest import AreaOfInterest

class ProjectForm(forms.ModelForm):
    select_area_of_interest = forms.ModelChoiceField(
        queryset=AreaOfInterest.objects.all(),
        required=False,
        label="Select Area of Interest"
    )
    upload_geojson = forms.FileField(required=False, label="Upload GeoJSON")

    class Meta:
        model = Project
        fields = ['name', 'description', 'status', 'select_area_of_interest', 'upload_geojson']