from django.contrib.gis.db import models
from interactive.models.Plate import Plate
from backend.models.AreaOfInterest import AreaOfInterest
from backend.models.DiscreteDistribution import DiscreteDistribution

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    plates = models.ManyToManyField(Plate, blank=True)
    discrete_distributions = models.ManyToManyField(DiscreteDistribution, blank=True)
    area_of_interest = models.ForeignKey(AreaOfInterest, related_name='projects', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
    def generate_identifier(self):
        # Lista para almacenar los identificadores de las placas asociadas al proyecto
        plate_identifiers = []
        
        # Iterar sobre las placas asociadas al proyecto
        for plate in self.plates.all():
            # Construir el identificador de la placa
            plate_identifier = f"{plate.id}-{plate.scenario.id}" if plate.scenario else f"{plate.id}-"
            plate_identifiers.append(plate_identifier)
        
        # Unir los identificadores de las placas en un único identificador para el proyecto
        return '-'.join(plate_identifiers)