from interactive.models.Scenario import Scenario
from backend.models import Amenity, GreenArea, LandUse, RoadNetwork, DiscreteDistribution
from backend.serializers import Amenity, GreenArea, LandUse, RoadNetwork, DiscreteDistribution

# Diccionario que mapea los tipos de datos a modelos y serializadores
data_mapping = {
    'amenities': {
        'model': Scenario.amenities.through,  # Asumiendo una relación ManyToMany
        'serializer': Amenity.AmenitySerializer,
        'relation_type': 'many_to_many',
    },
    'green_areas': {
        'model': Scenario.green_areas.through,
        'serializer': GreenArea.GreenAreaSerializer,
        'relation_type': 'many_to_many',
    },
    'land_uses': {
        'model': Scenario.land_uses.through,
        'serializer': LandUse.LandUseSerializer,
        'relation_type': 'many_to_many',
    },
    'roadnetwork': {
        'model': Scenario.road_network,
        'serializer': RoadNetwork.RoadNetworkSerializer,
        'relation_type': 'foreign_key',
    },
}
