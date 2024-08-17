from django.contrib import admin
from .models import Alert, Irregularity, Segment, Jams, AlertRecord, IrregularityRecord, JamRecord
# Register your models here.

admin.site.register(Alert)
admin.site.register(Irregularity)
admin.site.register(Segment)
admin.site.register(Jams)
admin.site.register(AlertRecord)
admin.site.register(IrregularityRecord)
admin.site.register(JamRecord)