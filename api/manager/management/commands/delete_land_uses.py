from backend.models.LandUse import LandUse
from interactive.models.Scenario import Scenario
from interactive.models.Plate import Plate

# Eliminar todos los registros del modelo LandUses
# LandUse.objects.all().delete()
Scenario.objects.all().delete()
Plate.objects.all().delete()

print("Registros de LandUses eliminados correctamente.")
