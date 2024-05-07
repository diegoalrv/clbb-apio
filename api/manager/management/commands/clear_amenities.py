from django.core.management.base import BaseCommand
from django.db import transaction
from backend.models.Amenity import Amenity

class Command(BaseCommand):
    help = 'Deletes all streets, nodes, and road networks from the database'

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Deleting all amenities...'))
            Amenity.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Amenities deleted successfully!'))
