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


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'fio',
        'order',
    ]
    list_editable = [
        'order', 
    ]


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'order',
    ]
    list_editable = [
        'order', 
    ]


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = [
        'adress',
        'phone_1',
        'phone_2',
    ]
