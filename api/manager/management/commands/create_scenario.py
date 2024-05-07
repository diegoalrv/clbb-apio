from django.core.management.base import BaseCommand
from backend.models.Amenity import Amenity
from backend.models.LandUse import LandUse
from backend.models.GreenArea import GreenArea
from backend.models.RoadNetwork import RoadNetwork
from interactive.models.Scenario import Scenario

class Command(BaseCommand):
    help = 'Crea un escenario con todos los datos actuales de la base'

    def add_arguments(self, parser):
        # Añadir un argumento de línea de comando para el nombre del escenario
        parser.add_argument('scenario_name', type=str, help='Nombre del escenario a crear o actualizar')

    def handle(self, *args, **kwargs):
        scenario_name = kwargs['scenario_name']  # Obtener el nombre del escenario desde los argumentos

        amenities = Amenity.objects.all()
        land_uses = LandUse.objects.all()
        green_areas = GreenArea.objects.all()
        road_network = RoadNetwork.objects.first()

        scenario, created = Scenario.objects.get_or_create(
            name=scenario_name,
            defaults={
                'road_network': road_network
            }
        )

        # Si el escenario ya existe, sobrescribe sus datos
        if not created:
            self.stdout.write(self.style.WARNING(f'Updating existing scenario: {scenario_name}'))
            scenario.amenities.clear()
            scenario.land_uses.clear()
            scenario.green_areas.clear()

        scenario.amenities.set(amenities)
        scenario.land_uses.set(land_uses)
        scenario.green_areas.set(green_areas)

        self.stdout.write(self.style.SUCCESS(f'Scenario "{scenario_name}" has been created or updated successfully!'))
