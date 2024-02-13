from backend.models.LandUse import LandUse
from backend.models.Scenario import Scenario
from backend.models.Plate import Plate

# Eliminar todos los registros del modelo LandUses
# LandUse.objects.all().delete()
Scenario.objects.all().delete()
Plate.objects.all().delete()

print("Registros de LandUses eliminados correctamente.")
