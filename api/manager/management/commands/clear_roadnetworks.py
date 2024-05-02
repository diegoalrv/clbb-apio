from django.core.management.base import BaseCommand
from django.db import transaction
from backend.models.RoadNetwork import Street, Node, RoadNetwork

class Command(BaseCommand):
    help = 'Deletes all streets, nodes, and road networks from the database'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Deleting all objects safely within a transaction
            self.stdout.write(self.style.WARNING('Deleting all streets...'))
            Street.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Streets deleted successfully!'))

            self.stdout.write(self.style.WARNING('Deleting all nodes...'))
            Node.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Nodes deleted successfully!'))

            self.stdout.write(self.style.WARNING('Deleting all road networks...'))
            RoadNetwork.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Road networks deleted successfully!'))

            self.stdout.write(self.style.SUCCESS('All data has been deleted.'))
