from django.contrib import admin
from contacts.models import *

# Register your models here.



@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'order',
    ]
    list_editable = [
        'order', 
    ]
