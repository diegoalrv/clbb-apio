# forms.py
from django import forms
from django.forms import ModelForm
from interactive.models.Plate import Plate
from interactive.models.Project import Project

class PlateForm(ModelForm):
    class Meta:
        model = Plate
        fields = ['name', 'code_number', 'code_type', 'geometry']

class AssociatePlateForm(forms.Form):
    plate = forms.ModelChoiceField(queryset=Plate.objects.all(), required=True)
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=True)
    upload_geojson = forms.FileField(required=False, label="Upload GeoJSON")

    action_choice = forms.ChoiceField(
        choices=[('select', 'Select Existing Plate'), ('upload', 'Upload GeoJSON')],
        widget=forms.RadioSelect,
        label="Action"
    )