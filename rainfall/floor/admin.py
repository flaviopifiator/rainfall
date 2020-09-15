from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from . import models


@admin.register(models.Floor, site=admin.site)
class FloorAdmin(LeafletGeoAdmin):
    list_display = ['name', 'hectares']


@admin.register(models.Rain, site=admin.site)
class RainAdmin(admin.ModelAdmin):
    list_display = ['floor', 'precipitation', 'date']
    list_filter = ['floor__name']
