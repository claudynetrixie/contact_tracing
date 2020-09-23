from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
# admin.site.register(Log1)
admin.site.register(Building)
admin.site.register(Room)
# admin.site.register(Stat)
admin.site.register(Log)
admin.site.register(InfectionReport)
admin.site.register(LocationLog)
