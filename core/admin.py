from django.contrib import admin
from .models import Faction, FactionDescription, Metro, Station, Character

admin.site.register(Faction)
admin.site.register(FactionDescription)
admin.site.register(Metro)
admin.site.register(Station)
admin.site.register(Character)