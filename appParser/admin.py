from django.contrib import admin
from .models import Status, LocationType, Location, Frequency, Config, ConfigLog

# Register your models here.

admin.site.register(Status)
admin.site.register(LocationType)
admin.site.register(Location)
admin.site.register(Frequency)
admin.site.register(Config)
admin.site.register(ConfigLog)