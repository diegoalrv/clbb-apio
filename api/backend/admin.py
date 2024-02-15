from django.contrib import admin

from backend.models.LandUse import LandUse
admin.site.register(LandUse)

from backend.models.DiscreteDistribution import DiscreteDistribution
admin.site.register(DiscreteDistribution)

from backend.models.AreaOfInterest import AreaOfInterest
admin.site.register(AreaOfInterest)



from backend.models.StreetNetwork import StreetNetwork
admin.site.register(StreetNetwork)
