from django.contrib import admin

from backend.models.LandUse import LandUse
admin.site.register(LandUse)

from backend.models.DiscreteDistribution import DiscreteDistribution
admin.site.register(DiscreteDistribution)

from backend.models.AreaOfInterest import AreaOfInterest
admin.site.register(AreaOfInterest)

from backend.models.RoadNetwork import RoadNetwork, Street, Node
admin.site.register(RoadNetwork)
admin.site.register(Street)
admin.site.register(Node)

from backend.models.Amenity import Amenity
admin.site.register(Amenity)
