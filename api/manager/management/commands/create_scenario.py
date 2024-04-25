from django.core.management.base import BaseCommand
from backend.models.Amenity import Amenity
from backend.models.LandUse import LandUse
from backend.models.GreenArea import GreenArea
from backend.models.RoadNetwork import RoadNetwork
from interactive.models.Scenario import Scenario

class Command(BaseCommand):
    help = 'Crea un escenario con todos los datos actuales de la base'

    def handle(self, *args, **kwargs):
        amenities = Amenity.objects.all()
        land_uses = LandUse.objects.all()
        green_areas = GreenArea.objects.all()
        street_network = RoadNetwork.objects.first()

        scenario, created = Scenario.objects.get_or_create(
            name='actual',
            defaults={
                'street_network': street_network
            }
        )

        if created:
            scenario.amenities.set(amenities)
            scenario.land_uses.set(land_uses)
            scenario.green_areas.set(green_areas)
            self.stdout.write(self.style.SUCCESS('Scenario "actual" creado exitosamente.'))
        else:
            self.stdout.write(self.style.WARNING('Scenario "actual" ya existe.'))
