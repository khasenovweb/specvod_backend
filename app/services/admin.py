from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from services.models import *



@admin.register(Service)
class ServiceAdmin(MPTTModelAdmin):
    """ Услуга """
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = [
        "hero_numbers",
        "preims",
        "sertificates",
        "promotions",
        "properties",
        "price_positions",
        "methods",
        "technics",
        "etaps",
    ]


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """ Характеристика """
    pass

