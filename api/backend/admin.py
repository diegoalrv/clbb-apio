from django.contrib import admin
from backend.models.LandUse import LandUse

# Register your models here.

admin.site.register(LandUse)


from backend.models.DiscreteDistribution import DiscreteDistribution
admin.site.register(DiscreteDistribution)
