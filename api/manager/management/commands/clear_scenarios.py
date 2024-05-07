from django.core.management.base import BaseCommand
from django.db import transaction
from interactive.models.Scenario import Scenario  # Asegúrate de importar correctamente tu modelo Scenario

class Command(BaseCommand):
    help = 'Deletes all scenarios from the database'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Deleting all scenarios safely within a transaction
            self.stdout.write(self.style.WARNING('Deleting all scenarios...'))
            count, _ = Scenario.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Scenarios deleted successfully! {count} records removed.'))
