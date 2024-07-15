# forms.py
from django import forms
from interactive.models.Project import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']  # Asegúrate de incluir los campos que sean necesarios
