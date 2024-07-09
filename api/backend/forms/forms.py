from django import forms

MODEL_CHOICES = [
    ('Amenity', 'Amenity'),
    ('AreaOfInterest', 'AreaOfInterest'),
    ('DiscreteDistribution', 'DiscreteDistribution'),
    ('GreenArea', 'GreenArea'),
    ('LandUse', 'LandUse'),
]

class UploadFileForm(forms.Form):
    file = forms.FileField()
    model_type = forms.ChoiceField(choices=MODEL_CHOICES)
